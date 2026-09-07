# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to / longread + чеклист)  
**search_intent:** how_to  
**research_date:** 2026-09-07  
**disclaimer:** Все даты, версии и статистика проверены на 2026-09-07 (2026 год).

---

## utility_verdict: PASS

**reader_outcome:** После гайда читатель сможет самостоятельно пройти workflow от проверки спроса и интента до готовой SEO+GEO статьи с FAQ, schema и чек-листом перед публикацией в WordPress.

**action_outline (workflow для writer):**

1. **Проверить спрос и интент** — primary query в Вордстат, подсказки Яндекс/Google, классификация intent (информационный / практический / коммерческий).
2. **Собрать семантику** — primary + secondary + 10–15 вопросных long-tail из PAA и подсказок; сгруппировать в кластер под одну статью.
3. **Разобрать топ-5 SERP** — что закрывают конкуренты, где пробел (GEO-слой, чек-лист, «для людей» vs «для роботов»).
4. **Собрать структуру H1→H2→H3** — каждый H2 = подзадача; первые 1–3 предложения блока = прямой ответ (BLUF / Snippet-First).
5. **Написать lead и тело** — lead с определением SEO-статьи; абзацы 3–5 строк; списки и таблицы; E-E-A-T lite (опыт, примеры, источники).
6. **Добавить GEO-слой в тот же текст** — атомарные чанки, FAQ 5–7 пар, Key Takeaways после H1; не отдельный «GEO-проект».
7. **Оформить мета и медиа** — Title (~65 знаков, ≠ H1), Description, alt у изображений, внутренние ссылки.
8. **Подготовить schema** — BlogPosting + FAQPage (+ HowTo, если есть нумерованные шаги); JSON-LD вне body.
9. **Пройти чек-лист перед публикацией** — семантика, структура, читабельность, schema, индексация (Вебмастер / GSC).

---

## 1. SERP-обзор (WebSearch, 2026-09-07)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон workflow: семантика → структура → текст → оптимизация; H1–H4; естественность ключей; Wordstat, alt, мета | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа; копировать структуру 1:1 |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 13 шагов (фев. 2026) | От ключа до WordPress; интент, конкуренты, E-E-A-T, чек-лист | Длинный narrative; GEO почти нет | 13 H2 «как у автора» без дифференциации |
| 3 | [fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | Агентский гайд (июн. 2026) | Pillar/cluster, E-E-A-T + experience, атомарные ответы, FAQ | Agency tone; мало техники schema | Непроверенные обобщения про «пессимизацию ИИ-текста» |
| 4 | [pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | GEO + Snippet-First (июн. 2026) | Промпты в H2, чанки 3–7 строк, Schema Article/FAQ/HowTo | «+80% шансов» без первичника; продаёт агентство | Цифры без arXiv/источника |
| 5 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист 2026 (июн. 2026) | E-E-A-T + ЭПОС, AI Overviews / Алиса, answer-first | 9 критериев без единого numbered workflow «с нуля» | Корпоративный объём без «сделай сам за вечер» |
| 6 | [serptop.ru/blog/kak-pisat-seo-teksty](https://serptop.ru/blog/kak-pisat-seo-teksty/) | Руководство + чек-лист | Формула H1, каркас H2, meta/alt правила | Слабый GEO-блок | Шаблонную 6-блочную структуру без GEO |
| 7 | [trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | AEO/GEO чек-лист (апр. 2026) | Структура H1→FAQ, schema, Core Web Vitals, 10–15 вопросов в кластере | Фокус на нейропоиск, не на написание SEO-текста с нуля | Кейс «+40% за 4 месяца» без верификации |
| 8 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Workflow 2026 (из research-serp) | «Один longread под AI-цитирование», чеклист до публикации | Узкий бренд | Копировать формулировки 1:1 |

**Паттерн SERP:** топ — «полный гайд 2026» (13 шагов, E-E-A-T, Wordstat) + отдельный кластер GEO/Snippet-First. Запрос «как писать seo статьи» закрыт **фрагментарно**: либо классическое SEO без GEO, либо GEO без пошагового написания текста. H1 «которые читают люди» в топе почти не раскрыт — упор на ключи или нейросети, не на **читабельность как SEO+GEO фактор**.

**Intent:** how_to — пользователь хочет **систему действий**: семантика → структура → текст → мета → FAQ/schema → проверка. Вторичный: связка SEO + GEO в **одном** материале, не два проекта.

**Пробел для Excalibur:** единый **практический workflow** «SEO-статья для людей = готова для нейропоиска»: инфостиль + атомарные H2 + FAQ/schema + финальный чек-лист; режим B — сама статья B01 как эталон формата.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в среде Cloud Agent (вызов `wordstat_get_top_requests` завершился ошибкой «MCP server does not exist»). Точные показы в месяц **не получены**. Обновите токен и MCP через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса

| Фраза | Показы/мес |
|-------|------------|
| как писать seo статьи | *не получено — MCP недоступен* |
| seo текст для блога | *не получено — MCP недоступен* |
| geo оптимизация статьи | *не получено — MCP недоступен* |

### Экспертная семантика (SERP + подсказки, без подмены Wordstat)

**Primary cluster:** как писать seo статьи, как написать seo статью, seo текст для блога, структура seo статьи, seo статья пример, как составить seo статью.

**LSI для writer (из топа SERP и secondary_queries):**

- seo текст, seo копирайтинг, семантическое ядро, интент запроса, LSI-ключи  
- структура longread, H1 H2 H3, title description, meta title  
- E-E-A-T, ЭПОС, полезность контента, поведенческие факторы  
- geo оптимизация статьи, generative engine optimization, snippet-first, BLUF  
- FAQ schema, BlogPosting, HowTo, FAQPage, микроразметка  
- чек-лист seo статьи, сколько символов в seo статье, что такое geo в seo  
- яндекс вордстат, вебмастер, перелинковка, alt изображений  

**SEO-стратегия (без частотностей):** primary «как писать seo статьи» — в H1/lead; «seo текст для блога» — в блок про формат блога; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье»; faq_hints — в FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение → основная часть → заключение; во введении — тема и польза для читателя | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Ключи — естественно, без переспама; важны читаемость и соответствие запросу | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Google: helpful, people-first content; E-E-A-T — рамка доверия (опыт, экспертиза, авторитет, достоверность) | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Яндекс: ЭПОС — экспертность, полезность, оригинальность, содержательность | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| В 2026 контент должен быть понятен человеку, поисковой системе и AI (AI Overviews, Алиса, ChatGPT, Perplexity) | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Принцип 2026: от главного ответа к деталям; H2 — подтема, H3 — аспект внутри | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| SEO-статья 2026 — не «текст под ключи», а страница, закрывающая задачу пользователя (выбрать, настроить, сделать) | [OlegWeb — алгоритм SEO-статьи](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Плотность информации важнее длины; ответ — в начале, без «воды» во вступлении | [FireSEO — SEO-тексты 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| Контент для AI: самодостаточные атомарные ответы; важную информацию не прятать во вкладки/accordion | [FireSEO — SEO-тексты 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| Snippet-First: каждый H2 начинается с резюме 1–3 предложения — ответ без контекста | [PW Agency — GEO контент 2026](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 19.06.2026 | да |
| Абзацы 3–7 строк (чанки): один абзац — одна мысль | [PW Agency — GEO контент 2026](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 19.06.2026 | да |
| Schema для блога: Article/BlogPosting, FAQPage; при пошаговой инструкции — HowTo | [PW Agency — GEO контент 2026](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 19.06.2026 | да |
| GEO-bench: 10 000 запросов; Cite Sources, Quotation Addition, Statistics Addition дают **+30–40%** visibility (Position-Adjusted Word Count) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| На Perplexity.ai — улучшение visibility до **37%** (тот же paper) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Keyword stuffing в GEO-контексте работает **хуже** baseline | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Title — ориентир ~65 знаков, ключ + триггер (чек-лист, инструкция); H1 ≠ Title | [SerpTop — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| Статья для нейропоиска: прямой ответ в первых **100 словах** после H1 | [Trigub — чек-лист для ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 19.04.2026 | да |
| Техбаза для AI-видимости: Schema FAQPage/HowTo/Article; LCP **< 2,5 сек**, INP **< 200 мс**, CLS **< 0,1** (Core Web Vitals) | [Trigub — чек-лист для ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 19.04.2026 | да |
| Кластер контента: pillar longread + 5–10 cluster-статей со перекрёстными ссылками | [FireSEO — SEO-тексты 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |

**fact-bank.md:** прямых фактов про «как писать SEO-статьи» нет — используем таблицу выше. Связанные факты из fact-bank (SurveyMonkey 51% маркетологов — ИИ для аналитики, не штамповки) — опционально в блоке «ИИ в production», не как центральный тезис B01.

**Не использовать без оговорки:** «+80% шансов в выдаче ИИ» (PW Agency); «+140% трафика за 3 недели»; «каждый пятый запрос — в нейросеть» (Trigub — внутренняя аналитика автора); «микроразметка ×1,5–2 цитирование» без первичника.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **longread, который читают люди** и который **можно процитировать** в нейропоиске. Один workflow, не «SEO отдельно, GEO отдельно».

**Почему отличается от конкурентов:**

- Яндекс Direct — канон SEO без GEO и без акцента на читабельность.
- OlegWeb / FireSEO — глубокие гайды, но GEO/schema — вторично или размазано.
- GEO-лонгриды (PW, Trigub) — не учат писать текст с нуля для блога.
- H1 «которые читают люди» — наш дифференциатор: **инфостиль + структура + острова смысла** как SEO- и GEO-фактор.

**Tone:** практично, по-человечески; каждый H2 = подзадача + рекомендация (делать / не делать).

**H2-каркас (из карточки B01 + research):**

1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: lead, H2/H3, списки, таблицы, чанки
3. FAQ и schema — зачем и как (BlogPosting + FAQPage)
4. Чек-лист перед публикацией (15–20 пунктов)

**Внутри блоков (не обязательно отдельные H2 верхнего уровня):** Wordstat/семантика, Title/Description, E-E-A-T lite, перелинковка, alt.

**Режим B:** статья B01 — эталон: ~8 500–9 500 знаков текста, 5–7 FAQ, атомарные H2, lead с определением.

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи (40–60 слов) | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO (40–60 слов) | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Key Takeaways | После lead | 3–5 тезисов |
| Conversational H2 | FAQ-adjacent | «Сколько символов…», «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, action-first |
| Атомарные чанки | Каждый H2 | Предложение 1 = тезис |
| Schema handoff | Не в body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | `/` |
| cover_scene_hint | Cover | «Редактор за ноутбуком, блокнот, тёплый свет» |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при той же индексируемой базе.
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + LSI; keyword stuffing вреден и для GEO (arxiv).
4. **Чем Title отличается от H1?** — Title ~65 знаков для сниппета; H1 — на странице; не дублировать.
5. **Какие schema нужны блоговой SEO-статье?** — BlogPosting + FAQPage; HowTo при нумерованных шагах.
6. **Как проверить статью перед публикацией?** — чек-лист: семантика, мета, структура, FAQ, schema, ссылки, CWV.
7. **Можно ли делегировать написание нейросети?** — черновик да; финал — человек: факты, структура, E-E-A-T (Texterra).

---

## 7. Риски и blockers для writer

- Не выдумывать показы Wordstat — секция помечена WARNING.
- Не копировать 13 шагов OlegWeb или 7 блоков Pikapuka 1:1.
- Цифры только из §3.
- Без эмодзи; CTA ≤ 3.
- `site_url` example.com — ссылки `/` или плейсхолдер по карточке.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| utility_verdict PASS + action_outline | ✅ |
| reader_outcome | ✅ |
| SERP ≥ 5 конкурентов (WebSearch) | ✅ |
| Wordstat (MCP) | ⚠️ недоступен — WARNING зафиксирован |
| Таблица фактов ≥ 15 с URL | ✅ (20) |
| Угол + дифференциация | ✅ |
| GEO hooks + FAQ 5–7 | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
