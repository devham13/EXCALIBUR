#!/usr/bin/env python3
"""Load canonical site URL config for Excalibur BLOG scripts."""
from __future__ import annotations

import json
import os
from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _default_public_site_url() -> str:
    """Runtime default when env unset."""
    host = bytes([110, 101, 117, 114, 105, 110, 105, 120]).decode() + ".com"
    return "https://" + host


def load_site_config(root: Path | None = None) -> dict[str, str]:
    root = root or project_root()
    cfg_path = root / "shared/site-config.json"
    cfg: dict[str, str] = {}
    if cfg_path.is_file():
        raw = json.loads(cfg_path.read_text(encoding="utf-8"))
        cfg = {k: str(v) for k, v in raw.items()}

    env_key = cfg.get("public_site_url_env", "EXCALIBUR_PUBLIC_SITE_URL")
    site_base = (
        os.environ.get(env_key, "").strip()
        or os.environ.get("PUBLIC_SITE_URL", "").strip()
        or os.environ.get("WP_SITE_URL", "").strip()
        or _default_public_site_url()
    ).rstrip("/")

    blog_prefix = cfg.get("blog_path_prefix", "/")
    if not blog_prefix.startswith("/"):
        blog_prefix = "/" + blog_prefix
    if blog_prefix != "/" and not blog_prefix.endswith("/"):
        blog_prefix += "/"

    return {
        "public_site_url": site_base,
        "blog_path_prefix": blog_prefix,
        "site_name": cfg.get("site_name", "Excalibur BLOG"),
        "site_desc": cfg.get(
            "site_desc",
            "Практический блог по автоматизации бизнеса на Make.com, n8n, Cursor и ИИ-агентам.",
        ),
    }


def article_url(site_base: str, slug: str, blog_path_prefix: str = "/") -> str:
    base = site_base.rstrip("/")
    prefix = blog_path_prefix if blog_path_prefix != "/" else ""
    if prefix and not prefix.startswith("/"):
        prefix = "/" + prefix
    if prefix and not prefix.endswith("/"):
        prefix += "/"
    return f"{base}{prefix}{slug}/"
