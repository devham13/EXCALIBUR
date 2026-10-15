# Research notes — B06 «Как настроить environment.json для Cursor Cloud Agents: пошаговая инструкция с Builds»

**topic_id:** B06  
**slug:** cursor-environment-json-cloud-agents  
**article_mode:** B (how-to)  
**research_date:** 2026-10-07  
**disclaimer:** Все даты, версии и статистика проверены на 07.10.2026.

---

## 1. SERP-обзор (WebSearch Cursor, 07.10.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | Официальная docs | Канон: resolution order, agent-led vs Dockerfile, install/start/terminals, secrets, path rules | EN; длинная; Automations не в фокусе | Перевод без русского чек-листа и типичных ошибок COPY |
| 2 | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | Официальная docs | Жизненный цикл Build, 4 триггера, install vs start, stale builds, debug | Мало «первый раз за 45 мин» | Сухой справочник без workflow |
| 3 | [learncursor.dev/.../cloud-agent-environment-json](https://www.learncursor.dev/learn/cursor-agents/cloud-agent-environment-json) | Сторонний reference EN | Поля schema, install в Build, branch-testing | Не официальный источник для SLA | Копировать как «официальную правду» |
| 4 | [learncursor.dev/.../cloud-agent-builds](https://www.learncursor.dev/learn/cursor-agents/cloud-agent-builds) | Сторонний EN | Fallback на last good Build | Дубли docs | 1:1 структура |
| 5 | [meta-journal.ru/.../nastroyka-cursor-cloud-agents-2026](https://www.meta-journal.ru/2026/09/13/nastroyka-cursor-cloud-agents-2026/) | RU how-to | environment.json в title | Смешивает Automations и environment | Увод в automation-триггеры вместо config-as-code |
| 6 | [forum.cursor.com/.../environment-json-deprecated](https://forum.cursor.com/t/has-environment-json-been-deprecated/153410) | Community + staff | Подтверждение: не deprecated; порядок приоритетов; snapshot ID из dashboard | Фрагментарно | Длинные треды без action steps |
| 7 | [cursor.com/changelog/cloud-in-agents-window](https://cursor.com/changelog/cloud-in-agents-window) | Changelog | Agent-led setup <10 мин, snapshot → environment.json | News-формат | Новость без чек-листа |
| 8 | [prod.cursor.com/docs/cloud-agent/settings](https://prod.cursor.com/docs/cloud-agent/settings) | Docs (settings) | Environments view, Builds tab, Update with Agent | Admin-угол | Enterprise-only детали без пояснения для solo |

**Паттерн SERP:** в топе доминируют **официальные** setup + builds; русскоязычные материалы чаще про Automations или «обзор Cloud Agents», а не про **config-as-code** и разделение **install / start / terminals**. Запрос «настройка cursor cloud agent» закрывается обобщёнными гайдами — пробел для пошагового **environment.json + Builds + verify**.

**Intent:** how_to — читатель хочет **закрепить окружение в репозитории**, дождаться **зелёного Build**, понять **что в install, что в start**, и запустить **тестовый Cloud Agent** без поломки команды.

**Пробел для «Ковчег»:** один русский workflow **45–60 мин**: wizard или Dockerfile → commit `.cursor/environment.json` → Trigger build → логи → test agent на ветке → чек-лист перед Automations; акцент на типичные ошибки (COPY всего репо, Docker в install вместо start, secrets только в dashboard).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

**⚠️ WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` и инструмент `wordstat_get_top_requests` **не подключены** в среде Cloud Agent (в каталоге dynamic tools доступны только Cursor Automation Tools, cursor, cursor-cloud, cursor-subscriptions). Точные показы в месяц **не получены** — в тексте статьи **не выдумывать** цифры спроса.

**Семантика (экспертная оценка без объёмов, для writer):**

- Ядро: настройка cursor cloud agent, cursor environment json, cloud agent builds  
- EN-хвост (часто в docs/SERP): `.cursor/environment.json`, install script, Dockerfile cloud agent  
- LSI: snapshot id, trigger build, install vs start, self-hosted machines (ограничение: без environment.json)  
- Связка с B03: MCP allowlist в environment.json (`mcpServerAllowlist`, `disableAllMcpServers`)

При появлении Wordstat на следующем прогоне — дополнить таблицу «Фраза | Показы/мес» и уточнить H2 под топ-3 фразы.

---

## 3. Таблица фактов (цифры и утверждения только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Cloud agents работают на **изолированных Ubuntu-машинах** с клонированными репо, зависимостями, secrets и сетью | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |
| Два пути настройки: **agent-led** из dashboard или **Dockerfile** через `.cursor/environment.json` | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |
| Порядок resolution (первое совпадение): **1)** `.cursor/environment.json` в репо **2)** personal saved **3)** team saved | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |
| **Self-Hosted Machines:** используют только repos окружения, **не читают** `.cursor/environment.json` | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |
| Agent-led setup: Cursor заявляет настройку dev environment **менее чем за 10 минут** (dashboard или Agents Window) | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |
| В Dockerfile **не копировать** весь проект — workspace и checkout commit управляет Cursor | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |
| Пути `build.dockerfile` и `build.context` **относительно `.cursor/`**; `.`, `./`, `..` означают **корень репозитория** | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |
| Команда **`install`** выполняется **при каждом Build** из **корня проекта**; раньше называлась update script | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |
| **`install` должен быть идемпотентным** — может повторяться на уже подготовленном диске | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |
| Build сохраняет **только disk state**; процессы, shell exports и in-memory caches **не переносятся** в snapshot | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 07.10.2026 | да |
| **`start`** и **`terminals`** выполняются **в начале каждого agent run** (после boot с Build) | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 07.10.2026 | да |
| **`terminals`** — процессы приложения в **tmux**, общие с агентом | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |
| Пример `start` для Docker: `sudo service docker start` | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |
| Build lifecycle: Trigger → Prepare (clone + `install`) → Snapshot → Activate → Start agents | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 07.10.2026 | да |
| **4 триггера Build:** Recurring, Configuration change, Manual, Agent-requested | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 07.10.2026 | да |
| Recurring Build **пропускается (Skipped)**, если нет новых коммитов на default branch и нет изменений config/secrets | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 07.10.2026 | да |
| При **failed Build** агенты продолжают стартовать с **последнего успешного active Build** | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 07.10.2026 | да |
| **Builds только для Cursor-hosted** Cloud Agents; Self-Hosted **never boot a Build** | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 07.10.2026 | да |
| **User secrets** добавляются при старте агента; **недоступны во время Build** и не попадают в shared snapshot | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 07.10.2026 | да |
| **Update stale builds:** порог по умолчанию **24 часа**; `0` = всегда pull latest на default branch при старте | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 07.10.2026 | да |
| Feature branch: агент стартует с active Build, затем **checkout запрошенной ветки**; исходник = ветка, deps = из Build | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 07.10.2026 | да |
| **Builds included** with Cloud Agents — **без отдельной платы** (по docs) | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 07.10.2026 | да |
| Snapshot или Dockerfile задаёт **base machine**; Cursor затем clone + `install` + новый bootable snapshot | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 07.10.2026 | да |
| `environment.json` **не deprecated**; staff: repo config **выше** personal/team wizard | [forum.cursor.com/t/has-environment-json-been-deprecated/153410](https://forum.cursor.com/t/has-environment-json-been-deprecated/153410) | 07.10.2026 | да (community + staff) |
| Snapshot ID можно взять в **Cloud Agents dashboard** (после Save environment) | [forum.cursor.com/t/has-environment-json-been-deprecated/153410](https://forum.cursor.com/t/has-environment-json-been-deprecated/153410) | 07.10.2026 | да |
| JSON Schema: `https://cursor.com/schemas/environment.schema.json`; unknown properties **reject** | [cursor.com/schemas/environment.schema.json](https://cursor.com/schemas/environment.schema.json) | 07.10.2026 | да |
| В schema: `snapshot` **имеет приоритет** над `build` и `image` при задании base | [cursor.com/schemas/environment.schema.json](https://cursor.com/schemas/environment.schema.json) | 07.10.2026 | да |
| `mcpServerAllowlist`, `disableAllMcpServers`, `egressAllowlist`, `egressMode` — поля environment.json | [cursor.com/schemas/environment.schema.json](https://cursor.com/schemas/environment.schema.json) | 07.10.2026 | да |
| Environments dashboard: install script для Builds, runtime/build secrets, **Builds tab** (trigger, pin, start agent from Build) | [prod.cursor.com/docs/cloud-agent/settings](https://prod.cursor.com/docs/cloud-agent/settings) | 07.10.2026 | да |
| Multi-repo environment: несколько репо в одном окружении; agent может менять несколько PR | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |
| Dockerfile builds используют **layer caching** при изменении Dockerfile | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 07.10.2026 | да |

**fact-bank.md:** записей по Cursor Cloud Agents / environment.json **нет** — факты только из таблицы выше.

**Не использовать без оговорки:** цифры «до 3× быстрее» из новостных сайтов (vibecoding.ru) — не в официальных docs; «Cursor 3.4» multi-repo — полезный контекст, но даты фич уточнять по changelog, не выдумывать версии IDE.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **45–60 минут** пройти цикл **environment.json → успешный Build → test Cloud Agent на feature branch**, понимая **install (Build)** vs **start/terminals (каждый run)** и не ломая команде active Build failed-конфигом.

**Почему отличается от конкурентов:**

- Официальные docs — канон, но без единого русского «полевого» чек-листа.  
- RU-материалы уводят в Automations, а не в **config-as-code**.  
- Learn Cursor — хороший EN reference, но не приоритет для GEO QA fact-check.  
- «Ковчег»: практик автоматизации, связка с **B03 (MCP)** через allowlist в environment.json, минимальные secrets.

**Tone:** environment.json = «Docker Compose для облачного агента в Git»; Build = «замороженный диск с зависимостями»; start = «поднять Docker/БД на каждый run».

**H2-каркас (из карточки B06 + research):**

1. Cloud Agent vs локальный Agent: когда нужен `.cursor/environment.json`  
2. Структура файла и приоритет над dashboard  
3. Dockerfile + `install`: что готовить в Build  
4. `start`, `terminals`, `ports`: что на каждый run  
5. Builds: триггеры, логи, failed vs active  
6. Secrets, egress, MCP allowlist  
7. Чек-лист перед production / Automations  

---

## 5. FAQ-кандидаты (из faq_hints + docs)

1. **Чем `install` отличается от `start`?** — install на этапе Build (диск); start/terminals при старте агента (процессы).  
2. **Нужен ли Dockerfile?** — нет, можно snapshot + install или только agent-led wizard; Dockerfile для system deps.  
3. **Как закрепить snapshot в environment.json?** — поле `snapshot` + id из dashboard после Save; commit в `.cursor/environment.json`.  
4. **Почему агент не видит зависимости после Build?** — install не idempotent/упал; смотреть failed Build; agent на ветке с другим lockfile — agent может rerun install.  
5. **Deprecated ли environment.json?** — нет, repo-level wins (forum staff).  
6. **Работает ли файл на Self-Hosted?** — нет, только hosted Cloud Agents.  
7. **Где user secrets vs build secrets?** — build secrets в install; user secrets только при agent start.

---

## 6. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение environment.json 40–60 слов | Lead | config-as-code для Cloud Agent VM |
| Таблица install / start / terminals | H2-4 | When / Use it for (из docs builds) |
| Пример минимального JSON (snapshot + install) | H2-2 | Блок кода + пояснение путей |
| Workflow | H2-3–5 | wizard или Dockerfile → commit → Trigger build → test agent |
| FAQ 5–7 | Конец | Ответы-действия |
| Internal link | Тело | [B03 MCP](/podklyuchenie-mcp-cursor/) для mcpServerAllowlist |

**Целевые формулировки:** «настройка cursor cloud agent», «cursor environment json», «cloud agent builds», «install start cursor agent».

---

## 7. Риски для writer

- Команды install (`npm`/`pnpm`/`pip`) — **из реального репо читателя**, в статье — шаблоны + «подставьте свой менеджер пакетов».  
- Не дублировать meta-journal automation-гайд.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Min **5** нумерованных шагов + чеклист **10+** пунктов.  
- Секреты — только dashboard/Secrets tab, не в JSON.  
- Ссылаться на [environment.schema.json](https://cursor.com/schemas/environment.schema.json) для полей, не выдумывать `startup`.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст или обновит `.cursor/environment.json`, разделит команды между **install** (Build) и **start/terminals** (run), дождётся **успешного active Build**, проверит логи при сбое, запустит **тестовый Cloud Agent с feature branch** и пройдёт чек-лист перед production/Automations.

**action_outline (для writer):**

1. **Подключить GitHub** (read/write для репо) и открыть **Cloud Agents dashboard** или Agents Window → guided setup (или сразу создать `.cursor/` в репо).  
2. **Выбрать базу:** agent-led snapshot **или** `build.dockerfile` (+ `context: ".."` при deps из корня); **не** `COPY` всего проекта в Dockerfile.  
3. **Написать `.cursor/environment.json`:** минимум `install`; при Docker/БД — `start`; при dev-сервере — `terminals` + опционально `ports`.  
4. **Secrets:** runtime/build secrets в dashboard (не в JSON); понимать, что **user secrets не в Build**.  
5. **Commit + push** на ветку; для feature-теста — agent **from branch** (config читается с commit старта).  
6. **Builds tab → Trigger build** (или дождаться configuration change); дождаться **Success** и **active** Build.  
7. **При Failed:** открыть логи; агенты остаются на **last good Build** — исправить install/Dockerfile, не паниковать.  
8. **Test Cloud Agent:** узкая задача (lint/test); проверить, что `start`/terminals подняли сервисы.  
9. **Чек-лист production:** egress/MCP allowlist, stale builds threshold, merge в default → recurring Build, затем Automations.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен в среде |
| Таблица фактов с URL | ✅ (30 фактов, 8 уникальных доменов-источников) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B06
article_dir: memory/blog/articles/B06-cursor-environment-json-cloud-agents
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 позиций (docs setup/builds, Learn Cursor, meta-journal, forum, changelog, settings). Wordstat: MCP user-mcp-kv недоступен в Cloud Agent — показы не собраны. Угол — 45–60 мин workflow environment.json + Builds + install vs start/terminals + verify test agent. 30 фактов с URL (8 источников). 9 шагов action_outline, 7 FAQ. Готов к writer.
===
