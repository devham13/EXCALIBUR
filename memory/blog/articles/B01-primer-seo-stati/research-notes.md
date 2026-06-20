# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-06-20  
**disclaimer:** Все даты, версии и статистика проверены на 20.06.2026.

---

## utility_verdict: PASS

**reader_outcome:** Читатель сможет пройти полный цикл — от сбора семантики и каркаса H2 до финального чеклиста — и опубликовать SEO+GEO longread, который закрывает запрос человека и готов к цитированию в нейропоиске.

**action_outline:**

1. **Интент и семантика** — определить тип запроса (how-to / comparison / commercial), собрать primary + 3–5 LSI-групп в Яндекс Вордстат и подсказках; сгруппировать в кластер.
2. **SERP-разбор** — выписать H2/H3, объём и формат (гайд, чек-лист, FAQ) у топ-5 конкурентов; закрыть пробелы, не копировать структуру 1:1.
3. **Каркас longread** — H1 (один), 4–6 H2 из карточки B01; после каждого H2 — прямой ответ 40–80 слов, затем детали.
4. **Lead и инфостиль** — первый абзац: определение + польза за 150–200 знаков; абзацы 3–5 строк, списки вместо «простынь».
5. **Текст с E-E-A-T lite** — кейс/наблюдение автора, ссылки на первичные источники, без выдуманных процентов.
6. **Мета и ключи** — Title (50–65 знаков, ≠ H1), Description (140–180 знаков); ключ в H1, первом абзаце и 1–2 H2 естественно.
7. **GEO-слой** — FAQ 5–7 пар, атомарные «острова смысла», упоминание llms.txt; даты datePublished/dateModified.
8. **Schema handoff** — BlogPosting + FAQPage (JSON-LD вне body); внутренняя ссылка на `/`.
9. **Чеклист перед публикацией** — семантика, мета, читабельность, FAQ, schema, ссылки, island-test по каждому H2.

---

## 1. SERP-обзор (WebSearch Cursor, 20.06.2026)

**Запросы:** «как писать seo статьи 2026», «seo текст для блога 2026», «geo оптимизация статьи 2026», H1 «Как писать SEO-статьи, которые читают люди 2026».

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: нет универсального объёма, H1 один, абзацы 3–5 строк, Wordstat, естественность ключей | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа |
| 2 | [olegweb.ru/.../kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм (обнов. 05.02.2026) | 13 шагов от темы до публикации; интент, SERP-разбор, чек-лист; акцент на опыт автора | WordPress-уклон; GEO вторичен | 13-шаговую структуру 1:1 |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-...](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Семантические кластеры, E-E-A-T, GEO-блок, промпты для нейросетей | Часть цифр без первичника (CTR +15–30%, «60% mobile») | Непроверенные проценты |
| 4 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-...](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский чек-лист (май 2026) | Семантика → E-E-A-T → Schema Article+FAQPage; Title ~65 знаков | Кейсы «+140%» без верификации | Agency-цифры в кейсах |
| 5 | [qvai.ru/media/kak-pisat-seo-stati](https://qvai.ru/media/kak-pisat-seo-stati) | Гайд «которые читают люди» | Близкий intent к H1 B01; баланс SEO и читабельности | Слабее GEO-слой | Заголовок без нашего workflow SEO+GEO |
| 6 | [seojazz.ru/blog/tekstovaja-optimizacija-v-2026-godu-...](https://seojazz.ru/blog/tekstovaja-optimizacija-v-2026-godu-rabota-s-kontentom-dlja-uluchshenija-relevantnosti-i-relevantnye-tegi/) | Текстовая оптимизация 2026 | Формулы Title/Description, AIO-чанки 120–180 слов, ревизия каждые 6–12 недель | Мало «с нуля» для блогера | Копировать формулы без адаптации под B01 |
| 7 | [mayai.ru/geo-seo-optimizaciya-neyropoisk](https://mayai.ru/geo-seo-optimizaciya-neyropoisk/) | GEO чек-лист 2026 | 15 пунктов P0/P1, answer-first 40–80 слов, FAQPage = видимый FAQ | Фокус GEO, не базовое написание | Весь чеклист как основной каркас |
| 8 | [habr.com/ru/articles/1042732](https://habr.com/ru/articles/1042732/) | GEO/AEO Habr 2026 | RAG-архитектура нейропоиска, 7 принципов GEO | Техничнее аудитории «пишу статью сам» | Перегруз RAG-терминами |
| 9 | [trigub.ru/geo-v-2026-godu](https://trigub.ru/geo-v-2026-godu/) | GEO практик 2026 | Answer-first после H2; различия Алисы vs AI Overviews; sameAs/Person | Не учит писать SEO-текст с нуля | Слепой перенос западных гайдов (автор: −40% эффекта) |

**Паттерн SERP (июнь 2026):** два кластера — «SEO-текст 2026» (E-E-A-T, Wordstat, чек-лист, ИИ как помощник) и «GEO-оптимизация 2026» (answer-first, FAQ, schema, llms.txt). Прямого совпадения с H1 «которые читают люди» + единый workflow SEO+GEO в одном материале почти нет.

**Intent:** `how_to` — пользователь хочет пошаговую систему: семантика → структура → текст → мета → FAQ/schema → GEO → проверка. Вторичный intent: связать SEO и GEO без двойной работы.

**Дифференциация Excalibur B01:** единый workflow «для людей и для машин»; режим B — сама статья как эталон longread 8 500–9 500 знаков; читабельность как SEO-фактор (острова смысла, инфостиль), не «ещё один список ключей».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 20.06.2026)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в текущей Cloud-сессии (`Server "user-mcp-kv" not found`). Инструмент `wordstat_get_top_requests` не вызывался — **точные показы/мес не получены**. Для восстановления: подключите MCP в Cursor и при ошибке 401 обновите OAuth-токен через [Yandex OAuth](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40).

### Экспертная семантика (без API; для writer до появления Wordstat)

| Фраза (приоритет) | Роль | Источник оценки |
|-------------------|------|-----------------|
| как писать seo статьи | primary_query | карточка B01, SERP |
| seo текст для блога | secondary | карточка B01, SERP |
| geo оптимизация статьи | secondary | карточка B01, SERP-кластер GEO |
| как написать seo статью | LSI | olegweb.ru, pikapuka.com в топе |
| seo копирайтинг 2026 | LSI | 1ps.ru, dzen.ru |
| e-e-a-t seo текст | LSI | pikapuka, seojazz |
| seo текст структура h2 | LSI | analito.ru, qvai.ru |
| сколько символов seo статья | FAQ-intent | faq_hints B01, SERP |
| что такое geo в seo | FAQ-intent | faq_hints B01, audit4seo, habr |
| llms.txt seo | LSI GEO | mayai.ru, digitalimpuls |
| faq schema seo статья | LSI | pikapuka, mayai.ru |
| seo статья чеклист | LSI | olegweb.ru, pikapuka |

**SEO-стратегия (до Wordstat):** primary в H1/Title/lead; secondary и FAQ-формулировки — в H2-вопросах и FAQ-блоке; LSI — естественно по тексту, без переспама.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title: 50–60 знаков; Description: 140–180 знаков; H1 ≠ Title | [SEO Jazz — текстовая оптимизация 2026](https://seojazz.ru/blog/tekstovaja-optimizacija-v-2026-godu-rabota-s-kontentom-dlja-uluchshenija-relevantnosti-i-relevantnye-tegi/) | 2026 | да |
| Первые 100–150 слов / краткое резюме под H2 — зона для AI-извлечения | [SEO Jazz — базовые SEO 2026](https://seojazz.ru/blog/bazovye-seo-trebovanija-v-2026-godu-fundamentalnye-pravila-poiskovoj-optimizacii-sajta/) | 2026 | да |
| Ревизия ключевых страниц — план каждые 6–12 недель | [SEO Jazz — базовые SEO 2026](https://seojazz.ru/blog/bazovye-seo-trebovanija-v-2026-godu-fundamentalnye-pravila-poiskovoj-optimizacii-sajta/) | 2026 | да |
| H1 должен отличаться от Title; Title ~65 знаков с триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Schema.org: Article + FAQPage для структуры и сниппета | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| После каждого H2 — 1–2 абзаца с прямым ответом, затем развёрнутый разбор (answer-first) | [Тригуб — GEO 2026](https://trigub.ru/geo-v-2026-godu/) | 2026 | да |
| GEO SEO: answer-first 40–80 слов; FAQPage schema = видимый FAQ на странице | [mayai.ru — GEO SEO чек-лист](https://mayai.ru/geo-seo-optimizaciya-neyropoisk/) | 2026 | да |
| Google AI Overviews: SEO остаётся базой; llms.txt optional, не замена sitemap | [mayai.ru — GEO SEO чек-лист](https://mayai.ru/geo-seo-optimizaciya-neyropoisk/) | 2026 | да |
| Нейропоиск (Perplexity, Алиса AI, AI Overviews) работает по RAG: поиск документов → извлечение фактов → генерация ответа | [Habr — GEO/AEO 2026](https://habr.com/ru/articles/1042732/) | 2026 | да |
| Смысловой кластер — 3–5 групп связанных запросов из Wordstat и подсказок | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Первые 30–50 слов должны давать прямой ответ на главный запрос | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Пошаговый алгоритм SEO-статьи: тема → интент → SERP → структура → ключи → экспертность → публикация (13 шагов) | [olegweb.ru — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Принцип «интент > частотность»: информационный запрос → гайд; коммерческий → цены и CTA | [Дзен — SEO-тексты 2026](https://dzen.ru/a/agQaAEwMsxSUd7wZ) | 2026 | да |
| Прямой ответ на первом экране — ориентир ≤150–200 знаков | [Дзен — SEO-тексты 2026](https://dzen.ru/a/agQaAEwMsxSUd7wZ) | 2026 | да |

**Не использовать без первичника:** «+140% трафика» (Pikapuka); «Description +15–30% CTR», «60% mobile» (1ps.ru); «GEO +30–40% visibility» (digitalapplied — исследование Princeton, упоминать осторожно); «−40% эффекта переноса гайдов» (trigub.ru — оценка автора).

---

## 4. Угол статьи и H2-каркас

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска (GEO). Единый workflow, не два проекта.

**H2 из карточки B01 (+ research):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как  
4. Чеклист перед публикацией  

**Подтемы внутри блоков:** Wordstat/кластер, Title/Description, E-E-A-T lite, llms.txt, AI-краулеры в robots.txt.

**Режим B:** статья B01 — эталон: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением, перелинковка на `/`.

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead | 40–60 слов |
| Определение GEO | Блок «SEO + GEO» | 40–60 слов |
| Conversational H2 | «Что такое GEO в SEO?», «Сколько символов…» | Вопрос в заголовке |
| FAQ 5–7 | Конец longread | 2–4 предложения на ответ |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA | Блок понятен без соседних |
| Schema | Вне body | BlogPosting + FAQPage |
| Даты | Метаданные | 2026-06-20 |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — дополнение к SEO: цитирование в AI-ответах при индексируемом структурированном контенте.  
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (50–65 знаков), H1 на странице; не дублировать.  
5. **Какие schema для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.  
6. **Что такое llms.txt?** — optional файл для AI-краулеров; не замена sitemap.  
7. **Как проверить статью перед публикацией?** — чеклист из action_outline, шаг 9.

---

## 7. Риски для writer

- Цифры только из таблицы фактов §3 и fact-bank.md.  
- Не копировать Pikapuka/olegweb 1:1.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Без эмодзи; site_url — `/` по карточке.  
- Wordstat-показы добавить после восстановления MCP (блок §2).

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента (свежий WebSearch) | ✅ |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL (≥15) | ✅ |
| action_outline + reader_outcome | ✅ |
| utility_verdict PASS | ✅ |
| GEO hooks + FAQ | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
