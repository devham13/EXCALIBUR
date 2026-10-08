# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-10-08  
**disclaimer:** Все даты, версии и статистика проверены на 2026-10-08 (2026 год).

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: семантика → структура → текст → оптимизация; H1–H4; естественность ключей; Wordstat; alt; мета; перелинковка | Нет GEO/нейропоиска; CTA Директа | Блок про Директ; копировать H-структуру без GEO-слоя |
| 2 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Пошаговый гайд 2026 (7 шагов) | Чёткий workflow: запросы → ТОП → структура → текст → Title/Description → релевантность → контроль | Мало GEO; без schema | Длинные личные истории вместо чеклиста |
| 3 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Алгоритм 13 шагов + WordPress | Интент, конкуренты, E-E-A-T, таблицы, финальный чеклист | Перегруз шагами для новичка; WP-специфика | 13 H2 «как есть» — сжать до workflow B01 |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread + ИИ | Правило «после каждого H2 — содержательный ответ»; семантика без спама | Много про ИИ-генерацию; длинный sales-тон | Копировать блок «только через ChatGPT» |
| 5 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский гайд (2026) | E-E-A-T, Wordstat/Serpstat, Article+FAQPage, Title ~65 знаков | Кейсы «+140%» без первичника | Непроверенные проценты; 7 разделов 1:1 |
| 6 | [private-seo.ru/blog/kak-pisat-seo-optimizirovannye-teksty-kotorye-nravyatsya-lyudyam](https://private-seo.ru/blog/kak-pisat-seo-optimizirovannye-teksty-kotorye-nravyatsya-lyudyam) | «Для людей» (09.2026) | Порядок: спрос → выдача → структура → ключи → title/H1 → чеклист | Узкий бренд | — |
| 7 | [roiseo.ru/blog/struktura-seo-stati-dlya-bloga](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон блоков блога | Первый экран: ответ 40–70 слов; таблица, ошибки, FAQ, schema | Мало про семантику/Wordstat | Копировать таблицу блоков без адаптации |
| 8 | [meta-journal.ru/2026/06/19/primer-seo-stati](https://www.meta-journal.ru/2026/06/19/primer-seo-stati/) | Близкий H1 «которые читают люди» | Совпадение с нашим angle | Конкурирует по заголовку; слабая дифференциация vs Excalibur | Не дублировать title 1:1 |

**Паттерн SERP (октябрь 2026):** доминируют «полный гайд 2026» (7–13 шагов), E-E-A-T, Wordstat, чек-листы. Отдельный кластер — GEO/AEO (Habr, vc.ru, tapbox). Прямого совмещения **SEO-writing + GEO-упаковка одной статьи** в одном материале мало: либо классический SEO (Яндекс, seoshkola), либо GEO без пошагового написания текста.

**Intent:** `how_to` — собрать семантику → структура → текст → мета → FAQ/schema → проверка. Вторичный: «seo текст для блога», «geo оптimизация статьи» (упаковка под нейроответы).

**Пробел для Excalibur:** единый **workflow SEO+GEO** с фокусом **«читают люди»** (инфостиль, атомарные H2, без переспама) + **чеклист перед публикацией**; сама статья B01 — эталон режима B (8,5–9,5k знаков).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** namespace `user-mcp-kv` недоступен в текущем Cloud Agent run (инструмент `wordstat_get_top_requests` не подключён). Точные **показы/мес** не получены. После подключения MCP повторить запросы для:

- `как писать seo статьи` (primary)
- `seo текст для блога`
- `geo оптимизация статьи`

Обновление токена (если 401): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (SERP + подсказки, **без цифр спроса**)

| Кластер | LSI / смежные формулировки |
|---------|----------------------------|
| Primary | как написать seo статью, seo текст для сайта, seo копирайтинг, структура seo статьи |
| Блог | seo текст для блога, статья для блога seo, longread seo |
| Техника | title description seo, h1 h2 seo, lsi слова, семантическое ядро статьи |
| Качество | e-e-a-t текст, seo без переспама, полезный контент |
| GEO | geo оптимизация статьи, generative engine optimization, faq schema, answer-first |

**SEO-стратегия для writer:** primary в H1/lead/Title; «seo текст для блога» — в H2 про структуру longread; «geo оптимизация статьи» — отдельный блок «SEO + GEO в одной статье»; faq_hints — в FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| К изображениям добавляют alt-текст; URL страницы — короткий и понятный | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Эффективность SEO-текста смотрят в Яндекс Метрике: запросы, время, возвраты | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title — ориентир ~55–60 символов; Description — ~150–160; ключ ближе к началу Title | [seoshkola.com — SEO-текст 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| Структура строится до текста: H1 с основным запросом, H2 — подвопросы, H3 — детали | [seoshkola.com — SEO-текст 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| Первый экран: H1 + краткий ответ на вопрос **40–70 слов** | [roiseo.ru — структура SEO-статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| После каждого H2 — сразу содержательный ответ, не «разогрев» | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Плотность информации важнее длины; прямой ответ в начале; FAQ и атомарные блоки для AI-выдач | [fireseo.ru — SEO 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| H1 должен отличаться от Title; Title ~65 знаков с триггером (чек-лист, инструкция) | [pikapuka.com — гайд E-E-A-T](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Schema.org: Article + FAQPage для сниппета и структуры | [pikapuka.com — гайд E-E-A-T](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [maryproject.ru — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| GEO-bench: **10 000** запросов; GEO-методы повышают visibility до **40%**; на Perplexity.ai — до **37%** | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | KDD 2024 | да |
| Цитаты, статистика и указание источников в тексте — сильные GEO-приёмы; keyword stuffing в GEO хуже baseline | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | KDD 2024 | да |
| GEO — оптимизация видимости в генеративных ответах; классическое SEO остаётся фундаментом (индекс, сниппет) | [habr.com/ru/articles/1030292](https://habr.com/ru/articles/1030292/) | 2026 | да |

**fact-bank.md:** нет строк, специфичных для SEO-копирайтинга — использовать таблицу выше; строки fact-bank про контент-завод/Make **не** вставлять в B01 без прямой связи с темой.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); «56% AI vs поиск» (blog.geouseo без первичника в fact-bank); «58–65% zero-click» (Habr 987506 — только как оценка индустрии).

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **longread для человека**, который **одновременно** готов к классической выдаче и к цитированию в нейроответах. Workflow: интент → семантика → каркас → текст → мета → FAQ/schema → GEO-чанки → **чеклист перед публикацией**.

**Почему отличается от конкурентов:**
- Яндекс — канон без GEO; GEO-гайды не учат писать с нуля.
- Агентские longread’ы — перегруз кейсами и CTA.
- H1 «которые читают люди» — редко раскрыт как **инфостиль + атомарные H2**, а не «ключи vs люди».

**Режим B:** статья B01 — **эталон формата**: 8 500–9 500 знаков, BlogPosting + FAQPage (schema отдельной ролью), 5–7 FAQ, перелинковка на `/`.

**H2-каркас (карточка B01 + research):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread  
3. FAQ и schema  
4. Чеклист перед публикацией  

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Answer-first 40–70 слов | Первый экран | Прямой ответ на primary query |
| Атомарные H2 | Каждый H2 | 1-е предложение = тезис; абзацы 3–5 строк |
| FAQ 5–7 | Конец | Ответы 2–4 предложения, ≤80 слов где возможно |
| Schema | Handoff schema-агенту | BlogPosting + FAQPage, не дублировать JSON-LD в body |
| faq_hints | FAQ | «сколько символов…», «что такое geo в seo» |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — дополнение: цель — цитирование в AI-ответах при сохранении индексируемого полезного текста.  
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (~55–65 знаков), H1 на странице; не дублировать дословно.  
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.  
6. **Что такое llms.txt?** — опциональный файл для AI-краулеров; не заменяет sitemap/robots.txt.  
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать Wordstat-цифры до подключения MCP.  
- Не копировать Pikapuka/olegweb 1:1.  
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).  
- Без эмодзи; CTA ≤ 3.  
- Внутренняя ссылка: `/` (карточка B01).

---

## 8. Utility gates (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за один цикл работы соберёт семантику по запросу, построит структуру longread с answer-first блоками, напишет и отредактирует SEO-текст без переспама, добавит FAQ и подготовит материал к schema, пройдёт чеклист перед публикацией и поймёт, какие GEO-приёмы (атомарные H2, цифры с источниками) усилят цитирование в нейроответах.

**action_outline:**

1. **Спрос и интент** — primary + 5–10 LSI в Wordstat/Вебмастере; открыть топ-10 SERP, выписать обязательные подтемы и пробелы.  
2. **Семантическая карта** — таблица: запрос / интент / будущий H2 или FAQ.  
3. **Каркас** — один H1, 4–6 H2 из карточки + подвопросы; lead с ответом **40–70 слов**.  
4. **Черновик текста** — абзацы 3–5 строк, списки/таблица; после каждого H2 — сразу суть; E-E-A-T lite (автор, дата, ссылки на источники).  
5. **On-page SEO** — Title (~55–65 зн.), Description (~150–160), alt у изображений, 2–4 осмысленные внутренние ссылки.  
6. **GEO-слой** — 5–7 FAQ; атомарные «острова» под H2; при необходимости упоминание llms.txt/доступности AI-ботов (без ухода в B04).  
7. **Чеклист перед публикацией** — 15–20 пунктов: семантика, мета, структура, FAQ, перелинковка, орфография, мобильная читаемость.  
8. **После публикации** — Метрика: запросы, время на странице, доработка через 4–6 недель по данным.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента | ✅ |
| Wordstat (MCP) | ⚠️ MCP недоступен; LSI из SERP |
| Таблица фактов ≥ 15 | ✅ (18 строк) |
| utility_verdict + action_outline | ✅ |
| GEO hooks + FAQ | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
