# Research notes — B06 «Как настроить Cursor Cloud Agents: пошаговая инструкция с environment.json и Builds»

**topic_id:** B06  
**slug:** nastroyka-cursor-cloud-agents-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-09-13  
**disclaimer:** Все даты, версии и статистика проверены на 13.09.2026.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | Официальная docs | Канон: agent-driven setup, Dockerfile, install/start/terminals, Secrets, resolution order | Английский; длинный reference без «первый прогон за 30 мин» | Сухой перевод без русского troubleshooting |
| 2 | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | Официальная docs | Жизненный цикл Build, install vs start vs terminals, secrets в Builds | Мало примеров JSON для monorepo | Копировать таблицы 1:1 без пояснения «что делать» |
| 3 | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | Официальная overview | Точки запуска (Desktop/Web/Slack/GitHub), billing, troubleshooting secrets | Обзор без пошагового first run | News-формат «что такое cloud agents» |
| 4 | [learncursor.dev/.../cloud-agent-environment-json](https://www.learncursor.dev/learn/cursor-agents/cloud-agent-environment-json) | EN reference (авг. 2026) | 10 полей schema, gotchas (paths, snapshot, no secrets in JSON) | Не про GitHub admin flow и spend limit | Структуру 1:1 |
| 5 | [learncursor.dev/.../cloud-agent-setup](https://www.learncursor.dev/learn/cursor-agents/cloud-agent-setup) | EN how-to | Environment + repo + first run | Без Builds-миграции и `start: "true"` workaround | Коммерческий bias Learn Cursor |
| 6 | [shtruzel.ru/.../cursor-agent-mode-kak-ispolzovat-2026](https://shtruzel.ru/articles/cursor-agent-mode-kak-ispolzovat-2026) | RU обзор 2026 | Subagents, self-hosted pools, контекст Agent Mode | Мало environment.json и Builds | Смешивать cloud setup с subagents как главный угол |
| 7 | [webedge.dev/ru/blog/cursor-cloud-agents-development-workflow-2026](https://webedge.dev/ru/blog/cursor-cloud-agents-development-workflow-2026/) | RU workflow | Dev workflow, PR из облака | Нет config-as-code и Builds tab | Trend-пост без чеклиста |
| 8 | [buildfastwithai.com/.../cursor-cloud-agents-development-environments-2026](https://www.buildfastwithai.com/blogs/cursor-cloud-agents-development-environments-2026) | EN longread | Pricing breakdown, comparison vs Codex/Copilot | Цены могут устареть; EN | Таблицу цен конкурентов без проверки на docs |

**Паттерн SERP:** топ — официальные docs Cursor (setup, builds, cloud-agent) + англоязычные reference-гайды (Learn Cursor, Steve Kinney) + русские обзоры workflow/subagents. Отдельного **русского how-to** «настройка cursor cloud agents + environment.json + Builds» в топе почти нет — пробел для практического гайда.

**Intent:** how_to — читатель хочет **подключить репозиторий, создать окружение, пройти первый Build, закоммитить `.cursor/environment.json` и запустить cloud agent с PR**. Вторичный intent: secrets, GitHub, отличие от локального агента, починка failed Build.

**SERP gaps (наша дифференциация):**
- Русский пошаговый first run: dashboard → GitHub → Secrets → agent-driven setup → commit environment.json → Enable Builds → test agent → PR.
- Таблица **install / start / terminals** с реальным JSON (monorepo + `start: "true"` workaround из forum).
- Troubleshooting: failed Build не ломает fleet; snapshot ID блокирует Dockerfile; secrets только при **новом** agent run; My Machines ≠ local mcp.json.
- Связка с внутренними статьями: B03 (MCP в dashboard для cloud), B05 rules (AGENTS.md cloud section).

---

## 2. Яндекс Wordstat

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` / инструмент `wordstat_get_top_requests` недоступен в текущей Cloud-сессии (namespace не подключён). Точные объёмы спроса **не получены** — цифры ниже **не использовать в тексте статьи**.

### Fallback: семантика по SERP + secondary queries (экспертная оценка, без показов)

| Кластер | Фразы для writer | Примечание |
|---------|------------------|------------|
| Primary | настройка cursor cloud agents | H1, lead |
| EN-кластер | cursor cloud agents setup, cursor background agents | Background Agents = старое имя (см. docs) |
| Config-as-code | cursor environment.json, cursor environment.json настройка | H2 про `.cursor/environment.json` |
| GitHub | cursor cloud agents github | H2 про подключение SCM |
| Secrets | cloud agents cursor secrets, cursor cloud agents secrets tab | H2 troubleshooting |
| Builds | cursor cloud agent builds, cursor builds environment | H2 Builds tab |
| RU long-tail | как настроить cursor cloud agents, облачные агенты cursor | FAQ |

**LSI для writer (SERP + docs, без выдуманных частотностей):**
- cloud agents / background agents (legacy name)
- environment.json, install, start, terminals, ports, build.dockerfile
- Builds tab, Trigger build, Enable Builds, active Build, failed Build
- snapshot ID, agent-driven setup, Cloud Agents dashboard
- Secrets tab, build secrets vs user secrets, spend limit
- GitHub read-write, multi-repo environment, repositoryDependencies
- AGENTS.md «Cursor Cloud specific instructions»
- Privacy Mode, team follow-ups, API pricing

**SEO-стратегия:** primary «настройка cursor cloud agents» в H1/lead; secondary «cursor environment.json настройка», «cursor cloud agents github», «cloud agents cursor secrets» — в H2 и FAQ. EN-термины (Cloud Agents, Builds) — с русской расшифровкой в первом упоминании.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Cloud Agents (ранее Background Agents) работают в изолированных Ubuntu VM с полным dev-окружением | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 13.09.2026 | да |
| Перед запуском cloud agent admin аккаунта должен подключить GitHub, GitLab, Bitbucket Cloud или Azure DevOps | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 13.09.2026 | да |
| Cloud agent клонирует repo, работает в отдельной ветке и пушит изменения для handoff (PR) | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 13.09.2026 | да |
| Запуск: Cursor Desktop (Cloud в dropdown), cursor.com/agents, Slack @cursor, GitHub/Bitbucket @cursor, Linear, API | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 13.09.2026 | да |
| Cloud Agents доступны на **всех платных** планах Cursor; нужен paid plan | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 13.09.2026 | да |
| Cloud Agents тарифицируются по **API pricing** выбранной модели; при первом запуске просят **spend limit** | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 13.09.2026 | да |
| Pro ($20/mo), Pro Plus ($60/mo), Ultra ($200/mo) включают доступ к Cloud Agents | [cursor.com/docs/models-and-pricing](https://cursor.com/docs/models-and-pricing) | 13.09.2026 | да |
| Agent-driven setup: Cursor может настроить cloud dev environment **менее чем за 10 минут** | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 13.09.2026 | да |
| Порядок resolution: 1) `.cursor/environment.json` в repo → 2) personal saved environment → 3) team saved environment | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 13.09.2026 | да |
| `install` выполняется **во время Build**; `start` и `terminals` — **при старте agent run** | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 13.09.2026 | да |
| `install` должен быть **idempotent** — может повторяться на prepared disk state | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 13.09.2026 | да |
| Builds сохраняют **disk state only**; процессы и in-memory caches не переносятся в snapshot | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 13.09.2026 | да |
| Failed Build **не заменяет** active Build; agents продолжают с последнего успешного | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 13.09.2026 | да |
| Новые environments используют Builds **по умолчанию** | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 13.09.2026 | да |
| Builds **не стоят дополнительно** (included with Cloud Agents) | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 13.09.2026 | да |
| По умолчанию recurring Build — **каждый час**; agents boot up to **3x faster** с Builds | [cursor.com/blog/builds](https://cursor.com/blog/builds) | 13.08.2026 | да |
| С **17 августа 2026** все new и existing environments используют builds by default | [cursor.com/blog/builds](https://cursor.com/blog/builds) | 13.08.2026 | да |
| `build.dockerfile` и `build.context` — paths **relative to `.cursor`**; `install` runs from **project root** | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 13.09.2026 | да |
| В Dockerfile **не COPY** весь project — Cursor checkout commit сам | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 13.09.2026 | да |
| Schema: **10 top-level fields**; unknown properties **rejected** (typo `startup` fails) | [cursor.com/schemas/environment.schema.json](https://www.cursor.com/schemas/environment.schema.json) | 13.09.2026 | да |
| В schema **нет поля secrets** — credentials только через Secrets tab dashboard | [learncursor.dev/.../cloud-agent-environment-json](https://www.learncursor.dev/learn/cursor-agents/cloud-agent-environment-json) | 14.08.2026 | да |
| Team/environment secrets доступны **во время Build**; user secrets — **только при старте agent** | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 13.09.2026 | да |
| Secrets inject **when agent starts**; running agents **не подхватят** новые secrets | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 13.09.2026 | да |
| `terminals` run in shared **tmux** session; `description` показывается agent | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 13.09.2026 | да |
| Workaround (forum, Cursor staff): без поля `start` terminals из environment.json **не запускаются** — добавить `"start": "true"` | [forum.cursor.com/t/.../168876](https://forum.cursor.com/t/cloud-agent-does-not-auto-start-terminals-from-repo-managed-environment-json-builds-enabled/168876) | 19.08.2026 | да (community + staff fix) |
| `start` command — **detached**, не блокирует agent; blocking setup → `install` | [forum.cursor.com/t/cloud-agent-start-script-not-blocking/158583](https://forum.cursor.com/t/cloud-agent-start-script-not-blocking/158583) | 2026 | да (forum, aligned with docs) |
| Snapshot ID в environment.json **берёт precedence** над Dockerfile build | [environment.schema.json](https://www.cursor.com/schemas/environment.schema.json) | 13.09.2026 | да |
| Staleness threshold default **24 hours** для Update stale builds | [cursor.com/docs/cloud-agent/builds](https://cursor.com/docs/cloud-agent/builds) | 13.09.2026 | да |
| Cloud Agents support MCP via dashboard dropdown; Team MCP в Integrations | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | 13.09.2026 | да |
| My Machines workers **не читают** local `~/.cursor/mcp.json` — MCP только из dashboard | [forum.cursor.com/t/.../160956](https://forum.cursor.com/t/my-machines-cloud-agent-worker-does-not-load-mcp-servers-from-the-host-s-local-cursor-mcp-config/160956) | 2026 | да (expected behavior per staff) |
| Рекомендация docs: секция **«Cursor Cloud specific instructions»** в AGENTS.md | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 13.09.2026 | да |
| AWS IAM: secret `CURSOR_AWS_ASSUME_IAM_ROLE_ARN`; STS credentials expire **1 hour** | [cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup) | 13.09.2026 | да |
| Computer use — **Enterprise only** (team feature setting) | [cursor.com/docs/cloud-agent/settings](https://cursor.com/docs/cloud-agent/settings) | 13.09.2026 | да |
| Team follow-ups: риск lateral movement через чужие secrets (admin toggle) | [cursor.com/docs/cloud-agent/settings](https://cursor.com/docs/cloud-agent/settings) | 13.09.2026 | да |

**fact-bank.md:** нет фактов по Cursor Cloud Agents — все цифры только из таблицы выше.

**Не использовать без оговорки:** точные показы Wordstat; цены конкурентов из buildfastwithai; «Cloud Agents бесплатны» — только API usage + paid plan.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **30–60 минут** пройти полный цикл: подключить GitHub → создать environment (agent-driven или Dockerfile) → добавить Secrets → дождаться **успешного Build** → закоммитить `.cursor/environment.json` → запустить первый cloud agent → получить PR с артефактами.

**Почему отличается от конкурентов:**
- Официальная docs — канон, но без русского «first PR из облака» и таблицы install/start/terminals.
- EN reference (Learn Cursor) — field-by-field, без admin flow и spend limit.
- RU обзоры (shtruzel, webedge) — Agent Mode/subagents, не environment.json + Builds.
- «Ковчег»: config-as-code + Builds tab + troubleshooting (failed Build, snapshot trap, `start: "true"`), язык для тимлида/автоматизатора.

**Tone:** Cloud Agent = «удалённый разработчик в VM»; Build = «готовый ноутбук с уже установленными deps»; environment.json = «Docker Compose для агента». Без hype «AI заменит команду».

**H2-каркас (из карточки B06 + research):**
1. Cloud Agents vs локальный агент: когда делегировать в облако  
2. GitHub/GitLab, paid plan, spend limit, Privacy Mode  
3. Agent-driven setup: dashboard, snapshot, первый Build  
4. Config-as-code: `.cursor/environment.json` — install, start, terminals, ports  
5. Builds и Dockerfile: idempotent install, Enable Builds, recurring/skipped  
6. Secrets, env vars, MCP в dashboard  
7. Troubleshooting: failed Build, snapshot vs Dockerfile, secrets, terminals  
8. FAQ + чеклист перед production agent  

**Conversion (conversion-map.md):**
- CTA Make/kv-ai — max 2× если уместно («cloud agent готовит PR → Make деплоит/публикует»)  
- Internal: [B03 MCP](/podklyuchenie-mcp-cursor/), [B05 rules](/nastroyka-cursor-rules-mdc/)  
- Official docs links — primary trust  

---

## 5. Пример environment.json (черновик для writer)

```json
{
  "name": "my-app-cloud",
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  },
  "install": "pnpm install",
  "start": "true",
  "terminals": [
    {
      "name": "dev",
      "command": "pnpm dev",
      "description": "Next.js dev server on port 3000"
    }
  ],
  "ports": [{ "name": "web", "port": 3000 }]
}
```

**Writer notes:** `"start": "true"` — workaround для terminals (forum 168876). Для Docker-heavy repos: `start`: `sudo service docker start`. Secrets — **не** в JSON.

---

## 6. FAQ-кандидаты (7)

1. **Чем Cloud Agents отличаются от локального Agent в Cursor?** — VM в облаке, parallel runs, PR/artifacts без локальной машины; локальный — instant feedback на вашем ПК.  
2. **Чем Cloud Agents отличаются от Cursor Automations?** — Agents = разовая/сессионная задача с PR; Automations = триггеры (cron, GitHub, Slack) на cursor.com/automations.  
3. **Что писать в `.cursor/environment.json`?** — base (`build`/`snapshot`), `install` для Build, `start`/`terminals`/`ports` для runtime; schema на cursor.com/schemas/environment.schema.json.  
4. **Нужен ли платный план?** — да, все paid plans; Hobby не подходит; usage по API pricing модели + spend limit.  
5. **Почему Build красный / failed?** — смотреть Builds tab logs; active Build не меняется; fix config → Trigger build → дождаться Success.  
6. **Почему agent не видит secrets?** — добавить в dashboard Secrets; **запустить новый** agent (не running session); team vs user vs environment-scoped.  
7. **Почему не стартуют terminals из environment.json?** — добавить `"start": "true"` (или реальную start-команду); проверить tmux logs в agent run.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Cloud Agents 40–60 слов | Lead после H1 | «Cloud Agents в Cursor — …» |
| Таблица install / start / terminals | H2-4–5 | Когда / команда / пример |
| Workflow diagram | H2-3–6 | GitHub → Environment → Build → Agent → PR |
| Пример environment.json | H2-4 | JSON + пояснение полей |
| Troubleshooting table | H2-7 | Симптом → действие |
| FAQ 7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «настройка cursor cloud agents», «cursor environment.json», «cursor cloud agents github», «cloud agents cursor secrets», «cursor builds».

---

## 8. Риски для writer

- Не выдумывать показы Wordstat — секция 2 без цифр.  
- Не писать secrets в environment.json примеры.  
- Snapshot ID: предупредить, что блокирует Dockerfile rebuild.  
- Background Agents = legacy name — упомянуть один раз.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Min **5** нумерованных шагов + чеклист **10+** пунктов.  
- Builds даты: «с 17.08.2026 by default» — из blog, не выдумывать новые даты.  
- Forum facts — помечать как «по ответу команды Cursor на форуме», не как SLA.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель подключит GitHub в Cloud Agents dashboard, создаст environment (agent-driven или через `.cursor/environment.json`), добавит Secrets, дождётся успешного Build, запустит cloud agent из Desktop или cursor.com/agents и получит PR с проверенным окружением; при failed Build или неработающих terminals сможет диагностировать проблему по Builds tab и logs.

**action_outline (для writer):**

1. **Проверить prerequisites:** paid Cursor plan, admin подключил GitHub/GitLab с read-write к repo, spend limit настроен.  
2. **Открыть** [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#environments) → **New environment** → выбрать repo (или multi-repo).  
3. **Agent-driven setup (рекомендуется):** Run setup agent → указать secrets для install → дождаться verification и **первого успешного Build** → Save snapshot / commit `.cursor/environment.json`.  
4. **Или manual:** создать `.cursor/Dockerfile` + `.cursor/environment.json` с `build`, `install`; push в repo; Trigger build в Builds tab.  
5. **Разделить команды:** dependency work → `install`; Docker daemon / long services → `start`; dev servers → `terminals` + `ports`; добавить `"start": "true"` если есть terminals без start.  
6. **Secrets:** dashboard Secrets tab (не в JSON); build secrets для private registry в install; после добавления secret — **новый** agent run.  
7. **Enable Builds** (если legacy env): Builds tab → Enable Builds или Run setup agent → Confirm first Build Success.  
8. **Первый agent run:** Desktop → Cloud dropdown **или** cursor.com/agents → prompt с чёткой задачей (fix + test + PR) → дождаться PR и artifacts.  
9. **Troubleshooting:** failed Build — logs + не трогает active; snapshot ID мешает Dockerfile — удалить snapshot field; secrets/MCP — dashboard not local mcp.json.

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

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B06
article_dir: memory/blog/articles/B06-nastroyka-cursor-cloud-agents-2026
status: ✅ PASS
utility_verdict: PASS
wordstat: ⚠️ MCP user-mcp-kv недоступен — семантика из SERP/WebSearch, без цифр спроса
summary: SERP — 8 конкурентов (cursor docs setup/builds, learncursor, shtruzel, webedge, buildfastwithai). Угол — русский how-to: GitHub → environment → Build → environment.json → first cloud agent → PR. 28 фактов с URL, 9 шагов action_outline, 7 FAQ, workaround start:true для terminals. Готов к writer.
===
