# Research notes — B06 «Как создать чат-бот для бизнеса с RAG: пошаговый workflow в n8n/Make с эскалацией и CRM»

**topic_id:** B06  
**slug:** chat-bot-dlya-biznesa-rag  
**article_mode:** B (how-to + workflow)  
**research_date:** 2026-06-21  
**disclaimer:** Все даты, версии и статистика проверены на 21.06.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [bothelp.io/ru/blog/luchshie-chat-boty-dlya-biznesa](https://bothelp.io/ru/blog/luchshie-chat-boty-dlya-biznesa) | Рейтинг SaaS (2026) | Кейсы, сравнение конструкторов, Telegram/MAX | Нет сквозного RAG-workflow; продаёт BotHelp | ТОП-10 без чек-листа запуска и метрик FCR |
| 2 | [mbk-agent.ru/blog/chat-boty-dlya-biznesa-2026](https://mbk-agent.ru/blog/chat-boty-dlya-biznesa-2026) | Обзор типов + цены | 11 типов ботов, кейсы | Мало техники n8n/Make/RAG; акцент на «ИИ-менеджеров» как маркетинг | Цены «под ключ» без первичника |
| 3 | [flow-masters.ru/blog/chatbots-business-2026](https://flow-masters.ru/blog/chatbots-business-2026/) | Тренды + платформы | CRM, квалификация лидов, омниканал | Нет пошаговой сборки AI Agent + Vector Store | Структуру рейтинга 1:1 |
| 4 | [blog.chatplace.io/chat-bot-v-telegram-dlya-biznesa](https://blog.chatplace.io/chat-bot-v-telegram-dlya-biznesa-kak-avtomatizirovat-prodazhi-i-zamenit-otdel-podderzhki/) | Telegram how-to | Автоматизация продаж в TG | Конструктор-centric; нет RAG/эскалации в n8n | Обещания «заменить отдел поддержки» |
| 5 | [dev.max.ru/docs/chatbots/bots-nocode/create](https://dev.max.ru/docs/chatbots/bots-nocode/create) | Официальная дока MAX | Лимиты ботов, токен, модерация, партнёры | Нет RAG и CRM-workflow | — (канон для MAX-фактов) |
| 6 | [blog.t-traf.ru/kak-sozdat-bota-v-max](https://blog.t-traf.ru/kak-sozdat-bota-v-max/) | MAX гайд (2026) | Bot API vs конструктор, модерация до 48 ч, 5 ботов/орг | Сценарный бот vs ИИ — без n8n RAG | Коммерческий хвост агентства |
| 7 | [n8n.io/workflows/7563](https://n8n.io/workflows/7563-create-a-company-policy-chatbot-with-rag-pinecone-vector-database-and-openai/) | Официальный RAG-шаблон n8n | Data load + retrieval, Pinecone, AI Agent | Нет Telegram/CRM/эскалации для бизнеса | Сухой перевод template без «на пальцах» |
| 8 | [dzen.ru/a/ajDfnoO-Zyx4kCo2](https://dzen.ru/a/ajDfnoO-Zyx4kCo2) | Workflow-гайд (автор блога) | Полный pipeline: задача → канал → RAG → CRM → FCR/CSAT | Уже наш контент на Дзен — не дублировать 1:1 | Копировать себя без дифференциации для WP |

**Паттерн SERP:** топ по запросу «чат боты для бизнеса 2026» — рейтинги конструкторов (BotHelp, SaleBot, ChatPlace) и обзоры «11 типов ботов». Отдельный кластер — Telegram и MAX как каналы. **Пробел:** почти никто не даёт один сквозной low-code workflow **n8n или Make + RAG + human handoff + CRM + метрики запуска** без 15 SaaS в таблице.

**Intent:** `how_to` — пользователь хочет запустить **рабочего** ИИ-бота для FAQ/лидов, а не выбрать «лучший конструктор». Вторичный intent: Telegram vs MAX, «как сделать без программиста», anti-hallucination через RAG.

**Пробел для «Ковчег»:** практик Make (Артур) показывает **один pipeline за 7–14 дней**, сравнивает n8n vs Make для того же кейса, CTA на курс Make для аудитории без DevOps; internal link на B02 (n8n AI agents) и B03 (MCP).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 21.06.2026)

⚠️ **WORDSTAT MCP UNAVAILABLE:** Инструмент `wordstat_get_top_requests` (сервер `user-mcp-kv`) недоступен в текущей Cloud-сессии research-агента (MCP не подключён). Точные объёмы спроса **не получены из API**. Writer **не должен** использовать цифры «показов/мес» до повторного вызова Wordstat Директором или обновления токена: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Запросы для обязательной проверки (primary + secondary из карточки B06)

| Фраза (очередь MCP) | Назначение |
|---------------------|------------|
| чат боты для бизнеса | primary_query |
| ии чат бот для бизнеса | secondary |
| чат бот для бизнеса telegram | канал |
| чат бот для бизнеса макс | канал MAX |
| как сделать чат бот для бiznesa | how_to tail |

### LSI для writer (из SERP + research-context, без цифр Wordstat)

- чат-бот для бизнеса с RAG / база знаний FAQ  
- n8n AI Agent + Vector Store Tool / Qdrant / Pinecone / pgvector / Supabase  
- Make AI Agents + Reasoning panel + CRM-модули  
- Telegram Business / Telegram Trigger / business_connection_id  
- MAX business.max.ru / Bot API platform-api.max.ru / модерация бота  
- эскалация оператору / human-in-the-loop / handoff  
- amoCRM Bitrix24 Google Sheets лид  
- FCR resolution rate / CSAT / fallback rate  
- anti-hallucination system prompt «только из контекста»  
- 50–100 тест-кейсов перед продакшеном  

**SEO-стратегия:** primary «чат боты для бизнеса» в H1/lead; secondary в H2 (Telegram, MAX, «как сделать»); long-tail «RAG n8n Make чат-бот CRM» — дифференциатор без конкуренции в SERP по точному H1 (SERP по H1 пуст в research-serp.json).

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| 65% респондентов McKinsey: организации регулярно используют gen AI минимум в одной бизнес-функции (early 2024) | [mckinsey.com/state-of-ai-2024](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2024) | 21.06.2026 | да |
| 71% организаций регулярно используют gen AI в ≥1 функции (опрос McKinsey, июль 2024) | [mckinsey.com/state-of-ai-how-organizations-are-rewiring](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value) | 21.06.2026 | да |
| RAG — стандартная практика для чат-ботов поддержки и HR-помощников (поиск по базе знаний) | [habr.com/selectel/1013862](https://habr.com/ru/companies/selectel/articles/1013862/) | 21.06.2026 | да |
| Организация или ИП на MAX: до **5** чат-ботов на один профиль; самозанятый — **2** | [dev.max.ru/docs/chatbots/bots-nocode/create](https://dev.max.ru/docs/chatbots/bots-nocode/create) | 21.06.2026 | да |
| Токен MAX-бота выдаётся после успешной модерации в кабинете «Чат-боты → Расширенные настройки» | [dev.max.ru/docs/chatbots/bots-nocode/create](https://dev.max.ru/docs/chatbots/bots-nocode/create) | 21.06.2026 | да |
| Модерация бота MAX: до **48 рабочих часов** (практика платформы, не SLA) | [blog.t-traf.ru/kak-sozdat-bota-v-max](https://blog.t-traf.ru/kak-sozdat-bota-v-max/) | 21.06.2026 | да (как ориентир, не гарантия) |
| Bot API MAX: endpoint `platform-api.max.ru`, лимит до **30 req/s** | [blog.t-traf.ru/kak-sozdat-bota-v-max](https://blog.t-traf.ru/kak-sozdat-bota-v-max/) | 21.06.2026 | да |
| n8n RAG: документы → chunk → embeddings → vector store; query через similarity search | [docs.n8n.io/advanced-ai/rag-in-n8n](https://docs.n8n.io/advanced-ai/rag-in-n8n/) | 21.06.2026 | да |
| n8n AI Agent + Vector Store как tool; limit chunks + Include Metadata | [docs.n8n.io/advanced-ai/rag-in-n8n](https://docs.n8n.io/advanced-ai/rag-in-n8n/) | 21.06.2026 | да |
| n8n tutorial: Chat Trigger → AI Agent → Chat Model → System message → Simple Memory | [docs.n8n.io/advanced-ai/intro-tutorial](https://docs.n8n.io/advanced-ai/intro-tutorial/) | 21.06.2026 | да |
| Simple Memory по умолчанию: **5** interactions | [docs.n8n.io/advanced-ai/intro-tutorial](https://docs.n8n.io/advanced-ai/intro-tutorial/) | 21.06.2026 | да |
| n8n Cloud Starter: **20 €/мес** (год), **2 500** workflow executions | [n8n.io/pricing](https://n8n.io/pricing/) | 21.06.2026 | да |
| n8n: один execution = полный прогон workflow (не каждый шаг) | [n8n.io/pricing](https://n8n.io/pricing/) | 21.06.2026 | да |
| n8n RAG template: Google Drive → split → OpenAI Embeddings → Pinecone; query через AI Agent + Vector Store QnA | [n8n.io/workflows/7563](https://n8n.io/workflows/7563-create-a-company-policy-chatbot-with-rag-pinecone-vector-database-and-openai/) | 21.06.2026 | да |
| Make AI Agents доступны **на всех тарифах** | [make.com/en/ai-agents](https://www.make.com/en/ai-agents/) | 21.06.2026 | да |
| Make: **3 000+** интеграций, визуальный builder | [make.com/en/ai-agents](https://www.make.com/en/ai-agents/) | 21.06.2026 | да |
| Make Free: **1 000 credits/мес** | [make.com/en/pricing](https://www.make.com/en/pricing) | 21.06.2026 | да |
| RAG chunking sweet spot: **500–1000** токенов, overlap **100–200** (10–20%) | [enterno.io/s/how-to-build-rag-chatbot](https://enterno.io/s/how-to-build-rag-chatbot) | 21.06.2026 | да |
| Support-bot pattern: chunk **800–1200** chars, top-k **3–5**, эскалация при confidence **< 0.75** | [rolandsoftwares.com/n8n-chatbot-customer-support](https://rolandsoftwares.com/content/n8n-chatbot-customer-support-how-to/) | 21.06.2026 | да (практика, не универсальный порог) |
| ~**40%** проектов автономных ИИ-агентов отменяются из-за скрытых затрат и нулевого ROI | [mayai.ru/kontent-zavod…](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) + fact-bank | 2026-06-11 | да |
| Автономные ИИ-системы завершают **< 2.5%** сложных неструктурированных задач без человека → Human-in-the-loop 2.0 | fact-bank / mayai.ru | 2026-06-11 | да |
| Базовая автоматизация на n8n/Make + API LLM ≈ **$150/мес** (ориентир стека) | fact-bank / mayai.ru | 2026-06-11 | да |
| Make.com: **2 500+** нативных интеграций; тарификация Compute Units | fact-bank | 2026-06-11 | да |
| Self-hosted n8n vs облачные SaaS: до **+35%** маржинальности на медиа-heavy пайплайнах | fact-bank | 2026-06-11 | да |

**Не использовать без первичника:** «886 показов/мес» и прочие Wordstat-цифры из Дзен-черновика; «85 млн пользователей MAX» (BotHelp marketing); «3–7 дней vs 3–8 недель» — только как ориентир практика с пометкой «по опыту внедрений».

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** собрать **один рабочий чат-бот для бизнеса** (FAQ или лиды) в **n8n или Make**: канал (Telegram / виджет / MAX) → AI Agent → **RAG по своим документам** → запись в CRM → **эскалация оператору** при низкой уверенности или триггер-словах → чек-лист метрик **FCR / CSAT / fallback** за 7–14 дней.

**Почему отличается от конкурентов:**
- Рейтинги SaaS не учат собирать anti-hallucination pipeline.
- Официальные n8n-шаблоны RAG не закрывают Telegram Business, MAX и CRM.
- «Ковчег»: язык для не-программистов, честное **n8n vs Make** (когда self-host/RAG глубже vs когда Make быстрее), CTA на курс Make.

**Tone:** по-человечески; RAG, Vector Store, handoff — «на пальцах». Без «ТОП-15 платформ».

**H2-каркас (из карточки + research):**
1. Задача и канал: FAQ vs лиды — Telegram, виджет или MAX  
2. База знаний для RAG: FAQ, цены, «что бот не делает»  
3. Workflow n8n/Make: триггер → AI Agent → Vector Store → ответ  
4. Эскалация и CRM (human-in-the-loop)  
5. Чек-лист запуска 7–14 дней: 50–100 тест-кейсов, FCR, CSAT  

**Conversion:**
- CTA курс Make: max 2× → kv-ai.ru/obuchenie-po-make (5 800 ₽/мес — единственный верифицированный прайс продукта из fact-bank/site-brief)  
- Telegram @maya_pro — 1× если уместно  
- Internal: `/avtomatizaciya-n8n-ai-agents/`, `/podklyuchenie-mcp-cursor/`

---

## 5. Workflow-схема (черновик для writer)

```text
Входящее сообщение (Telegram / Chat Trigger / MAX webhook)
  → классификация интента (или сразу AI Agent)
  → RAG: embed query → top-k chunks из Vector Store
  → AI Agent + System prompt («только из контекста; иначе эскалация»)
  → IF confidence низкая OR триггер («возврат», «аллергия», «оператор»)
       → handoff: уведомление оператору + ticket/CRM + pause bot
     ELSE
       → ответ пользователю
  → при лиде: HTTP/CRM tool → amoCRM / Sheets / Bitrix24
  → лог (PII замаскирован) для разбора галлюцинаций
```

**n8n ноды (MVP):** Telegram Trigger или Chat Trigger → AI Agent (Tools Agent) → OpenAI Chat Model → Postgres/Window Buffer Memory (session_id = chat_id) → Vector Store Tool + Qdrant/Pinecone/pgvector → HTTP Request (CRM) → IF/Switch (эскалация) → Telegram/Slack alert.

**Make MVP:** Chat/instant trigger → AI Agent → knowledge module / HTTP to vector DB → CRM module → Router по handoff flag.

---

## 6. FAQ-кандидаты (6)

1. **Как создать чат-бот для бизнеса без программиста?** — одна задача + канал + n8n/Make workflow с RAG и CRM; 3–7 дней при готовом FAQ.  
2. **Чем чат-бот с RAG отличается от конструктора без базы знаний?** — ответы только из ваших документов; без RAG модель «достраивает» цены и сроки.  
3. **ИИ чат-бот для бизнеса бесплатно — реально?** — n8n CE бесплатен + сервер + API LLM; Make Free 1 000 credits; «бесплатно без RAG» = риск галлюцинаций.  
4. **Как подключить чат-бота в Telegram для бизнеса?** — BotFather → Business mode → Telegram Trigger → memory по chat_id → тест до рекламы.  
5. **Нужен ли MAX, если уже есть Telegram?** — не обязателен на MVP; добавлять второй канал после стабильных метрик, учитывая модерацию MAX.  
6. **Когда эскалировать диалог оператору?** — нет факта в базе, жалоба, медицина/юридические темы, низкая уверенность; передавать полную историю в CRM.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «RAG-чат-бот для бизнеса» 40–60 слов | Lead | «RAG-чат-бот — …» |
| Workflow-схема A→B→C | H2-3 | ASCII / mermaid |
| Таблица «задача → канал → инструмент» | H2-1 | Таблица |
| Чек-лист 10+ пунктов запуска | H2-5 | Checkbox list |
| FAQ 6 | Конец | Ответы-действия |
| E-E-A-T | Автор | Артур Хорошев, Make + чат-боты |

**Целевые формулировки:** «чат боты для бизнеса», «как сделать чат бот для бизнеса», «ии чат бот для бизнеса», «чат бот telegram/max», «RAG n8n Make».

---

## 8. Риски для writer

- **Wordstat:** не писать показы/мес до MCP-проверки.  
- Не копировать рейтинги BotHelp/mbk 1:1.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Min **5** нумерованных шагов + чеклист **10+** пунктов (utility gate статьи).  
- Comparison n8n vs Make — честный; не обесценивать n8n для RAG/self-host.  
- Цены Make «Ковчег» — только 5 800 ₽/мес из brief.  
- Без эмодзи; дефис вместо длинного тире.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель выберет одну бизнес-задачу и канал (Telegram, виджет или MAX), подготовит FAQ для RAG, соберёт workflow в n8n или Make с AI Agent и Vector Store, настроит эскалацию и запись лидов в CRM, прогонит 50–100 тест-кейсов и проверит запуск по FCR/CSAT/fallback.

**action_outline (для writer):**

1. **Зафиксировать одну primary-задачу** (FAQ L1 или квалификация лидов) и один канал на MVP — не три параллельно.  
2. **Собрать базу знаний:** FAQ, прайс, регламенты + список запретов (медицина, скидки без документа); chunk 500–1000 токенов с overlap.  
3. **Выбрать платформу:** n8n (self-host/RAG/control) vs Make (быстрый SaaS) — таблица «выбирай если».  
4. **Поднять vector store** (Qdrant/Pinecone/pgvector/Supabase) и проиндексировать FAQ через n8n Data Loader или Make-аналог.  
5. **Собрать workflow:** триггер → AI Agent + Chat Model → Memory (session_id = chat_id) → Vector Store Tool + CRM tool.  
6. **System prompt:** «отвечай только из retrieved context; если факта нет — эскалируй»; max iterations на Agent.  
7. **Настроить handoff:** Switch по ключевым словам / флагу low confidence → уведомление оператору + CRM ticket с transcript.  
8. **Прогнать 50–100 тест-кейсов** (реальные переписки + jailbreak + цена без прайса) — таблица PASS/FAIL.  
9. **Запустить пилот 7–14 дней:** метрики FCR 60–80%, CSAT, fallback <20%, avg response <5 с на FAQ; weekly update FAQ по логам.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен — LSI без цифр |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ (6) |
| GEO hooks | ✅ |

**Writer:** готов с оговоркой по Wordstat. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + `conversion-map.md` + fact-bank (Human-in-the-loop, $150/mo stack).
