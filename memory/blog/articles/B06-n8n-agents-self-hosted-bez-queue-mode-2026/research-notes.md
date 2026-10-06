# Research notes — B06 «Как включить n8n Agents на своём сервере: чек-лист env, Docker и обход ограничения queue mode»

**topic_id:** B06  
**slug:** n8n-agents-self-hosted-bez-queue-mode-2026  
**article_mode:** B (checklist / how-to)  
**research_date:** 2026-10-06  
**disclaimer:** Все даты, версии и статистика проверены на 06.10.2026.

---

## 1. SERP-обзор (WebSearch + research-serp.json)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [docs.n8n.io/build/build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents) | Официальная docs | Канон: Agents vs workflows, publish, channels, **queue mode warning**, executions | Мало Docker/env «copy-paste» | Сухой пересказ без чек-листа продакшена |
| 2 | [docs.n8n.io/.../set-up-ai-assistant](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-ai-assistant) | Официальная docs | `N8N_ENABLED_MODULES`, Daytona, `WEBHOOK_URL`, таблица env | Смешивает instance-ai и agents | Путать обязательный минимум (agents) с «full experience» |
| 3 | [blog.n8n.io/introducing-n8n-agents](https://blog.n8n.io/introducing-n8n-agents/) | Официальный анонс (25.09.2026) | Продуктовая логика: один агент в Slack/cron/workflow; billing «one turn = one execution» | Нет queue mode / self-host env | Маркетинг без dual-instance схемы |
| 4 | [www.meta-journal.ru/2026/10/03/nastroyka-n8n-agents-2026](https://www.meta-journal.ru/2026/10/03/nastroyka-n8n-agents-2026/) | RU how-to (окт. 2026) | Standalone agent, Slack, расписание | Не фокус на queue mode + env | Структура 1:1 |
| 5 | [www.maatrix.io/blog/n8n-s-ai-agentami-na-svoem-servere](https://www.maatrix.io/blog/n8n-s-ai-agentami-na-svoem-servere/) | RU explainer | **Agents tab vs AI Agent node** — снимает типичную путаницу | Слабее про queue/workers | Продающий тон без таблицы симптом→fix |
| 6 | [singularitybyte.com/tutorials/n8n-agents-self-hosted-setup.html](https://singularitybyte.com/tutorials/n8n-agents-self-hosted-setup.html) | EN deep-dive | Явно про **queue mode catch**, версии 2.32.3+, Sustainable Use | Не русский SERP | Копировать версионную таблицу без сверки с docs |
| 7 | [qantcore.space/guide/ai-agenty-v-n8n](https://qantcore.space/guide/ai-agenty-v-n8n/) | RU AI Agent node | Multi-agent на canvas, шаблоны | Про **узел AI Agent**, не продукт Agents | Вводить читателя в «не тот продукт» |
| 8 | [joshuaopolko.com/n8n-self-hosted-guide](https://joshuaopolko.com/n8n-self-hosted-guide/) | EN self-host | Docker, scaling, AI | Agents как фича вторым планом | Переносить непроверенные цифры VPS |
| 9 | [docs.n8n.io/.../enable-queue-mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode) | Официальная docs | `EXECUTIONS_MODE=queue`, Redis, workers, Postgres | Не про Agents | Совмещать queue и Agents на одном инстансе |
| 10 | [github.com/n8n-io/n8n/security/advisories/GHSA-h44j-f5r5-ph73](https://github.com/n8n-io/n8n/security/advisories/GHSA-h44j-f5r5-ph73) | Security advisory | Hardening: `N8N_ENABLED_MODULES`, sharing credentials | Не setup-гайд | Паника без «обновитесь ≥2.28.1» |

**Паттерн SERP:** русскоязычный топ смешивает **n8n Agents (вкладка Agents, сент. 2026)** и **AI Agent node** в workflow. Запрос «n8n агенты на своем сервере» часто ведёт в гайды по LangChain-узлу, а не по env-модулю `agents`. Англоязычный слой точнее описывает queue mode limitation.

**Intent:** checklist — админ/DevOps уже поднял self-hosted n8n (часто в **queue mode**) и хочет **включить продукт Agents** без поломки продакшена.

**Пробел для «Ковчег»:** пошаговый **чек-лист env + Docker**, таблица **Agents vs AI Agent node vs workflow**, схема **двух инстансов** (queue для воркфлоу + regular для Agents), smoke-тест каналов, 15 пунктов перед продом.

---

## 2. Яндекс Wordstat (MCP `user-mcp-kv`)

**⚠️ WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` не подключён в Cloud Agent на 06.10.2026. Вызов `wordstat_get_top_requests` невозможен. Точные помесячные показы **не получены** в этом прогоне.

**Экспертная семантика (без цифр спроса):** head «n8n», «n8n docker», «n8n установка»; mid-tail «n8n агенты», «n8n ai»; long-tail «N8N_ENABLED_MODULES», «n8n queue mode», «n8n agents self hosted», «n8n agents docker compose».

**Справочно из карточки B06 / research B02 (не перепроверено Wordstat 06.10.2026):**

| Фраза | Показы/мес (источник) |
|-------|------------------------|
| n8n | 37 115 (B02 research, 11.06.2026) |
| n8n агенты | 699 (B02 research) |
| n8n ai | 720 (B02 research) |
| автоматизация n8n | 539 (B02 research) |
| n8n docker | 498 (B02 research) |
| n8n установка | 364 (B02 research) |

**LSI для writer:** `N8N_ENABLED_MODULES`, `instance-ai`, `N8N_WEBHOOK_URL`, `EXECUTIONS_MODE=queue`, Agents tab, Message an Agent node, publish agent, approvals, Daytona sandbox, Telegram/Slack channel, dual instance, regular mode.

**SEO-стратегия:** primary «n8n агенты на своем сервере» + disambiguation в lead; secondary env-запросы в H2/H3 и FAQ.

---

## 3. Таблица фактов (цифры и версии только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Продукт **n8n Agents** — автономные агенты рядом с workflow; reasoning loop, tools, publish, sessions | [docs: build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents) | 06.10.2026 | да |
| Self-hosted Agents: **n8n ≥ 2.32.3** (Beta floor в docs enable path) | [docs: set-up-ai-assistant](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-ai-assistant) | 06.10.2026 | да |
| Минимум для ручной сборки: добавить **`agents` в `N8N_ENABLED_MODULES`** | [docs: set-up-ai-assistant](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-ai-assistant) | 06.10.2026 | да |
| Опционально: `N8N_ENABLED_MODULES=instance-ai,agents` для AI-assisted building | [docs: set-up-ai-assistant](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-ai-assistant) | 06.10.2026 | да |
| Knowledge base на self-hosted: **`N8N_AGENTS_AI_SANDBOX_ENABLED=true`**, provider **`daytona`** | [docs: set-up-ai-assistant](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-ai-assistant) | 06.10.2026 | да |
| Каналы (Slack, Telegram, Linear): нужен публичный URL; в enable-agents блоке — **`WEBHOOK_URL`** | [docs: set-up-ai-assistant](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-ai-assistant) | 06.10.2026 | да |
| За reverse proxy предпочтителен **`N8N_WEBHOOK_URL`**; `WEBHOOK_URL` deprecated | [docs: configure-webhook-urls-with-reverse-proxy](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy) | 06.10.2026 | да |
| **Queue mode не поддерживается для Agents**; каналы (Telegram) могут падать — **regular mode** | [docs: build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents) | 06.10.2026 | да |
| Queue mode: **`EXECUTIONS_MODE=queue`**, Redis, workers, общая Postgres; SQLite не рекомендуется | [docs: enable-queue-mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode) | 06.10.2026 | да |
| Agents в **Preview**; поведение может меняться | [docs: build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents) | 06.10.2026 | да |
| Knowledge base на self-hosted — **Preview**, нужен sandbox | [docs: build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents) | 06.10.2026 | да |
| **One turn = one execution**; агенты делят квоту с workflow | [docs: build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents) | 06.10.2026 | да |
| Анонс Agents: 25.09.2026; агент в Slack, cron, workflow; workflows как tools | [blog.n8n.io/introducing-n8n-agents](https://blog.n8n.io/introducing-n8n-agents/) | 06.10.2026 | да |
| **Message an Agent** node вызывает опубликованного агента из workflow | [docs: build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents) | 06.10.2026 | да |
| AI Agent **workflow node** не равен продукту Agents (Settings > Agents / Agents tab) | [docs: build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents) + SERP MAATRIX | 06.10.2026 | да |
| CVE-2026-59207 / GHSA-h44j-f5r5-ph73: bypass Allowed HTTP Request Domains через Agents MCP; fix **≥2.28.1** (и 2.27.4) | [GitHub Advisory](https://github.com/n8n-io/n8n/security/advisories/GHSA-h44j-f5r5-ph73) | 06.10.2026 | да |
| Mitigation: убрать `agents` из `N8N_ENABLED_MODULES`, ограничить sharing credentials | [GitHub Advisory](https://github.com/n8n-io/n8n/security/advisories/GHSA-h44j-f5r5-ph73) | 06.10.2026 | да |
| Self-hosted: instance owner может **Enable Agents** в Settings > Agents (отдельно от Assistant) | [docs: build-and-manage-agents](https://docs.n8n.io/build/build-and-manage-agents) | 06.10.2026 | да |
| Docker Compose — официальный путь деплоя self-hosted | [docs: install-using-docker-compose](https://docs.n8n.io/deploy/host-n8n/install-options/install-using-docker-compose) | 06.10.2026 | да |
| Переход на self-hosted n8n может снизить накладные на медиа и поднять маржу контент-производства до **35%** (контекст ROI, не setup) | [fact-bank / mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 06.10.2026 | да (осторожно, не ядро статьи) |

**Не использовать без первичника:** «2.41.5 current stable» (SingularityByte); «40% приложений с ИИ-агентами» (home-hosted.ru SERP); любые «минимальные VPS $X» из EN-блогов.

**Writer note (docs drift):** в markdown docs от 2026 также указано «Agents on by default» на self-hosted ≥2.32.3 через Settings > Agents. Если вкладки нет — fallback на `N8N_ENABLED_MODULES=agents` по enable-agents.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** читатель с **production self-hosted n8n** (часто queue mode) получает **рабочий Agents** через: проверку версии, env/Docker, **regular-mode инстанс** (или второй контейнер), публичный webhook URL, publish + approvals, smoke-тест канала.

**Отличие от SERP:**
- Явное **разведение Agents vs AI Agent node**.
- Не «установите n8n с нуля», а **миграция/добавление модуля** и **обход queue**.
- Таблица **симптом → env/режим → fix** + чек-лист 15 пунктов (из карточки).

**Tone:** для админа/техлида, который уже автоматизирует на n8n; без новостного хайпа про релиз.

**H2-каркас (карточка B06):**
1. Agents vs AI Agent node vs workflow  
2. Минимальный self-host: ≥2.32.3, `N8N_ENABLED_MODULES`, regular mode  
3. Двухинстансная схема: queue + Agents  
4. Docker Compose env, `N8N_WEBHOOK_URL`, опционально Daytona  
5. Publish, approvals, smoke Slack/Telegram  
6. Чек-лист 15 пунктов + таблица troubleshooting  

**Internal links (карточка):** `/ustanovka-n8n-docker-vps/`, `/nastroyka-n8n-agents-2026/`, `/avtomatizaciya-n8n-ai-agents/`

---

## 5. FAQ-кандидаты (6)

1. **Поддерживает ли n8n Agents queue mode?** — Нет (официальное предупреждение docs); держите Agents на regular mode или отдельном инстансе.
2. **Что писать в `N8N_ENABLED_MODULES`?** — Минимум `agents`; при AI-assisted builder — `instance-ai,agents`; отключение — убрать `agents` или Settings > Agents off.
3. **Можно ли Agents и queue workflows на одном сервере?** — На одном **процессе** в queue mode Agents не поддерживаются; паттерн — **два инстанса** (или один regular, если нагрузка позволяет без queue).
4. **Нужен ли `WEBHOOK_URL` / `N8N_WEBHOOK_URL` для Telegram?** — Да для внешних каналов; за reverse proxy — `N8N_WEBHOOK_URL` + `N8N_PROXY_HOPS=1`.
5. **Чем Agents отличаются от AI Agent node?** — Agents: отдельный артеfact, publish, channels, schedules; node — агент внутри одного workflow.
6. **Сколько стоит run агента на self-hosted?** — Лицензия CE без per-execution cap; платите infra + LLM API; один turn = one execution в учёте n8n.

---

## 6. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «n8n Agents на self-hosted» 40–60 слов | Lead | disambiguation от AI Agent node |
| Таблица Agents vs node vs workflow | H2-1 | 3 колонки |
| ASCII/Timeline схема dual instance | H2-3 | queue workers → DB; agents regular → same/different DB |
| Чек-лист 15 пунктов | H2-6 | markdown checklist |
| FAQ 6 | Конец | ответы-действия |
| Island test | QA | каждый H2 = env/режим + рекомендация |

**Целевые формулировки:** «n8n агенты на своем сервере», «N8N_ENABLED_MODULES agents», «n8n queue mode agents», «n8n agents docker compose».

---

## 7. Риски для writer

- Не обещать Agents в **queue mode** на одном инстансе — противоречит docs.
- Не путать **`WEBHOOK_URL`** (enable-agents doc) и **`N8N_WEBHOOK_URL`** (reverse proxy) — показать оба с контекстом.
- Версию n8n указывать как **≥2.32.3** + «обновитесь до актуального stable перед продом» без выдуманного номера patch.
- Security: при упоминании GHSA — **patch ≥2.28.1** и approvals на write-tools.
- Без эмодзи; utility gate статьи: **5+ шагов** и **чек-лист 10+** (цель 15).
- Wordstat: не писать «699 показов» как свежие без пометки «B02, не перепроверено 06.10.2026».

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель проверит версию и режим инстанса, включит модуль Agents через env/Docker на **regular mode** (или поднимет второй инстанс рядом с queue production), настроит публичный webhook URL, опубликует агента с approvals, протестирует канал и пройдёт 15-пунктовый чек-лист перед продакшеном.

**action_outline (для writer):**

1. **Inventory:** версия n8n (≥2.32.3), `EXECUTIONS_MODE` (queue или regular), есть ли Redis/workers, текущий `N8N_ENABLED_MODULES`.
2. **Disambiguation:** убедиться, что нужен продукт **Agents tab**, не только AI Agent node в workflow.
3. **Решение по топологии:** если queue mode — спланировать **второй инстанс** Agents без `EXECUTIONS_MODE=queue`; если single small host — временно regular mode (осознанный trade-off).
4. **Env:** добавить `agents` (и опционально `instance-ai`) в `N8N_ENABLED_MODULES`; задать `N8N_WEBHOOK_URL` (или `WEBHOOK_URL` по enable doc) для каналов.
5. **Docker Compose:** продублировать env в `environment:` / `.env`, перезапуск контейнера, проверить вкладку Agents / Settings > Agents.
6. **Optional:** Daytona для knowledge base (`N8N_AGENTS_AI_SANDBOX_*`); иначе агент без KB, но рабочий.
7. **Build & publish:** Create Agent → model + instructions + tools/workflows → Preview → Publish; включить **approve** на опасные tools.
8. **Smoke-test:** chat в UI → подключить Telegram или Slack → проверить session log; из workflow — Message an Agent node.
9. **Hardening:** patch ≥2.28.1 (GHSA), audit shared credentials, финальный чек-лист 15 пунктов + таблица симптом→fix.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (10) |
| Wordstat MCP | ❌ недоступен (зафиксировано) |
| Таблица фактов с URL | ✅ (19 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ (6) |
| GEO hooks | ✅ |

**next_step:** excalibur-blog-writer → `article.html` по action_outline и h2_outline карточки B06.
