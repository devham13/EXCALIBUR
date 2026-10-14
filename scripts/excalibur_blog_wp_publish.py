#!/usr/bin/env python3
"""Publish one Excalibur blog article to WordPress (FTP bootstrap)."""
from __future__ import annotations

import argparse
import base64
import ftplib
import io
import json
import os
import sys
import urllib.request
from pathlib import Path
from typing import Callable

from asset_download import download_url_bytes
from excalibur_repo_paths import repo_relative
from image_validate import sniff_image_format, validate_image_file


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_env(root: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    for name in ("memory/site.env.local", "memory/site.env.local.example"):
        p = root / name
        if p.is_file():
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip()
            break
    for key, value in os.environ.items():
        if key.startswith(("FTP_", "SFTP_", "SSH_", "REMOTE_", "PUBLIC_", "EXCALIBUR_", "WP_")):
            env.setdefault(key, value)
    if not env.get("FTP_PASS") and os.environ.get("FTP_PASSWORD"):
        env["FTP_PASS"] = os.environ["FTP_PASSWORD"]
    if not env.get("FTP_HOST") and not (os.environ.get("SFTP_HOST") or os.environ.get("SSH_HOST")):
        raise FileNotFoundError("site.env.local or Cloud FTP/SSH secrets required under memory/")
    return env


def cover_url_from_registry(registry_path: Path) -> str:
    if not registry_path.is_file():
        return ""
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    for key in ("transparent_url", "remote_packaged_url", "packaged_url", "attachment_url", "url", "cover_url", "image_url"):
        value = str(registry.get(key) or "").strip()
        if value.startswith(("http://", "https://")):
            return value
    return ""


def normalize_cover_png(cover_path: Path, registry_path: Path, root: Path) -> dict[str, object]:
    evidence: dict[str, object] = {
        "path": repo_relative(cover_path, root),
        "source": "existing_file",
        "decode_verified": False,
    }
    errors = validate_image_file(cover_path) if cover_path.is_file() else [f"missing cover file: {cover_path}"]

    if errors:
        remote_url = cover_url_from_registry(registry_path)
        if not remote_url:
            raise RuntimeError("; ".join(errors) + "; no remote cover URL in cover-registry.json")
        data, remote_evidence = download_url_bytes(remote_url, timeout=20, retries=6, chunk_size=8 * 1024)
        detected = sniff_image_format(data)
        if not detected:
            raise RuntimeError("downloaded cover bytes are not a known image format")
        cover_path.parent.mkdir(parents=True, exist_ok=True)
        tmp = cover_path.with_name(f"{cover_path.stem}.tmp{cover_path.suffix}")
        try:
            if detected == "png":
                tmp.write_bytes(data)
            elif detected in {"webp", "jpeg", "gif"}:
                from PIL import Image

                with Image.open(io.BytesIO(data)) as image:
                    image.save(tmp, format="PNG")
            else:
                raise RuntimeError(f"unsupported cover format: {detected}")
            cover_errors = validate_image_file(tmp)
            if cover_errors:
                raise RuntimeError("; ".join(cover_errors))
            tmp.replace(cover_path)
        finally:
            tmp.unlink(missing_ok=True)
        evidence.update(
            {
                "source": "range_download",
                "remote_url": remote_url,
                "remote_content_type": remote_evidence.get("content_type"),
                "remote_content_range": remote_evidence.get("content_range"),
                "remote_signature_hex": remote_evidence.get("signature_hex"),
                "downloaded_bytes": len(data),
                "detected_remote_format": detected,
            }
        )

    final_errors = validate_image_file(cover_path)
    if final_errors:
        raise RuntimeError("; ".join(final_errors))
    if sniff_image_format(cover_path.read_bytes()) != "png":
        raise RuntimeError(f"cover must be a real PNG after normalization: {cover_path}")

    evidence.update(
        {
            "bytes": cover_path.stat().st_size,
            "detected_format": "png",
            "decode_verified": True,
        }
    )
    return evidence


def compress_image_for_upload(path: Path, *, max_side: int = 1280, quality: int = 82) -> tuple[bytes, str, str]:
    """Return (bytes, mime, upload_filename) as JPEG for smaller FTP bootstrap payload."""
    from PIL import Image

    with Image.open(path) as im:
        im = im.convert("RGB")
        w, h = im.size
        longest = max(w, h)
        if longest > max_side:
            scale = max_side / longest
            im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=quality, optimize=True)
    stem = path.stem
    return buf.getvalue(), "image/jpeg", f"{stem}.jpg"


def load_article(article_dir: Path) -> dict:
    meta_path = article_dir / "article.meta.json"
    html_path = article_dir / "article.html"
    if not meta_path.is_file() or not html_path.is_file():
        raise FileNotFoundError("article.meta.json and article.html required")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    content = html_path.read_text(encoding="utf-8").strip()
    cover_path = article_dir / "cover" / "cover.png"
    schema_path = article_dir / "schema.jsonld"
    cover_b64 = ""
    cover_mime = "image/png"
    cover_upload_name = "cover.png"
    cover_evidence: dict[str, object] = {}
    cover_reg = article_dir / "cover" / "cover-registry.json"
    if cover_path.is_file():
        cover_evidence = normalize_cover_png(cover_path, cover_reg, project_root())
        cover_bytes, cover_mime, cover_upload_name = compress_image_for_upload(cover_path)
        cover_b64 = base64.b64encode(cover_bytes).decode("ascii")
    schema_raw = ""
    if schema_path.is_file():
        schema_raw = schema_path.read_text(encoding="utf-8").strip()
    cover_alt = meta.get("cover_alt") or meta.get("cover_alt_text") or ""
    if cover_reg.is_file():
        reg = json.loads(cover_reg.read_text(encoding="utf-8"))
        cover_alt = cover_alt or reg.get("cover_alt_text", "")

    import re
    img_srcs = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', content)
    inline_images = []
    for src in img_srcs:
        if not src.startswith(("http://", "https://", "data:")):
            local_path = article_dir / src
            if local_path.is_file():
                img_bytes, img_mime, upload_name = compress_image_for_upload(local_path)
                b64_data = base64.b64encode(img_bytes).decode("ascii")
                inline_images.append({
                    "src": src,
                    "b64": b64_data,
                    "filename": upload_name,
                    "mime": img_mime,
                })

    return {
        "slug": meta["slug"],
        "title": meta.get("title") or meta.get("h1", ""),
        "excerpt": meta.get("description", ""),
        "content": content,
        "cover_b64": cover_b64,
        "cover_mime": cover_mime,
        "cover_upload_name": cover_upload_name,
        "cover_evidence": cover_evidence,
        "cover_alt": cover_alt,
        "schema_jsonld": schema_raw,
        "topic_id": meta.get("topic_id", ""),
        "inline_images": inline_images,
    }


FTP_PAYLOAD_CHUNK_BYTES = 32_768
FTP_UPLOAD_RETRIES = 8


def encode_payload_b64(payload: dict) -> str:
    return base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")


def build_runner_php() -> str:
    return """<?php
require __DIR__ . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/file.php';
require_once ABSPATH . 'wp-admin/includes/media.php';
require_once ABSPATH . 'wp-admin/includes/image.php';
require_once ABSPATH . 'wp-admin/includes/post.php';

$b64 = '';
for ($i = 0; ; $i++) {
    $path = __DIR__ . '/excalibur-blog-payload.part' . $i;
    if (!file_exists($path)) {
        break;
    }
    $b64 .= file_get_contents($path);
}
if ($b64 === '') {
    echo 'ERR no payload parts' . PHP_EOL;
    exit(1);
}
$p = json_decode(base64_decode($b64), true);
"""


def wp_publish_body_php() -> str:
    return """
$slug = $p['slug'];
$existing = get_page_by_path($slug, OBJECT, 'post');
if ($existing instanceof WP_Post) {{
    $post_id = (int) $existing->ID;
    wp_update_post([
        'ID' => $post_id,
        'post_title' => $p['title'],
        'post_name' => $slug,
        'post_content' => $p['content'],
        'post_excerpt' => $p['excerpt'],
        'post_status' => 'publish',
    ]);
}} else {{
    $post_id = (int) wp_insert_post([
        'post_title' => $p['title'],
        'post_name' => $slug,
        'post_content' => $p['content'],
        'post_excerpt' => $p['excerpt'],
        'post_status' => 'publish',
        'post_type' => 'post',
    ], true);
}}
if (is_wp_error($post_id)) {{
    echo 'ERR post: ' . $post_id->get_error_message() . PHP_EOL;
    exit(1);
}}
echo 'OK post=' . $post_id . ' slug=' . $slug . PHP_EOL;

if (!empty($p['cover_b64'])) {{
    $bin = base64_decode($p['cover_b64']);
    $tmp = wp_tempnam('excalibur-cover-' . $slug . '.png');
    file_put_contents($tmp, $bin);
    $cover_mime = !empty($p['cover_mime']) ? $p['cover_mime'] : 'image/png';
    $cover_upload = !empty($p['cover_upload_name']) ? $p['cover_upload_name'] : ($slug . '-cover.png');
    $file_array = [
        'name' => $slug . '-' . basename($cover_upload),
        'tmp_name' => $tmp,
        'type' => $cover_mime,
        'error' => 0,
        'size' => strlen($bin),
    ];
    $att_id = media_handle_sideload($file_array, $post_id, null, [
        'post_title' => $slug . ' cover',
    ]);
    if (is_wp_error($att_id)) {{
        echo 'WARN cover: ' . $att_id->get_error_message() . PHP_EOL;
    }} else {{
        set_post_thumbnail($post_id, (int) $att_id);
        if (!empty($p['cover_alt'])) {{
            update_post_meta((int) $att_id, '_wp_attachment_image_alt', sanitize_text_field($p['cover_alt']));
        }}
        echo 'OK featured_image=' . (int) $att_id . PHP_EOL;
    }}
    @unlink($tmp);
}}

if (!empty($p['schema_jsonld'])) {{
    update_post_meta($post_id, '_excalibur_blog_schema_jsonld', wp_slash($p['schema_jsonld']));
    update_post_meta($post_id, '_excalibur_blog_skip_theme_faq', '1');
    echo 'OK schema_meta=1' . PHP_EOL;
    echo 'OK skip_theme_faq_meta=1' . PHP_EOL;
}}

if (!empty($p['inline_images'])) {{
    $content_updated = $p['content'];
    foreach ($p['inline_images'] as $img) {{
        $bin = base64_decode($img['b64']);
        $filename = $img['filename'];
        $src = $img['src'];
        
        $tmp = wp_tempnam('excalibur-inline-' . $slug . '-' . sanitize_title($filename));
        file_put_contents($tmp, $bin);
        
        $img_mime = !empty($img['mime']) ? $img['mime'] : 'image/png';
        $file_array = [
            'name' => $slug . '-' . $filename,
            'tmp_name' => $tmp,
            'type' => $img_mime,
            'error' => 0,
            'size' => strlen($bin),
        ];
        
        $att_id = media_handle_sideload($file_array, $post_id, null, [
            'post_title' => $slug . ' ' . pathinfo($filename, PATHINFO_FILENAME),
        ]);
        
        if (is_wp_error($att_id)) {{
            echo 'WARN inline_img_upload: ' . $att_id->get_error_message() . ' for ' . $src . PHP_EOL;
        }} else {{
            $new_url = wp_get_attachment_url((int) $att_id);
            if ($new_url) {{
                $content_updated = str_replace('src="' . $src . '"', 'src="' . $new_url . '"', $content_updated);
                $content_updated = str_replace("src='" . $src . "'", "src='" . $new_url . "'", $content_updated);
                echo 'OK inline_image_upload=' . (int) $att_id . ' src=' . $src . ' url=' . $new_url . PHP_EOL;
            }}
        }}
        @unlink($tmp);
    }}
    wp_update_post([
        'ID' => $post_id,
        'post_content' => $content_updated,
    ]);
}}

$permalink = get_permalink($post_id);
echo 'permalink=' . $permalink . PHP_EOL;
"""


def build_php(payload: dict) -> str:
    """Full runner for dry-run byte estimate (payload uploaded separately in chunks)."""
    return build_runner_php() + wp_publish_body_php()


def ftp_upload_bytes(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    import time

    last_err: Exception | None = None
    for attempt in range(FTP_UPLOAD_RETRIES):
        try:
            ftp.storbinary(f"STOR {remote}", io.BytesIO(data))
            return
        except ftplib.error_temp as e:
            last_err = e
            time.sleep(min(2**attempt, 15))
    if last_err:
        raise last_err


def ftp_upload_payload_parts(ftp_connect_fn, b64: str) -> list[str]:
    part_names: list[str] = []
    chunk = FTP_PAYLOAD_CHUNK_BYTES
    for i in range(0, len(b64), chunk):
        name = f"excalibur-blog-payload.part{len(part_names)}"
        data = b64[i : i + chunk].encode("ascii")
        ftp = ftp_connect_fn()
        try:
            ftp_upload_bytes(ftp, name, data)
        finally:
            try:
                ftp.quit()
            except Exception:  # noqa: BLE001
                pass
        part_names.append(name)
        print(f"OK ftp_part={name} bytes={len(data)}", flush=True)
    return part_names


def trigger_bootstrap_http(public_base: str, remote: str) -> str:
    url = public_base.rstrip("/") + "/" + remote
    out = ""
    try:
        print(f"Triggering HTTP publish on {url}...")
        with urllib.request.urlopen(
            urllib.request.Request(url, headers={"User-Agent": "ExcaliburBlogPublish/1.0"}),
            timeout=15,
        ) as response:
            out = response.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"Local HTTP trigger failed ({type(e).__name__}: {e}). Entering Cloud WebFetch Fallback mode...")
        print(f"=== FALLBACK_TRIGGER_URL ===\n{url}\n=============================")
        print("Waiting for cloud-agent to write response to memory/webfetch-response.txt...")

        fallback_file = project_root() / "memory" / "webfetch-response.txt"
        fallback_file.unlink(missing_ok=True)

        import time

        for _ in range(120):
            if fallback_file.is_file():
                out = fallback_file.read_text(encoding="utf-8")
                fallback_file.unlink()
                print("Cloud response detected successfully!")
                break
            time.sleep(1)

        if not out:
            raise RuntimeError("Cloud WebFetch Fallback timed out after 120 seconds. Please trigger manually.")
    return out


def upload_bootstrap_artifacts(
    *,
    b64: str,
    runner: str,
    remote: str,
    write_file: Callable[[str, bytes], None],
    remove_file: Callable[[str], None],
    list_files: Callable[[], list[str]] | None = None,
) -> list[str]:
    if list_files:
        for name in list_files():
            if name == remote or name.startswith("excalibur-blog-payload.part"):
                try:
                    remove_file(name)
                except Exception:  # noqa: BLE001
                    pass
    part_names: list[str] = []
    chunk = FTP_PAYLOAD_CHUNK_BYTES
    for i in range(0, len(b64), chunk):
        name = f"excalibur-blog-payload.part{len(part_names)}"
        write_file(name, b64[i : i + chunk].encode("ascii"))
        part_names.append(name)
        print(f"OK payload_part={name} bytes={min(chunk, len(b64) - i)}", flush=True)
    write_file(remote, runner.encode("utf-8"))
    return part_names


def publish_via_sftp(env: dict[str, str], payload: dict, public_base: str) -> str:
    import paramiko

    remote = "excalibur-blog-publish-once.php"
    host = env.get("SFTP_HOST") or env.get("SSH_HOST") or ""
    user = env.get("SFTP_USER") or env.get("SSH_USER") or ""
    password = env.get("SFTP_PASSWORD") or env.get("SSH_PASSWORD") or ""
    port = int(env.get("SFTP_PORT") or env.get("SSH_PORT") or "22")
    root = (env.get("REMOTE_SITE_ROOT") or env.get("FTP_ROOT") or "/").strip()
    if not host or not user or not password:
        raise RuntimeError("SFTP/SSH credentials missing (SFTP_HOST/SSH_HOST, user, password)")

    b64 = encode_payload_b64(payload)
    runner = build_runner_php() + wp_publish_body_php()

    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    if root and root != "/":
        sftp.chdir(root)

    def sftp_write(name: str, data: bytes) -> None:
        with sftp.file(name, "w") as handle:
            handle.write(data)

    def sftp_remove(name: str) -> None:
        sftp.remove(name)

    def sftp_list() -> list[str]:
        return sftp.listdir(".")

    part_names = upload_bootstrap_artifacts(
        b64=b64,
        runner=runner,
        remote=remote,
        write_file=sftp_write,
        remove_file=sftp_remove,
        list_files=sftp_list,
    )
    sftp.close()
    transport.close()

    out = trigger_bootstrap_http(public_base, remote)

    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    if root and root != "/":
        sftp.chdir(root)
    try:
        sftp.remove(remote)
    except OSError:
        pass
    for name in part_names:
        try:
            sftp.remove(name)
        except OSError:
            pass
    sftp.close()
    transport.close()
    return out


def publish_via_ftp(env: dict[str, str], payload: dict, public_base: str) -> str:
    remote = "excalibur-blog-publish-once.php"
    ftp_root = (env.get("FTP_ROOT") or env.get("FTP_PATH") or "/").strip()
    if not ftp_root.startswith("/"):
        ftp_root = "/" + ftp_root
    if not ftp_root.endswith("/"):
        ftp_root += "/"

    def ftp_connect() -> ftplib.FTP:
        ftp = ftplib.FTP()
        ftp.connect(env["FTP_HOST"], int(env.get("FTP_PORT", "21")), timeout=120)
        ftp.login(env["FTP_USER"], env["FTP_PASS"])
        ftp.set_pasv(True)
        ftp.cwd(ftp_root)
        return ftp

    b64 = encode_payload_b64(payload)
    runner = build_runner_php() + wp_publish_body_php()

    def ftp_write(name: str, data: bytes) -> None:
        ftp = ftp_connect()
        try:
            ftp_upload_bytes(ftp, name, data)
        finally:
            ftp.quit()

    def ftp_remove(name: str) -> None:
        ftp = ftp_connect()
        try:
            ftp.delete(name)
        except ftplib.error_perm:
            pass
        finally:
            ftp.quit()

    part_names = upload_bootstrap_artifacts(
        b64=b64,
        runner=runner,
        remote=remote,
        write_file=ftp_write,
        remove_file=ftp_remove,
    )

    out = trigger_bootstrap_http(public_base, remote)

    ftp = ftp_connect()
    try:
        ftp.delete(remote)
    except ftplib.error_perm:
        pass
    for name in part_names:
        try:
            ftp.delete(name)
        except ftplib.error_perm:
            pass
    ftp.quit()
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", type=Path, required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--public-base", type=str, default=None, help="Override PUBLIC_SITE_URL")
    args = ap.parse_args()
    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    payload = load_article(article_dir)

    if args.dry_run:
        b64 = encode_payload_b64(payload)
        runner = build_php(payload)
        print(json.dumps({"dry_run": True, "slug": payload["slug"], "title": payload["title"]}, ensure_ascii=False, indent=2))
        print("PHP runner bytes:", len(runner.encode("utf-8")))
        print("Payload b64 bytes:", len(b64))
        print(
            "FTP parts:",
            (len(b64) + FTP_PAYLOAD_CHUNK_BYTES - 1) // FTP_PAYLOAD_CHUNK_BYTES,
            f"(chunk<={FTP_PAYLOAD_CHUNK_BYTES})",
        )
        return 0

    env = load_env(root)
    if env.get("EXCALIBUR_BLOG_ALLOW_PUBLISH", "").strip().lower() != "yes":
        print("BLOCKER: EXCALIBUR_BLOG_ALLOW_PUBLISH != yes", file=sys.stderr)
        return 1
    public = args.public_base or env.get("PUBLIC_SITE_URL") or env.get("WP_HOME") or ""
    if not public:
        print("PUBLIC_SITE_URL or --public-base required", file=sys.stderr)
        return 2
    if env.get("SFTP_HOST") or env.get("SSH_HOST"):
        print("Using SFTP bootstrap upload (SSH)", flush=True)
        out = publish_via_sftp(env, payload, public)
    else:
        out = publish_via_ftp(env, payload, public)
    print(out)

    result_path = article_dir / "wp-publish-result.json"
    permalink = ""
    for line in out.splitlines():
        if line.startswith("permalink="):
            permalink = line.split("=", 1)[1].strip()
    result = {
        "slug": payload["slug"],
        "topic_id": payload["topic_id"],
        "permalink": permalink,
        "cover_evidence": payload.get("cover_evidence", {}),
        "raw_output": out,
        "verdict": "pass" if "OK post=" in out else "fail",
    }
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if result["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
