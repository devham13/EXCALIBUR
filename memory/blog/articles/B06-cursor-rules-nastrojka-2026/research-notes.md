# Research notes — B06 «Как настроить Cursor Rules: пошаговая инструкция по .cursor/rules в 2026 году»

**topic_id:** B06  
**slug:** cursor-rules-nastrojka-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-06-18  
**disclaimer:** Все даты, версии и статистика проверены на 18.06.2026.

---

## 1. SERP-обзор (WebSearch, 18.06.2026; 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | Официальная docs (EN/RU) | Канон: 4 типа правил, таблица frontmatter, globs, Team Rules, AGENTS.md, import GitHub | Английский в EN-версии; мало troubleshooting на русском | Сухой перевод без пошагового «с нуля» |
| 2 | [cursor.com/ru/help/customization/rules](https://cursor.com/ru/help/customization/rules) | Официальная help (RU) | Миграция с `.cursorrules`, User vs Project vs Team, flat vs nested `.cursor/rules/` | Короткая; нет готового стека под автоматизацию контента | Копировать 1:1 без расширения кейсов |
| 3 | [ru.hexlet.io/blog/posts/cursor-rules](https://ru.hexlet.io/blog/posts/cursor-rules) | RU how-to (март 2026) | Анатомия `.mdc`, 4 режима, чеклист проверки чужих rules, примеры frontmatter | Уклон в разработку React/TS; нет n8n/content-seo | Структуру 1:1; спорную цифру «100% наборов с проблемами» без источника |
| 4 | [vibecoderz.ru/blog/cursor-rules](https://vibecoderz.ru/blog/cursor-rules) | RU гайд (май 2026) | Миграция, 4 режима, приоритеты, шаблоны под стеки | «−40–60% токенов» — оценка автора, не официальный Cursor | Цифру экономии токенов как факт Cursor |
| 5 | [forpes.ru/post/231998](https://forpes.ru/post/231998) | RU обзор Cursor 2026 | `/create-rule`, режимы, риск перегруза alwaysApply | Широкий обзор IDE, rules — один блок | News-формат «всё про Cursor» |
| 6 | [selectel.ru/blog/how-to-install-and-configure-cursor-ai](https://selectel.ru/blog/how-to-install-and-configure-cursor-ai/) | RU install + rules | Агент создаёт `.cursor/rules/` через UI; таблица применения | Устаревший акцент на `.cursorrules` в lead | Install-гайд как основа B06 |
| 7 | [medium.com/.../5-level-system](https://medium.com/@vibecodingdirectory/how-to-structure-cursor-rules-in-2026-the-5-level-system-cursor-rules-eaf0df16e8e7) | EN longread 2026 | «5-level system», модульность | Маркетинговый framing; нет RU | Концепцию «5 levels» как канон |
| 8 | [forum.cursor.com/t/documentation-page-schema-undocumented-for-rules/151461](https://forum.cursor.com/t/documentation-page-schema-undocumented-for-rules/151461) | Community + staff | Таблица 4 типов от staff; minimatch для globs; YAML-list для нескольких паттернов | Жалобы на inconsistent AI-generated frontmatter | Community glob hacks как официальная спека |

**Паттерн SERP:** топ — официальная docs Cursor + англоязычные `.mdc`-гайды 2026 + русские longread (Hexlet, VibeCoderz, Selectel). Отдельного русского how-to «настроить cursor rules с нуля за вечер» в топе мало — есть обзоры IDE и «топ-100 rules». Запрос на **пошаговую настройку `.cursor/rules/*.mdc`** с чеклистом коммита — пробел для «Ковчег».

**Intent:** how_to — читатель хочет **создать** папку `.cursor/rules/`, написать первые `.mdc` с корректным YAML-frontmatter, выбрать режим активации, проверить что правило подхватилось в Agent, закоммитить в Git. Вторичный intent: миграция с `.cursorrules`, набор rules под автоматизацию (general + n8n/content-seo).

**Пробел для «Ковчег»:** практический гайд на русском для **автоматизаторов и контент-команды** (не только Senior frontend): минимальный стек rules (general, components/workflows, content-seo), связка с [B03 MCP](/podklyuchenie-mcp-cursor/), чеклист 15 пунктов перед push, troubleshooting «правило не срабатывает».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в среде Cloud Agent (ListMcpResources: Server not found). Инструмент `wordstat_get_top_requests` недоступен. **Точные показы в месяц не получены — цифры спроса в статье не утверждать.**

**Экспертная семантика (без объёмов, для writer):**

| Кластер | Примеры формулировок | Роль в статье |
|---------|---------------------|---------------|
| EN core | cursor rules, cursor rules mdc, .cursor/rules | primary + H1 |
| RU intent | правила cursor ai, настройка cursor rules | secondary в H2/FAQ |
| Смежные | .cursorrules миграция, alwaysApply, globs | LSI в теле и FAQ |
| Связка | cursor rules vs mcp, cursor rules vs skills | FAQ (internal B03) |

**SEO-стратегия:** primary «cursor rules» в title/lead; secondary «cursor rules mdc», «настройка cursor rules», «правила cursor ai» — в H2 и FAQ. Не раздувать title под «топ-100 rules».

---

## 3. Таблица фактов (цифры и утверждения только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Cursor поддерживает 4 типа правил: Project (`.cursor/rules`), User, Team, AGENTS.md | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Project rules — файлы `.mdc` в `.cursor/rules`, под версионным контролем | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Обычный `.md` в `.cursor/rules` **игнорируется** системой rules (нет frontmatter) | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Для plain markdown без frontmatter — альтернатива **AGENTS.md** | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Содержимое правил добавляется **в начало контекста** модели при применении | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Frontmatter: `description`, `globs`, `alwaysApply` — три поля управления активацией | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| `alwaysApply: true` — правило всегда включено; **globs и description игнорируются** | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| `alwaysApply: false` + `globs` — auto-attach при файлах в контексте | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| `alwaysApply: false` + `description` (без globs) — Agent решает по описанию (Apply Intelligently) | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| `alwaysApply: false` без description и globs — только через `@rule` в чате (Manual) | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Создание: **`/create-rule`** в Agent или **Cursor Settings → Rules, Commands → + Add Rule** | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Примеры globs: `*.ts`, `**/*.ts`, `src/**`, `src/**/*.tsx`, несколько паттернов через **запятую** | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Best practice: держать правило **короче 500 строк**; дробить на модульные `.mdc` | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Правила **не влияют** на Cursor Tab и другие AI-функции вне Agent | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| User Rules **не применяются** к Inline Edit (Cmd/Ctrl+K); только Agent (Chat) | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Team Rules — планы **Team и Enterprise**; управление из dashboard Cursor | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Приоритет при конфликте: **Team Rules → Project Rules → User Rules** | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Import Remote Rule (GitHub): файлы попадают в **`.cursor/rules/imported/`** с сохранением относительных путей | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| AGENTS.md поддерживается в **корне и вложенных подкаталогах**; более узкие инструкции имеют приоритет | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| В правилах можно ссылаться на файлы через **`@filename.ts`** и вызывать правила через **`@rule-name`** | [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) | 18.06.2026 | да |
| Файл **`.cursorrules` в корне deprecated**; миграция через New Cursor Rule + Always Apply | [cursor.com/ru/help/customization/rules](https://cursor.com/ru/help/customization/rules) | 18.06.2026 | да |
| User Rules хранятся **локально в настройках Cursor**, не в репозитории | [cursor.com/ru/help/customization/rules](https://cursor.com/ru/help/customization/rules) | 18.06.2026 | да |
| Staff Cursor (forum): 4 типа правил — таблица alwaysApply / globs / description | [forum.cursor.com/t/documentation-page-schema-undocumented-for-rules/151461](https://forum.cursor.com/t/documentation-page-schema-undocumented-for-rules/151461) | 10.02.2026 | да |
| Community (forum): glob-движок — **standard minimatch**; для нескольких паттернов — YAML-list | [forum.cursor.com/t/documentation-page-schema-undocumented-for-rules/151461](https://forum.cursor.com/t/documentation-page-schema-undocumented-for-rules/151461) | 11.02.2026 | да (как community signal, не официальный SLA) |
| Troubleshooting: проверить путь `.cursor/rules/` (не `.cursor/rule/`), целостность `---` frontmatter | [developertoolkit.ai/en/cursor-ide/quick-start/project-rules](https://developertoolkit.ai/en/cursor-ide/quick-start/project-rules/) | 2026 | да |
| Hover **context gauge** у поля ввода — какие rules активны | [developertoolkit.ai/en/cursor-ide/quick-start/project-rules](https://developertoolkit.ai/en/cursor-ide/quick-start/project-rules/) | 2026 | да |

**Не использовать как факт Cursor:** «экономия токенов 40–60%» (vibecoderz.ru — оценка автора); «100% наборов rules с ошибками» (hexlet — без первичного исследования).

**fact-bank.md:** записей по Cursor Rules нет — все факты только из таблицы выше.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **30–45 минут** создать рабочую папку `.cursor/rules/` с **3–4 `.mdc` файлами** (general always-apply + auto-attach по glob + 1 manual), проверить активацию в Agent, мигрировать legacy `.cursorrules` при наличии и **закоммитить** rules в Git с чеклистом из 15 пунктов.

**Почему отличается от конкурентов:**
- Официальная docs — канон, но без сценария «контент-завод / n8n / SEO-воркфлоу».
- EN-гайды и «топ-100 rules» не закрывают русский how-to «настройка cursor rules с нуля».
- Hexlet/VibeCoderz — для разработчиков; «Ковчег» — автоматизатор + связка rules ↔ MCP (B03).

**Tone:** frontmatter = «когда правило включается»; globs = «для каких файлов»; alwaysApply = «в каждый чат или нет». Без Senior-снобизма.

**H2-каркас (из карточки + research):**
1. Зачем Cursor Rules в 2026: миграция `.cursorrules` → `.cursor/rules/*.mdc`
2. Создание первого правила: YAML-frontmatter, globs, alwaysApply без перерасхода контекста
3. Четыре режима активации: Always / Files / Intelligently / Manual (@rule)
4. Набор rules для автоматизации: general, components, n8n-workflows, content-seo
5. Чек-лист 15 пунктов перед коммитом `.cursor/rules` в Git
6. Troubleshooting + FAQ (vs MCP, vs Skills, когда alwaysApply true)

**Conversion (conversion-map.md):**
- CTA курс Make: max 2× — rules + сценарии автоматизации → kv-ai.ru/obuchenie-po-make
- Internal: [B03 MCP](/podklyuchenie-mcp-cursor/) — «rules задают поведение, MCP даёт tools»

---

## 5. Черновик набора rules (для writer, без выдуманных путей)

| Файл | Режим | globs / alwaysApply | Назначение |
|------|-------|---------------------|------------|
| `00-general.mdc` | Always Apply | `alwaysApply: true` | Стек, язык ответов, запреты (≤200 слов) |
| `frontend-components.mdc` | Apply to Files | `globs: src/**/*.tsx` | Стиль UI-компонентов |
| `n8n-workflows.mdc` | Apply to Files | `globs: workflows/**/*.json` | Конвенции n8n / Make-экспорт |
| `content-seo.mdc` | Apply Intelligently | `description: "SEO-статьи, meta, H1-H2, internal links"` | Контент-завод |
| `release-checklist.mdc` | Manual | без globs/description | `@release-checklist` перед релизом |

**Рекомендация writer:** один **полный** пример `00-general.mdc` с frontmatter в статье; остальные — сокращённые блоки или таблица «скопируйте и адаптируйте».

---

## 6. FAQ-кандидаты (5–7)

1. **Чем Cursor Rules отличаются от MCP?** — Rules = постоянные инструкции в контексте; MCP = внешние tools/API. Ссылка B03.
2. **Как написать cursor rules для проекта?** — `.cursor/rules/*.mdc`, frontmatter, commit в git.
3. **Когда ставить alwaysApply: true?** — только глобальный минимум (стек, язык); не для всех rules.
4. **Почему правило не применяется?** — неверный glob, `.md` вместо `.mdc`, нет description для Intelligent mode, проверить context gauge.
5. **Нужно ли удалять .cursorrules?** — после миграции в `.mdc` с Always Apply — да, формат deprecated.
6. **Rules vs AGENTS.md?** — `.mdc` для scoped rules; AGENTS.md для простого markdown без frontmatter.
7. **Rules vs Skills?** — Rules = системные инструкции; Skills = упакованные воркфлоу агента (кратко).

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Cursor Rules 40–60 слов | Lead после H1 | «Cursor Rules — …» |
| Таблица 4 режимов активации | H2-3 | alwaysApply / globs / description |
| Пример `.mdc` с frontmatter | H2-2 | Блок кода + пояснение полей |
| Workflow | H2-2–4 | Создать папку → первый .mdc → test Agent → modular rules → git |
| Чеклист 15 пунктов | H2-5 | Маркированный список |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «cursor rules», «cursor rules mdc», «настройка cursor rules», «правила cursor ai», «.cursor/rules».

---

## 8. Риски для writer

- Не выдумывать показы Wordstat — MCP недоступен.
- Не утверждать «40–60% экономии токенов» без пометки «оценка сообщества».
- Не копировать Hexlet/VibeCoderz 1:1.
- Объём: 8 500–9 500 знаков (quality-blog).
- Min **5** нумерованных шагов + чеклист **10+** (карточка: 15 пунктов).
- Не подменять how-to «топ-100 rules» без шагов настройки.
- Multiple globs: упомянуть comma-separated (docs) и YAML-list (forum) + совет «проверить в context gauge».

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст папку `.cursor/rules/`, напишет первые `.mdc` с корректным YAML-frontmatter, настроит нужный режим активации (always / glob / intelligent / manual), проверит подключение правила в Agent через context gauge или тестовый prompt, соберёт минимальный набор rules под свой стек автоматизации и закоммитит их в Git по чеклисту из 15 пунктов.

**action_outline (для writer):**

1. **Проверить legacy:** если в корне есть `.cursorrules` — запланировать миграцию; новые правила только в `.cursor/rules/*.mdc`.
2. **Создать каталог** `.cursor/rules/` в корне репозитория (или через Cursor Settings → Rules, Commands → + Add Rule / Command Palette «New Cursor Rule»).
3. **Написать первое правило `00-general.mdc`:** frontmatter `alwaysApply: true`, тело ≤200 слов — стек, язык, общие запреты.
4. **Добавить scoped-правило:** второй `.mdc` с `globs` (например `src/**/*.tsx` или `workflows/**/*.json`) и `alwaysApply: false`.
5. **Добавить intelligent-правило:** `.mdc` с детальным `description` (без globs) для редких доменных задач (SEO, API).
6. **Проверить активацию:** открыть Agent, hover context gauge / явный prompt по glob-файлу; при Manual — вызвать `@имя-правила`.
7. **Альтернатива быстрого старта:** команда `/create-rule` в чате Agent с описанием желаемого правила — сверить сгенерированный frontmatter с таблицей docs.
8. **Собрать набор для автоматизации:** general + 1–2 glob-rules под стек (components, n8n/content) + 1 manual checklist; не делать все rules alwaysApply.
9. **Перед git push:** пройти чеклист 15 пунктов (расширение `.mdc`, валидный YAML между `---`, нет секретов в rules, осмысленные имена файлов, `.cursor/rules` в `.gitignore` только если намеренно локально).

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (user-mcp-kv) |
| Таблица фактов с URL | ✅ (24 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + `conversion-map.md`.
