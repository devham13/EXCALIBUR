# Promotion checklist — B06 claude-code-hooks-nastrojka-2026

Дата публикации: 2026-07-08  
Live URL: [PRODUCTION_SITE]/2026/07/08/claude-code-hooks-nastrojka-2026/

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
CLAUDE.md не блокирует .env — exit 2 блокирует. Три hooks в settings.json за 20–40 минут.

• PostToolUse prettier на Edit|Write — формат без «напомни модели»
• PreToolUse protect-files.sh — exit 2 на .env и секреты
• Bash guard + проверка через /hooks и тест deny
• Scope: .claude/settings.json в Git для команды

Читать: [PRODUCTION_SITE]/2026/07/08/claude-code-hooks-nastrojka-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP Cursor) → link to B06 на упоминании hooks / Claude Code (anchor «claude code hooks» / «PreToolUse»)
- [ ] Обновить B02 (n8n-агенты) → link to B06 на связке IDE guardrails + automation pipeline

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «claude code hooks» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не встречаются в B01–B05; B06 уже содержит 3× ссылку на B03 `/podklyuchenie-mcp-cursor/`). llms.txt обновлён: 6 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker с `--site-base [PRODUCTION_SITE] для inbound-ссылок из B03/B02.
