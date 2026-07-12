# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + чеклист; статья — эталон формата)  
**research_date:** 2026-07-12  
**disclaimer:** Все даты, версии и статистика проверены на 2026-07-12 (2026 год).

---

## 1. SERP-обзор (WebSearch Cursor, июль 2026)

Источник: нативный **WebSearch** по запросам `как писать seo статьи 2026`, `seo текст для блога 2026`, `geo оптимизация статьи 2026`, H1. DuckDuckGo `research-serp.json` использован как дополнение; приоритет — свежие результаты WebSearch.

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон SEO: семантика (Wordstat, Вебмастер), H1–H4, естественные ключи, Title/Description, пошаговый workflow | Нет GEO/нейропоиска; CTA Директа в конце | Коммерческий блок Директа; копировать структуру без GEO-слоя |
| 2 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread + чек-лист (2026) | E-E-A-T, семантика, Schema Article + FAQPage, Title ~65 знаков | Непроверенные кейсы с процентами; agency-tone | Цифры «+140% за N недель»; 7-разделную структуру 1:1 |
| 3 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Практик, 13 шагов (обнов. 05.02.2026) | Полный цикл: интент → конкуренты → структура → WP → индексация; акцент на задачу пользователя | Мало GEO; привязка к WordPress | Telegram-CTA как основной фокус |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | Кластеры 3–5 групп из Wordstat; ключ в H1, lead, 1–2 H2, meta | Длинный sales-narrative про ИИ | Пересказ без собственного workflow |
| 5 | [gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-…](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | AI SEO + люди (19.06.2026) | Answer-first 40–60 слов; факты каждые 150–200 слов; автономные H3-блоки | Мало пошагового «с нуля» для новичка | Копировать объёмные абстракции без чеклиста |
| 6 | [trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | Чек-лист под ИИ (17.04.2026) | Notion-шаблон, кластер 10–15 вопросов, Schema, LCP, FAQ | Уклон в услуги SEO; цифры «−20% трафика» — внутренняя аналитика автора | Коммерческий bias; непроверенные кейсы «+40%» |
| 7 | [seocrawl.ai/blog/ai-overview-ranking-factors](https://seocrawl.ai/blog/ai-overview-ranking-factors) | AI Overviews (22.05.2026) | RAG, E-E-A-T, topical clusters, первые 100 слов блока; Conductor/BrightEdge stats | EN-ориентир; мало про Яндекс | Копировать EN-статистику без оговорки источника |
| 8 | [dobromarketing.ru/kak-pisat-seo-teksty/](https://dobromarketing.ru/kak-pisat-seo-teksty/) | Гайд «для людей и роботов» | План, семантика, чек-лист | Без GEO-слоя 2026 | Thin CTA-обёртка |

**Паттерн SERP (июль 2026):** доминируют longread «SEO-тексты 2026» (1ps, pikapuka, seomatik, hozyindachi) + отдельный кластер GEO/AI (trigub, gracie, seocrawl). H1 «которые **читают люди**» слабо закрыт: конкуренты говорят про E-E-A-T и ИИ, но редко связывают **читабельность** (инфostиль, «острова смысла», lead без воды) с пошаговым workflow.

**Intent:** `how_to` — собрать семантику → структура → текст → meta/schema → GEO-упаковка → чеклист перед публикацией. Вторичный: «seo текст для блога», «geo оптимизация статьи».

**Пробел для Excalibur:** один **практический workflow** «SEO + GEO в одной статье» с фокусом на **читаемость как фактор ранжирования и цитирования**, без agency-water и без «SEO vs GEO encyclopedia».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

### ⚠️ WORDSTAT MCP WARNING

MCP-сервер **`user-mcp-kv`** недоступен в текущем Cloud Agent окружении (сервер не подключён; вызов `wordstat_get_top_requests` завершился ошибкой «MCP server does not exist»).

**Точные объёмы показов в месяц не получены.** Для writer:

1. Подключите MCP `user-mcp-kv` в Cursor и повторите research, **или**
2. Проверьте фразы вручную в [wordstat.yandex.ru](https://wordstat.yandex.ru/) (регион 225), **или**
3. Обновите OAuth-токен Wordstat: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Семантическая оценка (без цифр спроса — только LSI из SERP + карточка темы)

**Primary / secondary (из `research-context.json`):**

| Фраза | Статус спроса |
|-------|---------------|
| как писать seo статьи | primary — проверить в Wordstat |
| seo текст для блога | secondary — проверить в Wordstat |
| geo оптимизация статьи | secondary — проверить в Wordstat |

**LSI для writer (из топа SERP, подсказок и конкурентов — без выдуманных частот):**

- как написать seo статью, seo текст 2026, seo копирайтинг, seo статья для сайта  
- семантическое ядро, яндекс вордстат, сбор ключевых слов, LSI-фразы, интент запроса  
- структура статьи H1 H2 H3, title description, метатеги, перелинковка  
- e-e-a-t, экспертность автора, уникальность, читабельность, вода в тексте  
- geo оптимизация, нейропоиск, ai overviews, answer-first, faq schema, llms.txt  
- сколько символов в seo статье, что такое geo в seo (faq_hints карточки)

**SEO-стратегия:** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блок про блог/longread; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье», не подменять H1.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Google не задаёт «предпочтительный объём слов» — пишите для людей, не под счётчик | [Google — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| People-first: контент для аудитории, а не для манипуляции выдачей; E-E-A-T через опыт и экспертизу | [Google — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| SEO-статья должна решать задачу пользователя лучше страниц конкурентов, а не только содержать ключи | [olegweb.ru — SEO-статья](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Семантику из Wordstat группируют в 3–5 смысловых кластеров; ключ — в H1, первом абзаце, 1–2 H2, title, description | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Прямой ответ на главный вопрос — в первых 40–60 словах блока, без «разогрева» | [gracie.digital — контент для людей и ИИ](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| Конкретика (статистика, цифры) — ориентир каждые 150–200 слов со ссылками на источники | [gracie.digital — контент для людей и ИИ](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| Каждый H2/H3-блок должен быть самодостаточным «мини-ответом» для извлечения ИИ | [gracie.digital — контент для людей и ИИ](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| Первые 100 слов после H1 — зона прямого ответа для нейропоиска | [trigub.ru — чек-лист под ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 17.04.2026 | да |
| Обязательные элементы для ИИ: списки, таблицы, определения терминов, FAQ + Schema (FAQPage, HowTo, Article) | [trigub.ru — чек-лист под ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 17.04.2026 | да |
| AI Overviews: 25,11% запросов в Q1 2026 vs 13,14% в марте 2025 (Conductor, цит. SEOcrawl) | [seocrawl.ai — AI Overview factors](https://seocrawl.ai/blog/ai-overview-ranking-factors) | 22.05.2026 | да (как вторичная цитата) |
| Контент-кластеры с перелинковкой обходят «широкие» сайты до **~30%** (June 2025 Core Update, цит. SEOcrawl) | [seocrawl.ai — AI Overview factors](https://seocrawl.ai/blog/ai-overview-ranking-factors) | 22.05.2026 | да (как вторичная цитата) |
| Первые 100 слов раздела — highest-value зона для цитирования AI Overview | [seocrawl.ai — AI Overview factors](https://seocrawl.ai/blog/ai-overview-ranking-factors) | 22.05.2026 | да |
| **96%** цитат AI Overview — из верифицируемо авторитетных источников (цит. SEOcrawl) | [seocrawl.ai — AI Overview factors](https://seocrawl.ai/blog/ai-overview-ranking-factors) | 22.05.2026 | да (с оговоркой «по оценке SEOcrawl») |
| Google **не требует** llms.txt для AI Overviews; FAQPage + answer-first 40–80 слов — базовая GEO-гигиена | [mayai.ru — GEO SEO чек-лист](https://mayai.ru/geo-seo-optimizaciya-neyropoisk/) | 2026 | да |
| llms.txt в мае 2026 **не является** фактором GEO-ранжирования; AI-боты редко запрашивают `/llms.txt` (анализ 515M bot events, Limy) | [limy.ai — LLMs.txt guide](https://limy.ai/blog/llms.txt-in-2026-the-full-guide) | 2026 | да |
| Стандарт llms.txt предложен 3 сентября 2024 (Jeremy Howard, llmstxt.org) | [habr.com — llms.txt 2026](https://habr.com/ru/articles/1037442/) | 2026 | да |

**fact-bank.md:** нет строк по SEO-writing — все цифры только из таблицы выше.

**Не использовать без оговорки:** «−20% трафика без нейровыдачи» (trigub, внутренняя аналитика); «+140% за 3 недели» (Pikapuka); «llms.txt обязателен»; любые частоты Wordstat без MCP/ручной проверки.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает интент человека **и** упакован для нейропоиска. Не «ещё один список ключей», а **единый workflow**: интент → семантика (Wordstat) → структура → инфостиль → FAQ/schema → GEO-чанки → **чеклист 15+ пунктов** перед публикацией.

**Почему отличается от конкурентов:**

- Яндекс Direct — канон без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские longread перегружены кейсами и CTA.
- H1 «**которые читают люди**» — редкий акцент: **читабельность** (lead, абзацы, island-блоки) как часть SEO/GEO, не «отдельная теория».

**Tone:** практично, по-человечески; каждый H2 = подзадача + рекомендация «делать / не делать».

**H2-каркас (из карточки + research):**

1. Зачем SEO и GEO в одной статье (один контент — два канала видимости)
2. Структура longread: H1–H3, lead, списки, таблицы, «острова смысла»
3. FAQ и schema — зачем и как (BlogPosting + FAQPage, JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

**Режим B:** сама статья B01 — **эталон** формата: 8 500–9 500 знаков, 5–7 FAQ, атомарные H2, lead с определением.

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO — …» |
| Conversational H2 | FAQ-adjacent | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, action |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Optional, не замена sitemap |
| Internal link | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — дополнение к SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI (Яндекс Direct).
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (Article) + FAQPage.
6. **Нужен ли llms.txt блогу?** — optional; Google не требует для AI Overviews; приоритет — HTML, schema, robots.txt.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, meta, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать частоты Wordstat — MCP недоступен.
- Не копировать структуру Pikapuka 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Минимум **5** нумерованных шагов в теле **или** чеклист **10+** пунктов (контракт utility-only).
- Без эмодзи в article.html.
- Цифры только из раздела 3 или fact-bank.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику в Wordstat, построит структуру longread с lead и «островами смысла», напишет текст без переспама, добавит FAQ и schema, пройдёт чеклист перед публикацией и поймёт, какие GEO-правки (answer-first, llms.txt optional) внести в ту же статью без отдельного «GEO-проекта».

**action_outline:**

1. **Проверить спрос и интент:** вбить primary query в Wordstat и SERP; зафиксировать тип выдачи (гайды/how-to) и 10–15 смежных вопросов для кластера.
2. **Собрать семантику:** сгруппировать фразы в 3–5 кластеров; primary — в H1 и lead, secondary — в H2 и FAQ.
3. **Разобрать топ-5 конкурентов:** выписать пробелы (что не закрыто) — основа дифференциации «для людей».
4. **Собрать структуру:** H1 → lead (40–100 слов прямого ответа) → H2 по кластерам → FAQ; после каждого H2 — тезис в первых 2 предложениях.
5. **Написать черновик:** абзацы 3–5 строк, списки/таблица, ключи естественно; убрать воду (island test).
6. **Усилить E-E-A-T lite:** автор, примеры, исходящие ссылки на источники фактов; Title/Description/H1 не дублировать.
7. **GEO-упаковка:** answer-first блоки, 5–7 FAQ, JSON-LD BlogPosting + FAQPage (handoff schema-агенту); llms.txt — optional упоминание.
8. **Чеклист перед публикацией:** meta, перелинковка, alt, даты, Rich Results Test; финальная вычитка на читабельность.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен; LSI — семантика из SERP |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `blog-topics.md` + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 конкурентов (Яндекс Direct, Pikapuka, olegweb, 1ps, gracie.digital, trigub, seocrawl, dobromarketing). Wordstat MCP недоступен (user-mcp-kv); LSI из SERP. Угол — единый workflow SEO+GEO longread «для людей»: читабельность, атомарные чанки, FAQ/schema, чеклист 15+. 20 фактов с URL, 8 шагов action_outline, 7 FAQ. Готов к writer.
===
