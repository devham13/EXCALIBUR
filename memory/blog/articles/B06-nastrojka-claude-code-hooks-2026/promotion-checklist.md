# Promotion checklist — B06 nastrojka-claude-code-hooks-2026

Дата публикации: 2026-06-20  
Live URL: https://mayai.ru/nastrojka-claude-code-hooks-2026/

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

```text
Claude Code из коробки не блокирует чтение .env — соберите guardrails за 45–60 минут.

• settings.json: иерархия User/Project/Local + permissions deny для secrets
• 3 hooks: PostToolUse format, PreToolUse block .env, Notification
• CLAUDE.md до 25 строк + чек-лист 15 пунктов перед prod
• Проверка /hooks, hot-reload и claude --safe-mode при сбое

Читать: https://mayai.ru/nastrojka-claude-code-hooks-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP Cursor) → link to B06 на упоминании «Claude Code» / «.mcp.json в Claude Code»
- [ ] Обновить B02 (n8n-агенты) → link to B06 на связке «Claude Code + n8n»

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «claude code» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не встречаются в B01–B05; B06 уже содержит outbound на B02/B03 и mayai.ru MCP). llms.txt обновлён: 6 статей в `memory/blog/llms.txt` и `memory/blog/llms-full.txt`. После publish — перезапустить interlinker с `--site-base https://mayai.ru` для inbound из B02/B03.
