#!/usr/bin/env python3
"""Load canonical production site settings for Excalibur BLOG scripts."""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _url_from_value(value: str) -> str:
    value = value.strip().rstrip("/")
    if not value:
        return ""
    if value.startswith("http://") or value.startswith("https://"):
        return value
    return f"https://{value}"


def load_production_site(root: Path | None = None) -> dict[str, Any]:
    root = root or project_root()
    path = root / "shared" / "production-site.json"
    if not path.is_file():
        return {"article_path_template": "/{slug}/"}
    return json.loads(path.read_text(encoding="utf-8"))


def default_public_site_url(root: Path | None = None) -> str:
    cfg = load_production_site(root)
    env_key = str(cfg.get("public_site_url_env") or "PUBLIC_SITE_URL")
    for key in (env_key, "PUBLIC_SITE_URL", "WP_SITE_URL"):
        val = os.environ.get(key, "").strip()
        if val:
            return _url_from_value(val)
    return ""


def article_public_url(slug: str, site_base: str | None = None, root: Path | None = None) -> str:
    cfg = load_production_site(root)
    base = _url_from_value(site_base) if site_base else default_public_site_url(root)
    if not base:
        raise RuntimeError("PUBLIC_SITE_URL is not set; configure Cloud Secrets or memory/site.env.local")
    template = str(cfg.get("article_path_template", "/{slug}/"))
    return f"{base}{template.format(slug=slug.strip('/'))}"
