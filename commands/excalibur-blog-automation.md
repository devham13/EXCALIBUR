---
description: Excalibur BLOG — полный автономный cron-прогон (Scout → pipeline → publish).
---

# Excalibur BLOG — Automation (cron)

Полный промпт для Cursor Automation: **`shared/excalibur-blog-automation-prompt.md`**

## Быстрый старт

1. Cursor → Automations → New → Schedule
2. Repository: EXCALIBUR
3. **Instructions:** скопируй блок PROMPT из `shared/excalibur-blog-automation-prompt.md`
4. Cloud Secrets:
   - `EXCALIBUR_PUBLIC_SITE_URL`
   - `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`
   - `FTP_*`

## Что делает один прогон

```text
today.py → [Scout если нет P0] → utility gate + research_start
  → research → writer → geo-qa → cover||schema → indexer → publish
  → live check → commit/PR
```

## Параметры триггера

- `publish: no` — без публикации (draft pipeline)
- `EXCALIBUR_TOPIC_ID=B04` — фиксированная тема (Scout пропускается)

## Директор

Оркестратор — **основной агент чата**, не Task. Субагенты — Task(...).

См. также: `commands/excalibur-blog-run.md`, `CLOUD-AUTOMATION.md`
