# Promotion checklist — B01 primer-seo-stati

Дата публикации: 2026-07-12  
Live URL: https://mayai.ru/2026/06/19/primer-seo-stati/

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
SEO-статья в 2026 — это не набор ключей, а единый workflow SEO + GEO: от семантики до FAQ и schema.

• Один longread вместо двух проектов: интент, H2-чанки, BlogPosting + FAQPage
• Lead 350–500 знаков, атомарные блоки для нейропоиска
• Чеклист из 15 пунктов перед публикацией

Читать: [URL]
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] B04 → B01: заменить текст «пример SEO-статьи (B01, href после публикации)» на `<a href="/primer-seo-stati/">как писать seo статьи</a>`
- [ ] B05/B02/B03: при упоминании «seo текст» / «longread» — inbound на B01 (interlinker не нашёл автоматических вхождений)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

Indexer (2026-07-12): `interlinker --apply` — 5 статей, 0 автоматических вставок (ключи B01 не совпали с незалинкованным текстом в B02–B05; outbound B01→B04 уже вручную). `llms.txt` / `llms-full.txt` обновлены (5 статей). После publish — перезапустить interlinker для inbound из B04.
