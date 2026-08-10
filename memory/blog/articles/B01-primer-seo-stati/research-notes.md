# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to + чеклист, эталон формата на самой статье)  
**search_intent:** how_to  
**research_date:** 2026-08-10  
**disclaimer:** Все даты, версии и статистика проверены на 10.08.2026 (2026 год).

---

## Utility gate

**utility_verdict:** PASS  
**reader_outcome:** После гайда читатель сможет самостоятельно собрать SEO+GEO longread для блога — от проверки интента и семантики до структуры, FAQ/schema и финального чеклиста перед публикацией.

**action_outline (workflow для writer):**

1. **Интент и SERP** — открыть топ-5 по «как писать seo статьи», определить формат (how-to vs справочник) и must-have блоки конкурентов.
2. **Семантика** — primary + 5–10 secondary/LSI в Wordstat и Вебмастере; зафиксировать кластер в плане H2.
3. **Каркас longread** — один H1, 4–6 H2 как подзадачи; lead 40–70 слов с прямым ответом; таблица или список в каждом крупном блоке.
4. **Текст для людей** — абзацы 3–5 строк, без воды; ключи естественно в H1, lead и части H2; E-E-A-T lite (автор, опыт, пример).
5. **GEO-слой** — атомарные «острова смысла» в каждом H2; FAQ 5–7 пар; определения SEO и GEO в первых абзацах.
6. **Техника страницы** — Title (~≤60 знаков), Description (140–160), alt у изображений, 3–5 внутренних ссылок, slug с ключом.
7. **Schema** — BlogPosting + FAQPage (JSON-LD вне body); дата публикации/обновления в метаданных.
8. **Финальный чеклист** — пройти 15+ пунктов (семантика, структура, FAQ, schema, читабельность) перед publish.

---

## 1. SERP-обзор (WebSearch, август 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон: workflow тема → семантика → структура → текст; H1–H4; естественность ключей; Wordstat; Title/Description | Нет GEO/нейропоиска; коммерческий хвост Директа | CTA Директа; копировать структуру без GEO-слоя |
| 2 | [olegweb.ru/.../kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый how-to (фев. 2026) | 13 шагов от ключа до WordPress; интент, конкуренты, чек-лист; акцент на поведение читателя | Мало GEO; WordPress-специфика | Копировать 13 шагов 1:1; Telegram-CTA |
| 3 | [roiseo.ru/blog/struktura-seo-stati-dlya-bloga](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон + чеклист (апр. 2026) | Lead 40–70 слов; блоки таблица/пример/ошибки/FAQ; AI-citable формат; Article + FAQPage | Фокус на структуре, не на полном цикле написания | Agency-CTA на услуги ROI SEO |
| 4 | [spilnoagency.com.ua/.../seo-copywriting](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | Инструкция 2026 | Title ≤60, Meta 140–160; 5–8 H2 как вопросы; TL;DR + FAQ; Schema HowTo/FAQPage; E-E-A-T | Часть Wordstat-цифр — из Serpstat (UA), не Яндекс РФ | Непроверенные % в кейсах агентства |
| 5 | [iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga](https://iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga-kak-pisat-stati-kotorye-privodyat-trafik/) | Чеклист 31 шаг / 4 фазы | Полный pipeline исследование → контент → on-page → «новое SEO» (AI Overviews) | Перегруз для новичка; bias западного чеклиста | Копировать все 31 пункт без адаптации под RU/GEO |
| 6 | [habr.com/ru/amp/publications/987506](https://habr.com/ru/amp/publications/987506/) | GEO/AEO технический гайд (2026) | SEO vs GEO vs AEO; answer-first; schema; robots для AI-ботов | Не учит писать SEO-текст с нуля; часть цифр без первичника | Zero-click % без первичника в основном тексте |
| 7 | [trigub.ru/geo-v-2026-godu](https://trigub.ru/geo-v-2026-godu/) | GEO для рунета (2026) | Алиса, Нейро, GigaChat; GEO как дополнение SEO | Отдельная тема, не how-to SEO-статьи | Sales-narrative агентства |

**Паттерн SERP:** топ — «полный гайд / пошаговый алгоритм 2026» с чек-листом, E-E-A-T и Wordstat. Отдельный кластер — GEO-лонгриды. Прямого совпадения с H1 «которые читают люди» мало — **content gap**: читабельность как SEO-фактор + единый workflow SEO+GEO.

**Intent:** how_to — пользователь хочет систему «семантика → структура → текст → техника → проверка». Вторичный: связать SEO-текст блога с GEO без второго проекта.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в текущем Cloud Agent окружении (MCP server does not exist). Вызов `wordstat_get_top_requests` для primary и secondary queries **не выполнен**. Точные объёмы спроса (показы/мес) **не получены** — не использовать выдуманные цифры в статье.

**Действие для пайплайна:** обновить токен/подключение MCP и переснять спрос перед следующим прогоном. OAuth: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Семантический кластер (экспертная оценка по SERP + карточка B01, без объёмов)

**Primary:** как писать seo статьи  

**Secondary (карточка):** seo текст для блога, geo оптимизация статьи  

**LSI для writer (из SERP, без частотности):**

- как написать seo статью / seo текст для сайта  
- seo копирайтинг / структура seo статьи  
- семантическое ядро / lsi ключевые слова / интент запроса  
- title description h1 h2  
- e-e-a-t / чеклист seo статьи  
- faq schema / blogposting  
- geo generative engine optimization / оптимизация под нейропоиск  
- сколько символов в seo статье (faq_hint из карточки)  
- что такое geo в seo (faq_hint)

**Кросс-ссылка (B04, Wordstat 11.06.2026):** «geo оптимизация» — 981 пок/мес; «geo оптимизация сайта» — 248. Для B01 использовать «geo оптимизация **статьи**» в GEO-блоке, не каннибализировать H1 B04.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение → основная часть по шагам → заключение со следующим шагом | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Первый экран: H1 + ответ на вопрос в **40–70 словах** | [ROI SEO — структура SEO-статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 22.04.2026 | да |
| Шаблон сильной статьи: объяснение, таблица, пример, ошибки, чек-лист, FAQ | [ROI SEO — структура SEO-статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 22.04.2026 | да |
| Article + BreadcrumbList + FAQPage; разметка = видимому контенту | [ROI SEO — структура SEO-статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 22.04.2026 | да |
| **3–5** внутренних ссылок на релевантные страницы | [ROI SEO — структура SEO-статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 22.04.2026 | да |
| Title **≤60** символов; Meta Description **140–160** | [Spilno — SEO-копирайтинг 2026](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да |
| План: **5–8 H2**, каждый — отдельный вопрос; TL;DR в начале + FAQ в конце | [Spilno — SEO-копирайтинг 2026](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да |
| Абзацы **2–4** предложения; списки и таблицы для читабельности | [Spilno — SEO-копирайтинг 2026](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да |
| SEO-статья 2026 = страница, закрывающая задачу пользователя, а не «текст под ключи» | [Olegweb — как написать SEO-статью](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Практический интент требует шагов, таблиц, чек-листов — не длинной теории | [Olegweb — как написать SEO-статью](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| GEO — эволюция SEO, не замена; классическая индексация остаётся базой | [Habr — GEO/AEO гайд](https://habr.com/ru/amp/publications/987506/) | 2026 | да |
| GEO-цель — попасть в источники, из которых LLM синтезирует ответ | [Habr — GEO/AEO гайд](https://habr.com/ru/amp/publications/987506/) | 2026 | да |
| Без индекса и топа в классической выдаче GEO-блоки бессмысленны | [Пустовалов — GEO для рунета](https://dipustovalov.ru/blog/geo-ai-poisk-runet-2026) | 2026 | да |
| Прямой ответ первым абзацем, FAQ и факты с источником повышают шанс цитирования в Нейро/Алисе | [Пустовалов — GEO для рунета](https://dipustovalov.ru/blog/geo-ai-poisk-runet-2026) | 2026 | да |

**Не использовать (нет первичника / непроверено):** «60–70% zero-click» (Habr без первичника); «+140% трафика» и подобные кейсы агентств; «373× рост AI-трафика» (Habr); точные % из Pikapuka/Digital Impuls без arxiv/первичника.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Отличие от конкурентов:**

- Яндекс — канон SEO без GEO-слоя.  
- GEO-гайды — не учат писать текст с нуля.  
- H1 «которые читают люди» слабо раскрыт в SERP → фокус на **читабельность как SEO-фактор** (структура, lead, «острова смысла»).

**Режим B:** сама статья B01 — эталон: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage.

**H2-каркас (из карточки B01):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как  
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead после H1 | 40–60 слов |
| Определение GEO | Блок «SEO + GEO» | 40–60 слов |
| Conversational H2 | FAQ-заголовки | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema | Вне body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | `/` |
| Alt обложки | Cover | «Редактор за ноутбуком…» (cover_scene_hint) |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — дополнение к SEO: цитирование в AI-ответах при базе индексируемого структурированного контента.  
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + тематические LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (~≤60 знаков), H1 — на странице; не дублировать.  
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting + FAQPage.  
6. **Что такое llms.txt и нужен ли он блогу?** — подсказка AI-краулерам; полезный сигнал, не замена sitemap.  
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать Wordstat-объёмы — MCP недоступен.  
- Цифры только из таблицы фактов §3.  
- Не копировать структуру Spilno/Olegweb 1:1.  
- Объём: 8 500–9 500 знаков (`quality-blog.md`).  
- Без эмодзи; CTA ≤ 3.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 5 конкурентов | ✅ |
| Wordstat (MCP) | ⚠️ недоступен — LSI из SERP |
| Таблица фактов с URL (≥15) | ✅ |
| utility_verdict PASS | ✅ |
| action_outline 5–9 шагов | ✅ (8) |
| reader_outcome | ✅ |
| GEO hooks + FAQ 5–7 | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
