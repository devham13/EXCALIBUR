# Research notes — B06 «Как настроить Make AI Agents: пошаговая инструкция для автоматизации бизнеса»

**topic_id:** B06  
**slug:** make-ai-agents-nastrojka-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-06-20  
**disclaimer:** Все даты, версии и статистика проверены на 2026-06-20 (2026 год).

---

## 1. SERP-обзор (WebSearch, 20.06.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [make.com/en/ai-agents](https://www.make.com/en/ai-agents) | Официальный продукт | 3000+ apps, Reasoning panel, FAQ «когда агент vs сценарий», кейсы | Нет пошаговой RU-инструкции | Сухой маркетинг без бизнес-кейса |
| 2 | [make.com/en/how-to-guides/build-ai-agents](https://www.make.com/en/how-to-guides/build-ai-agents) | Официальный how-to (апр 2025) | Канон: Create agent → tool-scenarios → Run an agent → Return output | Старая модель (отдельный раздел AI Agents), без next-gen canvas 2026 | Структуру 1:1; устаревший UI без Reasoning Panel |
| 3 | [make.com/en/blog/announcing-next-generation-make-ai-agents](https://www.make.com/en/blog/announcing-next-generation-make-ai-agents) | Официальный анонс (11.02.2026) | In-canvas agents, multi-modal, Library of Agents, in-canvas chat | Новости, мало «сделай сам» | Новостной угол без шагов |
| 4 | [mayai.ru/make-ai-agents-gayd-biznes](https://mayai.ru/make-ai-agents-gayd-biznes/) | RU how-to (экосистема автора) | Scenario Builder, Tools, Reasoning Panel, MCP, язык для no-code | Коммерческий хвост курса | Перегруз CTA; не копировать блоки 1:1 |
| 5 | [mayai.ru/sozdanie-ai-agenta-v-make-poshagovaya-instrukcziya-s-nulya](https://mayai.ru/sozdanie-ai-agenta-v-make-poshagovaya-instrukcziya-s-nulya/) | RU longread | Архитектура триггер-мозг-tools, Assistants API | Устаревший акцент на Assistants API vs Make AI Agents (New) | Устаревший стек без next-gen модулей |
| 6 | [growwstacks.com/blog/make-com-new-ai-agents-2026](https://growwstacks.com/blog/make-com-new-ai-agents-2026/) | EN tutorial 2026 | Hexagon-модуль, system prompt, memory, tool descriptions ≤240 символов | Сторонний блог, модели «GPT 5.2» без первичника Make | Непроверенные названия моделей |
| 7 | [stacksheriff.com/automation/make-ai-agents-tutorial](https://stacksheriff.com/automation/make-ai-agents-tutorial/) | EN tutorial | Operation-count traps, tool-calling loops | EN, bias к upsell | Цифры credits без help.make.com |
| 8 | [rutube.ru/video/9bfde0d1e3a65d6fa04a467d9b4dca84](https://rutube.ru/video/9bfde0d1e3a65d6fa04a467d9b4dca84/) | RU video | Визуальный walkthrough для RU-аудитории | Видео без текста, SEO-слабо | Транскрипт без переработки |

**Паттерн SERP:** по EN-запросу «make ai agents 2026» выдача смешивает generic AI agents (Claude, Microsoft Build) с продуктом Make; по RU/H1 — доминируют видео (Rutube, YouTube, VK) и mayai.ru. Официальный help.make.com по конфигурации есть, но контент в Archbee не индексируется полноценно. **Пробел:** русскоязычный пошаговый гайд next-gen Make AI Agents (Feb 2026) с чек-листом credits, guardrails и сравнением «агент vs сценарий» для B2B без кода.

**Intent:** `how_to` — собрать первого рабочего агента на канвасе Make, подключить tools/MCP, протестировать в Reasoning Panel и запустить в прод с лимитами.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **MCP WORDSTAT UNAVAILABLE:** инструмент `wordstat_get_top_requests` сервера `user-mcp-kv` недоступен в runtime Cloud Agent (MCP не подключён, env `YANDEX_*` / `WORDSTAT_*` отсутствуют). Точные показы в месяц **не получены** — цифры спроса в текст статьи не включать.

**Fallback (семантика из SERP + карточка темы, без выдуманных частот):**

| Кластер | Запросы / LSI | Интент |
|---------|---------------|--------|
| Product EN | make ai agents, make com ai agents | Навигационный + how-to по продукту Make |
| RU setup | make ai agents настройка, создание ai агента make | Чистый how-to |
| RU automation | make com автоматизация ии, make.com автоматизация | Шире: сценарии + ИИ; агент — подкластер |
| UI / фичи | reasoning panel make, make ai agents tools, make mcp server | Технический LSI для H2 |
| Сравнение | make ai agents vs n8n, make vs n8n ai agent | Comparison intent (связка с B02) |
| Бизнес | ai агент для бизнеса make, автоматизация бизнеса make | B2B pain → action |

**SEO-стратегия writer:** primary «make ai agents» в H1/lead + RU синонимы «настройка Make AI Agents», «создание AI-агента в Make»; secondary из карточки; internal link на B02 (`/avtomatizaciya-n8n-ai-agents/`) в блоке «когда Make, когда n8n».

**После восстановления MCP:** перезапросить `wordstat_get_top_requests` для: `make ai agents`, `make com`, `make com автоматизация`, `создание ai агента make`, `make.com ии`.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Make AI Agents доступны на **всех тарифах** | [make.com/en/ai-agents](https://www.make.com/en/ai-agents) | 20.06.2026 | да |
| Интеграции: **3000+ apps** для оркестрации агентами | [make.com/en/ai-agents](https://www.make.com/en/ai-agents) | 20.06.2026 | да |
| Код не нужен: агенты собираются в **visual builder** на том же канвасе, что и сценарии | [make.com/en/ai-agents](https://www.make.com/en/ai-agents) | 20.06.2026 | да |
| **Reasoning panel** показывает каждое решение агента на канвасе (не «чёрный ящик») | [make.com/en/blog/make-ai-agents-trust-through-transparency](https://www.make.com/en/blog/make-ai-agents-trust-through-transparency) | 20.06.2026 | да |
| Next-gen Make AI Agents анонсированы **11.02.2026**: in-canvas build/debug, multi-modal (PDF, CSV, images), Library of Agents | [make.com/en/blog/announcing-next-generation-make-ai-agents](https://www.make.com/en/blog/announcing-next-generation-make-ai-agents) | 20.06.2026 | да |
| In-canvas **chat** для теста и уточнения инструкций без выхода из Scenario Builder | [make.com/en/blog/announcing-next-generation-make-ai-agents](https://www.make.com/en/blog/announcing-next-generation-make-ai-agents) | 20.06.2026 | да |
| Агент vs сценарий: агент — когда нужны **суждение и неструктурированный ввод**; сценарий — когда «просто сделать» по правилам | [make.com/en/blog/when-to-use-ai-agents](https://www.make.com/en/blog/when-to-use-ai-agents) | 20.06.2026 | да |
| Пять паттернов агентов: conversational, synthesizer, routing, qualifier, orchestrator | [make.com/en/blog/make-ai-agents-trust-through-transparency](https://www.make.com/en/blog/make-ai-agents-trust-through-transparency) | 20.06.2026 | да |
| Tool = **сценарий Make** с **Return output** в конце; агент выбирает tool по name + description | [make.com/en/how-to-guides/build-ai-agents](https://www.make.com/en/how-to-guides/build-ai-agents) | 20.06.2026 | да |
| Scenario **outputs** (Return output + structured outputs) нужны для MCP и связки нескольких агентов | [make.com/en/blog/introducing-scenario-outputs](https://www.make.com/en/blog/introducing-scenario-outputs) | 20.06.2026 | да |
| Free: **1 000 credits/мес**, минимальный интервал между запусками **15 минут** | [make.com/en/pricing](https://www.make.com/en/pricing) | 20.06.2026 | да |
| Core **$12/мес**, Pro **$21/мес**, Teams **$38/мес** при 10k credits (monthly billing на странице pricing) | [make.com/en/pricing](https://www.make.com/en/pricing) | 20.06.2026 | да |
| Стандартный модуль = **1 credit** за действие (HTTP, Gmail, Sheets и т.д.) | [make.com/en/pricing](https://www.make.com/en/pricing) | 20.06.2026 | да |
| Billing unit с **августа 2025** — **credits** вместо operations (официальный переход) | [help.make.com/introducing-credits-new-billing-unit-live-in-make](https://help.make.com/introducing-credits-new-billing-unit-live-in-make) | 20.06.2026 | да |
| AI-модули могут потреблять **variable credits** (зависит от фичи/объёма) — см. How features use credits | [help.make.com/how-features-use-credits](https://help.make.com/how-features-use-credits) | 20.06.2026 | да (без фиксированного множителя в тексте) |
| Кейс: invoicing farmers **15 мин → менее 20 сек** на накладную (voice → Telegram/WhatsApp → agent) | [make.com/en/blog/make-ai-agents-cut-farmers-invoicing-time](https://www.make.com/en/blog/make-ai-agents-cut-farmers-invoicing-time) | 20.06.2026 | да |
| Кейс Celonis: снижение затрат на expense auditing **на 99,7%** с Make AI Agents | [make.com/en/success-stories/make-ai-agents-help-celonis-lower-expense-auditing-costs](https://www.make.com/en/success-stories/make-ai-agents-help-celonis-lower-expense-auditing-costs) | 20.06.2026 | да |
| Make.com: **2500+** нативных интеграций; переход на credits/Compute для медиа (контекст сравнения с n8n) | [fact-bank.md / mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 11.06.2026 | да |
| ~**40%** проектов автономных ИИ-агентов отменяются из-за скрытых затрат и нулевого ROI | [fact-bank.md / mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 11.06.2026 | да |
| Human-in-the-loop: автономные системы завершают **<2,5%** сложных неструктурированных задач без человека | [fact-bank.md / mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 11.06.2026 | да |
| Курс «Ковчег»: **5 800 ₽/мес**, **159+** уроков | [conversion-map.md / kv-ai.ru](https://kv-ai.ru/obuchenie-po-make) | 20.06.2026 | да |

**Не использовать без первичника Make:** «5 credits за вызов агента» (templates4make), «GPT 5.2 / Claude Opus 4.6» из сторонних блогов, «50–100 credits за run» — только как качественное предупреждение «сложный агент с несколькими tools съедает больше credits; смотрите Credit usage history».

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за одну сессию собрать **первого production-ready Make AI Agent (New)** на канвасе: выбрать LLM, написать Instructions, подключить 2–3 tools (модули + Call a scenario с Return output), протестировать в **Reasoning Panel / in-canvas chat**, обернуть триггером (Gmail/Webhook) и пройти **чек-лист guardrails** перед включением.

**Почему отличается от конкурентов:**
- Официальные посты Make — анонсы и EN-how-to без RU и без чек-листа credits/guardrails.
- RU-конкуренты часто пишут про Assistants API / старую архитектуру или продают курс без next-gen UI.
- «Ковчег»: практик Make, human-in-the-loop по умолчанию, связка с B02 (n8n vs Make), CTA max 2× на курс.

**Tone:** B2B no-code; Reasoning Panel, MCP, thread ID, Return output — сразу «на пальцах». Без hype «агент заменит отдел».

**H2-каркас (из blog-topics.md + research):**
1. Make AI Agents (New) в 2026: агент vs сценарий + когда не нужен агент
2. Подготовка: тариф, credits, Make AI provider vs свой API key
3. Сборка на канвасе: Instructions, Model, Knowledge (если нужно)
4. Tools: модули, Call a scenario, MCP; naming и descriptions
5. Тест: Reasoning Panel, in-canvas chat, типичные ошибки tool-calls
6. Прод: триггер Run an agent, лимиты, human approval, мониторинг credits

**Conversion:** CTA курс [kv-ai.ru/obuchenie-po-make](https://kv-ai.ru/obuchenie-po-make) max 2×; Telegram @maya_pro — 1× если уместно; internal link B02.

---

## 5. Workflow-схема (для writer)

```text
Триггер (Gmail / Webhook / Slack)
  → Make AI Agents: Run an agent (new)
       → [Reasoning Panel: выбор tool]
       → Tool A: Google Sheets (check data)
       → Tool B: Call scenario «notify_slack» (Return output)
  → Действие: ответ клиенту / запись в CRM
  → (опционально) Human approval на рискованные tools
```

---

## 6. FAQ-кандидаты (5–7)

1. **Чем Make AI Agents отличается от обычного сценария?** — Агент сам выбирает tools по контексту; сценарий идёт по фиксированным модулям. Действие: таблица «агент / сценарий» + правило из официального FAQ Make.
2. **Нужен ли код?** — Нет; visual builder. Действие: зарегистрироваться, открыть Scenario Builder.
3. **Как подключить CRM/Sheets/Telegram?** — Add tool → модуль или scenario-on-demand с Return output.
4. **Сколько тратится credits?** — Стандартный модуль 1 credit; AI-фичи variable; смотреть Credit usage history, не гадать.
5. **Make AI Agents vs n8n AI Agent?** — Make: SaaS, 3000+ apps, Reasoning panel; n8n: self-host, executions. Ссылка на B02.
6. **Что делать, если агент вызывает не тот tool?** — Уточнить Instructions и descriptions (≤240 символов), убрать лишние tools, смотреть Reasoning Panel.
7. **Когда нужен human-in-the-loop?** — Любые платежи, удаление данных, публикации от имени компании; approval-модуль или стоп-флаг.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «Make AI Agent» 40–60 слов | Lead | «Make AI Agent — …» |
| Таблица «агент vs сценарий» | H2-1 | 2 колонки + рекомендация |
| Workflow ASCII / mermaid | H2-3–5 | Триггер → Run agent → Tools |
| Чек-лист продакшена 10+ пунктов | H2-6 | Guardrails, credits, approval |
| FAQ 5–7 | Конец | Ответы-действия |
| E-E-A-T | Автор | Практик Make, курс «Ковчег» |

**Целевые формулировки:** make ai agents, make ai agents настройка, создание ai агента make, make com автоматизация ии, reasoning panel make.

---

## 8. Риски для writer

- Не писать article.html на этом шаге.
- Не выдумывать Wordstat-частоты и фиксированную цену credits за AI Agent run.
- Не копировать mayai.ru / growwstacks 1:1.
- Объём: 8 500–9 500 знаков (quality-blog).
- Без эмодзи; дефис вместо длинного тире; прямые кавычки.
- Min **5** нумерованных шагов + чеклист **10+** пунктов (utility gate статьи).
- Акцент на **Make AI Agents (New)** Feb 2026, не на deprecated Eden AI / чистый Assistants API как основной путь.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст и протестирует первого Make AI Agent на канвасе (Instructions, Model, 2–3 tools, Return output), отладит поведение через Reasoning Panel, подключит триггер для бизнес-кейса (поддержка/лиды/отчёты) и включит прод только после чек-листа credits и human approval.

**action_outline (для writer):**

1. **Выбрать кейс и проверить fit:** неструктурированный ввод (письмо, сообщение, PDF) → агент; фиксированный пайплайн → обычный сценарий.
2. **Подготовить аккаунт Make:** тариф (Free 1k credits или Core+), подключить LLM (Make AI provider или свой API key на Pro+).
3. **Создать сценарий-триггер** (Gmail Watch / Webhook) и добавить модуль **Make AI Agents (New) → Run an agent**.
4. **Create agent на канвасе:** имя, **Instructions** (роль, лимиты, формат ответа, «только через tools»).
5. **Выбрать Model** (large для multi-step, small для классификации; переключить после теста).
6. **Add tool:** 1–2 модуля (Sheets, Slack) + **Call a scenario** с on-demand сценарием и **Return output** / structured scenario outputs.
7. **Тест in-canvas chat + Reasoning Panel:** 3 промпта (норма, edge case, off-topic); править descriptions tools.
8. **Собрать prod-сценарий:** map message → Run agent → ответ/CRM; **thread ID** для контекста диалога где поддерживается.
9. **Чек-лист перед Active:** лимиты credits, убрать лишние tools, approval на рискованные действия, мониторинг Credit usage history.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ fallback SERP (MCP недоступен) |
| Таблица фактов с URL | ✅ (18 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + `conversion-map.md`.
