# Research notes — B06 «Как настроить Cursor Automations: чек-лист автоматических cloud-агентов в 2026»

**topic_id:** B06  
**slug:** nastrojka-cursor-automations-2026  
**article_mode:** B (checklist / how-to)  
**research_date:** 2026-06-22  
**disclaimer:** Все даты, версии и статистика проверены на 22.06.2026.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | Официальная help (EN) | Канон: 5 шагов создания, таблица триггеров, billing, scopes | Нет русского чек-листа; мало troubleshooting | Сухой перевод без сравнения с Background Agents |
| 2 | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | Официальная docs | Cloud Agents = бывшие Background Agents; Max Mode; MCP; paid plan | Не фокус на Automations UI | Путать «cloud agent из IDE» и «automation по триггеру» |
| 3 | [cursor.com/blog/automations](https://cursor.com/blog/automations) | Официальный анонс (март 2026) | Кейсы Cursor/Rippling: security review, PagerDuty, weekly digest | News-формат, нет пошагового setup | Копировать только истории без чек-листа |
| 4 | [cursor.com/changelog/05-20-26](https://cursor.com/changelog/05-20-26) | Changelog 3.5 | Agents Window, multi/no-repo, 5 marketplace-шаблонов, промо −50% | Кратко | Выдумывать даты релизов |
| 5 | [www.datacamp.com/tutorial/cursor-automations-hands-on-guide](https://www.datacamp.com/tutorial/cursor-automations-hands-on-guide) | Hands-on EN (2026) | PR review + cron coverage; permissions tiers; «start narrow» | Длинный tutorial; Sentry в таблице без подтверждения в help | Таблицу триггеров 1:1 (Sentry не верифицирован) |
| 6 | [www.developersdigest.tech/blog/cursor-automations-developer-guide-2026](https://www.developersdigest.tech/blog/cursor-automations-developer-guide-2026) | EN developer guide | Workflow-паттерны, CI/CD | Упоминает `.cursor/automations/` YAML — **не подтверждено** официальной help на 22.06.2026 | YAML-only setup как единственный путь |
| 7 | [shtruzel.ru/articles/cursor-agent-mode-kak-ispolzovat-2026](https://shtruzel.ru/articles/cursor-agent-mode-kak-ispolzovat-2026) | RU обзор Agent mode | Русский язык, Cloud Agents | Другой intent (Agent mode, не Automations checklist) | Смешивать Agent mode и Automations без таблицы |
| 8 | [kv-ai.ru/tpost/systemy-avtomatizacii-cursor-ai-agents](https://kv-ai.ru/tpost/systemy-avtomatizacii-cursor-ai-agents) | RU обзор | Триггеры GitHub/Slack на русском | Короткий, без чек-листа безопасности | Каннибализацию: у нас — полный checklist + MCP security |

**Паттерн SERP:** топ — официальные Cursor docs/changelog + англоязычные tutorials (DataCamp, byteiota, NextPj). Русскоязычный **checklist «настройка cursor automations»** почти не закрыт: есть новости (DTF, vc.ru, vibecoderz) и обзоры Agent mode, но нет пошагового чек-листа с триггерами, scopes, billing и MCP-security.

**Intent:** checklist — читатель хочет **создать и активировать** первую Automation (триггер → prompt → tools → repo scope), понять отличие от ручного Cloud Agent и не слить бюджет на широкие триггеры.

**Пробел для «Ковчег»:** практический русский чек-лист для команды автоматизации: Automations vs Cloud/Background Agents vs subagents; подготовка Pro + GitHub + billing; Marketplace vs Blank vs `/automate`; таблица триггеров; no-repo/multi-repo; MCP + secrets + Team Owned; internal link на B03 (MCP).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 22.06.2026)

### ⚠️ MCP UNAVAILABLE WARNING

Сервер `user-mcp-kv` **не подключён** в Cloud-сессии (`Server "user-mcp-kv" not found`). Инструмент `wordstat_get_top_requests` недоступен. **Точные показы/мес не получены — цифры ниже не использовать в тексте статьи.**

### Proxy-оценка спроса (SERP + смежная семантика B03, без выдуманных объёмов)

| Сигнал | Наблюдение | Источник proxy |
|--------|------------|----------------|
| EN primary «cursor automations» | Высокая конкуренция: docs, DataCamp, changelog 2026 | WebSearch 22.06.2026 |
| RU «настройка cursor automations» | Мало dedicated how-to; топ — новости и обзоры | research-serp.json `secondary_4` |
| Смежный спрос «cursor mcp» | 630 показов/мес (B03, Wordstat 11.06.2026) | B03 research-notes |
| Смежный «cursor cloud agent» | Обзоры RU/EN, intent смешанный с Agent mode | WebSearch |

### LSI для writer (SERP + changelog, без Wordstat-цифр)

- cursor automations, cursor automation github, cursor automations webhook  
- настройка cursor automations, cursor cloud agent, background agents  
- Agents Window, cursor.com/automations, /automate skill  
- триггер cron, GitHub PR opened, Slack emoji trigger, webhook endpoint  
- no-repo automation, multi-repo environment, Team Owned  
- cloud sandbox, Max Mode, API pricing, Run history  
- MCP server automation, secrets cloud-agents dashboard  
- computer use tool, marketplace templates  

**SEO-стратегия:** primary EN «cursor automations» в lead/H2; RU «настройка cursor automations» в H1 и FAQ; secondary «cursor cloud agent», «cursor automation github», «cursor automations webhook» — в подзаголовках и чек-листе. Связка с B03 по «MCP + automations».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Cursor Automations анонсированы 5 марта 2026: always-on agents по триггерам и инструкциям | [cursor.com/changelog/03-05-26](https://cursor.com/changelog/03-05-26) | 05.03.2026 | да |
| Триггеры на старте: schedules, Slack, Linear, GitHub, PagerDuty, webhooks | [cursor.com/changelog/03-05-26](https://cursor.com/changelog/03-05-26) | 05.03.2026 | да |
| При запуске automation поднимается cloud sandbox; agent использует настроенные MCP и модели | [cursor.com/changelog/03-05-26](https://cursor.com/changelog/03-05-26) | 05.03.2026 | да |
| У automation есть memory tool — учится на прошлых прогонах | [cursor.com/changelog/03-05-26](https://cursor.com/changelog/03-05-26) | 05.03.2026 | да |
| Создание: cursor.com/automations или шаблон Marketplace | [cursor.com/changelog/03-05-26](https://cursor.com/changelog/03-05-26) | 05.03.2026 | да |
| 20 мая 2026 (3.5): Automations в Agents Window + multi-repo + no-repo | [cursor.com/changelog/05-20-26](https://cursor.com/changelog/05-20-26) | 20.05.2026 | да |
| 7 дней после создания новой automation — agent runs со скидкой 50% | [cursor.com/changelog/05-20-26](https://cursor.com/changelog/05-20-26) | 20.05.2026 | да |
| 5 no-repo шаблонов Marketplace: Slack digest, Product analytics, Product FAQ, Product finance, Customer health | [cursor.com/changelog/05-20-26](https://cursor.com/changelog/05-20-26) | 20.05.2026 | да |
| 18 июня 2026 (3.8): skill `/automate` — описать задачу текстом, Cursor настроит triggers/instructions/tools | [cursor.com/changelog](https://cursor.com/changelog) / [06-18-26](https://cursor.com/changelog/06-18-26) | 18.06.2026 | да |
| Slack emoji trigger: реакция эмодзи на сообщение запускает automation | [cursor.com/changelog](https://cursor.com/changelog) | 18.06.2026 | да |
| 5 новых GitHub-триггеров: issue comment, PR review comment, PR review submitted, review thread updated, workflow run completed | [cursor.com/changelog](https://cursor.com/changelog) | 18.06.2026 | да |
| Computer use для automations включён по умолчанию — agent может записать demo/artifacts | [cursor.com/changelog](https://cursor.com/changelog) | 18.06.2026 | да |
| Создание automation: Agents Window, cursor.com/automations/new, Marketplace, 5 шагов (trigger → prompt → tools → repo scope → save) | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 22.06.2026 | да |
| No-repo: не клонирует код; подходит Slack/MCP/webhook/Linear/PagerDuty; **не** может править код или открывать PR | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 22.06.2026 | да |
| Single-repo и multi-repo environment — для задач с кодом в одной или нескольких базах | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 22.06.2026 | да |
| Полный список триггеров: Scheduled, GitHub/GitLab PR/push/CI/draft, Slack message/channel, Linear issue/cycle, PagerDuty, Webhook | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 22.06.2026 | да |
| Automation может иметь **несколько** триггеров; срабатывает при **любом** из них | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 22.06.2026 | да |
| Tools: Comment on PR, Request reviewers, Send to Slack, Read Slack channels, MCP server, Memories | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 22.06.2026 | да |
| Billing: каждый run = Cloud Agent run по **API pricing** выбранной модели | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 22.06.2026 | да |
| Permission scopes: Private, Team Visible, Team Owned (создание Team Owned — admin) | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 22.06.2026 | да |
| Cloud Agents (бывш. Background Agents) — Max Mode **всегда** включён, без toggle | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 22.06.2026 | да |
| Cloud Agents требуют **paid Cursor plan** | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 22.06.2026 | да |
| Cloud agent billing — API pricing модели + spend limit при первом использовании | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 22.06.2026 | да |
| Webhook: URL и API key появляются **после сохранения** automation | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) (сниппет WebSearch/docs) | 22.06.2026 | да (уточнить writer: help не дублирует — опираться на docs reference) |
| При promote в Team Owned — перегенерировать webhook API key; MCP OAuth перевести на team service account | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) (сниппет WebSearch) | 22.06.2026 | да |
| Bugbot — «оригинальная automation»: триггерится на PR, тысячи раз/день, поймал миллионы багов | [cursor.com/blog/automations](https://cursor.com/blog/automations) | 05.03.2026 | да |
| Pipeline: trigger → fresh cloud sandbox → clone repo (если scope с кодом) → agent + tools/MCP → verify → output (PR comment, Slack, PR) | [cursor.com/blog/automations](https://cursor.com/blog/automations), DataCamp tutorial | 22.06.2026 | да |
| GitHub PR automation требует GitHub App / read-write доступ к репо | [datacamp.com/tutorial/cursor-automations-hands-on-guide](https://www.datacamp.com/tutorial/cursor-automations-hands-on-guide) | 2026 | да (практика; сверять с docs setup) |
| Рекомендация «start narrow»: широкий trigger на busy repo быстро сжигает usage | [datacamp.com/tutorial/cursor-automations-hands-on-guide](https://www.datacamp.com/tutorial/cursor-automations-hands-on-guide) | 2026 | да (best practice) |
| Secrets для cloud agents: cursor.com/dashboard/cloud-agents, workspace/team scope | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 22.06.2026 | да |
| Guided cloud environment setup — «менее 10 минут» по заявлению docs | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 22.06.2026 | да |
| Автономные ИИ-системы завершают <2,5% сложных неструктурированных задач без человека — Human-in-the-loop норма | [fact-bank / mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 11.06.2026 | да (для блока guardrails) |
| ~40% проектов автономных агентов отменяются из-за скрытых затрат и нулевого ROI | [fact-bank / mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 11.06.2026 | да (осторожно: контекст enterprise, не Cursor-specific) |

**Не использовать без оговорки:** setup **только** через YAML `.cursor/automations/` (Developers Digest) — в официальной help на 22.06.2026 канон = UI (Agents Window / dashboard). Sentry как trigger — не в help-таблице.

**fact-bank.md:** прямых фактов про Cursor Automations нет; использованы 2 строки про ROI/HITL как guardrails для чек-листа безопасности.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **30–45 минут** пройти чек-лист и запустить **первую Automation** (рекомендация writer: PR review или weekly cron), с понятным выбором триггера, repo scope, tools/MCP и лимитов billing — без путаницы с ручным Cloud Agent из IDE.

**Почему отличается от конкурентов:**
- Официальная docs — канон, но без русского checklist и без сравнения «Automations vs Background Agents vs subagents».
- EN-tutorials длинные и IDE-centric; мало про Team Owned, webhook rotate, no-repo для бизнес-MCP.
- RU-новости (DTF/vc) — news, не actionable checklist.
- «Ковчег»: чек-лист 10+ пунктов + workflow-таблица + связка с B03 (MCP) и Make/n8n как complement (не замена).

**Tone:** Automations = «фабрика, которая просыпается от события, а не когда вы открыли чат». Триггер = будильник; instructions = регламент SOP; tools = разрешённые действия.

**H2-каркас (из карточки + research):**
1. Automations vs Cloud Agents (Background) vs subagents — таблица выбора  
2. Подготовка: paid plan, GitHub/GitLab, cloud billing/spend limit, Agents Window  
3. Создание: Marketplace / Blank / `/automate`  
4. Триггеры: cron, GitHub, Slack (+ emoji 3.8), Linear, PagerDuty, webhook  
5. Repo scope: no-repo / single / multi-repo + cloud environment  
6. Tools + MCP + secrets + чек-лист безопасности (Private → Team Owned, Memories с untrusted input)  
7. Мониторинг Run history, сужение триггеров, промо −50% (если ещё актуально на дату публикации)  
8. FAQ + финальный чек-лист перед prod  

**Conversion (осторожно, CTA ≤ 3):**
- Internal: [B03 MCP Cursor](/podklyuchenie-mcp-cursor/)  
- kv-ai.ru Make — только если уместно «Automations для кода + Make для контент-воронок»  
- Telegram @maya_pro — max 1×  

---

## 5. Черновик чек-листа для writer (10+ пунктов)

| # | Пункт | Делать / не делать |
|---|-------|-------------------|
| 1 | Paid Cursor plan + login | ✅ Делать перед любым cloud run |
| 2 | Подключить GitHub/GitLab с read-write, если нужен PR/code | ✅ / ⛔ no-repo — не подключать зря |
| 3 | Задать spend limit в cloud agents dashboard | ✅ Делать до массовых cron |
| 4 | Выбрать **узкий** первый триггер (1 PR event или 1 cron/week) | ✅ / ⛔ не «every push to main» в busy monorepo |
| 5 | Instructions как **SOP**, не one-off prompt | ✅ |
| 6 | Явно включить только нужные tools (Comment PR, Slack, MCP) | ✅ |
| 7 | Secrets — dashboard, не `.env` в prompt | ✅ |
| 8 | Memories — осторожно при untrusted Slack/webhook input | ✅ guardrail |
| 9 | Прогон test PR / manual webhook → проверить Run history | ✅ |
| 10 | 3–7 дней мониторинг usage → расширять триггеры | ✅ |
| 11 | Team Owned — только после доверия; rotate webhook key | ✅ |
| 12 | Promote scope → проверить MCP OAuth на team account | ✅ |

---

## 6. FAQ-кандидаты (7)

1. **Что такое Cursor Automations?** — Always-on cloud agents по триггеру (schedule/event/webhook), не ручной чат в IDE.  
2. **Как запустить automation по расписанию?** — Trigger Scheduled/cron → указать repo (если нужен код) → prompt → save → дождаться первого run в history.  
3. **Чем Automations отличаются от Background/Cloud Agents?** — Cloud Agent: вы инициируете; Automation: инициирует Slack/GitHub/cron/webhook; параллельность и память между runs.  
4. **Нужен ли репозиторий?** — Нет для Slack/MCP/webhook-only; да для PR review и code changes.  
5. **Как настроить webhook?** — Save automation → скопировать URL + API key → POST из CI/мониторинга.  
6. **Сколько стоит?** — API pricing модели за каждый Cloud Agent run; следить за частотой триггеров.  
7. **Как подключить MCP к automation?** — Tool MCP server в настройках automation + secrets; см. B03 для базовой настройки mcp.json.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Automations 40–60 слов | Lead | «Cursor Automations — …» |
| Таблица Automations vs Cloud Agent vs subagents | H2-1 | 3 колонки + «когда что» |
| Таблица триггеров (сжатая из help) | H2-4 | Trigger \| Fires when \| Use case |
| Workflow | H2-3–6 | Trigger → scope → prompt → tools → save → test |
| Чек-лист 10+ | H2-7 / финал | Нумерованный список |
| FAQ 7 | Конец | Ответы-действия |
| Internal link B03 | H2-6 | MCP setup |

**Целевые формулировки:** «cursor automations», «настройка cursor automations», «cursor cloud agent», «cursor automation github», «cursor automations webhook».

---

## 8. Риски для writer

- Не выдумывать Wordstat-цифры — MCP недоступен.  
- Не утверждать YAML-only setup без оговорки.  
- Промо −50% (20.05.2026, 7 дней) — на 22.06.2026 **скорее всё**; проверить актуальность или писать «бывало в релизе 3.5».  
- Sentry trigger — не включать (нет в official help table).  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Min **5** нумерованных шагов + чек-лист **10+** (utility gate статьи).  
- Без эмодзи в article; дефис вместо длинного тире.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель откроет Agents Window или cursor.com/automations, создаст automation (шаблон, Blank или `/automate`), выберет триггер и repo scope, подключит tools/MCP, сохранит и проверит первый run в Run history, настроит billing guardrails и поймёт, когда использовать Automations вместо ручного Cloud Agent.

**action_outline (для writer):**

1. **Проверить доступ:** paid plan, cloud agents enabled, spend limit в dashboard; подключить GitHub/GitLab при code-триггерах.  
2. **Открыть Automations:** Agents Window в IDE **или** [cursor.com/automations/new](https://cursor.com/automations/new).  
3. **Выбрать способ создания:** Marketplace-шаблон (PR review / no-repo digest) **или** + New Automation **или** `/automate` в локальной agent-сессии (3.8+).  
4. **Настроить trigger(ы):** начать с одного (PR opened **или** weekly Scheduled); для webhook — сохранить и скопировать URL + API key.  
5. **Задать repo scope:** no-repo (Slack/MCP only) / single-repo / multi-repo environment; для cron без кода — явно указать repo если нужны PR.  
6. **Написать instructions-SOP:** что проверять, когда молчать, куда постить результат; включить computer use demo только если нужно.  
7. **Подключить tools:** Comment on PR, Send to Slack, MCP (см. B03); secrets через cloud-agents dashboard.  
8. **Выбрать visibility:** Private для эксперимента → Team Visible/Team Owned после стабилизации (rotate webhook при promote).  
9. **Save → test run → Run history:** оценить качество 3–7 дней, сузить или расширить триггеры; мониторить API usage.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (SERP proxy) |
| Таблица фактов с URL | ✅ (28 фактов) |
| utility_verdict + action_outline | ✅ |
| Чек-лист 10+ черновик | ✅ |
| FAQ 7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + internal B03.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B06
article_dir: memory/blog/articles/B06-nastrojka-cursor-automations-2026
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 конкурентов (official help/docs/blog, DataCamp, Developers Digest, shtruzel RU, kv-ai). Wordstat: MCP user-mcp-kv недоступен — proxy через SERP + B03 «cursor mcp» 630. Угол — русский checklist Automations: триггеры, repo scope, MCP/security, vs Cloud Agents. 28 фактов с URL, 9 шагов action_outline, чек-лист 12 пунктов, 7 FAQ. Готов к writer.
===
