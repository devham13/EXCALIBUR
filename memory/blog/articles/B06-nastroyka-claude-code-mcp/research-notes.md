# Research notes — B06 «Как настроить Claude Code: пошаговая инструкция для автоматизации с MCP и hooks»

**topic_id:** B06  
**slug:** nastroyka-claude-code-mcp  
**article_mode:** B (how-to)  
**research_date:** 2026-07-07  
**disclaimer:** Все даты, версии и статистика проверены на 07.07.2026.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | Официальная docs (RU) | Канон: native install, Windows/WSL, системные требования, auth, обновления | Мало бизнес-сценариев; MCP/hooks — на других страницах | Сухой пересказ без workflow «install → MCP → hook» |
| 2 | [code.claude.com/docs/ru/mcp](https://code.claude.com/docs/ru/mcp) | Официальная docs MCP (RU) | `claude mcp add`, `.mcp.json`, scope, `/mcp`, OAuth, безопасность | Для разработчиков; нет связки с Make/n8n/Wordstat для маркетолога | Копировать 1:1 без русского «на пальцах» |
| 3 | [code.claude.com/docs/ru/hooks-guide](https://code.claude.com/docs/ru/hooks-guide) | Официальная docs hooks (RU) | Первый hook, `/hooks`, типы command/http/mcp_tool | Мало готовых примеров под автоматизацию контента | Длинный reference без action steps |
| 4 | [habr.com/ru/articles/987094](https://habr.com/ru/articles/987094/) | RU longread (перевод) | Skills, MCP, hooks, субагенты, контекст | Уклон в dev-сетап; 20–30 MCP «в конфиге» без пошагового install | Структуру 1:1; перегруз MCP-серверами |
| 5 | [habr.com/ru/amp/publications/1028988](https://habr.com/ru/amp/publications/1028988/) | RU advanced (Habr) | PreToolUse/PostToolUse, скрипты в `.claude/hooks/` | Для senior; нет Windows-first и «первого pipeline» | Inline bash-простыни в JSON как единственный паттерн |
| 6 | [dtf.ru/howto/4796778-ustanovka-claude-i-claude-code-v-rossii](https://dtf.ru/howto/4796778-ustanovka-claude-i-claude-code-v-rossii) | RU install + регион | Россия, оплата, Windows/Mac/Linux, VS Code | Фокус на доступ из РФ, почти без MCP/hooks | Уход в «как зарегистрироваться» вместо настройки |
| 7 | [okhlopkov.com/claude-code-nastrojka-mcp-hooks-skills-2026](https://okhlopkov.com/claude-code-nastrojka-mcp-hooks-skills-2026/) | RU practitioner blog | MCP + hooks + skills + CLAUDE.md, «рабочий сетап» | Личный блог; мало troubleshooting Windows PATH | Личный стек как универсальный рецепт |
| 8 | [claudeskills.ru/blog/claude-code-windows](https://claudeskills.ru/blog/claude-code-windows) | RU Windows how-to | PowerShell install, типичные ошибки Git/PATH | Узкий фокус install; без MCP pipeline | Коммерческий bias без официальных ссылок |

**Паттерн SERP:** в топе — **официальная docs Anthropic (RU)** + **русские гайды по установке из РФ** + **англоязычные deep-dive по hooks/MCP tool hooks (2026)**. Запрос по H1 попадает прямо в [docs/ru/mcp](https://code.claude.com/docs/ru/mcp) и Habr — конкуренция с каноном, но **пробел**: единый русскоязычный **business how-to** «от нуля до первого автоматизированного pipeline» (install + CLAUDE.md + 2 MCP + 1 hook) для аудитории без dev-бэкграунда.

**Intent:** how_to — читатель хочет **установить** Claude Code, **войти**, **настроить проект** (CLAUDE.md, permissions), **подключить MCP** (Wordstat, filesystem, интеграции), **повесить hook** для guardrails/уведомлений и **прогнать первую headless- или полуавтономную задачу**.

**Пробел для «Ковчег»:** связка с **B03 (Cursor MCP)** и **B02 (n8n)** — Claude Code как CLI-агент для скриптов/CI и подготовки сценариев, Cursor как IDE; один сквозной чеклист без новостного шума.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 07.07.2026)

⚠️ **WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` **не подключён** в среде Cloud Agent (вызов `wordstat_get_top_requests` недоступен: «MCP server does not exist»). **Точные объёмы показов не получены.** Для восстановления: подключить MCP в Cursor IDE; при ошибке `401 Unauthorized` обновить токен через [OAuth Yandex](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40) и повторить research.

**Запросы, которые должны быть сняты при восстановлении MCP:**

| Запрос (для wordstat_get_top_requests) | Роль |
|--------------------------------------|------|
| claude code | primary_query |
| claude code mcp | secondary |
| как установить claude code | secondary |
| claude code windows | secondary |
| claude code hooks | secondary |
| настройка claude code | LSI (из SERP) |
| claude code установка | LSI |
| claude code mcp server | LSI |

### LSI для writer (из SERP + secondary_queries, **без объёмов** — до повторного Wordstat)

- claude code установка, claude code windows, claude code linux, claude code wsl  
- claude code mcp, claude mcp add, `.mcp.json`, `/mcp`  
- claude code hooks, PostToolUse, PreToolUse, mcp_tool hook  
- CLAUDE.md, `.claude/settings.json`, permissions  
- как установить claude code в россии, claude code pro max  
- claude code vs cursor, claude code automation  

**SEO-стратегия (черновик):** primary «claude code» в H1/lead; secondary «claude code mcp», «как установить claude code», «claude code hooks», «claude code windows» — в H2/H3 и FAQ. После Wordstat — уточнить приоритеты по таблице показов.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Claude Code: macOS 13.0+, Windows 10 1809+, Ubuntu 20.04+, Debian 10+, Alpine 3.19+; 4 ГБ+ ОЗУ; x64/ARM64 | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 07.07.2026 | да |
| Native install (рекомендуется): `curl -fsSL https://claude.ai/install.sh \| bash` (macOS/Linux/WSL); Windows PowerShell: `irm https://claude.ai/install.ps1 \| iex` | [code.claude.com/docs/ru/quickstart](https://code.claude.com/docs/ru/quickstart) | 07.07.2026 | да |
| Альтернативы: Homebrew `brew install --cask claude-code`, WinGet `winget install Anthropic.ClaudeCode` | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 07.07.2026 | да |
| Native install автообновляется в фоне; Homebrew/WinGet — ручное обновление | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 07.07.2026 | да |
| На native Windows рекомендуется Git for Windows для Bash tool; без него — PowerShell как shell tool | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 07.07.2026 | да |
| Проверка: `claude --version`, диагностика `claude doctor` | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 07.07.2026 | да |
| Auth: Pro, Max, Team, Enterprise или Console; **бесплатный план Claude.ai не включает Claude Code** | [code.claude.com/docs/ru/setup](https://code.claude.com/docs/ru/setup) | 07.07.2026 | да |
| Pro: $20/мес ($200/год); Max 5x: $100/мес; Max 20x: $200/мес | [support.claude.com/en/articles/11049762-choosing-a-claude-ai-plan](https://support.claude.com/en/articles/11049762-choosing-a-claude-ai-plan) | 07.07.2026 | да |
| Pro/Max: лимиты использования **общие** для Claude (web) и Claude Code | [support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan) | 07.07.2026 | да |
| Если задан `ANTHROPIC_API_KEY`, Claude Code может аутентифицироваться по API (отдельная биллинг-логика) | [support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan) | 07.07.2026 | да |
| MCP — открытый протокол интеграции AI с инструментами; Claude Code подключает сотни внешних сервисов | [code.claude.com/docs/ru/mcp](https://code.claude.com/docs/ru/mcp) | 07.07.2026 | да |
| HTTP MCP (рекомендуется для remote): `claude mcp add --transport http <name> <url>` | [code.claude.com/docs/ru/mcp](https://code.claude.com/docs/ru/mcp) | 07.07.2026 | да |
| Stdio MCP: `claude mcp add --env KEY=val --transport stdio <name> -- <command> [args]`; разделитель `--` обязателен | [code.claude.com/docs/ru/mcp](https://code.claude.com/docs/ru/mcp) | 07.07.2026 | да |
| Scope MCP: `local` (по умолчанию), `project` (`.mcp.json` в репо), `user` (все проекты) | [code.claude.com/docs/ru/mcp](https://code.claude.com/docs/ru/mcp) | 07.07.2026 | да |
| Управление: `claude mcp list`, `claude mcp get`, `claude mcp remove`; в сессии — `/mcp` | [code.claude.com/docs/ru/mcp](https://code.claude.com/docs/ru/mcp) | 07.07.2026 | да |
| Project `.mcp.json` требует одобрения; в недоверенной папке servers остаются `Pending approval` (v2.1.196+) | [code.claude.com/docs/ru/mcp](https://code.claude.com/docs/ru/mcp) | 07.07.2026 | да |
| HTTP/SSE auto-reconnect: до 5 попыток с экспоненциальной задержкой | [code.claude.com/docs/ru/mcp](https://code.claude.com/docs/ru/mcp) | 07.07.2026 | да |
| Hooks: глобально `~/.claude/settings.json`, проект `.claude/settings.json`, локально `.claude/settings.local.json` | [code.claude.com/docs/ru/settings](https://code.claude.com/docs/ru/settings) | 07.07.2026 | да |
| Типы hooks: `command`, `http`, `mcp_tool`, `prompt`, `agent` (experimental) | [code.claude.com/docs/ru/hooks-guide](https://code.claude.com/docs/ru/hooks-guide) | 07.07.2026 | да |
| Просмотр hooks: команда `/hooks` в Claude Code | [code.claude.com/docs/ru/hooks-guide](https://code.claude.com/docs/ru/hooks-guide) | 07.07.2026 | да |
| MCP tools в matcher: паттерн `mcp__<server>__<tool>` | [code.claude.com/docs/ru/hooks-guide](https://code.claude.com/docs/ru/hooks-guide) | 07.07.2026 | да |
| Hook `type: "mcp_tool"` вызывает tool на **уже подключённом** MCP server (без shell subprocess) | [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide) | 07.07.2026 | да |
| `mcp_tool` hooks: поля `server`, `tool`, опционально `input` с `${tool_input.file_path}` и др. | [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide) | 07.07.2026 | да |
| Функция `mcp_tool` hooks добавлена в Claude Code v2.1.118 (релиз 23.04.2026, по community-источникам) | [aiagentsfirst.com/claude-code-hooks-mcp-tool](https://aiagentsfirst.com/claude-code-hooks-mcp-tool) | 07.07.2026 | да (версия — сверить с `claude --version` в QA) |
| CLAUDE.md: project memory в корне или `.claude/CLAUDE.md`; user-level `~/.claude/CLAUDE.md` | [code.claude.com/docs/ru/settings](https://code.claude.com/docs/ru/settings) | 07.07.2026 | да |
| Настройки через `/config`; permissions через `/permissions` | [code.claude.com/docs/ru/settings](https://code.claude.com/docs/ru/settings) | 07.07.2026 | да |
| MCP анонсирован Anthropic 25.11.2024 как open-source стандарт | [anthropic.com/news/model-context-protocol](https://www.anthropic.com/news/model-context-protocol) | 25.11.2024 | да |

**fact-bank.md:** нет записей по Claude Code — все цифры только из таблицы выше.

**Не использовать без оговорки:** «Claude Sonnet 5 / 1M context» из snippets research-serp (DTF/tech-insider) — не подтверждено официальной docs на дату research.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **30–45 минут** пройти путь **install → auth → CLAUDE.md → 1–2 MCP → 1 hook → тестовая автоматизация** (например: hook на PostToolUse + MCP Wordstat/filesystem для сбора семантики или правки файлов), с чеклистом для Windows и macOS.

**Почему отличается от конкурентов:**
- Официальная docs — канон, но разбита на setup/mcp/hooks без «первого pipeline» для автоматизатора.
- DTF/VC — доступ из РФ, мало MCP+hooks.
- Habr — dev-глубина, не B2B «на пальцах».
- **Ковчег:** CLI-агент + MCP + hooks как **операционный слой** рядом с Make/n8n (B02) и Cursor MCP (B03).

**Tone:** Claude Code = «агент в терминале, который сам правит файлы и вызывает ваши инструменты»; MCP = «розетки к Wordstat, GitHub, n8n»; hooks = «автопилот-правила: формат, лог, блок опасных команд».

**H2-каркас (из карточки + research):**
1. Claude Code vs Cursor: когда CLI, когда IDE (таблица выбора)  
2. Установка native install + первый запуск (macOS, Linux, WSL, Windows PowerShell)  
3. Auth Pro/Max, API key, регион — что проверить до MCP  
4. CLAUDE.md + `.claude/settings.json`: память проекта и permissions  
5. MCP: `claude mcp add` + `.mcp.json` (HTTP + stdio), проверка `/mcp`  
6. Hooks: command + `mcp_tool`; пример уведомления или post-edit  
7. Чеклист pipeline install → MCP → hook → headless `-p` / CI  

**Conversion:** max 2× CTA Make/kv-ai; internal: B03, B02; Telegram — 1× если уместно.

---

## 5. Стартовый набор MCP (черновик для writer)

| Server | Зачем автоматизатору | Транспорт | Примечание |
|--------|---------------------|-----------|------------|
| Filesystem MCP | Чтение/запись артеfactов контент-пайплайна в проекте | stdio | Официальный `@modelcontextprotocol/server-filesystem` — проверить README |
| Wordstat MCP (user-mcp-kv) | Спрос и LSI для SEO-статей из Claude Code | stdio/HTTP | Только если reader уже настроил MCP в Cursor/Claude; не выдумывать endpoint |
| GitHub MCP | PR, issues для контент-репо | stdio + PAT | `--env GITHUB_TOKEN=...` |
| n8n / Make | Триггер сценариев после подготовки контента | HTTP webhook MCP или custom | Связка с B02; описать как «следующий шаг», не полный n8n-гайд |

**Рекомендация writer:** один **полный** рабочий пример MCP (filesystem или HTTP Notion из docs), остальное — таблица «что добавить вторым шагом».

---

## 6. FAQ-кандидаты (5–7)

1. **Как установить Claude Code на Windows?** — PowerShell: `irm https://claude.ai/install.ps1 \| iex`; проверка `claude --version`; опционально Git for Windows.  
2. **Нужна ли подписка?** — Да, Pro/Max/Team/Enterprise/Console; free plan не даёт Claude Code.  
3. **Чем Claude Code отличается от Cursor?** — CLI-агент в терминале/CI vs IDE; MCP похож, конфиг другой (`claude mcp` / `.mcp.json` vs `.cursor/mcp.json`).  
4. **Как подключить MCP к Claude Code?** — `claude mcp add --transport http|stdio ...` или `.mcp.json`; проверка `/mcp`.  
5. **Где настроить hooks?** — `~/.claude/settings.json` или `.claude/settings.json`; проверка `/hooks`.  
6. **Что такое mcp_tool hook?** — Вызов MCP tool на событии (PostToolUse и др.) без bash-скрипта.  
7. **Работает ли из России?** — Зависит от доступа к Anthropic и оплаты; не обещать обход; ссылка на актуальные how-to только как «что проверить», без гарантий.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Claude Code 40–60 слов | Lead | «Claude Code — agentic CLI…» |
| Таблица Claude Code vs Cursor | H2-1 | Когда CLI / когда IDE |
| Блок install-команд | H2-2 | bash + PowerShell |
| Пример `.mcp.json` + `claude mcp add` | H2-5 | Код + пояснение `--` |
| Пример hook (Notification или PostToolUse) | H2-6 | JSON settings |
| Workflow | H2-7 | install → auth → CLAUDE.md → MCP → hook → test |
| FAQ 5–7 | Конец | Ответы-действия |

---

## 8. Риски для writer

- Не выдумывать версии Claude Code — «на дату статьи», `claude --version`.  
- Не копировать okhlopkov/habr 1:1.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Min **5** нумерованных шагов + чеклист **10+** пунктов.  
- Без эмодзи; дефис вместо длинного тире.  
- Wordstat-цифры — **только после повторного MCP**; сейчас LSI без объёмов.  
- Регион/оплата — осторожно, без «100% работает из РФ».

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель установит Claude Code (native install), войдёт под Pro/Max, создаст CLAUDE.md и settings, подключит минимум один MCP-сервер через `claude mcp add` или `.mcp.json`, настроит один hook (command или mcp_tool), проверит конфигурацию через `/mcp` и `/hooks`, и выполнит первую тестовую автоматизированную задачу в своём проекте.

**action_outline (для writer):**

1. **Проверить систему:** macOS 13+ / Windows 10 1809+ / Linux; 4 ГБ RAM; интернет; подписка Pro/Max (не free).  
2. **Установить native:** macOS/Linux/WSL — `curl -fsSL https://claude.ai/install.sh | bash`; Windows PowerShell — `irm https://claude.ai/install.ps1 | iex`; опционально Git for Windows.  
3. **Проверить install:** `claude --version`, при ошибках — `claude doctor`; на Windows при `command not found` — PATH/перезапуск терминала.  
4. **Аутентифицироваться:** `claude` в каталоге проекта; browser OAuth; убедиться, что **не** перехватывает `ANTHROPIC_API_KEY`, если нужен лимит подписки.  
5. **Создать CLAUDE.md** с правилами проекта (тон, стек, запреты) и базовый `.claude/settings.json` (permissions / mode).  
6. **Подключить первый MCP:** например `claude mcp add --transport stdio myfs -- npx -y @modelcontextprotocol/server-filesystem /path/to/allowed/dir` **или** HTTP server из docs; для project-scope — `.mcp.json` + одобрение в интерактивном `claude`.  
7. **Проверить MCP:** `claude mcp list`, в сессии `/mcp` — server connected, tools видны.  
8. **Добавить hook:** в `.claude/settings.json` — PostToolUse auto-format **или** Notification desktop **или** `type: "mcp_tool"` на подключённый server; проверить `/hooks`.  
9. **Прогнать pipeline:** тестовый prompt, который использует MCP tool + срабатывание hook; зафиксировать чеклист «готово к CI/headless» (упомянуть `-p` / non-interactive из docs quickstart).

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен — LSI без объёмов |
| Таблица фактов с URL | ✅ (24 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов с оговоркой по Wordstat. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + `conversion-map.md`.
