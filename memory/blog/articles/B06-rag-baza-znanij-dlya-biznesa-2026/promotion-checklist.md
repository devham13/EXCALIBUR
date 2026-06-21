# Promotion checklist — B06 rag-baza-znanij-dlya-biznesa-2026

Дата публикации: 2026-06-21  
Live URL: https://mayai.ru/rag-baza-znanij-dlya-biznesa-2026/

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

```text
ChatGPT не видит ваши PDF — а менеджеры поддержки отвечают на одни и те же вопросы из регламентов?

RAG база знаний решает это иначе: перед ответом система ищет фрагменты в ваших документах и отвечает с цитатой.

Главное из гайда:
• MVP на n8n + Qdrant/pgvector: ingestion, hybrid BM25+vector, rerank и golden set 20–30 вопросов.
• Таблица Qdrant vs pgvector — когда брать отдельный search-сервис, а когда Postgres рядом с CRM.
• Webhook-бот с HITL: эскалация человеку, если rerank не уверен — без этого ~40% AI-проектов срываются.

Пошаговое руководство без ML-команды:
Читать: https://mayai.ru/rag-baza-znanij-dlya-biznesa-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

Interlinker: 0 auto-injected links (keywords B06 не совпали в теле других статей; writer уже добавил 2 internal: n8n, MCP). После publish — рассмотреть ручную ссылку из B02 §RAG и B05 §RAG.
