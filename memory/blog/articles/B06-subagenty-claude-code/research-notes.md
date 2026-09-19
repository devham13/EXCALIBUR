# Research notes — B06 «Как настроить subagents в Claude Code: пошаговая инструкция с готовыми ролями»

**topic_id:** B06  
**slug:** subagenty-claude-code  
**article_mode:** B (how-to)  
**research_date:** 2026-07-08  
**disclaimer:** Все даты, версии и статистика проверены на 08.07.2026.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | Официальная docs (EN) | Канон: frontmatter, приоритеты scope, background/foreground, вложенность 5 уровней, v2.1.198 | Английский; длинная reference без «первый subagent за 10 минут» | Сухой перевод без русских путей и чеклиста |
| 2 | [code.claude.com/docs/ru/sub-agents](https://code.claude.com/docs/ru/sub-agents) | Официальная docs (RU) | Локализация; те же факты про `.claude/agents/` | Reference, не пошаговый onboarding | Копировать структуру 1:1 |
| 3 | [claude.com/blog/subagents-in-claude-code](https://claude.com/blog/subagents-in-claude-code) | Официальный блог Anthropic (07.04.2026) | Когда делегировать; conversational invocation; Skills vs CLAUDE.md vs subagents | Устаревший акцент на `/agents` wizard (удалён в 2.1.198) | Не писать «открой `/agents` wizard» как главный способ |
| 4 | [checkroi.ru/blog/subagenty-claude-code/](https://checkroi.ru/blog/subagenty-claude-code/) | RU how-to 2026 | 7 ролей, сравнение со Skills/Agent Teams | Часть фактов без привязки к changelog; wizard `/agents` | Структуру и таблицу ролей 1:1 |
| 5 | [smyslokod.ru/guides/subagents-dlya-claude-code](https://smyslokod.ru/guides/subagents-dlya-claude-code) | RU гайд | Примеры YAML, практические сценарии | Перегруз nested agents / бюджет без официальных цифр | Цифры про «$47k за 3 дня» — не из fact-bank |
| 6 | [habr.com/ru/companies/otus/articles/1054590/](https://habr.com/ru/companies/otus/articles/1054590/) | RU longread (OTUS) | Объяснение routing по `description`; Dynamic Workflows | Неточности во встроенных агентах (не «code-reviewer из коробки») | Выдуманные built-in роли |
| 7 | [code.claude.com/docs/ru/agents](https://code.claude.com/docs/ru/agents) | Официальная docs: параллель | Матрица subagents vs agent view vs agent teams vs workflows | Не how-to первого subagent | Уход в Agent Teams как основной сюжет |
| 8 | [github.com/anthropics/claude-code/releases/tag/v2.1.198](https://github.com/anthropics/claude-code/releases/tag/v2.1.198) | Changelog (01.07.2026) | Background-by-default; удаление `/agents` wizard; Explore inherits model | Release notes, не tutorial | Новостной формат без шагов |

**Паттерн SERP:** топ — официальная docs Anthropic + англоязычные tutorials (Tembo, MindStudio) + русские SEO-гайды с готовыми ролями. Запрос «как создать subagent claude code» в research-serp.json вернул **0 результатов** — явный пробел для пошагового RU how-to. Конкуренты часто **не обновили** блок про `/agents` wizard (удалён с 2.1.198 от 01.07.2026).

**Intent:** how_to — читатель хочет **создать первый custom subagent**, положить файл в `.claude/agents/`, проверить делегирование, получить 5–7 готовых ролей и понять, когда subagent лучше Skill или Agent Teams.

**Пробел для «Ковчег»:** практический RU-гайд с актуальным workflow **без wizard `/agents`** (v2.1.198+), готовые copy-paste роли, таблица «subagent vs Skill vs slash-command», чеклист безопасности tools/permissions, troubleshooting «агент не подхватился».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в Cloud Agent окружении (нет инструмента `wordstat_get_top_requests`). Точные объёмы спроса из Яндекс Wordstat **не получены**.

**Экспертная семантика (WebSearch + SERP, без выдуманных цифр):**

| Фраза | Оценка спроса | Комментарий |
|-------|---------------|-------------|
| subagents claude code | низкий EN long-tail | primary_query на англ.; в RU-SERP доминируют транслит и «субагенты» |
| claude code субагенты | средний niche | несколько RU-гайдов в топе; Habr OTUS + checkroi + smyslokod |
| как создать subagent claude code | очень низкий / zero SERP | research-serp: 0 results — целевой gap для H2 «первый subagent» |
| claude code agents настройка | средний (широкий) | смешивается с MCP/Hooks/Skills — writer должен сузить к subagents |
| параллельные агенты claude code | средний niche | пересечение с agent teams, worktrees, dynamic workflows |

### LSI для writer (SERP + docs)

- `.claude/agents/`, `~/.claude/agents/`, YAML frontmatter, `name`, `description`
- tools, disallowedTools, model sonnet/haiku/opus, permissionMode
- Explore, Plan, general-purpose (built-in)
- background subagent, Ctrl+B, `/tasks`, v2.1.198
- Agent Teams, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, worktree, isolation
- Skills vs subagents, CLAUDE.md delegation policy
- `/doctor` duplicate names, перезапуск сессии

**SEO-стратегия:** primary «subagents claude code» + RU «субагенты claude code» в lead; secondary «как создать subagent» в H2 шага 1–2; «claude code agents настройка» — в блок сравнения расширений, не размывать фокус.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Subagent — специализированный AI-помощник в **отдельном контекстном окне** с собственным system prompt, tools и permissions; возвращает в основную сессию **только итог** | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Custom subagent — Markdown-файл с YAML frontmatter; обязательные поля **`name`** и **`description`** | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Project scope: `.claude/agents/`; user scope: `~/.claude/agents/` (из settings docs) | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 08.07.2026 | да |
| Приоритет scope (высший → низший): managed settings → `--agents` CLI → `.claude/agents/` → `~/.claude/agents/` → plugin `agents/` | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Project subagents рекомендуется **коммитить в git** для команды | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Встроенные subagents: **Explore**, **Plan**, **general-purpose** (+ helper: statusline-setup, claude-code-guide) | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Explore: read-only (Write/Edit denied); для discovery/search | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Plan: read-only; research в plan mode | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| General-purpose: все tools; сложные multi-step задачи | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Explore и Plan **не загружают** CLAUDE.md и git status родителя (остальные subagents загружают) | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| **`description`** — главный сигнал автоделегирования; писать поведенчески («когда использовать») | [claude.com/blog/subagents-in-claude-code](https://claude.com/blog/subagents-in-claude-code) | 07.04.2026 | да |
| Фраза «Use proactively» в description — документированный сигнал для автовызова | [claude.com/blog/subagents-in-claude-code](https://claude.com/blog/subagents-in-claude-code) | 07.04.2026 | да |
| Родительская сессия **не видит** промежуточные tool calls subagent — только финальный текст | [code.claude.com/docs/en/tools-reference](https://code.claude.com/docs/en/tools-reference) | 08.07.2026 | да |
| Максимальная глубина вложенных subagents: **5 уровней**; лимит фиксирован, не настраивается | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Subagents работают **в одной сессии**; для независимых параллельных сессий — background agents / agent view | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Agent Teams — эксперимент; включается `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`; peer-to-peer, отдельные context windows | [code.claude.com/docs/en/glossary](https://code.claude.com/docs/en/glossary) | 08.07.2026 | да |
| **Claude Code v2.1.198** выпущен **1 июля 2026** | [github.com/anthropics/claude-code/releases/tag/v2.1.198](https://github.com/anthropics/claude-code/releases/tag/v2.1.198) | 01.07.2026 | да |
| С v2.1.198 subagents по умолчанию работают **в background**; foreground — когда результат нужен до продолжения | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| С v2.1.198 команда **`/agents` wizard удалена** — создавать через prompt Claude или правку `.claude/agents/` | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| До v2.1.197 `/agents` открывал wizard с Running/Library tabs | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да (историческая справка) |
| С v2.1.198 built-in **Explore наследует model** основной сессии (на Claude API capped at Opus), не всегда Haiku | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Ctrl+B — отправить running subagent в background; `/tasks` — список фоновых задач | [claude.com/blog/subagents-in-claude-code](https://claude.com/blog/subagents-in-claude-code) | 07.04.2026 | да |
| С v2.1.186 permission prompts background subagents **показываются в main session** (имя subagent в диалоге) | [code.claude.com/docs/en/tools-reference](https://code.claude.com/docs/en/tools-reference) | 08.07.2026 | да |
| Если `~/.claude/agents/` не существовал при старте сессии — **перезапустить Claude Code** после создания | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| С v2.1.196 `/doctor` сообщает о **duplicate agent names** в одном scope | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Skills — on-demand workflows в `.claude/skills/`; subagents — **изолированный контекст**; docs рекомендует Skills когда workflow в main context | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| `--agents` JSON flag — session-only subagents без записи на диск | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Поле `tools`: comma-separated allowlist; если omitted — наследует все tools родителя | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| `background: true` в frontmatter — всегда background; unset + v2.1.198 → Claude выбирает, default background | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |
| Subagents vs Agent Teams vs Dynamic Workflows — сравнительная таблица в RU docs | [code.claude.com/docs/ru/agents](https://code.claude.com/docs/ru/agents) | 08.07.2026 | да |
| Блог Anthropic: сигнал делегирования — **10+ файлов** или **3+ независимых подзадачи** | [claude.com/blog/subagents-in-claude-code](https://claude.com/blog/subagents-in-claude-code) | 07.04.2026 | да |
| `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1` — отключить только built-in Explore/Plan (v2.1.198+) | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) | 08.07.2026 | да |

**Не использовать без оговорки:** «code-reviewer / test-writer из коробки» — в официальных docs built-in только Explore, Plan, general-purpose. Готовые reviewer/test-writer — **custom** шаблоны.

**fact-bank.md:** нет фактов по Claude Code subagents — все цифры только из таблицы выше.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **15–25 минут** создать **первый project-level subagent** в `.claude/agents/`, проверить автоделегирование по `description`, скопировать **5–7 готовых ролей** (reviewer, security, tests, docs, migration-check) и выбрать между subagent / Skill / Agent Teams по таблице — без новостного формата про релиз 2.1.198 (релиз — 1 абзац контекста, не lead).

**Почему отличается от конкурентов:**
- Официальная docs — reference, не onboarding с чеклистом.
- RU-конкуренты часто устарели про `/agents` wizard.
- Habr OTUS путает built-in и custom роли.
- «Ковчег»: copy-paste YAML + troubleshooting + security checklist + актуальный v2.1.198 workflow.

**Tone:** subagent = «отдельная вкладка с задачей, которая возвращает только вывод»; `description` = «кнопка автоделегирования». Без hype про «100 агентов».

**H2-каркас (карточка B06 + research):**
1. Subagents vs Skills vs основной агент: когда делегировать (таблица + рекомендация)
2. Первый subagent: prompt Claude или ручной файл `.claude/agents/` (**не wizard `/agents`** на 2.1.198+)
3. YAML-frontmatter: description, tools, model, permissionMode, memory, background
4. Семь готовых ролей с полными конфигами (copy-paste)
5. Параллель: background default, Ctrl+B, `/tasks`; когда Agent Teams (experimental)
6. CLAUDE.md: политика «всегда reviewer read-only»
7. Чеклист безопасности и troubleshooting
8. FAQ

**Conversion:** max 2× CTA Make/kv-ai если уместно; internal link на B03 (MCP Cursor) при упоминании `mcpServers` в frontmatter.

---

## 5. Готовые роли (черновик для writer — минимальные каноничные конфиги)

| Роль | name | tools (рекомендация) | model | Когда вызывать |
|------|------|----------------------|-------|----------------|
| Code reviewer | code-reviewer | Read, Grep, Glob | sonnet | После правок кода, перед commit |
| Security audit | security-reviewer | Read, Grep, Glob | sonnet | Auth, payments, user data |
| Test writer | test-writer | Read, Write, Edit, Bash, Grep, Glob | sonnet | Новая фича без тестов |
| Doc writer | doc-writer | Read, Write, Edit, Grep, Glob | haiku | README, API docs |
| Migration checker | migration-checker | Read, Grep, Glob, Bash | sonnet | SQL/DB migrations |
| Explore helper | codebase-explorer | Read, Grep, Glob, Bash | haiku | Override Explore на дешёвой модели |
| Plan helper | architecture-planner | Read, Grep, Glob | sonnet | Design before implement |

Writer: дать **полный markdown каждой роли** (frontmatter + body 5–10 строк prompt), не только таблицу.

---

## 6. FAQ-кандидаты (7)

1. **Где хранить subagents?** — `.claude/agents/` (проект, git) или `~/.claude/agents/` (все проекты); managed settings для org.
2. **Как создать subagent в Claude Code 2.1.198+?** — Попросить Claude создать файл или написать `.md` вручную; `/agents` wizard больше не открывается.
3. **Почему Claude не вызывает моего subagent?** — Проверить `description`, перезапуск сессии, `/doctor` на дубликаты имён, явный prompt «Use the X agent».
4. **Чем subagent отличается от Skill?** — Subagent = изолированный context + делегирование; Skill = workflow/instructions on-demand в main или через preload.
5. **Можно ли запускать subagents параллельно?** — Да; с 2.1.198 по умолчанию background; Ctrl+B и `/tasks` для контроля.
6. **Subagents vs Agent Teams?** — Subagents в одной сессии, отчёт родителю; Agent Teams — эксперимент, отдельные сессии + shared task list.
7. **Как ограничить опасные tools?** — Явный `tools` allowlist; `disallowedTools`; read-only reviewer без Write/Edit/Bash.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение subagent 40–60 слов | Lead | «Subagent в Claude Code — …» |
| Таблица subagent vs Skill vs Agent Teams | H2-1 | 3 строки + «делать / не делать» |
| Пример frontmatter + body | H2-2–3 | Блок кода |
| Workflow | H2-2–4 | Выбор scope → файл → test delegation → git commit → parallel |
| 7 готовых ролей | H2-4 | Copy-paste blocks |
| FAQ 7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «subagents claude code», «субагенты claude code», «как создать subagent claude code», «.claude/agents/».

---

## 8. Риски для writer

- **Критично:** не строить статью вокруг `/agents` wizard — с 2.1.198 (01.07.2026) удалён; упомянуть как legacy до 2.1.197.
- Не выдумывать built-in роли кроме Explore/Plan/general-purpose.
- Не копировать checkroi/smyslokod 1:1.
- Объём: 8 500–9 500 знаков (quality-blog).
- Min **5** нумерованных шагов + чеклист **10+** пунктов (utility gate статьи).
- Agent Teams — experimental, не main path.
- Цифры Wordstat — не писать выдуманные «показы/мес».

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст первый custom subagent в `.claude/agents/`, настроит `description` и `tools` для автоделегирования, скопирует 5–7 готовых ролей под свой репозиторий, проверит parallel/background через prompt и `/tasks`, и по таблице выберет subagent вместо Skill или Agent Teams; при сбое пройдёт чеклист (перезапуск, `/doctor`, явный вызов).

**action_outline (для writer):**

1. **Проверить версию Claude Code** (`claude --version`) — ориентир 2.1.198+ (июль 2026); обновить при необходимости (`npm i -g @anthropic-ai/claude-code`).
2. **Выбрать scope:** project `.claude/agents/` (коммит в git) vs user `~/.claude/agents/` (личные роли).
3. **Создать первый файл** `code-reviewer.md`: YAML с `name`, `description` (поведенческий триггер + «Use proactively»), `tools: Read, Grep, Glob`, `model: sonnet`, body = job description reviewer.
4. **Перезапустить сессию**, если каталог agents создавался впервые; проверить `/doctor` на duplicate names.
5. **Протестировать делегирование:** prompt «Use the code-reviewer agent on staged changes» + вариант без имени (проверка auto-routing по description).
6. **Ограничить tools** на read-only ролях (убрать Write, Edit, Bash); для test-writer — явный allowlist.
7. **Добавить 6 остальных ролей** из раздела 5 одним commit; описать в README команды для команды.
8. **Настроить CLAUDE.md** (опционально): политика «code review → read-only subagent».
9. **Параллель:** попросить 2–3 independent subtasks «in parallel»; мониторить `/tasks`; упомянуть Ctrl+B и background-by-default (2.1.198).
10. **Чеклист безопасности:** deny Agent tool если нужно запретить nested spawn; permission prompts в main session; не давать Bash network ролям reviewer.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен; семантика из WebSearch |
| Таблица фактов с URL | ✅ (28 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B06
article_dir: memory/blog/articles/B06-subagenty-claude-code
status: ✅ PASS
utility_verdict: PASS
summary: SERP 8 конкурентов; gap RU how-to + актуальный workflow без /agents wizard (v2.1.198). 28 фактов, 10 action steps, 7 FAQ. Wordstat MCP недоступен.
===
