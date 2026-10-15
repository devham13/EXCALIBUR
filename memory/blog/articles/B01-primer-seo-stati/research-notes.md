# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + эталон формата на самой статье)  
**research_date:** 2026-10-06  
**disclaimer:** Все даты, версии и статистика проверены на 2026-10-06 (2026 год).

**utility_gate (тема):** PASS (`search_intent: how_to`, `article_mode: B`)

---

## 1. SERP-обзор (WebSearch Cursor, 06.10.2026)

Источник: живой WebSearch + сверка с `research-serp.json` (18 уникальных URL). Топ не «новости», а пошаговые гайды 2026; доминируют longread с семантикой → структура → E-E-A-T/GEO → чек-лист.

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: H1–H4, естественность ключей, Wordstat/Вебмастер, абзацы 3–5 строк, title/description, alt, перелинковка; 5 шагов workflow | Нет GEO/нейропоиска; CTA Директа | Блоки про запуск рекламы; «SEO = ключи» без GEO-слоя |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Правило «ответ сразу после H2»; смысл → ключи; списки/таблицы; полный цикл | Уклон в массовую генерацию ИИ | Копировать промпт-фабрику 1:1 |
| 3 | [articleai.ru/blog/kak-napisat-seo-statyu-v-2026-…](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Агентский how-to (17.08.2026) | Семантика → конкуренты → алгоритм; FAQ/schema; мониторинг Вебмастер | «Плотность 2–4%», «70% успеха на подготовке» — без первичника | Цифры плотности ключей как норма |
| 4 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-…](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Чек-лист + E-E-A-T (2026) | Serpstat/Wordstat, schema Article+FAQ, title ~65 знаков | Кейсы с % без источника | Agency-кейсы с непроверенным ROI |
| 5 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 7 шагов для новичков (2026) | Чёткий workflow: запросы → SERP → структура → текст → meta → релевантность → публикация | Мало GEO | — |
| 6 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 13 шагов + WordPress (2026) | Интент, таблицы/списки, финальный чек-лист | Длинный WP-уклон | 13 H2 под копию 1:1 |
| 7 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Короткий принцип «полный ответ на странице» | Поведенческий сигнал (не возвращаться в поиск) | Мало чек-листа/schema/GEO | «Просто следуй принципам» без шагов |
| 8 | [leadstream.marketing/blog/geo-optimization-guide-2026](https://leadstream.marketing/blog/geo-optimization-guide-2026) | GEO-справочник (2025–2026) | Таблица SEO vs AEO vs GEO; FAQ/schema для AI | Не учит писать текст с нуля | Sales-narrative агентства |

**Паттерн SERP:** запрос «как писать seo статьи 2026» закрывают **инструкции 7–13 шагов**, чек-листы и блоки про ИИ. H1 «которые читают люди» в топе почти не встречается — пробел для Excalibur.

**Intent:** `how_to` — собрать семантику → структура longread → текст для людей → meta/schema → GEO-чанки → чеклист перед публикацией. Вторичный: связать **seo текст для блога** и **geo оптимизация статьи** в одном workflow, не двумя проектами.

---

## 2. Яндекс Wordstat (MCP `user-mcp-kv`, 06.10.2026)

### ⚠️ WORDSTAT AUTH WARNING

Вызов `wordstat_get_top_requests` для `как писать seo статьи`, `seo текст для блога`, `geo оптимизация статьи` **не выполнен**: namespace MCP `user-mcp-kv` недоступен в среде Cloud Agent (сервер не подключён к сессии).  

**Действие для команды:** подключить MCP в `.cursor/mcp.json` / Cloud Secrets и обновить OAuth-токен Wordstat:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40  

**Точные показы/мес в таблицу ниже не заносились** — без API цифры не выдумываем.

### LSI и смежные формулировки (экспертная семантика по SERP + подсказки, без частотности)

**Кластер «написание»:** как написать seo статью, seo копирайтинг, seo текст для блога, seo текст для сайта, структура seo статьи, пошаговая инструкция seo статья.

**Кластер «семантика»:** семантическое ядро, яндекс вордстат, lsi фразы, сбор ключевых слов, кластеризация запросов, интент запроса.

**Кластер «техника»:** title description, h1 h2 h3, meta-теги, alt текст, внутренняя перелинковка, schema.org article, faqpage, blogposting json-ld.

**Кластер «качество»:** e-e-a-t, читабельность, переспам ключей, уникальность текста, поведенческие факторы, полнота ответа.

**Кластер «GEO» (secondary):** geo оптимизация статьи, generative engine optimization, нейропоиск, ai overviews, answer-first, атомарные блоки, llms.txt.

**SEO-стратегия для writer:** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блок про формат блога; «geo оптимизация статьи» — отдельный подблок внутри H2 «SEO + GEO», не подменять H1.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир **3–5 строк**; списки для перечислений | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| **H1 — один** на страницу; H2–H4 для смысловых блоков | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают **смысл и полезность**, не плотность ключей; переспам вреден | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в **Яндекс Вордстат** и **Яндекс Вебмастер** | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Кластеризация: под каждую смысловую группу запросов — **отдельная страница** | [Яндекс — семантическое ядро](https://direct.yandex.ru/base/articles/semanticheskoe-yadro-sajta) | 2026 | да |
| Для новых сайтов разумнее начинать со **СЧ/НЧ**, затем добавлять ВЧ | [Яндекс — семантическое ядро](https://direct.yandex.ru/base/articles/semanticheskoe-yadro-sajta) | 2026 | да |
| Title — ориентир **~60 символов**, description **140–160** с ключом | [Pawetta — SEO-текст 2026](https://pawetta.com/baza/seo-tekst-kak-pisat/) | 2026 | да |
| Информационная статья в рунете — ориентир **4000–8000 знаков** при полноте темы | [Pawetta — SEO-текст 2026](https://pawetta.com/baza/seo-tekst-kak-pisat/) | 2026 | да (как ориентир ниши, не норма Excalibur) |
| How-to статья — **1200–2500 слов** (ориентир типа страницы) | [Spilno Agency — SEO copywriting 2026](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да (как диапазон типа, не догма) |
| После каждого **H2 — содержательный ответ** в первых предложениях | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Главный ключ — H1, первый абзац, 1–2 H2, title/description; LSI — по смыслу | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| SEO-статья в топ закрывает **интент**; прямой ответ в **первых ~100 словах** | [Seotika — SEO-статьи 2026](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| Иерархия заголовков **H1 → H2 → H3** без пропуска уровней | [Seotika — SEO-статьи 2026](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| GEO (Generative Engine Optimization) — оптимизация для **цитирования в ответах AI**, не замена SEO | [LeadStream — GEO 2026](https://leadstream.marketing/blog/geo-optimization-guide-2026) | 12.2025 | да |
| AEO — оптимизация под **featured snippets / быстрые ответы** в классическом поиске | [LeadStream — GEO 2026](https://leadstream.marketing/blog/geo-optimization-guide-2026) | 12.2025 | да |
| Главная задача статьи — **полный ответ**; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| Schema **Article/BlogPosting + FAQPage** — гигиена для сниппета и структуры | [Pikapuka — гайд SEO](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| H1 должен **отличаться** от Title | [Pikapuka — гайд SEO](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |

**fact-bank.md:** фактов по SEO-написанию нет — использовать только таблицу выше.

**Не использовать как факт:** «+140% трафика» (Pikapuka); «плотность ключей 2–4%» (ArticleAI); «подготовка = 70% успеха» (ArticleAI); «56% AI vs поиск» из сниппетов без первичника LeadStream.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** одна **рабочая система** для автора блога: SEO-статья 2026 = longread, который **дочитывают люди** и который **можно процитировать** в нейропоиске. Фокус H1 — читабельность (структура, lead, «острова смысла») + техника (meta, FAQ, schema handoff, GEO-чанки).

**Отличие от конкурентов:**
- Яндекс — канон без GEO; GEO-гайды не учат писать с нуля.
- Агентские longread’ы перегружены E-E-A-T-кейсами и ИИ-масштабом.
- Excalibur B01 — **эталон**: сам материал демонстрирует формат (режим B, 8,5–9,5k знаков по quality-blog).

**H2-каркас (карточка + research):**
1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

**Tone:** практично, по-человечески; без корпоративной воды и эмодзи в `article.html`.

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок SEO+GEO | «GEO — …» |
| Conversational H2 | FAQ hints | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA | Блок понятен без соседних |
| Schema handoff | meta | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Упоминание, не замена sitemap |
| internal_links | карточка | `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — **8 500–9 500** знаков текста.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + тематическая лексика (Яндекс).
4. **Чем Title отличается от H1?** — Title для сниппета (~60 знаков), H1 — на странице; не дублировать.
5. **Какие schema для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt?** — опциональный файл для AI-краулеров; не замена robots/sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, meta, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать Wordstat-частотность до появления MCP-данных.
- Не копировать 7–13 шагов конкурентов 1:1.
- Объём: **8 500–9 500** знаков (`shared/quality-blog.md`).
- Минимум **5** нумерованных шагов в теле + чеклист **10+** пунктов.
- Без эмодзи в HTML; CTA ≤ 3.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за одну сессию соберёт семантику под один запрос, спланирует структуру longread с FAQ, напишет и оптимизирует черновик под людей и нейропоиск, оформит Title/Description и передаст schema на публикацию, затем пройдёт финальный чеклист перед выкладкой.

**action_outline (workflow для how-to):**

1. **Зафиксировать интент:** один primary query («как писать seo статьи»), secondary — в подзаголовках/FAQ; выписать 5–10 вопросов пользователя из SERP и «People also ask».
2. **Собрать семантику:** Wordstat + подсказки → кластер 15–25 фраз; убрать мусор; для каждого H2 — свой подкластер (после появления MCP — зафиксировать показы в таблице).
3. **Разобрать топ-5 URL:** таблица H2 конкурентов, пробелы (читабельность, GEO, чеклист) — наш дифференциатор.
4. **Собрать скелет:** H1 из карточки; 4 H2 из outline; 5–7 FAQ; план lead (40–60 слов определение + обещание результата).
5. **Написать черновик «для людей»:** короткие абзацы, списки, таблица SEO vs GEO; после каждого H2 — прямой ответ; без переспама.
6. **Техслой SEO:** Title (~60), Description (140–160), slug; ключ в lead и 1–2 H2; alt у иллюстраций; 2–4 осмысленные внутренние ссылки.
7. **GEO-слой:** атомарные блоки, answer-first в FAQ; handoff JSON-LD BlogPosting + FAQPage (schema-агент); упомянуть llms.txt опционально.
8. **Чеклист 15–20 пунктов:** семантика, meta, структура, факты с URL, schema, мобильность, перелинковка — printable logic.
9. **Публикация и контроль:** отправка URL в Вебмастер; через 2–4 недели — позиции, время на странице, доработка слабых H2.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (см. §2) |
| Таблица фактов с URL | ✅ (18) |
| utility_verdict + action_outline | ✅ |
| GEO hooks + FAQ | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
