# Promotion checklist — B06 ustanovka-claude-code

Дата публикации: YYYY-MM-DD  
Live URL: https://mayai.ru/blog/ustanovka-claude-code/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage + HowTo (theme или plugin)
- [ ] Проверить internal links из статьи (200): `/podklyuchenie-mcp-cursor/` (2×)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Claude Code за 30 минут — или снова command not found?

• Native install (sh/ps1), brew, winget — таблица методов без sudo npm
• CLAUDE.md, `.mcp.json`, hooks и headless `claude -p` для CI
• Чеклист из 11 ошибок: PATH, auth, MCP, лимиты Pro/Max
• Связка с MCP Cursor и Make/n8n для публикации сценариев

Читать: https://mayai.ru/blog/ustanovka-claude-code/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP Cursor) → link to B06 на упоминании Claude Code / terminal MCP
- [ ] Обновить B02 (n8n-агенты) → link to B06 на headless / CI automation (anchor «claude code cli»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «claude code» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 — длинные фразы, не встречаются в B01–B05; B06 уже содержит 2× outbound на B03 `/podklyuchenie-mcp-cursor/`). llms.txt и llms-full.txt обновлены: 6 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker с `--site-base https://mayai.ru` для inbound из B02/B03.
