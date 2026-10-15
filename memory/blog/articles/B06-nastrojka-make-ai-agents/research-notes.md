# Research notes — B06 «Как настроить Make AI Agents: пошаговое руководство по созданию агента с инструментами»

**topic_id:** B06  
**slug:** nastrojka-make-ai-agents  
**article_mode:** B (how-to)  
**research_date:** 2026-09-12  
**disclaimer:** Все даты, версии и статистика проверены на 12.09.2026.

---

## 1. SERP-обзор (WebSearch, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [help.make.com/introduction-to-make-ai-agent-new](https://help.make.com/introduction-to-make-ai-agent-new) | Официальный intro (Jul 2026) | Канон: релиз 02.02.2026, open beta, когда agent vs scenario vs AI app, core concepts | Нет полного пошагового кейса «с нуля до prod» | Сухой перевод docs без «на пальцах» |
| 2 | [help.make.com/create-your-first-ai-agent](https://help.make.com/create-your-first-ai-agent) | Официальный how-to (Jul 2026) | 6 шагов: plan → scenario → configure → tools → knowledge → test; MCP, sub-agents, RAG | Английский; нет русскоязычного контекста для ЦА «Ковчег» | Структуру 1:1 без адаптации под бизнес-кейс |
| 3 | [mayai.ru/make-ai-agents-gayd-biznes](https://mayai.ru/make-ai-agents-gayd-biznes/) | RU гайд (2026) | Reasoning Panel, MCP, system prompt, tools на русском | Коммерческий bias; нет таблицы credits | Продажный тон; непроверенные цифры ROI |
| 4 | [mayai.ru/sozdanie-ai-agenta-v-make-poshagovaya-instrukcziya-s-nulya](https://mayai.ru/sozdanie-ai-agenta-v-make-poshagovaya-instrukcziya-s-nulya/) | RU пошаговый (2026) | Близко к H1, 10 шагов для новичков | Мало про credits и guardrails | Дублирование mayai без уникального угла |
| 5 | [stacksheriff.com/automation/make-ai-agents-tutorial](https://stacksheriff.com/automation/make-ai-agents-tutorial/) | EN tutorial (2026) | Tool-calling loops, pricing traps, operation count | Нет RU; фокус на EN-аудиторию | Копировать pricing без сверки с help.make.com |
| 6 | [silentinfotech.com/blog/ai-9/make-com-ai-agents-explained-650](https://silentinfotech.com/blog/ai-9/make-com-ai-agents-explained-650) | EN «What changed 2026» | 8-step checklist, agent vs scenario на canvas | Агентский blog, нет triage-кейса | Pre-build checklist 1:1 |
| 7 | [make.com/en/how-to-guides/how-to-use-an-ai-agent-to-sort-emails](https://www.make.com/en/how-to-guides/how-to-use-an-ai-agent-to-sort-emails) | Официальный use case | Gmail triage: system prompt, tools, labels; Core+ для prod | Узкий кейс (email sort) | Перегрузить статью только email-кейсом |
| 8 | [baeseokjae.github.io/posts/make-ai-agents-guide-2026](https://baeseokjae.github.io/posts/make-ai-agents-guide-2026/) | EN community guide | Maia, multimodal, reasoning panel | Не primary source | Цифры без URL на help.make.com |

**Паттерн SERP:** топ — официальная документация Make (Feb–Jul 2026) + русскоязычные гайды mayai.ru + EN tutorials. Видео (YouTube, Rutube) — вторичный формат. Запрос «make ai agents настройка» пересекается с общими «как создать AI-агента 2026» (n8n, no-code) — writer должен держать фокус на **Make AI Agent (New)**, не размывать в общий обзор платформ.

**Intent:** how_to — пользователь хочет собрать первого агента в Make: провайдер, instructions, tools (модули / сценарии / MCP), knowledge (RAG), тест и запуск.

**Пробел для «Ковчег»:** связный RU-гайд от практика Make с чеклистом credits, guardrails (approval после agent), сравнением «agent vs линейный scenario» и ссылкой на `/avtomatizaciya-n8n-ai-agents/` для читателей, выбирающих платформу.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в текущей сессии (namespace не найден). Точные объёмы спроса **не получены**. Ниже — семантика из SERP и карточки темы; writer не должен указыать «X показов/мес» без повторного прогона Wordstat.

**Экспертная семантика (без цифр спроса):**

| Кластер | LSI-фразы |
|---------|-----------|
| Primary | make ai agents настройка, make ai agents как создать |
| Product | make.com ai agents инструкция, Make AI Agent New, Run an agent |
| Tools | агент make сценарии инструменты, Call a scenario, MCP make |
| Concepts | system prompt instructions, reasoning panel, knowledge RAG |
| Comparison | make ai agents vs scenario, make vs n8n ai agent |

**SEO-стратегия:** primary «make ai agents настройка» в H1/lead; secondary в H2/H3; не каннибализировать B02 (n8n) — один блок «когда n8n, когда Make» со internal link.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Make AI Agent (New) выпущен **2 февраля 2026** | [help.make.com/introduction-to-make-ai-agent-new](https://help.make.com/introduction-to-make-ai-agent-new) | 03.07.2026 | да |
| Статус продукта: **open beta**; функции и тарификация могут меняться | [help.make.com/introduction-to-make-ai-agent-new](https://help.make.com/introduction-to-make-ai-agent-new) | 03.07.2026 | да |
| Доступен на **всех тарифах** с Make's AI Provider; custom AI provider — на **paid plans** | [help.make.com/introduction-to-make-ai-agent-new](https://help.make.com/introduction-to-make-ai-agent-new) | 03.07.2026 | да |
| Make AI Agents работают с **3000+ apps** | [make.com/en/ai-agents](https://www.make.com/en/ai-agents) | 12.09.2026 | да |
| Агент живёт **внутри scenario** на том же canvas, что и модули | [help.make.com/create-your-first-ai-agent](https://help.make.com/create-your-first-ai-agent) | 20.07.2026 | да |
| Модуль: **Make AI Agent (New) > Run an agent** | [help.make.com/create-your-first-ai-agent](https://help.make.com/create-your-first-ai-agent) | 20.07.2026 | да |
| **Reasoning** — пошаговое мышление агента для отладки | [help.make.com/introduction-to-make-ai-agent-new](https://help.make.com/introduction-to-make-ai-agent-new) | 03.07.2026 | да |
| Tools: **модули**, **scenarios** (Call a scenario), **MCP servers**, **sub-agents** | [help.make.com/create-your-first-ai-agent](https://help.make.com/create-your-first-ai-agent) | 20.07.2026 | да |
| **Agent nesting** — только **1 уровень** (sub-agent не может иметь sub-agent) | [help.make.com/create-your-first-ai-agent](https://help.make.com/create-your-first-ai-agent) | 20.07.2026 | да |
| Knowledge хранится в **RAG vector database**; форматы: **JSON, TXT, CSV, PDF** | [help.make.com/create-your-first-ai-agent](https://help.make.com/create-your-first-ai-agent) | 20.07.2026 | да |
| **Step timeout** по умолчанию: **300 секунд (5 минут)** | [help.make.com/create-your-first-ai-agent](https://help.make.com/create-your-first-ai-agent) | 20.07.2026 | да |
| Scenario-tool должен заканчиваться **Return outputs**; on-demand toggle для вызова агентом | [help.make.com/create-your-first-ai-agent](https://help.make.com/create-your-first-ai-agent) | 20.07.2026 | да |
| **Run an agent** с Make's AI Provider: **1 credit/operation + credits по AI tokens** | [help.make.com/credit-usage-for-ai-agents](https://help.make.com/credit-usage-for-ai-agents) | 08.09.2026 | да |
| **Run an agent** с custom AI provider: **1 credit/operation** (tokens — провайдеру) | [help.make.com/credit-usage-for-ai-agents](https://help.make.com/credit-usage-for-ai-agents) | 08.09.2026 | да |
| **Chat**: 1 credit/operation + 1 credit за каждый вызванный tool (+ tokens при Make AI Provider) | [help.make.com/credit-usage-for-ai-agents](https://help.make.com/credit-usage-for-ai-agents) | 08.09.2026 | да |
| Knowledge PDF/DOCX upload: 1 credit/operation + **10 tokens/page** + embedding (Make AI Provider) | [help.make.com/credit-usage-for-ai-agents](https://help.make.com/credit-usage-for-ai-agents) | 08.09.2026 | да |
| Billing unit с **27 августа** — **credits** (не operations) | [make.com/en/pricing](https://www.make.com/en/pricing) | 12.09.2026 | да |
| Free: **1 000 credits/мес**, **15-min** minimum interval между runs | [make.com/en/pricing](https://www.make.com/en/pricing) | 12.09.2026 | да |
| Free: **2 active scenarios** (из how-to email sort guide) | [make.com/en/how-to-guides/how-to-use-an-ai-agent-to-sort-emails](https://www.make.com/en/how-to-guides/how-to-use-an-ai-agent-to-sort-emails) | 12.09.2026 | да |
| Agent для **flexible reasoning**; AI app — predefined logic + AI content; standard scenario — fixed I/O | [help.make.com/introduction-to-make-ai-agent-new](https://help.make.com/introduction-to-make-ai-agent-new) | 03.07.2026 | да |
| Не делегировать агенту: sensitive data, high-stakes finance, strict legal | [help.make.com/introduction-to-make-ai-agent-new](https://help.make.com/introduction-to-make-ai-agent-new) | 03.07.2026 | да |
| AI Agents API endpoints в **open beta** (create/update/delete/run) | [developers.make.com/api-documentation/api-reference/ai-agents](https://developers.make.com/api-documentation/api-reference/ai-agents) | 12.09.2026 | да |
| Module tools vs scenarios: module — быстрый 1-step; scenario — multi-step + filters + I/O | [help.make.com/tools-for-ai-agents](https://help.make.com/tools-for-ai-agents) | 12.09.2026 | да |
| Make.com >2500 integrations (fact-bank); pricing page: **3000+ apps** | [memory/brief/fact-bank.md](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) + [make.com/en/pricing](https://www.make.com/en/pricing) | 12.09.2026 | да (уточнить «3000+» как на pricing) |

**Не использовать без первичника:** конкретные $/мес Core/Pro из сторонних обзоров (comparedge, pondero) — только если writer сверит актуальную страницу make.com/en/pricing на дату публикации.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** пошагово собрать **первого рабочего Make AI Agent (New)** на canvas: trigger → Run an agent → instructions → 2–3 tools → knowledge → тест в Chat/Reasoning → guardrails перед prod.

**Почему отличается от конкурентов:**
- Официальные docs — на английском, без русского «на пальцах» и без блока credits.
- mayai.ru — сильные кейсы, но перегружены контент-заводом; мало универсального workflow triage/lead.
- «Ковчег»: один сквозной бизнес-кейс (например, triage заявок из формы/Slack), чеклист credits, internal link на B02 для comparison.

**Tone:** по-человечески; MCP, RAG, reasoning — сразу простым языком. Без «Maia» как бренда LLM, если нет в официальных docs (использовать «Make's AI Provider»).

**H2-каркас (из карточки + research):**
1. Когда выбирать Make AI Agents вместо линейного сценария
2. Создание агента: LLM-провайдер, instructions и лимиты (step timeout, nesting)
3. Подключение tools: модули, Call a scenario, MCP
4. Front-end сценария: trigger (Webhook/Slack/Gmail) + structured output (response format)
5. Knowledge (RAG), тест в Chat + Reasoning, чеклист перед production

**Conversion:**
- CTA курс Make: max 2× → kv-ai.ru/obuchenie-po-make
- Internal link: `/avtomatizaciya-n8n-ai-agents/` (B02)

---

## 5. Agent vs Scenario vs AI app (черновик таблицы для writer)

| Тип | Когда использовать | Пример |
|-----|-------------------|--------|
| **Standard scenario** | Fixed logic, same output for same input | Sync CRM ↔ Sheets |
| **Scenario + AI app** | Predefined steps + AI-generated content | Translate, summarize |
| **Scenario + AI Agent** | Judgment, variable I/O, tool choice | Ticket triage, lead research |

---

## 6. FAQ-кандидаты (7)

1. **Чем Make AI Agents отличается от обычного сценария?** — Агент сам выбирает tools и шаги по instructions; линейный scenario — фиксированная цепочка модулей.
2. **Нужен ли свой OpenAI ключ для агента в Make?** — Нет на старте: Make's AI Provider на всех тарифах; на paid — можно подключить OpenAI/Claude/Gemini и платить tokens провайдеру.
3. **Как добавить MCP в Make AI Agents?** — В Run an agent → Add MCP → connection → выбрать tools; ограничить список, иначе растут tokens.
4. **Сколько credits съедает один run агента?** — Минимум 1 credit/operation + каждый tool + tokens (см. help.make.com/credit-usage-for-ai-agents).
5. **Какие файлы загружать в Knowledge?** — JSON, TXT, CSV, PDF; для частых обновлений — отдельный scenario с Knowledge app.
6. **Как тестировать агента до prod?** — In-canvas Chat, Run once с прошлым bundle, вкладки Output и Reasoning в History.
7. **Можно ли вложить агента в агента?** — Да, один уровень sub-agent; глубже — через Call a scenario.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «Make AI Agent» 40–60 слов | Lead | «Make AI Agent — …» |
| Таблица agent vs scenario vs AI app | H2-1 | 3 строки + рекомендация |
| Workflow-схема | H2-2 | Trigger → Run an agent → Tools → Output |
| Таблица credits (agent run) | H2-5 / FAQ | Из help.make.com |
| FAQ 5–7 | Конец | Ответы-действия |
| Internal link B02 | Comparison блок | n8n vs Make one paragraph |

---

## 8. Риски для writer

- Продукт в **open beta** — явно предупредить читателя; не обещать неизменность pricing.
- Не путать старый Make AI Agents (отдельная вкладка) и **Make AI Agent (New)** на canvas (Feb 2026).
- Цифры credits/tokens — только из help.make.com/credit-usage-for-ai-agents.
- Min **5** нумерованных шагов + **чеклист 10+** пунктов перед prod (utility gate статьи).
- Объём: 8 500–9 500 знаков (quality-blog).
- Без эмодзи; дефис вместо длинного тире.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст сценарий с Make AI Agent (New), настроит провайдер и instructions, подключит 2–3 tools (модуль или Call a scenario), добавит knowledge при необходимости, протестирует через Chat и Reasoning и включит guardrails (лимиты, approval) перед production.

**action_outline (для writer):**

1. **Выбрать кейс и тип automation:** agent (гибкие решения) vs linear scenario — по таблице из раздела 5; зафиксировать один бизнес-процесс (triage, lead, content draft).
2. **Create scenario + trigger:** Webhooks / Gmail Watch / Slack — источник input; на Free — учесть 15-min interval и 2 active scenarios.
3. **Добавить Make AI Agent (New) > Run an agent;** connection: Make's AI Provider (Free) или custom OpenAI/Claude (paid).
4. **Написать Instructions:** роль, цель, шаги, guardrails, формат JSON/text output; указать, что агент **не** делает.
5. **Настроить Input** — map данных из trigger; опционально Conversation ID + Maximum conversation history для multi-turn.
6. **Add tools (2–3 max на MVP):** module tool (Sheets/Slack) и/или Call a scenario с Return outputs + On-demand; при необходимости Add MCP с минимальным набором tools.
7. **Add knowledge:** upload PDF/CSV или Knowledge app scenario для FAQ/brand guide; проверить расход credits на embedding.
8. **Test:** Chat на canvas → Run once → History → Reasoning tab; disable tool по одному для изоляции ошибок; step timeout 300s по умолчанию.
9. **Prod checklist:** filter до agent, approval после, logging, лимит tools, мониторинг credits (75%/90% notifications на pricing FAQ).

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ (7) |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.
