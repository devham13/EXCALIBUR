#!/usr/bin/env python3
"""Deploy excalibur-blog-ui plugin to WordPress via SSH/SFTP."""
from __future__ import annotations

import os
import stat
from pathlib import Path

import paramiko

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_SRC = ROOT / "memory/wp/plugins/excalibur-blog-ui"


def wp_root_from_theme(theme_path: str) -> str:
    marker = "/wp-content/themes/"
    if marker not in theme_path:
        raise RuntimeError(f"Cannot derive WP root from theme path: {theme_path}")
    return theme_path.split(marker, 1)[0]


def upload_dir(sftp: paramiko.SFTPClient, local: Path, remote: str) -> None:
    try:
        sftp.mkdir(remote)
    except OSError:
        pass

    for item in sorted(local.iterdir()):
        remote_path = f"{remote}/{item.name}"
        if item.is_dir():
            upload_dir(sftp, item, remote_path)
        else:
            sftp.put(str(item), remote_path)
            print(f"uploaded {item.relative_to(ROOT)} -> {remote_path}")


def main() -> int:
    host = os.environ["SSH_HOST"]
    user = os.environ["SSH_USER"]
    pwd = os.environ["SSH_PASSWORD"]
    port = int(os.environ.get("SSH_PORT", "22"))
    theme = os.environ["SSH_THEME_PATH"]
    wp_root = wp_root_from_theme(theme)
    wp_cli = os.environ.get("WP_CLI_BIN", "wp")
    remote_plugin = f"{wp_root}/wp-content/plugins/excalibur-blog-ui"

    if not PLUGIN_SRC.is_dir():
        raise SystemExit(f"Missing plugin source: {PLUGIN_SRC}")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=user, password=pwd, timeout=30)

    sftp = client.open_sftp()
    upload_dir(sftp, PLUGIN_SRC, remote_plugin)
    sftp.close()

    cmds = [
        f"{wp_cli} --path={wp_root} plugin is-active excalibur-blog-ui 2>/dev/null || {wp_cli} --path={wp_root} plugin activate excalibur-blog-ui",
        f"{wp_cli} --path={wp_root} cache flush 2>/dev/null || true",
    ]
    for cmd in cmds:
        stdin, stdout, stderr = client.exec_command(cmd, timeout=120)
        out = stdout.read().decode()
        err = stderr.read().decode()
        code = stdout.channel.recv_exit_status()
        print("===", cmd[:120], "===")
        print(out or err)
        if code != 0 and "plugin activate" in cmd:
            raise RuntimeError(f"wp-cli failed: {err or out}")

    client.close()
    print("OK: excalibur-blog-ui deployed and active")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
