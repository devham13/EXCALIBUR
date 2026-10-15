# Promotion checklist — B01 primer-seo-stati

Дата публикации: 2026-08-11  
Live URL: [PUBLIC_SITE_URL]/2026/06/19/primer-seo-stati/

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
SEO-статья в 2026 — не поле ключей, а longread с прямым ответом в начале: один workflow SEO + GEO за одну сессию.

• Интент → семантика → H2-чанки → meta/FAQ/schema → чеклист 18 пунктов
• Lead 350–500 знаков, атомарные блоки для нейропоиска
• Таблица SEO vs GEO + island test для каждого H2

Читать: [PUBLIC_SITE_URL]/2026/06/19/primer-seo-stati/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] После publish — перезапустить interlinker для inbound из B02/B03/B04/B05 (если появятся новые anchor matches)
- [x] Outbound B01 → B04: anchor «geo оптимизация» (interlinker --apply, 2026-08-11)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как писать seo статьи» (ручная проверка / Wordstat)

## Notes

Indexer (2026-08-11): interlinker --apply — 1 автоматическая вставка (B01 → B04, anchor «geo оптимизация»). llms.txt и llms-full.txt обновлены: 5 статей в `memory/blog/llms.txt`. Отчёт: `memory/blog/interlink-suggestions.json`.
