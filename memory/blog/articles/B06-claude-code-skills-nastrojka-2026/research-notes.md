# Research notes — B06 «Как создать Claude Code skills: пошаговая настройка SKILL.md и кастомных команд»

**topic_id:** B06  
**slug:** claude-code-skills-nastrojka-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-07-09  
**disclaimer:** Все даты, версии и статистика проверены на 09.07.2026.

---

## 1. SERP-обзор (WebSearch, 09.07.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | Официальная docs (RU) | Канон: пути, frontmatter, dynamic context, subagent fork, `/skills` | Длинная; мало «первый skill за 30 мин» на русском | Сухой перевод без чеклиста production |
| 2 | [claude.com/docs/skills/how-to](https://claude.com/docs/skills/how-to) | Официальная docs (Agent Skills) | Структура каталога, лимиты name/description, packaging ZIP | Про Claude.ai upload, не только CLI | Путать лимит 200 символов (Claude.ai) с 1024 (спецификация) без оговорки |
| 3 | [ru.hexlet.io/blog/posts/claudeskills](https://ru.hexlet.io/blog/posts/claudeskills) | RU how-to | 6 блоков сильного skill, тест-кейсы, антипаттерны | Мало про frontmatter v2 (disable-model-invocation, allowed-tools) | Структуру 1:1 |
| 4 | [habr.com/ru/articles/1011524](https://habr.com/ru/articles/1011524/) | RU longread (инженер Anthropic) | Папка ≠ один md, progressive disclosure, pitfalls | Обзорный; не пошаговый SKILL.md с нуля | News-tone «огромный гайд» без action steps |
| 5 | [claudskills.com/learn/writing-a-skill-md-file](https://claudskills.com/learn/writing-a-skill-md-file/) | EN практик | Формула description как trigger, 200–400 символов | EN; community, не канон | Цифры без сверки с docs |
| 6 | [checkroi.ru/blog/claude-code-skills-kak-sozdat](https://checkroi.ru/blog/claude-code-skills-kak-sozdat/) | RU how-to | Примеры SKILL.md, типичные ошибки | Слабее про monorepo / nested skills | Коммерческий CTA |
| 7 | [vc.ru/ai/2863948-claude-skills-nastroika-claude-code](https://vc.ru/ai/2863948-claude-skills-nastroika-claude-code) | RU обзор | Широкая аудитория | Смешивает skills + hooks + MCP без decision tree | Обзор без production checklist |
| 8 | [github.com/anthropics/skills](https://github.com/anthropics/skills) | Официальные примеры + skill-creator | Референс SKILL.md, meta-skill для создания | Не tutorial для новичка | Копировать skill-creator целиком в статью |

**Паттерн SERP:** в англоязычном топе доминируют **подборки** («10 best skills 2026») — listicle без создания своего SKILL.md. В русском топе — смешанные гайды (Hexlet, Habr, vc.ru), но мало одного связного how-to: **выбор механизма → каталог → frontmatter → тест auto-invocation → production (allowed-tools, git, skill-creator eval)**.

**Intent:** how_to — читатель хочет **создать и проверить свой skill**, а не скачать чужой топ-10. Вторичный intent: понять, чем skill отличается от slash command, hooks, subagents, MCP.

**Пробел для «Ковчег»:** пошаговый русский гайд для разработчика/автоматизатора с **рабочим примером** (например summarize-changes из docs), decision tree «когда skill, а не CLAUDE.md/hook», чеклист production и связка с внутренними статьями (hooks, MCP, subagents).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 09.07.2026)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` недоступен в текущем cloud-окружении (в каталоге MCP только Cursor Automation Tools и cursor-cloud). Инструмент `wordstat_get_top_requests` не вызывался. **Точные объёмы спроса не получены** — не использовать выдуманные цифры показов в статье.

**Семантическая оценка (не Wordstat, только для writer):**

| Кластер | Наблюдение из SERP |
|---------|-------------------|
| `claude code skills` | EN-запрос; конкуренция listicle + official docs |
| `как создать skill claude code` | RU how-to intent; в топе Hexlet, docs RU, checkroi |
| `claude code skill md` / `SKILL.md` | Технический long-tail, сильный match с H1 |
| `настройка skills claude code` | Смешан с MCP/hooks в выдаче — нужен decision tree в статье |
| `claude code custom skills` | EN; упор на `.claude/skills/` и community repos |

**LSI для writer (SERP + docs, без частот):**

- claude code skills, SKILL.md, YAML frontmatter, description trigger  
- ~/.claude/skills/, .claude/skills/, slash command, /skill-name  
- disable-model-invocation, allowed-tools, context fork, dynamic context `!`cmd``  
- skill-creator, bundled skills, /skills menu, skillOverrides  
- skills vs hooks vs subagents vs MCP  

**SEO-стратегия:** primary «claude code skills» + RU «как создать skill claude code» в lead/H2; «SKILL.md», «настройка skills claude code» — в подзаголовках и FAQ. Без цифр Wordstat в title/meta.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Skill — каталог с обязательным `SKILL.md`; Claude подключает skill по relevance или через `/skill-name` | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| Custom commands объединены со skills: `.claude/commands/deploy.md` и `.claude/skills/deploy/SKILL.md` оба дают `/deploy` | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) | 09.07.2026 | да |
| Skills следуют открытому стандарту Agent Skills; Claude Code добавляет invocation control, subagents, dynamic context | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) | 09.07.2026 | да |
| Personal skills: `~/.claude/skills/<name>/SKILL.md` — для всех проектов | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| Project skills: `.claude/skills/<name>/SKILL.md` — только для репозитория | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| Имя каталога = команда вызова (`/deploy-staging` из `.claude/skills/deploy-staging/`) | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| При совпадении имён: enterprise > personal > project; project skill перекрывает bundled skill с тем же именем | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| `description` + `when_to_use` обрезаются на **1536 символах** в listing skills | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| Основной `SKILL.md` — **до 500 строк**; детали — в references/scripts/assets | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| `name`: lowercase, цифры, дефисы; **макс. 64 символа**; должно совпадать с именем каталога (Agent Skills spec) | [claude.com/docs/skills/how-to](https://claude.com/docs/skills/how-to) | 09.07.2026 | да |
| Agent Skills spec: description до **1024 символов**; Claude.ai upload — лимит **200 символов** для description | [claude.com/docs/skills/how-to](https://claude.com/docs/skills/how-to) | 09.07.2026 | да (с оговоркой про платформу) |
| `disable-model-invocation: true` — только ручной вызов пользователем | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| `user-invocable: false` — скрыть из `/` menu; Claude может вызывать автоматически | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| `allowed-tools` — инструменты без per-use approval пока skill активен | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| `context: fork` — skill выполняется в изолированном subagent | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| Dynamic context: строка `!`git diff HEAD`` подставляет вывод shell до отправки Claude | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| Live change detection: правки в `~/.claude/skills/` и `.claude/skills/` подхватываются **без перезапуска** сессии | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| Bundled skills: `/code-review`, `/batch`, `/debug`, `/loop`, `/claude-api` (если не отключены `disableBundledSkills`) | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| `/run`, `/verify`, `/run-skill-generator` требуют Claude Code **v2.1.145+** | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| Nested qualified names (`/apps/web:deploy`) — **v2.1.203+** | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| `${CLAUDE_PROJECT_DIR}` в skill body — **v2.1.196+** | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| Стек skills `/code-review /fix-issue 123` — **v2.1.199+** (до 6 skills) | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| Меню `/skills`: Space переключает visibility → `skillOverrides` в `.claude/settings.local.json` | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| Рекомендация: project skills коммитить в git (`.claude/skills/`) | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| skill-creator: `/plugin install skill-creator@claude-plugins-official` для evals и оптимизации description | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| После auto-compaction: re-attach до **5000 tokens** на skill, общий бюджет **25000 tokens** | [code.claude.com/docs/ru/skills](https://code.claude.com/docs/ru/skills) | 09.07.2026 | да |
| skill-creator (Anthropic): делать description «чуть настойчивее» — модель склонна undertrigger skills | [github.com/anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | 09.07.2026 | да |
| Официальные примеры skills — репозиторий `anthropics/skills` на GitHub | [github.com/anthropics/skills](https://github.com/anthropics/skills) | 09.07.2026 | да |

**fact-bank.md:** фактов по Claude Code Skills нет — все утверждения только из таблицы выше.

---

## 4. Decision tree: skill vs другие механизмы (для writer)

| Механизм | Когда использовать | Не использовать когда |
|----------|-------------------|------------------------|
| **SKILL.md** | Повторяемый workflow, чеклист, domain conventions; lazy-load тела skill | Разовый факт про проект → CLAUDE.md |
| **Slash command / skill (legacy `.claude/commands/`)** | То же, что skill; commands без supporting files | Нужны scripts/references → каталог skill |
| **Hooks** | Детерминированные события (PreToolUse, Stop) | Обучение модели «как писать API» |
| **Subagents** | Изоляция контекста, параллельные роли | Простая одношаговая инструкция |
| **MCP** | Внешние API, БД, OAuth-сервисы | Только текстовые правила без tools |

---

## 5. Угол статьи (utility-only, режим B)

**Главный угол:** за **30–45 минут** создать **первый рабочий skill** в `.claude/skills/` или `~/.claude/skills/`, проверить **auto-invocation** по `description`, научиться **ручному вызову** `/skill-name`, добавить **production-поля** (`disable-model-invocation`, `allowed-tools`) и закоммитить в git.

**Почему отличается от конкурентов:**
- Listicle «top 10 skills» не учат писать SKILL.md.
- Habr/vc.ru — широкий обзор экосистемы, не один сквозной workflow.
- Official docs — канон, но без русского «с нуля за полчаса» + чеклист ошибок description.

**Tone:** практик автоматизации; «description = триггер, не реклама»; без hype про «100 skills».

**H2-каркас (карточка B06 + research):**
1. Skills vs hooks vs subagents vs MCP — decision tree (таблица §4)  
2. Где хранить: personal vs project vs plugin; приоритет имён  
3. Анатомия SKILL.md: frontmatter + тело + optional scripts/references  
4. Пошагово: mkdir → SKILL.md → тест auto + manual invoke  
5. Frontmatter production: disable-model-invocation, allowed-tools, context: fork  
6. Dynamic context `!`cmd`` и supporting files  
7. Чеклист production: 5 тест-промптов, git, skill-creator eval, skillOverrides  
8. FAQ (3–5) + internal links  

**Internal links (из карточки):**
- `/subagenty-claude-code/`
- `/claude-code-hooks-nastrojka-2026/`
- `/nastroyka-claude-code-mcp/`

---

## 6. FAQ-кандидаты (5–7)

1. **Где хранятся skills Claude Code?** — `~/.claude/skills/` (глобально) или `.claude/skills/` (проект); nested для monorepo.  
2. **Чем skill отличается от slash command?** — commands merged; skill = каталог + frontmatter + optional files.  
3. **Как вызвать skill вручную?** — `/имя-каталога` или stack `/skill-a /skill-b args` (v2.1.199+).  
4. **Почему Claude не активирует skill автоматически?** — слабый description; усилить триггеры; проверить `disable-model-invocation`; skill-creator eval.  
5. **Сколько строк в SKILL.md?** — до 500 в основном файле; остальное — references/.  
6. **Можно ли без перезапуска?** — да, при правке существующего каталога skills; новый top-level каталог — restart.  
7. **Skill vs MCP?** — skill = инструкции/workflow; MCP = внешние tools/API (ссылка на статью MCP).

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение skill 40–60 слов | Lead | «Claude Code skill — каталог с SKILL.md…» |
| Таблица personal vs project | H2-2 | Путь + кто видит |
| Минимальный SKILL.md (YAML + body) | H2-4 | Блок кода из docs summarize-changes |
| Workflow | H2-4–7 | Идея → каталог → frontmatter → тест → git |
| Decision tree | H2-1 | Таблица skill/hook/subagent/MCP |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «claude code skills», «как создать skill claude code», «SKILL.md», «настройка skills claude code».

---

## 8. Риски для writer

- Не выдумывать версии CLI — указывать «на дату статьи»; версии features — только из таблицы фактов (2.1.145, 2.1.196, 2.1.199, 2.1.203).  
- Не путать лимит description 200 (Claude.ai upload) и 1536 (listing в Claude Code).  
- Не копировать Hexlet/Habr 1:1.  
- Min **5** нумерованных шагов + чеклист **10+** пунктов (utility gate статьи).  
- Не подменять how-to списком «100 лучших skills».  
- Без эмодзи; прямые кавычки.

**Пример skill для статьи (канон):** `summarize-changes` из [official docs](https://code.claude.com/docs/ru/skills) — git diff injection + короткие instructions.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст каталог skill с валидным SKILL.md (frontmatter + инструкции), разместит его в `~/.claude/skills/` или `.claude/skills/`, проверит автоматическую активацию по description и ручной вызов `/skill-name`, настроит при необходимости `disable-model-invocation` и `allowed-tools`, прогонит 3–5 тест-промптов и закоммитит project skill в git.

**action_outline (для writer):**

1. **Выбрать scope:** personal (`~/.claude/skills/`) для всех проектов или project (`.claude/skills/`) для команды — по decision tree §4.  
2. **Сформулировать одну повторяемую задачу** (commit message, code review checklist, deploy prep) — не «всё про проект».  
3. **Создать каталог** `mkdir -p .claude/skills/<skill-slug>/` (kebab-case = будущая команда `/skill-slug`).  
4. **Написать SKILL.md:** YAML `description` с явными trigger phrases + markdown body с numbered steps и форматом выхода; при необходимости одна строка dynamic context `!`cmd``.  
5. **Запустить Claude Code** в корне проекта; проверить skill в `/skills` или `/` autocomplete.  
6. **Тест A (auto):** промпт, совпадающий с description («что изменилось в git?») — skill должен подгрузиться.  
7. **Тест B (manual):** `/skill-slug` — skill выполняется по инструкции.  
8. **Production frontmatter:** для side-effect workflows — `disable-model-invocation: true`; для доверенных git-команд — `allowed-tools: Bash(git *)`; для изоляции — `context: fork`.  
9. **Чеклист:** 5 тест-кейсов, description ≤1536 символов, SKILL.md ≤500 строк, commit `.claude/skills/`, опционально skill-creator eval.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (см. §2) |
| Таблица фактов с URL | ✅ (28 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.
