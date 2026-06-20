# Research notes — B06 «Как настроить Claude Code: пошаговая инструкция по hooks, settings.json и CLAUDE.md»

**topic_id:** B06  
**slug:** nastrojka-claude-code-hooks-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-06-20  
**disclaimer:** Все даты, версии и статистика проверены на 20.06.2026 (2026 год).

---

## 0. Utility gate (тема)

```bash
python3 scripts/excalibur_blog_utility_gate.py --topic-id B06
# → topic B06: PASS
```

**search_intent:** how_to · **article_mode:** B · **utility_gate preflight:** PASS (подтверждено скриптом и `research-context.json`).

---

## 1. SERP-обзор (WebSearch, 20.06.2026 + сверка с research-serp.json)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [code.claude.com/docs/ru/hooks-guide](https://code.claude.com/docs/ru/hooks-guide) | Официальная docs (RU) | Канон: события, matcher, `/hooks`, примеры Notification/PostToolUse | Мало связки settings + CLAUDE.md + permissions в одном workflow | Сухой перевод без сценария «первый продакшен-сетап» |
| 2 | [code.claude.com/docs/ru/hooks](https://code.claude.com/docs/ru/hooks) | Справочник hooks (RU) | Полная схема JSON, exit codes, 5 типов handler, 30+ событий | Reference, не пошаговый onboarding | Структуру справочника 1:1 как статью |
| 3 | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | Официальная settings | Иерархия scope, permissions, hot-reload, `$schema` | EN; объёмная таблица ключей | Перечисление всех ключей settings без отбора |
| 4 | [smyslokod.ru/guides/hooks-v-claude-code](https://smyslokod.ru/guides/hooks-v-claude-code) | RU how-to hooks | 7 готовых хуков, 4 уровня конфигов, копипаст settings.json | Узкий фокус только на hooks | Копировать примеры 1:1 без адаптации под аудиторию автоматизации |
| 5 | [matveev.tech/claude-code-settings-json](https://matveev.tech/claude-code-settings-json/) | RU settings.json гайд | TL;DR по scope, `/config`, резервные копии | Слабая часть про CLAUDE.md и permissions | Дублировать TL;DR без своего угла |
| 6 | [okhlopkov.com/claude-code-nastrojka-mcp-hooks-skills-2026](https://okhlopkov.com/claude-code-nastrojka-mcp-hooks-skills-2026/) | RU личный сетап | MCP + hooks + skills в одном посте | Широкий обзор, не чек-лист guardrails | Расширять статью до «всё про экосистему» |
| 7 | [habr.com/ru/articles/987094](https://habr.com/ru/articles/987094/) | RU longread Habr | Практика автоматизации, реальный сетап | Длинный narrative, смешивает темы | Структуру Habr-эссе |
| 8 | [vc.ru/claudedry/2983306](https://vc.ru/claudedry/2983306-polnyj-gajd-po-claude-code) | Мега-гайд 220+ источников | Широта охвата | Utility-light: «вообще про Claude Code», не узкий how-to по hooks/settings | Формат «энциклопедия + новости» |
| 9 | [aiorg.dev/blog/claude-code-hooks](https://aiorg.dev/blog/claude-code-hooks) | EN hooks 20+ examples | Много готовых конфигов | Английский; security без RU контекста | EN-блоки без локализации команд (osascript vs notify-send) |
| 10 | [checkroi.ru/blog/hooks-claude-code](https://checkroi.ru/blog/hooks-claude-code/) | RU «10 защитных хуков» | Security angle | Мало про CLAUDE.md и иерархию settings | Только security без полного setup |

**Паттерн SERP:** официальная docs Anthropic (RU hooks/settings) + русские гайды 2026 с готовыми JSON + широкие обзоры (vc.ru, Habr). Запросы «claude code hooks» и «settings json» закрыты **фрагментами** — редко одна статья связывает **установку → settings → CLAUDE.md → hooks → permissions → чек-лист**.

**Intent:** how_to — читатель хочет **настроить** Claude Code под свой репозиторий: создать/отредактировать `settings.json`, написать лаконичный `CLAUDE.md`, включить 2–3 hooks как guardrails (форматирование, блок `.env`, уведомления), настроить `permissions` и проверить через `/hooks` и `--safe-mode`.

**Пробел для блога:** компактный **workflow A→B→C** для автоматизатора/техлида (не только senior backend): «за один вечер собрать командный сетап в `.claude/settings.json` + `CLAUDE.md` + 3 hooks», с troubleshooting и чек-листом 15 пунктов. Связка с B03 (MCP в Cursor) и B02 (n8n agents) — Claude Code в терминале vs IDE.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

**⚠️ WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в Cloud-окружении агента (`Server "user-mcp-kv" not found`). Инструмент `wordstat_get_top_requests` недоступен. **Точные показы/мес не получены — цифры спроса в статье не утверждать.**

**Семантика (экспертная оценка по SERP + EN-рынок, без выдуманных объёмов):**

| Кластер | Запросы | Роль в статье |
|---------|---------|---------------|
| Бренд + продукт | claude code, claude code 2026 | primary в lead/H1 |
| Конфигурация | claude code settings json, настройка claude code | H2 про иерархию settings |
| Автomation | claude code hooks, hooks claude code | H2 guardrails + примеры JSON |
| Сравнение | claude code vs cursor, claude code mcp | FAQ (кратко, без ухода в comparison-статью) |
| RU long-tail | как настроить claude code, claude code установка | FAQ + numbered steps |

**LSI для writer (из SERP + docs, без Wordstat-цифр):**

- settings.json, `.claude/settings.json`, `~/.claude/settings.json`, settings.local.json  
- CLAUDE.md, CLAUDE.local.md, claudeMdExcludes  
- hooks, PreToolUse, PostToolUse, SessionStart, Notification, `/hooks`  
- permissions allow deny ask, autoMode, disableAllHooks  
- `$schema` json.schemastore.org/claude-code-settings.json  
- `--safe-mode`, `CLAUDE_CODE_SAFE_MODE`, `claude doctor`  
- `$CLAUDE_PROJECT_DIR`, exit code 2, matcher Edit\|Write  
- MCP в Claude Code (`.mcp.json`) — 1 абзац + internal link B03  

**SEO-стратегия:** primary «claude code» + «настройка claude code» в title/H1; secondary «claude code hooks», «settings json» — в H2 и FAQ; не раздувать title словом «новости 2026».

---

## 3. Таблица фактов (цифры и утверждения только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Claude Code — агент для терминала, IDE, desktop и browser; читает кодовую базу, редактирует файлы, запускает команды | [claude.com/product/claude-code](https://claude.com/product/claude-code) | 20.06.2026 | да |
| Установка CLI: `curl -fsSL https://claude.ai/install.sh \| bash` | [claude.com/product/claude-code](https://claude.com/product/claude-code) | 20.06.2026 | да |
| Claude Code входит в планы Pro (от $17/мес при годовой подписке, $20/мес помесячно) и Max | [claude.com/product/claude-code](https://claude.com/product/claude-code) | 20.06.2026 | да |
| Официальный конфиг — `settings.json` с иерархией: user `~/.claude/settings.json`, project `.claude/settings.json`, local `.claude/settings.local.json` | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 20.06.2026 | да |
| Приоритет scope: Managed → CLI args → Local → Project → User | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 20.06.2026 | да |
| CLAUDE.md: user `~/.claude/CLAUDE.md`, project `CLAUDE.md` или `.claude/CLAUDE.md`, local `CLAUDE.local.md` | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 20.06.2026 | да |
| JSON Schema для автодополнения: `"$schema": "https://json.schemastore.org/claude-code-settings.json"` | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 20.06.2026 | да |
| Изменения `permissions`, `hooks`, `apiKeyHelper` подхватываются без перезапуска; срабатывает hook `ConfigChange` | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 20.06.2026 | да |
| Ключи `model` и `outputStyle` читаются при старте сессии; mid-session — `/model` | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 20.06.2026 | да |
| С v2.1.181 можно менять опцию через `/config key=value` без UI | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 20.06.2026 | да |
| Hooks — команды shell, HTTP, MCP tool, prompt или agent на lifecycle-событиях | [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) | 20.06.2026 | да |
| Схема hooks: событие → массив matcher-групп → массив handlers с `"type": "command"` и т.д. | [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) | 20.06.2026 | да |
| Пять типов handler: `command`, `http`, `mcp_tool`, `prompt`, `agent` | [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) | 20.06.2026 | да |
| Exit code **2** блокирует действие (PreToolUse, UserPromptSubmit и др.); exit **1** — non-blocking error | [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) | 20.06.2026 | да |
| `"disableAllHooks": true` отключает user/project/local hooks (managed hooks могут остаться) | [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) | 20.06.2026 | да |
| Меню `/hooks` — read-only просмотр; правки только через JSON или просьбу Claude | [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide) | 20.06.2026 | да |
| Default timeout: 600 с для command/http/mcp_tool; 30 с для prompt; 60 с для agent | [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) | 20.06.2026 | да |
| MCP tools в matcher: паттерн `mcp__server__tool`; для всех tools сервера — `mcp__memory__.*` | [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) | 20.06.2026 | да |
| Пример permissions: `"allow": ["Bash(npm run lint)"]`, `"deny": ["Read(./.env)"]` | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 20.06.2026 | да |
| `--safe-mode` / `CLAUDE_CODE_SAFE_MODE`: не грузятся CLAUDE.md, skills, plugins, hooks, MCP, custom commands/agents | [code.claude.com/docs/ru/whats-new/2026-w24](https://code.claude.com/docs/ru/whats-new/2026-w24) | 8–12.06.2026 | да |
| Релизы недели 24 (8–12 июня 2026): v2.1.166 → v2.1.176; `/cd` для смены каталога (v2.1.169) | [code.claude.com/docs/ru/whats-new/2026-w24](https://code.claude.com/docs/ru/whats-new/2026-w24) | 8–12.06.2026 | да |
| Устаревший пример hooks в таблице settings (`{"PreToolUse": {"Bash": "..."}}`) — **невалиден**; нужен массив matcher-объектов | [github.com/anthropics/claude-code/issues/18960](https://github.com/anthropics/claude-code/issues/18960) | 2026 | да (как предупреждение writer) |
| Хук vs CLAUDE.md: инструкции в CLAUDE.md модель может «забыть»; hook выполняется детерминированно | [code.claude.com/docs/ru/hooks-guide](https://code.claude.com/docs/ru/hooks-guide) | 20.06.2026 | да |
| Linux-уведомление Notification hook: `notify-send 'Claude Code' '...'` | [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide) | 20.06.2026 | да |
| Managed settings Linux path: `/etc/claude-code/managed-settings.json` | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 20.06.2026 | да |
| Claude Code хранит до **5** резервных копий конфигов с timestamp | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 20.06.2026 | да |

**fact-bank.md:** записей про Claude Code нет — все факты только из таблицы выше.

**Не использовать без оговорки:** цифры Wordstat; «220+ источников» из vc.ru как E-E-A-T; версии CLI старше v2.1.176 как «последние» — сверять с [GitHub releases](https://github.com/anthropics/claude-code/releases) на дату публикации.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **45–60 минут** пройти полный сетап Claude Code в репозитории: `/login` → базовый `.claude/settings.json` → короткий `CLAUDE.md` → **3 hooks** (PostToolUse format, PreToolUse block `.env`, Notification) → `permissions` deny для секретов → проверка `/hooks`, тест prompt, при сбое — `--safe-mode` и `claude doctor`.

**Почему отличается от конкурентов:**

- Официальная docs — канон, но разнесена по settings/hooks/CLAUDE.md без единого чек-листа.
- Мега-гайды (vc.ru) — широта без actionable guardrails.
- RU-блоги с 7–10 hooks — мало про permissions и перегруз CLAUDE.md.
- **Наш фокус:** workflow + чек-лист 15 пунктов + связь «инструкция (CLAUDE.md) vs enforcement (hooks + permissions)».

**Tone:** «CLAUDE.md = договорённость с агентом; hooks = охранник у двери». Без новостного FOMO про «панику производительности 2026».

**H2-каркас (из карточки B06 + research):**

1. Установка и первый запуск: install script, `/login`, `/config`, выбор модели  
2. Иерархия settings.json (user / project / local) + `$schema`  
3. CLAUDE.md без перегруза: что в project-level, что в hooks  
4. Hooks guardrails: PreToolUse, PostToolUse, SessionStart (+ Notification на Linux)  
5. Permissions и auto-mode: deny `.env`, allow lint/test  
6. Чек-лист 15 пунктов + troubleshooting (`--safe-mode`, `/hooks`, invalid JSON)  
7. FAQ (5–7): hooks vs CLAUDE.md, путь settings, Claude Code vs Cursor, MCP  

**Internal links:** `/podklyuchenie-mcp-cursor/` (MCP — соседний слой), `/avtomatizaciya-n8n-ai-agents/` (фоновые сценарии vs терминальный агент).

---

## 5. Черновик hooks для writer (копипаст-блоки, проверить пути ОС)

| # | Событие | Matcher | Назначение | Exit |
|---|---------|---------|------------|------|
| 1 | PostToolUse | Edit\|Write | auto-format (prettier/ruff) | 0 |
| 2 | PreToolUse | Read | блок чтения `.env` / secrets | 2 + JSON deny |
| 3 | PreToolUse | Bash | блок `git push` в main (regex/if) | 2 |
| 4 | Notification | *(empty)* | notify-send на Linux | 0 |
| 5 | SessionStart | startup | inject `additionalContext` (кратко) | 0 |

**Рекомендация:** в статье **полностью** разобрать hooks 1–2–4; остальные — в чек-листе «расширить позже».

---

## 6. FAQ-кандидаты (5–7)

1. **Как настроить Claude Code с нуля?** — install → `/login` → `.claude/settings.json` + `CLAUDE.md` → `/hooks`.  
2. **Где лежит settings.json?** — `~/.claude/` (глобально) vs `.claude/` в репо; local — `.claude/settings.local.json`.  
3. **Что такое hooks и чем отличаются от CLAUDE.md?** — hooks = код на события; CLAUDE.md = текстовые инструкции без гарантии исполнения.  
4. **Как отключить все hooks для отладки?** — `disableAllHooks: true` или `claude --safe-mode`.  
5. **Почему hook не срабатывает?** — неверная nested-схема JSON, matcher, путь без `$CLAUDE_PROJECT_DIR`, смотреть `/hooks` и debug log.  
6. **Claude Code vs Cursor?** — Claude Code = терминальный/IDE агент Anthropic; Cursor = IDE с Agent + `.cursor/mcp.json` (1 абзац + link B03).  
7. **Нужен ли CLAUDE.md, если есть hooks?** — да: hooks не заменяют conventions/build commands; не дублировать hook-логику в markdown.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение hooks + settings 40–60 слов | Lead | «Claude Code настраивается через…» |
| Таблица scope settings | H2-2 | User / Project / Local + пути |
| Workflow | H2-2–5 | install → settings → CLAUDE.md → hooks → permissions → verify |
| Пример валидного hooks JSON | H2-4 | PostToolUse + PreToolUse |
| Чек-лист 15 пунктов | H2-6 | Numbered checklist |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff → schema agent | BlogPosting + FAQPage |

---

## 8. Риски для writer

- **Не копировать** невалидный flat-map пример hooks из старых пересказов settings.md.  
- **Не выдумывать** показы Wordstat.  
- Объём: 8 500–9 500 знаков (`quality-blog`).  
- Min **5** numbered steps + чек-лист **15** пунктов (карточка темы).  
- Платформенные команды: macOS osascript vs Linux notify-send — явно помечать ОС.  
- Цены Pro/Max — с оговоркой «на дату статьи, см. claude.com».  
- Без emoji; дефис вместо длинного тире.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель установит Claude Code, создаст проектный `.claude/settings.json` и `CLAUDE.md`, добавит рабочие hooks (форматирование + защита секретов + уведомление), настроит permissions deny для `.env`, проверит конфигурацию через `/hooks`, при ошибках изолирует проблему через `--safe-mode` или `claude doctor`, и пройдёт чек-лист из 15 пунктов перед командным продакшен-сетапом.

**action_outline (для writer):**

1. **Установить Claude Code** (`curl -fsSL https://claude.ai/install.sh | bash`), выполнить `/login`, открыть `/config` — выбрать модель и базовые permissions.  
2. **Создать структуру `.claude/`** в репозитории: `settings.json` (командный) + при необходимости `settings.local.json` (личные overrides, в `.gitignore`).  
3. **Добавить `$schema`** и блок `permissions`: allow для lint/test, deny для `.env` и опасных Bash-паттернов.  
4. **Написать лаконичный `CLAUDE.md`** (build/test команды, стиль коммитов, layout репо) — не дублировать то, что пойдёт в hooks.  
5. **Добавить hooks в `settings.json`:** PostToolUse (format), PreToolUse (block secrets), Notification (Linux `notify-send`); использовать nested schema с `"type": "command"`.  
6. **Проверить:** `/hooks` — источник и matcher; тестовый prompt на edit файла и попытку read `.env` (ожидать block).  
7. **Hot-reload:** убедиться, что правка hooks подхватывается без перезапуска; при странном поведении — `claude --safe-mode` для изоляции конфига.  
8. **Диагностика:** `claude doctor` при invalid JSON; сверить с официальным hooks reference, не с устаревшими gist.  
9. **Финал:** пройти чек-лист 15 пунктов (backup, git commit settings, deny secrets, timeout hooks, документировать для команды).

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (10) |
| Wordstat MCP | ⚠️ недоступен (без цифр) |
| Таблица фактов с URL | ✅ (25 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.
