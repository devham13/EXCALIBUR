# Research notes — B06 «Чек-лист Human-in-the-Loop для AI-агентов: как настроить контроль человека в n8n, Make и Cursor»

**topic_id:** B06  
**slug:** human-in-the-loop-ai-agents-n8n  
**article_mode:** B (checklist + how-to)  
**research_date:** 2026-08-29  
**disclaimer:** Все даты, версии и статистика проверены на 29.08.2026.

---

## 1. SERP-обзор (WebSearch, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [docs.n8n.io/.../human-in-the-loop-for-tools](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools) | Официальная дока n8n | Канон: Approve/Deny, 9 каналов, `$tool`, `$fromAI()`, system prompt | Только n8n; нет Make/Cursor; нет чеклиста 25+ | Сухой перевод docs без risk-map |
| 2 | [blog.n8n.io/production-ai-playbook-human-oversight](https://blog.n8n.io/production-ai-playbook-human-oversight/) | Playbook n8n (2026) | HITL для tool calls vs output review; Chat send-and-wait | Англ.; один продукт; мало compliance | Маркетинговый тон «n8n решает всё» |
| 3 | [blog.n8n.io/human-in-the-loop-automation](https://blog.n8n.io/human-in-the-loop-automation/) | Обзор HITL n8n | Wait node + Slack/Telegram; use cases (refund, social) | Старые паттерны Wait без native tool gate | Структура 1:1; «1200+ integrations» без контекста |
| 4 | [humangent.io/blog/n8n-human-in-the-loop-guide](https://humangent.io/blog/n8n-human-in-the-loop-guide/) | Практический гайд | 3 native опции; v2.6.0+ tool review; CE без лимита | Коммерческий продукт HumanGent; нет Make/Cursor | Продажа approval inbox |
| 5 | [n8nautomation.cloud/.../human-in-the-loop-approval](https://n8nautomation.cloud/blog/n8n-human-in-the-loop-approval-ai-agent-workflows) | Tutorial blog | 5 workflow-паттернов; gated tools | Узкий фокус n8n; англ. | Паттерны без EU AI Act |
| 6 | [rills.ai/blog/make-com-human-approval-step](https://rills.ai/blog/make-com-human-approval-step) | Make workaround | Enterprise lock native HITL; webhook split-scenario | Только Make workaround; bias к Rills | Утверждения без ссылки на Make pricing |
| 7 | [make.com/en/blog/human-in-the-loop](https://www.make.com/en/blog/human-in-the-loop) | Официальный блог Make | HITL как design decision; Router + OzyApprovals пример | Enterprise для native app не явно; нет n8n | Общие определения без шагов |
| 8 | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | Дока Cursor | Webhook/Slack triggers; PR tools; team vs private billing | Cloud Agents без per-action approve | Путать Run Modes (local) с Automations |

**Паттерн SERP:** топ — официальная дока n8n + англоязычные tutorial-блоги про HITL для AI tool calls (v2.6, январь 2026). Отдельный кластер — EU AI Act + agentic governance (Praxikon, Confir). Make — «что такое HITL» и Enterprise-gated native app. **Нет** русскоязычного чеклиста, который связывает n8n + Make + Cursor в одном actionable guide с risk-map и 25+ пунктами.

**Intent:** checklist — пользователь уже запускает AI-агентов и хочет **настроить контроль человека** перед опасными tool calls (CRM, письма, платежи, удаление). Вторичный intent: compliance (EU AI Act), сравнение n8n vs Make по HITL.

**Пробел для «Ковчег»:** практический чек-лист HITL на трёх платформах из карточки B06 + карта рисков + graduation to autonomy; язык для no-code-практика Make (Артур).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в Cloud Agent окружении. Инструмент `wordstat_get_top_requests` недоступен. **Точные объёмы показов не получены** — таблица с цифрами ниже намеренно не заполнена (без выдуманных данных).

**Оценка спроса по SERP + смежная семантика (B02, 11.06.2026, MCP был доступен):**

| Фраза | Показы/мес | Источник оценки |
|-------|------------|-----------------|
| n8n | 37 115 | B02 research-notes (Wordstat) |
| n8n ai | 720 | B02 research-notes |
| n8n агенты | 699 | B02 research-notes |
| ии агенты и n8n | 74 | B02 research-notes |
| human in the loop n8n | *нет данных* | EN-запрос; низкий RU-объём, высокий product-intent в Google |
| контроль ии агентов человеком | *нет данных* | RU long-tail; SERP → n8n docs + community |

### LSI для writer (SERP + docs, без Wordstat)

- human in the loop n8n, human review tool calls, hitl ai agents  
- n8n `$tool.name`, `$tool.parameters`, `$fromAI()`, approve deny  
- n8n Chat send and wait, Wait node, Slack Telegram approval  
- Make human in the loop enterprise, create review request, webhook workaround  
- Cursor Cloud Agents branch protection, Automations webhook, Run Modes Auto-review  
- EU AI Act Article 14 human oversight, kill switch, audit trail  
- graduation to autonomy, risk map payments CRM delete email  
- контроль ии агентов, human-on-the-loop vs human-in-the-loop  

**SEO-стратегия:** primary EN «human in the loop n8n» в H1/lead + RU «контроль ии агентов» в H2; head «n8n ai» / «n8n агенты» через internal link на B02.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| n8n 2.6.0 (2026-01-26): native HITL для AI tool calls, generate HITL tool nodes для sendAndWait | [github.com/n8n-io/n8n/releases/tag/n8n@2.6.0](https://github.com/n8n-io/n8n/releases/tag/n8n@2.6.0) | 29.08.2026 | да |
| Human review: Approve выполняет tool с параметрами AI; Deny отменяет и сообщает агенту | [docs.n8n.io/.../human-in-the-loop-for-tools](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools) | 29.08.2026 | да |
| 9 каналов approval: Chat, Slack, Discord, Telegram, Teams, Gmail, WhatsApp, Google Chat, Outlook | [docs.n8n.io/.../human-in-the-loop-for-tools](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools) | 29.08.2026 | да |
| `$tool.name` — имя tool на canvas; `$tool.parameters` — параметры вызова (включая `$fromAI()`) | [docs.n8n.io/.../human-in-the-loop-for-tools](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools) | 29.08.2026 | да |
| System prompt должен описывать gated tools и поведение при Deny | [docs.n8n.io/.../human-in-the-loop-for-tools](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools) | 29.08.2026 | да |
| HITL review step: «+» на connector между AI Agent и tool → Add human review step | [blog.n8n.io/production-ai-playbook-human-oversight](https://blog.n8n.io/production-ai-playbook-human-oversight/) | 29.08.2026 | да |
| Chat node: «Send a message and wait for response» паузит workflow до ответа человека | [blog.n8n.io/production-ai-playbook-human-oversight](https://blog.n8n.io/production-ai-playbook-human-oversight/) | 29.08.2026 | да |
| n8n HITL (send-and-wait, Wait, AI tool review) работает на Community Edition без execution cap | [rills.ai/blog/n8n-human-approval-workflow](https://rills.ai/blog/n8n-human-approval-workflow) | 29.08.2026 | да |
| Make native app «Human in the loop»: 4 модуля (Create/Cancel/Watch/List); **выполнение только Enterprise** | [rills.ai/blog/make-com-human-approval-step](https://rills.ai/blog/make-com-human-approval-step) | 29.08.2026 | да |
| Make AI Agents GA 11.02.2026: in-canvas, Reasoning Panel, multimodal | [brahmalabs.io/compare/make-vs-brahmalabs](https://www.brahmalabs.io/compare/make-vs-brahmalabs/) | 29.08.2026 | да |
| EU AI Act: агенты = AI systems по Art. 3(1); high-risk → Art. 14 human oversight | [praxikon.com/.../agentic-ai-under-the-eu-ai-act](https://www.praxikon.com/en/posts/agentic-ai-under-the-eu-ai-act) | 29.08.2026 | да |
| Art. 14: oversight persons должны понимать limits, детектить сбои, override/halt | [confir.eu/eu-ai-act/agentic-ai-compliance](https://confir.eu/eu-ai-act/agentic-ai-compliance) | 29.08.2026 | да |
| High-risk AI systems: deadline compliance 2 December 2027 (Digital Omnibus, May 2026) | [confir.eu/eu-ai-act/agentic-ai-compliance](https://confir.eu/eu-ai-act/agentic-ai-compliance) | 29.08.2026 | да |
| Cursor Run Modes (Auto-review и др.) — **только local agents**; Cloud Agents не запрашивают approve per action | [cursor.com/docs/agent/security/run-modes](https://cursor.com/docs/agent/security/run-modes) | 29.08.2026 | да |
| Cursor Auto-review shipped as recommended default в Cursor 3.6 (29 May 2026) | [cursor.com/docs/agent/security/run-modes](https://cursor.com/docs/agent/security/run-modes) | 29.08.2026 | да |
| Cursor Automations: triggers GitHub/GitLab/Slack/webhook/Linear; tools Comment on PR, Request reviewers, Send to Slack | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 29.08.2026 | да |
| Cloud Agents: clone repo, branch, push PR; рекомендуют branch protection + CI на каждый PR | [checkmarx.com/.../cursor-security-risks](https://checkmarx.com/learn/ai-security/cursor-security-risks-practices-4-critical-security-controls/) | 29.08.2026 | да |
| HITL в sub-workflow при вызове из AI Agent: parent tool call может resolve до конца sub — лучше gate на connection в main workflow (n8n 2.6+) | [community.n8n.io/t/n8n-sub-workflow-hitl-issues](https://community.n8n.io/t/n8n-sub-workflow-hitl-issues-called-by-ai-agent/307499) | 29.08.2026 | да |
| Агент не «видит» review node — описать gate в description wrapped tool, иначе модель over-hedges | [github.com/n8n-io/skills/.../HUMAN_REVIEW.md](https://github.com/n8n-io/skills/blob/main/skills/n8n-agents-official/references/HUMAN_REVIEW.md) | 29.08.2026 | да |
| Автономные ИИ завершают <2.5% сложных неструктурированных задач без человека — HITL 2.0 как стандарт | [mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) (fact-bank) | 11.06.2026 | да |
| ~40% проектов автономных AI-агентов отменяются из-за скрытых затрат и нулевого ROI | [mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) (fact-bank) | 11.06.2026 | да |

**Не использовать без первичника:** «signed HMAC resume tokens n8n 2.35» (eastkode.in — third-party blog, не официальный changelog); «10 min–7 day timeout» без проверки в docs.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** чек-лист HITL — **карта рисков** (какие tool calls gate) + **пошаговая настройка** human review в n8n (native tool gate), workaround в Make (Enterprise vs webhook), **контроль Cloud Agents в Cursor** через branch protection + Automations + PR review — с **25+ пунктами** перед продакшеном.

**Почему отличается от конкурентов:**
- Официальные docs покрывают только один продукт.
- Англоязычные гайды не связывают compliance (EU AI Act) с конкретными кнопками Approve в Slack.
- «Ковчег»: три платформы из стека аудитории (n8n + Make + Cursor) в одном actionable checklist.

**Tone:** практик automation; EU AI Act — как триггер для checklist, не legal advice. RU + EN термины там, где ищут (HITL, human review).

**H2-каркас (из карточки B06 + research):**
1. Зачем HITL в 2026: EU AI Act, риски автономных действий
2. Карта рисков: платежи, CRM, письма, delete — что gate обязательно
3. n8n: Human Review для tool calls (Slack/Telegram, `$tool`, approve/deny)
4. Make: native HITL (Enterprise) vs webhook split-scenario
5. Cursor: Automations + branch protection + PR как HITL для Cloud Agents
6. Чек-лист HITL 25+ пунктов: политики, audit, тесты, graduation to autonomy

**Internal links (карточка):** `/avtomatizaciya-n8n-ai-agents/`, `/nastroyka-cursor-automations-2026/`

---

## 5. Risk-map (черновик для writer)

| Класс действия | Примеры tool calls | Рекомендация HITL | Платформа |
|----------------|-------------------|-------------------|-----------|
| Финансы | charge, refund, invoice | Human-in-the-loop обязательно | n8n gate / Make webhook |
| Исходящие comms | email client, Slack post, SMS | HITL + preview текста | n8n `$tool.parameters` |
| CRM write | update deal, delete contact | HITL на write/delete | n8n / Make Router |
| Data delete | DB delete, file remove | HITL + deny by default | n8n native gate |
| Read-only | get record, search KB | Можно без gate (on-the-loop) | logging only |
| Code/deploy | merge PR, deploy | Branch protection + required reviewers | Cursor/GitHub |

---

## 6. FAQ-кандидаты (5–7)

1. **Что такое human in the loop для AI-агентов?** — Checkpoint: агент предлагает action → человек approve/deny → tool выполняется или отменяется.
2. **Как включить human review в n8n?** — AI Agent → «+» на tool connection → Add human review step → канал (Slack/Telegram) → подключить gated tools.
3. **Чем HITL в n8n отличается от Make?** — n8n: native gate на каждом plan; Make: native app только Enterprise, иначе webhook split.
4. **Нужен ли HITL по EU AI Act?** — Для high-risk (Annex III) Art. 14 требует effective oversight; для остальных — best practice + GDPR Art. 22 при legal effects.
5. **Работают ли Cloud Agents Cursor без approve?** — Да; HITL = branch protection, required PR review, Automations с quality bar в prompt.
6. **Что писать в system prompt про gated tools?** — Список tools с review, поведение при Deny, не просить пользователя подтверждать то, что уже gate.
7. **Когда снимать HITL (graduation)?** — После N успешных прогонов на sandbox, метрики error rate, audit trail без инцидентов.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение HITL 40–60 слов | Lead | «Human-in-the-loop (HITL) — …» |
| Risk-map таблица | H2-2 | Действие → gate да/нет |
| Workflow n8n | H2-3 | Agent → [Human Review] → Tool → Approve/Deny branch |
| Чек-лист 25+ | H2-6 | Нумерованный checklist |
| FAQ 5–7 | Конец | Ответы-действия |
| Comparison n8n vs Make HITL | H2-3/4 | Таблица native vs Enterprise |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «human in the loop n8n», «human review n8n tool calls», «контроль ии агентов», «human in the loop make», «EU AI Act human oversight».

---

## 8. Риски для writer

- Не выдавать legal advice по EU AI Act — «ориентир для checklist», ссылка на первичник.
- Не путать Cursor Run Modes (local) и Cloud Agents (no per-action approve).
- Make Enterprise-only для native HITL — перепроверить формулировку «modules visible on all plans, execute on Enterprise» (rills.ai).
- Min **25 checklist items** + **5+ numbered setup steps** per platform (utility gate статьи).
- Объём: 8 500–9 500 знаков (quality-blog).
- CTA ≤ 3; internal links на B02 и Cursor automations article.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель составит карту рисков для своих AI-агентов, настроит human review для tool calls в n8n (Slack/Telegram + `$tool`), выберет путь HITL в Make (Enterprise native или webhook workaround), настроит контроль Cloud Agents в Cursor через branch protection и PR review, и пройдёт чек-лист 25+ пунктов перед снятием gate.

**action_outline (для writer):**

1. **Инвентаризация агентов:** список workflows (n8n/Make/Cursor) и всех tool calls с side effects.
2. **Risk-map:** классифицировать actions (finance, outbound, CRM write, delete, read-only, deploy) → отметить обязательный HITL.
3. **n8n — открыть AI Agent workflow:** на connector к risky tool нажать «+» → Add human review step.
4. **n8n — канал:** Slack или Telegram; в message template использовать `$tool.name` и `$tool.parameters`.
5. **n8n — system prompt:** перечислить gated tools, сценарий Deny, описание в tool description (anti over-hedge).
6. **n8n — тест:** sandbox credentials; Approve и Deny; проверить, что агент корректно обрабатывает rejection.
7. **Make — проверить план:** если Enterprise — Create review request; иначе split scenario + webhook approve/reject links.
8. **Make — Reasoning Panel:** лимит итераций; Router на approved/rejected path.
9. **Cursor — Cloud Agents:** включить branch protection, required reviewers, CI checks на PR от `cursor` bot.
10. **Cursor — Automations:** webhook/Slack trigger; в prompt — quality bar «open PR only if…»; Send to Slack для эскалации.
11. **Audit trail:** логировать execution id, tool params, reviewer, decision, timestamp (n8n execution log + external store).
12. **EU AI Act checklist:** задокументировать in-the-loop vs on-the-loop per agent; kill switch procedure.
13. **Graduation policy:** критерии снятия gate (N runs, error rate, compliance sign-off).
14. **Финальный прогон:** чек-лист 25+ из H2-6 — все пункты PASS перед prod.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ unavailable (без выдуманных цифр) |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| Risk-map + FAQ | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + `fact-bank.md`.
