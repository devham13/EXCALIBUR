# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + чеклист)  
**search_intent:** how_to  
**research_date:** 2026-07-09  
**disclaimer:** Все даты, версии и статистика проверены на 09.07.2026 (2026 год).

---

## 0. Utility gate (тема)

```bash
python3 scripts/excalibur_blog_utility_gate.py --topic-id B01
# topic B01: PASS
```

| Поле | Значение |
|------|----------|
| search_intent | how_to |
| article_mode | B |
| primary_query | как писать seo статьи |
| status | **PASS** |

**utility_verdict:** PASS

**reader_outcome:** Читатель пройдёт полный цикл написания SEO-статьи: соберёт семантику в Wordstat, разберёт SERP, соберёт структуру longread с GEO-чанками, напишет текст для людей, оформит мета/FAQ/schema и проверит материал чеклистом перед публикацией.

**action_outline (для writer):**

1. **Проверить спрос и интент** — primary «как писать seo статьи» + secondary «seo текст для блога», «geo оптимизация статьи»; зафиксировать практический intent (пошаговая инструкция, не определение).
2. **Собрать семантический кластер** — Wordstat + подсказки SERP: 3–5 смысловых групп (структура, ключи, E-E-A-T, техника, GEO).
3. **Разобрать топ-5–10 SERP** — выпишите H2 конкурентов, форматы (таблицы, FAQ, чек-листы), пробелы; не копировать структуру 1:1.
4. **Собрать скелет longread** — H1 с глаголом; lead 40–60 слов с прямым ответом; H2 по карточке B01 + подтемы из SERP.
5. **Написать черновик «сначала смысл»** — абзацы 3–5 строк, списки/таблицы; ключи естественно в H1, lead, 1–2 H2, Title/Description.
6. **Добавить GEO-слой** — самодостаточные H2/H3-блоки; JSON-LD BlogPosting + FAQPage (в schema, не в body); llms.txt — упомянуть как опциональный эксперимент, приоритет Schema.
7. **Оформить технику** — Title ≤60 знаков, Description 140–160, alt, 3–5 внутренних ссылок, robots.txt для AI search-ботов.
8. **Пройти чеклист перед публикацией** — 15+ пунктов: семантика, мета, island test, FAQ, факты только из таблицы ниже.
9. **Опубликовать и замерить** — Яндекс Метрика / GSC: запросы, время на странице, возвраты в поиск.

---

## 1. SERP-обзор (WebSearch, 09.07.2026)

Источник: живой WebSearch + сверка с `research-serp.json`. DuckDuckGo-«утка» использована только как стартовый список URL; приоритет — свежий анализ.

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | 5 шагов workflow; Wordstat; H1–H4; естественность ключей; alt, мета, перелинковка | Нет GEO/AI-выдачи; CTA Директа | Блок про Директ; «что такое SEO» без actionable шагов |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu) | Пошаговый how-to (фев. 2026) | 13 нумерованных шагов от темы до WordPress; таблица анализа конкурентов; интент | Нет отдельного GEO-блока; фокус WP | 13 шагов 1:1; хостинг-реклама |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Кластеризация Wordstat; H2 с ответом сразу; LSI без переспама | Длинный sales-narrative; ИИ без дисклеймеров Google | Структуру агентского гайда целиком |
| 4 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Чек-лист + E-E-A-T (2026) | Семантика, Title ~65 знаков, Schema Article+FAQ | Кейсы без первичника; agency CTA | «+140% трафика» и прочие % без URL |
| 5 | [gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | SEO+GEO практика (июнь 2026) | 40–60 слов lead; факты каждые 150–200 слов; island blocks; чек-лист GEO | Brandlight 70%→20% — вторичный источник | Непроверенные % Brandlight в тексте без оговорки |
| 6 | [yositeup.com/ru-ua/blog/ai-seo-workflow-2026-research-to-publication](https://yositeup.com/ru-ua/blog/ai-seo-workflow-2026-research-to-publication) | AI SEO workflow (2026) | Title 60 / Desc 140–160; H1≠Title; бриф 2500–3000 слов; финальный чек-лист | UA-рынок; AI Overviews 61% кликов — без первичника в сниппете | Цифры «8–12 ч → 2–3 ч» как универсальная норма |
| 7 | [shipmint.kz/blog/llms-txt-schema-org-vidimost-dlya-ai-poiska](https://shipmint.kz/blog/llms-txt-schema-org-vidimost-dlya-ai-poiska) | GEO техника (2026) | Приоритет Schema над llms.txt; цитата Google про LLMs.txt; JSON-LD типы | KZ-локализация; часть метрик агентские | SE Ranking цифры без проверки arxiv/отчёта в QA |
| 8 | [developers.google.com/search/docs/fundamentals/creating-helpful-content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Канон Google | People-first; E-E-A-T; нет «любимого» word count; SEO для people-first — ок | Не про Яндекс | Search-engine-first контент |

**Паттерн SERP (июль 2026):** доминируют «полный гайд 2026» с Wordstat, E-E-A-T, чек-листом и блоком про ИИ. Отдельный кластер — GEO (llms.txt, schema, AI-краулеры). H1 «которые читают люди» слабо представлен; дифференциатор — **читабельность + единый workflow SEO+GEO**.

**Intent:** how_to — пользователь хочет алгоритм от ключа до публикации. Вторичный: связать SEO-текст и GEO в одном материале без двойной работы.

**Пробел для Excalibur B01:** объединить канон Яндекса (семантика, структура) + Google people-first + практический GEO (schema first, island chunks) в **один чеклист для блогера**, без agency-water и без «магии llms.txt».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` недоступен в Cloud-среде прогона (MCP не подключён; инструмент `wordstat_get_top_requests` не вызывается). Точные объёмы показов в месяц **не получены** — цифры в таблицу спроса не добавлялись (запрет на выдумывание).

**Действие для пайплайна:** обновить токен / подключить MCP и перезапустить research, либо вручную проверить в [wordstat.yandex.ru](https://wordstat.yandex.ru/):

- `как писать seo статьи`
- `seo текст для блога`
- `geo оптимизация статьи`
- операторы: `"как писать seo статьи"`, `!как !писать !seo !статьи` (точная словоформа)

OAuth (при 401 API): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### LSI и смежные запросы (из SERP + WebSearch, без объёмов)

**Кластер 1 — написание и структура:** как написать seo статью, структура seo статьи, пошаговая инструкция seo текст, seo копирайтинг 2026, longread для блога  

**Кластер 2 — семантика:** семантическое ядро, lsi ключи, яндекс вордстат, сбор ключевых слов, интент запроса  

**Кластер 3 — техника on-page:** title description, метатеги, h1 h2 h3, внутренняя перелинковка, alt изображений  

**Кластер 4 — качество и E-E-A-T:** e-e-a-t, текст без воды, переспам ключей, уникальность, экспертность автора  

**Кластер 5 — GEO / AI:** geo оптимизация статьи, generative engine optimization, schema json-ld faqpage, llms.txt, ai overviews, нейропоиск  

**FAQ-хвосты (из карточки B01):** сколько символов в seo статье; что такое geo в seo  

**SEO-стратегия writer:** primary в H1/Title/lead; secondary в отдельных H2; LSI — естественно по кластерам 1–5.

---

## 3. Таблица фактов (цифры только с URL)

| # | Факт | Источник | Дата | Можно в текст |
|---|------|----------|------|---------------|
| 1 | Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 2 | Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 3 | H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 4 | Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 5 | Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 6 | Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 7 | Google: нет предпочтительного word count; не пишите «ради объёма» | [Google — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 2026 | да |
| 8 | Google: people-first контент; SEO допустим, если не search-engine-first | [Google — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 2026 | да |
| 9 | E-E-A-T: trust главный; experience, expertise, authoritativeness поддерживают доверие | [Google — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 2026 | да |
| 10 | Прямой ответ на главный вопрос — в первых 40–60 словах блока (GEO) | [Gracie Digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| 11 | Фактическая насыщенность: цифра/пример примерно каждые 150–200 слов | [Gracie Digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| 12 | Каждый H2/H3 должен быть самодостаточным «островом смысла» | [Gracie Digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| 13 | Title: до 60 символов; Meta Description: 140–160; H1 ≠ Title | [YoSiteUp — AI SEO workflow 2026](https://yositeup.com/ru-ua/blog/ai-seo-workflow-2026-research-to-publication) | 2026 | да |
| 14 | Основной запрос — в первых 150 словах | [YoSiteUp — AI SEO workflow 2026](https://yositeup.com/ru-ua/blog/ai-seo-workflow-2026-research-to-publication) | 2026 | да |
| 15 | Бриф longread: ориентир 2500–3000 слов, 5–6 H2, FAQ 5 вопросов | [YoSiteUp — AI SEO workflow 2026](https://yositeup.com/ru-ua/blog/ai-seo-workflow-2026-research-to-publication) | 2026 | да* |
| 16 | Google: «We currently have no plans to support LLMs.txt» (цитата в обзоре) | [Shipmint — llms.txt vs Schema](https://shipmint.kz/blog/llms-txt-schema-org-vidimost-dlya-ai-poiska) | 2026 | да* |
| 17 | Приоритет для AI-видимости: JSON-LD (Organization, WebSite, Article, FAQPage) | [Shipmint — llms.txt vs Schema](https://shipmint.kz/blog/llms-txt-schema-org-vidimost-dlya-ai-poiska) | 2026 | да |
| 18 | Извлекаемые пассажи для AI: ориентир 134–167 слов на блок (обзор Ziptie) | [Shipmint — llms.txt vs Schema](https://shipmint.kz/blog/llms-txt-schema-org-vidimost-dlya-ai-poiska) | 2026 | да* |
| 19 | llms.txt в 2026 не подтверждён как GEO ranking factor; боты краулят HTML | [Limy — LLMs.txt guide 2026](https://limy.ai/blog/llms.txt-in-2026-the-full-guide) | 2026 | да |
| 20 | Анализ Limy: 515M+ LLM bot events — доля запросов к `/llms.txt` статистически ничтожна | [Limy — LLMs.txt guide 2026](https://limy.ai/blog/llms-txt-in-2026-the-full-guide) | 2026 | да* |
| 21 | Практический how-to: 13 шагов от выбора темы до проверки перед публикацией | [OlegWeb — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| 22 | Интент «как написать seo-статью» — практический: нужен алгоритм, не определение | [OlegWeb — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| 23 | 3–6 дополнительных ключей + 6–8 подзаголовков в плане статьи | [Sostav — SEO-продвижение статей](https://www.sostav.ru/blogs/282649/69350) | 2025–2026 | да |
| 24 | Внутренняя перелинковка: 3–5 ссылок на якорные страницы (рекомендация в гайдах) | [TV_TE — SEO 2026](https://t-v.te.ua/ru/yak-pisati-seo-optimizovani-statti-u-2026-povnij-gid-dlya-trafiku/) | 2026 | да* |

\* Вторичный или отраслевой источник — в тексте с оговоркой «по данным исследования/гайда», без точных % если QA не найдёт первичник.

**Не использовать:** «+140% трафика» (Pikapuka); «AI Overviews 61% кликов» (YoSiteUp без первичника в статье); «Brandlight 70%→20%» без первичника; «+40% GEO» (Aggarwal) без arxiv.

**fact-bank.md:** прямых фактов по SEO-копирайтингу нет — опираться на таблицу выше.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **longread, который читают люди**, и который **готов к цитированию в AI** без отдельного «GEO-проекта». Единый workflow: интент → Wordstat → SERP → структура → текст → schema/FAQ → чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон без GEO-слоя.
- GEO-гайды не учат писать текст с нуля.
- Агентские longread перегружены CTA и непроверенными кейсами.
- H1 «которые читают люди» — редкий фокус в SERP: **читабельность как метод** (lead, абзацы, острова), не лозунг.

**Режим B:** минимум **5 нумерованных шагов** + **чеклист 10+ пунктов** + workflow `→` между этапами. Сама статья B01 — эталон формата блога (8 500–9 500 знаков текста по quality-blog).

**H2-каркас (карточка B01 + research):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как
4. Чеклист перед публикацией

**Подтемы внутри блоков:** Wordstat, Title/Description, E-E-A-T lite, перелинковка, robots.txt для AI search-ботов, llms.txt как опция.

**Tone:** практично, по-человечески; без корпоративной воды и эмодзи.

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | Прямой ответ на «как писать seo статьи» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | Generative Engine Optimization — … |
| Island test | Каждый H2 | Блок понятен без соседних |
| FAQ 5–7 | Конец | Ответы-действия, 2–4 предложения |
| Schema | schema-агент | BlogPosting + FAQPage JSON-LD |
| llms.txt | GEO-блок | Опционально; приоритет Schema (факты 16–19) |
| Внутренняя ссылка | Из карточки | `/` |
| cover_scene_hint | Cover | Редактор за ноутбуком, блокнот, тёплый свет |

**Целевые формулировки:** как писать seo статьи, seo текст для блога, geo оптимизация статьи, сколько символов в seo статье, что такое geo в seo.

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — Универсальной нормы нет (факт 1); для how-to longread Excalibur — 8 500–9 500 знаков при полноте ответа.
2. **Что такое GEO в SEO?** — Дополнение к SEO: оптимизация под цитирование в AI-ответах при том же индексируемом контенте.
3. **Нужен ли переспам ключей в 2026?** — Нет; естественные вхождения + тематические слова (факты 4, 8).
4. **Чем Title отличается от H1?** — Title для сниппета (≤60 знаков), H1 на странице; не дублировать (факт 13).
5. **Какие schema нужны блоговой SEO-статье?** — BlogPosting + FAQPage в JSON-LD (факт 17).
6. **Нужен ли llms.txt блогу?** — Не приоритет; Google не планирует поддержку (факт 16); schema важнее.
7. **Как проверить статью перед публикацией?** — Чеклист: семантика, мета, структура, FAQ, schema, ссылки, island test.

---

## 7. Риски и blockers для writer

- Не выдумывать Wordstat-показы — раздел 2 с WARNING.
- Не копировать Pikapuka / 1ps структуру 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Минимум 5 нумерованных шагов + чеклист 10+ (utility gate статьи).
- Без эмодзи; site_url — `/` по карточке.
- Цифры только из таблицы фактов §3.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | ✅ PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен — LSI без объёмов |
| Таблица фактов с URL | ✅ (24 факта) |
| utility_verdict + action_outline + reader_outcome | ✅ |
| GEO hooks + FAQ | ✅ |
| Режим B | ✅ |

**Writer:** готов с оговоркой по Wordstat — при появлении MCP директор может перезапустить research для таблицы показов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
