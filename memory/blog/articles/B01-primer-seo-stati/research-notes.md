# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to + чеклист)  
**research_date:** 2026-08-14  
**disclaimer:** Все даты, версии и статистика проверены на 14.08.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch Cursor, август 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread + ИИ | Пошаговый workflow: интент → Wordstat → кластеры → структура → черновик → оптимизация; lead 30–50 слов; таблица GEO-чеклиста | Перегруз про ИИ; коммерческие блоки агентства | Копировать 10+ разделов 1:1; непроверенные «до/после» без источника |
| 2 | [pikapuka.com — инструкция 2026](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | How-to + чек-лист | Глубокая семантика (Wordstat, Serpstat, LSI); E-E-A-T; Title ~65 знаков; H1 ≠ Title; Schema Article + FAQPage | Agency-tone; кейсы без первичника | 7-разделную структуру без дифференциации |
| 3 | [hozyindachi.ru — новые правила 2026](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | Практик SEO | Таблица типов запросов; техчеклист (Title 50–60, Description 140–155, 3–5 перелинковок); плотность ключа ≤2%; AI Overview/Алиса | Коммерческие CTA на услуги; «Баден-Баден 2,5%» без первичника Яндекса | Продажу SEO-аудита как главный CTA |
| 4 | [serpjet.ru — чек-лист SEO-статьи 2026](https://serpjet.ru/blog/chek-list-idealnoj-seo-stati-v-2026-ot-semantiki-do-cta-zamenit-seo-spetsialista-4847/) | Чек-лист B2B | Кластеры по интенту; H2 с пользой и цифрами; блоки «утверждение + доказательство + пример» под нейровыдачу | Уклон в автоматизацию SerpJet; «экономия 70%» — заявление без аудита | Sales-narrative агентства |
| 5 | [direct.yandex.ru — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса | Канон: workflow, H1–H4, абзацы 3–5 строк, естественность ключей, Wordstat, мета, alt | Нет GEO-слоя; промо Директа | Блок про рекламу; дублировать канон без практики |
| 6 | [maryproject.ru — статьи под SEO](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Агентский принцип | «Полный ответ на одной странице»; LSI и «хвосты»; сигнал «не возвращаться в поиск» | Мало actionable шагов, нет чек-листа/FAQ/schema | Формулировки «просто следуй принципам» |
| 7 | [qvai.ru — SEO-статьи для людей](https://qvai.ru/media/kak-pisat-seo-stati) | Методика практика | Баланс алгоритмов и живого читателя; нейроответы | Узкий бренд; мало техники | — |
| 8 | [mv-blog.ru — GEO чек-лист статьи](https://mv-blog.ru/blog/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | GEO + CMS | Lead 40–60 слов; FAQ 5–7 × до 80 слов; BlogPosting + FAQPage; Rich Results Test | Фокус на Битрикс, не на написание с нуля | CMS-специфику как универсальный стандарт |

**Паттерн SERP (август 2026):** топ — «полный гайд / чек-лист 2026» с E-E-A-T, Wordstat, структурой H1–H3 и блоком про нейровыдачу. Отдельный кластер — GEO-чеклисты. H1 «которые читают люди» встречается, но редко раскрывается через **читабельность как SEO-фактор** (инфостиль, lead, «острова смысла»).

**Intent:** `how_to` — пользователь хочет **пошаговую систему**: интент → семантика → структура → текст → техника → проверка. Вторичный intent: встроить **GEO** в тот же материал, не плодя вторую статью.

**Пробел для Excalibur:** единый workflow **SEO + GEO longread «для людей»**: от сбора семантики до чеклиста перед публикацией; сама статья B01 — эталон формата (режим B).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в среде Cloud Agent (сервер не подключён). Вызов `wordstat_get_top_requests` выполнить не удалось. **Точные объёмы спроса не получены.** Обновите токен и подключение через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (без цифр спроса — только LSI из SERP + конкурентов)

**Primary cluster:** как писать seo статьи, как написать seo статью, seo текст для блога, seo копирайтинг 2026, написание seo текстов.

**Инструменты и этапы:** семантическое ядро, кластеризация запросов, яндекс вордстат, поисковый интент, lsi фразы, структура h1 h2 h3, title description, перелинковка, микроразметка schema.org.

**Качество и алгоритмы:** e-e-a-t, инфостиль, переспам ключевых слов, поведенческие факторы, featured snippet, нейровыдача.

**GEO-слой (secondary):** geo оптimizaciya стati, generative engine optimization, faq для ai, answer-first, blogposting faqpage json-ld, llms.txt, цитирование нейросетями.

**FAQ-intent (из PAA/SERP):** сколько символов в seo статье; что такое geo в seo; можно ли писать seo текст с помощью ии; сколько ключевых слов использовать; чем seo текст отличается от обычного.

**SEO-стратегия для writer:** primary «как писать seo статьи» — H1/lead; «seo текст для блога» — H2 про формат; «geo оптимизация статьи» — отдельный H2 + FAQ; long-tail про чек-лист и структуру — в оглавление и FAQ.

*После восстановления Wordstat:* повторить запросы `как писать seo статьи`, `seo текст для блога`, `geo оптимизация статьи` (регион 225) и дополнить таблицу «Фраза | Показы/мес».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — он зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность; переспам ключей вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 должен отличаться от Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Title — ориентир ~65 знаков, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Schema.org: Article + FAQPage для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Первые 30–50 слов статьи должны давать прямой ответ на главный запрос | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Title 50–60 символов; Description 140–155 символов — рабочие ориентиры | [hozyindachi.ru — SEO-тексты 2026](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | 2026 | да |
| Внутренняя перелинковка: 3–5 ссылок на смежные материалы | [hozyindachi.ru — SEO-тексты 2026](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | 2026 | да |
| Информационные статьи по конкурентным запросам — ориентир 1500–3000 слов; лонгриды — 3000–5000+ (зависит от SERP) | [hozyindachi.ru — SEO-тексты 2026](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | 2026 | да (как ориентир, не норма) |
| Плотность основного ключа — не выше ~2%; переспам выше ~2,5% — риск фильтра «Баден-Баден» (отраслевое правило) | [hozyindachi.ru — SEO-тексты 2026](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | 2026 | да (с оговоркой «по практике SEO») |
| Главная задача статьи — полный ответ; возврат пользователя в поиск — негативный сигнал | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 14.08.2026 | да |
| LSI-термин «устарел» в индустрии; корректнее — покрытие интента, словарь темы, сущности | [seo-vladimir.ru — LSI 2026](https://seo-vladimir.ru/blog/lsi-copywriting-seo-2026/) | 2026 | да |
| Ключевое слово — не более 3–4 раз на 1000 знаков (ориентир без переспама) | [seo-vladimir.ru — LSI 2026](https://seo-vladimir.ru/blog/lsi-copywriting-seo-2026/) | 2026 | да (как практика, не официальная норма) |
| GEO lead: прямой ответ в первых 40–60 словах; FAQ 5–7 пар, ответы до ~80 слов | [mv-blog.ru — GEO чек-лист](https://mv-blog.ru/blog/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | 2026 | да |
| Для блога: JSON-LD BlogPosting + FAQPage; Question/Answer должны совпадать с видимым текстом | [mv-blog.ru — GEO чек-лист](https://mv-blog.ru/blog/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | 2026 | да |
| Универсальная GEO-база (robots.txt, schema, FAQ, таблицы) даёт ~70% эффекта для всех AI-моделей сразу | [geoscout.pro — GEO чек-лист 2026](https://geoscout.pro/ru/blog/geo-optimizaciya-pod-chatgpt-claude-perplexity-cheklist) | 2026 | да (как отраслевая оценка) |
| Princeton GEO-bench: добавление цитат и статистики даёт +30–40% visibility | [mayai.ru — GEO чек-лист 2026](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да (ссылка на arxiv через вторичный источник) |
| ~74% брендов из топ-10 Google присутствуют в ответах ChatGPT (Seer Interactive, цит. mayai) | [mayai.ru — GEO чек-лист 2026](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да (вторичная цитата) |
| Яндекс — ~69,3% российского поискового рынка (годовой отчёт 2025) | [seotop.biz — семантическое ядро](https://seotop.biz/blog/semanticheskoe-yadro/) | 02.2026 | да |
| Первая позиция в выдаче забирает почти треть кликов (данные Backlinko, цит. FedotovSEO) | [seotop.biz — семантическое ядро](https://seotop.biz/blog/semanticheskoe-yadro/) | 02.2026 | да (вторичная цитата) |

**fact-bank.md:** прямых фактов про SEO-статьи нет — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); «чек-лист экономит 70%» (SerpJet — без первичника); «AI обрабатывает 25% запросов»; любые показы Wordstat без повторного MCP-запроса.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один список ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO-практики на уровне одной статьи.
- GEO-гайды не учат писать текст с нуля.
- Агентские longread'ы перегружены CTA и непроверенными кейсами.
- H1 «которые читают люди» — слабо раскрыт в SERP; наш фокус: **читабельность как SEO-фактор** + техника.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

**Tone:** практично, по-человечески; без корпоративной воды; каждый H2 = подзадача + рекомендация «делать / не делать».

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead после H1 | 40–60 слов, прямой ответ |
| Определение GEO | H2 «SEO + GEO» | 40–60 слов |
| Conversational H2 | «Что такое GEO в SEO?», «Сколько символов нужно?» | Вопрос в заголовке |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, action-first |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | meta, не body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и топ SERP; для how-to longread Excalibur — 8 500–9 500 знаков текста.
2. **Что такое GEO в SEO?** — дополнение к SEO: цель — цитирование в AI-ответах при той же индексируемой базе.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + тематический словарь.
4. **Чем Title отличается от H1?** — Title для сниппета (~50–65 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны блоговой SEO-статье?** — BlogPosting + FAQPage.
6. **Можно ли писать SEO-текст только нейросетью?** — как черновик да; без экспертной правки E-E-A-T падает.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать статистику и показы Wordstat.
- Не копировать структуру Pikapuka / 1ps 1:1.
- Объём текста: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Min **5** нумерованных шагов + чеклист **10+** пунктов.
- Без эмодзи; CTA ≤ 3.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантический кластер под один запрос, спроектирует структуру longread с lead-ответом, напишет и оптимизирует текст без переспама, добавит FAQ и schema для GEO, пройдёт финальный чеклист и опубликует SEO-статью, которую дочитают люди и которую смогут процитировать нейропоисковики.

**action_outline (для writer):**

1. **Определить интент:** открыть топ-5 SERP по «как писать seo статьи»; зафиксировать тип контента (статья vs коммерция) и список подвопросов (PAA, «вместе ищут»).
2. **Собрать семантику:** базовый ключ в Wordstat + подсказки; сгруппировать запросы в 3–5 кластеров (один кластер = одна статья).
3. **Спроектировать каркас:** H1 с главным ключом; 4–6 H2 по подтемам; lead 40–60 слов с прямым ответом; план FAQ 5–7.
4. **Написать черновик для людей:** короткие абзацы, списки/таблицы, инфостиль; после каждого H2 — содержательный ответ без «воды».
5. **Встроить ключи естественно:** главный ключ в H1, первом абзаце, 1–2 H2, Title/Description; LSI по тексту без переспама (ориентир ≤2% плотности).
6. **Добавить E-E-A-T lite:** автор, дата, 1–2 проверяемых факта/примера из таблицы раздела 3.
7. **Упаковать GEO-слой:** answer-first блоки; FAQ в видимом HTML; BlogPosting + FAQPage JSON-LD (handoff schema-агенту).
8. **Техника:** Title 50–65 знаков, Description 140–160; alt у изображений; 3–5 внутренних ссылок; URL-ЧПУ.
9. **Финальный чеклист:** пройти 15–20 пунктов (семантика, мета, структура, FAQ, schema, читабельность, island test) — только после «да» публиковать.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен; LSI — экспертно |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
