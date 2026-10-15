#!/usr/bin/env python3
"""Publish one Excalibur blog article to WordPress (FTP bootstrap)."""
from __future__ import annotations

import argparse
import base64
import ftplib
import io
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

from asset_download import download_url_bytes
from excalibur_repo_paths import repo_relative
from image_validate import sniff_image_format, validate_image_file


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def merge_cloud_env(env: dict[str, str]) -> dict[str, str]:
    """Overlay Cloud Secrets / process env onto file-based site.env.local."""
    for key in (
        "FTP_HOST",
        "FTP_PORT",
        "FTP_USER",
        "FTP_PASS",
        "FTP_PASSWORD",
        "FTP_ROOT",
        "FTP_PATH",
        "REMOTE_SITE_ROOT",
        "PUBLIC_SITE_URL",
        "EXCALIBUR_PUBLIC_SITE_URL",
        "EXCALIBUR_BLOG_ALLOW_PUBLISH",
        "SFTP_HOST",
        "SFTP_PORT",
        "SFTP_USER",
        "SFTP_PASSWORD",
        "SSH_HOST",
        "SSH_PORT",
        "SSH_USER",
        "SSH_PASSWORD",
    ):
        value = os.environ.get(key, "").strip()
        if value:
            env[key] = value
    if not env.get("FTP_PASS") and env.get("FTP_PASSWORD"):
        env["FTP_PASS"] = env["FTP_PASSWORD"]
    if not env.get("PUBLIC_SITE_URL") and env.get("EXCALIBUR_PUBLIC_SITE_URL"):
        env["PUBLIC_SITE_URL"] = env["EXCALIBUR_PUBLIC_SITE_URL"]
    if not env.get("FTP_ROOT") and env.get("REMOTE_SITE_ROOT"):
        env["FTP_ROOT"] = env["REMOTE_SITE_ROOT"]
    return env


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
    env = merge_cloud_env(env)
    if not env.get("FTP_HOST") or not env.get("FTP_USER") or not env.get("FTP_PASS"):
        raise FileNotFoundError("FTP credentials missing (memory/site.env.local or Cloud FTP_* secrets)")
    return env


def remote_site_root(env: dict[str, str]) -> str:
    root = (env.get("FTP_ROOT") or env.get("FTP_PATH") or env.get("REMOTE_SITE_ROOT") or "/").strip()
    if not root.startswith("/"):
        root = "/" + root
    if not root.endswith("/"):
        root += "/"
    return root


def sftp_credentials(env: dict[str, str]) -> tuple[str, int, str, str]:
    host = (env.get("SFTP_HOST") or env.get("SSH_HOST") or env.get("FTP_HOST") or "").strip()
    port = int(env.get("SFTP_PORT") or env.get("SSH_PORT") or 22)
    user = (env.get("SFTP_USER") or env.get("SSH_USER") or env.get("FTP_USER") or "").strip()
    passwd = (env.get("SFTP_PASSWORD") or env.get("SSH_PASSWORD") or env.get("FTP_PASS") or "").strip()
    if not host or not user or not passwd:
        raise RuntimeError("SFTP credentials missing")
    return host, port, user, passwd


def sftp_account_candidates(env: dict[str, str]) -> list[str]:
    users: list[str] = []
    for key in ("SFTP_USER", "SSH_USER", "FTP_USER"):
        value = env.get(key, "").strip()
        if value and value not in users:
            users.append(value)
    remote_root = env.get("REMOTE_SITE_ROOT", "")
    match = re.search(r"/home/[^/]+/([^/]+)/", remote_root)
    if match:
        acct = match.group(1)
        for candidate in (acct, f"{acct}_blog"):
            if candidate not in users:
                users.append(candidate)
    return users


def sftp_upload(env: dict[str, str], remote_name: str, payload: bytes, remote_dir: str) -> None:
    import paramiko

    host, port, _, passwd = sftp_credentials(env)
    last_error: Exception | None = None
    for user in sftp_account_candidates(env):
        transport: paramiko.Transport | None = None
        try:
            transport = paramiko.Transport((host, port))
            transport.connect(username=user, password=passwd)
            sftp = paramiko.SFTPClient.from_transport(transport)
            if not sftp:
                raise RuntimeError("SFTP client unavailable")
            target_dir = remote_dir.rstrip("/") or "/"
            try:
                sftp.chdir(target_dir)
            except OSError:
                pass
            with sftp.file(remote_name, "w") as handle:
                handle.write(payload)
            print(f"OK sftp_upload user={user} dir={target_dir} file={remote_name}")
            sftp.close()
            transport.close()
            return
        except Exception as exc:
            last_error = exc
            if transport is not None:
                transport.close()
            continue
    raise RuntimeError(f"SFTP bootstrap failed: {last_error}")


def sftp_delete(env: dict[str, str], remote_name: str, remote_dir: str) -> None:
    import paramiko

    host, port, _, passwd = sftp_credentials(env)
    for user in sftp_account_candidates(env):
        transport: paramiko.Transport | None = None
        try:
            transport = paramiko.Transport((host, port))
            transport.connect(username=user, password=passwd)
            sftp = paramiko.SFTPClient.from_transport(transport)
            if not sftp:
                return
            target_dir = remote_dir.rstrip("/") or "/"
            try:
                sftp.chdir(target_dir)
            except OSError:
                pass
            try:
                sftp.remove(remote_name)
            except OSError:
                pass
            sftp.close()
            transport.close()
            return
        except Exception:
            if transport is not None:
                transport.close()
            continue


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
    cover_evidence: dict[str, object] = {}
    cover_reg = article_dir / "cover" / "cover-registry.json"
    if cover_path.is_file():
        cover_evidence = normalize_cover_png(cover_path, cover_reg, project_root())
        cover_b64 = base64.b64encode(cover_path.read_bytes()).decode("ascii")
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
                img_bytes = local_path.read_bytes()
                b64_data = base64.b64encode(img_bytes).decode("ascii")
                inline_images.append({
                    "src": src,
                    "b64": b64_data,
                    "filename": local_path.name
                })

    return {
        "slug": meta["slug"],
        "title": meta.get("title") or meta.get("h1", ""),
        "excerpt": meta.get("description", ""),
        "content": content,
        "cover_b64": cover_b64,
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
    $tmp = wp_tempnam('excalibur-cover-' . $slug . '.png');
    file_put_contents($tmp, $bin);
    $file_array = [
        'name' => $slug . '-cover.png',
        'tmp_name' => $tmp,
        'type' => 'image/png',
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
        
        $file_array = [
            'name' => $slug . '-' . $filename,
            'tmp_name' => $tmp,
            'type' => 'image/png',
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


def upload_bootstrap(env: dict[str, str], remote: str, php: str) -> str:
    """Upload one-shot bootstrap PHP via FTP; fall back to SFTP on 425 Bad IP."""
    ftp_root = remote_site_root(env)
    payload = php.encode("utf-8")

    def ftp_connect() -> ftplib.FTP:
        ftp = ftplib.FTP()
        ftp.connect(env["FTP_HOST"], int(env.get("FTP_PORT", "21")), timeout=120)
        ftp.login(env["FTP_USER"], env["FTP_PASS"])
        ftp.set_pasv(True)
        ftp.cwd(ftp_root)
        return ftp

    try:
        ftp = ftp_connect()
        try:
            ftp.storbinary(f"STOR {remote}", io.BytesIO(payload))
        except ftplib.error_perm as exc:
            if "425" in str(exc):
                print(f"FTP STOR 425 Bad IP ({exc}); switching to SFTP bootstrap on port 22...")
                ftp.quit()
                sftp_upload(env, remote, payload, ftp_root)
            else:
                raise
        else:
            ftp.quit()
    except ftplib.error_perm as exc:
        if "425" in str(exc):
            print(f"FTP login/path 425 ({exc}); switching to SFTP bootstrap on port 22...")
            sftp_upload(env, remote, payload, ftp_root)
        else:
            raise
    return ftp_root


def publish_via_ftp(env: dict[str, str], php: str, public_base: str) -> str:
    remote = "excalibur-blog-publish-once.php"
    ftp_root = upload_bootstrap(env, remote, php)

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
        for i in range(120):
            if fallback_file.is_file():
                out = fallback_file.read_text(encoding="utf-8")
                fallback_file.unlink()
                print("Cloud response detected successfully!")
                break
            time.sleep(1)
        
        if not out:
            raise RuntimeError("Cloud WebFetch Fallback timed out after 120 seconds. Please trigger manually.")

    try:
        ftp = ftplib.FTP()
        ftp.connect(env["FTP_HOST"], int(env.get("FTP_PORT", "21")), timeout=120)
        ftp.login(env["FTP_USER"], env["FTP_PASS"])
        ftp.set_pasv(True)
        ftp.cwd(ftp_root)
        try:
            ftp.delete(remote)
        except ftplib.error_perm:
            pass
        ftp.quit()
    except ftplib.error_perm as exc:
        if "425" in str(exc):
            sftp_delete(env, remote, ftp_root)
        else:
            try:
                sftp_delete(env, remote, ftp_root)
            except RuntimeError:
                pass
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
    public = (
        args.public_base
        or env.get("EXCALIBUR_PUBLIC_SITE_URL")
        or env.get("PUBLIC_SITE_URL")
        or env.get("WP_HOME")
        or ""
    )
    if not public:
        print("PUBLIC_SITE_URL or --public-base required", file=sys.stderr)
        return 2
    try:
        out = publish_via_ftp(env, php, public)
    except Exception as exc:
        out = f"ERR publish: {type(exc).__name__}: {exc}"
        print(out, file=sys.stderr)
        result_path = article_dir / "wp-publish-result.json"
        result = {
            "slug": payload["slug"],
            "topic_id": payload["topic_id"],
            "permalink": "",
            "cover_evidence": payload.get("cover_evidence", {}),
            "raw_output": out,
            "verdict": "fail",
        }
        result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return 1
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
