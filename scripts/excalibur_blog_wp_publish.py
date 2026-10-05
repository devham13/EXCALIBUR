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
import time
import urllib.request
from pathlib import Path

FTP_CHUNK_BYTES = 8 * 1024
FTP_STOR_MAX_ATTEMPTS = 20

from asset_download import download_url_bytes
from excalibur_repo_paths import repo_relative
from image_validate import sniff_image_format, validate_image_file


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_env(root: Path) -> dict[str, str]:
    for name in ("memory/site.env.local", "memory/site.env.local.example"):
        p = root / name
        if p.is_file():
            env: dict[str, str] = {}
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip()
            env = dict(env)
            break
    else:
        raise FileNotFoundError("site.env.local not found under memory/")
    for key, value in os.environ.items():
        if not value:
            continue
        if key.startswith(("FTP_", "SSH_", "PUBLIC_", "EXCALIBUR_BLOG", "WP_")) or key in {
            "WP_HOME",
            "WP_SITEURL",
        }:
            env[key] = value.strip()
    if os.environ.get("SSH_PASSWORD") and not env.get("SSH_PASS"):
        env["SSH_PASS"] = os.environ["SSH_PASSWORD"].strip()
    if os.environ.get("FTP_PASSWORD") and not env.get("FTP_PASS"):
        env["FTP_PASS"] = os.environ["FTP_PASSWORD"].strip()
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


def encode_image_bytes_for_publish(path: Path) -> tuple[bytes, str, str]:
    """Smaller FTP payload: JPEG for large PNG/WebP assets (WP sideload keeps filename/mime)."""
    raw = path.read_bytes()
    if len(raw) <= 150_000:
        ext = path.suffix.lower().lstrip(".") or "png"
        mime_map = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "webp": "image/webp", "gif": "image/gif"}
        return raw, path.name, mime_map.get(ext, "application/octet-stream")
    from PIL import Image

    buf = io.BytesIO()
    with Image.open(io.BytesIO(raw)) as image:
        image.convert("RGB").save(buf, format="JPEG", quality=85, optimize=True)
    return buf.getvalue(), f"{path.stem}.jpg", "image/jpeg"


def load_article(article_dir: Path) -> dict:
    meta_path = article_dir / "article.meta.json"
    html_path = article_dir / "article.html"
    if not meta_path.is_file() or not html_path.is_file():
        raise FileNotFoundError("article.meta.json and article.html required")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    content = html_path.read_text(encoding="utf-8").strip()
    cover_path = article_dir / "cover" / "cover.png"
    schema_path = article_dir / "schema.jsonld"
    cover_evidence: dict[str, object] = {}
    cover_reg = article_dir / "cover" / "cover-registry.json"
    cover_mime = "image/png"
    cover_upload_name = "cover.png"
    cover_b64 = ""
    if cover_path.is_file():
        cover_evidence = normalize_cover_png(cover_path, cover_reg, project_root())
        cover_bytes, cover_upload_name, cover_mime = encode_image_bytes_for_publish(cover_path)
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
                img_bytes, upload_name, mime = encode_image_bytes_for_publish(local_path)
                b64_data = base64.b64encode(img_bytes).decode("ascii")
                inline_images.append({
                    "src": src,
                    "b64": b64_data,
                    "filename": upload_name,
                    "mime": mime,
                })

    return {
        "slug": meta["slug"],
        "title": meta.get("title") or meta.get("h1", ""),
        "excerpt": meta.get("description", ""),
        "content": content,
        "cover_b64": cover_b64,
        "cover_upload_name": cover_upload_name,
        "cover_mime": cover_mime,
        "cover_evidence": cover_evidence,
        "cover_alt": cover_alt,
        "schema_jsonld": schema_raw,
        "topic_id": meta.get("topic_id", ""),
        "inline_images": inline_images,
    }


def build_php(payload: dict) -> str:
    b64 = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/file.php';
require_once ABSPATH . 'wp-admin/includes/media.php';
require_once ABSPATH . 'wp-admin/includes/image.php';
require_once ABSPATH . 'wp-admin/includes/post.php';

$p = json_decode(base64_decode('{b64}'), true);
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
    $cover_name = !empty($p['cover_upload_name']) ? $p['cover_upload_name'] : ($slug . '-cover.png');
    $cover_mime = !empty($p['cover_mime']) ? $p['cover_mime'] : 'image/png';
    $tmp = wp_tempnam('excalibur-cover-' . $slug . '-' . $cover_name);
    file_put_contents($tmp, $bin);
    $file_array = [
        'name' => $slug . '-' . $cover_name,
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
        
        $mime = !empty($img['mime']) ? $img['mime'] : 'image/png';
        $file_array = [
            'name' => $slug . '-' . $filename,
            'tmp_name' => $tmp,
            'type' => $mime,
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


def _ftp_connect(env: dict[str, str], ftp_root: str) -> ftplib.FTP:
    ftp = ftplib.FTP()
    ftp.connect(env["FTP_HOST"], int(env.get("FTP_PORT", "21")), timeout=120)
    ftp.login(env["FTP_USER"], env["FTP_PASS"])
    ftp.set_pasv(True)
    ftp.cwd(ftp_root)
    return ftp


def _ftp_remote_size(env: dict[str, str], ftp_root: str, remote: str) -> int | None:
    try:
        ftp = _ftp_connect(env, ftp_root)
        size = ftp.size(remote)
        ftp.quit()
        return int(size) if size is not None else None
    except Exception:
        return None


def _ftp_stor_bytes(env: dict[str, str], ftp_root: str, remote: str, data: bytes) -> None:
    last_err: Exception | None = None
    for attempt in range(FTP_STOR_MAX_ATTEMPTS):
        try:
            ftp = _ftp_connect(env, ftp_root)
            ftp.storbinary(f"STOR {remote}", io.BytesIO(data))
            ftp.quit()
            return
        except (ftplib.error_temp, ftplib.error_perm, OSError) as e:
            last_err = e
            time.sleep(min(8.0, 0.4 * (2**attempt)))
    raise RuntimeError(f"FTP STOR failed for {remote} after {FTP_STOR_MAX_ATTEMPTS} attempts: {last_err}")


def _ftp_upload_php(env: dict[str, str], ftp_root: str, remote: str, php: str) -> None:
    body = php.encode("utf-8")
    if len(body) <= 120_000:
        try:
            _ftp_stor_bytes(env, ftp_root, remote, body)
            return
        except RuntimeError:
            pass

    base = remote.replace(".php", "")
    part_names: list[str] = []
    chunks = [body[i : i + FTP_CHUNK_BYTES] for i in range(0, len(body), FTP_CHUNK_BYTES)]
    for idx, chunk in enumerate(chunks):
        part = f"{base}.part{idx:05d}"
        existing = _ftp_remote_size(env, ftp_root, part)
        if existing != len(chunk):
            print(f"FTP upload chunk {idx + 1}/{len(chunks)} ({len(chunk)} bytes)...", flush=True)
            _ftp_stor_bytes(env, ftp_root, part, chunk)
        else:
            print(f"FTP chunk {idx + 1}/{len(chunks)} already on server, skip", flush=True)
        part_names.append(part)

    loader = f"""<?php
$prefix = __DIR__ . '/{base}.part';
$buf = '';
for ($i = 0; $i < {len(part_names)}; $i++) {{
    $buf .= file_get_contents($prefix . str_pad((string) $i, 5, '0', STR_PAD_LEFT));
}}
$run = __DIR__ . '/{base}.assembled.php';
file_put_contents($run, $buf);
require $run;
for ($i = 0; $i < {len(part_names)}; $i++) {{
    @unlink($prefix . str_pad((string) $i, 5, '0', STR_PAD_LEFT));
}}
@unlink($run);
"""
    _ftp_stor_bytes(env, ftp_root, remote, loader.encode("utf-8"))


def _ftp_cleanup_publish_artifacts(env: dict[str, str], ftp_root: str, remote: str) -> None:
    base = remote.replace(".php", "")
    try:
        ftp = _ftp_connect(env, ftp_root)
    except Exception:
        return
    for name in (remote, f"{base}.assembled.php"):
        try:
            ftp.delete(name)
        except ftplib.error_perm:
            pass
    misses = 0
    for idx in range(5000):
        part = f"{base}.part{idx:05d}"
        try:
            ftp.delete(part)
            misses = 0
        except ftplib.error_perm:
            misses += 1
            if misses >= 3:
                break
    try:
        ftp.quit()
    except Exception:
        pass


def _trigger_publish_url(url: str) -> str:
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

        for i in range(120):
            if fallback_file.is_file():
                out = fallback_file.read_text(encoding="utf-8")
                fallback_file.unlink()
                print("Cloud response detected successfully!")
                break
            time.sleep(1)

        if not out:
            raise RuntimeError("Cloud WebFetch Fallback timed out after 120 seconds. Please trigger manually.")
    return out


def _sftp_upload_php(env: dict[str, str], remote: str, php: str) -> None:
    import paramiko

    wp_root = (env.get("SSH_WP_ROOT") or "").strip().rstrip("/")
    if not wp_root:
        raise RuntimeError("SSH_WP_ROOT required for SFTP publish")
    host = env.get("SSH_HOST", "").strip()
    user = env.get("SSH_USER", "").strip()
    password = env.get("SSH_PASS", "").strip()
    if not host or not user or not password:
        raise RuntimeError("SSH_HOST, SSH_USER, SSH_PASS required for SFTP publish")
    port = int(env.get("SSH_PORT", "22"))
    remote_path = f"{wp_root}/{remote}"
    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    try:
        with sftp.file(remote_path, "w") as handle:
            handle.write(php.encode("utf-8"))
        sftp.chmod(remote_path, 0o644)
    finally:
        sftp.close()
        transport.close()
    print(f"SFTP uploaded bootstrap ({len(php.encode('utf-8'))} bytes)", flush=True)


def _sftp_cleanup(env: dict[str, str], remote: str) -> None:
    import paramiko

    wp_root = (env.get("SSH_WP_ROOT") or "").strip().rstrip("/")
    if not wp_root:
        return
    host = env.get("SSH_HOST", "").strip()
    user = env.get("SSH_USER", "").strip()
    password = env.get("SSH_PASS", "").strip()
    if not host or not user or not password:
        return
    port = int(env.get("SSH_PORT", "22"))
    remote_path = f"{wp_root}/{remote}"
    base = remote.replace(".php", "")
    transport = paramiko.Transport((host, port))
    try:
        transport.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        for path in (remote_path, f"{wp_root}/{base}.assembled.php"):
            try:
                sftp.remove(path)
            except OSError:
                pass
        for idx in range(5000):
            part = f"{wp_root}/{base}.part{idx:05d}"
            try:
                sftp.remove(part)
            except OSError:
                if idx > 0:
                    break
        sftp.close()
    finally:
        transport.close()


def publish_via_ftp(env: dict[str, str], php: str, public_base: str) -> str:
    remote = "excalibur-blog-publish-once.php"
    url = public_base.rstrip("/") + "/" + remote

    if env.get("SSH_HOST", "").strip() and env.get("SSH_WP_ROOT", "").strip():
        _sftp_upload_php(env, remote, php)
    else:
        ftp_root = (env.get("FTP_ROOT") or env.get("FTP_PATH") or "/").strip()
        if not ftp_root.startswith("/"):
            ftp_root = "/" + ftp_root
        if not ftp_root.endswith("/"):
            ftp_root += "/"
        _ftp_upload_php(env, ftp_root, remote, php)

    out = _trigger_publish_url(url)

    if env.get("SSH_HOST", "").strip() and env.get("SSH_WP_ROOT", "").strip():
        _sftp_cleanup(env, remote)
    else:
        ftp_root = (env.get("FTP_ROOT") or env.get("FTP_PATH") or "/").strip()
        if not ftp_root.startswith("/"):
            ftp_root = "/" + ftp_root
        if not ftp_root.endswith("/"):
            ftp_root += "/"
        _ftp_cleanup_publish_artifacts(env, ftp_root, remote)
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
    php = build_php(payload)

    if args.dry_run:
        print(json.dumps({"dry_run": True, "slug": payload["slug"], "title": payload["title"]}, ensure_ascii=False, indent=2))
        print("PHP bytes:", len(php.encode("utf-8")))
        return 0

    env = load_env(root)
    if env.get("EXCALIBUR_BLOG_ALLOW_PUBLISH", "").strip().lower() != "yes":
        print("BLOCKER: EXCALIBUR_BLOG_ALLOW_PUBLISH != yes", file=sys.stderr)
        return 1
    public = args.public_base or env.get("PUBLIC_SITE_URL") or env.get("WP_HOME") or ""
    if not public:
        print("PUBLIC_SITE_URL or --public-base required", file=sys.stderr)
        return 2
    out = publish_via_ftp(env, php, public)
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
