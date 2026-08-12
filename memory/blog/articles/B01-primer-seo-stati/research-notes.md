# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-08-12  
**disclaimer:** Все даты, версии и статистика проверены на 12.08.2026 (2026 год).

---

## Utility gate

| Gate | Статус |
|------|--------|
| Topic utility (`excalibur_blog_utility_gate.py --topic-id B01`) | PASS |
| search_intent | how_to |
| article_mode | B |

**utility_verdict:** PASS

**reader_outcome:** После прочтения читатель сможет самостоятельно написать и опубликовать SEO-longread для блога: от проверки интента и структуры до FAQ/schema и GEO-упаковки, с финальным чеклистом перед публикацией.

**action_outline (workflow статьи):**

1. Проверить спрос и интент: Wordstat + топ-5 SERP по primary query, зафиксировать формат (гайд vs карточка).
2. Собрать семантику: primary + 5–10 LSI/вторичных запросов, сгруппировать по подтемам.
3. Разобрать конкурентов: что закрывают H2, где пробел (читабельность, GEO, чеклист).
4. Составить каркас: H1, 4–6 H2, lead 40–70 слов с прямым ответом, FAQ 5–7 пар.
5. Написать тело: каждый H2 = «остров смысла» (тезис в первом предложении), списки/таблицы, E-E-A-T lite.
6. Встроить SEO: Title (~60 знаков), Description (140–160), естественные ключи, 3–5 внутренних ссылок, alt.
7. Добавить GEO-слой: атомарные абзацы, цитаты/цифры с источниками, BlogPosting + FAQPage JSON-LD.
8. Пройти чеклист перед публикацией (семантика, мета, schema, ссылки, читабельность, robots для AI-краулеров).

---

## 1. SERP-обзор (WebSearch, август 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон SEO: интент, Wordstat, H1–H4, объём «по полноте ответа», абзацы 3–5 строк, Title/Description, перелинковка | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок про рекламу; копировать структуру без GEO |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu) | Пошаговый алгоритм 2026 (обнов. 05.02.2026) | 13 шагов от темы до индексации; интент, конкуренты, WordPress, чек-лист, личный опыт | Длинный affiliate-блок; GEO не выделен | Telegram/affiliate CTA; 13 H2 1:1 |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread агентства (обнов. 15.06.2026) | SEO vs SEO-статья, кластеры, ИИ без «вылета» из выдачи, FAQ | Продаёт услуги 1PS; перегруз историей алгоритмов | Agency tone; cookie-wall UX |
| 4 | [tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | Формула E-E-A-T 2026 | Интент > ключи; структура под доверие; чек-лист качества; форматы FAQ/гайд/сравнение | Мало техники (schema, GEO); короткий объём | CTA «бесплатный аудит» как главный вывод |
| 5 | [roiseo.ru/blog/struktura-seo-stati-dlya-bloga](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон + чек-лист для блога | Lead 40–70 слов, таблица блоков, FAQPage schema, ошибки + чек-лист | Узкий SEO-агентский угол; мало про GEO | Таблицу блоков можно адаптировать, не копировать |
| 6 | [habr.com/ru/publications/987506](https://habr.com/ru/publications/987506/) | GEO/AEO техгайд RU | GEO ≠ SEO; answer-first; robots.txt для AI-ботов; Schema FAQPage/HowTo | Фокус на разработчиков, не на «как писать текст» | Непроверенные «60–70% zero-click» без первичника в тексте |
| 7 | [searchengineland.com/what-is-generative-engine-optimization-geo-444418](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) | GEO framework EN | SEO как база GEO; entity clarity; self-contained paragraphs; метрики citations/SoV | EN, B2B global; мало RU-специфики (Алиса) | Копировать EN-термины без адаптации |

**Паттерн SERP (август 2026):** топ по «как писать seo статьи 2026» — длинные how-to с E-E-A-T, Wordstat, чек-листами (Яндекс Direct, olegweb, 1PS, Tolk). Отдельный кластер — GEO/AEO (Habr, Search Engine Land). Прямого совпадения с H1 «которые читают люди» мало: конкуренты продают «алгоритм» или «формулу», а не **читабельность + единый SEO+GEO workflow**.

**Intent:** how_to — пользователь хочет пошаговую систему: интент → семантика → структура → текст → техника → проверка. Вторичный intent: связать SEO-статью блога с GEO (цитирование в AI-ответах).

**Пробел для Excalibur:** один практический longread «для людей и для AI»: читабельность как SEO-фактор + атомарные H2 + FAQ/schema + чеклист 15+ пунктов без agency-воды.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 12.08.2026)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в текущем окружении Cloud Agent (`MCP server does not exist: user-mcp-kv`). Вызов `wordstat_get_top_requests` не выполнен. Точные объёмы спроса **не получены** из Wordstat API.

**Действие для оператора:** подключить MCP `user-mcp-kv` в environment и при необходимости обновить OAuth-токен:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса

| Фраза | Показы/мес |
|-------|------------|
| как писать seo статьи | *не получено — MCP недоступен* |
| seo текст для блога | *не получено — MCP недоступен* |
| geo оптимизация статьи | *не получено — MCP недоступен* |

### LSI для writer (экспертная семантика из SERP + карточка B01, без подстановки частот)

**Primary cluster:** как писать seo статьи, seo текст для блога, seo статья для сайта, написать seo текст, seo копирайтинг 2026

**Структура и техника:** структура seo статьи, заголовки h1 h2, title description, семантическое ядро, яндекс вордстат, lsi ключи, внутренние ссылки, alt текст, микроразметка faqpage

**Качество и интент:** поисковый интент, e-e-a-t, полезность контента, переспам ключей, чеклист перед публикацией, поведенческие факторы

**GEO/AIO cluster:** geo оптимизация статьи, generative engine optimization, answer-first, llms.txt, schema.org article, цитирование нейросетями, ai overviews

**FAQ-intent (из faq_hints карточки):** сколько символов в seo статье, что такое geo в seo

**SEO-стратегия для writer:** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блоке про формат блога; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье»; FAQ закрывает объём и определение GEO.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья 2026 — страница, закрывающая задачу пользователя, а не «текст под ключи» | [olegweb.ru — алгоритм SEO-статьи](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Сильный конкурент держится за счёт структуры, примеров, FAQ, перелинковки и поведенческой истории — не только текста | [olegweb.ru — алгоритм SEO-статьи](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| SEO-статья (блог) — информационный материал с целью ответить на вопросы и привлечь трафик; отличается от SEO-текста карточки/лендинга | [1PS.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| После каждого H2 — содержательный ответ; главный ключ в H1, первом абзаце, 1–2 H2, title и description | [1PS.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| Lead-абзац SEO-статьи для блога — 40–70 слов с прямым ответом на вопрос | [roiseo.ru — структура SEO-статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| Title — ориентир 60–70 символов с основным ключом; Description — 150–160 символов, влияет на CTR | [sostav.ru — SEO 2026](https://www.sostav.ru/blogs/287906/82274) | 2026 | да |
| GEO (Generative Engine Optimization) — оптимизация видимости контента в ответах генеративных поисковых систем; не замена SEO | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| GEO-bench (10 000 запросов): методы Cite Sources, Quotation Addition, Statistics Addition дают **+30–40%** по метрике Position-Adjusted Word Count | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Keyword stuffing в GEO-контексте работает **хуже** baseline | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| На Perplexity.ai зафиксировано улучшение visibility до **37%** (методы GEO) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| GEO строится на SEO-фундаменте; фокус смещается с кликов на цитирование в AI-ответах | [Search Engine Land — GEO guide](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) | 2026 | да |
| E-E-A-T: опыт, экспертиза, авторитетность, достоверность — отражать в структуре (автор, источники, дата обновления) | [tolk.digital — SEO-тексты 2026](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | 2026 | да |

**Не использовать в тексте (нет первичника / непроверено):** «60–70% zero-click» (Habr без первичной ссылки в research); «+140% трафика за 3 недели»; «HubSpot −80%» как универсальный прогноз; любые показы Wordstat без API.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс Direct — канон SEO без GEO-слоя.
- olegweb / 1PS — длинные алгоритмы с affiliate/agency CTA.
- GEO-гайды (Habr, SEL) не учат писать текст с нуля.
- H1 «которые читают люди» слабо раскрыт в SERP — наш фокус: **читабельность как SEO-фактор** (lead, абзацы, «острова смысла») + техника.

**Режим B:** сама статья B01 — эталон: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, перелинковка на `/`.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

**Tone:** практичный B2B без корпоративной воды (site-brief).

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2/H3 | FAQ-блок | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец longread | Ответ 2–4 предложения, action-first |
| Атомарные чанки | Каждый H2 | Тезис в первом предложении; абзацы 3–4 предложения |
| Schema handoff | meta, не body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Упоминание для AI-краулеров блога |
| E-E-A-T lite | Автор/редакция | Имя, роль, дата обновления |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и топ SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключевые слова в 2026 году?** — нет; естественные вхождения + LSI; переспам вреден (Яндекс Direct, arXiv GEO).
4. **Чем Title отличается от H1?** — Title для сниппета (~60–70 знаков), H1 — заголовок на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage для блока вопросов.
6. **Что такое llms.txt и нужен ли он блогу?** — файл-подсказка для AI-краулеров; дополнение к sitemap, не замена.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность, доступ AI-ботов.

---

## 7. Риски и blockers для writer

- Не выдумывать статистику Wordstat и рыночные проценты без URL.
- Не копировать структуру olegweb (13 шагов) или 1PS 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи; без VPN/обход блокировок.
- site_url — плейсхолдер `/` по карточке.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 5 конкурентов (WebSearch 2026) | ✅ |
| Wordstat (MCP) | ⚠️ сервер недоступен |
| Таблица фактов с URL (17 фактов) | ✅ |
| utility_verdict: PASS | ✅ |
| reader_outcome + action_outline | ✅ |
| GEO hooks + FAQ 5–7 | ✅ |
| Режим B описан | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
