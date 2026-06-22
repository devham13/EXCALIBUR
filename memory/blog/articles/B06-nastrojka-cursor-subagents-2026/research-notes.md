# Research notes — B06 «Как настроить субагентов в Cursor: пошаговое руководство по параллельной работе ИИ-команды»

**topic_id:** B06  
**slug:** nastrojka-cursor-subagents-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-06-22  
**disclaimer:** Все даты, версии и статистика проверены на 22.06.2026.

---

## 1. SERP-обзор (WebSearch, 22.06.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | Официальная docs (EN/RU) | Канон: формат `.cursor/agents/`, YAML, built-in explore/bash/browser, foreground/background, cloud `/in-cloud`, nested 2.5+ | Английский в EN-версии; мало troubleshooting на русском | Сухой перевод без сценария «первая команда агентов» |
| 2 | [cursor.com/changelog/2-4](https://cursor.com/changelog/2-4) | Официальный changelog | Дата релиза 22.01.2026; subagents + skills + image gen в одном пакете | Новостной формат, нет пошаговой настройки | News-угол «вышло обновление» без how-to |
| 3 | [habr.com/ru/articles/971620](https://habr.com/ru/articles/971620/) | RU longread (29K просмотров) | Оркестратор + CLI `agent`/`cursor-agent`; роли аналитик/архитектор/разработчик; «сверху вниз» с тестами | Хак через shell, не официальный Task API; для огромных монореп | Копировать CLI-оркестрацию как «единственный способ» |
| 4 | [habr.com/ru/companies/bothub/articles/1044774](https://habr.com/ru/companies/bothub/articles/1044774/) | RU обзор Cursor 2026 | Субагенты в контексте rules/skills/MCP; hooks `subagentStart`/`subagentStop` | Широкий обзор IDE, subagents — один из блоков | Структуру «всё про Cursor» 1:1 |
| 5 | [khar-ag.ru/docs/cursor-subagents-guide](https://khar-ag.ru/docs/cursor-subagents-guide/) | RU beginner guide | `.cursor/agents/`, frontmatter, отличие от skills | Поверхностно; мало про parallel/file ownership | Пересказ docs без угла автоматизации |
| 6 | [shtruzel.ru/articles/cursor-agent-mode-kak-ispolzovat-2026](https://shtruzel.ru/articles/cursor-agent-mode-kak-ispolzovat-2026) | RU how-to Agent Mode | Async subagents, readonly, дерево субагентов, `/multitask` | Смешивает Cloud Agents, Plan Mode, worktrees — reader теряется | Смешение всех режимов без decision tree |
| 7 | [medium.com/@codeandbird/cursor-subagents-complete-guide](https://medium.com/@codeandbird/cursor-subagents-complete-guide-5853e8d39176) | EN complete guide | Примеры security-auditor, file ownership, worktree conflicts | EN; поле `fast` model — проверить актуальность vs docs 2026 | Устаревшие поля frontmatter без сверки с docs |
| 8 | [dredyson.com/how-to-master-cursor-2-4-subagents](https://dredyson.com/how-to-master-cursor-2-4-subagents-a-complete-step-by-step-beginners-guide-with-real-world-examples/) | EN step-by-step | Пошаговый onboarding, readonly для тестов | JSON-формат конфига (не совпадает с markdown frontmatter docs) | Неверный формат файлов (JSON вместо `.md`) |

**Паттерн SERP:** топ — официальная docs Cursor + changelog 2.4 + русские обзоры Agent Mode. Отдельного русского how-to «настроить первых двух субагентов за 20 минут» почти нет: Habr даёт enterprise-оркестрацию, khar-ag — обзор, shtruzel — смесь режимов. **Пробел:** практический гайд для команды автоматизации (не только Senior-dev): создать reviewer + test-runner, запустить параллельно, не сломать репозиторий.

**Intent:** `how_to` — читатель хочет **создать** кастомных субагентов в `.cursor/agents/`, понять когда Agent делегирует сам vs явный вызов `/name`, и безопасно параллелить независимые задачи.

**Пробел для Excalibur BLOG:** пошаговая настройка **первой ИИ-команды** (2–3 subagent) + таблица «subagents vs Background Agents vs MCP-tools» + связка с [B03 MCP](/podklyuchenie-mcp-cursor/) для аудитории B2B-автоматизации.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 22.06.2026)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в Cloud Worker (нет `mcp.json`, `ListMcpResources` пуст, инструмент `wordstat_get_top_requests` недоступен). **Точные объёмы показов не получены** — цифры в статью не использовать.

**Экспертная семантика (без подстановки чисел):**

| Кластер | Оценка спроса RU | Комментарий |
|---------|------------------|-------------|
| `cursor subagents` (EN primary) | Низкий в Яндексе | Основной трафик — EN-документация и зарубежные гайды |
| `субагенты cursor` | Низкий–средний | Растёт после релиза 2.4 (янв. 2026); русские статьи на Habr/khar-ag |
| `cursor агенты настройка` | Средний | Шире intent — Agent Mode + Cloud Agents, не только subagents |
| `cursor 2.4 subagents` | Низкий | Long-tail, привязка к версии |
| Смежный (из B03) `cursor mcp` | **630 показов/мес** (B03, 11.06.2026) | Перекрёстный кластер «экосистема Cursor» |

### LSI для writer (SERP + docs, без Wordstat-цифр)

- `.cursor/agents/`, YAML frontmatter, `description`, `model: inherit`, `readonly`, `is_background`
- встроенные subagents: explore, bash, browser
- foreground vs background, параллельный запуск, `/verifier`, Task tool
- cloud subagents: `/in-cloud`, `/babysit`, Agents Window
- nested subagents (Cursor 2.5+), resume agent ID, `~/.cursor/subagents/`
- subagents vs skills vs rules vs MCP-tools
- file ownership, git worktrees, merge conflicts при параллели
- оркестратор, мультиагентная разработка, cursor agent mode

**SEO-стратегия:** primary EN «cursor subagents» — в slug/meta и lead; русские H2 «субагенты cursor», «настройка subagents»; secondary «cursor агенты настройка» — в блоке Agent Mode vs subagents. Не раздувать title версией «2.4» — в тексте указать минимальную версию.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Subagents представлены в релизе **Cursor 2.4** | [cursor.com/changelog/2-4](https://cursor.com/changelog/2-4) | 22.01.2026 | да |
| Subagents — независимые агенты для частей задачи родителя; работают **параллельно**, со **своим контекстом**, настраиваются промптами/tools/models | [cursor.com/changelog/2-4](https://cursor.com/changelog/2-4) | 22.01.2026 | да |
| Cursor включает **default subagents** для research codebase, terminal commands, parallel work streams — в editor и CLI | [cursor.com/changelog/2-4](https://cursor.com/changelog/2-4) | 22.01.2026 | да |
| Три **built-in** subagents: **Explore** (поиск по кодовой базе), **Bash** (shell-команды), **Browser** (MCP browser) | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Explore по умолчанию использует **более быструю модель** для параллельных поисков | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Кастомный subagent — markdown-файл с **YAML frontmatter** + промпт в теле | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Проектные subagents: **`.cursor/agents/`** (также `.claude/agents/`, `.codex/agents/` для совместимости) | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Глобальные subagents: **`~/.cursor/agents/`** (и `~/.claude/agents/`, `~/.codex/agents/`) | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| При конфликте имён **проектные** subagents побеждают; `.cursor/` > `.claude`/`.codex` | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Поля frontmatter: `name`, `description`, `model` (default **`inherit`**), `readonly` (default **false**), `is_background` (default **false**) | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| **`readonly: true`** — без прав на редактирование файлов и state-changing shell | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| **`is_background: true`** — subagent в фоне, родитель не блокируется | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| **Foreground** subagent блокирует родителя до завершения; **background** возвращает управление сразу | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Явный вызов: синтаксис **`/name`** в промпте (например `/verifier confirm the auth flow`) | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Параллель: одно сообщение Agent → несколько Task tool calls → subagents **одновременно** | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Поле **`description`** — главный сигнал автоделегирования; фразы «use proactively» / «always use for» усиливают триггер | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Subagents доступны в **editor, CLI и Cloud Agents** | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Cloud handoff: **`/in-cloud`** — задача на cloud VM/branch; **`/babysit`** — итерации по PR | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Cloud subagents берут MCP с **cursor.com/agents** (team config), не из локальной сессии | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Background subagents пишут прогресс в **`~/.cursor/subagents/`** | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Subagents можно **resume** по agent ID после завершения | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| С **Cursor 2.5** subagents могут запускать **дочерних** subagents (есть лимит вложенности; у subagent второго уровня нельзя запускать дальше) | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Subagents **наследуют MCP-tools** родителя (кроме cloud subagents) | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| **5 subagents параллельно ≈ 5× token usage** (независимые context windows) | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Agent Mode **делегирует** subagents для параллельного search/shell/browser; кастомные — через `.cursor/agents/` | [cursor.com/ru/help/ai-features/agent](https://cursor.com/ru/help/ai-features/agent) | 22.06.2026 | да |
| Subagents vs **Skills**: subagents — изоляция контекста и параллель; skills — single-purpose repeatable actions | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Cursor 2.4: hook commands стартуют **40× быстрее** | [cursor.com/changelog/2-4](https://cursor.com/changelog/2-4) | 22.01.2026 | да |
| Cursor 2.4: **async Q&A** — agent задаёт уточняющие вопросы, не останавливая работу | [computerra.ru/334399](https://www.computerra.ru/334399/cursor-2-4-predstavil-subagents-i-vstroennuyu-generatsiyu-izobrazhenij/) | 2026 | да (пересказ релиза) |
| Рекомендация docs: начать с **2–3 focused** subagents, не десятков generic | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Anti-pattern: **50+ vague** subagents с «helps with coding» — Agent не знает когда делегировать | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |
| Model override: admin block, Max Mode required, plan limitation → fallback модели | [cursor.com/docs/subagents](https://cursor.com/docs/subagents) | 22.06.2026 | да |

**Не использовать без оговорки:** JSON-конфиг subagents из dredyson.com — **не канон** (официально только `.md` + YAML). Поле `fast` model из Medium — сверять с актуальным [models reference](https://cursor.com/docs/models-and-pricing); в docs 2026 указаны `inherit` или конкретный model ID.

**fact-bank.md:** нет фактов по Cursor subagents — все цифры только из таблицы выше.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **20–30 минут** создать **двух кастомных субагентов** (code-reviewer readonly + test-runner), положить в `.cursor/agents/`, вызвать явно и параллельно из Agent Mode, понять когда встроенные explore/bash/browser срабатывают сами — без enterprise-оркестратора на CLI.

**Почему отличается от конкурентов:**
- Official docs — канон, но без сценария «первая команда» и troubleshooting merge conflicts.
- Habr 971620 — для монореп через shell-оркестратор, порог входа высокий.
- Обзоры Agent Mode смешивают Cloud Agents, Plan, worktrees — reader не понимает **минимальный** path.
- Excalibur: B2B-язык, связка subagents + MCP (B03), decision table «что выбрать», file ownership перед параллелью.

**Tone:** subagent = «узкий специалист с отдельной памятью»; orchestrator = главный Agent в чате; `description` = «визитка для делегирования». Без обещаний «команда заменит отдел разработки».

**H2-каркас (из карточки + research):**
1. Subagents vs Agent Mode: когда параллелить, когда хватит одного агента  
2. Встроенные explore/bash/browser — что уже работает без настройки  
3. Структура `.cursor/agents/`: YAML frontmatter (таблица полей)  
4. Пошагово: reviewer (readonly) + test-runner (proactive description)  
5. Явный `/name` vs автоделегирование + parallel prompt  
6. Оркестрация: file ownership, worktrees, stop parent → stop children  
7. Subagents vs Background Agents vs MCP-tools (comparison table)  
8. Troubleshooting: subagent не в Task tool, wrong model, token/cost  
9. FAQ + чеклист перед git commit  

**Conversion:**
- Internal: [B03 MCP](/podklyuchenie-mcp-cursor/), [B02 n8n agents](/avtomatizaciya-n8n-ai-agents/)  
- CTA услуги AI-автоматизации — max 2×, не подменять how-to  

---

## 5. Стартовый набор subagents (черновик для writer)

| Subagent | Файл | readonly | is_background | Зачем |
|----------|------|----------|---------------|-------|
| code-reviewer | `.cursor/agents/code-reviewer.md` | true | false | Аудит PR/диффа без права ломать код |
| test-runner | `.cursor/agents/test-runner.md` | false | false | Запуск тестов после изменений (`description`: use proactively) |
| verifier | `.cursor/agents/verifier.md` | true | false | Проверка «сделано vs заявлено» (паттерн из docs) |

**Рекомендация writer:** в статье **полные** два файла (reviewer + test-runner) с готовым frontmatter; verifier — упомянуть как третий шаг. Коммит `.cursor/agents/` в репозиторий — best practice из docs.

---

## 6. FAQ-кандидаты (5–7)

1. **Как создать субагента в Cursor?** — Markdown в `.cursor/agents/name.md`, YAML frontmatter + инструкции; перезапуск не обязателен (Agent подхватывает из каталога).  
2. **Чем subagents отличаются от Cursor Rules?** — Rules = статический контекст; subagents = отдельное окно + делегирование задач.  
3. **Почему субагент не появляется в Task tool?** — неверный путь/формат файла, не Agent mode, слишком vague `description`, hooks/policy block.  
4. **Нужен ли Cursor 2.4+?** — да, feature с changelog 2.4 (22.01.2026); обновить через Help → About.  
5. **Foreground или background?** — foreground если нужен результат до следующего шага; background для long-running/parallel.  
6. **Subagents vs Skills?** — skills для one-shot процедур; subagents для изоляции контекста и параллели (таблица из docs).  
7. **Можно ли параллелить правки одного файла?** — нет, риск merge conflict; разнести file ownership или sequential.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение subagents 40–60 слов | Lead | «Субагенты в Cursor — …» |
| Таблица frontmatter полей | H2-3 | name/description/model/readonly/is_background |
| Workflow | H2-4–5 | Создать файл → commit → Agent prompt → parallel → review diff |
| Comparison table | H2-7 | subagents / Background Agents / MCP-tools |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «cursor subagents», «субагенты cursor», «настройка subagents cursor», «cursor агенты настройка».

---

## 8. Риски для writer

- Минимальная версия: **Cursor 2.4+** (22.01.2026), nested — **2.5+**; не выдумывать 3.x-only фичи без changelog.  
- Не копировать Habr CLI-оркестратор как основной путь — optional advanced box.  
- Не использовать JSON-формат subagents из сторонних EN-гайдов.  
- Объём: 8 500–9 500 знаков; min **5** нумерованных шагов + чеклист **10+** пунктов.  
- Без эмодзи; дефис вместо длинного тире.  
- Цифры Wordstat — **не писать** (MCP недоступен); token 5× — только из docs.  
- Каннибализация B03: B06 = subagents; MCP = подключение серверов, cross-link 1–2×.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст папку `.cursor/agents/`, настроит двух кастомных субагентов с YAML frontmatter (reviewer readonly + test-runner), вызовет их явно через `/name` и параллельно из Agent Mode, поймёт разницу со встроенными explore/bash/browser и не запустит параллельные правки одних и тех же файлов без plan file ownership.

**action_outline (для writer):**

1. **Обновить Cursor** до 2.4+ (Help → About или автообновление); включить **Agent mode** в чате.  
2. **Проверить built-in subagents:** дать Agent задачу на поиск по репо + shell — убедиться, что explore/bash срабатывают без ручной настройки.  
3. **Создать `.cursor/agents/`** в корне проекта (или `~/.cursor/agents/` для всех проектов).  
4. **Первый subagent — code-reviewer:** `code-reviewer.md`, `readonly: true`, чёткий `description` («Use when reviewing diffs/PRs»), промпт с чеклистом security/style.  
5. **Второй subagent — test-runner:** `test-runner.md`, `description` с «use proactively», инструкции run tests → fix → re-run.  
6. **Явный тест:** промпт `/code-reviewer проверь последние изменения` — проверить, что subagent стартует и не редактирует файлы.  
7. **Параллельный тест:** одно сообщение «Review API changes and update tests in parallel» — убедиться в двух Task/subagent потоках.  
8. **Background (опционально):** для long task выставить `is_background: true`; прогресс смотреть через `~/.cursor/subagents/`.  
9. **Закрепить в git:** commit `.cursor/agents/`; перед параллелью развести **file ownership**; internal link на B03 если subagent использует MCP-tools.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (без выдуманных цифр) |
| Таблица фактов с URL | ✅ (28 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B06
article_dir: memory/blog/articles/B06-nastrojka-cursor-subagents-2026
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 конкурентов (cursor docs/changelog 2.4, Habr 971620/1044774, khar-ag, shtruzel, Medium, dredyson). Wordstat MCP недоступен — цифры не использованы. Угол — за 20–30 мин создать reviewer + test-runner в .cursor/agents/, parallel + /name, comparison subagents vs Background vs MCP. 28 фактов с URL, 9 шагов action_outline, 7 FAQ. Готов к writer.
===
