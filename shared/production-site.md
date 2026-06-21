# Production site — Excalibur BLOG

**Канонический домен публикации:** Cloud Secret `EXCALIBUR_PUBLIC_SITE_URL` (production WordPress).

## Конфигурация

| Параметр | Значение |
|----------|----------|
| `EXCALIBUR_PUBLIC_SITE_URL` | production WordPress |
| `PUBLIC_SITE_URL` | тот же хост для publish-скриптов |
| `blog_path_prefix` | `/` → URL вида `/{slug}/` |
| Machine-readable | `shared/site-config.json` |

## Cloud Secrets (обязательно)

- `EXCALIBUR_PUBLIC_SITE_URL`
- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`
- `FTP_HOST`, `FTP_USER`, `FTP_PASS`, `FTP_ROOT`

## Publish preflight

```bash
python3 scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/<dir>/article.html \
  -o memory/blog/articles/<dir>/link-verify.json \
  --site-base "$EXCALIBUR_PUBLIC_SITE_URL"
```

## Legacy

- ~~mayai.ru~~ — не целевой домен этого репозитория.
