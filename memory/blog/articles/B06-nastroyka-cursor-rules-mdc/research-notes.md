# Research notes — B06 «Как настроить Cursor Rules (.mdc): пошаговая инструкция для Agent mode в 2026»

**topic_id:** B06  
**slug:** nastroyka-cursor-rules-mdc  
**article_mode:** B (how-to)  
**research_date:** 2026-09-10  
**disclaimer:** Все даты, версии и статистика проверены на 10.09.2026.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/docs/rules](https://cursor.com/docs/rules) | Официальная docs (EN) | Канон: 4 типа rules, frontmatter-таблица, globs, Team Rules, AGENTS.md, nested AGENTS.md, import GitHub | Мало troubleshooting «rules молчат»; нет миграции .cursorrules пошагово | Сухой перевод без сценария Agent mode |
| 2 | [cursor.com/ru/docs/rules](https://cursor.com/ru/docs/rules) | Официальная docs (RU) | Те же факты на русском; `/create-rule`, Customize → Rules | Короткая FAQ; нет чек-листа миграции за 5 мин | Копировать 1:1 без угла «автоматизация / контент-завод» |
| 3 | [stackhawk.com/blog/cursor-rules/](https://www.stackhawk.com/blog/cursor-rules/) | EN how-to (2026) | Legacy vs .mdc, mkdir, kebab-case, globs vs description, git clone imported | EN; enterprise security bias | Структуру 1:1 |
| 4 | [dev.to/dublecc/how-to-configure-cursor-rules-in-2026](https://dev.to/dublecc/how-to-configure-cursor-rules-in-2026-cursorrules-the-complete-guide-360) | Longread EN (2026) | Иерархия AGENTS.md + .mdc, deprecation .cursorrules, token efficiency | Много «что такое rules», мало RU | News-формат |
| 5 | [design.dev/guides/cursor-rules/](https://design.dev/guides/cursor-rules/) | Гайд EN | 4 activation modes, YAML reference, migration block | Сторонний; расхождение «.md тоже работает» vs официальный «ignored» | Противоречие с docs — держаться cursor.com |
| 6 | [ru.hexlet.io/blog/posts/cursor-rules](https://ru.hexlet.io/blog/posts/cursor-rules) | RU longread | Таблица «было/стало», 4 режима, миграция, примеры frontmatter | Уклон в React/TS для разработчиков | Нишевый dev-фокус как основной угол |
| 7 | [insidepc.tech/.../cursorrules-pravila-proekta](https://insidepc.tech/ai/ai-guides/cursorrules-pravila-proekta-nastraivaem-cursor-svoy-stek) | RU how-to | Сравнение форматов, YAML-поля, «.md ignored» по первоисточнику | Мало Agent mode troubleshooting | — |
| 8 | [mayai.ru/cursor-rules-nastroyka-proekta/](https://mayai.ru/cursor-rules-nastroyka-proekta/) | RU how-to (свой сайт) | Новичковый сценарий, Active Rules, Wordstat-цифры, лендинг/HTML | Уже опубликован; пересечение с B06 | Каннибализация: B06 — **Agent mode + модульная архитектура + миграция за 5 мин + связка с B03 MCP** |

**Паттерн SERP:** топ — официальная docs Cursor + EN-гайды 2026 (.mdc, frontmatter, AGENTS.md) + русские обзоры (Hexlet, insidepc, mayai). Запрос «cursor rules» (248 показов/мес по вторичному источнику) закрыт множеством гайдов, но **узкий intent «Agent mode + .mdc с нуля за 20–40 мин»** на русском с чек-листом миграции и troubleshooting silent YAML — дифференциатор для «Ковчег».

**Intent:** how_to — пользователь хочет **создать** `.cursor/rules/*.mdc`, выбрать режим (`alwaysApply` / `globs` / `description` / manual), **проверить** загрузку в Agent (Active Rules), **мигрировать** с `.cursorrules`, закоммитить в git. Вторичный intent: не перегрузить контекст; не дублировать AGENTS.md.

**Пробел для «Ковчег»:** пошаговый гайд для **автоматизаторов и вайбкодеров** (не только Senior TS): от первого `00-general.mdc` до модульных правил под стек + миграция + тест в Agent + internal link на B03 (MCP). Язык «на пальцах», без 400 строк в одном alwaysApply.

---

## 2. Яндекс Wordstat

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` / инструмент `wordstat_get_top_requests` недоступен в среде Cloud Agent (namespace не подключён). Точные объёмы из API **не получены**.

**Вторичный источник** (цитата из опубликованного RU-гайда с указанием Wordstat, дата сбора автора — 22.06.2026): [mayai.ru/cursor-rules-nastroyka-proekta/](https://mayai.ru/cursor-rules-nastroyka-proekta/)

| Фраза | Показы/мес | Примечание |
|-------|------------|------------|
| cursor rules | 248 | primary_query |
| как настроить cursor | 186 | LSI, близкий intent |
| cursor rules 1c | 34 | отраслевой long-tail |
| cursor directory rules | 13 | шаблоны / cursor.directory |
| cursor ai rules | 9 | узкий синоним |

**Семантика (экспертная оценка без API):** кластер «cursor rules» / «настройка cursor rules» / «cursor rules mdc» — низко- и mid-volume, **высокая прикладная ценность** (пользователь уже в Cursor и ищет настройку инструкций). Secondary из карточки: «миграция с cursorrules на mdc», «.cursor/rules инструкция».

### LSI для writer (SERP + Wordstat secondary)

- cursor rules mdc, .cursor/rules, alwaysApply, globs, description  
- настройка cursor rules, миграция cursorrules → mdc  
- Agent mode, Active Rules, Settings → Rules  
- AGENTS.md, User Rules, Team Rules  
- /create-rule, Customize → Add Rule  
- cursor.directory, awesome-cursorrules  
- troubleshooting: правило не применяется, silent YAML, .md вместо .mdc  

**SEO-стратегия:** primary «cursor rules» в H1/lead; secondary «cursor rules mdc», «настройка cursor rules», «миграция с cursorrules на mdc» — в H2/H3 и FAQ. Long-tail «cursor rules 1c» — одним абзацем или FAQ, не в title.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Cursor поддерживает 4 типа rules: Project Rules (`.cursor/rules`), User Rules, Team Rules, AGENTS.md | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| Project rules — файлы `.mdc` в `.cursor/rules`, version-controlled | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| Обычный `.md` в `.cursor/rules` **игнорируется** (нет frontmatter для description/globs/alwaysApply) | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| AGENTS.md — plain markdown альтернатива `.cursor/rules` для простых кейсов | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| Nested AGENTS.md: файлы в подпапках применяются при работе с файлами в этой ветке; более глубокие инструкции имеют приоритет | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| 4 режима UI: Always Apply, Apply Intelligently, Apply to Specific Files, Apply Manually (@-mention) | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| `alwaysApply: true` — правило всегда в контексте; globs и description игнорируются | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| `alwaysApply: false` + `globs` — auto-attach при файлах в контексте | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| `alwaysApply: false` + `description` без globs — Agent решает по description | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| `alwaysApply: false` без description и globs — только при @-mention правила в чате | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| Несколько glob-паттернов — через **запятую** (например `docs/**/*.md, docs/**/*.mdx`) | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| Создание rules: `/create-rule` в Agent или Customize → Rules → Add Rule | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| Best practice: правила **короче 500 строк**; дробить на composable rules | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| Precedence при конфликте: **Team Rules → Project Rules → User Rules** (ранние побеждают) | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| Team Rules — dashboard, планы Team и Enterprise; free-form text, glob optional | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| User Rules — Customize → Rules, глобально; **только Agent (Chat)**, не Tab и не Inline Edit (Cmd/Ctrl+K) | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| Rules **не влияют** на Cursor Tab и другие AI-фичи вне Agent | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| Remote rules из GitHub → `.cursor/rules/imported/` с сохранением относительных путей | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| В правилах можно ссылаться на файлы через `@filename.ts` | [cursor.com/docs/rules](https://cursor.com/docs/rules) | 10.09.2026 | да |
| `.cursorrules` в корне — **legacy**; Cursor рекомендует миграцию на `.cursor/rules/*.mdc` | [stackhawk.com/blog/cursor-rules/](https://www.stackhawk.com/blog/cursor-rules/) | 2026 | да (community + согласовано с docs) |
| Миграция: разбить монолит на тематические `.mdc`, добавить frontmatter, удалить `.cursorrules` после проверки | [stackhawk.com/blog/cursor-rules/](https://www.stackhawk.com/blog/cursor-rules/) | 2026 | да |
| Репозиторий awesome-cursorrules — **40 747** stars (GitHub) | [github.com/PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | 10.09.2026 | да |
| «cursor rules» — **248** показов/мес (РФ, Wordstat по вторичному источнику) | [mayai.ru/cursor-rules-nastroyka-proekta/](https://mayai.ru/cursor-rules-nastroyka-proekta/) | 22.06.2026 | да (с оговоркой: не прямой API) |
| «как настроить cursor» — **186** показов/мес | [mayai.ru/cursor-rules-nastroyka-proekta/](https://mayai.ru/cursor-rules-nastroyka-proekta/) | 22.06.2026 | да (с оговоркой) |

**Не использовать без оговорки:** утверждение «.cursorrules silently ignored in Agent mode» (thepromptshelf) — спорно; официально legacy **ещё читается**, но для Agent mode в 2026 writer должен рекомендовать `.mdc` как primary. Не писать «40 tools limit» — не относится к rules.

**fact-bank.md:** записей по Cursor Rules нет — все факты из таблицы выше.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **20–40 минут** поднять **рабочий набор Project Rules** в `.cursor/rules/*.mdc` для **Agent mode**: один `alwaysApply`-файл (короткий), один glob-scoped под стек, проверка в Active Rules, миграция с `.cursorrules` без конфликта, commit в git.

**Почему отличается от конкурентов:**
- Официальная docs — канон, но без пошагового «первый вечер» и чек-листа silent YAML.
- EN-гайды не бьют в RU-intent «настройка cursor rules».
- mayai.ru уже закрывает новичка/HTML — B06 углубляет **Agent mode, модульность, миграция за 5 мин, troubleshooting**.
- «Ковчег»: автоматизация + связка rules (как думать) → MCP B03 (к чему подключаться).

**Tone:** Rules = «стикеры на мониторе агента»; frontmatter = «когда стикер виден»; Tab ≠ Agent. Без снобизма Senior-dev.

**H2-каркас (из карточки + research):**
1. Зачем Cursor Rules в 2026: Agent mode, контекст, почему `.cursorrules` устарел  
2. Структура `.cursor/rules/`: создание `.mdc` с YAML (alwaysApply, globs, description)  
3. Четыре режима активации: always / globs / agent-requested / manual  
4. Модульная архитектура: general + stack-specific (пример Next/API/тесты или контент-репо)  
5. Миграция с `.cursorrules`: чек-лист за 5 минут  
6. Troubleshooting: не подхватывается, перегруз контекста, конфликт с AGENTS.md  
7. FAQ + финальный чек-лист  

**Conversion:**
- Internal: [B03 MCP](/podklyuchenie-mcp-cursor/) — rules + MCP  
- CTA Make/kv-ai.ru — max 2× если уместно (автоматизация после rules)  

---

## 5. Шаблоны frontmatter (черновик для writer)

**00-general.mdc (Always):**
```yaml
---
alwaysApply: true
---
```
3–15 пунктов: язык ответов, «спроси перед удалением», команды lint/test.

**stack-scoped (Auto Attached):**
```yaml
---
description: ""
globs: "src/**/*.tsx,src/**/*.ts"
alwaysApply: false
---
```

**agent-requested:**
```yaml
---
description: "RPC/API conventions when editing backend services"
alwaysApply: false
---
```

**manual:** пустой frontmatter кроме `alwaysApply: false` — вызов `@rule-name`.

---

## 6. FAQ-кандидаты (7)

1. **Как настроить cursor rules с нуля?** — Создать каталог `.cursor/rules/`, добавить `.mdc` с YAML `---`, задать режим, проверить Settings → Rules и Active Rules в новом Agent-чате.  
2. **Чем `.mdc` отличается от `.cursorrules`?** — `.mdc` в папке с frontmatter и scoped activation; `.cursorrules` — legacy один файл в корне.  
3. **Почему cursor rules не работают в Agent mode?** — Проверить: каталог vs файл, расширение `.mdc`, закрывающий `---`, неверный glob (`*.tsx` vs `**/*.tsx`), дубль с `.cursorrules`, модель Auto (community tip — явная модель).  
4. **Always Apply или globs?** — Always только для 3–15 глобальных пунктов; стек и папки — в отдельные `.mdc` с globs.  
5. **Rules vs AGENTS.md?** — AGENTS.md для простого always-on markdown; `.mdc` когда нужны globs и режимы; не дублировать противоречия.  
6. **Влияют ли rules на Tab / Cmd+K?** — Нет, только Agent (Chat) по официальной docs.  
7. **Как мигрировать с `.cursorrules`?** — Backup → разбить на 2–3 `.mdc` → frontmatter → тест → удалить legacy файл.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Cursor Rules 40–60 слов | Lead после H1 | «Cursor Rules — постоянные инструкции для Agent…» |
| Таблица 4 режимов activation | H2-3 | alwaysApply / globs / description / manual |
| Таблица иерархии rules | H2-1 | Team → Project → User + AGENTS.md |
| Workflow | H2-2–5 | mkdir → .mdc → frontmatter → test → git commit |
| Пример YAML + body | H2-2 | Блок кода |
| FAQ 7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «cursor rules», «cursor rules mdc», «настройка cursor rules», «миграция cursorrules».

---

## 8. Риски для writer

- Держаться **cursor.com/docs/rules** по `.md ignored` и precedence — не design.dev «.md works».  
- Не выдумывать версию Cursor — «актуальная на 10.09.2026».  
- Не копировать mayai/hexlet 1:1 — другой угол (Agent + модульность + migration timer).  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Min **5** нумерованных шагов + чеклист **10+** пунктов (utility gate статьи).  
- Wordstat-цифры — с оговоркой «по данным Wordstat, июнь 2026» или без цифр если QA strict.  
- Не уходить в новость «Cursor закрыт в России» — не intent темы B06.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст каталог `.cursor/rules/`, добавит минимум два `.mdc` (general + scoped), выберет режим activation через frontmatter, проверит загрузку правил в Agent через Settings → Rules и Active Rules, при необходимости перенесёт содержимое из `.cursorrules` без конфликта и закоммитит rules в git для команды.

**action_outline (для writer):**

1. **Открыть проект в Cursor** и убедиться, что работает **Agent mode** (не только Tab). Переименовать legacy `.cursorrules` в backup, если файл есть.  
2. **Создать каталог** `.cursor/rules/` в корне репозитория (`mkdir -p .cursor/rules` или Command Palette → New Cursor Rule).  
3. **Добавить `00-general.mdc`** с `alwaysApply: true` и 5–15 пунктами (язык, стек, запреты, «спроси перед удалением»).  
4. **Добавить scoped rule** (например `frontend.mdc`) с `alwaysApply: false` и `globs` под свой стек (`**/*.html`, `src/**/*.tsx` и т.д.).  
5. **Проверить YAML:** открывающий и **закрывающий** `---`; расширение `.mdc`, не `.md`.  
6. **Открыть Cursor Settings → Rules** — убедиться, что Project Rules показывают правильный тип (Always / Auto Attached).  
7. **Новый Agent-чат:** спросить «какие правила активны?» — сверить **Active Rules** с ожидаемыми файлами.  
8. **Прогнать тестовый prompt** под glob (например правка `.tsx` / HTML) без копипаста инструкций в чат.  
9. **Миграция (если был `.cursorrules`):** разбить монолит на 2–3 `.mdc`, назначить frontmatter, протестировать, удалить legacy файл.  
10. **`git add .cursor/rules/` и commit** — чтобы команда получила те же rules.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен; secondary mayai |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B06
article_dir: memory/blog/articles/B06-nastroyka-cursor-rules-mdc
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 конкурентов (cursor.com/docs, stackhawk, dev.to, design.dev, hexlet, insidepc, mayai). Wordstat MCP недоступен; LSI из secondary (cursor rules 248/мес). Угол — Agent mode: .cursor/rules/*.mdc за 20–40 мин, 4 режима frontmatter, миграция .cursorrules, troubleshooting silent YAML. 22 факта с URL, 10 шагов action_outline, 7 FAQ. Готов к writer.
===
