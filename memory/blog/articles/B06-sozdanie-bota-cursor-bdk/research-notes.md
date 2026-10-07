# Research notes — B06 «Как создать и задеплоить бота на Cursor BDK: пошаговая инструкция с evals и GitHub-триггером»

**topic_id:** B06  
**slug:** sozdanie-bota-cursor-bdk  
**article_mode:** B (how-to)  
**research_date:** 2026-10-07  
**disclaimer:** Все даты, версии и статистика проверены на 07.10.2026.

---

## 1. SERP-обзор (WebSearch, октябрь 2026)

Запрос **«cursor bdk»** в автоматическом SERP (preflight) сильно зашумлён: WoW «Blood Death Knight», кастомные курсоры, новости про SpaceX/Cursor. Релевантные источники по **Bot Development Kit** находятся по связкам `bot development kit cursor`, `@cursor/bdk`, `bdk init`, H1 статьи. Ниже — **8 осмысленных конкурентов/референсов** после ручного отбора через WebSearch.

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [README @cursor/bdk (npm/jsDelivr)](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/README.md) | Официальный канон BDK | Node 22.13+, `bdk init`, структура `bot/`/`evals/`, таблица BDK vs Automations vs Grok Bot, шаблоны | Английский; нет русского пошагового деплоя | Сухой перевод README без сценария «с нуля до GitHub» |
| 2 | [AGENTS.md @cursor/bdk](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/AGENTS.md) | AX / CLI для агентов | Skills-матрица, GitHub channel, MCP mount, init-поведение | Для coding agents, не для новичка | Копировать CLI-справочник 1:1 вместо гайда |
| 3 | [Changelog: Rollouts and Security Review](https://cursor.com/changelog/rollouts-and-security-reviewer) | Официальный продукт | BDK как движок Rollouts; контекст «зачем BDK существует» | Dashboard-боты Teams/Enterprise, не self-serve BDK-проект | Подменять how-to новостью про Rollouts |
| 4 | [The New Stack: Rollouts + BDK](https://thenewstack.io/cursor-rollouts-firetiger-production/) | Аналитика (24.09.2026) | Объясняет связь Firetiger → Rollouts → `@cursor/bdk` на npm | EN; enterprise-фокус | Длинный M&A-нарратив без шагов |
| 5 | [Cursor Automations docs](https://cursor.com/docs/cloud-agent/automations) | Официальная docs | Когда хватит Automations (prompt + trigger в UI) | Не про код в репозитории | Смешивать Automations и BDK в одну инструкцию |
| 6 | [npm @cursor/july](https://www.npmjs.com/package/@cursor/july) | Пакет / зеркало BDK CLI | Те же README-блоки, версия и дата публикации | Путаница july vs bdk в названии | Выдумывать, что пакеты несвязаны — в README явно «BDK» |
| 7 | [Habr: Telegram-бот в Cursor AI](https://habr.com/ru/articles/874220/) | RU how-to | Популярен в SERP по «бот в Cursor» | **Другой продукт:** IDE + Python/Telegram, не BDK | Выдавать за BDK-гайд |
| 8 | [insidepc: Telegram-бот в Cursor](https://insidepc.tech/ai/ai-guides/sobiraem-telegram-bota-cursor-idei-deploya) | RU гайд | Деплой бота через IDE | Нет `bdk init`, evals, GitHub channel | Структуру «Telegram pet project» как основу B06 |

**Паттерн SERP:** русскоязычный топ по смежным запросам — **Telegram/IDE-боты**, а не **Cursor BDK**. Официальный how-to живёт в npm/README, skills и docs guides на jsDelivr. **Пробел для «Ковчег»:** первый **русский** пошаговый маршрут: scaffold → `bot/instructions.md` + tools/MCP → `bdk eval` → GitHub channel (replay/fixtures) → `bdk deploy` с service account, плюс таблица «BDK vs Automations».

**Intent:** how_to — читатель хочет **репозиторий с агентом**, локальный playground, регрессионные evals и пробуждение от GitHub (или cursor-events), затем деплой на Cursor-managed hosting.

---

## 2. Яндекс Wordstat

⚠️ **WORDSTAT UNAVAILABLE:** MCP-сервер `user-mcp-kv` (`wordstat_get_top_requests`) **не подключён** в среде Cloud Agent (namespace отсутствует в каталоге инструментов). Точные показы/мес **не получены** — не использовать выдуманные цифры спроса.

**Экспертная семантика (без объёмов, для LSI writer):**

| Кластер | Фразы для H2/FAQ |
|---------|------------------|
| Продукт | cursor bdk, bot development kit cursor, @cursor/bdk, bdk init |
| CLI | bdk dev, bdk serve, bdk eval, bdk deploy, bdk validate |
| GitHub | cursor bdk github channel, bdk github replay, github forward |
| Качество | bdk evals, bdk hillclimb, regression ratchet |
| Деплой | как задеплоить bdk агента, CURSOR_SERVICE_ACCOUNT_KEY, cursor-managed hosting |
| Сравнение | bdk vs cursor automations, bdk vs grok bot |

**SEO-стратегия:** primary «cursor bdk» / «bot development kit cursor» в title и lead; secondary — в H2 про GitHub channel, evals, deploy. Не таргетировать «telegram бот cursor» (другой intent, каннибализация с Habr).

---

## 3. Таблица фактов (цифры и утверждения только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| BDK — open-source версия движка Bugbot, Security Review, Approval Bot и Rollouts | [README @cursor/bdk](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/README.md) | 07.10.2026 | да |
| Проект BDK — папка Markdown + TypeScript; агент в `bot/`, evals в корне `evals/` | [README @cursor/bdk](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/README.md) | 07.10.2026 | да |
| Минимум Node **22.13+**; старт: `npm i -g @cursor/bdk` → `bdk init ./my-bot` → `bdk dev` | [README @cursor/bdk](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/README.md) | 07.10.2026 | да |
| Scaffold без global install: `npx @cursor/bdk init ./my-bot` | [README @cursor/bdk](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/README.md) | 07.10.2026 | да |
| Шаблоны init: `security-reviewer`, `grokbot-agents`, `thermo-review`, `agentic-owners`, `triage-linear`/`triage-jira`; `--template triage` → linear | [README @cursor/bdk](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/README.md) | 07.10.2026 | да |
| Документация: `bdk docs`; при `bdk serve` — также `/docs` | [README @cursor/bdk](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/README.md) | 07.10.2026 | да |
| Деплой: на Cursor-managed hosting **или** свой инфраструктурный процесс | [README @cursor/bdk](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/README.md) | 07.10.2026 | да |
| Триггеры: source-control events, Slack, webhooks, schedules | [README @cursor/bdk](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/README.md) | 07.10.2026 | да |
| Сравнение: Automations = prompt+trigger в dashboard; Grok Bot = интерактив в app; BDK = versioned TS/MD проект с тестами | [README @cursor/bdk](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/README.md) | 07.10.2026 | да |
| Rollouts пересобран на Bot Development Kit; пакет `@cursor/bdk` на npm | [The New Stack](https://thenewstack.io/cursor-rollouts-firetiger-production/) | 24.09.2026 | да |
| Rollouts и Security Review на Teams/Enterprise; включение из automations tab | [cursor.com/changelog](https://cursor.com/changelog/rollouts-and-security-reviewer) | 23.09.2026 | да |
| Verdict Rollouts по env: verified healthy / regression detected / inconclusive | [cursor.com/changelog](https://cursor.com/changelog/rollouts-and-security-reviewer) | 23.09.2026 | да |
| Eval-файлы: `evals/**/*.eval.ts`; `bot/evals/` **игнорируется** | [skills/evals](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/skills/evals/SKILL.md) | 07.10.2026 | да |
| Eval CLI: `bdk eval --dir . --list`; CI: `--json --no-stream --junit reports/evals.xml` | [skills/evals](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/skills/evals/SKILL.md) | 07.10.2026 | да |
| Model turns в evals требуют Cursor credential (API key / service account / `bdk login`); **Node, never Bun** | [skills/evals](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/skills/evals/SKILL.md) | 07.10.2026 | да |
| Hillclimb: measure → one lever → remeasure; каждое улучшение фиксируется eval | [skills/hillclimb](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/skills/hillclimb/SKILL.md) | 07.10.2026 | да |
| GitHub fixtures: `bdk github replay … --dry-run --out fixtures/github` | [skills/hillclimb](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/skills/hillclimb/SKILL.md) | 07.10.2026 | да |
| Deploy skill: только **pushed Git ref**; локальные файлы не заливаются; нужен `CURSOR_SERVICE_ACCOUNT_KEY` | [skills/deploy](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/skills/deploy/SKILL.md) | 07.10.2026 | да |
| Перед deploy: `bdk validate --dir`; успех деплоя — status `running`, не `pending`/`deploying` | [skills/deploy](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/skills/deploy/SKILL.md) | 07.10.2026 | да |
| GitHub channel: `POST …/v1/channels/github`; prod — `cursorAccount` + `serve --cursor-events`; dev — unsigned loopback + fixtures | [AGENTS.md](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/AGENTS.md) | 07.10.2026 | да |
| Replay: синтез payloads через `gh api`, подпись webhook; `--events '*'` по умолчанию `pull_request` | [AGENTS.md](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/AGENTS.md) | 07.10.2026 | да |
| npm `@cursor/july` v0.2.20, обновление 2026-10-06; weekly downloads ~5275 (npm stats) | [npm @cursor/july](https://www.npmjs.com/package/@cursor/july) | 07.10.2026 | да (как ориентир npm, не SLA) |
| Automations: cloud agents по расписанию/событиям GitHub, GitLab, Slack, Linear, webhooks | [cursor.com/docs/automations](https://cursor.com/docs/cloud-agent/automations) | 07.10.2026 | да |
| Debug: Bun → `NGHTTP2_FRAME_SIZE_ERROR`; использовать Node; MCP tools — `advertiseTools: true` | [skills/debug](https://cdn.jsdelivr.net/npm/@cursor/bdk@0.2.18/skills/debug/SKILL.md) | 07.10.2026 | да |

**fact-bank.md:** записей про BDK нет — опираемся на таблицу выше и официальные skills.

**Версии для writer:** в тексте указывать «актуальная версия `@cursor/bdk` на дату статьи»; для примеров можно сослаться на **0.2.18** (jsDelivr) и проверять `npm view @cursor/bdk version` в sidebox, не выдумывать будущие major.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за одну рабочую сессию пройти путь **init → настройка bot → локальный `bdk dev` → минимум 1 eval → GitHub replay/fixture → push + `bdk deploy`** с service account, понимая когда выбрать BDK, а когда хватит Automations.

**Почему отличается от конкурентов:**
- README/skills — канон на EN и фрагментами; нет связного RU how-to с GitHub + evals.
- Habr/insidepc закрывают «бот в Cursor IDE», но не **Bot Development Kit**.
- New Stack/changelog дают контекст Rollouts, но не учат scaffold своего агента.

**Tone:** «BDK = репозиторий, где агент как код»; Automations = «форма в dashboard для повторяющихся jobs». Без новостной воды про M&A.

**H2-каркас (карточка B06 + research):**
1. BDK vs Cursor Automations vs Grok Bot — таблица выбора  
2. Требования: Node 22.13+, Git, Cursor login / service account  
3. `bdk init` и дерево `bot/` + `evals/`  
4. `bot/instructions.md`, tools, MCP (`mcp-connections/`), subagents  
5. Локально: `bdk dev`, playground, `bdk run` / `bdk call`  
6. Evals + hillclimb loop (smoke eval, replay → fixture)  
7. GitHub channel: replay, forward, `--cursor-events` vs webhook URL  
8. Deploy: validate → push → `bdk deploy --ref` → verify `running`  
9. Troubleshooting (login, Bun, pending deploy, MCP OAuth)  
10. FAQ  

**Internal links:** [B03 MCP в Cursor](/podklyuchenie-mcp-cursor/) — подключение MCP для tools в BDK.

**Conversion (site-brief):** CTA Make/kv-ai — max 2× только если уместно «агент в репо + сценарии в Make»; не подменять деплой BDK рекламой.

---

## 5. FAQ-кандидаты (7)

1. **Чем BDK отличается от Cursor Automations?** — Automations: prompt и trigger в dashboard; BDK: TS/MD проект в Git с evals, custom tools и выбором хостинга.  
2. **Нужен ли отдельный репозиторий для деплоя BDK?** — Да, деплой берёт **закоммиченный и запушенный** ref; незакоммиченные правки не попадут на hosting.  
3. **Как писать evals для BDK?** — Файлы `evals/**/*.eval.ts`, `defineEval`, gates на tools (`calledTool` / `notCalledTool`); для GitHub — fixtures из `bdk github replay --dry-run --out`.  
4. **Можно ли тестировать GitHub без admin webhook?** — Да: `bdk github replay` и fixtures в `--dev` с `curl` + `x-github-event`.  
5. **Что нужно для `bdk deploy`?** — `CURSOR_SERVICE_ACCOUNT_KEY`, `bdk validate`, push, затем deploy; личный `bdk login` не смешивать с service account в CI.  
6. **Почему eval падает с ошибкой API key?** — Model turns требуют Cursor credential; для CI — service account или секрет в env.  
7. **Node или Bun?** — Только **Node 22.13+**; под Bun типичен `NGHTTP2_FRAME_SIZE_ERROR` на встроенных tools.

---

## 6. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение BDK 40–60 слов | Lead | «Cursor BDK — …» |
| Таблица BDK / Automations / Grok Bot | H2-1 | Из README |
| Workflow A→B→C | H2-3–8 | init → dev → eval → push → deploy |
| Пример дерева каталогов | H2-3 | ASCII tree |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | schema agent | BlogPosting + FAQPage |

**Целевые формулировки:** «cursor bdk», «как задеплоить bdk агента», «bdk init», «bdk evals», «cursor bdk github».

---

## 7. Риски для writer

- Не путать BDK с Telegram-гайдами Habr и с `@cursor/sdk` (програмmatic agents API — смежная, но другая точка входа).  
- Не выдумывать pricing Teams/Enterprise для self-hosted BDK-проекта.  
- Не печатать `CURSOR_SERVICE_ACCOUNT_KEY` и alias tokens деплоя.  
- Min **5** нумерованных шагов + чеклист **10+** (utility gate статьи).  
- Команды CLI — из README/skills; при расхождении july/bdk использовать **`@cursor/bdk`** в user-facing тексте.  
- Объём по `quality-blog`; без эмодзи.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель установит Node 22.13+, создаст проект через `bdk init`, настроит `bot/instructions.md` и минимум один channel/tool, поднимет `bdk dev`, добавит smoke-eval в `evals/`, проверит GitHub-сценарий через replay или fixture, запушит репозиторий и выполнит `bdk validate` + `bdk deploy` с service account, умея отличить BDK от Automations и починить типичные ошибки CLI.

**action_outline (для writer):**

1. **Проверить Node ≥ 22.13** (`node -v`); при необходимости обновить через nvm/fnm.  
2. **Выбрать формат агента** по таблице (если хватит dashboard-trigger — Automations; иначе BDK).  
3. **Scaffold:** `npx @cursor/bdk init ./my-agent` (или `--template security-reviewer` для PR-бота); открыть папку в Cursor.  
4. **Настроить агента:** отредактировать `bot/instructions.md`, добавить tool в `bot/tools/` или MCP в `bot/mcp-connections/`; при GitHub — `bot/channels/github.ts` с `githubChannel()`.  
5. **Локальный цикл:** `bdk dev` → playground; прогнать `bdk run --message "…"` или `bdk call` для детерминированного tool.  
6. **Evals:** создать `evals/smoke.eval.ts` с `t.succeeded()` + `calledTool`; запустить `bdk eval --dir . --tag smoke`.  
7. **GitHub без prod webhook:** `bdk github replay owner/repo#N --dir . --dry-run --out fixtures/github`, затем POST fixture в `--dev`.  
8. **Git:** commit + push; убедиться, что `git branch -r --contains HEAD` показывает remote.  
9. **Deploy:** export `CURSOR_SERVICE_ACCOUNT_KEY` → `bdk validate` → `bdk deploy --dir . --ref HEAD`; дождаться status **`running`**, сохранить slug; при redeploy сохранить `--cursor-events-repo` / `--allow-domain` если были.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ unavailable |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ (7) |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + internal B03.
