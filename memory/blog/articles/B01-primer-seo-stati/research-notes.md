# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + чеклист)  
**research_date:** 2026-08-07  
**disclaimer:** Все даты, версии и статистика проверены на 2026-08-07 (2026 год).

---

## 1. SERP-обзор (WebSearch Cursor, 07.08.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Практический гайд + ИИ | Пошаговый workflow: кластер → H1/H2 → смысл → семантика; правило «ответ сразу после H2»; примеры «плохо/хорошо» | Длинный sales-narrative; мало про GEO-чанки отдельным блоком | Копировать 10+ шагов 1:1; непроверенные кейсы роста |
| 2 | [pikapuka.com — инструкция 2026](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread | Семантика от интента; E-E-A-T; чек-лист; Schema Article + FAQPage; Title ~65 знаков | Кейсы «+140%» без первичника; перегруз agency-tone | Непроверенные проценты; 7-разделную структуру без дифференциации |
| 3 | [direct.yandex.ru — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный канон Яндекса (27.01.2026) | Авторитет; абзацы 3–5 строк; H1 один; естественность ключей; Wordstat; Title/Description | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа; «универсальные объёмы» без контекста SERP |
| 4 | [pawetta.com — SEO-копирайтинг 2026](https://pawetta.com/blog/seo-kopirayting/) | How-to + таблицы жанров | Интент → формат; объёмы по типам (1500–6000 слов); Title/H1 разные; чек-лист приёмки | Уклон в услуги агентства | Копировать прайс-CTA; «средний объём топ-10» без своей методики |
| 5 | [serpjet.ru — чек-лист SEO-статьи 2026](https://serpjet.ru/blog/chek-list-idealnoj-seo-stati-v-2026-ot-semantiki-do-cta-zamenit-seo-spetsialista-4847/) | Чек-лист B2B | Кластеризация по интенту; промпт-шаблон для ИИ; H1–H3 без переспама | Продаёт SaaS SerpJet; мало про читабельность «для людей» | Sales-first narrative; RAG-офферы вместо инструкции |
| 6 | [fireseo.ru — SEO-тексты 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyyj-tekst-v-2026-godu/) | GEO-aware гайд | Pillar/cluster; атомарные ответы; FAQ; маркеры личного опыта; очистка «следов ИИ» | Часть советов без первичных источников | Таблицы SEO vs GEO без arxiv-ссылок |
| 7 | [gracie.digital — контент для людей и ИИ](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | GEO + readability | H1 близок к нашей теме; answer-first 40–60 слов; island-блоки; таблица чек-листа | Цифра Brandlight «70%→20%» без первичника; agency CTA | Непроверенные % overlap Google/AI |
| 8 | [olegweb.ru — алгоритм от ключа до публикации](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 13 шагов + WordPress | Полный pipeline: спрос → интент → SERP → структура → WP → SEO Title | Перегруз шагами для новичка; мало GEO | 13 шагов как скелет 1:1 |

**Паттерн SERP (август 2026):** доминируют «полный гайд 2026» с чек-листом, E-E-A-T, Wordstat и блоком про ИИ/GEO. Прямого попадания в H1 «которые читают люди» мало — gracie.digital и bestseoserg.com близки по углу, но слабее по единому workflow SEO+GEO для блога.

**Intent:** `how_to` — пользователь хочет **пошаговую систему**: проверить спрос → интент/SERP → семантика → структура → текст → мета → FAQ/schema → GEO-чанки → финальный чеклист. Вторичный intent: связать **seo текст для блога** и **geo оптимизация статьи** в одном материале, не в двух проектах.

**Пробел для Excalibur:** большинство гайдов либо «SEO без GEO», либо «GEO без написания с нуля». Наш угол — **единый workflow «для людей»**: читабельность (структура, инфостиль, острова смысла) + техника (мета, schema, llms.txt) + **чеклист 15–20 пунктов перед публикацией**. Сама статья B01 — эталон формата (режим B).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` не подключён в Cloud Agent (MCP недоступен). Вызов `wordstat_get_top_requests` невозможен. **Точные объёмы спроса (показы/мес) не получены** — цифры в таблице ниже намеренно не указаны.

**Действие для следующего прогона:** подключите MCP в Cursor Secrets / `mcp.json` и авторизуйте Wordstat через:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Запросы для повторного сбора (primary + secondary)

| Фраза | Роль | Статус спроса |
|-------|------|---------------|
| как писать seo статьи | primary_query | ⚠️ объём не получен |
| seo текст для блога | secondary_1 | ⚠️ объём не получен |
| geo оптимизация статьи | secondary_2 | ⚠️ объём не получен |
| как написать seo статью | LSI (SERP) | ⚠️ объём не получен |
| seo копирайтинг 2026 | LSI (SERP) | ⚠️ объём не получен |
| чек-лист seo статьи | LSI (SERP) | ⚠️ объём не получен |
| структура seo статьи h1 h2 | LSI (SERP) | ⚠️ объём не получен |
| seo текст для сайта как написать | LSI (SERP) | ⚠️ объём не получен |
| geo оптимизация контента | LSI (GEO-кластер) | ⚠️ объём не получен |
| сколько символов seo статья | FAQ-intent | ⚠️ объём не получен |

### LSI для writer (экспертная семантика из SERP + WebSearch, без частотности)

**SEO-ядро:** как писать seo статьи, seo текст для блога, seo копирайтинг, как написать seo текст, структура seo статьи, семантическое ядро статьи, title description h1, lsi слова, переспам ключей, чек-лист seo статьи.

**GEO-слой:** geo оптимизация статьи, generative engine optimization, answer-first, атомарные блоки, faq schema, llms.txt, ai-краулеры robots.txt, цитирование нейросетями.

**Инструменты (упоминать как действие, не как рекламу):** Яндекс Вордстат, Яндекс Вебмастер, Rich Results Test, view-source для HTML-доступности.

**SEO-стратегия без Wordstat:** primary «как писать seo статьи» в H1/lead; secondary «seo текст для блога» — в блоке структуры longread; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье»; FAQ — «сколько символов», «что такое geo в seo».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир **3–5 строк**; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| **H1 — один** на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают **смысл и полезность**, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в **Яндекс Вордстат** | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Google не имеет «предпочтительного» word count — пишите столько, сколько нужно для полного ответа | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) — mix факторов качества; **trust** наиболее важен | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| SEO при people-first контенте — легитимная практика discovery, не «search engine-first» spam | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| Информационная статья — ориентир **1500–3000 слов**; гайд/лонгрид — **3000–6000 слов** (зависит от SERP) | [Pawetta — SEO-копирайтинг 2026](https://pawetta.com/blog/seo-kopirayting/) | 2026 | да |
| Title — до **~60 символов** с главным запросом; Description — **140–160 символов** | [Pawetta — SEO-копирайтинг 2026](https://pawetta.com/blog/seo-kopirayting/) | 2026 | да |
| Title и H1 должны быть **разными**, оба с главным запросом | [Pawetta — SEO-копирайтинг 2026](https://pawetta.com/blog/seo-kopirayting/) | 2026 | да |
| GEO-bench (Princeton): Cite Sources, Quotation Addition, Statistics Addition — **+30–40%** visibility (Position-Adjusted Word Count) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Keyword stuffing в GEO-контексте **хуже baseline (~−10%)** на Perplexity.ai | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Quotation Addition на Perplexity.ai — до **+37%** Subjective Impression vs baseline | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| AI-системы извлекают **фрагменты**, не страницу целиком — каждый H2/H3 = самодостаточный «остров» | [Gracie Digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| Прямой ответ на главный вопрос — в первых **40–60 словах** блока (answer-first) | [Gracie Digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| После каждого H2 — **содержательный ответ сразу**, без «разогрева» | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |

**fact-bank.md:** прямых фактов по SEO-writing нет — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); «overlap Google/AI 70%→20%» (Gracie/Brandlight без первичника); любые показы Wordstat — MCP недоступен.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый how-to longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один список ключей», а **единый workflow**: интент/SERP → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → **чеклист перед публикацией**.

**Почему отличается от конкурентов:**
- Яндекс Direct — канон SEO без GEO-слоя.
- GEO-гайды (fireseo, gracie) — не учат писать текст с нуля по семантике.
- Агентские longread (pikapuka, serpjet) — перегружены CTA и кейсами без источников.
- H1 «**которые читают люди**» слабо раскрыт в SERP — наш фокус: **читабельность как SEO-фактор** + атомарные блоки для AI.

**Tone:** практично, по-человечески; каждый H2 = подзадача + рекомендация «делать / не делать».

**H2-каркас (из карточки B01 + research):**
1. Зачем SEO и GEO в одной статье (не два проекта)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Answer-first | Каждый H2 | Первые 2–4 предложения = прямой ответ |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, action-oriented |
| Атомарные чанки | Каждый H2 | Island test: блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Опциональный сигнал для AI-краулеров |
| Внутренняя ссылка | Из карточки | На `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и топ SERP; для how-to longread Excalibur — 8 500–9 500 знаков текста.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + LSI; keyword stuffing хуже для GEO (arxiv).
4. **Чем Title отличается от H1?** — Title для сниппета (~60 символов), H1 — на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt и нужен ли он блогу?** — карта для AI-краулеров; полезный сигнал, не замена sitemap/robots.txt.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность, GEO-чанки.

---

## 7. Риски для writer

- Не выдумывать статистику Wordstat — MCP недоступен.
- Не копировать структуру Pikapuka/olegweb 1:1.
- Объём текста: **8 500–9 500** знаков (`quality-blog.md`).
- Без эмодзи в article.html.
- Min **5** нумерованных шагов в теле + чеклист **15–20** пунктов.
- site_url example.com — плейсхолдер `/` по карточке.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за одну сессию соберёт семантику по primary query, сверит интент с топ-5 SERP, построит структуру H1–H3 с answer-first блоками, напишет черновик без переспама, оформит Title/Description/FAQ, добавит JSON-LD и пройдёт чеклист 15–20 пунктов перед публикацией — с GEO-слойом (атомарные чанки, llms.txt) в том же материале.

**action_outline:**

1. **Проверить спрос и интент:** ввести «как писать seo статьи» в Wordstat и поиск; открыть топ-5 URL; зафиксировать формат (гайд/чек-лист), средний объём, повторяющиеся блоки (FAQ, таблицы).
2. **Собрать семантический кластер:** primary + 15–25 LSI из Wordstat и подсказок; сгруппировать в 3–5 смысловых групп → будущие H2.
3. **Составить скелет:** H1 (один) + H2/H3; после каждого H2 — тезис-ответ в первом абзаце; lead 40–60 слов с определением и обещанием результата.
4. **Написать черновик «для людей»:** абзацы 3–5 строк, списки, таблица «делать/не делать»; ключи естественно в H1, lead, 1–2 H2, Title/Description; без keyword stuffing.
5. **Добавить E-E-A-T lite:** маркеры опыта («в нашей практике», пример, скрин); автор/редакция; исходящие ссылки на канон (Яндекс Direct, Google Search Central) там, где даёте правила.
6. **Упаковать для GEO:** FAQ 5–7 вопросов с короткими ответами; атомарные H2-блоки; упоминание llms.txt и доступности AI-ботов в robots.txt (без блокировки без причины).
7. **Техника публикации:** Title ≤60 символов, Description 140–160; alt у изображений; 2–5 внутренних ссылок; slug латиницей.
8. **Schema (отдельно от body):** BlogPosting + FAQPage JSON-LD; datePublished/dateModified = дата прогона.
9. **Финальный чеклист:** пройти 15–20 пунктов (семантика, мета, island test, FAQ, schema, перелинковка, читабельность) — только после ✅ публиковать.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | ✅ PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (18 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `blog-topics.md` + `site-brief.md`.

**Blocker для Director (не writer):** при следующем прогоне подключить `user-mcp-kv` и пересобрать раздел Wordstat с точными показами.
