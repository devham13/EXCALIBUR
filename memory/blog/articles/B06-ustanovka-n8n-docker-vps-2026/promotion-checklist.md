# Promotion checklist — B06 ustanovka-n8n-docker-vps-2026

Дата публикации: YYYY-MM-DD  
Live URL: https://mayai.ru/blog/ustanovka-n8n-docker-vps-2026/ (заполнить после publish)

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage + HowTo (theme или plugin)
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Webhook CRM и Telegram требуют HTTPS — поднимите n8n на своём VPS за вечер: Docker Compose, Postgres 18, Caddy и рабочие runners.

• Pin n8n 2.42.6 + PostgreSQL 18 в одном compose
• N8N_WEBHOOK_URL и external task runners без облачных лимитов
• 12 пунктов prod-чеклиста и бэкап .env с encryption key
• Дальше — ИИ-агенты (B02) и MCP в Cursor (B03)

Читать: https://mayai.ru/blog/ustanovka-n8n-docker-vps-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] B02 → B06: inbound «установка n8n на VPS» (indexer ✅)
- [ ] B05 → B06 на блоке self-hosted n8n (anchor «установка n8n на vps»)
- [ ] B03 → B06 на связке MCP + self-host (опционально)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «установка n8n на vps» (ручная проверка / Wordstat)

## Notes

Indexer: `excalibur_blog_interlinker.py --apply` — 0 auto (Cyrillic `\b` / длинные anchor_variants); вручную 4 контекстных `<a>` (B06→B02×2, B06→B03×1, B02→B06×1). llms: 6 статей в `memory/blog/llms.txt` и `memory/blog/llms-full.txt` (site-base mayai.ru).
