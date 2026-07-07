# Research notes — B06 «Как запустить dynamic workflows в Claude Code: пошаговая инструкция по ultracode и оркестрации субагентов»

**topic_id:** B06  
**slug:** dinamicheskie-workflow-claude-code  
**article_mode:** B (workflow how-to)  
**research_date:** 2026-07-07  
**disclaimer:** Все даты, версии и статистика проверены на 07.07.2026.

---

## 1. SERP-обзор (WebSearch, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | Официальная docs (EN) | Канон: ultracode, `/workflows`, лимиты 16/1000, save, resume, `/config`, permission modes | Английский; длинная справка без «первый запуск за 10 минут» | Сухой пересказ без русского чеклиста и сравнения с subagents |
| 2 | [code.claude.com/docs/ru/workflows](https://code.claude.com/docs/ru/workflows) | Официальная docs (RU) | Локализация терминов; тот же канон | Нет сценариев «аудит legacy-репо маркетолога/автоматизатора» | Копировать 1:1 без практического угла «Ковчег» |
| 3 | [claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) | Product announcement (GA) | Дата релиза, GA, кейс Bun, два способа старта, предупреждение о токенах | News-формат; мало CLI-команд | Новостной lead «вышло обновление» без пошаговых шагов |
| 4 | [buildthisnow.com/.../claude-code-dynamic-workflows](https://www.buildthisnow.com/blog/guide/development/claude-code-dynamic-workflows) | Longread EN (2026) | Примитивы `agent()`, `parallel()`, `pipeline()`, Pro vs Max, alt+w | Неофициальные детали (проверять по docs); EN | Структуру 1:1; спорные цифры без сверки с docs |
| 5 | [developersdigest.tech/.../claude-code-dynamic-workflows-guide](https://www.developersdigest.tech/blog/claude-code-dynamic-workflows-guide) | Гайд 2026 (EN) | Связка v2.1.154, три триггера, `/deep-research` | Пересказ docs | Дублировать без таблицы «workflow vs subagents vs MCP» |
| 6 | [smyslokod.ru/guides/dynamic-workflows-v-claude-code](https://smyslokod.ru/guides/dynamic-workflows-v-claude-code) | RU гайд | Русский intent по H1; пошаговый уклон | Меньше про `/config`, size guideline v2.1.202+ | SEO-клон без уникального чеклиста бюджета |
| 7 | [agentpedia.codes/ru/blog/claude-opus-4-8-claude-code-workflows](https://agentpedia.codes/ru/blog/claude-opus-4-8-claude-code-workflows) | RU how-to | Ключевые слова workflow/ultracode | Слабая привязка к официальным лимитам и permission modes | Перегруз Opus 4.8 без инструкции «сначала узкая задача» |
| 8 | [medium.com/.../effective-claude-code-workflows-in-2026](https://medium.com/data-science-collective/effective-claude-code-workflows-in-2026-what-changed-and-what-works-now-c93ebc6f8f50) | Общий workflow 2026 | CLAUDE.md, /plan, hooks — полезный контекст «до ultracode» | **Не** про dynamic workflows / ultracode | Смешивать «обычный workflow» и «dynamic workflows» в одном H2 без таблицы |

**Паттерн SERP:** по `claude code workflow 2026` топ смешивает **dynamic workflows** (Anthropic GA, май 2026) и **общие практики** Claude Code (CLAUDE.md, hooks, MCP). По русскому H1 — официальная RU-docs + 2–3 нишевых гайда; **нет** одного русского how-to с полным циклом: версия → `/config` → первый ultracode → `/workflows` → save → бюджет/resume.

**Intent:** workflow — пользователь хочет **запустить** dynamic workflow (не просто «работать в Claude Code»): проверить v2.1.154+, включить feature, триггернуть ultracode или фразу «use a workflow», мониторить `/workflows`, сохранить скрипт, не сжечь лимит.

**Пробел для «Ковчег»:** пошаговая инструкция на русском для разработчика/техлида автоматизации: когда ultracode оправдан vs subagents/MCP; первый безопасный прогон на узкой задаче; чеклист токенов и permission; связка с [B03 MCP Cursor](/podklyuchenie-mcp-cursor/) (MCP tools в allowlist до длинного run).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в Cloud run (доступны только Cursor Automation Tools, cursor-cloud). Инструмент `wordstat_get_top_requests` не вызывался — **точные показы/мес не получены**.

**Экспертная семантика (без цифр спроса, для LSI writer):**

| Кластер | Фразы-кандидаты |
|---------|-----------------|
| Core | claude code workflow, claude code ultracode, dynamic workflows claude code |
| Commands | /workflows claude code, /effort ultracode, /deep-research claude code |
| Compare | claude code subagents, agent teams claude code, ultracode vs xhigh |
| Setup | claude code 2.1.154, claude code config dynamic workflows |
| RU long-tail | динамические workflow claude code, как запустить workflow claude code |

**SEO-стратегия:** primary `claude code workflow` в title/lead с уточнением **dynamic workflows**; secondary `claude code ultracode`, `dynamic workflows claude code`, `/workflows` — в H2/H3; не смешивать в title с «CLAUDE.md hooks» без disambiguation.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Dynamic workflows требуют Claude Code **v2.1.154 или новее** | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Фича доступна на всех paid plans, Anthropic API, Bedrock, Google Agent Platform, Microsoft Foundry | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| На **Pro** dynamic workflows включаются в `/config` (строка Dynamic workflows) | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Dynamic workflow — **JavaScript-скрипт**, который Claude пишет под задачу; runtime выполняет в фоне | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Промежуточные результаты хранятся в **переменных скрипта**, не в context window | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Триггер одной задачи: ключевое слово **`ultracode`** в промпте или естественная просьба («use a workflow», «run a workflow») | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| До **v2.1.160** литеральным триггером было слово **`workflow`**; NL-запросы работают в обеих версиях | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| **`/effort ultracode`** = `xhigh` reasoning + автоматическое планирование workflow для substantive tasks | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Ultracode действует **только текущую сессию**; для рутины — `/effort high` | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Ultracode доступен на моделях с поддержкой **`xhigh` effort** | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Мониторинг: команда **`/workflows`**; пауза **`p`**, stop **`x`**, save **`s`** | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Встроенный workflow: **`/deep-research <question>`** — параллельный web research с cross-check | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Save: **`.claude/workflows/`** (проект) или **`~/.claude/workflows/`** (личное) | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Лимит runtime: до **16 concurrent agents**, до **1000 agents total** за run | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Resume после pause — **в той же сессии**; выход из Claude Code → следующий запуск с нуля | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Subagents внутри workflow работают в **`acceptEdits`**; правки файлов auto-approved | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| **`Alt+W`** (Win/Linux) / **Option+W** (macOS) — отменить подсветку ultracode для одного промпта | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Setting **Dynamic workflow size** в `/config` (small/medium/large/unrestricted) — с **v2.1.202+** | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Отключение: toggle в `/config`, `"disableWorkflows": true` в settings, env `CLAUDE_CODE_DISABLE_WORKFLOWS=1` | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Релиз **v2.1.154** (28.05.2026): анонс dynamic workflows + `/workflows` | [github.com/anthropics/claude-code/releases/tag/v2.1.154](https://github.com/anthropics/claude-code/releases/tag/v2.1.154) | 28.05.2026 | да |
| Блог Anthropic: анонс **28 мая 2026**; update — **GA** (generally available) | [claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) | 28.05.2026 | да |
| GA: CLI, Desktop, VS Code extension; Pro/Max/Team/Enterprise; API, Bedrock, Vertex, Foundry | [claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) | 07.07.2026 | да |
| По умолчанию **включено** на Max, Team, Enterprise и при использовании через API | [claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) | 07.07.2026 | да |
| Pro: **opt-in** через `/config` | [claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) | 07.07.2026 | да |
| Dynamic workflows потребляют **существенно больше токенов**, чем обычная сессия — рекомендация начать с scoped task | [claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) | 07.07.2026 | да |
| Первый запуск workflow: показ плана и **запрос подтверждения** (зависит от permission mode) | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Кейс Bun (blog): ~**750 000** строк Rust, **99.8%** тестов, **11 дней** до merge — через dynamic workflows | [claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) | 28.05.2026 | да (как illustrative case, не SLA) |
| С v2.1.196: claims, которые verifier не смог проверить, помечаются **unverified**, не refuted | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |
| Workflow script пишется в `~/.claude/projects/` под сессию; можно diff и relaunch | [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) | 07.07.2026 | да |

**fact-bank.md:** нет строк про Claude Code dynamic workflows — все цифры только из таблицы выше.

**Не использовать без оговорки:** «до 1000 параллельных агентов одновременно» — одновременно max **16**; 1000 — **total per run**. Цифры Bun — кейс Anthropic, не гарантия для читателя.

---

## 4. Сравнение примитивов (для H2 writer)

| | Subagents / Skills | Agent teams | **Dynamic workflows** |
|---|-------------------|-------------|------------------------|
| Кто оркестрирует | Claude по turn | Lead agent | **JS-скрипт + runtime** |
| Где промежуточные данные | Context window | Shared task list | **Script variables** |
| Масштаб | Несколько задач за turn | Handful peers | **Десятки–сотни агентов** |
| Прерывание | Turn restart | Teammates продолжают | **Resumable в сессии** |
| Когда брать | Точечная делегация | Долгие peer-сессии | **Аудит/migration/research на весь repo** |

**MCP и hooks:** MCP расширяет tools агентов; hooks — lifecycle automation. Dynamic workflows **не заменяют** MCP: перед длинным run добавить нужные MCP в allowlist (docs). Internal link: [B03](/podklyuchenie-mcp-cursor/).

---

## 5. Угол статьи (utility-only, режим B)

**Главный угол:** за **20–40 минут** пройти полный цикл: проверка версии → включение в `/config` → первый run через **`ultracode:`** или **`/deep-research`** → мониторинг **`/workflows`** → save скрипта → возврат к **`/effort high`** для рутины.

**Почему не news-post:** фокус на действиях читателя, дата релиза — одна строка контекста, не lead.

**Tone:** «оркестратор = скрипт, не чат»; ultracode — режим для **тяжёлых** задач, не default на весь день.

**H2-каркас (из карточки + research):**
1. Dynamic workflows vs MCP, hooks, subagents: когда нужен ultracode (GA, v2.1.154+)  
2. Проверка версии и включение Dynamic workflows в `/config` (Pro vs Max/Team)  
3. Первый запуск: `ultracode:`, «use a workflow», `/effort ultracode`  
4. Панель `/workflows`: мониторинг, pause, save в `.claude/workflows/`  
5. Сценарии: аудит, migration, `/deep-research`  
6. Чеклист безопасности, бюджета токенов, resume  

**Conversion:** CTA курс Make max 2×; internal B03; Telegram @maya_pro 1× при уместности.

---

## 6. FAQ-кандидаты (5–7)

1. **Что такое ultracode в Claude Code?** — `/effort ultracode`: xhigh + авто-workflow; или ключевое слово `ultracode:` в одном промпте.  
2. **Чем workflow отличается от agent teams?** — Workflow = исполняемый JS-скрипт и runtime; teams = lead + peers в чате.  
3. **Как сохранить workflow для повторного запуска?** — `/workflows` → run → **`s`** → project или home path.  
4. **Сколько токенов тратит dynamic workflow?** — значительно больше обычной сессии; смотреть token totals в `/workflows`; начать с узкой задачи; опционально size guideline в `/config`.  
5. **Какая минимальная версия?** — **v2.1.154+**; проверка `claude --version`.  
6. **Pro vs Max — нужно ли включать вручную?** — Pro: да, `/config`; Max/Team/Enterprise/API: по умолчанию on (Enterprise — admin может выключить).  
7. **Можно ли продолжить после паузы?** — Да, в **той же сессии** через `/workflows` + `p`; новая сессия — с начала.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение dynamic workflow 40–60 слов | Lead | «Dynamic workflow в Claude Code — …» |
| Таблица subagents vs workflows | H2-1 | 5 строк |
| Workflow A→B→C | H2-3–4 | version → config → trigger → /workflows → save |
| Пример промпта ultracode | H2-3 | Блок кода text |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff | BlogPosting + FAQPage |

**Целевые формулировки:** `claude code workflow`, `claude code ultracode`, `dynamic workflows claude code`, `/workflows claude code`.

---

## 8. Риски для writer

- Не путать **dynamic workflows** с общими «Claude Code workflows» (CLAUDE.md, hooks).  
- Не обещать 1000 **parallel** — только 16 concurrent / 1000 total.  
- Ultracode на всю сессию — предупредить о cost; рекомендовать selective `ultracode:` или `/deep-research` для первого раза.  
- Permission: subagents в acceptEdits — явный блок «что может измениться без prompt».  
- Min **5** нумерованных шагов + чеклист **10+** (utility gate статьи).  
- Без эмодзи; дефис вместо длинного тире.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель проверит Claude Code ≥ v2.1.154, включит dynamic workflows в `/config` (если Pro), запустит первый workflow через `ultracode:` или `/deep-research`, отследит прогресс в `/workflows`, при успехе сохранит скрипт в `.claude/workflows/` и вернёт `/effort high` для повседневной работы, понимая лимиты агентов и расход токенов.

**action_outline (для writer):**

1. **Проверить версию:** `claude --version` ≥ **2.1.154**; при необходимости обновить (`claude update` / install script с claude.com).  
2. **Включить feature:** `/config` → **Dynamic workflows** ON (обязательно на **Pro**; на Max/Team/API обычно уже ON).  
3. **Выбрать модель с xhigh** (если планируется `/effort ultracode`); для разового run достаточно ключевого слова **`ultracode:`** в промпте.  
4. **Первый безопасный прогон:** `/deep-research <узкий вопрос>` **или** `ultracode: audit <одна папка>` — не весь monorepo с первого раза.  
5. **Подтвердить план** в CLI (Yes / View raw script); при необходимости **`Ctrl+G`** — просмотр JS-скрипта.  
6. **Мониторинг:** `/workflows` → фазы, token totals; **`p`** pause / **`x`** stop при перерасходе.  
7. **После успеха:** **`s`** → save в `.claude/workflows/` (командный) или `~/.claude/workflows/` (личный).  
8. **Вернуть режим:** `/effort high` — не оставлять ultracode на весь день.  
9. **Опционально:** Dynamic workflow size в `/config` (v2.1.202+) = `small` для экономии; MCP/tools в allowlist **до** длинного run.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ❌ (сервер недоступен; семантика без цифр) |
| Таблица фактов с URL | ✅ (28 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.
