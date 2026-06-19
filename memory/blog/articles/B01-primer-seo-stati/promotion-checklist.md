# Promotion checklist — B01 primer-seo-stati

Дата публикации: 2026-06-19  
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
SEO-статья в 2026 — не набор ключей, а единый workflow SEO + GEO: от семантики до FAQ и schema.

• Один longread вместо двух проектов: интент, H2-чанки, BlogPosting + FAQPage
• Lead 350–500 знаков, атомарные блоки для нейропоиска
• Чеклист из 15+ пунктов перед публикацией

Читать: https://mayai.ru/2026/06/19/primer-seo-stati/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B04 (GEO) → link to B01 на упоминании «seo текст» / «как писать seo статьи»
- [ ] Обновить B05 (контент-завод) → link to B01 на упоминании SEO+GEO workflow
- [ ] Outbound из B01 уже есть: `/geo-optimizaciya-sajta-2026/`, `/podklyuchenie-mcp-cursor/`

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как писать seo статьи» (ручная проверка / Wordstat)

## Notes

Indexer 2026-06-19: `excalibur_blog_interlinker.py --apply` — 0 новых автовставок (5 статей в индексе; якоря B01 не найдены в других HTML без существующих href на slug). Outbound B01→B03/B04 уже в article.html (формат `/slug/`, не `/blog/slug/`). llms.txt и llms-full.txt обновлены (5 статей). После publish — перезапустить interlinker для inbound из B02–B05.
