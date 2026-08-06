# Promotion checklist — B01 primer-seo-stati

Дата публикации: 2026-08-06  
Live URL: https://mayai.ru/blog/primer-seo-stati/ (заполнить после publish)

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

Читать: https://mayai.ru/blog/primer-seo-stati/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B04 → href `/blog/primer-seo-stati/` (сейчас plain text «пример SEO-статьи (B01)»)
- [ ] После publish — перезапустить `excalibur_blog_interlinker.py --apply` для inbound из B02–B05

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

Indexer 2026-08-06: 5 статей в corpus, 0 auto interlink opportunities (keyword overlap не совпал с regex). B01 article.html — 2 manual internal links: `/` (главная), `/blog/geo-optimizaciya-sajta-2026/`. llms.txt + llms-full.txt обновлены (5 статей, mayai.ru).
