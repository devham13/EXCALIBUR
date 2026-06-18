# Research notes — B06 «Как создать Telegram-бота с ИИ на n8n: пошаговая инструкция без кода»

**topic_id:** B06  
**slug:** telegram-bot-ii-n8n  
**article_mode:** B (how-to)  
**research_date:** 2026-06-18  
**disclaimer:** Все даты, версии и статистика проверены на 18.06.2026.

---

## 1. SERP-обзор (WebSearch, 18.06.2026; 10 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [mayai.ru/chat-bot-v-telegram-s-ii-sobiraem-na-n8n-bez-koda-za-30-minut](https://mayai.ru/chat-bot-v-telegram-s-ii-sobiraem-na-n8n-bez-koda-za-30-minut/) | Практик-гайд (2026) | AI Agent + WindowBuffer + Tools; голос; human-in-the-loop; выбор моделей | Много непроверенных цифр («конверсия ×2.5», «-30–50% API»); перегруз Make-ссылками | Выдуманную статистику; структуру 1:1 |
| 2 | [aibot.direct/blog/n8n-telegram-bot](https://aibot.direct/blog/n8n-telegram-bot) | Технический how-to | BotFather → Trigger → OpenAI/Claude; память через Sheets; команды Switch | Старый стек (OpenAI node вместо AI Agent); память через Code Node сложна для ЦА | Code Node для памяти как основной путь |
| 3 | [neiropotok.ru/blog/telegram-bot-s-ai-bez-koda](https://neiropotok.ru/blog/telegram-bot-s-ai-bez-koda) | Гайд 2026 | Пошагово AI Agent + OpenRouter; 30 мин; понятный язык | Нет эскалации к менеджеру; нет чеклиста продакшена | Минималистичную схему без бизнес-контура |
| 4 | [dipustovalov.ru/blog/telegram-bot-marketing-2026](https://dipustovalov.ru/blog/telegram-bot-marketing-2026) | Маркетинг + n8n | Метрики воронки, webhook vs polling, fallback, таблица платформ | Фокус на кнопочных воронках, не на ИИ-агенте | CR «22%» без контекста как универсальную норму |
| 5 | [habr.com/ru/companies/amvera/articles/890730](https://habr.com/ru/companies/amvera/articles/890730/) | Туториал Habr | 400+ интеграций; Telegram Trigger; WEBHOOK_URL; Postgres tool | Уклон в Amvera-хостинг; Chat Trigger, не AI Agent node | Продажу одного хостинга как единственный путь |
| 6 | [market-n8n.ru/tpost/j326dpica1-sozdanie-umnih-botov-v-n8n-chat-boti-ass](https://market-n8n.ru/tpost/j326dpica1-sozdanie-umnih-botov-v-n8n-chat-boti-ass) | Коммерческий гайд | AI Agent, webhook, память | Агрессивный маркетинг; смешение парсеров и support-ботов | Хайп «90% бизнесов сливают бюджет» |
| 7 | [bothost.ru/blog/post/mcp-telegram-bot-n8n-guide](https://bothost.ru/blog/post/mcp-telegram-bot-n8n-guide) | MCP + Telegram | Свежий угол MCP в связке с ботом | Сложнее для новичка; другой intent (MCP) | MCP как обязательный шаг для MVP |
| 8 | [vc.ru/id5114590/2598791-sozdanie-ai-agenta-dlya-telegram-na-n8n](https://vc.ru/id5114590/2598791-sozdanie-ai-agenta-dlya-telegram-na-n8n) | VC how-to | Бесплатный старт, AI Agent для TG | Короткий, без voice/handoff/checklist | Поверхностный финал без продакшена |
| 9 | [docs.n8n.io/.../telegramtrigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/) | Официальная docs | Канон событий Trigger (Message, Callback Query…) | Нет бизнес-кейсов и выбора Cloud/self-host | Сухой перевод без «на пальцах» |
| 10 | [n8n.io/workflows/3350-telegram-ai-bot-to-human-handoff-for-sales-calls](https://n8n.io/workflows/3350-telegram-ai-bot-to-human-handoff-for-sales-calls/) | Официальный шаблон | Human-in-the-loop handoff; Redis FSM; Send and Wait | 39 нод, сложно для первого бота | Копировать шаблон целиком без упрощения |

**Паттерн SERP:** топ закрывают «собери за 15–30 минут» (AI Agent + Trigger + Send). Отдельный кластер — маркетинговые воронки без ИИ (dipustovalov). Запрос «телеграм бот с ии» в выдаче уводит в **обзоры готовых ботов** (vc.ru, dtf.ru), а не DIY на n8n — каннибализация низкая, но нужен явный отстрой «свой бот под бизнес, не каталог чужих».

**Intent:** `how_to` — собрать **своего** Telegram-бота с ИИ в n8n без кода. Вторичный intent: память диалога, лиды/FAQ, голос, передача менеджеру.

**SERP gaps (наш угол Excalibur):**
1. **Операционная система, не «чат ради чата»:** заявка → квалификация → запись в CRM/таблицу → эскалация человеку (human-in-the-loop по умолчанию).
2. **Чеклист перед продакшеном:** HTTPS/webhook, fallback, Error Workflow, Max Iterations, хранение `telegram_id`, кнопка «Поговорить с менеджером».
3. **Cloud vs self-host decision tree** под Telegram webhooks (без DevOps-воды).
4. **Голосовые сообщения** одной веткой Switch + Whisper (конкуренты либо пропускают, либо размазывают).
5. **Отличие от B02:** узкий канал Telegram, не общий гайд по AI Agent; ссылка на B02 как «углубление в агентов».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

**⚠️ WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в runtime Cloud Agent (`ListMcpResources`: Server "user-mcp-kv" not found). Инструмент `wordstat_get_top_requests` вызвать невозможно. **Точные показы/мес не получены** — цифры спроса в статью не вставлять.

**Семантическая оценка (SERP + кластер B02 Wordstat от 11.06.2026):**
- Ядро «telegram бот n8n» — **нишевый long-tail** внутри кластера n8n (head «n8n» ~37k, «n8n ai» ~720, «n8n агенты» ~699 — из research B02).
- Вторичный «телеграм бот с ии» тянет **информационный** intent (обзоры готовых ботов), не how-to n8n — в статье явно позиционировать DIY для бизнеса.
- «telegram trigger n8n» — техничный подзапрос (документация + YouTube EN); закрывать блоком настройки Trigger.
- «как сделать бота в телеграм с нейросетью» — широкий запрос; конкуренты предлагают BotFather + конструкторы без n8n — отстройка через «своя логика + CRM без кода».

### LSI для writer (без объёмов)

- telegram trigger n8n, telegram bot api, botfather, webhook https  
- ai agent node n8n, tools agent, window buffer memory, session key chat id  
- openai chat model, claude, gpt-4o-mini, openrouter  
- human in the loop, send and wait, эскалация менеджеру  
- голосовые сообщения telegram whisper, switch node  
- n8n cloud vs self-hosted, WEBHOOK_URL, ssl сертификат  
- лиды faq google sheets crm bitrix amocrm  
- чеклист перед запуском, fallback, error workflow  

**SEO-стратегия:** primary «telegram бот n8n» в H1/URL; secondary в H2/H3; head «n8n» через internal link на `/avtomatizaciya-n8n-ai-agents/`.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| n8n — open source платформа с **400+ интеграциями**, включая LLM и векторные БД | [habr.com/ru/companies/amvera/articles/890730](https://habr.com/ru/companies/amvera/articles/890730/) | 18.06.2026 | да |
| Развёртывание первого AI-чата в n8n на Habr оценивается в **~30 минут** | [habr.com/ru/companies/amvera/articles/890730](https://habr.com/ru/companies/amvera/articles/890730/) | 18.06.2026 | да |
| Для Telegram webhook на self-host нужна переменная **WEBHOOK_URL** с HTTPS-доменом | [habr.com/ru/companies/amvera/articles/890730](https://habr.com/ru/companies/amvera/articles/890730/) | 18.06.2026 | да |
| Все запросы к Telegram Bot API — только через **HTTPS** | [core.telegram.org/bots/api](https://core.telegram.org/bots/api) | 18.06.2026 | да |
| `setWebhook` принимает **HTTPS URL**; порты webhook: **443, 80, 88, 8443** | [core.telegram.org/bots/api#setWebhook](https://core.telegram.org/bots/api#setWebhook) | 18.06.2026 | да |
| Telegram Trigger: событие **Message** — входящие текст/фото/стикеры и т.д. | [docs.n8n.io/.../telegramtrigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/) | 18.06.2026 | да |
| AI Agent node **обязан** иметь минимум один подключённый **Tool** sub-node | [docs.n8n.io/.../n8n-nodes-langchain.agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/) | 18.06.2026 | да |
| С версии **1.82.0** все AI Agent работают как **Tools Agent** | [docs.n8n.io/.../n8n-nodes-langchain.agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/) | 18.06.2026 | да |
| Simple Memory (Window Buffer): параметры **Session Key** и **Context Window Length** | [docs.n8n.io/.../memorybufferwindow](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/) | 18.06.2026 | да |
| Simple Memory **не работает** в active production при **queue mode** n8n | [docs.n8n.io/.../memorybufferwindow](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/) | 18.06.2026 | да |
| n8n Cloud **Starter: 20 €/мес** (год), **2 500 executions** | [n8n.io/pricing](https://n8n.io/pricing/) | 18.06.2026 | да |
| n8n Cloud **Pro: 50 €/мес**, **10 000 executions** | [n8n.io/pricing](https://n8n.io/pricing/) | 18.06.2026 | да |
| Trial Starter/Pro: **14 дней**, карта не нужна | [n8n.io/pricing](https://n8n.io/pricing/) | 18.06.2026 | да |
| **Execution** = один полный прогон workflow (не каждый шаг) | [n8n.io/pricing](https://n8n.io/pricing/) | 18.06.2026 | да |
| Hosted n8n: данные в **EU (Frankfurt)** | [n8n.io/pricing](https://n8n.io/pricing/) | 18.06.2026 | да |
| Telegram webhooks требуют **SSL/HTTPS**; для теста — n8n.cloud trial или `--tunnel` | [aibot.direct/blog/n8n-telegram-bot](https://aibot.direct/blog/n8n-telegram-bot) | 18.06.2026 | да |
| Webhook даёт ответ **0–100 ms** vs long polling **0,5–2 сек** (авторский кейс) | [dipustovalov.ru/blog/telegram-bot-marketing-2026](https://dipustovalov.ru/blog/telegram-bot-marketing-2026) | 18.06.2026 | да (с оговоркой «в кейсе автора») |
| CR бота в целевое действие **15–35%**; формы на сайте **4–8%** (авторский бенчмарк) | [dipustovalov.ru/blog/telegram-bot-marketing-2026](https://dipustovalov.ru/blog/telegram-bot-marketing-2026) | 18.06.2026 | да (как ориентир, не гарантия) |
| n8n self-hosted на VPS **~500 ₽/мес** vs n8n cloud **~1 800 ₽/мес** (оценка автора) | [dipustovalov.ru/blog/telegram-bot-marketing-2026](https://dipustovalov.ru/blog/telegram-bot-marketing-2026) | 18.06.2026 | да (как диапазон, не оферта) |
| Шаблон **workflow 3350**: bot-to-human handoff через Redis + Human-in-the-loop + Telegram | [n8n.io/workflows/3350](https://n8n.io/workflows/3350-telegram-ai-bot-to-human-handoff-for-sales-calls/) | 18.06.2026 | да |
| Сборка AI-бота с WindowBuffer + Tools — **30–40 минут** (оценка практика) | [mayai.ru/chat-bot-v-telegram-s-ii-sobiraem-na-n8n-bez-koda-za-30-minut](https://mayai.ru/chat-bot-v-telegram-s-ii-sobiraem-na-n8n-bez-koda-za-30-minut/) | 18.06.2026 | да (как оценка времени) |

### Из fact-bank.md (переиспользовать в статье)

| Факт | Источник | Можно в текст |
|------|----------|---------------|
| Автономные ИИ-системы завершают **<2,5%** сложных неструктурированных задач без человека — **Human-in-the-loop 2.0** как стандарт | [mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | да |
| Базовая автоматизированная система на API LLM + no-code (Make, n8n) — **~$150/мес** | [mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | да |
| **~40%** проектов автономных ИИ-агентов отменяются из-за скрытых затрат и нулевого ROI | [mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | да |

**Не использовать без первичника:** «конверсия диалога ×2.5 с памятью» (mayai.ru); «40% обращений вне рабочих часов» (aibot.direct); «n8n 2.0 Agentic Update» как релизную версию без docs; CR «22%» dipustovalov как обещание читателю.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** пошагово собрать **рабочего Telegram-бота с ИИ в n8n** (Trigger → AI Agent → Send Message) для **бизнес-задач** (лиды, FAQ, эскалация), без кода и с чеклистом перед продакшеном.

**Почему отличается от конкурентов и B02:**
- B02 — общий AI Agent в n8n + comparison с Make; B06 — **узкий канал Telegram** и операционный контур «заявка → CRM → менеджер».
- Конкуренты дают MVP за 30 мин, но редко закрывают **fallback, handoff, голос, хранение лидов** в одном гайде для B2B без техбэкграунда.
- Excalibur: human-in-the-loop по умолчанию, без обещаний «бот заменит отдел продаж».

**Tone:** простой B2B; webhook, session key, Tools Agent — сразу «на пальцах». Без эмодзи в тексте статьи.

**H2-каркас (из карточки + research):**
1. Зачем бизнесу Telegram-бот с ИИ в 2026 (боль: потерянные заявки, ночные обращения)
2. Подготовка: BotFather, API-ключ LLM, n8n Cloud vs self-host (HTTPS)
3. Сборка workflow: Telegram Trigger → AI Agent → Send Message
4. Память, system prompt и 1–2 tools (лиды, FAQ)
5. Голосовые сообщения и эскалация к менеджеру
6. Чеклист перед запуском в продакшен

**Internal link:** `/avtomatizaciya-n8n-ai-agents/` (B02) — «углубиться в AI Agent и RAG».

**Conversion:** мягкий CTA на AI-аудит / внедрение (site-brief), max 3, не подменяет шаги.

---

## 5. Workflow-схема (черновик для writer)

```text
Telegram Trigger (Message)
    → [Switch: voice / text / команда]
        → voice: Get File → Whisper → текст
        → text: AI Agent
            ├── Chat Model (OpenAI / Claude / OpenRouter)
            ├── Window Buffer Memory (Session Key = chat.id)
            └── Tools (1–2): Google Sheets FAQ | HTTP → CRM
    → Telegram Send Message (chat.id, ответ агента)
    → [опционально] Send and Wait → чат менеджера (handoff)
```

---

## 6. FAQ-кандидаты (7)

1. **Как подключить Telegram к n8n?** — BotFather `/newbot` → токен → credential в Telegram Trigger → Updates: Message → Activate workflow.
2. **Нужен ли HTTPS для Telegram-бота в n8n?** — да, webhook только HTTPS; Cloud trial или self-host с доменом и SSL.
3. **Какая модель лучше для Telegram-бота?** — старт: `gpt-4o-mini` или аналог (цена/скорость); сложная поддержка: GPT-4o / Claude Sonnet; локально: Ollama на том же сервере.
4. **Как добавить память диалога в n8n?** — Window Buffer Memory к AI Agent; Session Key = `{{ $json.message.chat.id }}`; длина окна 10–20 сообщений.
5. **Чем AI Agent отличается от ноды OpenAI?** — Agent сам выбирает tools; для FAQ/лидов нужен Agent, не одиночный «Message a Model».
6. **Как передать диалог менеджеру?** — кнопка «Связаться с менеджером» + Telegram Send and Wait или упрощённый handoff по шаблону n8n 3350.
7. **Сколько стоит запуск?** — n8n Cloud от 20 €/мес + API LLM отдельно; self-host CE бесплатно + VPS; ориентир полной системы ~$150/мес (fact-bank).

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «Telegram-бот с ИИ на n8n» 40–60 слов | Lead | «Это связка…» |
| Workflow ASCII/mermaid | H2-3 | Trigger → Agent → Send |
| Таблица Cloud vs self-host | H2-2 | 4–5 критериев |
| Чеклист продакшена 10+ пунктов | H2-6 | Да/нет |
| FAQ 7 | Конец | Ответы-действия |
| Island test | QA | Каждый H2 = подзадача + рекомендация |

**Целевые формулировки:** «telegram бот n8n», «telegram trigger n8n», «телеграм бот с ии без кода», «память диалога n8n», «чат бот telegram n8n».

---

## 8. Риски для writer

- Не выдумывать показы Wordstat — MCP недоступен.
- Не копировать mayai/neiropotok 1:1; не обещать CR/ROI без оговорки «в вашей нише зависит от трафика».
- Объём: 8 500–9 500 знаков (quality-blog).
- Без эмодзи; дефис вместо длинного тире; прямые кавычки.
- Min **5 нумерованных шагов** + **чеклист 10+** (utility gate статьи).
- Упомянуть Simple Memory + queue mode как предупреждение для self-host enterprise.
- CTA ≤ 3.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст и активирует Telegram-бота с ИИ в n8n (BotFather, Trigger, AI Agent с моделью и памятью, ответ в чат), подключит 1–2 tools для лидов или FAQ, при необходимости добавит ветку голоса и эскалацию менеджеру и пройдёт чеклист перед продакшеном.

**action_outline (для writer):**

1. **Создать бота в @BotFather** (`/newbot`), сохранить токен; отключить публичный доступ к токену.
2. **Выбрать хостинг n8n:** Cloud (14-day trial, HTTPS из коробки) или self-host с `WEBHOOK_URL` и SSL; зафиксировать выбор в таблице.
3. **Новый workflow:** Telegram Trigger → Updates **Message** → credential с токеном.
4. **Добавить AI Agent:** подключить Chat Model (API-ключ), написать **system prompt** (роль, тон, «не выдумывать цены», когда звать менеджера).
5. **Подключить Window Buffer Memory:** Session Key `{{ $json.message.chat.id }}`, окно 10–20 реплик.
6. **Добавить 1–2 Tool sub-nodes** (например Google Sheets «поиск FAQ» или HTTP webhook в CRM) с понятным description для LLM.
7. **Telegram Send Message:** Chat ID из trigger, текст из output AI Agent; протестировать в личном чате с ботом.
8. **Опционально:** Switch на voice → Whisper; кнопка/handoff через Send and Wait по мотивам workflow 3350.
9. **Чеклист продакшена:** fallback на непонятные фразы, Error Workflow, Max Iterations, лог `telegram_id`, кнопка менеджера, Activate + мониторинг Execution Log.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (10) |
| Wordstat MCP | ⚠️ недоступен (зафиксировано) |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| SERP gaps | ✅ |
| FAQ 7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + internal link B02.
