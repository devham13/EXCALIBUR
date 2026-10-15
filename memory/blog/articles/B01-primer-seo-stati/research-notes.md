# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-10-07  
**disclaimer:** Все даты, версии и статистика проверены на 07.10.2026 (2026 год).

**utility_gate (topic):** PASS (`search_intent: how_to`, `article_mode: B`)

---

## 1. SERP-обзор (WebSearch Cursor + research-serp.json, 07.10.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: workflow, H1–H4, Вордстат/Вебмастер, естественные ключи, абзацы 3–5 строк, title/description, alt | Нет отдельного GEO-слоя; коммерческий хвост про Директ | CTA Директа; «универсальный объём» без нашего longread-ориентира для режима B |
| 2 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Практический how-to 2026 | 7 шагов от запросов до контроля после публикации; чек-лист; акцент «текст под запрос, не под ключи» | Мало GEO/schema; личный блог без эталона «meta-journal» | Копировать 7 H2 1:1 |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Правило «после каждого H2 — содержательный ответ»; LSI без насильственных вставок; E-E-A-T для YMYL | Перегруз про ИИ-генерацию; длинная воронка агентства | Блок «пишите только через ChatGPT» как единственный путь |
| 4 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread | Wordstat/Serpstat, E-E-A-T, schema Article+FAQ, title ~65 знаков | Непроверенные кейсы с %; 7-разделная структура «как у всех» | Проценты трафика без первичника |
| 5 | [seotika.ru/kak-pisat-seo-stati/](https://seotika.ru/kak-pisat-seo-stati/) | Агентский гайд 2026 | Поведенческие сигналы, GEO/AEO в lead; таблицы и чек-листы | Ориентир «1500–3000 слов» и «плотность 1–2%» — спорно для нашего бренда | Жёсткая «плотность ключей» как KPI |
| 6 | [articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-…](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | SEO+GEO workflow 2026 | FAQ, schema, чек-лист 18 пунктов; SEO+GEO в одном цикле | Продуктовый уклон AI-платформы | Продажу SaaS вместо чек-листа |
| 7 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Короткий принципиальный гайд | «Полный ответ на одной странице»; возврат в поиск = минус | Мало шагов, FAQ, schema | Формат «только принципы» без workflow |
| 8 | [habr.com/ru/articles/1030292/](https://habr.com/ru/articles/1030292/) | GEO/AEO полевое руководство | Chunking/RAG, извлекаемость абзацев; GEO как надстройка над SEO | Цифры «−20–40% органики» без единого первичника в тексте | Fear-narrative без actionable локального чек-листа |

**Паттерн SERP (окт. 2026):** доминируют «полный гайд 2026» (семантика → структура → текст → мета → публикация). Отдельный кластер — GEO-лонгриды. H1 «…которые читают люди» слабо представлен; в research-serp по H1 встречается [meta-journal.ru/2026/06/19/primer-seo-stati/](https://www.meta-journal.ru/2026/06/19/primer-seo-stati/) — наш канонический slug.

**Intent:** `how_to` — пошаговая система от интента до чек-листа публикации. Вторичный: связать **SEO-текст для блога** и **GEO-оптимизацию статьи** в одном материале без двух отдельных проектов.

**Пробел для Excalibur B01:** единый workflow «для людей + для роботов/LLM», режим B как **живой эталон** (8,5–9,5k знаков, FAQ, schema handoff), без agency-water и без фейковых кейсов.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 07.10.2026)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` / инструмент `wordstat_get_top_requests` **не подключён** в среде Cloud Agent на 07.10.2026. Вызов невозможен — **точные показы/мес не получены**, цифры спроса в текст статьи **не вставлять**.

При появлении MCP повторить запросы: `как писать seo статьи`, `seo текст для блога`, `geo оптимизация статьи`. При 401 — обновить токен: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### LSI для writer (SERP + secondary_queries, без выдуманных частот)

- как написать seo статью / seo статья пошагово  
- seo текст для сайта / seo текст для блога  
- seo копирайтинг, структура seo статьи  
- семантическое ядро, яндекс вордстат, LSI-фразы  
- title и description, meta description для статьи  
- h1 h2 структура, чек-лист seo текста  
- geo оптимизация статьи, generative engine optimization  
- faq для seo, schema.org faqpage, blogposting  
- ee-a-t / экспертность автора, переспам ключей  
- как писать тексты для людей и поисковиков  

**SEO-стратегия без Wordstat:** primary «как писать seo статьи» — H1, lead, title; secondary «seo текст для блога», «geo оптимизация статьи» — H2 и FAQ; conversational FAQ из паттернов SERP (объём, title vs h1, GEO vs SEO).

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата источника | Можно в текст |
|------|----------|----------------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции; критерий — полнота ответа | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не количество повторов ключей; переспам вреден | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на снипpet и кликабельность | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| К изображениям добавляют alt-текст; имена файлов — понятные (латиница) | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-тексты без ценности для пользователя (переоптимизация, скрытый текст, запросный спам) — нарушение для Яндекса | [Яндекс Вебмастер](https://yandex.ru/support/webmaster/ru/threat/seo-text) | актуально 2026 | да |
| Title в снипpet должен быть информативным, не шаблонным («Каталог» без уточнения) | [Яндекс Вебмастер — title](https://yandex.ru/support/webmaster/ru/search-results/title) | актуально 2026 | да |
| H1 ≠ Title: Title для снипpet, H1 — заголовок на странице | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Ориентир Title ~65 знаков с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| После каждого H2 в how-to — сразу содержательный ответ, не «разогрев» | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Главный ключ — H1, первый абзац, 1–2 H2, title/description; LSI — только если вписывается | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Первые 2–3 абзаца — прямой ответ; суть за ~15–20 секунд чтения | [LVSEO — SEO-копирайтинг](https://lvseo.ru/articles/seo-kopirayting) | 2026 | да |
| GEO (Generative Engine Optimization) формализован в препринте «GEO: Generative Engine Optimization» (KDD 2024) | [vc.ru — Writing for GEO](https://vc.ru/id4616024/3174294-kak-pisat-stati-dlya-generativnogo-poiska-i-seo) | 2026 | да |
| RAG-системы извлекают **фрагменты** текста; каждый абзац/H2 конкурирует отдельно | [Habr — GEO/AIO/AEO](https://habr.com/ru/articles/1030292/) | 2026 | да |
| Техническое SEO (crawlability, structured data) остаётся фундаментом; GEO — надстройка над SEO, не замена | [Habr — GEO/AIO/AEO](https://habr.com/ru/articles/1030292/) | 2026 | да |
| Главная задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**Не использовать без первичника:** «+140% трафика» (Pikapuka); «плотность ключей 1–2%» как нorma (Seotika); «−20–40% органики» (Habr) — только как осторожный контекст без точных %; Princeton GEO-bench цифры (+40% и т.д.) — упоминать исследование, не KPI без ссылки на arxiv/KDD.

**fact-bank.md:** прямых строк про SEO-writing нет; опираемся на таблицу выше. Факты про ИИ-заводы из fact-bank — **не смешивать** с B01, кроме общего принципа «51% маркетологов используют нейросети для аналитики, не для штамповки» (если writer добавит блок про ИИ — только из fact-bank с URL mayai.ru).

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает интент человека **и** упакован для извлечения фрагментов (GEO). Не «ещё один список ключей», а **единый workflow** с чек-листом перед публикацией.

**Почему отличается:** Яндекс даёт канон без GEO-слоя; GEO-гайды не учат писать с нуля; агентские материалы — вода и непроверенные кейсы. H1 «которые читают люди» = **читабельность как SEO/GEO-фактор** (3–5 строк, острова смысла, FAQ).

**Режим B:** статья B01 — **эталон** формата блога: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage (schema — отдельная роль), lead без «в этой статье».

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | Direct answer |
| Определение GEO 40–60 слов | Блок SEO+GEO | Direct answer |
| Первые 100–150 слов | Lead + первый H2 | Front-loading тезиса |
| Атомарные H2 | Каждый раздел | Первое предложение = вывод |
| FAQ 5–7 | Перед schema | Ответы-действия 2–4 предложения |
| Таблица SEO vs GEO (кратко) | Один H2 | 3–4 строки, не копировать audit4seo 1:1 |
| llms.txt | Упоминание | Что это, зачем блогу |
| E-E-A-T lite | Автор из registry | Без выдуманных регалий |
| Внутренняя ссылка | По карточке | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); для how-to longread Excalibur — 8 500–9 500 знаков при полноте ответа.  
2. **Что такое GEO в SEO?** — оптимизация под цитирование в генеративной выдаче; база — индексируемый структурированный контент.  
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + тематические слова.  
4. **Чем Title отличается от H1?** — Title для снипpet, H1 на странице; не дублировать дословно.  
5. **Какие schema для блога?** — BlogPosting + FAQPage (JSON-LD, не в body).  
6. **Что такое llms.txt?** — подсказка AI-краулерам; дополнение к sitemap, не замена.  
7. **Как проверить статью перед публикацией?** — чек-лист: интент, мета, H2-ответы, FAQ, ссылки, читабельность, GEO-чанки.

---

## 7. Utility (Gate 2)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт мини-семантику и outline, напишет черновик с читаемой структурой (H1–H3, lead, списки), настроит title/description, добавит FAQ и GEO-«острова», пройдёт чек-лист перед публикацией и получит материал, пригодный и для людей, и для поиска/нейровыдачи.

**action_outline (для writer):**

1. Зафиксировать primary query и интент; выписать 5–10 подвопросов из SERP (без копирования структуры одного конкурента).  
2. Собрать семантику: основной запрос + LSI из раздела 2; отметить secondary «seo текст для блога», «geo оптимизация статьи».  
3. Построить outline: один H1, 4–5 H2 как подзадачи, FAQ-блок; после каждого H2 — прямой ответ в первом абзаце.  
4. Написать lead (350–500 символов): определение SEO-статьи + обещание результата без «в этой статье».  
5. Наполнить тело: абзацы 3–5 строк, минимум один чек-лист или таблица; блок SEO+GEO с определением GEO.  
6. Подготовить title (~65 знаков) и description; H1 не дублировать title.  
7. Добавить 5–7 FAQ с ответами-действиями; перелинковка на `/`.  
8. Финальный чек-лист 15–18 пунктов (семантика, мета, структура, FAQ, alt, ссылки, island test).  
9. Handoff для schema: BlogPosting + FAQPage; даты 2026-10-07.

---

## 8. Риски и blockers для writer

- Не выдумывать показы Wordstat и KPI-трафика.  
- Не копировать Pikapuka/Seotika 1:1.  
- Объём: 8 500–9 500 знаков (`quality-blog.md`).  
- Без эмодзи; CTA ≤ 3.  
- Цифры Princeton/рынка AI — только с оговоркой «исследование» или без %.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента | ✅ |
| Wordstat (попытка MCP) | ⚠️ MCP недоступен |
| Таблица фактов с URL (≥10) | ✅ (18) |
| utility_verdict + action_outline | ✅ |
| GEO hooks + FAQ | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
