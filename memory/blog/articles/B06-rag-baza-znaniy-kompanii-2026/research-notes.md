# Research notes — B06 «Как настроить RAG для базы знаний компании: пошаговое руководство в 2026»

**topic_id:** B06  
**slug:** rag-baza-znaniy-kompanii-2026  
**article_mode:** B (how-to + workflow)  
**research_date:** 2026-09-11  
**disclaimer:** Все даты, версии и статистика проверены на 11.09.2026.

---

## 1. SERP-обзор (WebSearch, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cloud.ru/blog/rag-rukovodstvo-2026](https://cloud.ru/blog/rag-rukovodstvo-2026) | Полное руководство (сент. 2026) | Pipeline 4 шага, failure points, Anthropic contextual retrieval, ruMTEB, Managed RAG | Мало пошагового «сделай сам» для SMB; продаёт Cloud.ru | Цифры рынка без ссылки на Just AI; vendor-lock Managed RAG |
| 2 | [novacom.ru/blog/rag-system-implementation-guide](https://novacom.ru/blog/rag-system-implementation-guide) | Enterprise how-to (май 2026) | Чанкинг, hybrid+rerank, eval 50–100 пар, стеки PoC→prod, 152-ФЗ | Длинный dev-ориентированный текст; мало no-code | Таблицы цен API без даты проверки writer |
| 3 | [mayai.ru/rag-baza-znanij-kompanii](https://mayai.ru/rag-baza-znanij-kompanii/) | Workflow 7 шагов (июнь 2026) | Пилот 2–4 нед., golden dataset, ACL, hybrid+rerank, эскалация | Пересекается с нашей темой; CTA на Make-курс | Копировать структуру 1:1; Wordstat-цифры без MCP-проверки |
| 4 | [nbmit.ru/blog/ai/rag-knowledge-base-preparation](https://nbmit.ru/blog/ai/rag-knowledge-base-preparation) | Чек-лист подготовки KB | Structure-aware chunking, 512/128 старт, ACL до генерации, версии | Узкий фокус на ingestion, нет стека | Microsoft 512/128 как «универсальная норма» без eval |
| 5 | [ai.low-light.ru/blog/rag-sistemy-korporativnaya-baza-znaniy-2026](https://ai.low-light.ru/blog/rag-sistemy-korporativnaya-baza-znaniy-2026/) | Гайд реализации 2026 | Citations, ACL, eval | Общие формулировки | Sales-CTA агентства |
| 6 | [woghan.ru/articles/rag-dlya-korporativnyh-dokumentov-dogovory-wiki-tikety-prava](https://woghan.ru/articles/rag-dlya-korporativnyh-dokumentov-dogovory-wiki-tikety-prava/) | Корп. документы + права | ACL до retrieval, метаданные owner/updated_at, тикеты vs wiki | Нет пошагового pipeline | — |
| 7 | [habr.com/ru/articles/1070662](https://habr.com/ru/articles/1070662/) | RAG «под капотом» (2026) | top_k_retrieve 30–50, top_k_final 3–5, cross-encoder | Технично для не-dev аудитории | Код 1:1 без «на пальцах» |
| 8 | [qdrant.tech/documentation/tutorials-basics/reranking-hybrid-search](https://qdrant.tech/documentation/tutorials-basics/reranking-hybrid-search/) | Официальный tutorial Qdrant | Dense+sparse+RRF+ColBERT rerank, prefetch pattern | Англ., без 152-ФЗ / RU compliance | — |

**Паттерн SERP:** топ — «RAG база знаний 2026» longread + пошаговые гайды (nedigital, mayai, novacom). Отдельный кластер — hybrid search + reranking (англ. reference 2026). Мало материалов, которые **сводят в один workflow**: аудит → chunking → hybrid+rerank → промпт → eval → канал с эскалацией **на русском для no-code/low-code**.

**Intent:** how_to — пользователь хочет **настроить RAG** на корпоративных документах, а не «узнать что такое RAG». Вторичный intent: hybrid vs vector-only, размер чанков, Qdrant/pgvector/Dify, обновление базы.

**Пробел для «Ковчег»:** практический workflow за 2–4 недели пилота; честный стек (PoC Chroma → prod Qdrant/pgvector); связка с n8n/Make для re-index; eval на 20–30 вопросах; 152-ФЗ без vendor-lock.

---

## 2. Яндекс Wordstat

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в среде Cloud Agent (инструмент `wordstat_get_top_requests` недоступен). Точные объёмы спроса из API **не получены**.

**Вторичные данные (цитировать с оговоркой «по данным Вордстат, июнь 2026, источник mayai.ru — не верифицировано MCP):**

| Фраза | Показы/мес | Источник |
|-------|------------|----------|
| rag база знаний | 419 | [mayai.ru/rag-baza-znanij-kompanii](https://mayai.ru/rag-baza-znanij-kompanii/) |
| rag система | 2 125 | [mayai.ru/rag-baza-znanij-kompanii](https://mayai.ru/rag-baza-znanij-kompanii/) |
| rag как настроить | 53 | [mayai.ru/rag-baza-znanij-kompanii](https://mayai.ru/rag-baza-znanij-kompanii/) |
| база знаний для ии агента | 47 | [mayai.ru/rag-baza-znanij-kompanii](https://mayai.ru/rag-baza-znanij-kompanii/) |

**Экспертная семантика (без цифр):** кластер растёт вместе с корпоративными ИИ-агентами; primary «rag база знаний» — mid-tail; head «rag система» — шире, но размывает intent. Writer: primary в H1/lead; «rag система», «как настроить rag», «корпоративная база знаний ии», «hybrid search reranking» — в H2/H3 и FAQ.

### LSI для writer (SERP + secondary queries)

- rag pipeline, ingestion, chunking, embeddings, vector store  
- hybrid search, BM25, RRF, cross-encoder rerank, top-k  
- golden dataset, RAGAS, faithfulness, context precision  
- ACL, 152-ФЗ, YandexGPT, GigaChat, pgvector, Qdrant, ChromaDB, Dify  
- re-index, cron, n8n, Confluence, Notion, PDF OCR  
- «нет в базе», citations, human-in-the-loop, эскалация  

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| RAG-pipeline: индексация (offline) + retrieval + augmentation + generation (online) | [cloud.ru/blog/rag-rukovodstvo-2026](https://cloud.ru/blog/rag-rukovodstvo-2026) | 07.09.2026 | да |
| Чанки обычно 200–1000 токенов; Microsoft Azure рекомендует 500–700 для большинства сценариев | [cloud.ru/blog/rag-rukovodstvo-2026](https://cloud.ru/blog/rag-rukovodstvo-2026) | 07.09.2026 | да |
| Чанки <100 токенов теряют контекст; >2000 — размывают релевантность | [cloud.ru/blog/rag-rukovodstvo-2026](https://cloud.ru/blog/rag-rukovodstvo-2026) | 07.09.2026 | да |
| Anthropic contextual retrieval: неудачные top-20 извлечения 5,7% → 3,7% (−35%) | [cloud.ru/blog/rag-rukovodstvo-2026](https://cloud.ru/blog/rag-rukovodstvo-2026) | 07.09.2026 | да |
| Контекстные embeddings + BM25 + reranker: неудачи до 1,9% (−67% vs baseline) | [cloud.ru/blog/rag-rukovodstvo-2026](https://cloud.ru/blog/rag-rukovodstvo-2026) | 07.09.2026 | да |
| >70% крупных российских компаний используют generative AI (исследование Just AI/Onside, дек. 2025) | [cloud.ru/blog/rag-rukovodstvo-2026](https://cloud.ru/blog/rag-rukovodstvo-2026) | 07.09.2026 | да |
| Рынок generative AI в РФ ~58 млрд ₽ в 2025 vs ~13 млрд годом ранее (Just AI/Onside, март 2026) | [cloud.ru/blog/rag-rukovodstvo-2026](https://cloud.ru/blog/rag-rukovodstvo-2026) | 07.09.2026 | да |
| Managed RAG Cloud.ru: max файл 25 МБ; PDF без OCR (сканы не обрабатываются) | [cloud.ru/blog/rag-rukovodstvo-2026](https://cloud.ru/blog/rag-rukovodstvo-2026) | 07.09.2026 | да |
| Качество RAG на ~70% определяется retrieval (Novacom) | [novacom.ru/blog/rag-system-implementation-guide](https://novacom.ru/blog/rag-system-implementation-guide) | 22.05.2026 | да |
| Рекомендуемый chunk: 500–1000 токенов; overlap 50–200 (10–20%) | [novacom.ru/blog/rag-system-implementation-guide](https://novacom.ru/blog/rag-system-implementation-guide) | 22.05.2026 | да |
| Reranking улучшает качество retrieval на 10–25% | [novacom.ru/blog/rag-system-implementation-guide](https://novacom.ru/blog/rag-system-implementation-guide) | 22.05.2026 | да |
| Golden dataset: 50–100 пар (вопрос, эталон, источник) | [novacom.ru/blog/rag-system-implementation-guide](https://novacom.ru/blog/rag-system-implementation-guide) | 22.05.2026 | да |
| PoC стек: LangChain + ChromaDB + text-embedding-3-small; 2–3 недели | [novacom.ru/blog/rag-system-implementation-guide](https://novacom.ru/blog/rag-system-implementation-guide) | 22.05.2026 | да |
| OpenAI text-embedding-3-small: $0.02/1M токенов | [novacom.ru/blog/rag-system-implementation-guide](https://novacom.ru/blog/rag-system-implementation-guide) | 22.05.2026 | да |
| Cohere Rerank: ~$1/1000 запросов | [novacom.ru/blog/rag-system-implementation-guide](https://novacom.ru/blog/rag-system-implementation-guide) | 22.05.2026 | да |
| Пилот RAG: 50–200 файлов, один сценарий, 2–4 недели | [mayai.ru/rag-baza-znanij-kompanii](https://mayai.ru/rag-baza-znanij-kompanii/) | 16.06.2026 | да |
| Golden dataset пилота: 20–30 реальных вопросов | [mayai.ru/rag-baza-znanij-kompanii](https://mayai.ru/rag-baza-znanij-kompanii/) | 16.06.2026 | да |
| Hybrid BM25 + vector: +5–10% на корп. формулировках (May AI) | [mayai.ru/rag-baza-znanij-kompanii](https://mayai.ru/rag-baza-znanij-kompanii/) | 16.06.2026 | да |
| Top-20 → rerank → top-3–5 в LLM — типовой pipeline | [mayai.ru/rag-baza-znanij-kompanii](https://mayai.ru/rag-baza-znanij-kompanii/) | 16.06.2026 | да |
| Стартовый chunk для RU корп. текста: 256–512 токенов, overlap 10–20% | [mayai.ru/rag-baza-znanij-kompanii](https://mayai.ru/rag-baza-znanij-kompanii/) | 16.06.2026 | да |
| NBM-IT: старт 512 токенов + 128 overlap (Microsoft reference) | [nbmit.ru/blog/ai/rag-knowledge-base-preparation](https://nbmit.ru/blog/ai/rag-knowledge-base-preparation) | 2026 | да |
| ACL проверять до генерации, не только в промпте | [nbmit.ru/blog/ai/rag-knowledge-base-preparation](https://nbmit.ru/blog/ai/rag-knowledge-base-preparation) | 2026 | да |
| Права применять до поиска и до передачи текста в LLM | [woghan.ru/articles/rag-dlya-korporativnyh-dokumentov-dogovory-wiki-tikety-prava](https://woghan.ru/articles/rag-dlya-korporativnyh-dokumentov-dogovory-wiki-tikety-prava/) | 2026 | да |
| RRF: fusion по рангам, не по raw scores (BM25 vs vector) | [ubuntu.com/blog/hybrid-search-and-reranking-a-deeper-look-at-rag](https://ubuntu.com/blog/hybrid-search-and-reranking-a-deeper-look-at-rag) | 2026 | да |
| Hybrid: top 50–100 кандидатов → rerank → top 5–10 в LLM | [ubuntu.com/blog/hybrid-search-and-reranking-a-deeper-look-at-rag](https://ubuntu.com/blog/hybrid-search-and-reranking-a-deeper-look-at-rag) | 2026 | да |
| RRF default k=60; k=30–40 для top-1 precision | [digitalapplied.com/blog/hybrid-search-bm25-vector-reranking-reference-2026](https://www.digitalapplied.com/blog/hybrid-search-bm25-vector-reranking-reference-2026) | 2026 | да |
| top_k_retrieve 30–50 для reranker; top_k_final 3–5 в промпт LLM | [habr.com/ru/articles/1070662](https://habr.com/ru/articles/1070662/) | 2026 | да |
| HNSW vs IVFFlat: HNSW — default для RAG; IVFFlat при >5M векторов и статичной базе | [ai-uchi.ru/guides/rag-na-praktike-langchain-pgvector-poiskovaia-sistema](https://ai-uchi.ru/guides/rag-na-praktike-langchain-pgvector-poiskovaia-sistema/) | 2026 | да |
| chunk_size=1000, overlap=200 — старт для pgvector/LangChain | [ai-uchi.ru/guides/rag-na-praktike-langchain-pgvector-poiskovaia-sistema](https://ai-uchi.ru/guides/rag-na-praktike-langchain-pgvector-poiskovaia-sistema/) | 2026 | да |
| Seven Failure Points RAG (Barnett et al., CAIN 2024): большинство сбоев на retrieval | [cloud.ru/blog/rag-rukovodstvo-2026](https://cloud.ru/blog/rag-rukovodstvo-2026) | 07.09.2026 | да |
| Lost in the Middle (Liu et al., TACL 2024): точность падает, если ключевой факт в середине длинного контекста | [cloud.ru/blog/rag-rukovodstvo-2026](https://cloud.ru/blog/rag-rukovodstvo-2026) | 07.09.2026 | да |
| <2,5% сложных неструктурированных задач завершаются без человека (fact-bank) | [mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 11.06.2026 | да |

**Не использовать без первичника:** «Recall@10 ≥ 90%» (AGmind via mayai — ориентир, не гарантия); «85–95% с rerank» (mayai); точные Wordstat-цифры как «официальные» без MCP.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **2–4 недели пилота** пройти полный workflow: **аудит 50–200 документов → chunking+метаданные → индекс → hybrid search + rerank → промпт с цитатами → eval 20–30 вопросов → канал с эскалацией**.

**Почему отличается от конкурентов:**
- Cloud.ru / Habr — теория и облако, мало «сделай сам» для ops/no-code.
- Novacom — enterprise-dev, без связки n8n/Make для re-index.
- Mayai — близкий workflow, но наш материал расширяет **hybrid+rerank** и **сравнение стека** (Dify / Qdrant / pgvector) по карточке B06.

**Tone:** по-человечески; embedding, rerank, RRF — «на пальцах». Без «RAG решит всё» и без FUD.

**H2-каркас (из blog-topics.md + research):**
1. Аудит документов: дубликаты, версии, ACL, выбор источников (Confluence, Notion, Drive)
2. Chunking и embeddings: размер чанков, overlap, модели для RU
3. Hybrid search + reranking: vector + BM25, top-k, cross-encoder
4. Промпт RAG: цитирование, temperature 0, «нет в базе»
5. Eval и мониторинг: RAGAS, 20–50 контрольных вопросов, re-index SLA
6. Сравнение стека: Dify, Qdrant/pgvector, low-code vs self-hosted

**Internal links (карточка):** `/avtomatizaciya-n8n-ai-agents/`, `/geo-optimizaciya-sajta-2026/`

---

## 5. Workflow-схема (для writer)

```
Документы → Парсинг/OCR → Чанкинг + метаданные → Embed → Vector DB (+ BM25 index)
                                                              ↓
Запрос → ACL-фильтр → Hybrid search (vector + BM25) → RRF → Rerank top-20→5
                                                              ↓
System prompt + top-3–5 чанков + вопрос → LLM → Ответ + citations → Log / 👍👎
                                                              ↓
Re-index (cron/webhook) ←── owner базы + golden dataset eval каждый спринт
```

---

## 6. Comparison-матрица стека (черновик)

| Критерий | ChromaDB (PoC) | Qdrant | pgvector | Dify (managed workflow) |
|----------|----------------|--------|----------|-------------------------|
| Старт | pip, zero config | Docker / cloud | Ext. PostgreSQL | SaaS / self-host |
| Hybrid + rerank | Вручную / LangChain | Native sparse+dense+RRF | SQL BM25 + vector + RRF | UI pipeline, меньше кода |
| ACL | App-layer фильтры | Payload filters | Row-level + WHERE | Workspace roles |
| 152-ФЗ / on-prem | Self-host | Self-host | Yandex Managed PG | Self-host edition |
| Когда выбрать | Пилот до ~1k docs | Prod, hybrid native | Уже есть PostgreSQL | Быстрый MVP без DevOps |

**Позиция автора:** PoC на Chroma/LangChain за выходные; prod — Qdrant или pgvector + n8n cron для re-index; Dify — если команда без Python и нужен UI за дни.

---

## 7. FAQ-кандидаты (из карточки + research)

1. **Сколько документов нужно для первого RAG?** — 50–200 актуальных файлов на один сценарий, не вся компания.
2. **Чем hybrid search лучше vector-only?** — BM25 ловит артикулы/номера договоров; vector — синонимы; RRF объединяет.
3. **Как обновлять базу без потери качества?** — re-index по webhook/cron, hash файла, версии индекса, прогон golden dataset.
4. **Какой размер чанка для русского регламента?** — старт 256–512 или 500–700 токенов; проверить на своих 20–30 вопросах.
5. **Нужен ли reranker?** — да, если baseline промахивается; +10–25% по Novacom; top-20 → rerank → top-3–5.
6. **Как не допустить утечки закрытых документов?** — ACL-фильтр в query vector DB до LLM.
7. **RAG или fine-tuning?** — RAG для меняющихся регламентов; fine-tuning для стиля/формата.

---

## 8. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «RAG для базы знаний» 40–60 слов | Lead | «RAG для базы знаний — …» |
| Workflow-схема A→B→C | После lead | ASCII / mermaid |
| Таблица стека | H2-6 | Comparison + «выбирай если» |
| Чеклист prod (10+ пунктов) | Финал H2-5 | Island-test actionable |
| FAQ 5–7 | Конец | Ответы-действия |

**Целевые формулировки:** «rag база знаний», «как настроить rag», «rag система», «hybrid search reranking», «корпоративная база знаний ии».

---

## 9. Риски для writer

- Wordstat-цифры — только с пометкой «по mayai.ru / не MCP» или опустить.
- Не копировать mayai/novacom 1:1.
- Цифры рынка 58 млрд / 70% — только со ссылкой на cloud.ru → Just AI.
- Min **5 нумерованных шагов** + **чеклист 10+** + workflow-схема (utility gate статьи).
- Без article.html на этапе research.

---

## 10. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за 2–4 недели пилота соберёт RAG на корпоративных документах: проведёт аудит и ACL, настроит chunking и индекс, включит hybrid search с rerank, напишет промпт с цитатами, прогонит 20–30 контрольных вопросов и подключит канал (чат/Telegram) с эскалацией к человеку.

**action_outline (для writer):**

1. **Выбрать один сценарий** (FAQ поддержки, HR или продукт) и собрать 50–200 актуальных документов; назначить owner базы; разметить ACL (отдел, роль).
2. **Подготовить корпус:** парсинг PDF/DOCX (OCR для сканов), dedup, structure-aware chunking (256–512 или 500–700 токенов, overlap 10–20%), метаданные file_name, section, updated_at, acl.
3. **Выбрать стек PoC:** ChromaDB или Qdrant + embedding (BGE-M3 / text-embedding-3-small); зафиксировать модель до индексации; для 152-ФЗ — YandexGPT/GigaChat + on-prem vector DB.
4. **Построить ingestion:** embed → vector store; настроить cron/webhook (n8n/Make) на re-index при изменении файла; хранить hash и версию индекса.
5. **Настроить retrieval:** hybrid vector + BM25 → RRF (k≈60) → rerank top-20 → top-3–5; ACL-фильтр в query; порог similarity для отсечения шума.
6. **Промпт и генерация:** system prompt «только по контексту, нет данных — скажи, цитируй источник»; temperature 0; логировать fallback «не нашёл».
7. **Eval:** golden dataset 20–30 (пилот) / 50–100 (prod) вопросов; метрики faithfulness, context precision (RAGAS); прогон после каждого изменения chunk/top-k.
8. **Канал и prod:** Telegram/виджет/Slack; 👍/👎; эскалация на юридические/HR темы; мониторинг latency и drift eval раз в спринт.

---

## 11. Handoff writer

- **Primary query:** rag база знаний  
- **Secondary:** rag система, как настроить rag, корпоративная база знаний ии, hybrid search reranking  
- **Конкуренты для diff:** cloud.ru, novacom, mayai (не копировать структуру)  
- **Обязательные блоки:** workflow-схема, comparison стека, чеклист prod, FAQ 5–7  
- **Fact-bank:** human-in-the-loop <2,5% — можно в блок эскалации  
