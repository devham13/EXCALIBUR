# Promotion checklist — B06 nastrojka-claude-code-auto-mode-2026

Дата публикации: 2026-07-10  
Live URL: ${PUBLIC_SITE_URL}/2026/07/10/nastrojka-claude-code-auto-mode-2026/

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
Auto Mode в Claude Code снимает десятки подтверждений на push, тесты и деплой — без bypass permissions.

• Shift+Tab / --permission-mode auto + autoMode.environment в ~/.claude/settings.json
• Проверка правил: claude auto-mode defaults → claude auto-mode config
• 4 слоя защиты: hard_deny, managed deny, hooks, sandbox
• Чеклист 15 пунктов перед unattended-сессией на shared infra

Читать: ${PUBLIC_SITE_URL}/2026/07/10/nastrojka-claude-code-auto-mode-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP Cursor) → link to B06 на упоминании Claude Code / permission mode (если anchor встречается)
- [ ] После publish — перезапустить interlinker с `--site-base ${PUBLIC_SITE_URL} для inbound из B01–B05

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «claude code auto mode» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B01–B05 не встречаются в B06; B06 уже содержит 3 ручные internal links на /dinamicheskie-workflow-claude-code/, /claude-code-hooks-nastrojka-2026/, /nastroyka-claude-code-mcp/). llms.txt обновлён: 6 статей в `memory/blog/llms.txt` и `memory/blog/llms-full.txt`.
