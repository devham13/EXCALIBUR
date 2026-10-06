# Promotion checklist — B01 primer-seo-stati

Дата публикации: 2026-10-06  
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
SEO-статья в 2026 — это не набор ключей, а единый workflow SEO + GEO: от семантики до FAQ и schema.

• Один longread вместо двух проектов: интент, H2-чанки, BlogPosting + FAQPage
• Lead 350–500 знаков, атомарные блоки для нейропоиска
• Чеклист из 15 пунктов перед публикацией

Читать: [URL]
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] После publish — перезапустить interlinker для inbound из B02/B03/B04 на «как писать seo статьи»
- [x] Outbound B01 → B04 (`/blog/geo-optimizaciya-sajta-2026/`, anchor «geo оптимизация») — indexer 2026-10-06

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как писать seo статьи» (ручная проверка / Wordstat)

## Notes

Indexer 2026-10-06: interlinker `--apply` — 1 вставка (B01 → B04). Отчёт: `memory/blog/interlink-suggestions.json`. llms: `memory/blog/llms.txt`, `memory/blog/llms-full.txt` (5 статей).
