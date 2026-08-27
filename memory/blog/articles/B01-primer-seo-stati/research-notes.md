# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + демонстрация формата на самой статье)  
**research_date:** 2026-08-27  
**disclaimer:** Все даты, версии и статистика проверены на 27.08.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch Cursor, 27.08.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | 5 шагов workflow; Wordstat/Вебмастер; H1–H4; абзацы 3–5 строк; Title/Description; естественность ключей | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок про Директ |
| 2 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (май 2026) | Интент → Wordstat → структура → E-E-A-T; Title ~65 знаков; Schema Article+FAQPage; чек-лист | Кейсы без первичника; GEO как побочный эффект | Непроверенные «+140%»; копия 7-разделной структуры 1:1 |
| 3 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист 9 критериев (июнь 2026) | E-E-A-T + ЭПОС; answer-first; AI Overviews/Алиса; FAQ только под реальные вопросы | Мало пошагового workflow «с нуля» | Agency-tone «обновим ваши статьи» |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | H2 = подтема кластера; ответ сразу после H2; LSI без насилия; island test | Перегруз про ИИ-агентов | Шаблон «сначала смысл, потом ключи» без GEO-слоя |
| 5 | [fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | Практик (июнь 2026) | Плотность информации > длина; атомарные ответы; pillar+cluster; чек-лист перед публикацией; позиция Google/Яндекс про ИИ | Мало техники schema/FAQ | Sales-narrative agency |
| 6 | [www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | How-to (2026) | Правильный порядок: спрос → текст → оптимизация; структура до написания; аудит ТОПа | Без GEO-блока | Старт с «10 000 знаков и 15 ключей» |
| 7 | [totheweb.com/blog/beyond-seo-your-geo-checklist-mastering-content-creation-for-ai-search-engines/](https://totheweb.com/blog/beyond-seo-your-geo-checklist-mastering-content-creation-for-ai-search-engines/) | GEO-чек-лист EN (2026) | Answer-first 60–100 слов; citations +30–40% visibility; question H2; FAQ schema | EN, не RU workflow письма | Копировать EN-формулировки дословно |
| 8 | [mayai.ru/geo-optimizaciya-sajta-2026/](https://mayai.ru/geo-optimizaciya-sajta-2026/) | GEO DIY RU (2026) | Связка SEO+GEO; FAQ ≤80 слов; Princeton +30–40%; 74% топ-10 Google в ChatGPT | Фокус на сайт, не на статью | 32-пунктовый site-checklist как основа B01 |

**Паттерн SERP (август 2026):** топ — «полный гайд/чек-лист 2026» с E-E-A-T, Wordstat, answer-first. Отдельный кластер — GEO/AEO под нейровыдачу. H1 «которые читают люди» слабо занят; дифференциатор — **читабельность + единый workflow SEO→GEO** на одной странице.

**Intent:** `how_to` — пользователь хочет **пошаговую систему**: интент → семантика → структура → черновик → мета/schema → GEO-чанки → финальный чеклист. Вторичный: «seo текст для блога», «geo оптимизация статьи».

**Пробел Excalibur:** объединить канон Яндекса (семантика, структура) с **практикой GEO-упаковки** (BLUF, FAQ, schema) без agency-воды и без «новостей про алгоритмы».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в текущем Cloud Agent run (namespace not found). Вызов `wordstat_get_top_requests` не выполнен. Точные объёмы спроса **не получены** — цифры ниже **не использовать** в тексте статьи.

**Действие для ops:** подключить MCP `user-mcp-kv` в Cursor (Settings → Tools & MCP) или обновить OAuth-токен Wordstat:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (SERP + secondary sources, без Wordstat)

| Фраза (кандидат) | Источник оценки | Примечание |
|------------------|-----------------|------------|
| как писать seo статьи | primary_query карточки B01 | главный ключ |
| как написать seo статью | Pikapuka, SERP | синоним primary |
| seo текст для блога | secondary_query B01 | H2/LSI |
| seo копирайтинг | spilnoagency.com (Serpstat, вторичный) | ~390/мес — **не верифицировано Wordstat** |
| seo тексты | spilnoagency.com (Serpstat, вторичный) | ~390/мес — **не верифицировано Wordstat** |
| geo оптимизация статьи | secondary_query B01 | GEO-блок |
| e-e-a-t seo текст | SERP 2026 | LSI |
| чек-лист seo статьи | SERP intent | LSI для Title |
| структура seo статьи | Wordstat-кандидат | LSI |
| schema faq seo | SERP | LSI техника |

### LSI для writer (из SERP + конкурентов, без выдуманных частот)

- как писать seo статьи, seo текст для блога, seo копирайтинг, структура seo статьи  
- семантическое ядро, Wordstat, LSI, поисковый интент, Title, Description, H1–H3  
- E-E-A-T, ЭПОС, инфостиль, перелинковка, alt-текст, ЧПУ  
- GEO, answer-first, BLUF, FAQPage, BlogPosting, нейровыдача, Алиса AI, AI Overviews  
- чек-лист перед публикацией, Featured Snippet, атомарные чанки  

**SEO-стратегия (до появления Wordstat):** primary «как писать seo статьи» в H1/lead; secondary «seo текст для блога» — в блок структуры longread; «geo оптимизация статьи» — отдельный H2, не в Title целиком.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир **3–5 строк**; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в **Яндекс Вордстат** и **Яндекс Вебмастер** | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-текст 2026: workflow **5 шагов** — тема → семантика → структура → текст → оптимизация | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title — ориентир **~65 знаков**, с ключом и триггером (чек-лист, инструкция); H1 ≠ Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Schema.org: **Article + FAQPage** для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Google — E-E-A-T; Яндекс — **ЭПОС** (экспертность, полезность, оригинальность, содержательность) | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Базовый принцип 2026: **от главного ответа к деталям** — сначала суть, потом нюансы | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| FAQ нужен только когда закрывает **реальные** вопросы пользователя, не «ради SEO» | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| После каждого H2 — **содержательный ответ** сразу, без «разогрева» | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| **Плотность информации важнее длины**; ответ — как можно раньше в тексте | [FireSEO — SEO-текст 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| Google и Яндекс: **не важно**, кто написал (ИИ или человек), если контент полезен; массовая генерация без ценности = spam | [FireSEO — SEO-текст 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| Правильный порядок: **спрос и задача страницы → текст → оптимизация**, не «N знаков и M ключей» | [Hardkod — SEO-текст](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | 2026 | да |
| Princeton GEO-bench: citations/statistics дают **+30–40%** visibility в AI-ответах | [totheweb.com — GEO checklist 2026](https://totheweb.com/blog/beyond-seo-your-geo-checklist-mastering-content-creation-for-ai-search-engines/) | 2026 | да |
| Google AI Overviews на **64,7%** question-запросов vs **13,7%** всех запросов (55 393 запроса, arXiv 2026) | [totheweb.com — GEO checklist 2026](https://totheweb.com/blog/beyond-seo-your-geo-checklist-mastering-content-creation-for-ai-search-engines/) | 2026 | да |
| **~7 из 10** Google-поисков заканчиваются без клика (SparkToro, цит. totheweb) | [totheweb.com — GEO checklist 2026](https://totheweb.com/blog/beyond-seo-your-geo-checklist-mastering-content-creation-for-ai-search-engines/) | 2026 | да (как вторичная цитата) |
| BLUF: нейросети с **повышенным весом** сканируют первые **~200 слов** | [geo-course.ru — BLUF/GEO](https://geo-course.ru/blog/kak-pisat-kontent-dlya-nejrosetej/) | 2026 | да |
| Оптимальный GEO-чанк: абзац **150–190 слов**, самодостаточный без контекста | [geo-course.ru — BLUF/GEO](https://geo-course.ru/blog/kak-pisat-kontent-dlya-nejrosetej/) | 2026 | да |
| Первые **2–3 предложения** раздела — прямой ответ на вопрос H2 (AEO/GEO) | [site-rb.ru — SEO для нейросетей](https://www.site-rb.ru/blog/seo-dlya-neyrosetey-kak-popast-v-otvety-chatgpt-perplexity-yandeks-ai-i-google-ai-overview/) | 2026 | да |
| **74%** брендов из топ-10 Google присутствуют в ответах ChatGPT (Seer Interactive, цит. mayai.ru) | [mayai.ru — GEO 2026](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да (вторичная цитата) |
| FAQ-ответ для GEO — до **80 слов** на вопрос | [mayai.ru — GEO 2026](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да |
| Если пользователь **возвращается в поиск** после статьи — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**fact-bank.md:** прямых фактов по SEO-письму нет — использовать только таблицу выше.

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); Serpstat-цифры spilnoagency без Wordstat; «микроразметка ×1,5–2» без первичника; любые «показы/мес» без MCP Wordstat.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow A→B→C**: интент → семантика → структура → черновик → мета/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс Direct — канон без GEO-слоя.
- GEO-гайды (totheweb, mayai) — про сайт/цитирование, не про написание текста с нуля.
- Агентские гайды (Pikapuka, FireSEO) — перегружены кейсами и CTA.
- H1 «**которые читают люди**» — фокус на **читабельность как SEO+GEO-фактор** (инфостиль, «острова смысла», answer-first).

**Tone:** практично, по-человечески; без корпоративной воды; каждый H2 = подзадача + «делать / не делать».

**H2-каркас (из карточки B01 + research):**
1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ hints | «Сколько символов…», «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, ≤80 слов |
| Атомарные чанки | Каждый H2 | 1-е предложение = тезис; абзац 150–190 слов max |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` |
| Cover | cover_scene_hint | Редактор за ноутбуком, блокнот, тёплый свет |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — **8 500–9 500** знаков текста.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Можно ли писать SEO-статью только нейросетью?** — черновик да; публикация без фактчека, опыта и правок — риск spam/low quality (Google/Яндекс).
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность, GEO-чанки.

---

## 7. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель сможет **с нуля написать и подготовить к публикации SEO+GEO longread**: собрать семантику, спроектировать структуру под интент, написать читаемый черновик, оформить мета и schema, упаковать answer-first блоки и FAQ для нейровыдачи и пройти финальный чеклист перед публикацией.

**action_outline (how-to, 9 шагов):**

1. **Определить интент** primary_query и secondary_queries; классифицировать информационный vs коммерческий угол страницы.
2. **Собрать семантику** в Wordstat/Вебмастер: 15–25 фраз, LSI из SERP «Вместе ищут» / PAA; убрать запросы с другим intent.
3. **Аудит ТОП-5 SERP:** карта H2 конкурентов, must-have темы, content gap (что добавить уникального).
4. **Составить каркас до текста:** H1 (≠ Title), 4–6 H2 из карточки, H3 при необходимости, lead 40–60 слов, блок FAQ 5–7.
5. **Написать черновик для человека:** инфостиль, абзацы 3–5 строк, списки/таблицы; после каждого H2 — прямой ответ в первых 2–3 предложениях.
6. **Интегрировать ключи естественно:** primary в H1, первом абзаце, 1–2 H2; Title ~65 знаков, Description 140–160; alt без переспама.
7. **Добавить E-E-A-T lite:** автор, 1 кейс/цифра/ошибка из практики, исходящие ссылки на источники фактов.
8. **Упаковать GEO:** атомарные чанки 150–190 слов, FAQ ≤80 слов, перелинковка на `/`; handoff schema BlogPosting + FAQPage.
9. **Пройти чеклист публикации:** island test каждого H2, мета, schema, мобильность, дата обновления; не публиковать без фактчека.

---

## 8. Риски для writer

- **Wordstat:** не утверждать частотности до подключения MCP.
- Не копировать структуру Pikapuka (7 разделов) 1:1.
- Объём текста: **8 500–9 500** знаков (`quality-blog.md`).
- Минимум **5** нумерованных шагов в теле + чеклист **15–20** пунктов.
- Без эмодзи в `article.html`; site_url — `/` по карточке.
- Не писать `article.html` на шаге research.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| H2 outline | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
