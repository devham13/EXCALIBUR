# Promotion checklist — B06 rag-baza-znaniy-kompanii-2026

Дата публикации: 2026-09-11  
Live URL: https://mayai.ru/blog/rag-baza-znaniy-kompanii-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage + HowTo (theme или plugin)
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
Confluence есть, ChatGPT выдумывает регламент? RAG для базы знаний — ответ по вашим PDF и wiki с цитатой.

• Пилот за 2–4 недели: 50–200 документов, hybrid BM25+vector, rerank top-20→5
• Промпт с цитатами и честным «нет в базе», eval на 20–30 вопросах (RAGAS)
• Таблица стека Chroma/Qdrant/pgvector/Dify + чеклист prod из 12 пунктов
• ~70% качества RAG — retrieval, не модель (Novacom)

Читать: https://mayai.ru/blog/rag-baza-znaniy-kompanii-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить B02 (n8n) → link to B06 на H2 «Подключите память и RAG» (anchor «база знаний RAG» или «как настроить RAG»)
- [ ] Обновить B05 (контент-завод) → link to B06 на упоминании «технология RAG» (anchor «RAG база знаний»)
- [ ] Обновить B04 (GEO) → link to B06 на абзаце про RAG в нейропоиске (anchor «rag система»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «rag база знаний» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker --apply — 0 автоматических вставок (anchor_variants B06 — длинные фразы, не встречаются в B01–B05; slug B06 отсутствует в других статьях). B06 уже содержит outbound на B02 (n8n/Make) и B04 (GEO). llms.txt и llms-full.txt обновлены: 6 статей в `memory/blog/llms.txt`. После publish — перезапустить interlinker с `--site-base https://mayai.ru` для inbound из B02/B05; при необходимости добавить anchor «rag база знаний» в anchor_variants B06 для матча в B02.
