# Promotion checklist — B06 cursor-hooks-nastroyka-governance

Дата публикации: 2026-08-26  
Live URL: https://mayai.ru/2026/08/26/cursor-hooks-nastroyka-governance/

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
Cloud Agent без hooks может выполнить rm -rf и force-push — за 30–45 минут соберите repo-first governance в .cursor/hooks.json.

• 7 шагов: hooks.json, block-dangerous.sh, deny + failClosed, audit-log
• Таблица Hooks vs Rules vs MCP allowlist для Cloud Agents
• Cloud-матрица: beforeMCPExecution не работает в VM — MCP через allowlist
• Чеклист из 12 пунктов + FAQ (7 вопросов)

Читать: https://mayai.ru/2026/08/26/cursor-hooks-nastroyka-governance/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP) → link to B06 на упоминании governance/allowlist (anchor «cursor hooks» / «hooks.json»)
- [ ] Обновить B04 (GEO) → link to B06 на упоминании Cloud Agent guardrails (anchor «cursor hooks governance»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как настроить cursor hooks» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не встречаются в B01–B05; B06 уже содержит 3× outbound на B03 `/podklyuchenie-mcp-cursor/`). llms.txt и llms-full.txt обновлены: 6 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker с `--site-base https://mayai.ru` для inbound-ссылок из B03/B04.
