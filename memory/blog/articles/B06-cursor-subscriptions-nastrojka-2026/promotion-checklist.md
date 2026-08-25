# Promotion checklist — B06 cursor-subscriptions-nastrojka-2026

Дата публикации: YYYY-MM-DD  
Live URL: https://mayai.ru/cursor-subscriptions-nastrojka-2026/

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

```text
PR упал CI, а вы в Slack? Cursor Subscriptions (фича cloud agents, не тариф Pro) ставит «будильник» на pull request и Slack-тред — agent просыпается на событие.

• GitHub + Slack + spend limit за 30–45 минут
• Subscription vs Automations: одна длинная задача vs новый run на каждый trigger
• /goal, /autopilot, wake-on-reply в Slack-треде до 180 дней
• Security checklist: 12 пунктов перед production

Читать: https://mayai.ru/cursor-subscriptions-nastrojka-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP) → inbound link на B06 при упоминании cloud agents / Subscriptions
- [ ] Обновить B02 (n8n-агенты) → link to B06 на связке cloud agents + автоматизация

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «cursor subscriptions» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не встречаются в B01–B05; B06 уже содержит 2× ссылку на B03 `/podklyuchenie-mcp-cursor/`). llms.txt обновлён: 6 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker с `--site-base https://mayai.ru` для inbound-ссылок из B02/B03.
