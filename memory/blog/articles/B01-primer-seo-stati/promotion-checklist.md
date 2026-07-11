# Promotion checklist — B01 primer-seo-stati

Дата публикации: 2026-07-11  
Live URL: /2026/06/19/primer-seo-stati/ (full URL in wp-publish-result.json)

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
• Чеклист из 16 пунктов перед публикацией

Читать: /2026/06/19/primer-seo-stati/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B04 → link to B01 на упоминании «пример SEO-статьи» (href после publish)
- [ ] После publish — перезапустить `excalibur_blog_interlinker.py --apply --site-base https://mayai.ru` для inbound из B02/B03/B05

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как писать seo статьи» (ручная проверка / Wordstat)

## Notes

Indexer (2026-07-11): interlinker --apply — 0 автоматических вставок (5 статей в `memory/blog/articles`; slug `geo-optimizaciya-sajta-2026` уже в B01, anchor_variants B02/B03/B05 не встречаются в тексте B01). Outbound в B01: `/` (главная блога), `/geo-optimizaciya-sajta-2026/` (B04). llms.txt и llms-full.txt обновлены: 5 статей. Отчёт: `memory/blog/interlink-suggestions.json`.
