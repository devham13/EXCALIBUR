# Promotion checklist — B06 nastrojka-cursor-rules

Дата публикации: 2026-06-20  
Live URL: https://mayai.ru/2026/06/20/nastrojka-cursor-rules/

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
Agent в Cursor отвечает по-разному, пока нет .mdc в .cursor/rules — за 20–40 минут фиксируете general + stack-правила.

• 9 шагов: legacy .cursorrules → mkdir → New Cursor Rule → frontmatter
• Таблица 4 режимов: alwaysApply, globs, description, @rule
• Чек-лист миграции и troubleshooting «молчащих» правил
• Связка Rules + MCP: правила задают стиль, MCP — доступ к сервисам

Читать: https://mayai.ru/2026/06/20/nastrojka-cursor-rules/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B03 (MCP Cursor) → link to B06 на упоминании «cursor rules» / «.mdc»
- [ ] После publish перезапустить interlinker с `--site-base https://mayai.ru` для inbound из B01–B05

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «cursor rules» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 не встречаются вне заголовков/ссылок в B01–B05; B06 уже содержит 2× ссылку на B03 MCP). llms.txt обновлён: 6 статей в `memory/blog/llms.txt` и `memory/blog/llms-full.txt`.
