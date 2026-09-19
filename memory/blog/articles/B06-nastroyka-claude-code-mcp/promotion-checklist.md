# Promotion checklist — B06 nastroyka-claude-code-mcp

Дата публикации: 2026-07-07  
Live URL: /2026/07/07/nastroyka-claude-code-mcp/

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
Claude Code за 45 минут: install → MCP → hook без копипаста в чат.

• Native install одной командой (PowerShell / bash) + проверка claude --version
• MCP через claude mcp add или .mcp.json; hooks в .claude/settings.json
• Таблица Claude Code vs Cursor + чеклист pipeline из 12 пунктов
• Связка с n8n/Make: CLI готовит артефакты, сценарии публикуют 24/7

Читать: /2026/07/07/nastroyka-claude-code-mcp/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (Cursor MCP) → link to B06 на упоминании CLI / terminal agent (anchor «claude code» / «настроить claude code»)
- [ ] Обновить B02 (n8n-агенты) → link to B06 на упоминании headless / CI automation

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «claude code» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (keywords B06 «claude code» / anchor_variants не встречаются в B01–B05; B06 уже содержит 2× ручные ссылки на B03 и B02). llms.txt обновлён: 6 статей. После publish — перезапустить interlinker для inbound-ссылок из B03/B02.
