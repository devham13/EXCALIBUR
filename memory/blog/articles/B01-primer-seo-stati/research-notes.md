# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + чеклист)  
**research_date:** 2026-08-29  
**disclaimer:** Все даты, версии и статистика проверены на 29.08.2026.

---

## 1. SERP-обзор (WebSearch, август 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Агентский longread (обновлён 15.06.2026) | Семантические кластеры 3–10 запросов; таблица «было/стало» 2026; блок про ИИ + E-E-A-T; Wordstat в workflow | Длинный sales-narrative агентства; GEO без практического чеклиста для блога | Копировать 20-минутную структуру 1:1; непроверенные кейсы |
| 2 | [texterra.ru — чек-лист SEO-контента 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Редакционный чек-лист (04.06.2026) | 9 критериев качества; E-E-A-T + ЭПОС Яндекса; AI-выдача (OAI-SearchBot vs GPTBot); answer-first | Мало пошагового «с нуля» для новичка; без JSON-LD примеров | Продажа услуг «обновим ваши статьи» вместо инструкции |
| 3 | [hardkod.ru — как написать SEO-статью](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | Технический гайд (обновлён 17.08.2026) | Чёткий порядок: интент → семантика → ТОП → структура → черновик → SEO-доработка; примеры плохо/хорошо | Нет GEO-слоя; CTA на SEO-услуги | Копировать 6 шагов без дифференциации «для людей» |
| 4 | [direct.yandex.ru — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный канон Яндекса (27.01.2026) | Wordstat, естественность ключей, H1–H4, объём без нормы, абзацы 3–5 строк | Нет нейропоиска/GEO; коммерческий контекст Директа | CTA Директа; «универсальная формула объёма» |
| 5 | [it-agency.ru — SEO-статьи с ИИ](https://www.it-agency.ru/academy/good-article-using-ai/) | Практик + промпты (2026) | Требования к H2/H3 (вводный абзац, не «склейка»); блоки «Важно/Совет»; human-in-the-loop | Узкий фокус на ИИ-pipeline, не полный SEO-workflow | Шаблоны промптов без контекста блога |
| 6 | [zvonkooo.ru — GEO-оптимизация](https://www.zvonkooo.ru/blog/geo-optimizatsiya-otvety-ai/) | GEO-гайд (28.04.2026) | 6 правил GEO-цитируемости; замеры AI-видимости; список AI-краулеров | Не учит писать SEO-статью с нуля | Цифры ROI без первичника |
| 7 | [impact-dl.ru — GEO и ответы ИИ 2026](https://impact-dl.ru/geo-otvety-ii-2026-chto-pomogaet-popast-v-citatu/) | Критический GEO-разбор (2026) | FAQ/Schema — не главный рычаг цитирования; акцент на ясный ответ, факты, доступ краулеров | Мало how-to по написанию текста | Продавать GEO «только через Schema» |

**Паттерн SERP:** топ — «полный гайд 2026» + чек-листы (E-E-A-T, семантика, структура). Отдельный кластер — GEO для AI-выдачи. Прямого совпадения с H1 «которые читают люди» мало: конкуренты говорят про «качество» и «полезность», но редко связывают читабельность с пошаговым workflow SEO+GEO.

**Intent:** `how_to` — пользователь хочет алгоритм: семантика → структура → черновик → мета → FAQ/schema → GEO-чанки → финальный чеклист. Вторичный intent: «seo текст для блога», «geo оптимизация статьи».

**Пробел Excalibur:** единый практический workflow «SEO + GEO в одной статье» с акцентом на **читаемость** (острова смысла, lead-абзац, чеклист 15+ пунктов) — режим B, сама статья как эталон.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

> ⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в этом Cloud Agent run (namespace not found). Инструмент `wordstat_get_top_requests` не вызван. Точные показы в месяц **не получены**. Обновите токен и подключите MCP: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (без цифр спроса — только для ориентира writer)

**Кластер primary («как писать seo статьи»):**  
как написать seo статью, seo текст как писать, seo статья для сайта, seo копирайтинг 2026, структура seo статьи, семантическое ядро для статьи, оптимизация текста для поиска.

**Кластер secondary («seo текст для блога»):**  
seo текст для блога, статья для блога seo, longread seo, контент для блога seo, title description для статьи блога.

**Кластер GEO («geo оптимизация статьи»):**  
geo оптимизация статьи, geo seo, оптимизация под ai поиск, цитирование в нейроответах, llms.txt для блога, faq schema для ai.

**FAQ-хвосты (из карточки B01 + SERP):**  
сколько символов в seo статье, что такое geo в seo, чем title отличается от h1, нужен ли переспам ключей 2026, какие schema для seo статьи.

**SEO-стратегия writer:** primary в H1/Title/lead; secondary и LSI — в H2 и FAQ; GEO-формулировки — отдельный блок «SEO + GEO в одной статье», не отдельный sales-пост.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; перечисления — списками | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Google: helpful, people-first content + E-E-A-T; Яндекс: релевантность + ЭПОС (экспертность, полезность, оригинальность, содержательность) | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Базовый принцип 2026: от главного ответа к деталям — сначала суть, потом нюансы | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Для ChatGPT Search не закрывать OAI-SearchBot; GPTBot связан с обучением моделей — это разные боты | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Порядок написания SEO-статьи: интент → семантика → анализ ТОП → структура → черновик для человека → SEO-доработка | [Hardkod — SEO-статья 2026](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | 17.08.2026 | да |
| Заголовки H2/H3 должны отвечать на реальные вопросы, а не существовать ради ключа | [Hardkod — SEO-статья 2026](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | 17.08.2026 | да |
| Одна страница закрывает один смысловой кластер — обычно 3–10 связанных запросов | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| В 2026 приоритет: интент и полнота ответа, LSI-кластер, E-E-A-T, структура для AI-агентов | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| GEO — подготовка контента к извлекаемости и цитированию в AI-ответах; не замена SEO | [Zvonko — GEO-оптимизация](https://www.zvonkooo.ru/blog/geo-optimizatsiya-otvety-ai/) | 28.04.2026 | да |
| FAQ и Schema полезны для SEO-гигиены, но в 2026 не главный рычаг цитирования в AI-ответах | [Impact DL — GEO 2026](https://impact-dl.ru/geo-otvety-ii-2026-chto-pomogaet-popast-v-citatu/) | 2026 | да |
| 51% маркетологов используют нейросети для аналитики и оптимизации, а не для слепой штамповки контента | [fact-bank → mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 11.06.2026 | да |

**Не использовать без первичника:** «+140% трафика за 3 недели»; «64% падение CTR» (generative-optimization.ru — агентский вторичник); «ROI GEO 400–1600%»; «44,2% цитат ChatGPT из первой трети» без arXiv/первичника.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Единый workflow: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс/Hardkod дают канон SEO без связки с GEO-практикой для блога.
- GEO-гайды не учат писать текст с нуля.
- H1 «которые читают люди» — слабо раскрыт в SERP; фокус: **читабельность как SEO-фактор** (острова смысла, короткие абзацы, answer-first).

**H2-каркас (из карточки B01):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD в handoff schema, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

**Режим B:** сама статья B01 — эталон: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2.

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-хвосты | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Короткий ответ 2–4 предложения — действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; абзац 3–5 строк |
| Island test | QA | Блок понятен без соседних |
| llms.txt | GEO-блок | Упоминание для AI-краулеров блога |
| Внутренняя ссылка | Из карточки | На `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и ТОП SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — на странице; не дублировать дословно.
5. **Какие schema для SEO-статьи блога?** — BlogPosting + FAQPage.
6. **Что такое llms.txt?** — манифест для AI-краулеров; дополнение к sitemap, не замена.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность, robots для AI-ботов.

---

## 7. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантический кластер, спроектирует структуру longread с lead и FAQ, напишет черновик «для людей», доработает мета и GEO-чанки и пройдёт финальный чеклист перед публикацией SEO-статьи блога.

**action_outline (для writer):**

1. **Определить интент** одним предложением: какой результат получит человек после прочтения (how-to, не «вообще про SEO»).
2. **Собрать семантику** в Wordstat/Webmaster: primary + 3–5 групп LSI; одна страница = один кластер 3–10 запросов.
3. **Проанализировать ТОП-5 SERP:** какие вопросы закрыты, где пробел; не копировать структуру 1:1.
4. **Составить outline до текста:** H1, 4 H2 из карточки, H3 по FAQ-хвостам; после каждого H2 — содержательный lead-абзац.
5. **Написать черновик для человека:** короткие абзацы 3–5 строк, списки/таблицы, без переспама; E-E-A-T lite (автор, дата, источники фактов).
6. **Доработать SEO-элементы:** Title (~65 зн.), Description, ключ в lead, внутренние ссылки, alt по смыслу картинки.
7. **Добавить GEO-слой:** answer-first в начале, атомарные H2-чанки, блок FAQ 5–7, упоминание llms.txt и доступа AI-краулерам.
8. **Передать schema-агенту:** BlogPosting + FAQPage (JSON-LD вне body).
9. **Пройти чеклист 15–20 пунктов** перед публикацией (семантика, мета, факты, schema, перелинковка, мобильная вёрстка).

---

## 8. Риски для writer

- Не выдумывать статистику Wordstat — показы не получены в этом прогоне.
- Не копировать структуру Pikapuka/1PS 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи; CTA ≤ 3.
- Цифры только из таблицы фактов / fact-bank.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (7) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (16) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
