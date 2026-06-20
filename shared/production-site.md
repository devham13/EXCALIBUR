# Excalibur BLOG — production site

## Канонический сайт публикации

| Поле | Источник |
|------|----------|
| **Production URL** | env `PUBLIC_SITE_URL` (Cloud Secrets / `memory/site.env.local`) |
| **Permalink** | `$PUBLIC_SITE_URL/{slug}/` |
| **Конфиг** | `shared/production-site.json` |

## Cloud Secrets / env

```bash
PUBLIC_SITE_URL=<https://your-production-wordpress>
EXCALIBUR_BLOG_ALLOW_PUBLISH=yes
FTP_*
```

**Обязательно:** `PUBLIC_SITE_URL` = **production** WordPress, не staging и не legacy-домены.

## Скрипты

- `excalibur_blog_link_verify.py --site-base $PUBLIC_SITE_URL`
- `excalibur_blog_interlinker.py` / `excalibur_blog_llms_generator.py` — URL из `excalibur_site_config.py`
- Permalink: `/{slug}/` (без `/blog/`)

## Post-publish gate

```bash
curl -sI "$PUBLIC_SITE_URL/{slug}/" | head -1
```

HTTP 200 обязателен. 404 → verdict **FAIL**.

## Legacy

`published_legacy` в ledger — старые прогоны на mayai.ru.
