# Research notes — B06 «Как настроить hooks в Claude Code: пошаговая инструкция для детерминированной автоматизации»

**topic_id:** B06  
**slug:** claude-code-hooks-nastrojka-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-07-08  
**disclaimer:** Все даты, версии и статистика проверены на 08.07.2026.

---

## 0. Utility gate (тема)

```bash
python3 scripts/excalibur_blog_utility_gate.py --topic-id B06
# → OK UTILITY GATE PASS (search_intent: how_to, article_mode: B)
```

**utility_gate_topic:** PASS (подтверждено скриптом и `research-context.json`).

---

## 1. SERP-обзор (WebSearch + research-serp.json, 9 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | Официальный reference (EN) | Канон: 30 событий, 5 типов handler, exit codes, JSON schema, async/HTTP/MCP | Сухой reference; мало «первый hook за 10 минут» | Перевод таблицы 1:1 без workflow |
| 2 | [code.claude.com/docs/ru/hooks-guide]([PRODUCTION_SITE]/docs/ru/hooks-guide) | Официальный how-to (RU) | Notification, PostToolUse prettier, protect-files, `/hooks`, troubleshooting | Не закрывает production-чеклист команды | Копировать примеры без адаптации под RU-аудиторию автоматизации |
| 3 | [claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more]([PRODUCTION_SITE]/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) | Официальный блог Anthropic | Hooks vs CLAUDE.md/skills: детерминизм, низкий context cost, exit 2 | Обзор «7 методов», без полного settings.json | Новостной тон «что вышло» |
| 4 | [smyslokod.ru/guides/hooks-v-claude-code]([PRODUCTION_SITE]/guides/hooks-v-claude-code) | RU how-to | 7 готовых примеров, settings.json | Мало про enterprise (`allowManagedHooksOnly`) | Структура 1:1 |
| 5 | [checkroi.ru/blog/hooks-claude-code]([PRODUCTION_SITE]/blog/hooks-claude-code/) | RU security | 10 защитных hooks | Узкий security-угол | Fear-mongering без positive workflow |
| 6 | [okhlopkov.com/claude-code-nastrojka-mcp-hooks-skills-2026]([PRODUCTION_SITE]/claude-code-nastrojka-mcp-hooks-skills-2026/) | RU personal setup | Hooks + MCP + skills в одном сетапе | Hooks — часть большого обзора, не фокус | Смешивать MCP/skills как основной контент B06 |
| 7 | [techbytes.app/posts/claude-code-2026-cheat-sheet-hooks-mcp-commands]([PRODUCTION_SITE]/posts/claude-code-2026-cheat-sheet-hooks-mcp-commands/) | EN cheat sheet | Prompt/agent hooks, JSON schema | Cheat sheet ≠ пошаговый гайд | Список команд без шагов |
| 8 | [aiorg.dev/blog/claude-code-hooks]([PRODUCTION_SITE]/blog/claude-code-hooks) | EN examples | 20+ copy-paste configs | EN; смешение lifecycle events без приоритетов | Копипаст без объяснения exit codes |
| 9 | [scalably.io/blog/claude-code-hooks-guide]([PRODUCTION_SITE]/blog/claude-code-hooks-guide) | EN practical | Реальный settings.json, `$CLAUDE_PROJECT_DIR`, matcher | EN; нет RU troubleshooting | Перегруз inline shell в JSON |

**Паттерн SERP:** доминирует **официальная docs** (EN + RU hooks-guide) и англоязычные «complete guide / cheat sheet 2026». Русскоязычные статьи — обзоры с готовыми сниппетами (smyslokod, checkroi, okhlopkov), но редко дают **единый workflow**: первый hook → PreToolUse guard → PostToolUse format → `/hooks` verify → production checklist.

**Intent:** how_to — пользователь хочет **настроить hooks в settings.json**, понять **PreToolUse vs PostToolUse**, заблокировать опасные команды/секреты **детерминированно** (не «попросить Claude в CLAUDE.md»), проверить конфиг через `/hooks`.

**Пробел для «Ковчег»:** пошаговый RU-гайд для разработчика/техлида автоматизации: от `/hooks` или `.claude/settings.json` до **3 рабочих hooks** (format, protect .env, bash guard) + чеклист 10 hooks для команды + troubleshooting exit code 1 vs 2; связка с B03 (MCP — внешние tools; hooks — lifecycle внутри Claude Code).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в текущем окружении Cloud Agent (MCP not found). Точные объёмы показов **не получены** — не использовать выдуманные цифры спроса в статье.

**Экспертная семантика (без Wordstat, для writer):**

| Кластер | Примеры запросов | Роль в статье |
|---------|------------------|---------------|
| Primary EN | claude code hooks | H1, lead, schema |
| RU how-to | настройка hooks claude code, hooks settings.json claude code | H2, FAQ |
| Event-specific | PreToolUse hook claude code, PostToolUse hook | H2-4, H2-3 |
| Смежные (не каннибализировать) | claude code skills, claude code mcp | 1 абзац «чем отличаются» + internal B03 |

**LSI для writer (SERP + docs, без частот):**

- settings.json hooks block, `.claude/settings.json`, `~/.claude/settings.json`, settings.local.json  
- PreToolUse, PostToolUse, Stop, SessionStart, Notification  
- matcher Edit\|Write, Bash, mcp__.*  
- exit code 2, permissionDecision deny, hookSpecificOutput  
- `/hooks` menu, disableAllHooks, allowManagedHooksOnly  
- CLAUDE_PROJECT_DIR, timeout, type command http prompt agent mcp_tool  

**SEO-стратегия:** primary «claude code hooks» в title/lead; secondary RU-фразы — в H2 и FAQ; long-tail PreToolUse — в блок безопасности.

---

## 3. Таблица фактов (цифры только с URL)

| # | Факт | Источник | Дата | Можно в текст |
|---|------|----------|------|---------------|
| 1 | Hooks — user-defined команды, HTTP endpoints или LLM prompts, срабатывающие на события lifecycle Claude Code | [claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more]([PRODUCTION_SITE]/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) | 2026 | да |
| 2 | Семь методов управления поведением Claude Code: CLAUDE.md, rules, skills, subagents, hooks, output styles, appending system prompt | [claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more]([PRODUCTION_SITE]/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) | 2026 | да |
| 3 | Hooks имеют **низкий context cost**: конфиг вне основного контекста; blocking stderr попадает в контекст | [claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more]([PRODUCTION_SITE]/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) | 2026 | да |
| 4 | Для детерминизма («каждый раз после edit — prettier») docs рекомендуют hook, а не инструкцию в CLAUDE.md | [claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more]([PRODUCTION_SITE]/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) | 2026 | да |
| 5 | PreToolUse hook может inspect tool call и **exit code 2** для deny | [claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more]([PRODUCTION_SITE]/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) | 2026 | да |
| 6 | Официальный reference перечисляет **30 hook events** (SessionStart … SessionEnd, включая PreToolUse, PostToolUse, Stop, PreCompact и др.) | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 7 | Пять типов handler: `command`, `http`, `mcp_tool`, `prompt`, `agent` | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 8 | Конфиг hooks: трёхуровневая вложенность — event → matcher group → handler | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 9 | `~/.claude/settings.json` — глобально для всех проектов, не shareable | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 10 | `.claude/settings.json` — project-level, можно коммитить в репозиторий | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 11 | `.claude/settings.local.json` — project-local, gitignored при создании Claude Code | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 12 | Plugin hooks в `hooks/hooks.json` плагина | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 13 | Skills/agents могут объявлять hooks во frontmatter | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 14 | Команда `/hooks` — read-only browser: события, matchers, source layer (User/Project/Local/Plugin/Session/Built-in) | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 15 | `"disableAllHooks": true` временно отключает hooks; managed hooks не отключаются user/project/local disable | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 16 | Enterprise: `allowManagedHooksOnly` блокирует user/project/plugin hooks (кроме force-enabled plugin hooks) | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 17 | PreToolUse срабатывает **до** permission-mode check; `permissionDecision: "deny"` блокирует даже в `bypassPermissions` / `--dangerously-skip-permissions` | [code.claude.com/docs/en/hooks-guide]([PRODUCTION_SITE]/docs/en/hooks-guide) | 08.07.2026 | да |
| 18 | Exit 0: success; JSON на stdout обрабатывается **только** при exit 0 | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 19 | Exit 2: blocking error; stdout/JSON игнорируется; stderr → feedback Claude (PreToolUse блокирует tool) | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 20 | Exit 1 (и другие ≠0, ≠2): **non-blocking** для большинства events — tool всё равно выполнится | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 21 | Нельзя смешивать exit 2 и JSON: при exit 2 JSON игнорируется | [code.claude.com/docs/en/hooks-guide]([PRODUCTION_SITE]/docs/en/hooks-guide) | 08.07.2026 | да |
| 22 | PreToolUse JSON deny: `hookSpecificOutput` + `permissionDecision` (`allow`/`deny`/`ask`/`defer`) + `permissionDecisionReason` | [code.claude.com/docs/en/hooks-guide]([PRODUCTION_SITE]/docs/en/hooks-guide) | 08.07.2026 | да |
| 23 | Несколько PreToolUse hooks: приоритет решений **deny → defer → ask → allow** | [code.claude.com/docs/en/hooks-guide]([PRODUCTION_SITE]/docs/en/hooks-guide) | 08.07.2026 | да |
| 24 | Matcher для tool events: `Bash`, `Edit\|Write`, `mcp__.*` и т.д. | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 25 | Timeout defaults (сек): **600** command/http/mcp_tool; **30** prompt; **60** agent; UserPromptSubmit снижает command/http/mcp_tool до **30**; MessageDisplay — до **10** | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 26 | `$CLAUDE_PROJECT_DIR` / `${CLAUDE_PROJECT_DIR}` — корень проекта; использовать в путях к `.claude/hooks/*.sh` | [code.claude.com/docs/en/hooks-guide]([PRODUCTION_SITE]/docs/en/hooks-guide) | 08.07.2026 | да |
| 27 | PostToolUse пример docs: prettier после Edit\|Write через `jq -r '.tool_input.file_path'` | [code.claude.com/docs/en/hooks-guide]([PRODUCTION_SITE]/docs/en/hooks-guide) | 08.07.2026 | да |
| 28 | protect-files.sh: `exit 2` + stderr при совпадении protected path (.env и др.) | [code.claude.com/docs/en/hooks-guide]([PRODUCTION_SITE]/docs/en/hooks-guide) | 08.07.2026 | да |
| 29 | PermissionRequest hooks **не** срабатывают в non-interactive `-p`; для автomation — PreToolUse | [code.claude.com/docs/en/hooks-guide]([PRODUCTION_SITE]/docs/en/hooks-guide) | 08.07.2026 | да |
| 30 | SessionStart/Setup hooks: только `type: "command"` и `type: "mcp_tool"` | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 31 | Async hooks: только `type: "command"`; `asyncRewake` на exit 2 будит Claude | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |
| 32 | WorktreeCreate: **любой** non-zero exit code aborts создание worktree (исключение из правила «только 2 блокирует») | [code.claude.com/docs/en/hooks]([PRODUCTION_SITE]/docs/en/hooks) | 08.07.2026 | да |

**fact-bank.md:** фактов по Claude Code hooks нет — все утверждения только из таблицы выше и official docs.

**Не использовать без оговорки:** цифры «17 events / 12 events / 30 events» из сторонних блогов (morphllm, claudefa.st) — в статье опираться на **30 events** из official reference; не писать «hooks появились в June 2025» без первичного источника Anthropic.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **20–40 минут** собрать минимальный **production-ready** набор hooks в `.claude/settings.json`: PostToolUse auto-format, PreToolUse protect secrets + bash guard, Notification (или Stop-check), проверить через `/hooks`, понять exit codes и не сломать guardrail exit 1 вместо 2.

**Почему отличается от конкурентов:**
- Official docs — reference, не «первый проектный settings.json с нуля».
- Cheat sheets дают JSON без troubleshooting exit 1/2.
- RU-обзоры смешивают MCP/skills; B06 — **только hooks** + internal link на B03.
- «Ковчег»: фокус на **детерминированных quality gates** для команд автоматизации, не новость про Claude Code.

**Tone:** hooks = «страховой полис на событиях», CLAUDE.md = «памятка модели»; exit 2 = «стоп-кран», exit 1 = «сигнализация без блокировки».

**H2-каркас (из карточки + research):**
1. Hooks vs CLAUDE.md/skills/MCP: когда нужен детерминизм  
2. Где хранить конфиг: global / project / local / managed  
3. PostToolUse: автоформатирование после Edit\|Write  
4. PreToolUse: блокировка Bash и защита .env/credentials  
5. Stop, SessionStart, Notification: контекст, алерты, проверка перед завершением  
6. Production checklist: 10 hooks + `/hooks` + disableAllHooks  
7. Troubleshooting: exit 1 vs 2, JSON wrapper, hook error в transcript  
8. FAQ + workflow-схема PreToolUse → tool → PostToolUse → Stop  

**Conversion:** max 2× CTA курс Make (связка «Claude Code hooks + n8n/Make pipeline»); internal [B03 MCP Cursor](/podklyuchenie-mcp-cursor/).

---

## 5. Черновик готовых hooks (для writer, из official docs)

| Hook | Event | Matcher | Назначение |
|------|-------|---------|------------|
| prettier-format | PostToolUse | Edit\|Write | `jq` + prettier на file_path |
| protect-env | PreToolUse | Edit\|Write (+ Read/Bash при расширении) | `.claude/hooks/protect-files.sh`, exit 2 |
| bash-guard | PreToolUse | Bash | блок `rm -rf`, `drop table` и т.д. |
| desktop-notify | Notification | "" (empty) | osascript / notify-send / PowerShell |
| session-context | SessionStart | startup\|resume | stdout → additionalContext (кратко) |

**Рекомендация writer:** один полный walkthrough (protect-files + prettier), остальные — таблица «добавьте следующим шагом».

---

## 6. FAQ-кандидаты (7)

1. **Что такое hooks в Claude Code?** — Shell/HTTP/MCP/prompt/agent handlers в `settings.json`, срабатывают на lifecycle events; детерминированная автоматизация.  
2. **Как добавить hook в settings.json?** — ключ `"hooks"` → массив по event → matcher → `{ "type": "command", "command": "..." }`; проверить `/hooks`.  
3. **PreToolUse vs PostToolUse?** — PreToolUse **до** tool (может блокировать); PostToolUse **после** успеха (format, audit; не отменяет уже сделанное).  
4. **Почему hook «не блокирует», хотя script падает?** — скорее всего **exit 1**, не 2; для policy enforcement — только exit 2 или JSON deny на exit 0.  
5. **Чем hooks отличаются от skills?** — Skills = инструкции/воркфлоу в контексте; hooks = код вне контекста, гарантированное выполнение на событии.  
6. **Чем hooks отличаются от MCP?** — MCP = внешние tools/данные; hooks = перехват lifecycle внутри Claude Code (ссылка B03).  
7. **Где лежит settings.json для команды?** — `.claude/settings.json` в репо (shareable); личные overrides — `settings.local.json` или `~/.claude/settings.json`.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение hooks 40–60 слов | Lead | «Hooks в Claude Code — …» |
| Таблица расположений settings | H2-2 | global / project / local |
| Пример JSON hooks block | H2-3–4 | PostToolUse + PreToolUse |
| Workflow | H2-3–6 | event → matcher → script → exit code → `/hooks` verify |
| Таблица exit codes | H2-7 | 0 / 2 / other |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «claude code hooks», «настройка hooks claude code», «PreToolUse hook», «hooks settings.json claude code».

---

## 8. Риски для writer

- Не выдумывать количество events — **30** из official reference (08.07.2026).  
- Не копировать aiorg/techbytes 1:1.  
- Min **5** нумерованных шагов + чеклист **10+** пунктов (utility gate статьи).  
- Примеры bash/osascript — давать варианты Linux/macOS/Windows где уместно (docs hooks-guide).  
- Не подменять how-to списком «20 hooks без настройки».  
- Без эмодзи; прямые кавычки.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст или отредактирует `.claude/settings.json` с hooks PostToolUse и PreToolUse, напишет/подключит скрипты в `.claude/hooks/`, проверит конфиг через `/hooks`, корректно заблокирует опасное действие через exit 2 или JSON deny, настроит Notification/SessionStart по необходимости и устранит типичные ошибки (exit 1 вместо 2, неверный matcher, PermissionRequest в `-p` mode).

**action_outline (для writer):**

1. **Выбрать scope конфига:** team hooks в `.claude/settings.json` (commit) vs personal в `~/.claude/settings.json` или `.claude/settings.local.json`.  
2. **Создать каталог** `.claude/hooks/` в корне проекта; `chmod +x` для shell-скриптов.  
3. **Добавить PostToolUse hook** с matcher `Edit|Write`: команда prettier/eslint через `jq -r '.tool_input.file_path'` (пример из hooks-guide).  
4. **Написать `protect-files.sh`:** читать JSON stdin, проверять `tool_input.file_path` / Bash command на `.env`, secrets; при match — stderr + **exit 2**.  
5. **Зарегистрировать PreToolUse** в settings.json: matcher `Edit|Write`, command `"$CLAUDE_PROJECT_DIR/.claude/hooks/protect-files.sh"`.  
6. **Добавить PreToolUse Bash guard** (отдельный matcher `Bash`): блок destructive patterns (`rm -rf`, `drop table`).  
7. **Проверить конфиг:** команда `/hooks` в Claude Code — event, matcher, source layer (Project).  
8. **Прогнать тест:** попросить Claude прочитать `.env` или выполнить blocked command — убедиться в deny и feedback в transcript.  
9. **Опционально:** Notification hook (Linux `notify-send` / Windows toast) и SessionStart hook с кратким `additionalContext`; при CI `-p` — только PreToolUse, не PermissionRequest.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (9) |
| Wordstat MCP | ⚠️ недоступен (сервер не найден) |
| Таблица фактов с URL | ✅ (32 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ (7) |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.
