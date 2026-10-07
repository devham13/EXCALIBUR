# Promotion checklist — B06 cursor-environment-json-cloud-agents

Дата публикации: 2026-10-07  
Live URL: https://www.meta-journal.ru/2026/10/07/cursor-environment-json-cloud-agents/

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
Cursor Cloud Agent держится на .cursor/environment.json: install на Build, start при run, secrets через env — не в репо.

• Триггер Builds и failed vs active snapshot
• Dockerfile без COPY всего репо — типичная ловушка
• Verify на feature branch перед Automations

Читать: https://mayai.ru/blog/cursor-environment-json-cloud-agents/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

Indexer: 0 новых hub-and-spoke ссылок (opportunities_found=0 при 6 статьях в memory); llms.txt обновлён.
