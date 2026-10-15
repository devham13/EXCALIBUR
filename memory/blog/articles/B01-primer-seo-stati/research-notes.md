# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + эталон формата на самой статье)  
**research_date:** 2026-10-11  
**disclaimer:** Все даты, версии и статистика проверены на 11.10.2026 (2026 год).

**utility_gate (тема):** PASS (`search_intent: how_to`, `article_mode: B`) — повторная проверка `excalibur_blog_utility_gate.py --topic-id B01`.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: workflow, H1–H4, Wordstat/Вебмастер, естественность ключей, абзацы 3–5 строк, alt, мета | Нет GEO-слоя; CTA Директа | Блоки про Директ и «запустите кампанию» |
| 2 | [articleai.ru/.../kak-napisat-seo-statyu-v-2026...](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Агентский how-to 2026 | Семантика → публикация, AI-выдача | Перегруз ИИ-инструментами без «для людей» | Структура 1:1 |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu...](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Longread + чек-лист (2026) | E-E-A-T, Schema Article+FAQ, Title ~65 знаков | Кейсы с % без первичника | Непроверенные «+140% трафика» |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026...](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 с примерами | «Сначала смысл, потом ключи»; H2 = подтема кластера | Длинный блок про ИИ вместо читабельности | Копировать 7-разделный каркас |
| 5 | [private-seo.ru/blog/kak-pisat-seo-optimizirovannye-teksty...](https://private-seo.ru/blog/kak-pisat-seo-optimizirovannye-teksty-kotorye-nravyatsya-lyudyam) | Пошаговая инструкция (обнов. 28.09.2026) | Порядок: спрос → выдача → структура → слова; чек-лист перед публикацией | Мало GEO/schema | — |
| 6 | [hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | Гайд 2026 | Анти-паттерн «10 000 знаков + 15 ключей»; структура до текста | Без llms.txt / GEO-hooks | — |
| 7 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 13 шагов до WordPress | Интент, конкуренты, WP-оформление | Узкий фокус на WP, не на «читают люди» | — |
| 8 | [roiseo.ru/blog/razmetka-voprosov-otvetov-ii-poisk/](https://roiseo.ru/blog/razmetka-voprosov-otvetov-ii-poisk/) | FAQPage + GEO (30.07.2026) | Отмена FAQ rich results Google 07.05.2026; FAQPage для понимания/AI; answer-first | Не учит писать текст с нуля | Fear-mongering про schema |

**Паттерн SERP (окт. 2026):** доминируют «полный гайд 2026» (семантика → структура → оптимизация → чек-лист). Отдельный кластер — GEO + FAQ/schema. Заголовок «которые читают люди» встречается точечно ([meta-journal.ru](https://www.meta-journal.ru/2026/06/19/primer-seo-stati/) в research-serp), но без глубокого раскрытия читабельности как SEO-сигнала.

**Intent:** how_to — пользователь хочет **алгоритм**: интент → семантика → каркас H2 → черновик для человека → мета/ссылки → FAQ/schema → GEO-упаковка → чеклист. Вторичный: «seo текст для блога», «geo оптимизация статьи».

**Пробел для Excalibur B01:** единый workflow **SEO + GEO** с акцентом на **читабельность** (lead, «острова смысла», инфостиль) и **режим B** — сама статья как эталон longread 8 500–9 500 знаков.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 11.10.2026)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` (инструмент `wordstat_get_top_requests`) **не подключён** в текущем Cloud Agent run — namespace отсутствует в каталоге MCP. Вызов API не выполнен; **точные показы в месяц не получены**. Не использовать выдуманные цифры спроса до подключения MCP или ручной проверки в [wordstat.yandex.ru](https://wordstat.yandex.ru/).

**Запросы для повторного прогона Wordstat (директор / локальный Cursor с MCP):**

| Запрос | Назначение |
|--------|------------|
| как писать seo статьи | primary_query |
| seo текст для блога | secondary_1 |
| geo оптимизация статьи | secondary_2 |
| как написать seo статью | частый синоним в SERP |
| seo копирайтинг | смежный спрос |
| структура seo статьи | LSI / H2 |

### LSI для writer (из SERP + secondary, без частотности)

- как писать seo статьи / seo текст для блога / seo статья 2026  
- структура seo статьи, семантическое ядро, интент запроса  
- title description h1, внутренние ссылки, alt изображений  
- e-e-a-t, чек-лист перед публикацией  
- geo оптимизация статьи, faq schema, llms.txt, нейропоиск  

**SEO-стратегия:** primary в H1 и lead; secondary в H2 и FAQ; long-tail «сколько символов в seo статье», «что такое geo в seo» — из `faq_hints` карточки B01.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата источника | Можно в текст |
|------|----------|----------------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| К изображениям добавляют alt-текст; имена файлов — латиницей | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение → основная часть по шагам → заключение со следующим шагом | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title — ориентир ~60 знаков в десктопной выдаче (дальше обрезка) | [SEO Writer — seo-tekst](https://ai-seowriter.ru/blog/seo-tekst) | 2026 | да |
| H1 не должен дублировать Title слово в слово | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Title ~65 знаков с ключом и триггером (чек-лист, инструкция) — практический ориентир агентских гайдов | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Нормальный порядок: спрос и задача страницы → текст для человека → SEO-доводка (не «N ключей сначала») | [Hardkod — seo-tekst 2026](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | 2026 | да |
| После каждого H2 — содержательный ответ, не «заголовок ради ключа» | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| 7 мая 2026 Google прекратил показ FAQ rich results (аккордеон в выдаче) | [ROI SEO — FAQPage](https://roiseo.ru/blog/razmetka-voprosov-otvetov-ii-poisk/) | 30.07.2026 | да |
| Тип FAQPage на schema.org остаётся валидным; Google может использовать для понимания страницы без rich result | [Progress — SEO and GEO 2026](https://www.progress.com/blogs/seo-and-geo-guide) | 2026 | да |
| Для GEO FAQPage полезен: LLM часто не выполняют JS — JSON-LD дублирует пары вопрос–ответ | [Progress — SEO and GEO 2026](https://www.progress.com/blogs/seo-and-geo-guide) | 2026 | да |
| Специальной Schema «только для AI Overviews» нет; важны индексируемость, canonical, ответ в видимом HTML | [ROI SEO — FAQPage](https://roiseo.ru/blog/razmetka-voprosov-otvetov-ii-poisk/) | 30.07.2026 | да |
| Главная задача статьи — полный ответ; возврат в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| GEO (Generative Engine Optimization) дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого контента | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Нейросистемы извлекают пассажи — каждыy H2 = «остров смысла» | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Стандарт llms.txt — сентябрь 2024 (Jeremy Howard / Answer.AI) | [Digital Impuls — GEO](https://digitalimpuls.ru/blog/geo-optimization-2026/) | 2026 | да |

**Не использовать без первичника:** «+140% трафика за 3 недели» (Pikapuka); «микроразметка ×1,5–2 цитирование» без исследования; «25% запросов через AI» без источника.

**fact-bank.md:** нет строк по SEO-writing — опираться на таблицу выше.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает интент человека **и** упакован для нейропоиска (FAQ, schema, атомарные H2). Не «ещё один список ключей», а **workflow A→Z** с финальным чеклистом 15+ пунктов.

**Почему отличается от конкурентов:**

- Яндекс — канон без GEO-слоя; GEO-гайды не учат писать с нуля.
- Агентские longread’ы перегружены E-E-A-T-кейсами и CTA.
- H1 «которые читают люди» — слабо раскрыт в SERP; наш фокус: **читабельность = SEO** (lead, абзацы, инфостиль, island test) + техника.

**Режим B:** статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage (schema — отдельная роль), перелинковка на `/`.

**H2-каркас (карточка B01 + research):**

1. Зачем SEO и GEO в одной статье (один контент — два канала)  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как (JSON-LD вне body)  
4. Чеклист перед публикацией (15–20 пунктов)

**Tone:** практично, по-человечески; без корпоративной воды и эмодзи.

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-темы | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец longread | Answer-first, 2–4 предложения |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Зачем блогу |
| Alt обложки | Cover | `cover_scene_hint` из карточки |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); ориентир — полнота ответа и SERP; для how-to Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — дополнение к SEO для цитирования в AI-ответах.  
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 на странице; не дублировать.  
5. **Какие schema для SEO-статьи блога?** — BlogPosting + FAQPage; тексты FAQ = видимый HTML.  
6. **Нужен ли llms.txt?** — полезный сигнал для AI-краулеров, не замена sitemap.  
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать Wordstat-показы и статистику трафика.  
- Не копировать Pikapuka / 1ps 1:1.  
- Объём: 8 500–9 500 знаков (`quality-blog.md`).  
- Min **5** нумерованных шагов + чеклист **10+** (utility gate статьи).  
- Без эмодзи; internal link на `/` по карточке.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику по primary/secondary запросам, построит структуру longread под интент, напишет черновик «для людей», добавит Title/Description/alt/перелинковку, оформит FAQ и подготовит handoff под schema, пройдёт чеклист GEO (answer-first, атомарные H2, llms.txt) и опубликует материал, пригодный и для поиска, и для нейровыдачи.

**action_outline (для writer):**

1. **Зафиксировать интент** по primary «как писать seo статьи»: how_to, результат — опубликованная инструкция, не обзор «что такое SEO».  
2. **Собрать семантику:** primary + secondary из карточки; LSI из раздела 2; проверить топ-5 URL из SERP на пробелы (читабельность, GEO).  
3. **Составить каркас H2** по карточке B01; под каждым H2 — один подвопрос и тезис в первом предложении.  
4. **Написать lead:** прямой ответ + польза за 15–20 секунд чтения; определение SEO-статьи 40–60 слов.  
5. **Черновик для человека:** абзацы 3–5 строк, списки/таблица, без переспама; затем вставить ключи в H1, lead, 1–2 H2, Title/Description.  
6. **Добавить блок SEO+GEO:** GEO-определение, «острова смысла», упоминание llms.txt и FAQ (07.05.2026 — без обещания FAQ-сниппета Google).  
7. **FAQ 5–7:** answer-first; формулировки согласовать со schema-ролью (дословное совпадение JSON-LD и HTML).  
8. **Чеклист 15+ пунктов** перед публикацией: мета, alt, ссылки, island test, даты, перелинковка `/`.  
9. **Self-check режима B:** статья сама демонстрирует все приёмы, которые описывает.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (см. раздел 2) |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `blog-topics.md` + `site-brief.md`.
