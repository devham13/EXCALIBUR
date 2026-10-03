# Research notes — B06 «Как настроить n8n Agents в 2026: standalone-агент, Slack, расписание и workflows как tools»

**topic_id:** B06  
**slug:** nastroyka-n8n-agents-2026  
**article_mode:** B (how-to)  
**search_intent:** how_to  
**research_date:** 2026-10-03  
**disclaimer:** Все даты, версии и статистика проверены на 03.10.2026 (Europe/Moscow).

---

## 1. SERP-обзор (WebSearch + research-serp.json, актуализация 03.10.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [blog.n8n.io/introducing-n8n-agents](https://blog.n8n.io/introducing-n8n-agents/) | Официальный launch (25.09.2026) | Канон: Agents vs workflows, tools (MCP / nodes / workflows), Slack/schedule, Message an Agent, pricing turn=execution | Нет пошагового скрина Agents tab на русском | Пересказ без практики «сделай сам» |
| 2 | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents/) | Официальная дока | Agent Builder, draft/publish, channels, schedules, self-host env, preview | Сухой EN, мало бизнес-контекста для РФ | Копировать структуру docs 1:1 |
| 3 | [community.n8n.io/t/306323](https://community.n8n.io/t/introducing-n8n-agents-a-new-way-to-build-agents-you-set-up-once-and-use-anywhere/306323) | FAQ от команды | Отличие AI Agent node vs Agent, rollout 2.32.3+, self-hosted Beta | Форум EN | Устаревшие версии без сверки с docs |
| 4 | [habr.com/ru/companies/polzaai/articles/1070604](https://habr.com/ru/companies/polzaai/articles/1070604/) | RU longread | Установка, первый AI Agent в workflow, массовый охват | **Не про новый продукт n8n Agents** (фокус на AI Agent node) | Путать два продукта в одной статье |
| 5 | [qantcore.space/guide/ai-agenty-v-n8n](https://qantcore.space/guide/ai-agenty-v-n8n/) | RU how-to | Шаблоны, безопасность self-host | Workflow-агент, не Agents tab | Без блока Slack + schedule + publish |
| 6 | [meta-journal.ru/.../n8n-multi-agent-orkestraciya-2026](https://www.meta-journal.ru/2026/06/22/n8n-multi-agent-orkestraciya-2026/) | Multi-agent | Orchestrator / sub-agents в canvas | Другой паттерн (LangChain в workflow) | Смешивать с standalone Agents без пояснения |
| 7 | [nordflux.de/ru/guides/sozdanie-ii-agenta-s-n8n](https://nordflux.de/ru/guides/sozdanie-ii-agenta-s-n8n-poshagovaya-instruktsiya) | RU инструкция | Пошаговость | Классический AI Agent node | — |
| 8 | [mayai.ru/n8n-gayd-biznes-ai-agenty-mcp](https://mayai.ru/n8n-gayd-biznes-ai-agenty-mcp/) | Курс/гайд | MCP, бизнес-угол | Не закрывает H1 (Agents tab, Message an Agent) | Агрессивный sales без utility |

**Паттерн SERP (октябрь 2026):** русскоязычная выдача по «n8n агенты» всё ещё dominated гайдами про **AI Agent node внутри workflow**. Официальный запуск **n8n Agents** (отдельный артефакт, Agents tab, publish, channels) попадает в EN (blog, docs, community). **Intent how_to:** пользователь хочет «настроить агента» и часто не различает node vs Agents — статья должна явно развести и дать пошаговый сценарий под H1.

**Пробел для блога:** один связный гайд: создать standalone-агента → Preview → опубликовать → Slack + cron → подключить 1–2 workflow как tools → вызвать из automation через Message an Agent → чеклист preview/безопасности 2026.

**Internal link (карточка):** `/avtomatizaciya-n8n-ai-agents/` (B02 — AI Agent node; B06 — новый Agents product, без каннибализации если развести в lead).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` в этой Cloud-сессии недоступен (namespace not found). Точные **показы/мес** из API **не получены**. Обновите токен/подключение MCP и вызовите `wordstat_get_top_requests` для primary и secondary. При 401: [OAuth Yandex](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40).

**Семантический приоритет (из SERP + карточки темы, без цифр спроса):**

| Кластер | Запросы writer |
|---------|----------------|
| Head | n8n, n8n ai |
| Primary | n8n агенты, n8n agents настройка |
| Secondary (карточка) | n8n ai, создание ии агента n8n, n8n cloud agents |
| Product LSI | n8n agents tab, agent builder, message an agent, workflows as tools, publish agent, preview n8n agents |
| Channels | n8n agents slack, расписание агента n8n, cron agent n8n |
| Safety | approval tool calls, per-tool credentials, max iterations (node), preview status 2026 |

**Архив (только ориентир, перепроверить через MCP):** в research B02 от 11.06.2026 фиксировалось «n8n агенты» ≈699 пок/мес, «n8n ai» ≈720, head «n8n» ≈37k — **не использовать как актуальные цифры** до нового вызова Wordstat.

---

## 3. Таблица фактов (цифры и версии только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| n8n Agents анонсированы 25.09.2026; агент описывается текстом, выбираются model, tools и workflows | [blog.n8n.io/introducing-n8n-agents](https://blog.n8n.io/introducing-n8n-agents/) | 2026-09-25 | да |
| Один turn агента = **one execution**; вызовы tools к workflows и sub-agents **не считаются отдельно**; квота общая с workflows | [blog.n8n.io/introducing-n8n-agents](https://blog.n8n.io/introducing-n8n-agents/) | 2026-09-25 | да |
| Сборка через n8n Assistant расходует **AI credits** (как любой диалог Assistant) | [blog.n8n.io/introducing-n8n-agents](https://blog.n8n.io/introducing-n8n-agents/) | 2026-09-25 | да |
| Функция **Preview** (beta): тестировать до publish; держать approvals на чувствительных tools | [blog.n8n.io/introducing-n8n-agents](https://blog.n8n.io/introducing-n8n-agents/) | 2026-09-25 | да |
| Cloud: Agents на latest stable; self-hosted Community — с доп. setup; Enterprise — preview с governance «on the way» (формулировка launch post) | [blog.n8n.io/introducing-n8n-agents](https://blog.n8n.io/introducing-n8n-agents/) | 2026-09-25 | да |
| Agents: **Cloud все планы**; self-hosted с **n8n 2.32.3+**; **не** на self-hosted Enterprise (docs на 03.10.2026) | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents/) | 2026-10-03 | да |
| Статус **Preview**; поведение может меняться; на self-hosted knowledge base тоже Preview | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents/) | 2026-10-03 | да |
| Agent Builder: Model, Instructions, Tools, Skills, Knowledge, Memory, Sub-agents в draft; **Channels и Schedules** работают после **Publish** | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents/) | 2026-10-03 | да |
| Tools: built-in integrations, **workflows в том же project**, custom JSON schema, **MCP servers** | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents/) | 2026-10-03 | да |
| Channels (docs): **Slack, Telegram, Linear**; в launch post также **Discord** и schedule | [docs.n8n.io](https://docs.n8n.io/build/build-and-manage-agents/) + [blog](https://blog.n8n.io/introducing-n8n-agents/) | 2026-10-03 | да (указать расхождение: Discord — в анонсе) |
| Schedules: hourly, daily, weekly, monthly, **custom cron**; только **published** версия | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents/) | 2026-10-03 | да |
| **Message an Agent** node: workflow шлёт сообщение опубликованному агенту; 1 message = 1 execution | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents/) | 2026-10-03 | да |
| Self-host manual: `agents` в **N8N_ENABLED_MODULES**; full experience: **instance-ai**, **WEBHOOK_URL** для channels, Daytona для KB | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents/) | 2026-10-03 | да |
| **Queue mode не поддерживается** для agents; channels (Telegram) могут падать — regular mode | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents/) | 2026-10-03 | да |
| Knowledge: csv, pdf, markdown, txt; Cloud — да; self-hosted — Daytona sandbox | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents/) | 2026-10-03 | да |
| Episodic memory требует **OpenAI credential** | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents/) | 2026-10-03 | да |
| Sensitive tools: **Approve / Reject** перед запуском | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents/) | 2026-10-03 | да |
| AI Agent node **не изменён**; старые workflow продолжают работать | [blog.n8n.io/introducing-n8n-agents](https://blog.n8n.io/introducing-n8n-agents/) | 2026-09-25 | да |
| Standalone Agent vs AI Agent node: agent живёт в project, своя memory/sessions; node — только внутри одного workflow | [community.n8n.io/t/306323](https://community.n8n.io/t/introducing-n8n-agents-a-new-way-to-build-agents-you-set-up-once-and-use-anywhere/306323) | 2026-08-05 | да |
| Cloud rollout: Preview с **2.32.3**, рекомендация **2.34.x**; phased rollout — Agents tab может появиться с задержкой | [community.n8n.io/t/306323](https://community.n8n.io/t/introducing-n8n-agents-a-new-way-to-build-agents-you-set-up-once-and-use-anywhere/306323) | 2026-08-05 | да |
| Cloud Starter **20 €/mo** (annual): Agents preview, **1 600** Assistant credits/mo, AI без своих API keys (Gateway) | [n8n.io/pricing](https://n8n.io/pricing/) | 2026-10-03 | да |
| Execution = один полный прогон workflow **или** один turn агента; не per-step | [n8n.io/pricing](https://n8n.io/pricing/) + docs Agent executions | 2026-10-03 | да |
| Tools Agent node (legacy path): **Max Iterations**, System Message, human review на tools (Chat/Slack/Telegram) | [docs.n8n.io/.../tools-agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent/) | 2026-10-03 | да (для сравнения / fallback) |
| Self-hosted n8n снижает накладные на медиа vs cloud SaaS; маржинальность контент-производства до **+35%** (контекст автomation) | [fact-bank / mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 2026-06-11 | да |
| Базовый стек API + no-code (Make, n8n) ~**$150/мес** (ориентир бюджета) | [fact-bank / mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026-06-11 | да (осторожно: не «цена n8n Agents») |

**Не использовать без первичника:** прогноз Gartner «40% приложений к концу 2026» из Habr/PolzaAI — только если writer найдёт первичный отчёт Gartner; цифры «10 tools ломают модель» — маркeting paraphrase без URL.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** пошагово пройти **новый продукт n8n Agents** (не заменяя B02): создать агента во вкладке Agents → настроить model + instructions + минимальный набор tools → **опубликовать** → подключить **Slack** и **расписание** → добавить **готовый workflow как tool** (write-safe паттерн) → из другого workflow вызвать агента через **Message an Agent** → пройти **preview-чеклист 2026** (approvals, квота executions, Preview status).

**reader_outcome:** Читатель опубликует standalone n8n Agent, подключит Slack и cron-задачу, даст агенту безопасный доступ к бизнес-логике через workflow-tools и сможет встроить того же агента в существующую automation через Message an Agent.

**Отличие от конкурентов:** явное сравнение **Agents vs AI Agent node** + фокус на publish/channels/schedules/workflows-as-tools (официальный launch), а не пересказ Docker + Telegram node tutorial.

**H2-каркас (из blog-topics.md + research):**

1. Agents vs AI Agent node — когда что выбирать (таблица + рекомендация).
2. Первый агент: Agents tab → Create Agent → model → instructions → tools → Preview в Chat UI.
3. Publish, draft vs published, откат версии.
4. Slack (и при необходимости Telegram) как channel.
5. Schedules: daily/cron, только published agent.
6. Workflows as tools + sub-agents; паттерн «CRM note workflow» без прямых write-credentials у агента.
7. Message an Agent из workflow + переиспользование одной published версии.
8. Чеклист безопасности и preview-ограничений 2026 (approvals, executions, queue mode, self-host env).

**Tone:** практик, без «замените сотрудников»; Human-in-the-loop на destructive actions.

**FAQ hints (карточка):** как создать ии агента в n8n; чем agents отличается от ai agent node; slack; стоимость turn в cloud.

---

## 5. Workflow-схема (для writer)

```text
[Agents tab: Create Agent] → draft (model + instructions + tools)
    → Preview (Chat UI, sessions log)
    → Publish
        ├─ Channel: Slack
        ├─ Schedule: cron «утренний triage»
        └─ Tool: Workflow «Add CRM note only»
[Existing workflow] → Message an Agent → published agent → reply to next node
```

---

## 6. FAQ-кандидаты (ответы-действия)

1. **Чем n8n Agents отличается от AI Agent node?** — Agent: один раз в Agent Builder, publish, Slack/schedule/несколько workflows; node: только внутри одного workflow run.
2. **Нужен ли publish для Slack?** — да, channels и schedules работают на published версии; draft правьте через Preview.
3. **Сколько стоит один диалог в Cloud?** — один turn = one execution из общей квоты плана; см. pricing + docs.
4. **Можно ли дать агенту доступ к CRM?** — через workflow-tool с узкими правами и approval, не прямой credential на агенте.
5. **Self-hosted: почему нет Agents tab?** — версия 2.32.3+, `N8N_ENABLED_MODULES=agents`, проверить rollout/docs Enable agents.
6. **Можно ли в queue mode?** — нет, для agents пока regular mode (docs warning).

---

## 7. GEO hooks

| Hook | Где |
|------|-----|
| Определение «n8n Agent (2026)» 40–60 слов | Lead |
| Таблица Agents vs AI Agent node | H2-1 |
| Workflow ASCII (раздел 5) | H2-6–7 |
| Таблица типов tools (MCP / node / workflow) | H2-2 или H2-6 |
| FAQ 5–6 | конец |
| Island test | каждый H2 = подзадача + «делать / не делать» |

---

## 8. Риски для writer

- **Не путать** B06 (Agents product) и B02 (AI Agent node в workflow) — internal link с явным disambiguation.
- Не обещать Enterprise self-hosted Agents «уже в prod» — сверять docs (Enterprise coming / preview).
- Цены Cloud — только с n8n.io/pricing; turn=execution — с blog/docs.
- Preview: писать «тестируйте до publish», не «enterprise-ready без оговорок».
- Wordstat: не вставлять выдуманные показы; после MCP — обновить раздел 2.
- Объём и slop: `shared/quality-blog.md`, utility gate статьи (5+ шагов, чеклист).

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**action_outline (для writer):**

1. **Проверить доступ:** Cloud (latest) или self-host ≥2.32.3 с модулем `agents`; убедиться, что видна вкладка **Agents** (иначе обновить версию / подождать rollout).
2. **Create Agent:** имя, icon, **Model** (Gateway credits или свой API key).
3. **Instructions:** роль, tone, когда звать tools, запреты (не выдумывать данные, эскалация человеку).
4. **Tools (минимум):** один built-in read-only + один **workflow-tool** «узкая write-операция» с отдельными credentials.
5. **Preview:** прогнать 3–5 реплик, открыть **Sessions** → проверить tool calls; включить **approval** на опасный tool.
6. **Publish** snapshot; убедиться, что draft можно править без изменения production.
7. **Channel Slack:** подключить, протестировать thread/conversation из docs; не production-inbox на первый день.
8. **Schedule:** daily или custom cron с чётким objective; проверить last/next run в UI.
9. **Workflow integration:** в отдельном workflow добавить **Message an Agent**, передать контекст ticket/lead, использовать ответ в следующих nodes; при изменении агента — republish и проверить все callers.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8+) |
| Wordstat MCP | ⚠️ недоступен (см. §2) |
| Таблица фактов с URL | ✅ (22+ факта) |
| utility_verdict + reader_outcome + action_outline | ✅ |
| FAQ | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `memory/brief/site-brief.md` + `fact-bank.md`.
