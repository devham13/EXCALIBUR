# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-08-27  
**disclaimer:** Все даты, версии и статистика проверены на 2026-08-27 (2026 год).

---

## 1. SERP-обзор (WebSearch Cursor, 27.08.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Авторитет; 5 шагов (тема → семантика → структура → текст → оптимизация); H1–H4; Wordstat/Вебмастер; примеры «плохо/хорошо»; абзацы 3–5 строк | Нет GEO/нейропоиска; CTA Директа; «читабельность для людей» не выделена отдельно | Блок про Директ; копировать H-структуру 1:1 без GEO-слоя |
| 2 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист агентства (июн. 2026) | 9 критериев качества; E-E-A-T + ЭПОС; AI-выдача (Overviews, Алиса, ChatGPT); answer-first; различие OAI-SearchBot vs GPTBot | Agency CTA «обновим ваши статьи»; нет единого numbered workflow | Продающий блок TexTerra |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (2026) | Семантика, LSI, E-E-A-T; Title ~65 знаков; чек-лист 10 шагов; Schema Article + FAQPage | «+140% за 3 недели» без первичника; 7 разделов — перегруз | Непроверенные проценты кейсов |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samomostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | H2 = подтема кластера; «сначала смысл, потом оптимизация»; island test для E-E-A-T | Длинный sales-narrative; ИИ как центр, не workflow | Структуру 1:1 |
| 5 | [serpjet.ru/blog/chek-list-idealnoj-seo-stati-v-2026-ot-semantiki-do-cta-zamenit-seo-spetsialista-4847](https://serpjet.ru/blog/chek-list-idealnoj-seo-stati-v-2026-ot-semantiki-do-cta-zamenit-seo-spetsialista-4847/) | Чек-лист B2B | Кластеризация по интенту; промпт-гайд для ИИ; RAG-подход | Продаёт SerpJet; мало про «читают люди» | Agency bias |
| 6 | [pawetta.com/baza/seo-tekst-kak-pisat](https://pawetta.com/baza/seo-tekst-kak-pisat/) | Практик (2026) | Title ≤60, description 140–160; H2-вопросы для быстрых ответов Яндекса; workflow «интент → Wordstat → структура» | Узкий фокус на текст, без schema/GEO deep-dive | — |
| 7 | [pawetta.com/blog/geo-optimizaciya](https://pawetta.com/blog/geo-optimizaciya/) | GEO-гайд (июл. 2026) | GEO поверх SEO; answer-first 2–3 предложения; Schema FAQPage/HowTo; llms.txt | Отдельная тема, не how-to написания с нуля | Цены услуг |
| 8 | [developers.google.com/search/docs/fundamentals/creating-helpful-content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Официальный Google | People-first; E-E-A-T; Who/How/Why; ИИ не запрещён, spam — массовая генерация без ценности | Нет пошагового workflow для копирайтера | — |

**Паттерн SERP (август 2026):** топ — «полный гайд / чек-лист 2026» с E-E-A-T, Wordstat, AI-выдачей. Отдельный кластер — GEO-лонгриды. H1 «которые читают люди» слабо закрыт: конкуренты говорят про «качество» и «полезность», но редко связывают **читабельность (инфостиль, структура, island test)** с SEO + GEO в одном workflow.

**Intent:** `how_to` — пользователь хочет **пошаговую систему**: интент → семантика → структура → черновик → оптимизация → GEO-слой → чеклист перед публикацией. Вторичный: «seo текст для блога», «geo оптимизация статьи».

**Пробел для Excalibur:** единый **action-first workflow** «SEO + GEO в одной статье» с акцентом на **читаемость как фактор ранжирования и цитирования**; режим B — сама статья B01 как эталон формата.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` не подключён в Cloud Agent environment (27.08.2026). Инструмент `wordstat_get_top_requests` недоступен. **Точные объёмы спроса не получены — цифры показов в текст не включать.**

При восстановлении MCP — повторить запросы:
- `как писать seo статьи` (primary)
- `seo текст для блога`
- `geo оптимизация статьи`

### LSI-кластеры (из SERP + secondary queries, без Wordstat)

| Кластер | Фразы для writer |
|---------|------------------|
| Написание | как писать seo статьи, seo текст для блога, seo копирайтинг, написать seo статью самому |
| Структура | структура seo статьи, заголовки h1 h2, title description, чек-лист seo статьи |
| Семантика | семантическое ядро, lsi слова, wordstat, поисковый интент |
| Качество | e-e-a-t, инфостиль, переспам, полезный контент, people-first |
| GEO | geo оптимизация статьи, generative engine optimization, ai выдача, faq schema, answer-first |

**SEO-стратегия без Wordstat:** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блок про формат блога; «geo оптимизация статьи» — отдельный H2 или подблок в workflow, не подменять H1.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир **3–5 строк**; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| **H1 — один** на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают **смысл и полезность**, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в **Яндекс Вордстат** и **Яндекс Вебмастер** | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-текст 2026: двигаться **от главного ответа к деталям** — сначала суть, потом нюансы | [TexTerra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| E-E-A-T — **не показатель для накрутки**; рамка доверия (опыт, экспертиза, авторитет, достоверность) | [TexTerra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Яндекс **ЭПОС**: экспертность, полезность, оригинальность, содержательность | [TexTerra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Для AI-выдачи: **короткий прямой ответ** в начале; H2/H3 понятны без контекста; даты публикации/обновления | [TexTerra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Не блокировать **OAI-SearchBot** для ChatGPT-поиска; отличать от **GPTBot** (обучение моделей) | [TexTerra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| H1 **отличается** от Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Title — ориентир **~65 знаков**, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Title до **60** символов, description **140–160** с ключом (практика копирайтера) | [Pawetta — SEO-текст](https://pawetta.com/baza/seo-tekst-kak-pisat/) | 2026 | да |
| H2-**вопросы** («сколько ключей», «какой объём») попадают в блок быстрых ответов Яндекса | [Pawetta — SEO-текст](https://pawetta.com/baza/seo-tekst-kak-pisat/) | 2026 | да |
| GEO (Generative Engine Optimization) — оптимизация под **цитирование в ответах AI**, стоит **на SEO** | [Pawetta — GEO-гайд](https://pawetta.com/blog/geo-optimizaciya/) | 11.07.2026 | да |
| Прямой ответ в **первых 2–3 предложениях** раздела — ключевой GEO-приём | [Pawetta — GEO-гайд](https://pawetta.com/blog/geo-optimizaciya/) | 11.07.2026 | да |
| Google: контент **people-first**; E-E-A-T — mix факторов, **не отдельный ranking factor** | [Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| Google **не запрещает** ИИ; нарушение — автоматизация **для манипуляции выдачей** без пользы | [Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| Google рекомендует **bylines** и прозрачное авторство (Who/How/Why) | [Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| Google **не имеет** предпочтительного word count | [Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| Schema **FAQPage** и **HowTo** — машиночитаемые Q&A для AI-поиска | [Pawetta — GEO-гайд](https://pawetta.com/blog/geo-optimizaciya/) | 11.07.2026 | да |
| Главная задача статьи — **полный ответ**; возврат в поиск = сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**fact-bank.md:** прямых фактов по SEO-написанию нет — использовать только таблицу выше.

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «40% эффекта от answer-first» (Pawetta — без первичника); любые показы Wordstat без MCP.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → черновик для людей → техника → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- TexTerra даёт чек-лист критериев, но не связный numbered workflow.
- H1 «**которые читают люди**» — слабо раскрыт в SERP; наш фокус: **инфостиль + island test + атомарные H2** как SEO- и GEO-фактор одновременно.

**Режим B:** статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**Tone:** практично, по-человечески; без корпоративной воды.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (один контент, две цели)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD)
4. Чеклист перед публикацией (15–20 пунктов)

Подтемы внутри блоков: семантика/Wordstat, Title/Description, E-E-A-T lite, llms.txt, OAI-SearchBot.

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead после H1 | 40–60 слов |
| Определение GEO | Блок «SEO + GEO» | 40–60 слов |
| Conversational H2 | «Что такое GEO в SEO?», «Сколько символов нужно?» | Вопрос в заголовке |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, action |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA | Блок понятен без соседних |
| Schema | handoff schema-агенту | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и конкуренты; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — дополнение к SEO: цель — цитирование в AI-ответах при базе индексируемого контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 — на странице.
5. **Какие schema для SEO-статьи блога?** — BlogPosting + FAQPage.
6. **Можно ли писать SEO-статью нейросетью?** — да как черновик; факты, опыт и редактура — человек (Google people-first).
7. **Как проверить статью перед публикацией?** — чеклист: интент, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать статистику и показы Wordstat.
- Не копировать структуру Pikapuka (7 разделов) 1:1.
- Объём: **8 500–9 500** знаков (quality-blog.md).
- Без эмодzi в article.html.
- Min **5** нумерованных шагов в теле + чеклист 10+ пунктов.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель пройдёт полный цикл написания SEO-статьи: определит поисковый интент и соберёт семантику, построит структуру H1–H3 с answer-first блоками, напишет черновик для людей, добавит E-E-A-T и техоптимизацию (Title/Description, перелинковка), упакует материал под GEO (FAQ, schema, атомарные чанки) и проверит готовность по чеклисту перед публикацией.

**action_outline (для how-to статьи):**

1. **Определить интент:** вбить primary query в Яндекс/Google; классифицировать (информационный/коммерческий); зафиксировать, что пользователь сделает после прочтения.
2. **Собрать семантику:** Wordstat + топ-10 SERP → таблица: основной ключ, LSI, вопросы для FAQ; кластеризовать по подтемам для H2.
3. **Построить каркас:** H1 с ключом (≠ Title); H2 = подзадача + прямой ответ в первом абзаце; H3 для деталей; lead 40–60 слов с определением.
4. **Написать черновик для людей:** короткие абзацы (3–5 строк), списки/таблицы, инфостиль без воды; ключи естественно в H1, lead, 1–2 H2.
5. **Добавить E-E-A-T:** byline, 1 кейс/цифра/скрин, ссылки на первоисточники; island test каждого H2.
6. **Техоптимизация:** Title ~60–65 знаков, Description 140–160; alt у изображений; 2–4 осмысленные внутренние ссылки.
7. **GEO-слой:** FAQ 5–7 вопросов (ответ ≤80 слов); JSON-LD BlogPosting + FAQPage; проверить robots.txt (OAI-SearchBot не заблокирован).
8. **Финальный чеклист:** интент закрыт, мета, структура, FAQ/schema, факты проверены, читабельность — опубликовать.

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
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 конкурентов (Яндекс Direct, TexTerra, Pikapuka, 1ps.ru, SerpJet, Pawetta×2, Google Search Central). Wordstat MCP недоступен — LSI из SERP. Угол — единый workflow SEO+GEO longread «для людей»: инфостиль, answer-first, FAQ/schema, чеклист. 22 факта с URL, 8 шагов action_outline, 7 FAQ. Готов к writer.
===
