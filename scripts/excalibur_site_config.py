#!/usr/bin/env python3
"""Load canonical production site settings for Excalibur BLOG scripts."""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

# Project-scoped env (не конфликтует с PUBLIC_SITE_URL других репозиториев в Cloud Secrets)
PRIMARY_PUBLIC_SITE_URL_ENV = "EXCALIBUR_PUBLIC_SITE_URL"
LEGACY_PUBLIC_SITE_URL_ENVS = ("PUBLIC_SITE_URL", "WP_SITE_URL", "WP_HOME")


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


def public_site_url_env_keys(root: Path | None = None) -> tuple[str, ...]:
    cfg = load_production_site(root)
    primary = str(cfg.get("public_site_url_env") or PRIMARY_PUBLIC_SITE_URL_ENV)
    keys: list[str] = [primary]
    for legacy in LEGACY_PUBLIC_SITE_URL_ENVS:
        if legacy not in keys:
            keys.append(legacy)
    return tuple(keys)


def resolve_public_site_url(local_env: dict[str, str] | None = None, root: Path | None = None) -> str:
    for key in public_site_url_env_keys(root):
        val = (os.environ.get(key) or (local_env or {}).get(key) or "").strip()
        if val:
            return _url_from_value(val)
    return ""


def default_public_site_url(root: Path | None = None) -> str:
    return resolve_public_site_url(None, root)


def article_public_url(slug: str, site_base: str | None = None, root: Path | None = None) -> str:
    base = _url_from_value(site_base) if site_base else default_public_site_url(root)
    if not base:
        raise RuntimeError(
            f"{PRIMARY_PUBLIC_SITE_URL_ENV} is not set; configure Cloud Secrets or memory/site.env.local"
        )
    cfg = load_production_site(root)
    template = str(cfg.get("article_path_template", "/{slug}/"))
    return f"{base}{template.format(slug=slug.strip('/'))}"
