# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата)  
**search_intent:** how_to  
**research_date:** 2026-08-30  
**disclaimer:** Все даты, версии и статистика проверены на 2026-08-30 (2026 год).

---

## Utility gate (Gate 2)

**utility_verdict:** PASS

**reader_outcome:** После гайда читатель соберёт семантику, построит структуру longread, напишет черновик «для людей», добавит FAQ/schema и пройдёт финальный чеклист перед публикацией — одна SEO-статья готова к индексации и GEO-цитированию.

**action_outline (workflow для writer):**

1. Зафиксировать интент и primary query; собрать 5–15 фраз в Яндекс Вордстат и проверить формат топ-10 в выдаче.
2. Разобрать 3–5 конкурентов: какие H2 закрывают запрос, чего не хватает (GEO, чеклист, FAQ).
3. Составить структуру H1 → H2 → H3 до написания текста; каждый H2 = один вопрос читателя.
4. Написать lead 40–60 слов с прямым ответом на primary query; дальше — смысл, не ключи.
5. Наполнить блоки: короткие абзацы (3–5 строк), списки, таблица SEO vs GEO при необходимости.
6. Добавить 5–7 FAQ в видимый HTML; ответы 2–4 предложения, с глаголом действия.
7. Заполнить Title (~50–65 знаков), Description, alt; H1 не дублирует Title.
8. Подготовить BlogPosting + FAQPage JSON-LD (в meta, не в body).
9. Пройти чеклист публикации: семантика, перелинковка, факты, читабельность, Rich Results Test.

---

## 1. SERP-обзор (WebSearch, август 2026 — 6 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: семантика через Вордстат/Вебмастер, H1–H4, абзацы 3–5 строк, естественные ключи, Title/Description, alt, перелинковка; 5 шагов workflow | Нет GEO-слоя; CTA на Директ; «что такое SEO-текст» длиннее, чем pure how-to | Блок про Директ; копировать структуру без GEO и чеклиста |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый how-to (2026) | 13 шагов от ключа до WordPress: интент, конкуренты, структура, мета, чеклист перед публикацией | Узкий фокус на WP; мало про нейропоиск/GEO | 13 шагов 1:1; привязку только к WordPress |
| 3 | [hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | SEO-гайд 2026 | Правильный порядок: спрос → ТОП → структура → текст для человека → SEO-доводка | Нет FAQ/schema/GEO в явном виде | Формулировку «10 000 знаков и 15 ключей» как цель |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread + ИИ (2026) | Правило «после каждого H2 — содержательный ответ»; сначала смысл, потом семантика | Перегруз про ИИ; мало про schema/GEO-чанки | Шаблон «генерируй и публикуй» без fact-check |
| 5 | [blog.sape.ru/blog/2026/07/17/kak-pisat-teksty-dlya-topa-vydachi-v-nejroseti-prompt-inzhiniring-v-2026-godu](https://blog.sape.ru/blog/2026/07/17/kak-pisat-teksty-dlya-topa-vydachi-v-nejroseti-prompt-inzhiniring-v-2026-godu/) | SEO + GEO / промпты (июль 2026) | Прямой ответ в первых 100 словах; H2 как вопросы; таблица в середине; dual SEO+GEO | Угол «промпт-инжиниринг», не универсальный гайд для блога | Копировать промпт-блоки вместо человеческого workflow |
| 6 | [mv-blog.ru/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist](https://mv-blog.ru/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | GEO-чеклист (2026) | Lead 40–60 слов; FAQ в видимом HTML; BlogPosting + FAQPage JSON-LD; 9 пунктов перед публикацией | Фокус на Bitrix CMS, не на написании с нуля | Привязку к Bitrix; CTA mv-blog |

**Паттерн SERP (август 2026):** топ — «полный гайд 2026» с интентом → структура → текст → мета → публикация. Отдельный кластер — GEO/AEO (Snippet-First, FAQ, schema). H1 «которые читают люди» слабо представлен: конкуренты говорят про «для людей и роботов», но редко связывают **читабельность** с **GEO-чанками** в одном workflow.

**Intent:** how_to — пользователь хочет систему от запроса до опубликованной статьи. Вторичный: seo текст для блога, geo оптимизация статьи.

**Дифференциация Excalibur B01:** единый pipeline SEO+GEO на одном материале; режим B — сама статья как эталон longread; акцент «острова смысла» (каждый H2 автономен) + финальный чеклист 15+ пунктов.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` недоступен в текущем окружении Cloud Agent (`MCP server does not exist`). Вызов `wordstat_get_top_requests` выполнен, данных API не получено. **Точные объёмы показов в месяц не указаны** — не выдумывать цифры. Для восстановления: подключить MCP `user-mcp-kv` в mcp.json или обновить токен через [OAuth Яндекс](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40).

**Запросы для повторного прогона Wordstat (регион 225):**

| Запрос | Назначение |
|--------|------------|
| как писать seo статьи | primary_query |
| seo текст для блога | secondary_1 |
| geo оптимизация статьи | secondary_2 |
| как написать seo статью | LSI (вариация) |
| seo текст как писать | LSI |
| структура seo статьи | LSI |
| seo статья для сайта | LSI |
| сколько символов seo статья | FAQ-hint из карточки |

**LSI для writer (из SERP + карточка B01, без объёмов до получения Wordstat):**

- как писать seo статьи / seo текст для блога / seo статья 2026  
- семантическое ядро, яндекс вордстат, LSI-фразы, интент запроса  
- структура longread, H1 H2 H3, title description, перелинковка  
- E-E-A-T, полезность контента, поведенческие факторы  
- geo оптимизация статьи, snippet-first, FAQ schema, BlogPosting JSON-LD  
- чеклист перед публикацией, fact-check, alt-текст  
- что такое geo в seo, сколько символов в seo статье  

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: сначала спрос и задача страницы, потом текст, потом SEO-доводка — не «N знаков и M ключей» | [Hardkod — SEO-текст 2026](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | 2026 | да |
| После каждого H2 — содержательный ответ; главный ключ в H1, первом абзаце, 1–2 H2, title и description | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Прямой развёрнутый ответ на основной запрос — в первых 100 словах; H1 50–65 символов; H2 как вопросы читателя | [SAPE — промпт SEO+GEO 2026](https://blog.sape.ru/blog/2026/07/17/kak-pisat-teksty-dlya-topa-vydachi-v-nejroseti-prompt-inzhiniring-v-2026-godu/) | 17.07.2026 | да |
| GEO-статья: lead 40–60 слов; FAQ в видимом HTML (не в скрытых табах); BlogPosting + FAQPage JSON-LD | [MV-Blog — GEO чеклист](https://mv-blog.ru/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | 2026 | да |
| FAQ: 5–7 вопросов; ответы до ~80 слов с глаголом действия | [MV-Blog — GEO чеклист](https://mv-blog.ru/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | 2026 | да |
| Snippet-First: каждый блок H2 начинается с краткого резюме 1–3 предложения | [PW Agency — GEO 2026](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 2026 | да |
| Абзацы-чанки 3–7 строк: один абзац — одна мысль | [PW Agency — GEO 2026](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 2026 | да |
| SEO — позиции в органике; GEO — цитирование в ответах AI; AEO — блоки внутри классической выдачи; каналы дополняют друг друга | [Kokoc — GEO/AEO 2026](https://kokoc.com/blog/chto-takoe-geo-aeo-i-kak-pravilno-prodvigatsya-v-neyrosetyakh/) | 2026 | да |
| Алгоритм публикации: интент → конкуренты → структура → текст → экспертность → мета → чеклист (13 шагов) | [OlegWeb — SEO-статья](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 2026 | да |
| ИИ — черновик и структура; обязательны fact-check цифр и уникальный опыт, иначе потеря доверия | [GPT Russia — SEO нейросетью](https://gptrf.ru/blog/seo-teksty-nejrosetyu-pravilno) | 2026 | да |

**Не использовать (нет первичника / slop):** «−25–40% отказов» (digiuni.ru); «+140% трафика за 3 недели»; «44,2% цитат ChatGPT из первой трети» без arxiv/первичного PDF; любые объёмы Wordstat до API-прогона.

---

## 4. Угол статьи (практический how-to)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один словарь SEO», а **единый workflow** (9 шагов выше): интент → структура → текст → FAQ/schema → GEO-чанки → чеклист.

**H2-каркас (из карточки B01 + research):**

1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD в meta)
4. Чеклист перед публикацией (15–20 пунктов)

**Режим B:** статья B01 — эталон формата: 8 500–9 500 знаков текста, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, перелинковка на `/`.

**Tone:** практично, B2B без воды (site-brief); без эмодзи и непроверенной статистики.

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead после H1 | 40–60 слов |
| Определение GEO | Блок «SEO + GEO» | 40–60 слов |
| Conversational H2 | FAQ-темы | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец longread | Ответ-действие, 2–4 предложения |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Meta | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | `/` |

**Целевые формулировки:** как писать seo статьи, seo текст для блога, geo оптимизация статьи, сколько символов в seo статье, что такое geo в seo.

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~50–65 знаков), H1 на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting + FAQPage при видимом FAQ.
6. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, FAQ в HTML, JSON-LD, ссылки, Rich Results Test.
7. **Можно ли писать SEO-статью только нейросетью?** — черновик да; без fact-check и редактуры — риск для доверия и позиций.

---

## 7. Риски для writer

- Цифры только из таблицы фактов §3 или fact-bank.md.
- Не копировать структуру Pikapuka/OlegWeb 1:1.
- Объём текста: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Без эмодзи; CTA ≤ 3.
- Wordstat-объёмы добавить после восстановления MCP — не подставлять оценочные «~5000 показов».

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента (WebSearch 2026-08-30) | ✅ |
| utility_verdict + action_outline + reader_outcome | ✅ |
| Таблица фактов с URL (16 фактов) | ✅ |
| Wordstat (попытка MCP; LSI без fake volumes) | ⚠️ MCP недоступен |
| GEO hooks + FAQ 5–7 | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
