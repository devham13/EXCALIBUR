# Promotion checklist — B01 primer-seo-stati

Дата публикации: 2026-06-19  
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
Статью написали, ключи вставили, а из выдачи никто не кликает? В 2026 SEO без GEO — половина работы.

• Один longread: интент, H2-чанки, BlogPosting + FAQPage
• Lead 350–500 знаков, атомарные блоки для нейропоиска
• Чеклист из 15 пунктов перед публикацией

Читать: [URL]
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

Indexer 2026-06-19: interlinker `--apply` — 0 автоматических вставок (ключи anchor_variants не встречаются в body других статей без существующих ссылок). После publish — ручная перелинковка B04/B05 на `/blog/primer-seo-stati/`. Inline figures: 3× `<figure class="inline-quad">` из cover-registry (H2 якоря синхронизированы после GEO QA).
