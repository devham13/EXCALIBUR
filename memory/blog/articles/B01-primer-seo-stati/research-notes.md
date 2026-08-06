# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата на самой статье)  
**research_date:** 2026-08-06  
**disclaimer:** Все даты, версии и статистика проверены на 2026-08-06 (2026 год).

---

## 1. SERP-обзор (WebSearch, август 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон: интент, Wordstat, H1–H4, естественные ключи, мета, перелинковка; 5 шагов workflow | Нет GEO/нейропоиска; CTA Директа в конце | Блок про Директ; копировать структуру без GEO-слоя |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Кластеризация Wordstat (3–5 групп); правило «ответ сразу после H2»; чек-лист | Длинный sales-narrative про ИИ-инструменты | Непроверенные кейсы трафика; 1:1 структура |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский гайд (2026) | E-E-A-T, семантика, Schema Article+FAQPage, Title ~65 знаков | Кейсы «+140% за 3 недели» без первичника | Agency tone; 7-разделный каркас 1:1 |
| 4 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм (обнов. 05.02.2026) | 13 шагов от ключа до WordPress; интент, конкуренты, чек-лист | Мало GEO; уклон в WP-хостинг/шаблоны | Партнёрские CTA Timeweb/Paradigma |
| 5 | [fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | Практический гайд 2026 | Плотность информации > длина; атомарные ответы для AI; pillar+cluster; чек-лист E-E-A-T | Спорные эксперименты «ИИ vs человек» без методологии | Копировать таблицу ИИ vs эксперт без оговорок |
| 6 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | SEO-агентство | Принцип «полный ответ на одной странице»; LSI; поведенческий сигнал | Мало actionable шагов, нет чек-листа 15+ | «Просто следуй принципам» без workflow |
| 7 | [gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | AI SEO 2026 | Прямое попадание в H1 «читают люди» + AI | Узкая ниша digital-агентства | Копировать tone-of-voice 1:1 |
| 8 | [searchengineland.com/what-is-generative-engine-optimization-geo-444418](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) | GEO reference (EN) | SEO vs GEO таблица; метрики citations/SoV | Не учит писать текст с нуля на RU | Переводить EN-блоки без адаптации под RU-поиск |

**Паттерн SERP:** доминируют «полный гайд 2026» с E-E-A-T, Wordstat, чек-листом и блоком про ИИ. Отдельный кластер — GEO-лонгриды (secondary query). H1 «которые читают люди» слабо закрыт: близкий [bestseoserg.com](https://bestseoserg.com/blog/kak-pisat-seo-teksty.html), но без единого SEO+GEO workflow.

**Intent:** `how_to` — пользователь хочет **пошаговую систему** от семантики до публикации и проверки. Вторичный intent: понять, как упаковать статью и для Google/Яндекса, и для AI-выдачи (GEO).

**Пробел для Excalibur:** единый **action-first** workflow «для людей + для нейропоиска» без agency-воды; сама статья B01 — **эталон режима B** (longread 8,5–9,5k знаков, FAQ, schema).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` **не подключён** в Cloud-среде (вызов `wordstat_get_top_requests` недоступен; сервер отсутствует в списке MCP). Точные показы/мес **не получены** из API.

**Действие для пайплайна:** подключить MCP и обновить токен через:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (без цифр спроса — только LSI из SERP + WebSearch)

**Primary cluster:** как писать seo статьи, как написать seo статью, как писать seo тексты, seo копирайтинг 2026

**Secondary (из карточки темы):**
- seo текст для блога, seo текст для сайта, структура seo статьи  
- geo оптимизация статьи, seo и geo, оптимизация под ai выдачу  

**Long-tail / FAQ-intent:**
- сколько символов в seo статье, title и description для статьи  
- что такое geo в seo, e-e-a-t в статье  
- чек-лист seo статьи, семантическое ядро для статьи  
- как проверить seo статью перед публикацией  

**SEO-стратегия для writer:** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блок про формат блога; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье»; faq_hints — в FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — он зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир **3–5 строк**; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| **H1 — один** на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают **смысл и полезность**, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в **Яндекс Вордстат** и **Яндекс Вебмастер** | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| **Title и Description** влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-текст: 5 шагов — тема/конкуренты → семантика → структура → текст → оптимизация | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| После каждого **H2** — сразу содержательный ответ (не «заголовок ради ключей») | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Фразы Wordstat группируют в **3–5 смысловых кластеров** на одну страницу | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Title — ориентир **~65 знаков**, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| H1 должен **отличаться** от Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Schema.org **Article + FAQPage** — для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Запрос «как написать SEO-статью» — **практический информационный** интент: нужны шаги, примеры, чек-листы | [olegweb.ru — алгоритм SEO-статьи](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| **Плотность информации важнее длины**; ответ — в начале, без «воды» | [FireSEO — SEO-тексты 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| Для AI-выдачи нужны **атомарные самодостаточные** абзацы; важную информацию не прятать во вкладки | [FireSEO — SEO-тексты 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| Работает модель **Pillar + Cluster**: один большой гайд + 5–10 узких статей со ссылками | [FireSEO — SEO-тексты 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| Главная задача статьи — **полный ответ**; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| GEO (Generative Engine Optimization) — оптимизация видимости в **ответах генеративных поисковиков**, не замена SEO | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Методы Cite Sources, Quotation Addition, Statistics Addition дают **+30–40%** visibility (Position-Adjusted Word Count) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| На Perplexity.ai — улучшение visibility до **37%** (Princeton GEO-bench) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| **Keyword stuffing** в GEO-контексте работает **хуже baseline** (≈ −10% / −30% в таблице методов) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| SEO: цель — **ранжирование и клик**; GEO: цель — **цитирование в AI-ответе** (citations, share of voice) | [Search Engine Land — GEO](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) | 2026 | да |

**fact-bank.md:** прямых фактов по SEO-написанию нет — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); непроверенные «AI обрабатывает 25% запросов»; точные показы Wordstat (MCP недоступен).

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → текст для людей → GEO-чанки → FAQ/schema → финальный чек-лист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды перегружены E-E-A-T-кейсами и CTA.
- H1 «которые читают люди» слабо раскрыт в SERP — наш фокус: **читабельность как SEO-фактор** + техника.

**Tone:** практично, по-человечески; каждый H2 = подзадача + рекомендация (делать / не делать).

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (не два проекта)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чек-лист перед публикацией (15–20 пунктов)

**Режим B:** сама статья B01 — эталон: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2.

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO — …» |
| Conversational H2 | FAQ-блок | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, action-first |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и конкуренты в SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + LSI; keyword stuffing хуже для GEO (Princeton).
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Как проверить статью перед публикацией?** — чек-лист: семантика, мета, структура, FAQ, schema, ссылки, читабельность, GEO-чанки.
7. **Можно ли писать SEO-статью с помощью ИИ?** — да как черновик; обязательны личный опыт, факты с источниками, удаление ИИ-штампов (FireSEO, Яндекс).

---

## 7. Черновик чек-листа (15–20 пунктов для writer)

1. Проверен интент запроса в SERP (how-to, не «что такое»).  
2. Собран кластер 3–5 групп фраз (Wordstat/подсказки).  
3. H1 один, содержит primary query, отличается от Title.  
4. Title ~65 знаков + Description с триггером.  
5. Lead-абзац отвечает на запрос в первых 2–3 предложениях.  
6. Каждый H2 начинается с прямого ответа.  
7. Абзацы 3–5 строк; списки/таблицы где уместно.  
8. Главный ключ: H1, первый абзац, 1–2 H2, Title/Description.  
9. LSI распределены естественно, без переспама.  
10. Есть блок личного опыта / пример / кейс (E-E-A-T lite).  
11. FAQ 5–7 вопросов с короткими action-ответами.  
12. JSON-LD BlogPosting + FAQPage (schema-роль, не в body).  
13. Alt у изображений; внутренние ссылки на `/` и hub-страницы.  
14. GEO: атомарные чанки, определения 40–60 слов, stats/citations где уместно.  
15. Удалены ИИ-штампы («в заключение», «важно понимать»).  
16. Финальный island test: каждый H2 actionable без контекста соседей.  
17. Даты datePublished/dateModified согласованы с прогоном.  
18. Нет выдуманной статистики — только таблица фактов §3.

---

## 8. Риски для writer

- Не выдумывать показы Wordstat (MCP недоступен).  
- Не копировать структуру Pikapuka/olegweb 1:1.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Без эмодзи в article.html.  
- CTA ≤ 3; не подменять пользу.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель пройдёт полный цикл написания SEO-статьи: проверит интент и семантику, соберёт структуру longread для людей, добавит GEO-упаковку (атомарные блоки, FAQ, schema), пройдёт чек-лист перед публикацией и опубликует материал, который одновременно читается и ранжируется.

**action_outline:**

1. **Зафиксировать задачу и интент:** вбить primary query в Яндекс/Google; определить тип страницы (гайд vs коммерция); записать, что должен сделать читатель после прочтения.  
2. **Собрать семантику:** Wordstat + подсказки + «Похожие вопросы»; сгруппировать фразы в 3–5 кластеров; выбрать главный и 15–25 LSI/хвостов.  
3. **Разобрать топ-5 SERP:** H1/H2, таблицы, FAQ, дата, пробелы; выписать, чем ваша статья будет полнее (опыт, чек-лист, GEO).  
4. **Собрать структуру:** H1 + 4–6 H2 из карточки; под каждым H2 — тезис-ответ; наметить FAQ 5–7 и таблицу/чек-лист.  
5. **Написать черновик «смысл первым»:** короткие абзацы, списки, без переспама; lead с определением SEO-статьи в 40–60 слов.  
6. **Усилить E-E-A-T и GEO:** кейс/скрин/цифра с URL; блок «SEO + GEO»; атомарные абзацы; stats/citations по Princeton-тактикам.  
7. **Техническая упаковка:** Title/Description, ключи в зонах; перелинковка; alt; JSON-LD BlogPosting + FAQPage (handoff schema-роли).  
8. **Финальный чек-лист (§7):** пройти 15–18 пунктов; island test; убрать воду и ИИ-штампы; согласовать даты метаданных.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks + чек-лист | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 конкурентов (Яндекс Direct, 1ps, Pikapuka, olegweb, FireSEO, MaryProject, gracie.digital, Search Engine Land). Wordstat MCP недоступен (⚠️ без показов/мес). Угол — единый how-to workflow SEO+GEO longread «для людей»: читабельность, атомарные чанки, FAQ/schema, чек-лист 18 пунктов. 20 фактов с URL, 8 шагов action_outline, 7 FAQ. Готов к writer.
===
