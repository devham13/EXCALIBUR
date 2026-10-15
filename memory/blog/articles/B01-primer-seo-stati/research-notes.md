# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата)  
**research_date:** 2026-09-09  
**disclaimer:** Все даты, версии и статистика проверены на 2026-09-09.

---

## 1. SERP-обзор (WebSearch, 2026-09-09; 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон SEO-текста: семантика → структура → текст → мета; примеры «плохо/хорошо»; Wordstat; абзацы 3–5 строк; без переспама | Нет GEO/нейропоиска; CTA Директа в конце | Коммерческий блок про Директ; копировать H1–H4 без GEO-слоя |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-...](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 | Кластеры из Wordstat (3–5 групп); «сначала смысл, потом оптимизация»; E-E-A-T + ИИ; практические примеры | Длинный narrative; GEO как побочный эффект | Структуру 1:1; непроверенные кейсы роста |
| 3 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм (13 шагов, фев. 2026) | Полный цикл: спрос → интент → конкуренты → структура → WP → индексация; таблица «что у конкурента / что делать вам» | Уклон в WordPress-хостинг; мало про schema/GEO | Affiliate-блоки Timeweb/Paradigma; 13 H2 как копипаст |
| 4 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Гайд для новичков 2026 | План, семантика, чек-лист для топа; простой язык | Поверхностный GEO; мало про AI-выдачу | Generic «люди и роботы» без actionable GEO |
| 5 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-...](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (2026) | E-E-A-T, Schema Article+FAQPage, Title ~65 знаков, чек-лист 10 шагов | Agency tone; кейсы без первичника | «+140% трафика» и прочие цифры без URL |
| 6 | [articleai.ru/blog/kak-napisat-seo-statyu-v-2026-...](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Инструкция 2026 | Семантика → публикация; актуальный год в title | Продаёт AI-сервис; thin differentiation | Product-led CTA вместо чеклиста |
| 7 | [neurounit.ai/blog/seo-dlya-bloga-kak-vesti](https://neurounit.ai/blog/seo-dlya-bloga-kak-vesti/) | SEO для блога | «Одна статья = один кластер»; первый абзац решает удержание; hub-spoke перелинковка | Мало техники schema/GEO | SaaS-продукт как главный герой |
| 8 | [habr.com/ru/articles/1042732](https://habr.com/ru/articles/1042732/) | GEO/AEO longread 2026 | RAG-архитектура; Answer-First; Schema FAQPage; GEO не заменяет SEO | Encyclopedia, не учит писать с нуля | Копировать таблицу SEO vs GEO целиком; agency bias |

**Паттерн SERP (сентябрь 2026):** топ по «как писать seo статьи 2026» — longread-гайды с чек-листом, Wordstat, E-E-A-T и блоком про ИИ/GEO. Прямого попадания в H1 «которые читают люди» мало: конкуренты говорят «для людей и роботов», но не связывают **читабельность** (инфостиль, короткие абзацы, lead-ответ) с **извлекаемостью для AI**.

**Intent:** how_to — пользователь хочет **пошаговый workflow**: проверить спрос → собрать семантику → структура → черновик → мета → FAQ/schema → финальный чеклист. Вторичный intent: как в одной статье совместить SEO и GEO без двух отдельных проектов.

**Пробел для Excalibur:** единый **action-first** гайд «SEO + GEO в одном longread» с акцентом на **читаемость как фактор ранжирования и цитирования**; режим B — сама статья B01 = эталон (8,5–9,5k знаков, FAQ, BlogPosting + FAQPage).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 2026-09-09)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в текущем Cloud Agent окружении (namespace не подключён; вызов `wordstat_get_top_requests` невозможен). Точные объёмы показов **не получены**. Обновите токен и MCP через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40 — см. `.cursor/skills/excalibur-research/SKILL.md`.

### Таблица спроса

| Фраза | Показы/мес |
|-------|------------|
| как писать seo статьи | *не получено — MCP недоступен* |
| seo текст для блога | *не получено — MCP недоступен* |
| geo оптимизация статьи | *не получено — MCP недоступен* |

### Экспертная семантика (без объёмов; для writer до повторного прогона Wordstat)

**Primary cluster:** как писать seo статьи, как написать seo статью, seo текст для сайта, seo текст для блога, seo статья пример, seo оптимизированная статья.

**LSI из SERP + конкурентов (вписывать естественно):**

- семантическое ядро, кластер запросов, LSI-слова, интент запроса, Wordstat, Яндекс Вебмастер  
- структура longread, H1 H2 H3, lead-абзац, title description, meta-теги, alt-текст  
- E-E-A-T, экспертность автора, переспам, уникальность, внутренняя перелинковка  
- FAQ блок, FAQPage schema, BlogPosting, JSON-LD, Rich Results Test  
- GEO, answer-first, нейровыдача, AI Overviews, Алиса AI, цитирование нейросетями  
- чеклист перед публикацией, сколько символов в seo статье  

**SEO-стратегия (до данных Wordstat):** primary «как писать seo статьи» в H1/lead; secondary «seo текст для блога» — в блок про блог и hub-spoke; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье», не в title целиком (риск путаницы с локальной geo-SEO).

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — он зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир **3–5 строк**; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| **H1 — один** на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают **смысл и полезность**, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в **Яндекс Вордстат** и **Яндекс Вебмастер** | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-текст должен **полностью отвечать** на запрос пользователя — критерий качества важнее объёма | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Фразы из Wordstat группируют в **3–5 смысловых кластеров** — основа структуры статьи | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| После каждого H2 — **содержательный ответ** сразу, не «в этой части мы рассмотрим…» | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Главный ключ — в H1, первом абзаце, 1–2 заголовках H2, title и description | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Для блога: **одна статья = один смысловой кластер** (главный запрос + хвосты) | [NeuroUnit — SEO для блога](https://neurounit.ai/blog/seo-dlya-bloga-kak-vesti/) | 2026 | да |
| **Первый абзац** решает удержание: если нет ответа на вопрос — пользователь уходит | [NeuroUnit — SEO для блога](https://neurounit.ai/blog/seo-dlya-bloga-kak-vesti/) | 2026 | да |
| E-E-A-T: «Experience» добавлено в **декабре 2022** (ранее E-A-T) | [Semrush — E-E-A-T](https://www.semrush.com/blog/eeat/) | 2026 | да |
| E-E-A-T **не является** подтверждённым прямым ranking factor; используется в Search Quality Rater Guidelines | [Semrush — E-E-A-T](https://www.semrush.com/blog/eeat/) | 2026 | да |
| Контент с сильными E-E-A-T-сигналами лучше виден и в **AI-ответах** (ChatGPT, Perplexity и др.) | [Semrush — E-E-A-T](https://www.semrush.com/blog/eeat/) | 2026 | да |
| Генеративные поисковики (Perplexity, Алиса AI, Google AI Overviews) работают на **RAG**: извлечение чанков → суммаризация → синтез | [Habr — GEO/AEO 2026](https://habr.com/ru/articles/1042732/) | 02.06.2026 | да |
| Стратегия **Answer-First**: прямой ответ на интент — в **первых 2–5 предложениях** раздела | [Habr — GEO/AEO 2026](https://habr.com/ru/articles/1042732/) | 02.06.2026 | да |
| GEO **не заменяет** SEO, а надстраивается над индексируемым контентом | [Habr — GEO/AEO 2026](https://habr.com/ru/articles/1042732/) | 02.06.2026 | да |
| Оптимальный блок ответа для извлечения ИИ — **40–80 слов**, самодостаточный | [trigub.ru — GEO 2026](https://trigub.ru/blog/geo-prodvizhenie-sayta/) | 2026 | да |
| FAQPage JSON-LD — прямой сигнал для answer engines; ответ FAQ **≤80 слов** | [CrawlProof — AI schema](https://crawlproof.com/blog/ai-publishing-schema-markup-answer-engine-citations) | 2026 | да |
| `datePublished` / `dateModified` в schema должны **совпадать** с видимой датой на странице | [CrawlProof — AI schema](https://crawlproof.com/blog/ai-publishing-schema-markup-answer-engine-citations) | 2026 | да |
| В 2026 недостаточно «ключи + уникальность» — нужны интент, структура, полнота ответа, опыт автора | [olegweb.ru — SEO-статья](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |

**fact-bank.md:** прямых фактов по SEO-написанию нет — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика» (Pikapuka); «Answer-first +30–40%» без указания источника агентства; HubSpot −70–80% как универсальный прогноз (только как цитированный кейс Habr).

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **longread, который читают люди** и который **можно процитировать** в нейровыдаче. Единый workflow: интент → кластеры Wordstat → структура H2 → черновик без воды → мета → FAQ/schema → GEO-упаковка (answer-first чанки) → чеклист 15+ пунктов.

**Почему отличается от конкурентов:**

- Яндекс даёт канон SEO без GEO; GEO-гайды (Habr) не учат писать текст с нуля.  
- Агентские гайды перегружены кейсами и CTA.  
- H1 «**которые читают люди**» — слабо раскрыт в SERP; наш фокус: **инфостиль + атомарные блоки** = и поведение, и RAG.

**Tone:** практично, по-человечески; каждый H2 = подзадача + «делать / не делать».

**H2-каркас (из карточки B01 + research):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как (JSON-LD вне body)  
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO — …» |
| Answer-first | Каждый H2 | Первое предложение = прямой ответ |
| FAQ 5–7 пар | Конец | 40–80 слов на ответ |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Island test | QA | Блок понятен без соседних |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при той же базе контента.  
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + тематические слова.  
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 — на странице; не дублировать дословно.  
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.  
6. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.  
7. **Можно ли писать SEO-статью только под роботов?** — нет; без удержания человека падают и SEO-, и GEO-сигналы.

---

## 7. Риски для writer

- Не выдумывать объёмы Wordstat — ждать MCP или пометка «уточните в Вордстат».  
- Не копировать Pikapuka/olegweb 1:1.  
- Объём текста: **8 500–9 500** знаков (`quality-blog.md`).  
- Min **5** нумерованных шагов + чеклист **10+** пунктов.  
- Без эмодзи; site_url — `/` по карточке.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за один проход соберёт семантический кластер в Wordstat, построит структуру longread с answer-first блоками, напишет черновик без переспама, оформит Title/Description и FAQ, подключит BlogPosting + FAQPage schema и пройдёт финальный чеклист перед публикацией — с учётом GEO для нейровыдачи.

**action_outline (для writer):**

1. **Проверить спрос и интент:** вбить primary_query в Wordstat и SERP; выписать 15–25 фраз; отсечь запросы с другим intent; сгруппировать в 3–5 кластеров.  
2. **Разобрать топ-5 конкурентов:** какие H2 закрывают подвопросы; чего не хватает (FAQ, таблицы, lead-ответ, schema).  
3. **Собрать outline:** H1 с главным ключом; H2 по кластерам; под каждым H2 — тезис первой строки (answer-first).  
4. **Написать черновик:** lead с прямым ответом; абзацы 3–5 строк; списки и таблица; личный опыт/пример без выдуманных цифр.  
5. **Встроить семантику:** главный ключ в H1, lead, 1–2 H2, title/description; LSI — только где звучит естественно.  
6. **Оформить мета и медиа:** Title ~60–65 знаков, description с пользой; alt у изображений; внутренние ссылки на hub-страницы.  
7. **Добавить FAQ 5–7** и JSON-LD BlogPosting + FAQPage (schema — отдельная роль pipeline).  
8. **GEO-упаковка:** каждый H2 — самодостаточный чанк 40–80 слов в первом блоке; видимые datePublished/dateModified.  
9. **Финальный чеклист 15+ пунктов** перед публикацией (семантика, переспам, schema, мобильность, перелинковка).

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (см. §2) |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
