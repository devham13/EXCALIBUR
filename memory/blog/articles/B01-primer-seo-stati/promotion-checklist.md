# Promotion checklist — B01 primer-seo-stati

Дата публикации: 2026-10-04  
Live URL: https://mayai.ru/blog/primer-seo-stati/ (подтвердить после publish)

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
Пишешь SEO для робота — а люди уходят на 3-й абзац? В 2026 один longread = SEO + GEO в одном workflow.

• Lead 350–500 знаков, answer-first в каждом H2, FAQ + BlogPosting/FAQPage
• Чеклист 17 пунктов перед публикацией; объём — по SERP, не по «норме символов»
• Эталон формата — эта статья на mayai.ru

Читать: https://mayai.ru/blog/primer-seo-stati/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как писать seo статьи» (ручная проверка / Wordstat)

## Notes

Indexer (2026-10-04): `excalibur_blog_interlinker.py --apply --blog-dir memory/blog/articles` — загружено 5 статей, 0 автоматических вставок (нет пересечения ключей source→target без self-link). Отчёт: `memory/blog/interlink-suggestions.json`. После publish — при необходимости ручные контекстные ссылки из hub-статей (B04 GEO, B03 MCP). Обновлены `memory/blog/llms.txt`, `memory/blog/llms-full.txt`.
