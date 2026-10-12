# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-10-12  
**disclaimer:** Все даты, версии и статистика проверены на 12.10.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch + research-serp.json, октябрь 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: интент, семантика, H1–H4, естественность ключей, Wordstat; «нет универсального объёма» | Нет GEO/нейропоиска; CTA Директа | Продвижение рекламы; копировать H-структуру без GEO |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 2026 (13 шагов) | От спроса до WordPress: интент, конкуренты, мета, перелинковка | Узкий WP-фокус; мало про AI-цитирование | 13 шагов 1:1 |
| 3 | [seotika.ru/kak-pisat-seo-stati](https://seotika.ru/kak-pisat-seo-stati/) | Агентский гайд «в ТОП» 2026 | Lead за 100 слов; объём 1500–3000 слов; GEO/AEO-блок; метрики | Плотность 1–2% — эвристика агентства; sales в конце | Кейсы агентства как «универсальная норма» |
| 4 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 7 шагов для новичков | Чёткий workflow: запросы → SERP → структура → релевантность | Без schema/GEO чек-листа | Авторский tone «я пишу так» без дифференциации |
| 5 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread + ИИ 2026 | Семантика, E-E-A-T, ИИ как помощник | Перегруз «полный цикл ИИ»; размытый GEO | Структура «сначала смысл, потом ключи» — ок, но не клон |
| 6 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | E-E-A-T + schema (2026) | FAQPage, Title ~65 знаков, чек-лист | Непроверенные кейсы роста % | Копировать 7-разделный каркас |
| 7 | [habr.com/ru/articles/1030292](https://habr.com/ru/articles/1030292/) | GEO/AIO полевое руководство | RAG, chunking, GEO как надстройка над SEO; распределение усилий 40/35/25 | Не учит писать статью с нуля | Паника «−20–40% органики» без контекста ниши |
| 8 | [articleai.ru/.../kak-napisat-seo-statyu-v-2026](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | AI-first SEO 2026 | Быстрый цикл публикации | Thin differentiation vs human-first | Обещания «30–60 мин вместо 8 часов» как единственный путь |

**Паттерн SERP:** доминируют **пошаговые гайды 2026** (7–13 шагов) + отдельный кластер **GEO/AEO**. Запрос «как писать seo статьи» закрывают агентства и EdTech; **слабо раскрыт H1 «которые читают люди»** — читабельность как SEO/GEO-фактор (острова смысла, lead, отказ от переспама).

**Intent:** `how_to` — собрать семантику → структура → текст → мета → FAQ/schema → проверка. Вторичный: **seo текст для блога**, **geo оптимизация статьи** в одном материале.

**Пробел Excalibur:** единый **workflow SEO+GEO** для longread блога (режим B): не «ключи ради ключей», а **читаемость + извлекаемость для AI** + финальный чек-лист 15–20 пунктов.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` не подключён в Cloud Agent run (инструмент `wordstat_get_top_requests` недоступен). **Точные показы в месяц не получены** — не использовать выдуманные цифры спроса.

**Действие для пайплайна:** обновить OAuth-токен и MCP при необходимости: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### LSI и смежные формулировки (из SERP + secondary_queries, без Wordstat)

**Primary cluster:** как писать seo статьи, как написать seo статью, seo текст для блога, seo статья для сайта, seo копирайтинг, написание seo текстов.

**Семантика и структура:** семантическое ядро, сбор ключевых слов, интент запроса, структура seo статьи, заголовки h1 h2 h3, title и description, мета-теги, внутренняя перелинковка, lsi слова, релевантность текста.

**Качество и E-E-A-T:** полезный контент, уникальность текста, экспертность автора, факты и источники, чек-лист seo текста, проверка перед публикацией.

**GEO / нейропоиск:** geo оптимизация статьи, generative engine optimization, aeo, нейропоиск, faq для seo, schema.org faqpage, blogposting, answer-first, цитирование нейросетями, llms.txt.

**Инструменты (упоминать как действие):** яндекс вордстат, яндекс вебмастер, google search console, rich results test.

**FAQ hints (карточка B01):** сколько символов в seo статье; что такое geo в seo.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику анализируют через Яндекс Вордстат (частотность, формулировки) | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение → основная часть по шагам → заключение со следующим шагом | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и description влияют на сниппет и кликабельность | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Кластеризация семантики: группы запросов → отдельные страницы под смысл | [Яндекс Direct — семантическое ядро](https://direct.yandex.ru/base/articles/semanticheskoe-yadro-sajta) | 2026 | да |
| Не гнаться за максимумом вхождений — приоритет пользе пользователя | [Яндекс Direct — семантическое ядро](https://direct.yandex.ru/base/articles/semanticheskoe-yadro-sajta) | 2026 | да |
| Черновик сначала «для человека», затем SEO-доработка (структура, ключи в контексте) | [Яндекс Direct — SEO-копирайтинг](https://direct.yandex.ru/base/articles/chto-takoe-seo-kopirayting-i-kak-napisat-seo-tekst) | 2026 | да |
| SEO-статья в ТОП закрывает интент; lead — ответ в первых ~100 словах | [Seotika — как писать SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| Ориентир объёма информационной статьи у Seotika: **1500–3000 слов** (агентская эвристика, не норма Яндекса) | [Seotika — как писать SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да (с оговоркой «ориентир рынка») |
| Иерархия H1 → H2 → H3 без пропуска уровней | [Seotika — как писать SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| GEO (Generative Engine Optimization) formalized; GEO-bench — 10k queries; методы Cite Sources / Quotation / Statistics дают **+30–40%** visibility (Position-Adjusted Word Count) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Keyword stuffing в GEO-контексте **хуже baseline (~−10%)** | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| RAG-системы извлекают **фрагменты (chunks)**, не страницы целиком — каждый абзац конкурирует отдельно | [Habr — GEO/AIO 1030292](https://habr.com/ru/articles/1030292/) | 2026 | да |
| GEO — надстройка над SEO: ориентир распределения усилий **40%** техSEO, **35%** GEO-контент, **25%** авторитет/citations (авторская модель Habr) | [Habr — GEO/AIO 1030292](https://habr.com/ru/articles/1030292/) | 2026 | да (как модель, не официальная норма) |
| В SEO конкуренция за клики; в GEO — за **пересказ** формулировок, которые можно извлечь | [Habr — GEO часть 1](https://habr.com/ru/articles/1056746/) | 2026 | да |
| Google AI Overviews: **58–65%** запросов заканчиваются без клика (цит. в Habr tech-гайде) | [Habr — 987506](https://habr.com/ru/articles/987506/) | 2026 | да (вторичная цитата, оговорка) |

**fact-bank.md:** прямых строк про SEO-writing нет — использовать таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); фиксированная «норма 10 000 знаков»; плотность ключей 1–2% как обязательное правило Яндекса.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **longread для человека**, который одновременно **готов к нейропоиску**: один workflow от интента до чек-листа публикации. Акцент H1 — **«которые читают люди»**: короткие абзацы, lead с ответом, «острова смысла» под RAG, без переспама.

**Почему отличается:** Яндекс — канон без GEO; GEO-гайды — без письма с нуля; агентства — перегруз кейсами. Excalibur B01 — **эталон формата блога** (8,5–9,5k знаков, FAQ, schema handoff).

**H2-каркас (карточка B01):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread (H1–H3, lead, списки, таблицы)  
3. FAQ и schema  
4. Чек-лист перед публикацией  

**Tone (site-brief):** практично, по-человечески, без корпоративной воды.

---

## 5. GEO hooks (writer / schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок SEO+GEO | «GEO — …» |
| Answer-first | Каждый H2 | 1–2 предложения — прямой ответ |
| FAQ 5–7 | Конец | 2–4 предложения, действие |
| BlogPosting + FAQPage | schema role | JSON-LD, не в body |
| Internal link | Карточка | `/` или hub блога |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — оптимизация под цитирование в AI-ответах при сохранении классического SEO-фундамента.  
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + тематические слова.  
4. **Чем Title отличается от H1?** — Title для сниппета, H1 на странице; не дублировать дословно.  
5. **Какие schema для блога?** — BlogPosting + FAQPage.  
6. **Что такое llms.txt?** — опциональный сигнал для AI-краулеров, не замена robots/sitemap.  
7. **Как проверить статью перед публикацией?** — чек-лист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Цифры только из раздела 3 или fact-bank.  
- Не клонировать Pikapuka / olegweb 1:1.  
- Объём: 8 500–9 500 знаков (`quality-blog.md`).  
- Без эмодzi в article.html.  
- Wordstat-показы не утверждать до подключения MCP.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за один цикл подготовит SEO-longread для блога: соберёт семантику и структуру по SERP, напишет текст с lead и «островами смысла» под GEO, оформит Title/Description/FAQ, подготовит данные для BlogPosting+FAQPage и пройдёт финальный чек-лист перед публикацией.

**action_outline:**

1. **Интент и семантика:** зафиксировать primary/secondary запросы; собрать кластер в Вордстат и 3–5 URL из TOP SERP; выписать вопросы пользователя (PAA, заголовки конкурентов).  
2. **Каркас:** H1 = главный запрос + польза; H2 = подзадачи; под каждым H2 — тезис-ответ в первом абзаце; план FAQ 5–7.  
3. **Lead:** в 2–3 предложениях прямой ответ «как писать seo статьи» + результат для читателя (что получит после гайда).  
4. **Черновик тела:** писать для человека — абзацы 3–5 строк, списки, таблица «делать / не делать»; факты со ссылками; без переспама.  
5. **GEO-слой:** у каждого H2 — самодостаточный chunk; блок «SEO + GEO» с определениями; conversational подзаголовки из faq_hints.  
6. **On-page SEO:** Title (~60–65 знаков), Description, H1 ≠ Title; alt у изображений; 2–4 внутренние ссылки.  
7. **FAQ + schema handoff:** короткие ответы-действия; передать writer/schema роли JSON-LD BlogPosting + FAQPage (author из registry).  
8. **Чек-лист публикации:** релевантность, мета, иерархия заголовков, FAQ, schema, ссылки, дата обновления, island test по каждому H2.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (18) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
