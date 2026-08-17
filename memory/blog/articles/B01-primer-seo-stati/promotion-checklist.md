# Promotion checklist — B01 primer-seo-stati

Дата публикации: 2026-08-17  
Live URL: https://... (заполнить после publish)

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
Вы тратите часы на seo текст для блога, а в выдаче его обходят страницы с таблицами, FAQ и прямым ответом в первом абзаце?

• Единый workflow SEO + GEO: интент → outline → FAQ → schema
• Lead 350–500 знаков, атомарные H2 для нейропоиска
• Чеклист из 14 пунктов перед публикацией

Читать: [URL]
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

Indexer (2026-08-17): interlinker --apply — 0 автоматических вставок (5 статей в `memory/blog/articles`; ключевые фразы не совпали между источниками). В article.html уже есть ручная ссылка на `/blog/geo-optimizaciya-sajta-2026/`. llms.txt и llms-full.txt обновлены (5 записей).
