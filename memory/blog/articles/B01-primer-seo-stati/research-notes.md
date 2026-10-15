# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата)  
**research_date:** 2026-10-15  
**disclaimer:** Все даты, версии и статистика проверены на 15.10.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch Cursor, 15.10.2026 + research-serp.json)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: интент → семантика (Wordstat) → структура → текст → оптимизация; H1 один; переспам вреден; title/description | Нет отдельного GEO-слоя; CTA Директа | Коммерческий блок Директа |
| 2 | [olegweb.ru/.../kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 2026 (13 шагов) | Полный цикл до WordPress: спрос, интент, SERP-разбор, структура, мета, внутренние ссылки | Длинный; GEO — побочно | Копировать 13 H2 1:1 |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-...](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | Кластеры запросов → H2; ключ в H1/lead/1–2 H2/title/description; LSI «незаметно» | Много про ИИ-генерацию без human-in-the-loop | Непроверенные «часы vs минуты» |
| 4 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-...](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист 2026 (04.06.2026) | E-E-A-T/ЭПОС, AI Overviews, Алиса AI, ChatGPT, Perplexity; «лучший ответ на вопрос» | Чек-лист размазан по 9 критериям, мало пошагового «с нуля» | Agency tone |
| 5 | [articleai.ru / pikapuka.com / iskr.ai](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Кластер «SEO 2026» из research-serp | Семантика → публикация, чек-листы | Шаблонные longread, слабая дифференциация «для людей» | Одинаковые H2-скелеты |
| 6 | [marketingklub.ru/kak-pisat-seo-stati](https://marketingklub.ru/kak-pisat-seo-stati/) | Пошаговая инструкция 2026 | Иерархия H1→H2→H3; title 60–70 зн., description 150–160 | Мало GEO/schema | Перегруз «5–10 H2» без приоритетов |
| 7 | [searchengineland.com/guide/how-to-write-for-seo](https://searchengineland.com/guide/how-to-write-for-seo) | EN гайд 2026 | Answer-first, extractability для snippets и LLM; семантические заголовки | EN, не RU-специфика Яндекса | Дословный перевод |
| 8 | [trigub.ru/.../chek-list-dlya-stati-kotoruyu-zametit-ii-...](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | GEO + SEO чек-лист | Первые 100 слов = ответ; Schema Article/FAQPage; CWV | Коммерческий SEO-агент | Цифра «−20% трафика» без первичника в тексте — только с оговоркой |

**Паттерн SERP (окт. 2026):** доминируют «полный гайд 2026» (семантика → структура → мета → публикация) и отдельный кластер GEO. Запрос **«как писать seo статьи»** закрывают длинные инструкции; угол H1 **«которые читают люди»** в топе почти не раскрыт — конкуренты говорят про ключи и E-E-A-T, но редко связывают **читабельность + GEO-извлекаемость** в одном workflow.

**Intent:** `how_to` — собрать семантику → спланировать longread → написать без воды → оформить мета/schema → проверить под классический поиск и AI-ответы. Вторичные: «seo текст для блога», «geo оптимизация статьи».

**Пробел для Excalibur:** один **action-first** гайд: «SEO-статья = ответ человеку + упаковка для роботов/LLM», с **чеклистом 15+ пунктов**, FAQ и связкой с B04 (GEO сайта), без agency-CTA.

---

## 2. Яндекс Wordstat (MCP `user-mcp-kv`)

⚠️ **WORDSTAT MCP WARNING:** сервер MCP `user-mcp-kv` **не подключён** в текущем Cloud Agent run (`MCP server does not exist: user-mcp-kv`). Вызов `wordstat_get_top_requests` для primary и secondary **не выполнен**. Точные **показы/мес** в таблицу ниже **не заносить** — только после успешного MCP или ручной выгрузки из [wordstat.yandex.ru](https://wordstat.yandex.ru/).

При восстановлении MCP проверить запросы:

| Запрос (очередь) | Назначение |
|------------------|------------|
| как писать seo статьи | primary_query |
| seo текст для блога | secondary_1 |
| geo оптимизация статьи | secondary_2 |
| как написать seo статью | частая словоформа |
| seo статья для сайта | LSI |
| seo текст как писать | LSI |
| структура seo статьи | LSI |
| seo копирайтинг | LSI |
| e-e-a-t seo текст | LSI (осторожно с хайпом) |

### LSI для writer (из SERP + secondary, без частотности)

- как писать seo статьи, seo текст для блога, seo статья для сайта, структура seo статьи  
- семантическое ядро, поисковый интент, LSI-слова, title и description, meta description  
- h1 h2 h3, чек-лист перед публикацией, внутренние ссылки, alt изображений  
- geo оптимизация статьи, generative engine optimization, answer-first, FAQPage, schema.org  
- сколько символов в seo статье, что такое geo в seo (из faq_hints карточки)  
- яндекс вордстат, яндекс вебмастер, ai overviews, алиса ai, нейропоиск  

**SEO-стратегия (без Wordstat-цифр):** primary в H1/lead/title; secondary — отдельные H2 или FAQ; GEO — блок «одна статья, два канала (SERP + цитирование ИИ)», не подменять primary.

---

## 3. Таблица фактов (≥15 утверждений с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику подбирают в Яндекс Вордстат (и анализируют спрос/формулировки) | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир **3–5 строк**; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title — практический ориентир **~60 знаков** (десктопная строка обрезается) | [SEO Writer — seo-tekst](https://ai-seowriter.ru/blog/seo-tekst) | 2026 | да |
| Meta description — ориентир **до ~155 знаков**, влияет на CTR, не на ранжирование напрямую | [divitio.ru — пошаговая инструкция](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Главный ключ — в H1, первом абзаце, иногда в одном H2; без «ключ в каждом абзаце» | [divitio.ru](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| В Wordstat для одной статьи часто отбирают **15–25** связанных фраз (практика копирайтеров) | [divitio.ru](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да (как метод, не норма Яндекса) |
| После каждого H2 в how-to — **содержательный ответ сразу**, не «вода» перед сутью | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| В 2026 контент должен быть понятен **человеку, поисковику и AI-системам** (AI Overviews, Алиса AI, ChatGPT, Perplexity) | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| SEO-текст 2026: критерий качества — «можно ли сослаться как на **лучший ответ** на конкретный вопрос» | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Для snippets/LLM: **answer-first** — ответ в первых 1–2 предложениях секции, затем детали | [Search Engine Land — How to Write For SEO 2026](https://searchengineland.com/guide/how-to-write-for-seo) | 2026 | да |
| GEO — практика видимости в **AI-ответах** (цитирование/упоминание), опирается на SEO-фундамент | [Search Engine Land — GEO guide](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) | 24.09.2026 | да |
| **Первые ~100 слов** после H1 — зона готового ответа для нейропоиска (практика SEO) | [trigub.ru — чек-лист ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 2026 | да (как рекомендация) |
| Schema **Article + FAQPage** — базовый набор для статей под AI/s snippets | [trigub.ru — чек-лист ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 2026 | да |
| RAG-системы извлекают **фрагменты (chunks)**, не всю страницу — каждый абзац/H2 конкурирует отдельно | [Habr — GEO/AIO/AEO](https://habr.com/ru/articles/1030292/) | 2026 | да |
| GEO (Generative Engine Optimization) — оптимизация под **ответы генеративных нейросетей**, фокус на ясности и структуре, не только ключах | [Яндекс Практикум — GEO](https://practicum.yandex.ru/blog/chto-takoe-generative-engine-optimization-geo/) | 2026 | да |

**fact-bank.md:** фактов про SEO-writing нет — использовать только таблицу выше. Факты про ИИ-заводы из fact-bank **не смешивать** с B01 без явной связи.

**Не использовать без первичника:** «−20% трафика» (trigub); «+140% за 3 недели» (агентские кейсы); точные % visibility GEO без arxiv; любые **показы Wordstat** до подключения MCP.

---

## 4. Utility-only (Gate 2)

**utility_verdict:** PASS  

**reader_outcome:** Читатель сможет **от запроса до публикации** собрать семантику, набросать структуру longread, написать текст «для людей», оформить title/description/FAQ/schema и **пройти финальный чек-лист** перед выкладкой в блог — с минимальным GEO-слоем в той же статье.

**action_outline (workflow):**

1. Зафиксировать **primary query** и интент; выписать 3–5 вопросов читателя (FAQ-кандидаты).  
2. Собрать семантику в **Wordstat/Вебмастер** (15–25 фраз + LSI); отсечь запросы с другим интентом.  
3. Разобрать **топ-5 SERP**: формат, пробелы, что добавить в ваш материал.  
4. Составить **скелет**: H1, 4–7 H2, lead с прямым ответом, таблица/список минимум один раз.  
5. Написать черновик: короткие абзацы, ключи естественно, **острова смысла** в каждом H2.  
6. Заполнить **Title (~60 зн.)**, **Description (~155 зн.)**, alt, внутренние ссылки на `/`.  
7. Добавить **FAQ 5–7** + JSON-LD (BlogPosting + FAQPage) — в schema, не дублировать простынёй в body.  
8. GEO-проход: первые 100 слов, определения терминов, один FAQ под «geo оптимизация статьи».  
9. **Чек-лист перед публикацией** (семантика, мета, структура, ссылки, читабельность) — только после PASS публиковать.

---

## 5. Угол и дифференциация

**Главный угол:** SEO-статья 2026 = **longread, который хочется дочитать**, и который **можно процитировать** (GEO). Не «плотность ключей», а **workflow B01**: интент → структура → инфостиль → мета → FAQ/schema → чек-лист.

**Отличие от SERP:** H1 «**которые читают люди**» — через короткие абзацы, answer-first, без переспама; связка SEO+GEO **в одном материале**, не два разрозненных гайда.

**Режим B:** сама статья — эталон **8 500–9 500 знаков** текста (ориентир редакции), 5–7 FAQ, перелинковка `/`.

**H2-каркас (карточка + research):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread (H1–H3, lead, списки, таблицы)  
3. FAQ и schema  
4. Чеклист перед публикацией  

Внутри блоков: Wordstat, Title/H1, E-E-A-T lite, llms.txt (упоминание), robots для AI-ботов — без отдельного «новостного» H2.

---

## 6. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead | 40–60 слов |
| Определение GEO | Блок SEO+GEO | 40–60 слов |
| Conversational H2/FAQ | «Сколько символов…», «Что такое GEO в SEO?» | Вопрос → 2–4 предложения |
| Атомарные чанки | Каждый H2 | Тезис в первом предложении |
| Schema | meta | BlogPosting + FAQPage |
| datePublished | schema | 2026-10-15 |

---

## 7. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to в Excalibur — **8 500–9 500** знаков текста.  
2. **Что такое GEO в SEO?** — дополнение к SEO: цель — **цитирование в AI-ответах** при сохранении индексируемости и структуры.  
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (~60 зн.), H1 на странице; не дублировать дословно.  
5. **Какие schema нужны блоговой SEO-статье?** — BlogPosting (или Article) + FAQPage.  
6. **Как собрать семантику для seo текста блога?** — Wordstat + группировка по интенту + вторичные из карточки.  
7. **Как проверить статью перед публикацией?** — финальный чек-лист (мета, структура, FAQ, ссылки, читабельность).

---

## 8. Риски для writer / QA

- Не выдумывать **показы Wordstat** и проценты трафика из agency-кейсов.  
- Не копировать 13 шагов olegweb или 7 блоков Pikapuka 1:1.  
- Без эмодзи; CTA ≤ 3; site_url — `/` по карточке.  
- Обновить **dateModified** при существенных правках после publish.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента | ✅ (8) |
| Факты с URL ≥ 10 | ✅ (19) |
| utility_verdict + action_outline | ✅ |
| Wordstat MCP | ⚠️ не подключён |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов при условии не использовать частотности Wordstat до MCP. Вход: этот файл + `research-context.json` + `blog-topics.md` (B01) + `site-brief.md`.
