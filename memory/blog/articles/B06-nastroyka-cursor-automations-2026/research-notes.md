# Research notes — B06 «Как настроить Cursor Automations и Cloud Agents: пошаговая инструкция по event-driven автоматизации»

**topic_id:** B06  
**slug:** nastroyka-cursor-automations-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-08-28  
**disclaimer:** Все даты, версии и статистика проверены на 28.08.2026.

---

## 1. SERP-обзор (WebSearch, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | Официальная docs (EN) | Канон: триггеры, repo scope, `/automate`, промпты, MCP | Английский; мало troubleshooting UTC/MSK | Сухой перевод без сценариев «бриф к утру / PR-review» |
| 2 | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | Официальная help (EN) | Таблица триггеров, tools, billing, permission levels | Нет связки с `/goal`, Subscriptions, environment.json | Копировать 1:1 без русского workflow |
| 3 | [learncursor.dev/guides/cursor-automations](https://www.learncursor.dev/guides/cursor-automations) | Гайд 2026 (EN) | `/automate`, фильтры триггеров, team playbook, Memories | Новостной уклон (June 2026 update) | Структуру 1:1; news-формат без шагов |
| 4 | [datacamp.com/tutorial/cursor-automations-hands-on-guide](https://www.datacamp.com/tutorial/cursor-automations-hands-on-guide) | Hands-on EN (2026) | PR review + cron, MCP в Automations, Run History | Для разработчиков; нет RU и MSK/cron | Коммерческий bias DataCamp |
| 5 | [pondero.ai/coding/guides/cursor-v35-automations-setup-may-2026](https://pondero.ai/coding/guides/cursor-v35-automations-setup-may-2026/) | Гайд v3.5 (EN) | No-repo + multi-repo, Marketplace templates | Узкий фокус на Slack digest / finance | Шаблонные сценарии как единственный путь |
| 6 | [startdebugging.net/2026/07/build-a-cursor-automation-with-automate-skill-and-github-triggers](https://startdebugging.net/2026/07/build-a-cursor-automation-with-automate-skill-and-github-triggers/) | GitHub triggers + `/automate` | 5 GitHub-триггеров июня 2026, tool toggles | Billing «Max Mode» — не официальный канон | Утверждение «всегда Max Mode» без ссылки на docs |
| 7 | [mayai.ru/kak-nastroit-cursor-automations-po-raspisaniyu](https://mayai.ru/kak-nastroit-cursor-automations-po-raspisaniyu/) | RU how-to (cron) | No-repo бриф, Test run, UTC→MSK | Узкий intent (только schedule) | Каннибализация: B06 шире (Agents + events + troubleshooting) |
| 8 | [mayai.ru/cursor-cloud-agents-avtomatizaciya](https://mayai.ru/cursor-cloud-agents-avtomatizaciya/) | RU обзор Agents | Secrets dashboard, spend limit, MCP «на пальцах» | Мало event-driven (/goal, subscriptions) | Пересказ без чеклиста troubleshooting |

**Паттерн SERP:** доминируют официальные docs Cursor + англоязычные tutorials (DataCamp, Learn Cursor, Pondero). Русскоязычный топ — узкие статьи mayai (cron, webhook). **Пробел:** единый русский how-to «Cloud Agents vs Automations → первая Automation → cron/GitHub → secrets → /goal → troubleshooting UTC/403» для автоматизаторов и маркетологов без глубокого dev-бэкграунда.

**Intent:** how_to — пользователь хочет **создать и активировать** Automation (или понять, когда нужен Cloud Agent вручную vs Automation), выбрать trigger, scope репозитория, secrets, сделать Test run и прочитать Run History. Вторичные: cron по Москве, GitHub PR, webhook, MCP-tools.

**Пробел для «Ковчег»:** event-driven автоматизация на русском с decision tree «Agent mode vs Automation», чеклист подготовки среды, два сценария (no-repo бриф + repo PR-review), блок Aug 2026 (/goal, Subscriptions, subagent VMs), troubleshooting UTC и secrets — без новостного «вышло обновление».

---

## 2. Яндекс Wordstat

⚠️ **WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` не подключён в текущем Cloud Agent run (инструмент `wordstat_get_top_requests` недоступен). **Точные показы/мес не получены — цифры спроса в текст статьи не использовать.** После подключения MCP повторить запросы: `cursor automations`, `cursor cloud agents настройка`, `cloud agents cursor github`, `cursor automations cron`, `автоматизация cursor по расписанию`.

### SERP-fallback: семантический кластер (без объёмов)

| Кластер | Запросы (primary + secondary + LSI из SERP) | Роль в статье |
|---------|---------------------------------------------|---------------|
| Core EN | cursor automations, cursor automate, cursor.com/automations | H1, lead, URL dashboard |
| Cloud Agents | cursor cloud agents, cloud agents cursor github, cursor cloud agents настройка | H2 «Agents vs Automations» |
| Schedule | cursor automations cron, автоматизация cursor по расписанию, scheduled trigger | H2 cron + UTC/MSK |
| Events | github pr automation cursor, webhook cursor automation, slack trigger | H2 triggers |
| Skills | /automate skill cursor, cursor marketplace automation template | Альтернативный путь создания |
| Long-tail RU | как настроить cursor automations, cursor agent по расписанию | FAQ |

### LSI для writer (из SERP + карточка B06)

- cursor automations, cloud agents, event-driven, trigger, scheduled, cron UTC  
- no repository / single repository / multi-repo environment  
- `/automate`, `/goal`, subscriptions, Run History, Test run  
- Dashboard Secrets, `.cursor/environment.json`, spend limit  
- GitHub PR opened, webhook API key, MCP server, Memories  
- Max Mode / API pricing — только с официальной формулировкой help  
- internal: [B03 MCP](/podklyuchenie-mcp-cursor/)

**SEO-стратегия (до Wordstat):** primary «cursor automations» в H1/lead; secondary «cursor cloud agents настройка», «cursor automations cron», «автоматизация cursor по расписанию» — в H2 и FAQ. После восстановления MCP — уточнить приоритеты по таблице показов.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Cursor Automations запускают Cloud Agents в фоне — по расписанию или по событиям GitHub, GitLab, Slack, webhooks, Linear, PagerDuty и др. | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 28.08.2026 | да |
| Создать Automation: Agents Window, `cursor.com/automations/new` или шаблон Cursor Marketplace | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 28.08.2026 | да |
| Пять шагов настройки: trigger → prompt → optional tools → repo scope → save & activate | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 28.08.2026 | да |
| **No repository:** агент не клонирует код; подходит для Slack/MCP/webhook/Linear/PagerDuty; не может править код и открывать PR | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 28.08.2026 | да |
| **Single repository:** работа в одном репо и ветке — review/изменения кода | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 28.08.2026 | да |
| **Multi-repo environment:** задача на нескольких репозиториях в одной среде | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 28.08.2026 | да |
| Automation может иметь несколько триггеров; запуск — когда срабатывает **любой** из них | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 28.08.2026 | да |
| Scheduled trigger: preset или cron expression | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 28.08.2026 | да |
| Для Slack и cron Cursor **по умолчанию** не подключает репозиторий; для source control triggers repo **обязателен** | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 28.08.2026 | да |
| Tools: Comment on PR, Request reviewers, Send to Slack, Read Slack channels, MCP server, Memories (`MEMORIES.md`) | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 28.08.2026 | да |
| Automations создают Cloud Agent runs; каждый run billed at **API pricing** выбранной модели | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 28.08.2026 | да |
| Permission levels: **Private**, **Team Visible**, **Team Owned** (последний — только team admin) | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 28.08.2026 | да |
| Webhook trigger: HTTP POST на endpoint автоматизации | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 28.08.2026 | да |
| Cloud Agents доступны на **всех paid** планах Cursor; при первом использовании просят задать spend limit | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 28.08.2026 | да |
| План **Start** (India) **не включает** Automations — нужен Pro или выше | [cursor.com/docs/models-and-pricing](https://cursor.com/docs/models-and-pricing) | 28.08.2026 | да |
| Секреты — через **Secrets tab** в dashboard (`cursor.com/dashboard/cloud-agents`); в `.cursor/environment.json` **нет поля secrets** | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 28.08.2026 | да |
| Типы секретов: Environment Variable, Runtime Secret (redacted в transcript/commits), Build Secret (только Docker build) | [cursor.com/docs/cloud-agent/security-network](https://cursor.com/docs/cloud-agent/security-network) | 28.08.2026 | да |
| Порядок environment: `.cursor/environment.json` в репо → personal saved → team saved (первое совпадение wins) | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 28.08.2026 | да |
| Agent-driven setup cloud environment: «less than **10 minutes**» (официальная формулировка) | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 28.08.2026 | да |
| **19 августа 2026:** Subscriptions — cloud agents мониторят PR, Slack thread, scheduled tasks; wake on event | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Cloud agents auto-subscribe к PR, которые сами создали; доводят до CI green, фиксят failures и bot comments | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| **`/goal`** — long-lived objective до полного завершения; пример: «fix all flaky tests and make CI green» | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Subagents на **отдельных VM** с изолированной копией проекта | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Mid-run steering: follow-up ждёт следующий tool call, не обрывает агента mid-action | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Subscriptions **пока только для cloud agents** (не local agent) | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Slack triggers: видны только **public channels**; без фильтра new-message — только top-level messages | [learncursor.dev/learn/cursor-agents/cloud-agent-automations](https://www.learncursor.dev/learn/cursor-agents/cloud-agent-automations) | 28.08.2026 | да (community/docs mirror) |
| Webhook URL и API key появляются **только после Save** automation | [mayai.ru/kak-nastroit-cursor-automations-po-webhook](https://mayai.ru/kak-nastroit-cursor-automations-po-webhook) | 28.08.2026 | да (практика + согласуется с docs flow) |
| Cron в Automations на форуме Cursor описан как **UTC**; UI может показывать local time — риск «9:00 стало 11:00» | [forum.cursor.com/t/automations-show-human-readable-description-for-cron-schedules/164058](https://forum.cursor.com/t/automations-show-human-readable-description-for-cron-schedules/164058) | 2026 | да (community + troubleshooting) |
| Для **9:00 MSK** (UTC+3, лето): cron UTC = `0 6 * * *` (ежедневно 06:00 UTC) | расчёт от UTC+3 + forum UTC note | 28.08.2026 | да (как формула, не product SLA) |
| Environment snapshots хранятся до **90 дней** неактивности, затем удаляются | [cursor.com/docs/cloud-agent/security-network](https://cursor.com/docs/cloud-agent/security-network) | 28.08.2026 | да |
| `/automate` skill: описать workflow на естественном языке — Cursor настраивает triggers, instructions, tools | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 28.08.2026 | да |

**Не использовать без оговорки:** «Automations всегда в Max Mode» — в официальном help только API pricing; third-party статьи могут путать с legacy Max Mode (+20% на request-based plans).

**fact-bank.md:** нет строк про Cursor Automations — все product-факты из таблицы выше.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **30–45 минут** подготовить среду (paid plan, GitHub, Secrets, при необходимости `environment.json`), создать **первую Automation** с правильным trigger и repo scope, прогнать **Test run**, прочитать Run History и устранить типичные ошибки (UTC/cron, лишние tools, secrets 403).

**Почему отличается от конкурентов:**
- Официальная docs — канон, но без русского workflow «бриф без repo + PR-review с repo».
- EN-tutorials не закрывают MSK/cron и Secrets dashboard для не-dev аудитории.
- Узкие RU-статьи mayai дробят тему (только cron или только webhook).
- «Ковчег»: decision tree Agents vs Automations, event-driven Aug 2026 (/goal, subscriptions), чеклист troubleshooting, связка с B03 MCP.

**Tone:** Automation = «агент, который просыпается сам, когда случилось событие или наступило время»; Cloud Agent = «тот же агент, но вы запускаете вручную из IDE/web»; trigger = «будильник или дверной звонок»; repo scope = «нужен ли агенту доступ к коду».

**H2-каркас (из карточки + research):**
1. Cloud Agents vs Automations: что выбрать  
2. Подготовка: paid plan, GitHub, Dashboard Secrets, `.cursor/environment.json`  
3. Создание Automation: trigger (cron, PR, Slack, webhook) + repo scope  
4. Event subscriptions и `/goal`: долгая цель до CI green  
5. Subagents на изолированных VM и mid-run steering  
6. Test run, Run History, troubleshooting (UTC, billing, secrets 403)  
7. FAQ + чеклист перед продакшеном  

**Conversion:** max 2× курс Make при уместности; internal [B03 MCP](/podklyuchenie-mcp-cursor/); CTA ≤ 3.

---

## 5. Два сценария для writer (черновик)

| Сценарий | Trigger | Repo scope | Tools | Результат |
|----------|---------|------------|-------|-----------|
| **A. Утренний бриф** | Scheduled (daily) | No repository | минимум / без MCP | markdown-бриф в Run History |
| **B. PR code review** | GitHub PR opened + PR pushed | Single repository | Comment on PR, MCP опционально | комментарии на PR без auto-merge |

**Рекомендация:** в статье полностью расписать **A** (проще для первого Test run), **B** — сокращённый второй блок или таблица «следующий шаг».

---

## 6. FAQ-кандидаты (7)

1. **Как настроить cursor automations?** — `cursor.com/automations/new` → trigger → instructions → tools → scope → Test run.  
2. **Чем cloud agents отличаются от automations?** — Cloud Agent: ручной запуск; Automation: тот же cloud agent, но trigger/event/schedule.  
3. **Нужен ли GitHub для брифа по расписанию?** — нет, выберите No repository для cron/Slack без правок кода.  
4. **Как работает /goal?** — long-lived objective в новом чате cloud agent; pair с Custom Mode или `/loop`.  
5. **Почему automation сработала не в 9:00 по Москве?** — cron считается в UTC; пересчитать hour или использовать schedule picker и сверить Run History timestamp.  
6. **Где хранить API-ключи?** — Dashboard → Cloud Agents → Secrets; не в `environment.json` и не в промпте.  
7. **Когда webhook URL пустой?** — сохраните и активируйте Automation — URL/key после Save.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Automations 40–60 слов | Lead | «Cursor Automations — …» |
| Таблица Agents vs Automations | H2-1 | Когда / кто инициирует / где runs |
| Workflow A→B→C | H2-3 | trigger → prompt → scope → activate → history |
| Таблица repo scope | H2-2–3 | No / Single / Multi |
| Таблица triggers (top-6 для RU аудитории) | H2-3 | Scheduled, PR, Slack, Webhook, Linear, CI |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «cursor automations», «cursor cloud agents настройка», «cursor automations cron», «автоматизация cursor по расписанию».

---

## 8. Риски для writer

- Не выдумывать показы Wordstat — MCP недоступен.  
- Не утверждать «Automations = всегда Max Mode» без официального источника.  
- CRON_TZ — только как community workaround с оговоркой «не в официальной docs».  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Min **5** нумерованных шагов + чеклист **10+** пунктов.  
- Без эмодзи; дефис вместо длинного тире.  
- Secrets/API keys — не печатать в примерах реальные значения.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель подключит GitHub и Secrets, выберет между Cloud Agent и Automation, создаст первую Automation (cron или GitHub) с корректным repo scope, выполнит Test run, прочитает Run History и исправит типичные сбои (UTC/cron, лишние tools, недоступные secrets); при необходимости задаст `/goal` для долгой event-driven задачи.

**action_outline (для writer):**

1. **Проверить paid plan** (Pro+; Start без Automations) и подключить GitHub/GitLab/Bitbucket в Cursor dashboard.  
2. **Задать spend limit** в Cloud Agents dashboard; добавить секреты (Runtime Secret для токенов) — **не** в git.  
3. **Выбрать сценарий:** no-repo scheduled бриф **или** single-repo PR automation — заполнить decision table H2-1.  
4. **Открыть** `cursor.com/automations/new` (или Agents Window → Automations → New); для обучения — blank, не Marketplace.  
5. **Настроить trigger:** Scheduled с preset или cron (UTC→MSK формула); для PR — GitHub PR opened + pushed + target repo.  
6. **Написать instructions:** формат выхода, запреты (no PR для брифа), decision rules «comment vs silence».  
7. **Tools + scope:** минимум tools; No repository / Single / Multi по таблице фактов; MCP — только доверенные (ссылка B03).  
8. **Save → Activate → Test run;** проверить Run History, timestamp cron, артефакт (комментарий/markdown).  
9. **Опционально:** `/goal` + subscriptions для PR-to-green; subagents для parallel fixes — отдельный подраздел Aug 2026.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ unavailable (SERP fallback) |
| Таблица фактов с URL | ✅ (28 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ (7) |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + `conversion-map.md`.
