# Promotion checklist — B06 claude-code-skills-nastrojka-2026

Дата публикации: 2026-07-09  
Live URL: {{PUBLIC_SITE_URL}}/2026/07/09/claude-code-skills-nastrojka-2026/

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
Claude Code без skills — вы каждый раз объясняете одно и то же? За 30–45 минут соберёте первый SKILL.md с auto-invocation.

• Decision tree: skill vs hook vs subagent vs MCP
• 7 шагов: mkdir, frontmatter, /skills, тест A/B, production-поля
• Чеклист из 12 пунктов + лимиты 1536/500 строк
• Связка с hooks, subagents и Make.com для CRM/мессенджеров

Читать: {{PUBLIC_SITE_URL}}/2026/07/09/claude-code-skills-nastrojka-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP Cursor) → link to B06 на упоминании Claude Code / skills (если появится в тексте после publish)
- [x] После publish: interlinker с `--site-base {{PUBLIC_SITE_URL}}` — 0 inbound (anchor_variants B06 не в B01–B05)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «claude code skills» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не встречаются в B01–B05; B06 уже содержит 3× internal links: subagents, hooks, MCP). llms.txt обновлён: 6 статей в `memory/blog/llms.txt` + `memory/blog/llms-full.txt`.
