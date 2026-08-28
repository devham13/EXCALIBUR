# Promotion checklist — B06 nastroyka-cursor-automations-2026

Дата публикации: 2026-08-28  
Live URL: https://mayai.ru/2026/08/28/nastroyka-cursor-automations-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
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
Cursor Automations: cron сам, а вы снова копируете prompt? За 30–45 минут — первая Automation с Test run и Run History.

• 5 шагов dashboard: trigger → instructions → tools → repo scope → save
• Cron UTC→MSK: 9:00 по Москве летом = 0 6 * * *
• Repo scope: No repository для брифа, Single для PR-review
• Чеклист 11 пунктов + troubleshooting secrets и webhook
• Связка с MCP (B03) и Make.com для CRM→Telegram

Читать: https://mayai.ru/2026/08/28/nastroyka-cursor-automations-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP) → link to B06 на упоминании Automations/Cloud Agents
- [ ] Обновить B02 (n8n) → link to B06 на упоминании event-driven / cron автоматизации
- [ ] После publish — перезапустить interlinker для inbound из B02/B03/B04

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «cursor automations» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (B06 slug уже в outbound B03; anchor_variants B06 не встречаются в других статьях). llms.txt обновлён: 6 статей в `memory/blog/llms.txt`. schema.jsonld image URL верифицирован: `nastroyka-cursor-automations-2026-cover.png` (cover готов).
