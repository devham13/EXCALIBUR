# Research notes — B06 «Как настроить Cursor Automations: пошаговая инструкция по Cloud Agents для бизнеса»

**topic_id:** B06  
**slug:** nastroyka-cursor-automations  
**article_mode:** B (how-to)  
**research_date:** 2026-09-11  
**disclaimer:** Все даты, версии и статистика проверены на 11.09.2026.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | Официальная docs (EN) | Канон: триггеры, tools, billing, repo scope, webhook, cron, permissions | Английский; мало бизнес-кейсов на русском | Сухой перевод без сценариев «бриф к утру / заявка из CRM» |
| 2 | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | Официальная help | Таблица триггеров, FAQ no-repo, billing one-liner | Короткая; нет CRON_TZ и Make/n8n | Копировать 1:1 без расширения |
| 3 | [cursor.com/blog/automations](https://cursor.com/blog/automations) | Product blog (05.03.2026) | Реальные кейсы Cursor/Rippling: security review, PagerDuty, cron digest | Новостной тон; не пошаговый гайд | News-формат «вышло обновление» без шагов |
| 4 | [learncursor.dev/learn/cursor-agents/cloud-agent-automations](https://www.learncursor.dev/learn/cursor-agents/cloud-agent-automations) | EN how-to 2026 | 5 шагов, таблица триггеров, Max Mode billing note | EN; нет webhook POST-примера для Make | Структуру 1:1 |
| 5 | [byteiota.com/cursor-automations-tutorial-2026-setup-guide](https://byteiota.com/cursor-automations-tutorial-2026-setup-guide/) | EN tutorial | Setup, self-hosted machines, pricing mention | Коммерческий bias; мало RU | Продажу своих услуг |
| 6 | [mayai.ru/kak-nastroit-cursor-automations-po-webhook](https://mayai.ru/kak-nastroit-cursor-automations-po-webhook/) | RU how-to (смежный intent) | Webhook POST + Bearer, no-repo, history check | Узкий intent (только webhook); каннибализация | Дублировать webhook-статью — в B06 webhook = один H2 |
| 7 | [mayai.ru/kak-nastroit-cursor-automations-po-raspisaniyu](https://mayai.ru/kak-nastroit-cursor-automations-po-raspisaniyu/) | RU how-to (cron) | CRON_TZ=Europe/Moscow, no-repo для брифов | Узкий intent (только cron) | То же — cron = секция, не отдельная статья |
| 8 | [kingy.ai/news/cursor-automate-skill-ai-coding-agents](https://kingy.ai/news/cursor-automate-skill-ai-coding-agents/) | EN guide `/automate` | Skill-based creation, safety, Cloud Agent env | News URL; не для бизнес-аудитории «Ковчег» | News-угол |

**Паттерн SERP:** топ — официальные cursor.com/docs + blog/changelog; второй слой — EN tutorials 2026; русский контент фрагментирован (отдельные статьи «только webhook» / «только cron» на mayai и Дзен). Запрос «настройка cursor automations» почти не закрыт **единым** русским how-to с триггерами + billing + Make/n8n.

**Intent:** how_to — пользователь хочет **создать и активировать** первую Automation (trigger → prompt → tools → repo scope), проверить Run History, настроить cron или webhook для бизнес-процесса без ручного чата.

**Пробел для «Ковчег»:** пошаговый гайд на русском для автоматизатора/маркетолога: Cloud Agent vs Automation vs чат; spend limit + Secrets; cron с московским временем; webhook из Make/n8n/CRM; связка с B03 (MCP) и B05 (контент-завод). Язык «на пальцах», не Senior-only.

**GEO-контекст (не main angle):** в свежем SERP встречаются материалы о ограничениях Cursor в РФ (сентябрь 2026). Writer: одним абзацем в FAQ/рисках — проверить доступ аккаунта/VPN/корпоративный план; **не** строить статью вокруг новости блокировки.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 11.09.2026)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в Cloud Agent окружении (namespace отсутствует в dynamic tools). Вызов `wordstat_get_top_requests` для `cursor automations` выполнить не удалось. **Точные объёмы показов не получены** — цифры ниже не использовать в тексте статьи.

### Экспертная семантика (SERP + secondary queries, без Wordstat-цифр)

| Кластер | Фразы-кандидаты | Назначение в статье |
|---------|-----------------|---------------------|
| Primary EN | cursor automations, cursor cloud agents | H1, lead, slug |
| Setup RU | настройка cursor automations, cursor automations webhook, cursor automations cron | H2, FAQ |
| Смежные | cursor automate skill, cursor automations make n8n | Workflow H2 |
| Long-tail | CRON_TZ Europe/Moscow cursor, webhook API key cursor automation | Troubleshooting |

### LSI для writer (из SERP + docs, без выдуманных показов)

- cursor automations настройка, cloud agents, trigger prompt tools  
- cursor automations cron, scheduled trigger, CRON_TZ  
- cursor automations webhook, POST Bearer API key  
- /automate skill, cursor.com/automations, Agents Window  
- no repository, multi-repo environment, Run History  
- MCP, Memories, computer use, spend limit, on-demand billing  
- Make.com, n8n, CRM webhook, Slack trigger  

**SEO-стратегия:** primary «cursor automations» в title/lead; secondary «настройка cursor automations», «cursor cloud agents» — в H2; long-tail cron/webhook — в соответствующих секциях и FAQ. После восстановления Wordstat — перепроверить показы и скорректировать FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Cursor Automations анонсированы 5 марта 2026: always-on agents по расписанию или событиям (Slack, Linear, GitHub PR, PagerDuty, webhooks) | [cursor.com/changelog/03-05-26](https://cursor.com/changelog/03-05-26) | 05.03.2026 | да |
| При запуске automation агент поднимает cloud sandbox, следует инструкциям с настроенными MCP и моделями, верифицирует результат; доступен memory tool | [cursor.com/blog/automations](https://cursor.com/blog/automations) | 05.03.2026 | да |
| Создать automation: Agents Window, [cursor.com/automations](https://cursor.com/automate), skill `/automate` в локальной сессии, или шаблон Marketplace | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Пять шагов: trigger → prompt → optional tools → repo scope (none/single/multi) → save & activate | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| `/automate` skill: описать workflow plain language — Cursor настраивает triggers, instructions, tools | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Automation может иметь **несколько** triggers; запуск при срабатывании **любого** | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Для Slack и cron по умолчанию **нет** repository; для source control triggers repo **обязателен** | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Scheduled: preset или **cron expression**; запуск может быть с задержкой, но не раньше указанного времени | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Webhook: private HTTP endpoint; URL и API key появляются **только после Save** automation | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Source control: GitHub, GitLab, Bitbucket Cloud; GitHub — полный набор триггеров (CI completed, labels, review comments и др.) | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| PR из fork не поддерживаются (кроме trigger PR merged) — ошибка «Fork pull requests not supported» | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Slack triggers: только **public** channels; emoji reaction, channel created, new message | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Tools: PR creation (default on), comment on PR, request reviewers, Send/Read Slack, MCP, Memories, **computer use** (default on) | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Memories: `MEMORIES.md` by default; enabled by default; осторожно с untrusted input | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Billing: automations = cloud agent runs; **maximum context window** модели, без переключателя context | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Private/Team Visible billing → создатель; Team Owned → team usage pool + service account | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Promote to Team Owned: перегенерировать webhook API key; перенастроить MCP OAuth на service account | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| GitHub identity: comments/approvals as `cursor`; private automations open PR as user account; team-scoped as `cursor` | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 11.09.2026 | да |
| Help: automations без repo **не клонируют код** — для Slack/MCP/webhook/Linear/PagerDuty workflows | [cursor.com/help/ai-features/automations](https://cursor.com/help/ai-features/automations) | 11.09.2026 | да |
| Cloud Agents доступны на **всех paid plans**; тарификация по API pricing выбранной модели | [cursor.com/help/ai-features/cloud-agents](https://cursor.com/help/ai-features/cloud-agents) | 11.09.2026 | да |
| Pro **$20/mo** включает Cloud Agents; plan **Start (India)** **не** включает Automations — нужен Pro+ | [cursor.com/docs/account/pricing](https://cursor.com/docs/account/pricing) | 11.09.2026 | да |
| Bugbot (reference automation): triggered **thousands of times a day**; caught **millions of bugs** since launch | [cursor.com/blog/automations](https://cursor.com/blog/automations) | 05.03.2026 | да (как product claim Cursor) |
| Cursor Projects (10.09.2026): coordinator + schedule/Slack/PR subscriptions — смежный продукт, не замена Automations UI | [cursor.com/changelog](https://cursor.com/changelog) | 10.09.2026 | да (краткое сравнение в H2-1) |
| Aug 19 2026: cloud agents subscriptions — PR monitor, Slack thread, cron (пересекается с Automations) | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Forum (staff): cloud agents потребляют **included usage first**, затем on-demand; нужен on-demand enabled + spend limit | [forum.cursor.com/t/what-is-the-pricing-structure-for-using-cloud-agents/156843](https://forum.cursor.com/t/what-is-the-pricing-structure-for-using-cloud-agents/156843) | 2026 | да (community + staff correction, не официальный SLA) |
| Forum: spend limiter требует ~**$2 headroom** под hard limit перед стартом Cloud Agent run | [forum.cursor.com/t/what-is-the-pricing-structure-for-using-cloud-agents/156843](https://forum.cursor.com/t/what-is-the-pricing-structure-for-using-cloud-agents/156843) | 2026 | да (community tip) |
| Power users (multiple agents/automation): often **$200+/mo** total usage (ориентир Cursor pricing page) | [cursor.com/docs/account/pricing](https://cursor.com/docs/account/pricing) | 11.09.2026 | да |
| **CRON_TZ=Europe/Moscow** в cron string для локального времени — community workaround (не в официальной docs на 11.09.2026) | [mayai.ru/kak-nastroit-cursor-automations-po-raspisaniyu](https://mayai.ru/kak-nastroit-cursor-automations-po-raspisaniyu/) | 2026 | да (с пометкой «проверьте в Run History») |

**Не использовать без оговорки:** «Automations всегда в Max Mode» — в learncursor есть формулировка; официальная docs (09.2026) говорит о max **context window** cloud agents, не legacy Max Mode toggle. Писать: «полное контекстное окно модели, без уменьшения в UI».

**fact-bank.md:** фактов по Cursor Automations нет — все цифры только из таблицы выше. Общие факты про ROI контент-заводов (mayai) — не подменять ими pricing Cursor.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **30–45 минут** пройти путь от paid-аккаунта до **работающей Automation** с одним триггером (cron **или** webhook), проверить Run History, подключить минимальный tool stack (Slack/MCP по необходимости) и понять billing/no-repo vs repo-backed сценарии для бизнеса.

**Почему отличается от конкурентов:**
- Официальная docs — канон, но без Make/n8n и «бриф к утру» для не-dev.
- EN tutorials не закрывают русский intent «настройка cursor automations».
- mayai уже разбил webhook/cron на отдельные URL — B06 = **единый** гайд по карточке B06.
- «Ковчег»: автоматизация бизнес-процессов, связка с B03 (MCP) и B02 (Make/n8n как внешний оркестратор webhook).

**Tone:** Automation = «робот-смена, который просыпается по будильнику или звонку webhook и делает одну задачу по инструкции»; Cloud Agent в чате = «разовый подрядчик». Без hype «25% рынка AI-tools» из пересказов новостей.

**H2-каркас (из карточки + research):**
1. Cloud Agent vs Automation vs чат vs Projects (2026)  
2. Подготовка: Pro+, on-demand, spend limit, Secrets, GitHub  
3. Первая Automation: UI `/automate` или cursor.com/automations/new  
4. Cron: preset vs custom, CRON_TZ, no-repo бриф  
5. Webhook: Save → URL + API key → POST из Make/n8n  
6. MCP, Memories, multi-repo для сложных сценариев  
7. Чек-лист безопасности и типичные ошибки  

**Conversion (conversion-map.md):**
- CTA Make/kv-ai — max 2×: «webhook из Make + MCP в Cursor» → [kv-ai.ru/obuchenie-po-make](https://kv-ai.ru/obuchenie-po-make)  
- Internal: [B03 MCP](/podklyuchenie-mcp-cursor/), [B05 контент-завод](/avtonomnyj-kontent-zavod-nejroseti/)  
- Telegram @maya_pro — 1× если уместно  

---

## 5. Сценарии для writer (черновик)

| Сценарий | Trigger | Repo scope | Tools | Для кого |
|----------|---------|------------|-------|----------|
| Утренний бриф | Scheduled (cron) | No repository | Send to Slack (opt.) | Маркетолог, PM |
| Review PR на баги | PR opened/pushed | Single repo | Comment on PR | Dev team |
| Заявка с сайта | Webhook POST | No repository | MCP + Slack | Support/продажи |
| Security scan | Push to main | Single repo | Send to Slack | Tech lead |
| Триаж Slack | New message + keyword | Single or none | Linear MCP, PR creation | Support |

**Рекомендация writer:** один **полный** walkthrough — cron no-repo бриф; webhook — второй мини-кейс с curl/HTTP Request Make; PR-review — упомянуть как следующий шаг со ссылкой на docs.

---

## 6. FAQ-кандидаты (5–7)

1. **Чем Cursor Automations отличается от Cloud Agent в чате?** — Automations = фоновые runs по trigger без ручного prompt; чат = разовая задача.  
2. **Нужен ли репозиторий?** — Нет для cron/Slack/webhook без правок кода; да для PR/push triggers.  
3. **Как настроить cron по Москве?** — Custom cron; community: `CRON_TZ=Europe/Moscow 0 9 * * 1-5`; сверить Run History.  
4. **Сколько стоит?** — Cloud agent API pricing; included usage first (forum); Pro $20/mo минимум для Automations; установить spend limit.  
5. **Где взять webhook URL?** — Только после Save automation; Bearer с API key в POST.  
6. **Можно ли без GitHub?** — Да для no-repo workflows; для code changes — подключить GitHub/GitLab/Bitbucket или Origin.  
7. **Automations vs Cursor Projects?** — Projects = long-running coordinator + shared context; Automations = trigger-action factory (кратко, без ухода в beta-news).

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Automations 40–60 слов | Lead после H1 | «Cursor Automations — …» |
| Таблица trigger → когда использовать | H2-3 | 5–7 строк |
| Workflow A→B→C | H2-3–5 | Подготовка → Create → Test run → Monitor billing |
| Пример cron + webhook (curl) | H2-4–5 | Блоки кода |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |
| E-E-A-T | Автор | Артур Хорошев, автоматизация Make + Cursor |

**Целевые формулировки:** «cursor automations», «настройка cursor automations», «cursor cloud agents», «cursor automations webhook», «cursor automations cron».

---

## 8. Риски для writer

- Не выдумывать pricing per-run — только API rates + spend limit + included pool.  
- CRON_TZ — community workaround; предложить проверку timestamp в Run History.  
- Не копировать byteiota/learncursor 1:1.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Min **5** нумерованных шагов + чеклист **10+** пунктов (utility gate статьи).  
- Webhook secrets/API key — не в скриншотах; Dashboard Secrets для токенов Slack и т.д.  
- Russia access — 1 абзац FAQ, не lead.  
- Projects (10.09.2026) — не смешивать UI с Automations page без пояснения.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель включит on-demand billing и spend limit, создаст Automation через cursor.com/automations или `/automate`, выберет trigger (cron или webhook), задаст prompt и repo scope, сохранит и проверит успешный run в History; при необходимости отправит POST из Make/n8n и настроит mосковское расписание с проверкой фактического времени запуска.

**action_outline (для writer):**

1. **Проверить план:** Pro/Pro Plus/Ultra (не Start India); включить **on-demand billing** и задать **spend limit** с запасом ~$2 headroom (forum tip).  
2. **Подключить интеграции:** GitHub/GitLab при repo-backed сценарии; Slack/Linear по задаче; Secrets в dashboard для API-токенов.  
3. **Открыть** [cursor.com/automations/new](https://cursor.com/automate) или Agents Window → New Automation (альтернатива: `/automate` в локальном Agent).  
4. **Выбрать trigger:** Scheduled (preset для первого test) **или** Webhook; для брифа без кода — cron + **No repository**.  
5. **Написать prompt:** формат выхода (markdown), длина, критерий готовности, явные запреты (no PR, no clone если no-repo).  
6. **Включить tools по минимуму:** Send to Slack / MCP только если нужны; оставить computer use осознанно.  
7. **Save & Activate** → для webhook скопировать URL + API key → отправить тестовый **POST** с `Authorization: Bearer <key>` и JSON-телом.  
8. **Проверить Run History:** статус FINISHED, output, billing dashboard; для cron — при сдвиге времени попробовать `CRON_TZ=Europe/Moscow …` и re-save.  
9. **Масштабировать:** добавить MCP (→ B03), multi-repo environment, Team Owned для командного billing — по чек-листу раздела 8.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ unavailable (SERP fallback) |
| Таблица фактов с URL | ✅ (26 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + `conversion-map.md`.
