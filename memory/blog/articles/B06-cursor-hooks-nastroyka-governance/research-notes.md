# Research notes — B06 «Как настроить Cursor Hooks: пошаговая инструкция для governance cloud-агентов»

**topic_id:** B06  
**slug:** cursor-hooks-nastroyka-governance  
**article_mode:** B (how-to)  
**research_date:** 2026-08-26  
**disclaimer:** Все даты, версии и статистика проверены на 26.08.2026.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | Официальная docs (EN) | Канон: hooks.json, cloud matrix, failClosed, matcher, API input/output | Английский; мало governance-сценариев для Cloud Agents на русском | Сухой перевод без пошагового «с нуля» |
| 2 | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | Официальная docs Cloud | Какие hooks работают в cloud, read-only фаза, project vs user hooks | Нет готовых скриптов guardrails | Копировать таблицу без практики |
| 3 | [dzen.ru — Нейро Алекс](https://dzen.ru/a/akLZoBe30xWLi9SG) | RU how-to (2026) | hooks.json, failClosed, matcher regex, audit, troubleshooting | Уклон в IDE; cloud-ограничения описаны фрагментарно | Структуру 1:1; «один hook на вечер» как единственный метод |
| 4 | [dreaming.press — Govern Cursor Agent](https://dreaming.press/posts/how-to-govern-cursor-agent-with-hooks.html) | EN longread | deny-only guardrails, shell/MCP gate, audit trail | Без Cloud Agents governance; EN | Пересказ без cloud-матрицы |
| 5 | [gist.github.com/alejo4373](https://gist.github.com/alejo4373/ea9bc4dc47c0d13ab64a926b5e44019f) | Технический референс | Разделение hooks vs permissions.json vs cli-config.json | User-level paths; не cloud-first | Путать hooks с permissions.json |
| 6 | [cursor.com/docs/reference/third-party-hooks](https://cursor.com/docs/reference/third-party-hooks) | Официальная docs | Claude Code совместимость, priority order, exit code 2 | Не про governance cloud | Уход в миграцию Claude Code как основной угол |
| 7 | [forum.cursor.com — hooks permissions](https://forum.cursor.com/t/hooks-return-allow-but-mcp-tool-still-requires-manual-approval-gets-skipped/155434) | Community / support | `allow`/`ask` не override MCP approval; только `deny` надёжен | Баг-репорты, не гайд | Обещать auto-approve через hooks |
| 8 | [graftsoul.com RU notes](https://www.grafsoul.com/ru/notes/agenty-programmisty-i-avtomatizatsiya-razrabotki-2026/cursor-nastroyte-rules-skills-hooks-run-modes-i-worktrees) | RU обзор 2026 | Hooks в контексте Rules/Skills/MCP | Обзор, не пошаговый governance для cloud | Обзорный формат без action_outline |

**Паттерн SERP:** топ — официальная docs Cursor + англоязычные security-guides + один русский практический пост (Дзен). Запрос «как настроить cursor hooks» почти не закрыт отдельным русским how-to с фокусом на **Cloud Agents + governance** (commit hooks в repo, audit, subagent guardrails).

**Intent:** how_to — пользователь хочет **создать и включить** `.cursor/hooks.json`, написать скрипты guardrails, заблокировать опасные shell-команды, залогировать действия агента и применить политику к **Cloud Agents** через репозиторий (не через `~/.cursor/`).

**Пробел для «Ковчег»:** пошаговый русский гайд «repo-first governance»: один минимальный hooks.json → shell guard → audit log → cloud-ограничения (какие hooks работают в VM, что **не** работает) → troubleshooting через Hooks output channel. Язык для тимлида/DevOps и автоматизатора, не только Senior IDE-user.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 26.08.2026)

⚠️ **WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` не подключён в Cloud Agent environment (проверено через GetDynamicTools, 26.08.2026). Инструмент `wordstat_get_top_requests` недоступен. Scout зафиксировал ту же проблему.

**Точные объёмы спроса не получены.** Не выдумывать цифры. Для ручной проверки после подключения MCP:

| Запрос для Wordstat | Назначение |
|---------------------|------------|
| как настроить cursor hooks | primary_query |
| cursor hooks | head term |
| cursor hooks.json | secondary |
| beforeShellExecution cursor | secondary (техн.) |
| beforeMCPExecution cursor | secondary (техн.) |
| cursor hooks governance | secondary (EN-RU mix) |
| cursor automations hooks | смежный (cloud) |

### LSI для writer (из SERP + карточки B06, без Wordstat-цифр)

- cursor hooks, hooks.json, `.cursor/hooks.json`, version 1  
- beforeShellExecution, beforeMCPExecution, afterShellExecution, afterMCPExecution  
- preToolUse, postToolUse, subagentStart, subagentStop, stop  
- failClosed, permission deny, matcher regex, exit code 2  
- governance cloud agents, audit trail, guardrails, allowlist MCP  
- Customize → Hooks, Hooks output channel, trusted workspace  
- permissions.json vs hooks (разные слои)  
- team hooks enterprise dashboard  

**SEO-стратегия:** primary «как настроить cursor hooks» в H1/lead; secondary «cursor hooks.json», «beforeShellExecution», «cursor hooks governance» — в H2/H3. Технические matcher-термины — в блоки кода и FAQ, не в title целиком.

**Смежный спрос (из B03 research, для контекста, не подставлять как hooks-цифры):** «cursor mcp» — 630 показов/мес (B03, 11.06.2026). Hooks — более узкий long-tail; ожидаемо ниже head «cursor mcp».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Hooks — скрипты, которые наблюдают, контролируют и расширяют agent loop; конфиг в `hooks.json` на уровне проекта или пользователя | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Hooks — spawned processes, stdio, JSON in/out | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Проектный конфиг: `.cursor/hooks.json`; пользовательский: `~/.cursor/hooks.json` | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Схема конфига: `"version": 1` | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Приоритет источников (высший → низший): Enterprise → Team → Project → User | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Project hooks: пути скриптов от корня проекта, напр. `.cursor/hooks/script.sh` | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| User hooks: пути от `~/.cursor/`, напр. `./hooks/script.sh` | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Только `beforeShellExecution` и `beforeMCPExecution` возвращают permission decision (allow/deny/ask) | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| По умолчанию сбой hook (crash, timeout, invalid JSON) — **fail-open** (действие проходит) | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| `failClosed: true` на объекте hook — при сбое **блокировать** действие; рекомендуется для security-critical hooks | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Exit code `2` от command hook = block (эквивалент `permission: "deny"`) | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| `matcher` для `beforeShellExecution` — regex по **полной строке shell-команды** | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Per-hook опции: `timeout` (сек), `loop_limit` (default 5 для stop/subagentStop), `failClosed`, `matcher` | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Отладка: вкладка Hooks в **Customize** + output channel **Hooks** | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Cursor следит за `hooks.json` и перезагружает при save; при проблемах — restart Cursor | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Cloud agents подхватывают **project hooks** из `.cursor/hooks.json` в репозитории | [cursor.com/docs/hooks#cloud-agent-support](https://cursor.com/docs/hooks#cloud-agent-support) | 26.08.2026 | да |
| User-level hooks (`~/.cursor/hooks.json`) **недоступны** в cloud agents (нет доступа к home VM) | [cursor.com/docs/hooks#cloud-agent-support](https://cursor.com/docs/hooks#cloud-agent-support) | 26.08.2026 | да |
| Cloud agents: только **command-based** hooks; prompt-based не поддерживаются | [cursor.com/docs/hooks#cloud-agent-support](https://cursor.com/docs/hooks#cloud-agent-support) | 26.08.2026 | да |
| Cloud: hooks **не выполняются** в read-only фазе; стартуют после writable environment | [cursor.com/docs/hooks#cloud-agent-support](https://cursor.com/docs/hooks#cloud-agent-support) | 26.08.2026 | да |
| Cloud **поддерживает**: beforeShellExecution, afterShellExecution, beforeReadFile, afterFileEdit, preToolUse, postToolUse, postToolUseFailure, subagentStart, subagentStop, beforeSubmitPrompt, preCompact, afterAgentResponse, afterAgentThought, stop | [cursor.com/docs/hooks#cloud-agent-support](https://cursor.com/docs/hooks#cloud-agent-support) | 26.08.2026 | да |
| Cloud **не поддерживает**: sessionStart, sessionEnd, beforeMCPExecution, afterMCPExecution, Tab hooks, workspaceOpen | [cursor.com/docs/hooks#cloud-agent-support](https://cursor.com/docs/hooks#cloud-agent-support) | 26.08.2026 | да |
| Enterprise: team/enterprise hooks через [dashboard](https://cursor.com/dashboard/team-content?section=hooks) | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Project hooks требуют **trusted workspace** для запуска | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| `beforeMCPExecution` input включает `mcp_server_name`, `tool_name`, `tool_input` | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| `afterShellExecution` получает `command`, `output`, `duration` (ms) — для audit | [cursor.com/docs/hooks](https://cursor.com/docs/hooks) | 26.08.2026 | да |
| Third-party: Claude Code hooks из `.claude/settings.json` при включённых Third-party skills | [cursor.com/docs/reference/third-party-hooks](https://cursor.com/docs/reference/third-party-hooks) | 26.08.2026 | да |
| `~/.cursor/permissions.json` — IDE auto-run allowlists; **отдельно** от hook scripts | [gist.github.com/alejo4373](https://gist.github.com/alejo4373/ea9bc4dc47c0d13ab64a926b5e44019f) | 26.08.2026 | да |
| `~/.cursor/cli-config.json` — permissions **CLI** agent; не Desktop hook pipeline | [gist.github.com/alejo4373](https://gist.github.com/alejo4373/ea9bc4dc47c0d13ab64a926b5e44019f) | 26.08.2026 | да |
| Known limitation (forum): hooks **deny** работает; `allow` не override MCP approval flow | [forum.cursor.com/t/155434](https://forum.cursor.com/t/hooks-return-allow-but-mcp-tool-still-requires-manual-approval-gets-skipped/155434) | 2026 | да (community, не SLA) |
| Known limitation: `permission: "ask"` для shell/MCP часто **не enforced**; для блокировки — только `deny` | [forum.cursor.com/t/155711](https://forum.cursor.com/t/the-cursor-hooks-did-not-execute-as-expected/155711) | 2026 | да (community) |
| Cursor CLI: расширенная поддержка hooks; lifecycle hooks в cloud/CLI — gaps (forum) | [forum.cursor.com/t/148316](https://forum.cursor.com/t/cursor-cli-doesnt-send-all-events-defined-in-hooks/148316) | 2026 | да (community) |
| Cloud Agents overview: hooks из repo для formatters, audit, policy checks | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 26.08.2026 | да |
| Internal link target: B03 MCP подключение — `/podklyuchenie-mcp-cursor/` | blog-topics B06 | 26.08.2026 | да |

**fact-bank.md:** нет фактов по Cursor Hooks — все цифры/утверждения только из таблицы выше.

**Критично для writer (cloud governance):** в Cloud Agents **нельзя** полагаться на `beforeMCPExecution` — hook deferred. MCP-governance для cloud: комбинация `preToolUse` (matcher `MCP:...`), audit через `postToolUse`, плюс MCP allowlist в Settings (B03). Shell-governance в cloud — через `beforeShellExecution` + `failClosed: true`.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **30–45 минут** создать в репозитории минимальный **governance-стек** для Cursor Agent / Cloud Agent: `.cursor/hooks.json` + 2–3 shell-скрипта (block dangerous shell, audit log, optional subagent guard), закоммитить в git, проверить в Hooks output channel и понимать, что сработает в Cloud VM, а что только локально.

**Почему отличается от конкурентов:**
- Официальная docs — канон, но без русского пошагового «первый hooks.json за вечер» под cloud.
- EN security-posts — IDE-first, без матрицы cloud vs local.
- Дзен-пост близок, но не выстраивает governance pipeline A→B→C для Cloud Agents и subagents.
- «Ковчег»: repo-first policy as code, audit trail, честные ограничения (`deny` only, no MCP hooks in cloud).

**Tone:** hooks = «таможня перед shell/MCP»; `failClosed` = «лучше остановить, чем пропустить rm -rf»; cloud = «только то, что в git, не в home».

**H2-каркас (из карточки + research):**
1. Hooks vs Rules vs MCP allowlist — когда что (таблица решений)  
2. Где лежит конфиг и приоритеты (project для cloud)  
3. Минимальный hooks.json (version 1, один beforeShellExecution)  
4. Скрипт block-dangerous.sh + matcher + failClosed  
5. Audit: afterShellExecution / postToolUse (JSONL лог)  
6. beforeMCPExecution локально + обход для cloud (preToolUse + Settings)  
7. Governance Cloud Agents: subagentStart, read-only фаза, enterprise team hooks  
8. Troubleshooting: Hooks channel, JSON, paths, trusted workspace  
9. FAQ + чеклист перед merge в main  

**Conversion:** CTA max 2× — связка hooks + MCP (internal B03), Make/automation по conversion-map при уместности.

---

## 5. Черновик минимального hooks.json (для writer, из docs)

```json
{
  "version": 1,
  "hooks": {
    "beforeShellExecution": [
      {
        "command": ".cursor/hooks/block-dangerous.sh",
        "matcher": "rm\\s+-rf|git\\s+push\\s+--force|npm\\s+publish",
        "timeout": 30,
        "failClosed": true
      }
    ],
    "afterShellExecution": [
      {
        "command": ".cursor/hooks/audit-shell.sh"
      }
    ],
    "subagentStart": [
      {
        "command": ".cursor/hooks/log-subagent.sh",
        "matcher": "generalPurpose|shell"
      }
    ]
  }
}
```

**Рекомендация writer:** один полный рабочий пример block + audit; MCP-guard — отдельный блок «только IDE» с `beforeMCPExecution` и примечанием про cloud.

---

## 6. FAQ-кандидаты (5–7)

1. **Что такое Cursor Hooks?** — JSON + скрипты в `.cursor/hooks.json`, события agent loop; создать файл и один hook.  
2. **Чем hooks отличаются от Cursor Rules?** — Rules = инструкции модели; hooks = исполняемый код до/после действий (deny/log).  
3. **Как заблокировать shell-команды?** — `beforeShellExecution` + stdout `{"permission":"deny"}` или exit 2 + `failClosed: true`.  
4. **Нужны ли hooks для Cloud Agents?** — да, project hooks в repo; user hooks не работают в cloud.  
5. **Работает ли beforeMCPExecution в Cloud Agent?** — нет (deferred); использовать preToolUse audit + MCP allowlist.  
6. **Hook не срабатывает — что проверить?** — Customize → Hooks, output Hooks, путь `.cursor/hooks/`, chmod +x, trusted workspace, valid JSON.  
7. **Hooks vs permissions.json?** — hooks = policy scripts; permissions.json = IDE allowlist auto-run (см. B03 для MCP).

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Hooks 40–60 слов | Lead после H1 | «Cursor Hooks — …» |
| Таблица Hooks vs Rules vs permissions.json | H2-1 | 3 строки + рекомендация |
| Cloud support matrix (краткая) | H2-7 | Таблица Yes/No из docs |
| Пример hooks.json + block script | H2-3–4 | Код + пояснение полей |
| Workflow | H2-3–7 | Создать → chmod → test → commit → cloud run → audit |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «как настроить cursor hooks», «cursor hooks.json», «beforeShellExecution cursor», «cursor hooks governance».

---

## 8. Риски для writer

- Не обещать auto-approve MCP через `permission: allow` — только deny надёжен (forum).  
- Явно указать: `beforeMCPExecution` **не в cloud** — иначе QA/fact-check fail.  
- Не путать `./hooks/` и `.cursor/hooks/` для project hooks.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Min **5** нумерованных шагов + чеклист **10+** пунктов.  
- Без эмодзи; дефис вместо длинного тире.  
- Не выдумывать Wordstat-цифры — пометка MCP unavailable сохраняется до ручной проверки.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст `.cursor/hooks.json` и скрипты в `.cursor/hooks/`, настроит `beforeShellExecution` с `failClosed` для блокировки опасных команд, добавит audit-log через `afterShellExecution`, закоммитит policy в репозиторий, проверит работу в Hooks output channel и поймёт, какие guardrails применимы к Cloud Agents (project hooks, shell/subagent), а какие только локально (beforeMCPExecution, user hooks).

**action_outline (для writer):**

1. **Создать структуру:** `.cursor/hooks.json` и каталог `.cursor/hooks/` в корне репозитория (не `./hooks/` без `.cursor/`).  
2. **Добавить минимальный конфиг** `"version": 1` с одним `beforeShellExecution`: `command`, `matcher` (regex опасных команд), `timeout: 30`, `failClosed: true`.  
3. **Написать `block-dangerous.sh`:** читать JSON stdin, при match — stdout `{"permission":"deny","user_message":"..."}` и/или exit 2; `chmod +x`.  
4. **Проверить локально:** Customize → Hooks → убедиться, что hook loaded; Output → Hooks — нет ошибок JSON/path.  
5. **Протестировать deny:** попросить Agent выполнить команду из matcher (например `rm -rf`) — команда должна быть заблокирована.  
6. **Добавить audit:** `afterShellExecution` → скрипт append JSONL (command, duration) в `.cursor/hooks/audit.log` или `/tmp` (не секреты в git).  
7. **MCP guard (IDE only):** опционально `beforeMCPExecution` с match по `mcp_server_name`; для cloud описать альтернативу — `preToolUse` matcher `MCP:...` + audit, MCP allowlist из B03.  
8. **Cloud governance:** закоммитить `.cursor/hooks.json` + scripts; убедиться, что workspace trusted; не полагаться на `~/.cursor/hooks.json` для cloud runs.  
9. **Troubleshooting чеклист:** invalid JSON, неверный relative path, hook timeout, fail-open без failClosed, read-only cloud phase без audit на первых turn.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ unavailable (LSI из SERP) |
| Таблица фактов с URL | ✅ (28 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + internal B03.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B06
article_dir: memory/blog/articles/B06-cursor-hooks-nastroyka-governance
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 конкурентов (cursor.com/docs/hooks, cloud-agent, dzen Нейро Алекс, dreaming.press, gist alejo4373, third-party-hooks, forum permissions bugs, graftsoul RU). Wordstat: MCP user-mcp-kv недоступен — точные показы не получены; LSI из SERP. Угол — repo-first governance: hooks.json + block shell (failClosed/deny) + audit + cloud matrix (beforeMCPExecution НЕ в cloud). 28 фактов с URL, 9 шагов action_outline, 7 FAQ. Готов к writer.
===
