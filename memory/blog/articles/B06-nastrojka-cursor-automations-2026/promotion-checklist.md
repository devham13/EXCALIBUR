# Promotion checklist — B06 nastrojka-cursor-automations-2026

Дата публикации: 2026-06-22  
Live URL: https://mayai.ru/blog/nastrojka-cursor-automations-2026/

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
Cursor Automations съедают бюджет — или работают сами?

• Чек-лист за 30–45 мин: trigger → SOP-instructions → MCP → repo scope → Run history
• Сравнение Automations vs Cloud Agent vs subagents — без путаницы и слива usage
• Billing guardrails: spend limit, узкий cron/GitHub-триггер, secrets в dashboard
• Связка с MCP: сначала серверы по гайду B03, потом automation

Читать: https://mayai.ru/blog/nastrojka-cursor-automations-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP в Cursor) → link to B06 на упоминании Automations / cloud agent (anchor «cursor automations»)
- [ ] B06 уже содержит inbound-ссылку на B03 (`/podklyuchenie-mcp-cursor/`)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «cursor automations» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не встречаются в B01–B05; B06 уже линкует B03). llms.txt обновлён: 6 статей в `memory/blog/llms.txt` и `memory/blog/llms-full.txt` (--site-base https://mayai.ru). После publish — перезапустить interlinker для inbound из B03/B02.
