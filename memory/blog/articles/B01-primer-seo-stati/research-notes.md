# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + чеклист)  
**search_intent:** how_to  
**research_date:** 2026-09-10  
**disclaimer:** Все даты, версии и статистика проверены на 2026-09-10 (2026 год).

---

## Utility gate

| Gate | Результат |
|------|-----------|
| Topic utility gate (`scripts/excalibur_blog_utility_gate.py --topic-id B01`) | **PASS** |
| `search_intent` | how_to |
| `article_mode` | B |

**utility_verdict:** PASS

**reader_outcome:** Читатель сможет пройти полный цикл написания SEO-статьи — от сбора семантики и разбора ТОПа до структуры, текста с GEO-чанками, мета-тегов, FAQ/schema и финального чеклиста перед публикацией.

**action_outline:**

1. Определить primary query и интент; собрать 5–20 смежных фраз в Wordstat, сгруппировать по смыслу и отсечь запросы с другим intent.
2. Разобрать ТОП-5–10 выдачи: формат страницы, медианный объём, повторяющиеся H2, таблицы/FAQ, пробелы конкурентов.
3. Собрать структуру (H1 → H2 → H3): перевернутая пирамида — прямой ответ в lead и после каждого H2.
4. Написать черновик: короткие абзацы (3–5 строк), списки, таблицы, тематическая полнота (LSI), сигналы E-E-A-T (опыт, кейсы, скриншоты).
5. Распределить ключи естественно: primary в H1, первом абзаце, 1–2 H2, Title/Description; без переспама.
6. Добавить GEO-слой: атомарные блоки 40–80 слов, FAQ 5–7 пар, BlogPosting + FAQPage JSON-LD.
7. Заполнить Title (55–60 знаков) и Description (150–160 знаков); alt у изображений; внутренние ссылки.
8. Прогнать финальный чеклист (15–20 пунктов): релевантность, читабельность, schema, переобход в Вебмастере.

---

## 1. SERP-обзор (WebSearch Cursor, 10.09.2026)

Источник: живой WebSearch по запросам «как писать seo статьи 2026», «seo текст для блога», «geo оптимизация статьи 2026». Preflight `research-serp.json` использован как стартовый список; secondary/h1-запросы в нём пустые — дополнены WebSearch.

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Авторитет; 5 шагов (тема → семантика → структура → текст → оптимизация); примеры «плохо/хорошо»; Wordstat, alt, мета, перелинковка | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа; канон H1–H4 без GEO |
| 2 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst) | Практик, 7 шагов + чек-лист (обнов. 10.07.2026) | Полный workflow до контроля после публикации; Title 55–60 / Description 150–160; чек-лист 10 пунктов | Мало GEO; upsell Seolity | Копировать 7 шагов 1:1; рекламные вставки сервисов |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii/) | Longread 2026 + ИИ | Кластеризация Wordstat, E-E-A-T, гибрид ИИ+эксперт | Длинный; фокус на ИИ-генерации | Шаблон «полное руководство» без дифференциации |
| 4 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 13 шагов + WordPress (фев. 2026) | Глубина: интент, конкуренты, WP-оформление, переобход | Нет отдельного GEO-блока; 13 шагов перегружают новичка | 13-шаговую структуру без сжатия |
| 5 | [fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | Агентство (июнь 2026) | E-E-A-T/Experience, атомарные ответы, pillar+cluster | Agency tone; мало пошаговой семантики | Таблицу «ИИ vs эксперт» без адаптации |
| 6 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (2026) | E-E-A-T, Schema Article+FAQ, чек-лист | Непроверенные кейсы (+140% трафика) | Непроверенные проценты в кейсах |
| 7 | [divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 6 шагов для новичков | Простые правила ключей; ориентир 1500+ знаков | Короткий; без GEO и schema | Абстрактный минимум объёма без SERP-метода |
| 8 | [habr.com/ru/articles/1042732](https://habr.com/ru/articles/1042732/) | GEO/AEO longread (2026) | RAG-архитектура, front-loading, 44,2% цитат в первых 30% текста | Фокус GEO, не «как написать статью» | Agency-кейсы и длинный narrative |

**Паттерн SERP (сент. 2026):** доминируют пошаговые гайды «SEO-текст 2026» (7–13 шагов) + отдельный кластер GEO/AEO. H1 «которые читают люди» в топе почти не встречается — дифференциатор свободен. Почти все конкуренты дают workflow, но **редко связывают SEO-написание и GEO-упаковку в одном actionable чеклисте** для владельца блога без SEO-команды.

**Intent:** how_to — пользователь хочет систему «с нуля до публикации». Вторичные: «seo текст для блога» (формат/объём), «geo оптимизация статьи» (упаковка под нейроответы).

**Пробел для Excalibur:** единый workflow **SEO + GEO в одной статье**, акцент на **читабельность как фактор ранжирования** (острова смысла, lead-ответ, без воды) + готовый чеклист 15–20 пунктов. Угол автоматизатора контента (B2B), не «копирайтинг ради ключей».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в среде Cloud Agent (namespace не подключён). Вызов `wordstat_get_top_requests` для `primary_query` «как писать seo статьи» и secondary не выполнен. **Точные объёмы спроса (показы/мес) в этой версии research не получены — не использовать выдуманные цифры.**

Обновление токена (когда MCP доступен): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (без цифр спроса — для writer до восстановления Wordstat)

**Primary cluster:** как писать seo статьи, как написать seo статью, seo текст для сайта/блога, seo статья 2026, seo копирайтинг.

**LSI из SERP + конкурентов (вписывать естественно):**

- семантическое ядро, Wordstat, интент запроса, LSI-слова, кластеризация запросов  
- структура статьи, H1 H2 H3, title description, мета-теги, перелинковка  
- E-E-A-T, experience, текстовая релевантность, переспам, читабельность  
- FAQ, Schema.org, BlogPosting, FAQPage, JSON-LD  
- GEO, generative engine optimization, нейроответ, атомарный блок, AI Overviews, Яндекс Нейро  
- чек-лист перед публикацией, переобход, Яндекс Вебmaster  

**Secondary queries (из карточки B01):**

- «seo текст для блога» — закрывать блоком формата longread + объём по медиане ТОПа  
- «geo оптимизация статьи» — отдельный H2 с 5–7 практических пунктов (front-loading, FAQ, schema)

---

## 3. Таблица фактов (15+ утверждений с URL)

| # | Факт | Источник | Дата | Можно в текст |
|---|------|----------|------|---------------|
| 1 | Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 2 | Абзацы SEO-текста — ориентир 3–5 строк; перечисления — списками | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 3 | H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 4 | Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 5 | Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 6 | Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 7 | SEO-текст в 2026 — полезный текст, структура и словарь под конкретный запрос; не «ключи через каждые два абзаца» | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| 8 | Title — до 55–60 символов; Description — до 150–160 символов | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| 9 | Объём текста ориентируют на медиану конкурентов в ТОПе, а не на абстрактные нормы | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| 10 | Плотность информации важнее длины; ответ на запрос — в начале текста | [FireSEO — SEO-тексты 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| 11 | Для ИИ-выдачи нужны атомарные самодостаточные ответы; важную информацию не прятать во вкладки/аккордеоны | [FireSEO — SEO-тексты 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| 12 | E-E-A-T в 2026 смещён на Experience: кейсы, ошибки из практики, авторские скриншоты | [FireSEO — SEO-тексты 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| 13 | Главный ключ — в H1, первом абзаце и один раз ближе к концу; LSI — свободно, без подсчёта процентов | [Divitio — пошаговая инструкция](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| 14 | Принцип перевернутой пирамиды: H2 с прямым ответом сразу после lead | [quality21.ru — структура под запрос](https://quality21.ru/kak-privyazat-strukturu-stati-k-realnomu-zaprosu-polzovatelya-rukovodstvo-dlya-avtorov-i-seo-specialistov/) | 2026 | да |
| 15 | GEO — оптимизация контента для цитирования в ответах генеративных систем (Яндекс Нейро, AI Overviews, Perplexity, ChatGPT Search) | [trigub.ru — GEO-продвижение](https://trigub.ru/blog/geo-prodvizhenie-sayta/) | 04–16.04.2026 | да |
| 16 | По данным Яндекса, **27–40%** запросов уже получают нейроответ (цит. trigub.ru) | [trigub.ru — GEO-продвижение](https://trigub.ru/blog/geo-prodvizhenie-sayta/) | 04–16.04.2026 | да* |
| 17 | Исследование Georgia Tech GEO: правильные стратегии цитируемости могут дать **+30–40%** visibility | [trigub.ru — GEO-продвижение](https://trigub.ru/blog/geo-prodvizhenie-sayta/) | 04–16.04.2026 | да* |
| 18 | **44,2%** цитат LLM приходится на первые **30%** текста страницы (Grows Memo, цит. Habr) | [habr.com/ru/articles/1042732](https://habr.com/ru/articles/1042732/) | 2026 | да* |
| 19 | **68,7%** цитируемых страниц используют структурированные заголовки (цит. Habr) | [habr.com/ru/articles/1042732](https://habr.com/ru/articles/1042732/) | 2026 | да* |
| 20 | RAG: генеративные движки извлекают чанки из индекса и формируют ответ со ссылками | [habr.com/ru/articles/1042732](https://habr.com/ru/articles/1042732/) | 2026 | да |
| 21 | Если пользователь возвращается в поиск — сигнал низкого качества страницы | [olegweb.ru — SEO-статья](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| 22 | После публикации URL отправляют на переобход в Яндекс.Вебмастере и Google Search Console | [olegweb.ru — SEO-статья](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |

\* Вторичные источники (агентские блоги / Habr с цитатами исследований). В тексте — с оговоркой «по данным исследований / по оценке индустрии», без выдачи за собственную статистику Excalibur.

**Не использовать (нет первичника / непроверено):** «+140% трафика за 3 недели» (Pikapuka); «80% пользователей не переходят на сайты» без оговорки источника; «микроразметка ×1,5–2» без arxiv; HubSpot −70–80% как универсальный прогноз.

**fact-bank.md:** прямых строк по SEO-написанию нет; использовать таблицу фактов выше. Строки fact-bank про ИИ-автоматизацию — только если writer явно связывает с human-in-the-loop при генерации черновиков.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **longread, который решает задачу человека** и одновременно **упакован для нейропоиска**. Не «ещё один список ключей», а **единый workflow** с чеклистом: интент → семантика → структура → текст → GEO-чанки → FAQ/schema → публикация.

**Отличия от конкурентов:**

| Конкурент | Их фокус | Наш фокус |
|-----------|----------|-----------|
| Яндекс Direct | Канон SEO без GEO | SEO + GEO в одном материале |
| SEO Школа / olegweb | 7–13 шагов, мало GEO | 8 шагов + чеклист 15–20 пунктов + GEO-блок |
| GEO-гайды (Habr, trigub) | Видимость в AI, не написание | Как **написать** текст, который AI процитирует |
| Pikapuka / агентства | E-E-A-T-кейсы, CTA | Практика для владельца блога, tone Excalibur |

**H2-каркас (из карточки B01 + research):**

1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, списки, таблицы, «острова смысла»
3. FAQ и schema — зачем и как (BlogPosting + FAQPage, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

**Режим B:** сама статья B01 — эталон формата: 8 500–9 500 знаков текста, 5–7 FAQ, workflow `→`, таблица SEO vs GEO (comparison element).

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead, 40–60 слов | «SEO-статья — …» |
| Определение GEO | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Front-loading | Каждый H2 | Первые 2–3 предложения = прямой ответ |
| FAQ | Конец | 5–7 пар, ответ 2–4 предложения |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Island test | QA | Блок понятен без соседних |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и медиана ТОПа; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~55–60 знаков), H1 на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting + FAQPage.
6. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность, переобход.

---

## 7. Риски и blockers для writer

- Не выдумывать Wordstat-цифры до восстановления MCP.
- Не копировать структуру конкурента 1:1 (особенно Pikapuka 7 разделов, olegweb 13 шагов).
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Без эмодзи, без VPN/обход блокировок.
- **ЗАПРЕЩЕНО на research-шаге:** писать `article.html`.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate PASS | ✅ |
| utility_verdict + reader_outcome + action_outline | ✅ |
| SERP ≥ 3 конкурента (WebSearch) | ✅ (8) |
| Таблица фактов ≥ 10 с URL | ✅ (22) |
| Wordstat | ⚠️ MCP недоступен — семантика экспертная |
| GEO hooks + FAQ | ✅ |
| H2 outline | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
