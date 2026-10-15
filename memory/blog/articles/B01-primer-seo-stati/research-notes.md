# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to + чеклист)  
**research_date:** 2026-08-30  
**disclaimer:** Все даты, версии и статистика проверены на 30.08.2026.

---

## 1. SERP-обзор (WebSearch, август 2026 — 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Кластеры из Wordstat, H1→H2-каркас, LSI без переспама, примеры «плохо/хорошо» | Мало отдельного GEO-блока; длинный sales-хвост | Копировать 10+ разделов 1:1; непроверенные кейсы роста |
| 2 | [hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | Пошаговый how-to 2026 | Правильный порядок: интент → семантика → SERP → структура → текст → SEO-доработка | Нет GEO/FAQ/schema; без чеклиста публикации | Формулировку «10 000 знаков + 15 ключей» как стартовую точку |
| 3 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса | Канон: семантика, H1–H4, естественность ключей, Title/Description, Wordstat | Нет GEO/нейропоиска; CTA Директа | Блок про рекламу; «SEO = ключи в текст» |
| 4 | [marketingklub.ru/kak-pisat-seo-stati](https://marketingklub.ru/kak-pisat-seo-stati/) | Инструкция + чек-лист | Иерархия H1–H3, Title 150–160 символов, типичные ошибки | Слабый GEO-слой; часть цифр без первичника | Жёсткие «обязательные» объёмы без контекста |
| 5 | [roiseo.ru/blog/struktura-seo-stati-dlya-bloga](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон + чек-лист блога | Answer-first 40–70 слов, таблица «ошибка → проверка → решение», FAQPage | Узкий фокус на структуру, мало про семантику | Agency-CTA в конце |
| 6 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Гайд для новичков 2026 | «Структура до текста»: H1→H2→H3, анализ пробелов ТОПа | Нет schema/GEO; короткий финальный чеклист | Копировать каркас H2 без дифференциации |
| 7 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист оптимизации 2026 | 9 критериев: структура, alt, списки, «главный ответ → детали» | Мало про нейропоиск; agency-tone | Перегруз «9 критериев» без workflow |
| 8 | [pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | GEO + SEO 2026 | Snippet-First, чанки 3–7 строк, E-E-A-T для ИИ | Фокус на GEO, не учит писать с нуля; цифры «+80%» без первичника | Непроверенные проценты цитируемости |

**Паттерн SERP:** топ — «полный гайд 2026» с пошаговым workflow (интент → Wordstat → структура → текст → мета). Отдельный кластер — GEO-лонгриды (Habr, sergeisivkov.ru, impact-dl.ru). Прямого совпадения с H1 «которые читают люди» в топе мало: конкуренты говорят про «трафик» и «топ», а не про читабельность как SEO-фактор.

**Intent:** how_to — пользователь хочет **систему**: собрать семантику → построить структуру → написать текст для людей → добавить SEO-мета → упаковать под GEO (FAQ, schema) → проверить чеклистом. Вторичный intent: связка SEO + GEO в одном материале, объём статьи, schema.

**Пробел для Excalibur:** единый **практический workflow** «для людей и нейропоиска» с чеклистом 15+ пунктов; сама статья B01 — **эталон формата** (режим B); угол «читабельность = SEO» (острова смысла, answer-first), а не «вставь 15 ключей».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в окружении Cloud Agent (namespace отсутствует в каталоге MCP). Вызов `wordstat_get_top_requests` невозможен. **Точные объёмы спроса из API не получены** — цифры ниже не подставлять в текст как «показы/мес».

**Действие для оператора:** подключить MCP `user-mcp-kv` в environment.json и/или обновить OAuth-токен Wordstat: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Семантические кластеры (экспертная оценка по SERP + подсказкам, без API-цифр)

| Кластер | Примеры фраз (LSI для writer) | Назначение в статье |
|---------|-------------------------------|---------------------|
| Написание | как писать seo статьи, как написать seo текст, seo копирайтинг | H1, lead, primary |
| Формат блога | seo текст для блога, структура seo статьи, seo статья пример | H2 «структура longread» |
| Оптимизация | seo оптимизация статьи, title description seo, переспам ключей | H2 «мета и ключи» |
| GEO/ИИ | geo оптимизация статьи, текст для нейросетей, faq schema | H2 «SEO + GEO» |
| Проверка | чеклист seo статьи, сколько символов seo статья | FAQ + финальный чеклист |

**PAA / подсказки из SERP (для FAQ):** «Какого размера должна быть статья?», «Можно ли писать с помощью ИИ?», «Чем Title отличается от H1?», «Что такое GEO в SEO?», «Какие schema нужны блогу?»

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции; критерий — полнота ответа | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; перечисления — списками | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Длина контента сама по себе не влияет на ранжирование — нет «магического» целевого объёма | [Google Search Central — SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) | 2026 | да |
| E-E-A-T: доверие (Trust) — главный аспект; контент может быть полезен через опыт или экспертизу | [Google — Creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 2026 | да |
| SEO best practices остаются актуальны для generative AI в Google Search (AI Overviews, AI Mode) | [Google — AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | 2026 | да |
| Google Search **не использует** llms.txt и специальные «AI-файлы» для ранжирования | [Google — AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | 2026 | да |
| Нет требования дробить контент на «микрочанки» специально для ИИ — делайте страницы для аудитории | [Google — AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | 2026 | да |
| Generative AI в Google использует RAG и query fan-out (параллельные связанные запросы) | [Google — AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | 2026 | да |
| Оптимизация для AI Search = тот же people-first контент + уникальная экспертиза, не «хаки GEO» | [Think with Google — AI Search era](https://business.google.com/en-all/think/search-and-video/ai-search-era-brand-authority-strategy/) | 06.2026 | да |
| Принцип «главный ответ → детали»: сначала суть, потом нюансы и примеры | [Texterra — чек-лист SEO-текста 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 2026 | да |
| Шаблон SEO-статьи блога: lead 40–70 слов с ответом, таблица, пример, ошибки, чек-лист, FAQ | [ROI SEO — структура статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| Порядок работы: интент → семантика → анализ ТОПа → структура H2/H3 → черновик → SEO-доработка | [Hardkod — SEO-статья 2026](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | 2026 | да |
| Snippet-First: каждый H2 начинается с краткого ответа 1–3 предложения | [PW Agency — GEO 2026](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 2026 | да* |
| Citation-ready абзац: 60–100 слов, структура «ответ → пояснение → вывод» | [sergeisivkov.ru — GEO чек-лист](https://www.sergeisivkov.ru/blog/kontent-dlya-geo/) | 2026 | да* |

\* Агентский источник; в тексте — как практическая рекомендация, не как «официальная норма Google/Яндекса».

**Не использовать без первичника:** «+80% шансов в выдаче ИИ» (PW Agency); «+140% трафика за 3 недели»; «Serpstat 390 запросов/мес» (spilnoagency — не Wordstat API); «60% прироста от текста» (GenOptima через sergeisivkov — вторичный).

**Из fact-bank (можно, если уместно):** 51% маркетологов используют нейросети для аналитики, не для слепой штамповки ([mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/), 2026-06-11).

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-слой → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды перегружены E-E-A-T-кейсами и CTA.
- H1 «которые читают люди» слабо раскрыт в SERP; наш фокус: **читабельность как SEO-фактор** (острова смысла, answer-first) + техника.

**Режим B:** сама статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (не два проекта, один контент)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

**Tone (site-brief):** практично, B2B без воды; термины GEO/E-E-A-T — «на пальцах».

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-заголовки | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, actionable |
| Island test | QA | Каждый H2 = самодостаточный блок |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Google vs «GEO-хаки» | Блок GEO | llms.txt полезен, но Google Search его не использует для ранжирования |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс, Google); ориентир — полнота ответа и конкуренты; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — дополнение к SEO: цель — цитирование в AI-ответах при той же базе: индексируемый, структурированный, people-first контент.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 — на странице; не дублировать дословно.
5. **Какие schema нужны блогу?** — BlogPosting (или Article) + FAQPage для блока вопросов.
6. **Нужен ли llms.txt?** — опциональный сигнал для AI-краулеров; не замена sitemap; для Google Search не обязателен.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать показы Wordstat — MCP недоступен.
- Не копировать структуру 1ps.ru / Pikapuka 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Min 5 нумерованных шагов + чеклист 10+ пунктов (utility gate статьи).
- Без эмодзи; дефис вместо длинного тире; прямые кавычки.
- Цифры только из таблицы фактов выше и fact-bank.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель определит поисковый интент, соберёт семантику в Wordstat, построит структуру SEO-статьи (H1–H3 + lead), напишет черновик «для людей», добавит мета/FAQ/schema и GEO-слой (answer-first блоки) и пройдёт финальный чеклист перед публикацией.

**action_outline (для writer):**

1. **Определить интент:** открыть SERP по primary query «как писать seo статьи», зафиксировать тип страниц (how-to) и обязательные подтемы конкурентов.
2. **Собрать семантику:** primary + secondary из карточки B01; кластеры в Wordstat; сгруппировать 3–5 смысловых блоков под H2.
3. **Разобрать ТОП-5:** выписать повторяющиеся H2 и пробелы (читабельность, GEO, чеклист) — наш дифференциатор.
4. **Составить каркас до текста:** H1 (один), 4–6 H2 из карточки, H3 для деталей; lead 40–70 слов с прямым ответом.
5. **Написать черновик для людей:** короткие абзацы, списки, таблица «ошибка → что делать»; без переспама ключей.
6. **Добавить SEO-слой:** Title (~60 знаков), Description (140–160), ключи в H1/первом абзаце/1–2 H2 естественно; alt у изображений.
7. **Добавить GEO-слой:** Snippet-First в начале каждого H2; FAQ 5–7; упомянуть llms.txt без мифа «обязателен для Google».
8. **Подготовить schema:** BlogPosting + FAQPage (handoff schema-агенту); даты 2026-08-30.
9. **Пройти чеклист 15+ пунктов** (семантика, мета, структура, ссылки, island test, mobile) перед publish.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (17 фактов) |
| utility_verdict + action_outline | ✅ |
| GEO hooks + FAQ 5–7 | ✅ |
| Режим B описан | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅
summary: Utility gate PASS. SERP — 8 конкурентов (1ps, Hardkod, Яндекс Direct, MarketingKlub, ROI SEO, SEO Школа, Texterra, PW Agency). Wordstat MCP недоступен (user-mcp-kv не подключён) — LSI из SERP без API-цифр. Угол — единый workflow SEO+GEO longread «для людей»: answer-first, FAQ/schema, чеклист 15+. 17 фактов с URL, action_outline 9 шагов, utility_verdict PASS. Готов к writer.
===
