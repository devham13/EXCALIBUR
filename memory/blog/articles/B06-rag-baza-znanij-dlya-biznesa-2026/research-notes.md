# Research notes — B06 «Как настроить RAG базу знаний для бизнеса: пошаговое руководство 2026»

**topic_id:** B06  
**slug:** rag-baza-znanij-dlya-biznesa-2026  
**article_mode:** B (how-to / workflow)  
**research_date:** 2026-06-21  
**disclaimer:** Все даты, версии и статистика проверены на 21.06.2026.

---

## 1. SERP-обзор (WebSearch, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [wildbots.ru/.../rag-agent-n8n-qdrant](https://wildbots.ru/ru/blog/rag-agent-po-korporativnoi-baze-znanii-arkhitektura-na-n8n-qdrant) | Практический longread (2026) | Ingestion + retrieval, чанкинг 500–1000 tok, hybrid RRF, reranker bge-reranker-v2-m3, multitenancy Qdrant, observability | DevOps-уровень; мало «для владельца без кода»; нет eval golden set пошагово | Перегруз YAML/API Qdrant; копировать структуру 1:1 |
| 2 | [ai.low-light.ru/.../rag-sistemy-korporativnaya-baza-znaniy-2026](https://ai.low-light.ru/blog/rag-sistemy-korporativnaya-baza-znaniy-2026/) | Enterprise-гайд | 5 слоёв архитектуры, BM25+vector+rerank, цифры бюджета/сроков | Фокус на кастом от 800 тыс ₽; слабый no-code/n8n блок | Цены железа «от 25 млн ₽» без контекста MVP |
| 3 | [habr.com/ru/articles/905076](https://habr.com/ru/articles/905076/) | Опытный how-to | Golden questions, минимальный сабсет данных, чистка устаревших Wiki, промпт-тюнинг | Нет стека 2026 (Qdrant/pgvector), нет n8n workflow | Устаревший стек OpenAI Assistants как единственный путь |
| 4 | [habr.com/ru/companies/amvera/articles/930250](https://habr.com/ru/companies/amvera/articles/930250/) | n8n + Qdrant tutorial | Пошагово: Form → Qdrant Vector Store → Recursive Splitter (400, overlap ¼) → AI Agent + tool | Привязка к Amvera Cloud; нет hybrid/rerank/eval | Рекламный хвост хостинга |
| 5 | [habr.com/ru/companies/flowwow/articles/1032120](https://habr.com/ru/companies/flowwow/articles/1032120/) | Enterprise-кейс n8n | 10 000+ документов, self-hosted n8n, локальный RAG в 5,5× дешевле коробки, human feedback кнопка | Нет воспроизводимого рецепта чанкинга/eval | Внутренняя архитектура без универсальных шагов |
| 6 | [n8n.io/workflows/11468](https://n8n.io/workflows/11468-build-a-rag-agent-with-n8n-qdrant-and-openai/) | Официальный шаблон n8n | Канон pipeline: Google Drive → chunk → embed → Qdrant → AI Agent chat | Single-vector RAG; нет BM25/rerank; EN-first | Сухой перевод template без бизнес-кейса |
| 7 | [promaren.ru/.../optimizaciya-rag-chunking](https://promaren.ru/blog/2026/04/05/optimizaciya-rag-v-2026-effektivnye-chunking-strategii/) | Chunking deep-dive | Стратегии semantic/recursive/metadata-aware, RAGAS-цикл, overlap 10–15% | Часть цифр без первичника («3 из 5», «+60%») | Непроверенные vendor-метрики в текст |
| 8 | [habr.com/ru/articles/989000](https://habr.com/ru/articles/989000/) | Обзор «что такое RAG» | Архитектуры, failure modes, серия с кодом | Режим A: мало actionable шагов для бизнеса | Длинное «вообще про RAG» без workflow |

**Паттерн SERP:** топ — либо enterprise-продажи (low-light, integrators), либо dev-туториалы (Habr, Wildbots, n8n template), либо conceptual (Habr 989000). Запрос «rag qdrant n8n» закрыт точечно (Amvera, Wildbots, workflow 11468), но **редко в одной статье**: чанкинг → hybrid → rerank → **golden set eval** → **webhook-бот с эскалацией**.

**Intent:** `how_to` — собрать рабочую RAG-базу на своих документах и подключить к поддержке/онбордингу. Вторичный: выбор Qdrant vs pgvector, self-hosted vs облако, 152-ФЗ/периметр.

**Пробел для Excalibur BLOG:** единый **бизнес-workflow** (аудит документов → MVP на n8n+Qdrant/pgvector → eval 20–30 вопросов → бот в Telegram/сайт с цитатами и **human-in-the-loop**), язык для РОП/ops без ML-бэкграунда, связка с CRM-автоматизацией (кластер блога).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` недоступен в среде прогона (ListMcpResources: server not found). Точные показы/мес **не получены**. Обновите токен через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (без цифр спроса — только для LSI writer)

| Кластер | Фразы для H2/H3 и FAQ |
|---------|------------------------|
| Head | rag база знаний, rag система, rag для бизнеса |
| Setup | настройка rag системы, корпоративная база знаний rag, построение rag |
| Stack | rag qdrant, pgvector rag, hybrid search rag, reranker rag |
| No-code | rag n8n, n8n qdrant openai, векторная база знаний |
| Quality | chunking rag, eval rag, ragas faithfulness, golden set |
| Biz | база знаний для поддержки, rag регламенты, rag онбординг |

**SEO-стратегия:** primary «rag база знаний» в H1/lead; secondary из карточки темы + LSI «rag qdrant n8n», «pgvector», «гибридный поиск», «reranker», «faithfulness».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| RAG: LLM ищет релевантные фрагменты во внешней базе и генерирует ответ с опорой на них, а не только из весов модели | [habr.com/ru/articles/989000](https://habr.com/ru/articles/989000/) | 2026 | да |
| Загрузка всей Wiki (~3000 док.) ухудшила качество vs узкий раздел SQA; после фильтра «обновлялось 2 года» осталось ~400 док. — качество выросло | [habr.com/ru/articles/905076](https://habr.com/ru/articles/905076/) | 2026 | да |
| Для Wiki-RAG ставили temperature=0, чтобы LLM не «додумывала» | [habr.com/ru/articles/905076](https://habr.com/ru/articles/905076/) | 2026 | да |
| Flowwow: >10 000 единиц документации; кастомная разработка оценивалась в 6–9 мес., n8n-сборка — 2,5 мес. | [habr.com/ru/companies/flowwow/articles/1032120](https://habr.com/ru/companies/flowwow/articles/1032120/) | 2026 | да |
| Локальный RAG на n8n обходится в **5,5× дешевле** корпоративных коробочных LLM-решений (кейс Flowwow) | [habr.com/ru/companies/flowwow/articles/1032120](https://habr.com/ru/companies/flowwow/articles/1032120/) | 2026 | да |
| Qdrant — open-source векторная БД на Rust для similarity search | [habr.com/ru/companies/amvera/articles/930250](https://habr.com/ru/companies/amvera/articles/930250/) | 2026 | да |
| В n8n tutorial Amvera: Recursive Character Text Splitter, chunk size **400**, overlap **¼ от chunk size** | [habr.com/ru/companies/amvera/articles/930250](https://habr.com/ru/companies/amvera/articles/930250/) | 2026 | да |
| Официальный n8n template 11468: полный single-vector RAG (ingestion + AI Agent chat) на Qdrant + OpenAI | [n8n.io/workflows/11468](https://n8n.io/workflows/11468-build-a-rag-agent-with-n8n-qdrant-and-openai/) | 2026 | да |
| Wildbots: дефолт чанков **500–1000 токенов**, overlap **10–20%**; hybrid dense+BM25, RRF, top_k≈20 → rerank до **5** чанков | [wildbots.ru/.../rag-agent-n8n-qdrant](https://wildbots.ru/ru/blog/rag-agent-po-korporativnoi-baze-znanii-arkhitektura-na-n8n-qdrant) | 2026 | да |
| Без reranking качество ответов RAG проседает на **25–40%** (оценка автора low-light) | [ai.low-light.ru/.../rag-sistemy-korporativnaya-baza-znaniy-2026](https://ai.low-light.ru/blog/rag-sistemy-korporativnaya-baza-znaniy-2026/) | 2026 | да (как оценка эксперта, не абсолют) |
| Retrieval типично: vector top-K **20–50**, BM25 top-K, rerank → top-N **5–10** в промпт | [ai.low-light.ru/.../rag-sistemy-korporativnaya-baza-znaniy-2026](https://ai.low-light.ru/blog/rag-sistemy-korporativnaya-baza-znaniy-2026/) | 2026 | да |
| Баланс размера чанка: **800–1500 символов** для большинства корп. задач (low-light) | [ai.low-light.ru/.../rag-sistemy-korporativnaya-baza-znaniy-2026](https://ai.low-light.ru/blog/rag-sistemy-korporativnaya-baza-znaniy-2026/) | 2026 | да |
| MVP на ~1000 док.: **6–8 недель**; пром. rollout 50–200k док.: **4–7 мес.** (low-light) | [ai.low-light.ru/.../rag-sistemy-korporativnaya-baza-znaniy-2026](https://ai.low-light.ru/blog/rag-sistemy-korporativnaya-baza-znaniy-2026/) | 2026 | да (диапазон, не обещание) |
| pgvector hybrid (vector + tsvector/BM25 + RRF k=60): retrieval precision **~62% → ~84%** на кейсе автора | [dev.to/lpossamai/.../hybrid-search-rag](https://dev.to/lpossamai/building-hybrid-search-for-rag-combining-pgvector-and-full-text-search-with-reciprocal-rank-fusion-6nk) | 2026 | да (один кейс) |
| RRF k=**60** — robust default для крупных корпусов; для 100–300 страниц пробуют k=**10–20** | [blog.gopenai.com/hybrid-search-rag](https://blog.gopenai.com/hybrid-search-in-rag-dense-sparse-bm25-splade-reciprocal-rank-fusion-and-when-to-use-which-fafe4fd6156e) | 2026 | да |
| RAGAS: reference-free метрики **faithfulness**, **answer relevance**, **context relevance** для RAG без human labels | [arxiv.org/html/2309.15217v1](https://arxiv.org/html/2309.15217v1) | 2023 (framework актуален 2026) | да |
| Типичные пороги prod: context recall **≥0.85**, faithfulness **≥0.90** (industry guide 2026) | [qaskills.sh/rag-evaluation-metrics-2026](https://qaskills.sh/blog/rag-evaluation-metrics-complete-2026) | 2026 | да (ориентир, не гарантия) |
| n8n: **70+ AI nodes**, vector stores включая Qdrant, pgvector, Pinecone, Weaviate | [digitalapplied.com/n8n-70-ai-nodes](https://www.digitalapplied.com/blog/n8n-70-ai-nodes-langchain-agent-workflows-open-source) | 2026 | да |
| Qdrant: Apache 2.0, self-host, hybrid dense+sparse, payload filtering | [nikta.ai/open-source-rag-tools-2026](https://nikta.ai/blog/luchshie-open-source-instrumenty-dlya-rag-sistem-v-2026-godu-polnyy-gid) | 2026 | да |
| pgvector: HNSW предпочтительнее IVFFlat для prod recall/latency trade-off | [rivestack.io/pgvector-hnsw-vs-ivfflat](https://rivestack.io/blog/pgvector-hnsw-vs-ivfflat) | 2026 | да |
| ~**40%** AI-agent проектов отменяются из-за скрытых затрат и нулевого ROI — аргумент за пилот + eval + HITL | [fact-bank / mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026 | да |
| Автономные ИИ-системы завершают **<2,5%** сложных неструктурированных задач без человека — HITL по умолчанию | [fact-bank / mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026 | да |

**Не использовать без первичника:** promaren «3 из 5 систем», «+60% точности»; prooftech «−80% времени поиска»; tashev.ru (placeholder-контент); mediaten «2 млн документов» без верификации в research.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** пошагово собрать **MVP RAG-базы знаний для поддержки/регламентов** на стеке **n8n + (Qdrant или pgvector)**: аудит документов → чанкинг → hybrid retrieval → rerank → промпт с цитатами → **golden set 20–30 вопросов (RAGAS/recall@5)** → webhook-бот с эскалацией человеку.

**Почему отличается от конкурентов:**
- Не «что такое RAG» на 10k знаков (Habr 989000), а **workflow A→B→C** с чеклистом.
- Не enterprise «от 25 млн ₽», а **пилот на сотнях–тысячах документов** и no-code ingestion через n8n.
- Закрывает пробел SERP: **eval + human-in-the-loop + интеграция** (Telegram/CRM), в духе site-brief Excalibur.

**Tone:** B2B без корпоративной воды; RAG, chunk, embedding, rerank — «на пальцах»; уверенность интегратора, без «+300% ROI».

**H2-каркас (из карточки B06 + research):**
1. RAG vs fine-tuning: когда база знаний лучше дообучения
2. Подготовка документов: чанкинг 300–800 токенов, метаданные, дедуп
3. Выбор стека: **таблица Qdrant vs pgvector**, эмбеддинги, hybrid BM25+vector
4. Reranker и промпт: top-K → top-N, цитаты, ответ «не знаю»
5. Golden Set и метрики: recall@5, faithfulness, RAGAS перед продом
6. Интеграция n8n/Make: webhook-бот, re-index, эскалация к менеджеру

**Internal links (карточка):** `/avtomatizaciya-n8n-ai-agents/`, `/podklyuchenie-mcp-cursor/`

**Conversion:** мягкий CTA AI-аудит / внедрение RAG под ключ (site-brief), max 2–3 CTA, не подменяют how-to.

---

## 5. Comparison-матрица Qdrant vs pgvector (черновик writer)

| Критерий | Qdrant | PostgreSQL + pgvector |
|----------|--------|------------------------|
| Когда брать | Greenfield RAG, hybrid sparse+dense, фильтры по metadata/ACL | Уже есть Postgres, <1M векторов, хотите один стек |
| Hybrid search | Native dense+sparse, RRF в Query API | tsvector + pgvector + RRF в SQL |
| Multitenancy | Payload `tenant_id` + `is_tenant` (официальный guide) | Row-level security + schema per tenant |
| Self-host / 152-ФЗ | Да, Docker/K8s | Да, если БД on-prem |
| Сложность для n8n | Нативные Qdrant Vector Store nodes | Supabase/pgvector nodes или HTTP |
| Масштаб | Миллионы+ векторов, квантизация | Замедление >1M векторов (AGmind, nikta) |
| MVP time | Qdrant Cloud trial или Docker + n8n template 11468 | Быстрее, если Postgres уже в контуре |

**Позиция автора:** pgvector — «RAG рядом с CRM/1С»; Qdrant — default для dedicated KB с hybrid и rerank.

---

## 6. FAQ-кандидаты (7)

1. **Как настроить RAG базу знаний с нуля?** — Список 20–30 эталонных вопросов → собрать минимальный корпус → n8n ingestion → Qdrant/pgvector → AI Agent с tool retrieval → прогнать golden set.
2. **Какой размер чанка выбрать для RAG?** — Старт 400–512 tok (или 500–1000 для длинных регламентов), overlap 10–20%; для структурных документов — резка по заголовкам, не только по токенам.
3. **Чем RAG отличается от обычного ChatGPT?** — ChatGPT не видит ваши PDF/Confluence; RAG подставляет найденные фрагменты и может требовать цитату источника.
4. **Qdrant или pgvector для корпоративной базы?** — Qdrant если нужен hybrid и отдельный search-сервис; pgvector если Postgres уже центр данных.
5. **Зачем reranker, если есть vector search?** — Vector даёт семантику, но промахивается по артикулам/кодам; rerank на top-20–50 кандидатах поднимает precision.
6. **Как проверить RAG перед запуском?** — Golden set 20–30 Q&A, метрики faithfulness и context recall (RAGAS), порог faithfulness ~0.9 на пилоте.
7. **Что делать, если бот ответил неправильно?** — Кнопка «сообщить об ошибке», лог chunk IDs, переиндексация документа, эскалация human-in-the-loop (не автоматически закрывать тикет).

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение RAG 40–60 слов | Lead | «RAG база знаний — …» |
| Workflow-схема | H2-2/H2-6 | Документы → chunk → embed → index → query → hybrid → rerank → LLM → чат |
| Таблица Qdrant vs pgvector | H2-3 | Comparison + «выбирай если» |
| Чеклист 10+ пунктов | Перед продом | Island-test actionable |
| FAQ 7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «rag база знаний», «настройка rag системы», «rag qdrant n8n», «корпоративная база знаний rag», «rag для бизнеса».

---

## 8. Риски для writer

- Wordstat-цифры **не писать** до обновления MCP-токена.
- Не копировать Wildbots/low-light структуру 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog`).
- Без эмодзи; дефис вместо длинного тире; прямые кавычки.
- Min **5** нумерованных шагов + **таблица** + **чеклист 10+** (utility gate статьи).
- Цены enterprise (800 тыс – 25 млн ₽) — только как диапазон рынка со ссылкой, не как оффер Excalibur.
- Human-in-the-loop обязателен в финале (fact-bank).

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель проведёт аудит документов, соберёт MVP RAG на n8n с Qdrant или pgvector (чанкинг, hybrid search, rerank), прогонит golden set из 20–30 вопросов с метриками faithfulness/recall и подключит webhook-бота поддержки с цитатами источников и эскалацией к человеку.

**action_outline (для writer):**

1. **Зафиксировать сценарий и golden set:** 20–30 реальных вопросов поддержки/онбординга + эталонные ответы; выбрать один отдел/продукт (не «вся Wiki»).
2. **Аудит и очистка корпуса:** удалить дубли и документы старше N лет; нормализовать PDF/DOCX → markdown; метаданные `doc_id`, `updated_at`, `acl`.
3. **Настроить ingestion в n8n:** trigger (Drive/S3/webhook) → Text Splitter (400–512 tok, overlap 10–20%) → Embeddings → Vector Store (Qdrant **или** pgvector).
4. **Выбрать vector DB:** по таблице раздела 5; для pgvector включить HNSW + tsvector; для Qdrant — payload-индексы `group_id`, `updated_at`.
5. **Включить hybrid retrieval:** BM25/sparse + dense, RRF (k=60 или 10–20 на малом корпусе); retrieve k=15–20.
6. **Добавить reranker:** срез до 4–6 чанков (bge-reranker-v2-m3 или hosted rerank); system prompt: «только по контексту», «не знаю» если пусто.
7. **Eval перед продом:** прогнать golden set, замерить faithfulness ≥0.9 и context recall; логировать chunk IDs; итерировать chunk size/overlap.
8. **Собрать retrieval-бота:** Chat/webhook Trigger → AI Agent + Qdrant tool → ответ с цитатой; кнопка «ошибка» → канал менеджеру (кейс Flowwow).
9. **Запланировать re-index и HITL:** cron/webhook на новые регламенты; эскалация в CRM/Telegram при низком score или жалобе пользователя.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (AUTH/server) |
| Таблица фактов с URL | ✅ (18 фактов) |
| utility_verdict + action_outline | ✅ |
| Comparison Qdrant vs pgvector | ✅ |
| FAQ 5–7 | ✅ (7) |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.
