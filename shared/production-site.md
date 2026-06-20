# Excalibur BLOG — production site

## Env (project-scoped)

Используй **префикс `EXCALIBUR_`**, чтобы не конфликтовать с другими проектами в общих Cloud Secrets:

| Variable | Назначение |
|----------|------------|
| **`EXCALIBUR_PUBLIC_SITE_URL`** | Production WordPress URL (primary) |
| `EXCALIBUR_BLOG_ALLOW_PUBLISH` | `yes` для publish |
| `EXCALIBUR_SITE_BRAND` | Название бренда (опционально) |
| `FTP_*` | Доступы WP (лучше тоже с префиксом, если shared secrets) |

Конфиг: `shared/production-site.json`

## Cloud Secrets (пример)

```bash
EXCALIBUR_PUBLIC_SITE_URL=<https://your-production-wordpress>
EXCALIBUR_BLOG_ALLOW_PUBLISH=yes
```

**Не используй** generic `PUBLIC_SITE_URL` в shared secrets — у других проектов может быть другой URL с тем же именем.

Legacy fallback в скриптах: `PUBLIC_SITE_URL`, `WP_SITE_URL` (только для миграции).

## Permalink

`$EXCALIBUR_PUBLIC_SITE_URL/{slug}/` — без префикса `/blog/`.

## Post-publish gate

```bash
curl -sI "$EXCALIBUR_PUBLIC_SITE_URL/{slug}/" | head -1
```

HTTP 200 обязателен. 404 → verdict **FAIL**.

## Legacy

`published_legacy` в ledger — старые прогоны на mayai.ru.
