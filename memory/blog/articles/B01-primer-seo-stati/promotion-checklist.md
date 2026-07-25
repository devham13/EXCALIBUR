# Promotion checklist — B01 primer-seo-stati

Дата публикации: 2026-07-11  
Live URL: /2026/06/19/primer-seo-stati/ (на PUBLIC_SITE_URL)

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
Вы пишете seo текст для блога, а в Яндекс Нейро цитируют чужие фрагменты? Проблема не в «магических ключах», а в отсутствии системы.

• Единый workflow SEO + GEO из 9 шагов: от Wordstat до чеклиста на 18 пунктов
• Answer-first блоки, FAQ + schema BlogPosting + FAQPage
• Таблица SEO vs GEO и longread 8 500–9 500 знаков для how-to

Читать: https://mayai.ru/blog/primer-seo-stati/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как писать seo статьи» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 1 автоматическая вставка (B01 → B04, anchor «geo оптимизация» в шаге 2 workflow). Inbound из B04 ожидается после перезапуска post-publish. llms.txt и llms-full.txt обновлены: 5 статей в `memory/blog/llms.txt`. site-base: https://mayai.ru.
