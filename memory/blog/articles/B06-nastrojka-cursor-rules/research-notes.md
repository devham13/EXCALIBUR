# Research notes — B06 «Как настроить Cursor Rules: пошаговая инструкция по .mdc-файлам в 2026 году»

**topic_id:** B06  
**slug:** nastrojka-cursor-rules  
**article_mode:** B (how-to)  
**research_date:** 2026-06-20  
**disclaimer:** Все даты, версии и статистика проверены на 20.06.2026 (2026 год).

---

## 1. Utility gate (тема)

```bash
python3 scripts/excalibur_blog_utility_gate.py --topic-id B06
# topic B06: PASS — OK UTILITY GATE PASS
```

| Поле | Значение |
|------|----------|
| search_intent | how_to |
| article_mode | B |
| utility_gate preflight | PASS (`utility-gate-topic.json`, `research-context.json`) |

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст папку `.cursor/rules/`, напишет 2–3 рабочих `.mdc`-файла с корректным YAML frontmatter (`alwaysApply`, `globs`, `description`), выберет режим активации под задачу, проверит правило в Agent, мигрирует устаревший `.cursorrules` и починит типичные сбои (битый frontmatter, конфликт форматов, неверные globs).

---

## 2. SERP-обзор (WebSearch, 20.06.2026, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/docs/rules](https://cursor.com/docs/rules) | Официальная docs (EN) | Канон: `.mdc`, 4 типа правил, таблица frontmatter, glob-примеры, Team Rules, AGENTS.md, import | Английский; мало troubleshooting на русском | Сухой перевод без пошагового сценария «с нуля» |
| 2 | [cursor.com/ru/help/customization/rules](https://cursor.com/ru/help/customization/rules) | Официальная help (RU) | New Cursor Rule, миграция `.cursorrules`, CLAUDE.md, приоритет Team > Project > User | Короткая; нет готовых шаблонов под стеки | Копировать 1:1 без расширения |
| 3 | [ru.hexlet.io/blog/posts/cursor-rules](https://ru.hexlet.io/blog/posts/cursor-rules) | RU longread (март 2026) | 4 режима активации, anti-patterns, таблицы «было/стало», проверка чужих rules | Фокус на разработчиков; нет связки Rules+MCP+Agent workflow | Структуру 1:1 |
| 4 | [habr.com/ru/companies/bothub/articles/1044774](https://habr.com/ru/companies/bothub/articles/1044774/) | RU mega-guide Cursor 2026 | Rules в контексте экосистемы (MCP, skills, hooks) | Rules — один из многих разделов, не dedicated how-to | Размывать фокус «всё про Cursor» |
| 5 | [vibecoderz.ru/blog/cursor-rules](https://vibecoderz.ru/blog/cursor-rules) | RU how-to | Практика `.cursor/rules`, стек, примеры | Коммерческий контекст vibecoding | Шаблоны без проверки frontmatter |
| 6 | [baeseokjae.github.io/posts/cursor-rules-advanced-2026](https://baeseokjae.github.io/posts/cursor-rules-advanced-2026/) | EN advanced 2026 | Framework templates, token budget | «5-level system» — неофициальная схема, не канон Cursor | Выдавать неофициальную «5-level» за официальную |
| 7 | [www.morphllm.com/cursor-rules-best-practices](https://www.morphllm.com/cursor-rules-best-practices) | EN best practices 2026 | 4 activation modes, типичные ошибки | Продаёт Morph; часть утверждений про Agent mode vs legacy | Коммерческий bias |
| 8 | [forum.cursor.com/t/how-to-figure-out-why-your-cursor-rules-arent-working/152439](https://forum.cursor.com/t/how-to-figure-out-why-your-cursor-rules-arent-working/152439) | Community troubleshooting | Silent failure при битом YAML; `.mdc` побеждает `.cursorrules` | Community, не SLA Cursor | Как единственный источник без оговорки |

**Паттерн SERP:** топ — официальная docs Cursor + англоязычные «complete guide 2026» + русские обзоры (Hexlet, Habr Bothub, vibecoderz). Запрос «настройка cursor rules» на русском закрыт фрагментарно: есть объяснения формата, но мало **единого пошагового гайда** «создай general.mdc → stack rule с globs → проверь в Agent → миграция → troubleshooting».

**Intent:** how_to — пользователь хочет **настроить** project rules в `.cursor/rules/*.mdc`, понять frontmatter и не перегружать контекст. Вторичный intent: миграция с `.cursorrules`, почему правило «не работает», какие globs ставить под React/Python/Markdown.

**Пробел для Excalibur / Maya AI:** русский **пошаговый** гайд для автоматизаторов и маркетологов с контент-стеком: минимальный набор правил (general + stack + content), таблица режимов активации, чек-лист миграции, troubleshooting frontmatter/globs, связка с **B03** (MCP) — «Rules задают поведение, MCP даёт tools».

---

## 3. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** MCP-сервер `user-mcp-kv` недоступен в текущем Cloud Automation worker (нет `CallMcpTool`, `MCP_KV_TOKEN` не задан в env). Инструмент `wordstat_get_top_requests` для `primary_query: cursor rules` **не вызван**. Точные объёмы спроса **не получены** — цифры ниже не выдумываем. Обновите токен и MCP на worker: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Семантическая карта (из карточки B06 + SERP, без показов)

| Кластер | Запросы | Интент |
|---------|---------|--------|
| Primary EN | cursor rules, cursor rules mdc | how_to, документация формата |
| Primary RU | настройка cursor rules, правила cursor для проекта | пошаговая настройка проекта |
| Long-tail | .cursor/rules примеры, cursor rules alwaysApply, cursor rules globs | шаблоны + troubleshooting |
| Смежный (verified B03 Wordstat) | cursor mcp — **630** показов/мес | экосистема Cursor; перекрёстная ссылка на B03 |

### LSI для writer (FAQ и H2/H3)

- `.cursor/rules`, `.mdc`, YAML frontmatter, `alwaysApply`, `globs`, `description`
- User Rules vs Project Rules vs Team Rules; приоритет Team > Project > User
- Always Apply / Apply Intelligently / Apply to Specific Files / Apply Manually
- миграция `.cursorrules` → `.mdc`; AGENTS.md; CLAUDE.md
- `@rule-name` в чате; `/create-rule`; New Cursor Rule (Cmd/Ctrl+Shift+P)
- glob: `**/*.tsx`, `src/**/*.ts`, comma-separated patterns
- правило не применяется; битый frontmatter; `.mdc` vs `.md`; Agent vs Tab
- cursor rules + MCP workflow (internal: B03)

### FAQ-кандидаты (из Wordstat/SERP hints + карточка)

1. **Как написать cursor rules mdc?** — создать `.cursor/rules/name.mdc`, YAML между `---`, body в Markdown.  
2. **Чем cursor rules отличается от .cursorrules?** — модульные `.mdc` с frontmatter и scoping; legacy файл deprecated.  
3. **Какие globs использовать?** — `**/*.tsx` для React, `**/*.py` для Python, `**/*.md` для контента; несколько паттернов через запятую.  
4. **Почему правило cursor не применяется?** — проверить тип правила, frontmatter, конфликт с `.cursorrules`, Agent vs Tab.  
5. **Что делает alwaysApply: true?** — правило в каждой сессии Agent; globs/description игнорируются (официальная docs).  
6. **Нужен ли перезапуск Cursor?** — изменения в `.mdc` подхватываются без рестарта (community); при сомнении — новый чат Agent.  
7. **Rules работают с Inline Edit (Cmd+K)?** — User Rules не применяются к Inline Edit; Project Rules — только Agent (Chat).

---

## 4. Таблица фактов (цифры только с URL)

| # | Факт | Источник | Дата | Можно в текст |
|---|------|----------|------|---------------|
| 1 | Project rules хранятся в `.cursor/rules` как `.mdc`, version-controlled | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 2 | Plain `.md` в `.cursor/rules` **игнорируется** rules system (нужно `.mdc` с frontmatter) | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 3 | Четыре типа правил: Always Apply, Apply Intelligently, Apply to Specific Files, Apply Manually | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 4 | При `alwaysApply: true` globs и description **игнорируются** | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 5 | При `alwaysApply: false` + `globs` — auto-attach когда matching file in context | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 6 | При `alwaysApply: false` + `description` (без globs) — Agent решает по relevance | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 7 | Без description и globs — правило только при `@`-mention в чате | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 8 | Несколько glob-паттернов — **через запятую** (например `docs/**/*.md, docs/**/*.mdx`) | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 9 | Рекомендация: правила **короче 500 строк**; дробить на composable rules | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 10 | Создание: `/create-rule` в Agent или Settings → Rules, Commands → + Add Rule | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 11 | New Cursor Rule: палитра Cmd/Ctrl+Shift+P; файл сохраняется в `.cursor/rules/` | [cursor.com/ru/help/customization/rules](https://cursor.com/ru/help/customization/rules) | 20.06.2026 | да |
| 12 | `.cursorrules` в корне — **legacy**, скоро перестанет поддерживаться; миграция через Always Apply rule | [cursor.com/ru/help/customization/rules](https://cursor.com/ru/help/customization/rules) | 20.06.2026 | да |
| 13 | Приоритет при конфликте: **Team Rules > Project Rules > User Rules** | [cursor.com/ru/help/customization/rules](https://cursor.com/ru/help/customization/rules) | 20.06.2026 | да |
| 14 | Rules применяются к **Agent (Chat)**; **не** к Tab autocomplete и **не** к Inline Edit | [cursor.com/ru/help/customization/rules](https://cursor.com/ru/help/customization/rules) | 20.06.2026 | да |
| 15 | User Rules **не** применяются к Inline Edit (Cmd/Ctrl+K) | [cursor.com/docs/rules](https://cursor.com/docs/rules) (FAQ) | 20.06.2026 | да |
| 16 | `CLAUDE.md` **всегда** применяется ко всем разговорам, независимо от `alwaysApply` | [cursor.com/ru/help/customization/rules](https://cursor.com/ru/help/customization/rules) | 20.06.2026 | да |
| 17 | Remote rules из GitHub → `.cursor/rules/imported/` | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 18 | Team Rules (Team/Enterprise): glob patterns, enforce toggle, dashboard sync | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 19 | Nested `AGENTS.md` в подпапках — instructions combine, более специфичные побеждают | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 20.06.2026 | да |
| 20 | Битый YAML frontmatter (нет closing `---`) → **silent failure**, правило не загружается | [forum.cursor.com/t/152439](https://forum.cursor.com/t/how-to-figure-out-why-your-cursor-rules-arent-working/152439) | 2026 | да (community) |
| 21 | Если есть и `.cursorrules`, и `.mdc` — **`.mdc` wins silently** | [forum.cursor.com/t/152439](https://forum.cursor.com/t/how-to-figure-out-why-your-cursor-rules-arent-working/152439) | 2026 | да (community) |
| 22 | UC Irvine (март 2026): проанализировано **401** публичный репозиторий с cursor rules | [habr.com/ru/companies/simpleone/articles/1039398](https://habr.com/ru/companies/simpleone/articles/1039398/) | 03.2026 | да |
| 23 | **28,7%** строк в изученных rules-файлах — буквальные дубликаты (copy-paste) | [habr.com/ru/companies/simpleone/articles/1039398](https://habr.com/ru/companies/simpleone/articles/1039398/) | 03.2026 | да |
| 24 | Glob-scoped rules с `alwaysApply: false` активируются при **чтении** matching file агентом, не на старте чата | [forum.cursor.com/t/160133](https://forum.cursor.com/t/glob-pattern-rules-are-never-respected-by-agent/160133) | 2026 | да (community) |

**fact-bank.md:** записей про Cursor Rules нет — все факты только из таблицы выше (+ смежный cursor mcp 630 из B03 research-notes, не дублировать как факт B06 без оговорки).

**Не использовать без оговорки:** «5-level rules system» из сторонних блогов — не официальная терминология Cursor. «`.cursorrules` ignored by Agent mode» — community claim; официально: legacy, deprecated, рекомендуется миграция.

---

## 5. Угол статьи (utility-only, режим B)

**Главный угол:** за **20–40 минут** поднять минимальный набор project rules: `general.mdc` (Always Apply, короткий) + `stack-*.mdc` (globs) + опционально `content.mdc` для markdown/SEO; проверить в Agent; мигрировать `.cursorrules`; связать с MCP (B03) одним workflow-блоком.

**Почему отличается от конкурентов:**
- Официальная docs — канон, но без русского пошагового «сделай сам» и чек-листа миграции.
- Hexlet/Habr — сильные обзоры, но не фокус на автоматизаторе контента + связка Rules→MCP→Agent.
- EN-гайды 2026 — шаблоны под фреймворки, мало RU troubleshooting globs/frontmatter.

**Tone:** «правило = короткая инструкция для Agent, не роман»; alwaysApply — «налог на контекст»; globs — «включать правило только когда Agent трогает нужные файлы».

**H2-каркас (из карточки + research):**
1. Зачем Cursor Rules в 2026: `.mdc` вместо `.cursorrules`  
2. Структура: `.cursor/rules` + frontmatter (`alwaysApply`, `globs`, `description`)  
3. Пошагово: `general.mdc` + правило под стек (React / Python / Markdown)  
4. Режимы активации (таблица 4 типов)  
5. Rules + MCP + Agent: единый workflow  
6. Чек-лист миграции и troubleshooting  

**Conversion:**
- Internal: [B03 MCP Cursor](/podklyuchenie-mcp-cursor/) — max 2×  
- CTA Make/kv-ai.ru — только если уместно (1×), не подменять how-to  

---

## 6. Черновики шаблонов для writer (frontmatter + skeleton)

### general.mdc (Always Apply — короткий)

```md
---
alwaysApply: true
---

- Язык ответов: русский
- Не выдумывать API/версии — проверять docs
- Минимальный diff; не трогать unrelated файлы
```

### react-components.mdc (globs)

```md
---
description: React/TSX components in src
globs: src/**/*.tsx, src/**/*.ts
alwaysApply: false
---

- Named exports, not default
- Co-locate tests next to component
```

### content-markdown.mdc (контент-стек)

```md
---
description: Blog/markdown content rules
globs: **/*.md, content/**/*
alwaysApply: false
---

- Lead: боль + ответ + результат
- Цифры только с источником
```

Writer: показать **полный** пример создания через New Cursor Rule + ручное редактирование файла.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Cursor Rules 40–60 слов | Lead | «Cursor Rules — постоянные инструкции для Agent…» |
| Таблица 4 режимов + frontmatter matrix | H2-4 | Таблица из docs |
| Workflow | H2-5 | Выбор типа → файл `.mdc` → git commit → тест в Agent → @rule |
| Troubleshooting matrix | H2-6 | symptom → fix |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** cursor rules, cursor rules mdc, настройка cursor rules, правила cursor для проекта, .cursor/rules примеры.

---

## 8. Риски для writer

- Не выдумывать версии Cursor — «актуально на 20.06.2026», ссылка на docs.  
- Не копировать baeseokjae/morph 1:1.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Min **5** нумерованных шагов + чеклист **10+** пунктов (utility gate статьи).  
- Community forum facts — с пометкой «по опыту сообщества / не официальный SLA».  
- Не обещать 100% соблюдение rules Agent (Hexlet/Habr: rules — подсказки, не жёсткий компилятор).

---

## 9. action_outline (для writer, 9 шагов)

1. **Проверить legacy:** если в корне есть `.cursorrules` — запланировать миграцию; не править параллельно два формата.  
2. **Создать каталог:** `mkdir -p .cursor/rules` в корне репозитория; добавить в git.  
3. **Создать первое правило:** Cmd/Ctrl+Shift+P → «New Cursor Rule» **или** Settings → Rules, Commands → + Add Rule; имя `general.mdc`.  
4. **Заполнить frontmatter:** для глобальных стандартов — `alwaysApply: true` (короткий body, ≤50 строк).  
5. **Добавить stack-rule:** второй файл с `alwaysApply: false` + `globs` под ваш стек (`**/*.py`, `**/*.tsx`, `**/*.md`).  
6. **Добавить intelligent-rule (опционально):** `description` без globs для редких workflow (деплой, миграции) — Agent подтянет по задаче.  
7. **Проверить в Agent:** новый чат → задача, затрагивающая glob-файл → убедиться, что стиль меняется; при необходимости `@rule-name`.  
8. **Миграция:** скопировать текст из `.cursorrules` в `general.mdc` с `alwaysApply: true`; удалить legacy файл; закоммитить.  
9. **Troubleshooting:** если правило «молчит» — проверить closing `---`, конфликт `.mdc`/`.cursorrules`, тип правила, Agent vs Tab; для globs — паттерн и факт чтения файла агентом.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (см. §3) |
| Таблица фактов с URL | ✅ (24 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B06
article_dir: memory/blog/articles/B06-nastrojka-cursor-rules
status: ✅ PASS
utility_verdict: PASS
summary: Utility gate PASS (how_to, mode B). SERP — 8 конкурентов (cursor.com/docs, ru/help, Hexlet, Habr Bothub, vibecoderz, baeseokjae, Morph, forum). Wordstat MCP недоступен на worker — LSI/FAQ без выдуманных показов; смежный cursor mcp 630 (B03). Угол — RU пошаговый .mdc setup: general + stack globs + 4 режима + миграция .cursorrules + troubleshooting + связка B03 MCP. 24 факта с URL, 9 шагов action_outline, 7 FAQ. Готов к writer.
===
