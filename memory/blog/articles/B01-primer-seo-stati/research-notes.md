# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата на самой статье)  
**research_date:** 2026-08-08  
**disclaimer:** Все даты, версии и статистика проверены на 08.08.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch, август 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Авторитет; 5 шагов (тема → семантика → структура → текст → оптимизация); Wordstat/Вебмастер; «плохо/хорошо»; естественность ключей; абзацы 3–5 строк | Нет GEO/нейропоиска; CTA Директа; мало финального чек-листа | Блок про Директ; копировать H1–H4 без GEO-слоя |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii/) | Longread 2026 + ИИ | Кластеризация Wordstat; H2 как вопросы; LSI без переспама; краткая инструкция в начале | Перегруз про «полный гайд с ИИ»; мало связки SEO+GEO в одном workflow | Дублировать 10+ разделов 1:1 |
| 3 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 13 шагов | Интент → SERP → структура → WordPress → мета → перелинковка → pre-publish | Длинный WP-фокус; GEO как побочный эффект | Копировать 13 шагов без сжатия в actionable workflow |
| 4 | [serptop.ru/blog/kak-pisat-seo-teksty](https://serptop.ru/blog/kak-pisat-seo-teksty/) | Гайд + чек-лист | Формула H1 «ключ + польза»; skeleton H2 (что/как/ошибки/CTA); мета ≤70/160 | Мало GEO; чек-лист без приоритетов | Agency-tone «получать клиентов» как главный месседж |
| 5 | [blog.sape.ru/blog/2026/07/17/kak-pisat-teksty-dlya-topa-vydachi-v-nejroseti-prompt-inzhiniring-v-2026-godu](https://blog.sape.ru/blog/2026/07/17/kak-pisat-teksty-dlya-topa-vydachi-v-nejroseti-prompt-inzhiniring-v-2026-godu/) | SEO + GEO + промпты (июль 2026) | H1 50–65 символов; lead 80–100 слов = прямой ответ; H2-вопросы; dual intent (органика + генеративная выдача) | Уклон в prompt-engineering; цифры SparkToro без первичника в тексте | Копировать блоки промптов как основу статьи |
| 6 | [divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | DIY 6 шагов | Wordstat 15–25 фраз от 50 показов; группировка LSI; «не считайте плотность вручную» | Короткий; нет FAQ/schema | Формулировки «просто следуйте» без чек-листа |
| 7 | [likacloud.com/ru/guide/seo/seo-optimize-checklist](https://www.likacloud.com/ru/guide/seo/seo-optimize-checklist/) | On-page чек-лист | Title/Description/H1–H3; FAQ-шаблон; критерии приёмки | Не учит писать текст с нуля | Копировать таблицы 1:1 |

**Паттерн SERP (авг. 2026):** топ — «полный гайд 2026» с E-E-A-T, Wordstat, 6–13 шагов; свежий слой — **SEO + генеративная выдача** (Sape, 1PS). Прямого совпадения с H1 «которые читают люди» в топ-5 почти нет: конкуренты продают «топ выдачи» или «SEO-тексты», а не **читабельность как SEO-фактор**.

**Intent:** `how_to` — пользователь хочет **систему**: проверить спрос → интент → структура → текст → мета/schema → финальный чеклист. Вторичный intent (из карточки): **SEO + GEO в одной статье**, не два отдельных проекта.

**Пробел для Excalibur:** единый **workflow за одну сессию** (60–90 мин): от blank page до publish-ready longread с FAQ/schema и GEO-чанками; акцент «для людей» = структура + lead + island test, а не «ещё один список ключей».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, регион 225, 08.08.2026)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в текущем Cloud-окружении (вызов `wordstat_get_top_requests` завершился ошибкой «MCP server does not exist»). Точные объёмы показов **не получены** — в тексте статьи нельзя указывать частотность без повторного прогона Wordstat.

**Действие для пайплайна:** обновить OAuth-токен и повторить вызов через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (без цифр спроса — только для writer до восстановления MCP)

**Primary:** как писать seo статьи  

**Secondary (из карточки B01):** seo текст для блога, geo оптимизация статьи  

**LSI-кандидаты (из SERP + конкурентов, вписывать органично):**

- как написать seo статью, seo текст для сайта, как писать seo тексты  
- семантическое ядро, яндекс вордстат, lsi слова, поисковый интент  
- структура seo статьи, заголовки h1 h2 h3, title description  
- мета теги, микроразметка schema faqpage, blogposting  
- e-e-a-t, чеклист перед публикацией, внутренние ссылки  
- geo оптимизация, generative engine optimization, нейропоиск, answer-first  
- сколько символов в seo статье, что такое geo в seo (faq_hints из карточки)

**SEO-стратегия для writer:** primary в H1/lead/Title; secondary в H2 и FAQ; LSI — по разделам, без keyword stuffing (канон Яндекса и Google).

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — он зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Google: контент для людей, не для манипуляции выдачей; SEO допустимо, если применено к people-first контенту | [Google Search Central — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 08.2026 | да |
| Google: E-E-A-T (Experience, Expertise, Authoritativeness, Trust); trust — ключевой | [Google Search Central — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 08.2026 | да |
| Google: нет «предпочтительного word count» — писать столько, сколько нужно для полного ответа | [Google Search Central — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 08.2026 | да |
| H1 — один; иерархия H1 → H2 → H3 без пропусков уровней | [petr-panda.ru — структура статьи](https://petr-panda.ru/struktura-stati-seo-opredelenie/) | 2026 | да |
| Meta description — ориентир до 160 символов; влияет на CTR, не на ранжирование напрямую | [petr-panda.ru — структура статьи](https://petr-panda.ru/struktura-stati-seo-opredelenie/) | 2026 | да |
| Title — ориентир ≤60–70 символов с основным ключом | [serptop.ru — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| Description — ориентир ≤160 символов с пользой и CTA | [serptop.ru — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| H1 ≠ Title: Title для сниппета, H1 — заголовок на странице | [evaris.ru — on-page SEO](https://evaris.ru/obuchenie/seo-osnovy/vnutrennyaya-optimizaciya/) | 2026 | да |
| Для генеративной выдачи: H1 50–65 символов, ключ в начале; lead 80–100 слов = прямой ответ | [Sape — промпт-инжиниринг SEO/GEO 2026](https://blog.sape.ru/blog/2026/07/17/kak-pisat-teksty-dlya-topa-vydachi-v-nejroseti-prompt-inzhiniring-v-2026-godu/) | 17.07.2026 | да |
| H2 лучше формулировать как вопросы пользователей — для сниппетов и AI-ответов | [Sape — промпт-инжиниринг SEO/GEO 2026](https://blog.sape.ru/blog/2026/07/17/kak-pisat-teksty-dlya-topa-vydachi-v-nejroseti-prompt-inzhiniring-v-2026-godu/) | 17.07.2026 | да |
| Schema.org: Article/BlogPosting + FAQPage для структуры и расширенных сниппетов | [serptop.ru — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| GEO (Generative Engine Optimization) дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого контента | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Нейросети извлекают пассажи (passages), не страницы целиком — каждый H2 = «остров смысла» | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Первые 100–150 слов — ключевая зона для извлечения ответа AI | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Главная задача статьи — полный ответ; возврат пользователя в поиск = сигнал низкого качества | [maryproject.ru — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**fact-bank.md:** прямых фактов про SEO-writing нет — использовать только таблицу выше.

**Не использовать без оговорки / первичника:** «68% запросов Google без клика» (SparkToro, цит. Sape); «+140% трафика за 3 недели»; «микроразметка ×1,5–2 цитирование» без arXiv/официального источника.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист 15–20 пунктов.

**Почему отличается от конкурентов:**
- Яндекс Direct даёт канон SEO без GEO-слоя.
- Sape/1PS уводят в промпты и ИИ; Excalibur — **ручной workflow** с human-in-the-loop.
- H1 «которые читают люди» слабо раскрыт в SERP — наш фокус: **читабельность = SEO** (lead, абзацы, island test) + техника.

**Режим B:** сама статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, внутренняя ссылка на `/`.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (один контент, две выдачи)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

**Tone (site-brief):** практично, B2B без воды; без эмодзи; дефис вместо длинного тире.

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO — …» |
| Conversational H2 | FAQ-adjacent | «Что такое GEO в SEO?», «Сколько символов…?» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, action-first |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; 3–4 предложения в абзаце |
| Island test | QA | Блок понятен без соседних |
| Schema | Не в HTML body | BlogPosting + FAQPage |
| llms.txt | Упоминание в GEO-блоке | Опциональный сигнал для AI-краулеров |
| Внутренняя ссылка | Из карточки | `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и конкуренты; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + LSI/тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (~60–70 знаков), H1 — на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt и нужен ли он блогу?** — файл для AI-краулеров; полезный сигнал, не замена sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать частотность Wordstat (MCP недоступен).
- Не копировать структуру olegweb (13 шагов) или Pikapuka 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи, без VPN/обход блокировок.
- Цифры только из таблицы фактов §3.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за одну рабочую сессию соберёт семантику по primary query, построит структуру longread с lead и H2-вопросами, напишет черновик без переспама, оформит Title/Description/FAQ/schema, добавит GEO-чанки (answer-first блоки) и пройдёт финальный чеклист перед публикацией в WordPress или CMS.

**action_outline (how-to, 8 шагов):**

1. **Проверить спрос и интент:** вбить «как писать seo статьи» в выдачу; отметить тип страниц (гайд vs коммерция); выписать 3–5 пробелов конкурентов; собрать 15–25 фраз в Wordstat (primary + LSI), сгруппировать в 3–5 кластеров.
2. **Разобрать ТОП-5 SERP:** длина, структура H2, форматы (списки/таблицы/FAQ); зафиксировать минимальный набор подтем для полноты ответа.
3. **Собрать outline до текста:** один H1; 4–6 H2 (в т.ч. вопросы из faq_hints); под каждым H2 — тезис первого абзаца; lead = прямой ответ в 80–100 словах.
4. **Написать черновик «для людей»:** абзацы 3–5 строк; ключ в H1, lead и 1–2 H2 естественно; LSI по разделам; таблица или список там, где упрощает выбор.
5. **Добавить E-E-A-T lite:** автор/редакция, один кейс или пример workflow, ссылки на 2–3 авторитетных источника (Яндекс/Google), без выдуманных процентов.
6. **Упаковать для GEO:** после каждого H2 — самодостаточный «остров»; FAQ 5–7 с короткими action-ответами; при необходимости упомянуть llms.txt.
7. **Техника on-page:** Title ≤70, Description ≤160, alt у изображений, 3–5 внутренних ссылок, slug с ключом; JSON-LD BlogPosting + FAQPage (в schema-агенте, не в body).
8. **Финальный чеклист 15–20 пунктов:** семантика, мета, один H1, FAQ, schema handoff, перелинковка, proofread, island test — только после ✅ публиковать.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (7) |
| Wordstat MCP | ⚠️ сервер недоступен; LSI — экспертно |
| Таблица фактов с URL | ✅ (21 факт) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| reader_outcome | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
