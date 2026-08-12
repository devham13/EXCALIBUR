# Promotion checklist — B01 primer-seo-stati

Дата публикации: 2026-08-12  
Live URL: /2026/06/19/primer-seo-stati/ (host: EXCALIBUR_PUBLIC_SITE_URL)

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
• Lead 40–70 слов, атомарные блоки для нейропоиска
• Чеклист из 15 пунктов перед публикацией

Читать: https://mayai.ru/blog/primer-seo-stati/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

Indexer (2026-08-12): interlinker --apply — 0 автоматических вставок (slug `geo-optimizaciya-sajta-2026` уже в article.html; anchor_variants B02–B05 не встречаются в тексте B01). Outbound: 1× `/blog/geo-optimizaciya-sajta-2026/`. llms.txt и llms-full.txt обновлены: 5 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker для inbound из B02–B05.
