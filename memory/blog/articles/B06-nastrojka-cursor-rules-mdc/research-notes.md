# Research notes — B06 «Как настроить Cursor Rules: пошаговая инструкция по .mdc-правилам для агента»

**topic_id:** B06  
**slug:** nastrojka-cursor-rules-mdc  
**article_mode:** B (how-to)  
**research_date:** 2026-08-15  
**disclaimer:** Все даты, версии и статистика проверены на 15.08.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch, 15.08.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/docs/rules](https://cursor.com/docs/rules) | Официальная docs (EN) | Канон: `.mdc`, 4 режима, frontmatter-матрица, AGENTS.md, Team Rules, import GitHub | Английский; мало русского troubleshooting | Сухой перевод без сценария «первый .mdc за 30 минут» |
| 2 | [mayai.ru/cursor-rules-nastroyka-proekta](https://mayai.ru/cursor-rules-nastroyka-proekta/) | RU how-to (лендинг/HTML) | Пошаговка, alwaysApply vs globs, Active Rules, Wordstat-цифры | Уклон в контент-завод; часть CTA | Структуру 1:1; quiz-блоки |
| 3 | [habr.com/ru/companies/bothub/articles/1044774](https://habr.com/ru/companies/bothub/articles/1044774/) | RU обзор Cursor 2026 | Rules + MCP + Skills в одном гайде; `/create-rule` | Не dedicated how-to по .mdc; news-формат | Уход в обзор всего Cursor |
| 4 | [insidepc.tech/.../cursorrules-pravila-proekta](https://insidepc.tech/ai/ai-guides/cursorrules-pravila-proekta-nastraivaem-cursor-svoy-stek) | RU longread (июль 2026) | Миграция `.cursorrules`→`.mdc`, диагностика, переименование типов 2026 | Для разработчиков; мало no-code аудитории | Перегруз таблицами без чеклиста |
| 5 | [learncursor.dev/learn/cursor-rules](https://www.learncursor.dev/learn/cursor-rules) | EN how-to | 4 режима, `/create-rule`, типичные причины «не работает» | EN; без русского Active Rules | Копировать формулировки дословно |
| 6 | [morphllm.com/cursor-rules-best-practices](https://www.morphllm.com/cursor-rules-best-practices) | EN best practices 2026 | Таблица frontmatter, anti-patterns, token budget | Коммерческий продукт | Продажный bias |
| 7 | [vibecodingacademy.ai/blog/cursor-rules-complete-guide](https://www.vibecodingacademy.ai/blog/cursor-rules-complete-guide) | EN guide + templates | Миграция с v0.43, 15 шаблонов | Шаблоны под React/Supabase, не автоматизацию | Framework-шаблоны как основной угол |
| 8 | [codehabits.dev/blog/cursor-rules-alwaysapply-globs](https://codehabits.dev/blog/cursor-rules-alwaysapply-globs) | EN troubleshooting | 4 attachment modes, comma-separated globs | Узкий фокус | Только troubleshooting без setup |

**Паттерн SERP:** топ — официальная docs Cursor + EN-гайды 2026 про `.mdc`/globs + русские статьи (mayai, insidepc, Habr). Запрос «cursor rules» (248 показов/мес по вторичным данным) закрыт смесью обзоров и нишевых гайдов; **пробел для «Ковчег»:** пошаговая русская инструкция для автоматизатора/маркетолога — от пустой папки до проверенного `project-overview.mdc` + file-scoped правил + чеклист git, без ухода в «что такое Cursor».

**Intent:** `how_to` — пользователь хочет **создать** `.cursor/rules/*.mdc`, выбрать режим (`alwaysApply` / globs / description / @-mention), **проверить** в Active Rules и **закоммитить** набор. Вторичный intent: миграция с `.cursorrules`, починка «правило молчит».

**Пробел для «Ковчег»:** workflow A→B→C для no-code аудитории; связка с B03 (MCP после rules); чеклист 15 пунктов из карточки темы; troubleshooting YAML/globs на русском.

---

## 2. Яндекс Wordstat

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в Cloud Agent окружении (15.08.2026). Вызов `wordstat_get_top_requests` выполнить не удалось. Точные объёмы из API Яндекс Вордстат **не получены**. Обновление токена (если 401 локально): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (вторичные данные, не верифицированы MCP на дату research)

Источник: [mayai.ru/cursor-rules-nastroyka-proekta](https://mayai.ru/cursor-rules-nastroyka-proekta/) — ссылка на Яндекс Вордстат от **22.06.2026**. Использовать в статье с оговоркой «по данным Wordstat, июнь 2026» или дождаться верификации MCP.

| Фраза | Показы/мес (вторично) |
|-------|----------------------|
| cursor rules | 248 |
| как настроить cursor | 186 |
| cursor rules 1c | 34 |
| cursor directory rules | 13 |
| cursor ai rules | 9 |

**Secondary queries из карточки B06 (LSI для writer, без MCP-цифр):**

- cursor rules настройка  
- .cursor/rules mdc  
- как настроить cursor rules  
- cursor rules примеры  
- alwaysApply cursor rules  
- cursor rules globs  
- project rules cursor  
- AGENTS.md cursor  

**SEO-стратегия:** primary «cursor rules» в H1/lead; «как настроить cursor rules», «.cursor/rules mdc», «cursor rules примеры» — в H2/H3 и FAQ. Long-tail «cursor rules 1c» — один FAQ-пункт или сноска, не в title.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Project Rules хранятся в `.cursor/rules` как `.mdc`, version-controlled | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| Plain `.md` в `.cursor/rules` **игнорируется** rules-системой (нет frontmatter) | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| Четыре UI-типа: Always Apply, Apply Intelligently, Apply to Specific Files, Apply Manually | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| При `alwaysApply: true` globs и description **игнорируются** | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| Несколько glob-паттернов — **через запятую** в одной строке | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| Рекомендация docs: правила **короче 500 строк**; дробить большие | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| Создание: `/create-rule` в Agent или Customize → Rules → Add Rule | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| Import Remote Rule (GitHub) → `.cursor/rules/imported/` | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| `AGENTS.md` — простая markdown-альтернатива без YAML; поддержка вложенных AGENTS.md | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| User Rules: Customize → Rules; **только Agent (Chat)**, не Tab и не Inline Edit (Cmd/Ctrl+K) | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| Team Rules — dashboard, планы Team/Enterprise; glob на Team Rules | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| Приоритет при конфликте: **Team Rules → Project Rules → User Rules** | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| Rules **не влияют** на Cursor Tab и другие AI-фичи кроме Agent | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| LLM не сохраняет память между completions; rules дают persistent context | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| Legacy `.cursorrules` в корне ещё читается, но deprecated; миграция на `.cursor/rules/*.mdc` | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 15.08.2026 | да |
| Deprecated `.cursorrules` в пользу Project Rules — ориентир **~v0.43, конец 2024** | [vibecodingacademy.ai/blog/cursor-rules-complete-guide](https://www.vibecodingacademy.ai/blog/cursor-rules-complete-guide) | 2026 | да (сторонний гайд, не официальный changelog) |
| Репозиторий awesome-cursorrules — **40 592** stars на GitHub | [github.com/PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | 15.08.2026 | да |
| Коллекция шаблонов: [cursor.directory](https://cursor.directory) | [mayai.ru/cursor-rules-nastroyka-proekta](https://mayai.ru/cursor-rules-nastroyka-proekta/) | 22.06.2026 | да |
| Habr-гайд: актуальная версия Cursor **3.6** (лето 2026); rules в `.cursor/rules/` как `.mdc` | [habr.com/ru/companies/bothub/articles/1044774](https://habr.com/ru/companies/bothub/articles/1044774/) | 2026 | да |
| Создание rule через `/create-rule` в чате агента — упомянуто в Habr | [habr.com/ru/companies/bothub/articles/1044774](https://habr.com/ru/companies/bothub/articles/1044774/) | 2026 | да |
| Типичная длина shipped rules — **~8 строк** (community observation) | [learncursor.dev/learn/cursor-rules](https://www.learncursor.dev/learn/cursor-rules) | 28.07.2026 | да (как практика, не SLA) |
| Старые названия типов (Auto Attached, Agent Requested) устарели в 2026 | [insidepc.tech/ai/ai-guides/cursorrules-pravila-proekta-nastraivaem-cursor-svoy-stek](https://insidepc.tech/ai/ai-guides/cursorrules-pravila-proekta-nastraivaem-cursor-svoy-stek) | 25.07.2026 | да |
| «cursor rules» — **248** показов/мес (Wordstat, вторично) | [mayai.ru/cursor-rules-nastroyka-proekta](https://mayai.ru/cursor-rules-nastroyka-proekta/) | 22.06.2026 | да с оговоркой MCP |
| «как настроить cursor» — **186** показов/мес (Wordstat, вторично) | [mayai.ru/cursor-rules-nastroyka-proekta](https://mayai.ru/cursor-rules-nastroyka-proekta/) | 22.06.2026 | да с оговоркой MCP |

**fact-bank.md:** записей по Cursor Rules нет — все факты из таблицы выше.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **30–45 минут** создать рабочий набор Project Rules: каталог `.cursor/rules/`, `00-project-overview.mdc` с `alwaysApply: true` (3–15 пунктов), одно file-scoped правило с `globs`, проверка в **Active Rules**, миграция/отключение legacy `.cursorrules`, коммит в git.

**Почему отличается от конкурентов:**
- Официальная docs — канон, но без русского чеклиста и сценария «автоматизатор без Senior-кода».
- Habr/vibecoderz — обзор всего Cursor, не focused how-to по `.mdc`.
- EN-гайды не закрывают русский intent «как настроить cursor rules».
- «Ковчег»: практик автоматизации, связка rules → MCP (internal B03), anti-pattern «400 строк alwaysApply».

**Tone:** rules = «стикер на мониторе для агента»; `.mdc` = markdown + YAML-шапка; Tab и Agent — разные каналы. Без снобизма.

**H2-каркас (из карточки B06 + research):**
1. Cursor Rules vs `.cursorrules`: что изменилось и зачем мигрировать  
2. Создание `.cursor/rules/` и первого `.mdc` с YAML frontmatter  
3. Четыре режима: alwaysApply, globs, description, @-mention — таблица «когда что»  
4. Пошаговая настройка `project-overview.mdc` + stack-scoped правило  
5. Проверка Active Rules и troubleshooting (YAML, `.md` вместо `.mdc`, globs)  
6. Чеклист 15 пунктов перед коммитом  
7. FAQ + ссылка на B03 MCP  

**Conversion:**
- Internal: [/podklyuchenie-mcp-cursor/](/podklyuchenie-mcp-cursor/) — «rules = как думать, MCP = к чему подключаться»  
- CTA курс Make: max 2× через kv-ai.ru при уместности  
- Шаблоны: cursor.directory, awesome-cursorrules — сжать до 20–40 строк  

---

## 5. FAQ-кандидаты (из faq_hints + SERP)

1. **Как настроить cursor rules?** — папка `.cursor/rules/`, файл `.mdc`, frontmatter, проверка Settings → Rules.  
2. **Чем cursor rules отличается от `.cursorrules`?** — `.mdc` + режимы; legacy файл deprecated.  
3. **Почему правило не применяется?** — не `.mdc`, битый YAML (`---`), неверные globs, `.cursor/rules` как файл, модель Auto.  
4. **Сколько правил можно добавить?** — формально много; practically 1–2 short Always + globs по типам файлов; лимит контекста.  
5. **Влияют ли rules на Tab?** — нет, только Agent (официально).  
6. **User Rules или Project Rules?** — личное vs git; не дублировать.  
7. **AGENTS.md или `.mdc`?** — AGENTS.md без условий; `.mdc` когда нужны globs/alwaysApply.

---

## 6. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Cursor Rules 40–60 слов | Lead | «Cursor Rules — постоянные инструкции для Agent…» |
| Таблица 4 режимов + frontmatter-матрица | H2-3 | alwaysApply / description / globs |
| Пример `project-overview.mdc` | H2-4 | Блок кода с `---` |
| Workflow | H2-2–5 | Папка → .mdc → Settings → Active Rules → git |
| Чеклист 15 пунктов | H2-6 | Маркированный список |
| FAQ 5–7 | Конец | Ответы-действия |

**Целевые формулировки:** «cursor rules», «как настроить cursor rules», «.cursor/rules mdc», «cursor rules примеры».

---

## 7. Риски для writer

- Не выдумывать версию Cursor — «актуально на 15.08.2026»; Habr указывает 3.6 как ориентир.  
- Wordstat-цифры — только с оговоркой «июнь 2026, mayai» или без цифр до MCP.  
- Не копировать mayai/insidepc 1:1.  
- Min **5** нумерованных шагов + чеклист **10+** (карточка: 15).  
- Без эмодзи; utility-only, не news про Cursor 3.x.  
- Не подменять how-to списком «топ-20 rules с GitHub».

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст каталог `.cursor/rules/`, добавит минимум два `.mdc` (общий alwaysApply + file-scoped с globs), проверит срабатывание в Active Rules нового Agent-чата, уберёт конфликт с legacy `.cursorrules` и закоммитит rules в git по чеклисту.

**action_outline (для writer):**

1. **Открыть проект** в Cursor; если есть `.cursorrules` — переименовать в backup (например `.cursorrules.bak`).  
2. **Создать каталог** `.cursor/rules/` в корне репозитория (не файл с таким именем).  
3. **Добавить `00-project-overview.mdc`:** YAML с `alwaysApply: true`, 3–15 пунктов (язык ответов, стек, «спроси перед удалением»).  
4. **Добавить stack-scoped `.mdc`:** `alwaysApply: false` + `globs` под ваши файлы (например `**/*.html` или `**/*.py`).  
5. **Проверить в Customize → Rules**, что оба правила видны с ожидаемым типом (Always / Apply to Specific Files).  
6. **Новый Agent-чат:** спросить «какие правила активны?» — убедиться, что `project-overview` в Active Rules; открыть файл под glob — проверить второе правило.  
7. **Тестовый промпт** без копипаста инструкций («создай секцию hero…» / «добавь функцию…») — сверить diff с правилами.  
8. **Troubleshooting при сбое:** расширение `.mdc`, закрывающий `---`, comma-separated globs, не `.md` в rules-папке.  
9. **Закоммитить** `.cursor/rules/` в git; при необходимости импорт шаблона с [cursor.directory](https://cursor.directory) с сокращением до 20–40 строк.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен; вторичные данные |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.
