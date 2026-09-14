# Promotion checklist — B06 nastrojka-cursor-rules-mdc

Дата публикации: 2026-08-15  
Live URL: https://neurinix.com/2026/08/15/nastrojka-cursor-rules-mdc/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage + HowTo (theme или plugin)
- [ ] Проверить internal links из статьи (200): /podklyuchenie-mcp-cursor/ (×2)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Agent в Cursor каждый раз «забывает» язык и стек? За 30–45 минут настроите Project Rules в .cursor/rules/*.mdc.

• Миграция с legacy .cursorrules → overview + globs
• Таблица 4 режимов: alwaysApply, globs, description, @-mention
• Чеклист из 15 пунктов перед git commit
• Связка с MCP: rules = поведение, MCP = доступ к API

Читать: https://neurinix.com/2026/08/15/nastrojka-cursor-rules-mdc/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP в Cursor) → link to B06 на упоминании «Cursor Agent» / «поведение агента»
- [ ] Обновить B04 (GEO) → link to B06 на упоминании «Cursor» / «AI-агенты в IDE» (если уместно)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «cursor rules» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не встречаются в B01–B05; B06 уже содержит 2× ссылку на B03 /podklyuchenie-mcp-cursor/). llms.txt обновлён: 6 статей в `memory/blog/llms.txt` и `memory/blog/llms-full.txt` (--site-base https://mayai.ru). После publish — перезапустить interlinker с `--site-base https://mayai.ru` для inbound-ссылок из B03/B04.
