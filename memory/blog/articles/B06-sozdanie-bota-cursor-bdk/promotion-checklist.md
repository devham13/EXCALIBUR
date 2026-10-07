# Promotion checklist — B06 sozdanie-bota-cursor-bdk

Дата публикации: 2026-10-07  
Live URL: https://www.meta-journal.ru/2026/10/07/sozdanie-bota-cursor-bdk/

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
🚀 Cursor BDK за вечер: init, evals, GitHub и deploy без webhook!

• BDK — репозиторий с bot/, evals/ и bdk deploy; Automations — prompt в dashboard
• Node 22.13+, bdk dev, smoke-eval, GitHub fixtures → push → validate → running
• Когда нужны hillclimb и GitHub channel — BDK, а не только Automations

Читать: https://www.meta-journal.ru/2026/10/07/sozdanie-bota-cursor-bdk/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

Indexer (2026-10-07): interlinker `--apply` — 0 новых вставок (6 статей в индексе; B03 MCP уже вручную в article.html). `memory/blog/llms.txt` и `llms-full.txt` обновлены с B06.
