# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-06-19  
**disclaimer:** Все даты, версии и статистика проверены на 19.06.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch Cursor, 19.06.2026)

Запросы: «как писать seo статьи 2026», «seo текст для блога 2026», «geo оптимизация статьи 2026», официальные материалы Яндекса.

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: workflow тема → семантика → структура → текст → оптимизация; H1–H4; естественные ключи; Wordstat; «нет универсального объёма» | Нет GEO/нейропоиска; CTA Директа | Блок про Директ; копировать H-структуру без GEO-слоя |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Агентский longread (обновл. 15.06.2026) | Таблица «было/стало» 2026; LSI-кластеры; E-E-A-T; правило «после H2 — содержательный ответ»; Title/H1/Description | Перегруз agency-экспертизой; ИИ как центр, не workflow | Копировать 7+ разделов 1:1; непроверенные кейсы |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (2026) | Wordstat → Serpstat; чек-лист 10 шагов; Schema Article + FAQPage; Title ~65 знаков | Кейсы «+140% трафика» без первичника | Непроверенные проценты; agency CTA |
| 4 | [qvai.ru/media/kak-pisat-seo-stati](https://qvai.ru/media/kak-pisat-seo-stati) | Практик | Близкий intent «статьи, которые читают люди» | Меньше глубины по GEO/schema | Thin content без чек-листа |
| 5 | [itiriy.ru/blog/e-e-a-t-faktory-v-kontent-marketinge-kak-pisat-stati-kotorye-popadut-v-top-v-2026](https://itiriy.ru/blog/e-e-a-t-faktory-v-kontent-marketinge-kak-pisat-stati-kotorye-popadut-v-top-v-2026/) | E-E-A-T гайд (2026) | E-E-A-T → AI-поиск; «нуггеты ответов» 40–80 слов; FAQ + Schema; тематические кластеры | Мало пошагового «с нуля» | Продажа «удалённой редакции» как CTA |
| 6 | [rookee.ru/blog/kak-pisat-kontent-dlya-ii-vydachi-i-adaptirovat-stati-pod-ai-otvety](https://rookee.ru/blog/kak-pisat-kontent-dlya-ii-vydachi-i-adaptirovat-stati-pod-ai-otvety/) | GEO/AEO практик | Answer-first; H2/H3 как вопросы; island-структура; адаптация под AI-ответы | Фокус на переработке, не на первой SEO-статье | Дублировать sales-narrative |
| 7 | [epokha.ai/blog/kak-popast-v-otvety-neyrosetey-2026](https://epokha.ai/blog/kak-popast-v-otvety-neyrosetey-2026) | GEO гайд (2026) | llms.txt + Schema.org + answer-first как единый фундамент | Не учит писать текст с нуля | Копировать platform-specific блоки без контекста SEO |
| 8 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Короткий SEO-гайд | Принцип «полный ответ на одной странице»; LSI | Нет чек-листа, FAQ, GEO | «Просто следуй принципам» без шагов |

**Паттерн SERP (июнь 2026):** выдача забита «полным гайдом SEO-текстов 2026» (1ps, pikapuka, seomatik, hozyindachi) с E-E-A-T и ИИ. Отдельный кластер — GEO/AEO (rookee, epokha, audit4seo). Официальный Яндекс — база без нейропоиска. **Пробел:** мало материалов, где H1 «которые **читают люди**» = центральная ось (читабельность + поведение + GEO в одном workflow), а не побочный абзац про «полезность».

**Intent:** `how_to` — пошаговая система: интент → семантика → outline → черновик → meta/FAQ/schema → GEO-чанки → чеклист. Вторичный: связка «seo текст для блога» + «geo оптимизация статьи» в одном материале.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** В Cloud-сессии 2026-06-19 инструмент `wordstat_get_top_requests` сервера `user-mcp-kv` **недоступен** (нет MCP-конфигурации / OAuth-токена Яндекс в secrets). **Точные объёмы показов не получены** — не использовать выдуманные цифры спроса в статье. Обновите токен через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Primary_query для повторного вызова:** `как писать seo статьи`  
**Secondary (рекомендуется scout/research):** `seo текст для блога`, `geo оптимизация статьи`, `как написать seo статью`, `seo копирайтинг`, `структура seo статьи`

### LSI-ключи (экспертная семантика по SERP + карточка B01; без цифр Wordstat)

| Группа | LSI-фразы для writer |
|--------|----------------------|
| Интент / how-to | как написать seo статью, как писать seo тексты, seo текст для блога, seo текст для сайта, гайд по seo тексту |
| Семантика | семантическое ядро, яндекс вордстат, lsi фразы, кластер запросов, ключевые слова естественно |
| Структура | структура seo статьи, заголовки h1 h2, title и description, lead абзац, чеклист seo статьи |
| Качество | e-e-a-t, экспертность автора, читабельность текста, поведенческие факторы, answer-first |
| GEO | geo оптимизация статьи, generative engine optimization, llms.txt, schema.org faqpage, нейроответы яндекс |
| FAQ-intent | сколько символов в seo статье, что такое geo в seo, нужен ли переспам ключей, чем title отличается от h1 |

**SEO-стратегия (без цифр спроса):** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блоке структуры longread; «geo оптимизация статьи» — в блоке SEO+GEO; faq_hints из карточки — в FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат; инструмент показывает частотность и вариации запросов | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и description влияют на сниппет и кликабельность | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение → основная часть → заключение; в intro — польза для читателя | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Кластеризация: под каждую смысловую группу ключей — отдельная страница | [Яндекс — семантическое ядро](https://direct.yandex.ru/base/articles/semanticheskoe-yadro-sajta) | 2026 | да |
| Нет универсальной формулы плотности ключей; важнее полнота раскрытия темы и семантическое покрытие | [Яндекс — ключевые слова](https://yandex.ru/adv/edu/materials/direct-kak-podobrat-klyuchevye-frazy) | 2026 | да |
| В 2026 приоритет — полезность и экспертность, а не «уникальность/тошнота» | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| После каждого H2 — содержательный ответ, не «заголовок ради ключей» | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| H1 не должен дублировать Title; главный ключ — в H1, первом абзаце, title, description | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| Короткие абзацы — ориентир до 4 предложений | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| E-E-A-T расширен до Experience в декабре 2022; Trust — фундамент остальных сигналов | [itiriy.ru — E-E-A-T 2026](https://itiriy.ru/blog/e-e-a-t-faktory-v-kontent-marketinge-kak-pisat-stati-kotorye-popadut-v-top-v-2026/) | 2026 | да |
| Для AI-поиска: самодостаточные блоки **40–80 слов**, отвечающие на один вопрос | [itiriy.ru — E-E-A-T 2026](https://itiriy.ru/blog/e-e-a-t-faktory-v-kontent-marketinge-kak-pisat-stati-kotorye-popadut-v-top-v-2026/) | 2026 | да |
| Answer-first: прямой ответ в первом абзаце раздела; H2/H3 — как вопросы пользователя | [Rookee — контент для ИИ-выдачи](https://rookee.ru/blog/kak-pisat-kontent-dlya-ii-vydachi-i-adaptirovat-stati-pod-ai-otvety/) | 2026 | да |
| GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого контента | [Эпоха ИИ — GEO 2026](https://epokha.ai/blog/kak-popast-v-otvety-neyrosetey-2026) | 2026 | да |
| llms.txt — Markdown-файл в корне домена с картой ключевого контента для языковых моделей | [Эпоха ИИ — GEO 2026](https://epokha.ai/blog/kak-popast-v-otvety-neyrosetey-2026) | 2026 | да |
| Google (май 2026): llms.txt **не** является ranking factor для AI Overviews; ценность — agent-readiness | [Shadow — What Is llms.txt](https://www.shadow.inc/resources/what-is-llms-txt) | 2026 | да |
| Keyword stuffing в GEO-контексте работает хуже baseline (≈ −10% visibility) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Главная задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| SEO-текст 2026 — «цифровой продукт»: прямой ответ на первом экране (ориентир ≤150–200 знаков) | [Дзен — SEO-тексты 2026](https://dzen.ru/a/agQaAEwMsxSUd7wZ) | 2026 | да* |

\* Вторичный источник (Дзен); в тексте — с оговоркой «практики рынка», не как официальная норма Яндекса.

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «llms.txt +30–60% цитирования» (Habr без первичника в fact-bank); «микроразметка ×1,5–2» без arXiv/официального источника.

**fact-bank.md:** прямых фактов по SEO-писательству нет — опираемся на таблицу выше и официальный Яндекс.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **longread для людей**, который одновременно **готов к нейропоиску**. Не «ещё один список ключей», а **единый workflow**: интент → семантика (Wordstat) → outline с answer-first → черновик → meta/FAQ/schema → GEO-чанки → **чеклист 15+ пунктов**.

**Отличие от конкурентов:**
- Яндекс — канон без GEO; GEO-гайды не учат писать с нуля.
- Агентские гайды (1ps, pikapuka) перегружены E-E-A-T-кейсами и ИИ-hype.
- H1 «**которые читают люди**» слабо раскрыт в SERP: наш фокус — **читабельность как SEO-сигнал** (структура, короткие абзацы, island test) + техника для AI.

**Режим B:** статья B01 — **эталон формата**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (карточка + research):**
1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок SEO+GEO | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-intent | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; ≤4 предложения в абзаце |
| Island test | QA | Блок понятен без соседних |
| Schema | meta/handoff | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Опциональный сигнал, не замена sitemap |
| E-E-A-T lite | Автор | Имя, роль, без выдуманных регалий |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI; переспам вреден (Яндекс, arXiv GEO).
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt и нужен ли он блогу?** — карта контента для LLM; полезный сигнал, не ranking factor Google.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, meta, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику в Вордстат, построит outline longread с answer-first блоками, напишет SEO+GEO текст с FAQ и schema, пройдёт финальный чеклист и опубликует статью, которую дочитывают люди и которую могут процитировать нейропоиск.

**action_outline:**

1. **Определить интент:** открыть SERP по primary query; отметить формат топа (гайд/чек-лист/коммерция) и список подвопросов для H2.
2. **Собрать семантику:** primary + LSI в Яндекс Вордстат и Вебмастер; сгруппировать запросы в кластер одной статьи.
3. **Собрать outline:** H1 с главным ключом; H2 по кластерам; lead с прямым ответом ≤150–200 знаков; таблица или список там, где сравнение/шаги.
4. **Написать черновик:** после каждого H2 — содержательный абзац 40–80 слов; абзацы ≤4 предложений; без переспама.
5. **Добавить E-E-A-T lite:** автор, факты с URL, «делать / не делать» в каждом H2.
6. **Оформить meta и FAQ:** Title (~65 зн.), Description, 5–7 FAQ с короткими ответами-действиями.
7. **Встроить GEO:** атомарные чанки, conversational заголовки, упоминание llms.txt; JSON-LD BlogPosting + FAQPage (вне body).
8. **Прогнать чеклист 15+ пунктов:** семантика, структура, ссылки, schema, читабельность, island test.
9. **Опубликовать и перелинковать:** внутренняя ссылка на `/`; запланировать обновление dateModified при правках.

---

## 8. Риски для writer

- Не выдумывать статистику Wordstat и «кейсы роста» агентств.
- Не копировать структуру 1ps/Pikapuka 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи в article.html.
- Цифры только из раздела 3; fact-bank по SEO пуст — не тянуть цифры про Make/n8n.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен; LSI из SERP |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ (9 шагов) |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
