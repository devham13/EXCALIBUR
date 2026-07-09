# Promotion checklist — B01 primer-seo-stati

Дата публикации: 2026-07-09  
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
SEO-статья в 2026 — не набор ключей, а единый workflow SEO + GEO: от семантики до FAQ и schema.

• Один longread вместо двух проектов: интент, H2-чанки, BlogPosting + FAQPage
• Lead 350–500 знаков, атомарные блоки для нейропоиска
• Чеклист из 15 пунктов перед публикацией

Читать: https://mayai.ru/blog/primer-seo-stati/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B04 → href на B01 (сейчас plain text «пример SEO-статьи» до publish)
- [ ] После publish — перезапустить `excalibur_blog_interlinker.py --apply` для inbound из B02/B05 (anchor «как писать seo статьи», «автоматизация контента»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как писать seo статьи» (ручная проверка / Wordstat)

## Notes

Indexer 2026-07-09: interlinker `--apply` — 0 новых вставок (B01→B04 «geo оптимизацию сайта» уже в article.html; ключи B02/B03/B05 не встречаются в тексте). Outbound: `/` (главная), `/geo-optimizaciya-sajta-2026/`. `memory/blog/llms.txt` и `llms-full.txt` обновлены — 5 статей. Отчёт: `memory/blog/interlink-suggestions.json`.
