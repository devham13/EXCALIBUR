# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to / longread + эталон формата)  
**research_date:** 2026-08-11  
**disclaimer:** Все даты, версии и статистика проверены на 11.08.2026.

---

## 1. SERP-обзор (WebSearch, 11.08.2026 — 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 | «Сначала смысл, потом оптимизация»; H2 = подтема + ответ сразу; LSI без насильственных вставок; блок про ИИ | Длинный; GEO как побочный эффект; мало printable-чеклиста | Копировать 10+ разделов 1:1 |
| 2 | [olegweb.ru — SEO-статья пошагово](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Практик WP (2026) | 13 нумерованных шагов от спроса до индексации; интент + конкуренты; чек-лист перед публикацией | Узкий фокус WordPress; GEO не выделен | Перегруз шагами без приоритетов |
| 3 | [direct.yandex.ru — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный Яндекс | Авторитет; workflow семантика→структура→текст; абзацы 3–5 строк; H1 один | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа |
| 4 | [serptop.ru — чек-лист SEO-текстов](https://serptop.ru/blog/kak-pisat-seo-teksty/) | Агентство + чек-лист | Формула H1; лид 50–100 слов с ключом; шаблон H2 (инструкция, ошибки, CTA) | Старый refresh; слабый GEO-слой | «Плотность ключей в %» как KPI |
| 5 | [roiseo.ru — структура SEO-статьи для блога](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон + чек-лист | Первый экран 40–70 слов; таблица «ошибка→проверка→решение»; FAQPage | Уклон в услуги ROI SEO | Agency CTA вместо DIY |
| 6 | [tolk.digital — формула SEO-текста 2026](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | Формула 2026 | Answer-first; блок автора; дата обновления; форматы FAQ/гайд/сравнение | Короткий; мало техники schema | Обобщения без чеклиста |
| 7 | [blog.click.ru — GEO vs SEO 2026](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | GEO+SEO RU | 17% довольствуются ответом ИИ без клика; двухэтапная стратегия SEO→GEO | Продаёт click.ru; мало «как написать с нуля» | Цифры NP Digital без первичника в тексте |
| 8 | [habr.com — GEO/AEO гайд](https://habr.com/ru/amp/publications/987506/) | Технический GEO | Answer-first; E-E-A-T; robots для AI-ботов; код-примеры | Не учит писать longread для людей | Тон «SEO мёртв» |

**Паттерн SERP (август 2026):** топ по «как писать seo статьи 2026» — длинные гайды (1ps, olegweb, seomatik, pikapuka) с акцентом на **интент → структура → E-E-A-T → FAQ**. Отдельный кластер — **GEO vs SEO**. Пробел: мало материалов, где **читабельность для людей** и **GEO-упаковка** описаны как **один workflow с printable-чеклистом**, а не два несвязанных гайда.

**Intent:** `how_to` — пользователь хочет **пошагово** собрать семантику, структуру, текст, мета, FAQ/schema и проверить перед публикацией. Вторичный: связать SEO-статью с **GEO** (ответ в нейровыдаче).

**Пробел для Excalibur:** практический гайд «SEO + GEO в одной статье» с фокусом **«которые читают люди»** (инфостиль, короткие абзацы, island-H2) + **15–20 пунктов чеклиста** + демонстрация формата на самой статье B01 (режим B).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 11.08.2026)

⚠️ **WORDSTAT MCP WARNING:** Сервер MCP `user-mcp-kv` недоступен в текущем Cloud Agent окружении (не подключён в runtime). Вызов `wordstat_get_top_requests` выполнить не удалось. **Точные объёмы показов не получены — цифры спроса ниже не указаны.** Обновите токен и подключение MCP через [авторизацию Yandex OAuth](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40) и перепроверьте research перед publish.

### Запросы для повторного замера (writer/QA)

| Запрос | Роль |
|--------|------|
| как писать seo статьи | primary_query |
| seo текст для блога | secondary_1 |
| geo оптимизация статьи | secondary_2 |
| как написать seo текст | LSI |
| seo статья для сайта | LSI |
| структура seo статьи | LSI |
| seo текст пример | LSI |
| сколько символов в seo статье | FAQ-intent |
| seo оптимизация текста | LSI |
| написание seo статей | LSI |

### LSI для writer (экспертная семантика без объёмов — до подключения Wordstat)

- **Интент и семантика:** интент запроса, семантическое ядро, LSI-слова, Wordstat, Яндекс Вебмастер, низко-/средне-/высокочастотные запросы  
- **Структура:** H1–H4, longread, lead-абзац, оглавление, FAQ-блок, таблица, чек-лист  
- **Оптимизация:** Title, meta description, alt изображений, перелинковка, canonical  
- **Качество:** E-E-A-T, уникальность, инфостиль, «острова смысла», поведенческие сигналы  
- **GEO-слой:** generative engine optimization, answer-first, FAQPage schema, AI-краулеры, нейропоиск, цитирование в ChatGPT/Алисе  
- **Техника:** Core Web Vitals, BlogPosting, JSON-LD, robots.txt  

**SEO-стратегия (без цифр):** primary «как писать seo статьи» — H1 + первый абзац; «seo текст для блога» — H2 про формат блога; «geo оптimizация статьи» — отдельный H2 «SEO + GEO в одной статье»; FAQ — «сколько символов в seo статье», «что такое geo в seo».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 2026 | да |
| Абзацы SEO-текста — ориентир **3–5 строк**; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 2026 | да |
| **H1 — один** на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 2026 | да |
| Семантику собирают в **Яндекс Вордстат** и **Яндекс Вебмастер** | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 2026 | да |
| Основной ключ — в **H1 и первый абзац**; варианты — в H2/H3 по смыслу | [SerpTop — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| Лид: основной ключ в первые **50–100 слов** | [SerpTop — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| Первый экран: H1 + краткий ответ **40–70 слов** | [ROI SEO — структура статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| После каждого H2 — **содержательный ответ сразу**, не «вода» перед сутью | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| **LCP ≤ 2,5 с**, **INP ≤ 200 мс**, **CLS ≤ 0,1** — порог «хорошо» (75-й перцентиль) | [web.dev — Core Web Vitals](https://web.dev/articles/vitals) | актуально | да |
| LCP «плохо» — **> 4 000 мс**; INP «плохо» — **> 500 мс**; CLS «плохо» — **> 0,25** | [web.dev — пороги CWV](https://web.dev/articles/defining-core-web-vitals-thresholds) | актуально | да |
| **17%** людей при поиске информации довольствуются ответом ИИ **без клика** по ссылкам (цит. click.ru) | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да (как вторичная оценка рынка) |
| Каждый четвёртый россиянин **ежедневно** пользуется нейросетями (цит. click.ru) | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да (как вторичная оценка) |
| GEO — оптимизация под генеративные системы; цель — **цитирование в ответе**, не только клик | [Habr — GEO/AEO](https://habr.com/ru/amp/publications/987506/) | 2026 | да |
| **60–70%** поисковых запросов в 2026 «заканчиваются без клика» (оценка в GEO-гайде Habr) | [Habr — GEO/AEO](https://habr.com/ru/amp/publications/987506/) | 2026 | да (с оговоркой «по оценке индустрии») |
| FAQ с разметкой **FAQPage** + таблицы/списки — формат, удобный для извлечения AI | [ROI SEO — структура](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) + [Habr GEO](https://habr.com/ru/amp/publications/987506/) | 2026 | да |
| Если пользователь **возвращается в поиск** — сигнал низкого качества ответа | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| H2 в тексте — ориентир **~1 на 1000 символов** без пробелов (агентская практика) | [Rush Agency — SEO-статьи](https://www.rush-agency.ru/blog/seo-prodvizhenie-stati-kak-pisat-seo-stati-pravilno/) | 2026 | да (как ориентир, не норма) |

**fact-bank.md:** прямых фактов про написание SEO-статей нет — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели»; «keyword stuffing +40% в GEO» без arxiv; NP Digital «0,35% GEO-трафика» без первичника.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Единый workflow: **интент → семантика → структура → черновик → GEO-чанки → мета/schema → чеклист перед публикацией**.

**Почему отличается от конкурентов:**
- Яндекс Direct — канон без GEO; GEO-гайды (Habr, click.ru) — без «как писать с нуля для людей».
- 1ps/olegweb — длинные энциклопедии; у нас **action-first** + **15–20 пунктов чеклиста**.
- H1 «**которые читают люди**» слабо раскрыт в SERP — наш дифференциатор: инфостиль, короткие абзацы, island-H2.

**Режим B:** сама статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, внутренняя перелинковка.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как (JSON-LD)  
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-заголовки | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, actionable |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в body | BlogPosting + FAQPage |
| Core Web Vitals | Чеклист / техблок | LCP/INP/CLS с web.dev |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптimizация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — **8 500–9 500** знаков текста.  
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при сохранении индексируемого структурированного контента.  
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 — на странице; не дублировать дословно.  
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.  
6. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, CWV.  
7. **Как писать, чтобы статью цитировали нейросети?** — answer-first, FAQ ≤80 слов, таблицы, E-E-A-T, дата обновления.

---

## 7. Черновик чеклиста для writer (15–20 пунктов)

1. Primary query и 3–5 secondary собраны (Wordstat / Вебмастер).  
2. Интент определён: how-to / checklist / comparison.  
3. SERP разобран: 3–5 URL конкурентов, пробелы зафиксированы.  
4. Outline: H1 + 4–6 H2 + FAQ; один H1 на страницу.  
5. Lead: ответ на главный вопрос в первых **40–70 слов**.  
6. Каждый H2 начинается с содержательного абзаца (не «в этой части мы…»).  
7. Абзацы **3–5 строк**; списки и таблица где уместно.  
8. Ключ в H1, первом абзаце, 1–2 H2, Title, Description — естественно.  
9. Title **~60–65** знаков; Description уникален; H1 ≠ Title.  
10. Alt у всех значимых изображений.  
11. FAQ **5–7** вопросов; ответы короткие и actionable.  
12. JSON-LD **BlogPosting + FAQPage** (schema-агент).  
13. Внутренние ссылки на hub/pillar (из карточки: `/`).  
14. Блок «ошибки» или «не делайте так» — минимум 3 пункта.  
15. E-E-A-T lite: автор, дата публикации/обновления.  
16. GEO: answer-first; при необходимости — robots не блокирует AI-ботов (ссылка на B04).  
17. Проверка: орфография, уникальность, нет воды (slop-blocklist).  
18. Core Web Vitals: LCP/INP/CLS в зелёной зоне (PageSpeed Insights).  
19. CTA ≤ 3, не подменяет пользу.  
20. Island test: каждый H2 полезен отдельно.

---

## 8. Риски для writer

- Не выдумывать объёмы Wordstat — ждать MCP или пометку QA.  
- Не копировать структуру olegweb (13 шагов) или 1ps 1:1.  
- Объём: **8 500–9 500** знаков (`quality-blog.md`).  
- Без эмодзи в article.html; без VPN/обходов.  
- Цифры только из таблицы фактов §3.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику по primary query, построит структуру longread с answer-first lead, напишет черновик с LSI без переспама, добавит FAQ и JSON-LD, пройдёт чеклист из 15–20 пунктов и опубликует SEO-статью, которую смогут читать люди и цитировать нейропоисковые системы.

**action_outline:**

1. **Проверить спрос и интент:** открыть Wordstat/Вебмастер по «как писать seo статьи»; зафиксировать primary + 5–10 LSI; определить тип intent (how-to).  
2. **Разобрать SERP:** выписать 3–5 конкурентов — структура H2, форматы (таблица, FAQ, чек-лист); отметить, чего не хватает для «читабельности».  
3. **Собрать outline:** H1 с primary; 4–6 H2 по логике пользователя; блок FAQ 5–7; место под таблицу «ошибка → что делать».  
4. **Написать lead и черновик:** первые 40–70 слов — прямой ответ; абзацы 3–5 строк; после каждого H2 — суть сразу; личный опыт/пример где возможно.  
5. **Встроить семантику:** ключ в H1, lead, 1–2 H2, Title, Description; LSI по тексту без переспама.  
6. **Добавить GEO-слой:** определение GEO в 40–60 слов; conversational подзаголовки; FAQ с короткими ответами для извлечения AI.  
7. **Оформить мета и медиа:** Title ~60–65 знаков, Description, alt; перелинковка; даты и автор.  
8. **Schema + финальный чеклист:** BlogPosting + FAQPage; пройти 15–20 пунктов §7; PageSpeed / Rich Results Test; публикация.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (18 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| Чеклист 15–20 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 конкурентов (1ps, olegweb, Яндекс Direct, SerpTop, ROI SEO, Tolk, click.ru GEO, Habr GEO). Wordstat MCP недоступен — LSI без цифр спроса, ⚠️ WARNING в notes. Угол — единый workflow SEO+GEO longread «для людей»: интент→структура→FAQ/schema→чеклист 15–20. 18 фактов с URL, 8 шагов action_outline, 7 FAQ. Готов к writer.
===
