# Research notes — B06 «Как настроить Cursor Automations: cron, webhook и триггеры для Cloud Agents»

**topic_id:** B06  
**slug:** nastroyka-cursor-automations-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-10-15  
**disclaimer:** Все даты, версии и статистика проверены на 15.10.2026.

---

## 1. SERP-обзор (WebSearch Cursor + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | Официальная docs (EN) | Канон: триггеры, repo/no-repo/multi-repo, billing, service account, webhook URL после Save, fork PR | Английский; мало troubleshooting cron UTC и багов расписания | Сухой перескод без чеклиста и MSK→UTC |
| 2 | [cursor.com/blog/automations](https://cursor.com/blog/automations) | Product blog (05.03.2026) | Кейсы review/monitoring/chores, Rippling cron каждые 2 ч, шаблоны | Не пошаговый UI-гайд | Новостной тон без action steps |
| 3 | [cursor.com/changelog/03-05-26](https://cursor.com/changelog/03-05-26) | Changelog GA | Дата запуска Automations, sandbox + MCP + memory | Одна страница | Отдельная «новость» без how-to |
| 4 | [datacamp.com/tutorial/cursor-automations-hands-on-guide](https://www.datacamp.com/tutorial/cursor-automations-hands-on-guide) | EN hands-on (2026) | Таблица триггеров, cron + repo для scheduled, Send to Slack vs Slack MCP | Не RU; фокус dev-команды | Структура 1:1 |
| 5 | [aiforpm.ru/blog/cursor-automations-guide](https://aiforpm.ru/blog/cursor-automations-guide) | RU how-to | PM-аудитория, cron UTC→MSK, 7 шагов | Пересекается с нашим intent | Каннибализацию без дифференциации (у нас — cron bug + webhook Bearer + billing guardrails) |
| 6 | [ardenisov.ru/cursor-automations-kak-polzovatsya/](https://ardenisov.ru/cursor-automations-kak-polzovatsya/) | RU обзор | 5 типов триггеров, сценарии за 30 мин | Мало webhook/cron edge cases | Обзор без чеклиста secrets/egress |
| 7 | [mayai.ru/kak-nastroit-cursor-automations-po-webhook/](https://mayai.ru/kak-nastroit-cursor-automations-po-webhook/) | RU webhook кейс | POST + Bearer, body в промпт, регенерация key после Run as | Узкий только webhook | Подменять полный гайд одним webhook |
| 8 | [meta-journal.ru/.../nastroyka-cursor-automations-2026](https://www.meta-journal.ru/2026/08/28/nastroyka-cursor-automations-2026/) | RU longread | billing guardrails, Run history | Часто в SERP; generic | Дублировать meta-journal структуру |

**Паттерн SERP (окт 2026):** в топе — **официальная docs Cursor** + англоязычные tutorial (DataCamp, byteiota, NextPj) + русские гайды (aiforpm, ardenisov, meta-journal, neirocursor). Запрос «cursor automations настройка» закрыт фрагментами; слабое место конкурентов — **смена cron без пересоздания**, **коллизия cron + event на одной automation**, **webhook до Save**, **Run as: Service account → regenerate key**, **$2 headroom** под spend limit.

**Intent:** how_to — читатель хочет **создать и активировать** automation на [cursor.com/automations](https://cursor.com/automate) с **Scheduled (cron)**, **Webhook (POST)** или **GitHub PR**, задать repo scope, secrets/MCP, прогнать test run и читать Run History.

**Пробел для «Ковчег»:** один русский workflow **B-режима**: Automations vs ручной Cloud Agent → три типа триггера (cron / webhook / GitHub) → чеклист billing + secrets + forum workarounds; язык для автоматизатора/маркетолога с GitHub, не только для Staff Engineer.

---

## 2. Яндекс Wordstat (MCP `user-mcp-kv`)

⚠️ **WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` / `wordstat_get_top_requests` не подключён в run 2026-10-15. Точные показы/мес **не получены** — цифры спроса в текст статьи не ставить.

**Семантика (экспертная оценка + SERP, без Wordstat):**

| Фраза (кандидат) | Комментарий |
|------------------|-------------|
| cursor automations настройка | primary_query карточки B06 |
| cursor automations cron | secondary; форум UTC/CRON_TZ |
| cursor automations webhook | secondary; docs + Bearer key |
| автоматизация cloud agents cursor | RU long-tail |
| cursor automations github pr | PR-триггеры, fork limitation |

### LSI для writer (SERP + docs)

- cursor.com/automations, New Automation, Run History, Test run  
- scheduled trigger, cron expression, CRON_TZ, UTC  
- webhook URL после Save, Authorization Bearer, POST JSON body в промпт  
- GitHub pull request opened / merged / push to main  
- no repository / single repo / multi-repo environment  
- Run as Me vs Service account, spend limit, on-demand billing  
- /automate skill, Marketplace template, Bugbot / Security Agents  
- MCP server tool, Memories, Computer use, egress  

**SEO-стратегия:** primary «cursor automations настройка» в H1/lead; secondary cron, webhook, github pr — в H2 и FAQ. Англ. «cursor automations» — в alt/schema где уместно.

---

## 3. Таблица фактов (цифры и утверждения только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Cursor Automations: cloud agents в фоне по расписанию или событиям GitHub, GitLab, Slack, webhooks, Linear и др. | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 15.10.2026 | да |
| Создание: Agents Window, cursor.com/automations, skill `/automate`, шаблон Marketplace | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 15.10.2026 | да |
| Шаги: trigger → prompt → optional tools (Slack, PR comment, MCP) → repo scope → save & activate | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 15.10.2026 | да |
| Automations биллятся как cloud agent usage; у automations нет переключателя context window — максимум модели | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 15.10.2026 | да |
| Run as Me: usage на создателя; Service account: на team usage pool, отдельный service account | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 15.10.2026 | да |
| Scheduled: пресеты или cron; запуск может задерживаться, но не раньше указанного времени | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 15.10.2026 | да |
| Для Slack/cron по умолчанию **без репозитория**; для code changes нужно явно указать repo | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 15.10.2026 | да |
| Source control triggers: **обязателен** repo или multi-repo | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 15.10.2026 | да |
| Webhook URL и API key появляются **только после Save** automation | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 15.10.2026 | да |
| PR-триггеры **не** работают на PR из fork («Fork pull requests not supported»); merged PR — исключение | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 15.10.2026 | да |
| Смена Run as на Service account: **regenerate webhook API key**; проверить MCP OAuth для service account | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 15.10.2026 | да |
| Computer use включён по умолчанию для каждой automation | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 15.10.2026 | да |
| GA Automations объявлены **5 марта 2026** (changelog) | [cursor.com/changelog/03-05-26](https://cursor.com/changelog/03-05-26) | 05.03.2026 | да |
| При invoke: cloud sandbox, MCP/модели из конфига, memory tool | [cursor.com/changelog/03-05-26](https://cursor.com/changelog/03-05-26) | 05.03.2026 | да |
| Триггеры GA: Slack, Linear, GitHub, PagerDuty, webhooks (+ schedules) | [cursor.com/changelog/03-05-26](https://cursor.com/changelog/03-05-26) | 05.03.2026 | да |
| Cron schedules в Automations выполняются в **UTC** (Colin, Cursor team) | [forum.cursor.com/t/automations-show-human-readable-description-for-cron-schedules/164058/6](https://forum.cursor.com/t/automations-show-human-readable-description-for-cron-schedules/164058/6) | 25.06.2026 | да |
| Локальное время cron: префикс `CRON_TZ=America/New_York` (пример из forum) | [forum.cursor.com/t/automations-show-human-readable-description-for-cron-schedules/164058/6](https://forum.cursor.com/t/automations-show-human-readable-description-for-cron-schedules/164058/6) | 25.06.2026 | да (как workaround; MSK — подобрать TZ) |
| Баг: смена daily→weekly cron может оставить daily runs; workaround — **удалить и создать заново** с нужным cron | [forum.cursor.com/t/automations-cron-not-working-correctly/154618](https://forum.cursor.com/t/automations-cron-not-working-correctly/154618) | 12.03.2026 | да (forum, confirmed bug) |
| Баг weekday cron: stale scheduler entries; fix — save с мелким изменением или пересоздание | [forum.cursor.com/t/automation-runs-daily-despite-cron-rule-saying-weekdays/155861](https://forum.cursor.com/t/automation-runs-daily-despite-cron-rule-saying-weekdays/155861) | 25.03.2026 | да |
| Hourly cron может перестать fire из‑за «stuck» run; workaround — delete + recreate automation | [forum.cursor.com/t/cursor-automations-stopped-running-on-hourly-schedule/155679](https://forum.cursor.com/t/cursor-automations-stopped-running-on-hourly-schedule/155679) | 23.03.2026 | да |
| Cron + Sentry на одной automation: cron может считаться duplicate активного run; split на две automations | [forum.cursor.com/t/cron-automation-stopped-running/165257](https://forum.cursor.com/t/cron-automation-stopped-running/165257) | 09.07.2026 | да |
| Cloud Agents: on-demand billing должен быть включён; перед первым run — **spending limit** | [forum.cursor.com/t/what-is-the-pricing-structure-for-using-cloud-agents/156843](https://forum.cursor.com/t/what-is-the-pricing-structure-for-using-cloud-agents/156843) | 07.04.2026 | да |
| Spend limiter: нужно ~**$2 headroom** под hard limit, иначе run не стартует | [forum.cursor.com/t/what-is-the-pricing-structure-for-using-cloud-agents/156843](https://forum.cursor.com/t/what-is-the-pricing-structure-for-using-cloud-agents/156843) | 30.04.2026 | да |
| Cloud Agents: included usage **сначала**, затем on-demand; **нет** отдельной платы за VM/RAM (официальный ответ kevinn) | [forum.cursor.com/t/what-is-the-pricing-structure-for-using-cloud-agents/156843](https://forum.cursor.com/t/what-is-the-pricing-structure-for-using-cloud-agents/156843) | 09.09.2026 | да |
| Outbound webhooks агента: только `statusChange` ERROR/FINISHED; verify HMAC `X-Webhook-Signature` | [cursor.com/docs/cloud-agent/api/webhooks](https://cursor.com/docs/cloud-agent/api/webhooks) | 15.10.2026 | да |
| Cloud Agents доступны на **paid** планах; cron/event — через Automations | [cursor.com/help/ai-features/cloud-agents](https://cursor.com/help/ai-features/cloud-agents) | 15.10.2026 | да |
| Bugbot как automation: тысячи триггеров/день, миллионы пойманных багов (marketing claim) | [cursor.com/blog/automations](https://cursor.com/blog/automations) | 05.03.2026 | да (как кейс Cursor, не как SLA) |
| Plan **Start** (India): Cloud Agents есть, **Automations нет** — нужен Pro+ | [cursor.com/docs/account/pricing](https://cursor.com/docs/account/pricing) | 15.10.2026 | да |

**fact-bank.md:** записей по Cursor Automations **нет** — факты только из таблицы выше (приоритет docs + forum staff).

**Не использовать без оговорки:** точные $/run и «Pro не включает cloud» — форум содержал противоречивые ответы; в статье опираться на актуальные [models-and-pricing](https://cursor.com/docs/models-and-pricing) и help cloud-agents.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **30–45 минут** пройти путь от нуля до **рабочей automation** с одним из трёх триггеров (cron digest, webhook из формы/CI, GitHub PR review), с **узким** trigger и repo scope, test run + Run History, и **guardrails** по billing/secrets.

**Отличие от конкурентов:**
- Docs — канон, но без MSK/UTC и forum workarounds.
- RU-гайды редко связывают **webhook Save-first**, **service account key regen**, **cron bug → recreate**.
- «Ковчег»: автоматизатор + Make-мышление, internal links B03 (MCP), B04/environment-json.

**Tone:** automation = «триггер + промпт + tools»; cron = «будильник в UTC»; webhook = «кнопка POST с Bearer». Без hype «замените n8n».

**H2-каркас (из карточки B06 + research):**
1. Automations vs ручной Cloud Agent; no-repo / single / multi-repo  
2. Создание на cursor.com/automations: trigger, prompt, tools, MCP  
3. Cron: пресеты, cron, UTC/MSK, баг смены расписания → пересоздание  
4. Webhook: Save → URL + API key, curl POST, body в промпт  
5. GitHub PR / Slack / Linear: минимальные шаблоны промпта  
6. Чеклист: secrets, spend limit + $2 headroom, service account, egress/MCP OAuth  

---

## 5. Сценарии-черновики для writer

| Сценарий | Trigger | Repo | Tools | Ожидание run |
|----------|---------|------|-------|--------------|
| Утренний digest в Slack | Scheduled 09:00 + CRON_TZ или UTC offset | Single repo main | Send to Slack, read git | Сообщение без PR |
| Заявка с сайта | Webhook POST JSON | No repo | MCP/email по необходимости | Ответ в history |
| PR smoke review | GitHub PR opened | Тот же repo | Comment on PR | Комментарий или «no issues» |
| Push main security | Push to branch main | Single | Send to Slack | Алерт только high-risk |

---

## 6. FAQ-кандидаты (из карточки + research)

1. **Нужен ли репозиторий для cron automation?** — Нет по умолчанию для scheduled; да, если agent должен менять код/открывать PR.  
2. **Как передать webhook body в промпт?** — JSON POST; по практике forum/community тело попадает в контекст промпта (проверить в Run History после test POST).  
3. **Почему cron не по расписанию?** — UTC vs MSK; stale schedule после edit → пересоздать automation; stuck run → recreate; не смешивать тяжёлый event-trigger и cron на одной automation.  
4. **Почему нет webhook URL?** — Сначала Save automation.  
5. **Fork PR не триггерит?** — Ожидаемое ограничение docs; merged PR — другое.  
6. **Automations на каком плане?** — Paid; Automations не на Start (India) — см. pricing docs.  
7. **Кто платит за run?** — Me → creator; Service account → team pool.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Automations 40–60 слов | Lead | trigger + prompt + cloud agent |
| Таблица триггеров (cron / webhook / GitHub) | H2 | Сравнение + когда что выбирать |
| Пример curl webhook | H2 webhook | POST + Bearer |
| Workflow | H2 | Dashboard → trigger → prompt → tools → repo → test → history |
| FAQ 5–7 | Конец | Ответы-действия |
| Internal | Тело | `/podklyuchenie-mcp-cursor/`, `/cursor-environment-json-cloud-agents/` |

**Целевые формулировки:** «cursor automations настройка», «cursor automations cron», «cursor automations webhook», «автоматизация cloud agents cursor».

---

## 8. Риски для writer

- Не выдумывать UI-лейблы 2026 — сверять с docs; дата research 15.10.2026.  
- Forum bugs — помечать «известная проблема / workaround», не как вечный закон продукта.  
- Min **5** нумерованных шагов + чеклист **10+** (utility gate статьи).  
- CTA ≤ 3; не подменять гайд рекламой Make.  
- Без эмодзи; дефис вместо длинного тире.  
- **Не писать** показы Wordstat — MCP недоступен.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст и активирует automation на cursor.com/automations с триггером Scheduled (cron с учётом UTC), Webhook (POST с Bearer после Save) или GitHub PR, задаст repo scope и tools/MCP, выполнит test run, проверит Run History и настроит spend limit и secrets так, чтобы автоматизация не съедала бюджет на широких триггерах.

**action_outline (для writer):**

1. **Проверить план и billing:** paid Cursor, on-demand включён, задан spending limit с запасом ~$2 до hard cap ([forum 156843](https://forum.cursor.com/t/what-is-the-pricing-structure-for-using-cloud-agents/156843)).  
2. **Открыть** [cursor.com/automations](https://cursor.com/automate) → New Automation; при необходимости подключить GitHub/Slack в Integrations.  
3. **Выбрать trigger:** Scheduled / Webhook / GitHub PR — один узкий сценарий на первую automation (не «на всё сразу»).  
4. **Написать prompt** с правилами: когда комментировать PR, когда молчать, формат вывода; @-mention включённых tools.  
5. **Repo scope:** no-repo для webhook-only Slack; single-repo + branch для cron с кодом; multi-repo только если нужен environment.  
6. **Tools:** включить только нужное (Send to Slack, Comment on PR, MCP); для MCP — см. internal B03; проверить OAuth при Run as Service account.  
7. **Cron:** задать пресет или cron; перевести желаемое MSK-время в UTC или `CRON_TZ=...`; **не менять** расписание in-place при баге — пересоздать automation.  
8. **Webhook:** Save → скопировать URL и API key → test `curl -X POST` с `Authorization: Bearer` и JSON body → проверить Run History.  
9. **Activate + Run History:** один manual test run; для GitHub — тестовый PR не из fork; мониторить duplicate/skipped cron в history.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (28 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + `research-serp.json` + карточка B06 + `site-brief.md`.
