# Research notes — B06 «Как настроить мультиагентную систему в n8n: пошаговое руководство по оркестрации ИИ-агентов»

**topic_id:** B06  
**slug:** n8n-multi-agent-orkestraciya-2026  
**article_mode:** B (how-to + checklist)  
**research_date:** 2026-06-22  
**disclaimer:** Все даты, версии и статистика проверены на 22.06.2026.

---

## 1. SERP-обзор (WebSearch, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [blog.n8n.io/multi-agent-systems](https://blog.n8n.io/multi-agent-systems/) | Официальный tutorial (дек 2025) | Supervisor + email/RAG sub-agents; AI Agent Tool vs MCP; handover оптимизация; шаблон workflow | Англ.; мало про Router/Reflexion на одном canvas; нет чеклиста prod | Перевод 1:1 без русских примеров контрактов JSON |
| 2 | [blog.n8n.io/production-ai-playbook-complex-agent-patterns](https://blog.n8n.io/production-ai-playbook-complex-agent-patterns/) | Production playbook (2026) | AI Agent Tool vs Call n8n Workflow Tool; session ID shared/isolated; deterministic routing; шаблоны | Dev-ориентирован; нет «когда не нужен multi-agent» для бизнеса | Копировать exercise-структуру без адаптации под ЦА «Ковчег» |
| 3 | [wildbots.ru/.../multiagentnie-sistemi-na-n8n](https://wildbots.ru/ru/blog/multiagentnie-sistemi-na-n8n-orkestratsiya-llm-v-realnikh-paipla) | RU deep-dive (2026) | Граница pipeline vs MAS; паттерны Orchestrator/Router/Reflexion; JSON task_envelope; sub-workflow воркеры | Длинный opinion-тон; нет сравнения с Make | Непроверенные «prod» цифры без URL |
| 4 | [lpmotor.ru/.../ii-agenta-v-n8n](https://lpmotor.ru/articles/kak-sozdat-i-nastroit-ii-agenta-v-n8n-polnoe-rukovodstvo-2603) | Single-agent how-to | Близкий стек нод (System Message, Max Iterations) | **Не multi-agent** — один AI Agent | Путать тему B06 с B02 |
| 5 | [logicworkflow.com/.../n8n-multi-agent-orchestration](https://logicworkflow.com/blog/n8n-multi-agent-orchestration/) | EN orchestration guide | Supervisor/Router/Pipeline/Swarm; AI Agent Tool vs sub-workflow; error handling | EN; marketing-CTA агентства | Claim «−40% cost» без первичника |
| 6 | [hatchworks.com/.../multi-agent-solutions-in-n8n](https://hatchworks.com/blog/ai-agents/multi-agent-solutions-in-n8n/) | EN patterns | Single Responsibility; routing vs orchestrator; node map | Общие формулировки | Структура 1:1 |
| 7 | [mayai.ru/multiagentnaya-ii-sistema-dlya-biznesa](https://mayai.ru/multiagentnaya-ii-sistema-dlya-biznesa/) | RU workflow (CrewAI/n8n) | JSON-контракты ролей; max iterations Critic; 30+ test cases; human-in-the-loop | Фокус CrewAI + n8n вперемешку | Продажа «7 агентов ради моды» |
| 8 | [medium.com/.../n8n-ai-agent-tool-trap](https://medium.com/@thequickstartcreative/the-n8n-ai-agent-tool-trap-convenience-now-cost-later-473d1d56fea0) | Anti-pattern essay | Embedded vs modular sub-workflows; observability; prod maintainability | Нет пошаговой сборки | Только критика без инструкции |

**Паттерн SERP:** англоязычный канон — официальный n8n blog (multi-agent tutorial + Production AI Playbook). RU-выдача — wildbots, mayai, lpmotor (часто single-agent). Запрос «n8n multi agent» в DuckDuckGo preflight дал 0 результатов — intent смешан с EN-кластером «ai agent tool n8n».

**Intent:** how_to — читатель уже знает один AI Agent (см. B02) и хочет **оркестрацию 2–4 специалистов**: AI Agent Tool на canvas или sub-workflows, память, prod-отладка.

**Пробел для «Ковчег»:** русскоязычный **пошаговый** гайд именно по multi-agent (не повтор B02): выбор паттерна → сборка orchestrator + 2 sub-agents → memory/session → чеклист prod; честный блок «когда один агент лучше»; ссылка на B02 как prerequisite.

---

## 2. Яндекс Wordstat

**⚠️ WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в Cloud-среде (ListMcpResources: server not found). Точные объёмы ниже — из успешного прогона **B02** (MCP, регион 225, 11.06.2026) для кластера «n8n + агенты»; повторный вызов `wordstat_get_top_requests` для B06 рекомендуется после восстановления MCP.

Обновление токена (если при восстановлении MCP будет 401): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (релевантные фразы к B06)

| Фраза | Показы/мес | Источник |
|-------|------------|----------|
| n8n | 37 115 | B02 Wordstat, 11.06.2026 |
| n8n ai | 720 | B02 Wordstat |
| **n8n агенты** | **699** | B02 Wordstat (primary_query B06) |
| n8n ии | 553 | B02 Wordstat |
| автоматизация n8n | 539 | B02 Wordstat |
| ии агенты и n8n | 74 | B02 Wordstat |
| создание ии агента n8n | 52 | B02 Wordstat |
| автоматизация ии n8n | 56 | B02 Wordstat |
| ai агенты и автоматизация с n8n | 30 | B02 Wordstat |
| как создать ии агента в n8n | 17 | B02 Wordstat |

**EN-кластер (SERP, без RU Wordstat):** «n8n multi agent», «ai agent tool n8n» — сильная EN-выдача (n8n.io, dev.to, automationatlas.io); в RU-Вордstate отдельного хвоста не зафиксировано — покрывать через LSI в тексте.

### LSI для writer (Wordstat + SERP)

- ai agent tool node, tools agent, call n8n workflow tool  
- orchestrator workers, supervisor delegator, router pattern, reflexion critic  
- sub-workflow, execute workflow trigger, task envelope json  
- simple memory, session id, postgres chat memory, memory manager  
- max iterations, human in the loop, queue mode  
- мультиагентная система n8n, оркестрация ии агентов  
- langchain n8n, mcp tool vs sub-agent  

**SEO-стратегия:** primary «n8n агенты» (699) + head «n8n ai» (720); H2 под «мультиагентная система n8n», «оркестрация ии агентов n8n»; internal link на B02 «автоматизация n8n».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Multi-agent системы Anthropic: +90,2% к single-agent, но ~15× больше токенов; ~80% разницы в performance объясняется token usage | [blog.n8n.io/multi-agent-systems](https://blog.n8n.io/multi-agent-systems/) | 22.12.2025 | да |
| AI Agent node: autonomous system; **минимум один tool sub-node** обязателен | [docs.n8n.io/.../n8n-nodes-langchain.agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/) | 22.06.2026 | да |
| До n8n 1.82.0 были типы agent; сейчас все AI Agent работают как **Tools Agent** | [docs.n8n.io/.../n8n-nodes-langchain.agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/) | 22.06.2026 | да |
| Механизм multi-agent в n8n: **AI Agent Tool** — второй агент как tool первого | [blog.n8n.io/production-ai-playbook-complex-agent-patterns](https://blog.n8n.io/production-ai-playbook-complex-agent-patterns/) | 2026 | да |
| Production-паттерн: **Call n8n Workflow Tool** — sub-workflow как tool с независимым тестом и версионированием | [blog.n8n.io/production-ai-playbook-complex-agent-patterns](https://blog.n8n.io/production-ai-playbook-complex-agent-patterns/) | 2026 | да |
| Рекомендация n8n: **deterministic routing** (Switch) когда категория известна; agent routing — когда input ambiguous | [blog.n8n.io/production-ai-playbook-complex-agent-patterns](https://blog.n8n.io/production-ai-playbook-complex-agent-patterns/) | 2026 | да |
| Session ID: shared — специалист видит историю orchestrator; isolated — контекст только через tool call | [blog.n8n.io/production-ai-playbook-complex-agent-patterns](https://blog.n8n.io/production-ai-playbook-complex-agent-patterns/) | 2026 | да |
| Официальный tutorial: hierarchical MAS — main agent + email sub-agent + RAG sub-agent | [blog.n8n.io/multi-agent-systems](https://blog.n8n.io/multi-agent-systems/) | 22.12.2025 | да |
| Sub-agent vs MCP tool: sub-agent имеет свой system prompt, LLM и memory; MCP — только tool access | [blog.n8n.io/multi-agent-systems](https://blog.n8n.io/multi-agent-systems/) | 22.12.2025 | да |
| Multi-agent в n8n по умолчанию **sequential**; параллель — Execute sub-workflow / HTTP Request / LangChain Code | [blog.n8n.io/multi-agent-systems](https://blog.n8n.io/multi-agent-systems/) | 22.12.2025 | да |
| Coordination overhead: 3 агента — 3 связи; 10 агентов — 45 связей | [blog.n8n.io/multi-agent-systems](https://blog.n8n.io/multi-agent-systems/) | 22.12.2025 | да |
| n8n visual builder: **1000+ integrations**, MCP support | [blog.n8n.io/multi-agent-systems](https://blog.n8n.io/multi-agent-systems/) | 22.12.2025 | да |
| Много tool descriptions у одного агента увеличивают tokens на каждый request; при 15 tools и использовании ~3 — разбить на focused agents | [blog.n8n.io/production-ai-playbook-complex-agent-patterns](https://blog.n8n.io/production-ai-playbook-complex-agent-patterns/) | 2026 | да |
| n8n Cloud Starter: 20 €/мес (год), 2 500 executions; Pro: 50 €/мес, 10 000 executions | [n8n.io/pricing](https://n8n.io/pricing/) | 22.06.2026 | да |
| Execution = один полный прогон workflow, не каждый step | [n8n.io/pricing](https://n8n.io/pricing/) | 22.06.2026 | да |
| Cloud trial Starter/Pro: без карты; Business trial 14 дней | [n8n.io/pricing](https://n8n.io/pricing/) | 22.06.2026 | да |
| Hosted n8n: данные в EU (Frankfurt) | [n8n.io/pricing](https://n8n.io/pricing/) | 22.06.2026 | да |
| Business plan: Queue mode (multiple instances), worker view | [n8n.io/pricing](https://n8n.io/pricing/) | 22.06.2026 | да |
| Автономные ИИ-системы завершают <2,5% сложных неструктурированных задач без human-in-the-loop | [fact-bank.md / mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 11.06.2026 | да |
| ~40% пилотов автономных агентов отменяются из-за скрытых затрат и нулевого ROI | [fact-bank.md / mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 11.06.2026 | да |
| Пилот MAS: цель 30+ test-кейсов, max iterations у Critic, точка эскалации к человеку | [mayai.ru/multiagentnaya-ii-sistema-dlya-biznesa](https://mayai.ru/multiagentnaya-ii-sistema-dlya-biznesa/) | 2026 | да |

**Не использовать без первичника:** «−40% cost» (logicworkflow); «3 агента заменили отдел из 5» (braintools); произвольные лимиты «не больше N sub-agents» — только рекомендации n8n про tool count и coordination overhead.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** пошагово собрать **рабочую мультиагентную систему из 1 orchestrator + 2–3 specialist sub-agents** в n8n, выбрать между **AI Agent Tool** (один canvas, MVP) и **Call n8n Workflow Tool** (prod), настроить memory/session и пройти **чеклист отладки** перед запуском.

**Prerequisite:** один AI Agent уже собран — см. internal link B02.

**Почему отличается от конкурентов:**
- Официальный n8n tutorial — EN и supervisor+Gmail/RAG, без русского чеклиста prod.
- wildbots — глубоко, но без linear how-to для новичка «Ковчег».
- lpmotor/fulcrumlabs — single-agent, не B06.

**Tone:** практик; «orchestrator», «tool-agent», «session ID» — сразу «на пальцах». Блок «когда **не** строить multi-agent» обязателен (однородная задача = один agent + RAG).

**H2-каркас (из карточки + research):**
1. Когда одного AI Agent мало: Supervisor-Worker vs один бот (3 сценария + anti-pattern)
2. Архитектура на canvas: AI Agent Tool и роли специалистов
3. Пошаговая сборка orchestrator + sub-agents (Tools Agent, descriptions, JSON-конверт)
4. Память, session ID, изоляция контекста между агентами
5. Production: sub-workflows, Switch-routing, human-in-the-loop, Queue Mode (Business)
6. Чеклист отладки multi-agent workflow (10+ пунктов)

**Conversion (conversion-map.md):**
- CTA курс Make max 2× — только если сравнение «сложный n8n MAS vs Make AI Agents для простого кейса»
- Internal: `/avtomatizaciya-n8n-ai-agents/` (B02)

---

## 5. Паттерны оркестрации (черновик для writer)

| Паттерн | Когда | Ноды n8n |
|---------|-------|----------|
| Supervisor / Orchestrator-Workers | Динамическое делегирование, параллельные подзадачи | AI Agent + AI Agent Tool или Call n8n Workflow Tool |
| Router | Чёткие домены (support/billing/docs) | LLM classify + **Switch** (дешевле agent-routing) |
| Pipeline | Последовательные стадии (research → write → review) | Sub-workflows или цепочка agents |
| Reflexion | Нужно качество выхода | Worker + Critic + IF loop + **max iterations** |

**Workflow-схема для статьи:**

```text
Chat Trigger → Orchestrator AI Agent → (AI Agent Tool: Specialist A | B | C)
                                      ↘ Call n8n Workflow Tool → Sub-workflow workers
Human approval (optional) ← IF quality check ← merge results → ответ пользователю
```

---

## 6. FAQ-кандидаты (5–7)

1. **Как работает AI Agent Tool в n8n?** — sub-node orchestrator; полный agent (model, prompt, tools) вызывается как tool через function calling.
2. **Чем multi-agent отличается от одного агента с 10 tools?** — разные промпты/модели/память; меньше tool noise; выше coordination cost.
3. **Сколько sub-agents можно связать?** — технически много; практически 2–5 на MVP; coordination overhead растёт (10 agents = 45 связей).
4. **AI Agent Tool или sub-workflow?** — Tool для MVP на одном canvas; sub-workflow для prod, тестов, команд и версий.
5. **Как разделить память между агентами?** — isolated session ID + явный JSON context в tool call vs shared session для continuity.
6. **Когда использовать Switch вместо orchestrator?** — когда категория запроса формализуема (ticket type, keyword).
7. **Типичные ошибки multi-agent в n8n?** — нет tool descriptions, shared memory без нужды, нет max iterations у Critic, embedded agents без sub-workflow на prod.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «мультиагентная система в n8n» 40–60 слов | Lead | «Мультиагентная система в n8n — …» |
| Таблица паттернов (Supervisor/Router/Pipeline/Reflexion) | H2-1 | Сравнительная таблица + «выбирай если» |
| Workflow-схема orchestrator → sub-agents | H2-2 | ASCII `→` |
| Чеклист 10+ пунктов prod | H2-6 | Нумерованный checklist |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «n8n агенты», «мультиагентная система n8n», «оркестрация ии агентов n8n», «ai agent tool n8n».

---

## 8. Риски для writer

- Не дублировать B02 (первый single agent) — только prerequisite + ссылка.
- Не выдумывать Wordstat кроме таблицы с пометкой источника B02.
- Объём: 8 500–9 500 знаков (quality-blog).
- Min **5 нумерованных шагов** + **чеклист 10+** (utility gate статьи).
- Без эмодзи; дефис вместо длинного тире.
- Human-in-the-loop — стандарт (fact-bank <2,5% fully autonomous).

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель спроектирует паттерн оркестрации (Supervisor или Router), соберёт в n8n orchestrator с 2–3 specialist sub-agents через AI Agent Tool или Call n8n Workflow Tool, настроит session ID и descriptions, прогонит чеклист отладки и решит, оставить систему на одном canvas или вынести воркеров в sub-workflows для prod.

**action_outline (для writer):**

1. **Проверить prerequisite:** один AI Agent работает (B02); если задача однородная — остановиться на single agent + RAG.
2. **Выбрать паттерн:** Supervisor (динамика), Router+Switch (формализуемые категории) или Pipeline (стадии).
3. **Создать orchestrator:** Chat Trigger → AI Agent (Tools Agent) + Chat Model + System Message с явным списком sub-agents/tools.
4. **Добавить 2–3 specialist sub-agents:** через AI Agent Tool (MVP) или отдельные workflows + Call n8n Workflow Tool (prod); прописать **tool description** и JSON task envelope (task, context, expected_output).
5. **Настроить memory:** Simple Memory / Postgres на orchestrator; **isolated session ID** у specialists или shared — по сценарию из playbook.
6. **Ограничить риски:** max iterations у Critic/reflexion loop; human-in-the-loop node на критичных действиях; Continue on Error на tools.
7. **Протестировать 10–30 кейсов:** execution logs каждого sub-agent; замерить tokens (ожидать рост vs single agent).
8. **Оптимизировать:** Switch вместо LLM-routing где можно; ≤5 tools на agent; file_id вместо full content между agents.
9. **Prod checklist:** sub-workflows версионированы, error workflow, Queue Mode при нагрузке (Business self-hosted), документированные контракты JSON.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat | ⚠️ MCP недоступен; данные B02 + primary 699 |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| Отличие от B02 | ✅ (multi-agent, не первый agent) |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + B02 как prerequisite.
