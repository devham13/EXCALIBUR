# Research notes — B06 «Как установить и настроить Claude Code: пошаговая инструкция для автоматизации разработки»

**topic_id:** B06  
**slug:** ustanovka-claude-code  
**article_mode:** B (how-to)  
**research_date:** 2026-08-13  
**disclaimer:** Все даты, версии и статистика проверены на 13.08.2026.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | Официальная docs (RU) | Канон: ОС, RAM, native/npm/apt/winget, Windows native vs WSL, troubleshooting | Мало связки «Claude Code vs Cursor» для бизнес-аудитории | Сухой пересказ без сценария автоматизации |
| 2 | [code.claude.com/docs/ru/quickstart](https://code.claude.com/docs/ru/quickstart) | Официальный quickstart (RU) | Первый сеанс, /login, базовые команды claude/-p/-c | Не закрывает hooks + headless CI/CD одним workflow | Копировать 1:1 без угла «автоматизация разработки» |
| 3 | [thecode.media/claude-code-gajd](https://thecode.media/claude-code-gajd/) | RU longread | Пошагово macOS/Linux/Windows, sudo npm предупреждение, claude doctor | Устаревшие детали npm (Node 18+) в части мест | Структуру 1:1 |
| 4 | [ailibri.com/blog/kak-ustanovit-claude-code](https://ailibri.com/blog/kak-ustanovit-claude-code) | RU гайд 2026 | Native installer, Pro $20, первый запуск | Коммерческий блог, мало MCP/hooks | Цены без ссылки на claude.com/pricing |
| 5 | [dev.to/.../claude-code-setup-in-2026](https://dev.to/dublecc/claude-code-setup-in-2026-install-paths-auth-and-the-first-run-errors-people-actually-hit-46ie) | EN setup 2026 | Таблица install paths, ANTHROPIC_API_KEY vs Pro, Git Bash на Windows | Английский; нет RU troubleshooting | Таблицу install paths без адаптации под RU-аудиторию |
| 6 | [habr.com/ru/articles/1022624](https://habr.com/ru/articles/1022624/) | Habr RU (Windows) | Native Windows, Git Bash, WSL 2, settings.json | Узкий фокус Windows enterprise | Enterprise-истории без how-to шагов |
| 7 | [habr.com/ru/companies/bothub/articles/983542](https://habr.com/ru/companies/bothub/articles/983542/) | Habr RU (обзор) | MCP claude mcp add, npm fallback | Смешивает Node 18+ для MCP и install | Обход подписки / grey-area конфиги |
| 8 | [claudeskills.ru/blog/claude-code-guide](https://claudeskills.ru/blog/claude-code-guide) | RU сторонний | CLAUDE.md, MCP, команды | Не официальный источник версий | Версии и команды без сверки с docs |

**Паттерн SERP:** топ — официальная документация Anthropic (setup/quickstart) + русские гайды 2026 (thecode.media, ailibri, Habr) + англоязычные «first-run errors». Запрос «claude code установка» закрыт фрагментарно: редко в одной статье есть **install + CLAUDE.md + MCP + hooks + headless (-p) + troubleshooting**.

**Intent:** how_to — читатель хочет **установить** Claude Code на своей ОС, **авторизоваться**, **настроить проект** (CLAUDE.md, permissions) и **подключить автоматизацию** (MCP, hooks, headless для скриптов). Вторичный intent: чем Claude Code отличается от Cursor/чата Claude для agentic-разработки.

**Пробел для Excalibur BLOG:** единый русский how-to для практика автоматизации (не только senior dev): native install → auth → CLAUDE.md → MCP через `.mcp.json` / `claude mcp add` → hooks для коммитов/тестов → `claude -p` для CI; troubleshooting npm/sudo/PATH/Plan Mode; мягкая связка с [B03 MCP Cursor](/podklyuchenie-mcp-cursor/) (MCP-концепция та же, конфиг другой).

---

## 2. Яндекс Wordstat

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в среде Cloud Agent (MCP не подключён). Инструмент `wordstat_get_top_requests` не вызывался. **Точные объёмы спроса (показы/мес) не получены** — не использовать выдуманные цифры в статье.

**Экспертная семантика (без объёмов, для LSI writer):**

| Кластер | Ключевые фразы (LSI) |
|---------|---------------------|
| Установка | claude code установка, claude code cli, npm install claude code, install.sh, install.ps1 |
| Платформы | claude code windows, claude code mac, claude code linux, claude code wsl |
| Настройка | claude code настройка, CLAUDE.md, claude code settings, claude doctor |
| MCP | claude code mcp, claude mcp add, .mcp.json, /mcp |
| Автоматизация | claude code hooks, claude code headless, claude -p, claude code ci cd |
| Сравнение | claude code vs cursor, claude code vs chatgpt codex, как пользоваться claude code |
| Оплата | claude code подписка, claude pro claude code, claude code api key |

**SEO-стратегия (без Wordstat-цифр):** primary «claude code» в H1/lead; secondary «claude code установка», «claude code mcp», «claude code hooks», «как пользоваться claude code», «claude code cli» — в H2/H3 и FAQ. Long-tail «claude code windows wsl», «claude doctor», «npm @anthropic-ai/claude-code» — в troubleshooting и таблицах.

**После восстановления MCP:** повторить `wordstat_get_top_requests` для `claude code`, `claude code установка`, `claude code mcp`, `как пользоваться claude code` и обновить таблицу спроса.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Claude Code поддерживает macOS 13.0+, Windows 10 1809+ / Windows Server 2019+, Ubuntu 20.04+, Debian 10+, Alpine Linux 3.19+ | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 13.08.2026 | да |
| Минимум оборудования: 4 ГБ+ ОЗУ, процессор x64 или ARM64; нужен интернет | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 13.08.2026 | да |
| Рекомендуемая установка macOS/Linux/WSL: `curl -fsSL https://claude.ai/install.sh \| bash` | [code.claude.com/docs/ru/quickstart](https://code.claude.com/docs/ru/quickstart) | 13.08.2026 | да |
| Windows PowerShell: `irm https://claude.ai/install.ps1 \| iex` | [code.claude.com/docs/ru/quickstart](https://code.claude.com/docs/ru/quickstart) | 13.08.2026 | да |
| Windows CMD: `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` | [code.claude.com/docs/ru/quickstart](https://code.claude.com/docs/ru/quickstart) | 13.08.2026 | да |
| Native install автообновляется в фоне; Homebrew и WinGet — **ручное** обновление | [code.claude.com/docs/ru/quickstart](https://code.claude.com/docs/ru/quickstart) | 13.08.2026 | да |
| Homebrew: `brew install --cask claude-code` (stable ~неделя отставания) или `claude-code@latest` | [code.claude.com/docs/ru/quickstart](https://code.claude.com/docs/ru/quickstart) | 13.08.2026 | да |
| WinGet: `winget install Anthropic.ClaudeCode` | [code.claude.com/docs/ru/quickstart](https://code.claude.com/docs/ru/quickstart) | 13.08.2026 | да |
| npm (с v2.1.198): `npm install -g @anthropic-ai/claude-code`, требует **Node.js 22+** | [code.claude.com/docs/en/install](https://code.claude.com/docs/en/install) | 13.08.2026 | да |
| **Не использовать** `sudo npm install -g` — риски прав и безопасности | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 13.08.2026 | да |
| npm-пакет ставит тот же native binary, что standalone installer | [code.claude.com/docs/en/install](https://code.claude.com/docs/en/install) | 13.08.2026 | да |
| Обновление npm: `npm install -g @anthropic-ai/claude-code@latest` (не `npm update -g`) | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 13.08.2026 | да |
| Диагностика: `claude doctor` | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 13.08.2026 | да |
| На macOS/Linux launcher: `~/.local/bin/claude` (symlink в `~/.local/share/claude/versions/`) | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 13.08.2026 | да |
| Бесплатный план Claude.ai **не включает** Claude Code; нужны Pro/Max/Team/Enterprise или Console/API | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 13.08.2026 | да |
| Claude Pro: **$20/мес** при помесячной оплате ($17/мес при годовой, $200 upfront); включает Claude Code | [claude.com/pricing](https://claude.com/pricing) | 13.08.2026 | да |
| Claude Max: от **$100/мес** (5x или 20x usage vs Pro) | [claude.com/pricing](https://claude.com/pricing) | 13.08.2026 | да |
| Лимиты usage сбрасываются в **скользящем 5-часовом окне**; Claude Code и чат делят один пул | [claude.com/pricing](https://claude.com/pricing) (FAQ) | 13.08.2026 | да |
| Первый запуск: `claude` → браузерная auth; переключение аккаунта: `/login` | [code.claude.com/docs/ru/quickstart](https://code.claude.com/docs/ru/quickstart) | 13.08.2026 | да |
| Headless/скрипты: `claude -p "query"` (print mode, без интерактива) | [code.claude.com/docs/ru/cli-reference](https://code.claude.com/docs/ru/cli-reference) | 13.08.2026 | да |
| Plan Mode: `--permission-mode plan` (только план, без правок до approve) | [code.claude.com/docs/ru/cli-reference](https://code.claude.com/docs/ru/cli-reference) | 13.08.2026 | да |
| Windows native: Git for Windows опционален; без него shell tool = PowerShell; с Git Bash — Bash tool | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 13.08.2026 | да |
| WSL 2: поддерживается **sandboxed command execution**; WSL 1 — без sandbox | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 13.08.2026 | да |
| CLAUDE.md: `./CLAUDE.md` или `./.claude/CLAUDE.md`; автогенерация: `/init` | [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) | 13.08.2026 | да |
| Project MCP config: **`.mcp.json` в корне репозитория**, не внутри `.claude/` | [code.claude.com/docs/en/debug-your-config](https://code.claude.com/docs/en/debug-your-config) | 13.08.2026 | да |
| MCP scopes: `local` (default, ~/.claude.json per project), `project` (.mcp.json), `user` (~/.claude.json global) | [code.claude.com/docs/en/mcp-quickstart](https://code.claude.com/docs/en/mcp-quickstart) | 13.08.2026 | да |
| Добавление MCP CLI: `claude mcp add --transport http <name> <url>` или stdio через `-- npx ...` | [code.claude.com/docs/en/mcp-quickstart](https://code.claude.com/docs/en/mcp-quickstart) | 13.08.2026 | да |
| Проверка MCP/hooks: команды сеанса `/mcp`, `/hooks`; конфиг hooks в `"hooks"` key settings (`.claude/settings.json` или `~/.claude/settings.json`) | [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide) | 13.08.2026 | да |
| Desktop app — альтернатива CLI без терминала (macOS/Windows/Linux) | [code.claude.com/docs/ru/quickstart](https://code.claude.com/docs/ru/quickstart) | 13.08.2026 | да |

**fact-bank.md:** записей по Claude Code нет — все факты только из таблицы выше.

**Не использовать без оговорки:** сторонние гайды с Node 18+ для npm-install (официально с v2.1.198 — Node 22+); Habr-статьи про обход подписки через сторонние API; VPN/обход блокировок (site-brief запрет).

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **20–40 минут** установить Claude Code нативным установщиком на своей ОС, пройти auth, создать/инициализировать **CLAUDE.md**, подключить **первый MCP-сервер**, добавить **hook** для рутины (коммит/тест) и проверить **headless**-вызов `claude -p` для скрипта автоматизации.

**Почему отличается от конкурентов:**
- Официальная docs — канон, но разбита на setup/quickstart/mcp/hooks без единого «от нуля до автоматизации».
- RU-гайды часто останавливаются на install + первый prompt.
- Excalibur: B2B-практик автоматизации, связка agentic CLI + MCP + hooks + CI, сравнение с Cursor (internal link B03).

**Tone:** Claude Code = «агент в терминале, который читает репозиторий и выполняет команды с вашим approve»; MCP = «розетка для внешних tools» (как в B03, но `.mcp.json` и `claude mcp add`); hooks = «скрипт на событие, без участия Claude в решении запускать или нет».

**H2-каркас (из карточки + research):**
1. Claude Code vs Cursor vs чат Claude: что выбрать для автоматизации в 2026  
2. Установка CLI: macOS, Linux, Windows native, WSL (таблица методов)  
3. Auth, claude doctor, PATH (~/.local/bin)  
4. CLAUDE.md, /init, permissions, папка .claude  
5. MCP: claude mcp add, .mcp.json, /mcp, scope local/project/user  
6. Hooks: settings.json, PreToolUse/SessionStart, связка с MCP  
7. Headless: claude -p, --permission-mode plan, CI-паттерн  
8. Troubleshooting: sudo npm, EBADENGINE Node 22, command not found, лимиты Pro/Max  

**Internal links:** [B03 MCP Cursor](/podklyuchenie-mcp-cursor/) — общая логика MCP, отличия конфигов.

---

## 5. Сравнение Claude Code / Cursor / чат (черновик для writer)

| Критерий | Claude Code (CLI) | Cursor (IDE) | Claude.ai (чат) |
|----------|-------------------|--------------|-----------------|
| Где работает | Терминал, CI, VS Code extension | IDE (форк VS Code) | Браузер / apps |
| Agentic: правка файлов, bash | Да, с approve | Да, Agent mode | Ограниченно (artifacts) |
| MCP | `.mcp.json`, `claude mcp add`, `/mcp` | `.cursor/mcp.json` (см. B03) | Connectors (другой UX) |
| Headless / CI | `claude -p`, JSON output | Cloud Agents (отдельный продукт) | Нет |
| Hooks | `.claude/settings.json` hooks | Rules, не тот же hooks API | Нет |
| Лучше для | Скрипты, серверы, git-воркфлоу, CI | Ежедневная разработка в IDE | Брейншторм, документы |

**Рекомендация writer:** не объявлять «один победитель» — дать decision tree: «IDE каждый день → Cursor; terminal/CI/automation repo → Claude Code; оба могут сосуществовать».

---

## 6. FAQ-кандидаты (из карточки + research)

1. **Как установить Claude Code на Windows?** — PowerShell `irm https://claude.ai/install.ps1 \| iex` или WSL + install.sh; перезапуск терминала для PATH.  
2. **Нужен ли Node.js?** — для **native install** нет; для npm-пути да (Node 22+ с v2.1.198).  
3. **Чем Claude Code отличается от Cursor?** — см. таблицу §5; Cursor = IDE-first, Claude Code = terminal/CI-first.  
4. **Как подключить MCP к Claude Code?** — `claude mcp add ...` или `.mcp.json` в корне; проверка `/mcp`.  
5. **Бесплатно ли Claude Code?** — нет; нужен платный план или Console/API credits.  
6. **Что делать, если `claude: command not found`?** — проверить PATH (`~/.local/bin` на Unix, `%USERPROFILE%\.local\bin` на Windows), `claude doctor`.  
7. **Можно ли запускать без интерактива?** — `claude -p "задача"`; для CI — `--output-format json`, лимиты `--max-budget-usd`.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Claude Code 40–60 слов | Lead | «Claude Code — agentic CLI от Anthropic…» |
| Таблица install methods | H2-2 | native / brew / winget / npm + auto-update |
| Блок команд install (3 ОС) | H2-2 | code blocks из official docs |
| Workflow | H2-4–7 | install → auth → CLAUDE.md → MCP → hook → claude -p test |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «claude code», «claude code установка», «claude code mcp», «claude code hooks», «как пользоваться claude code».

---

## 8. Риски для writer

- Не выдумывать Wordstat-объёмы (MCP недоступен).  
- Версию Node для npm брать **22+** (official v2.1.198+), не 18 из старых RU-гайдов.  
- Не описывать обход подписки / VPN (site-brief).  
- Min **5** нумерованных шагов + чеклист **10+** (utility gate статьи).  
- Без эмодзи; дефис вместо длинного тире; прямые кавычки.  
- Цены Pro/Max — только с claude.com/pricing на дату статьи.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель установит Claude Code нативным способом на своей ОС, авторизуется, проверит установку через `claude doctor`, настроит CLAUDE.md и permissions, подключит MCP-сервер через `claude mcp add` или `.mcp.json`, добавит hook для автоматизации рутины и запустит одноразовую задачу через `claude -p` для CI/скриптов.

**action_outline (для writer):**

1. **Проверить prerequisites:** ОС из supported list, 4+ ГБ RAM, платная подписка Claude или Console API; выбрать путь: native (рекомендуется) vs npm (если уже есть Node 22+).  
2. **Установить CLI:** выполнить install.sh (macOS/Linux/WSL) или install.ps1 (Windows); альтернатива brew/winget/apt по таблице docs; перезапустить терминал.  
3. **Проверить PATH и health:** `claude --version`, при ошибке «command not found» добавить `~/.local/bin` (или Windows `%USERPROFILE%\.local\bin`); `claude doctor`.  
4. **Авторизоваться:** `claude` → browser login или Console; при конфликте `ANTHROPIC_API_KEY` — unset или явный выбор метода auth.  
5. **Инициализировать проект:** `cd` в репозиторий → `/init` или вручную `CLAUDE.md` (build/test команды, conventions); при необходимости `.claude/settings.json` для permissions.  
6. **Подключить MCP:** `claude mcp add --scope project ...` или `.mcp.json` в корне; approve в сеансе; проверить `/mcp` (не класть MCP config в `.claude/`).  
7. **Добавить hook:** в settings `"hooks"` (например PreToolUse для git commit или SessionStart для контекста); проверить `/hooks`.  
8. **Проверить headless:** `claude -p "explain this repo structure"` или тест CI с `--output-format json`; для планирования без правок — `--permission-mode plan`.  
9. **Troubleshooting чеклист:** sudo npm, EBADENGINE → upgrade Node 22+, 403 on curl → troubleshoot-install docs, лимиты usage → Settings > Usage / upgrade plan.

---

## 10. Handoff writer

- **primary_query:** claude code  
- **secondary_queries:** claude code установка, claude code mcp, claude code hooks, как пользоваться claude code, claude code cli  
- **cover_scene_hint:** терминал с логотипом Claude Code, CLAUDE.md, hooks, MCP-серверы, Routines/Headless  
- **sources_priority:** code.claude.com/docs/ru/* > claude.com/pricing > thecode.media (RU sanity check)  
- **blockers:** none
