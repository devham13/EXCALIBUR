# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-08-29  
**disclaimer:** Все даты, версии и статистика проверены на 29.08.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch, август 2026 — 6 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: workflow «семантика → структура → текст → мета»; H1–H4; абзацы 3–5 строк; естественные ключи; Wordstat/Вебмастер; примеры «плохо/хорошо» | Нет GEO/нейропоиска; CTA Директа в конце | Блок про Директ; копировать H-структуру без GEO-слоя |
| 2 | [hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | Практический how-to (2026) | Порядок «спрос → текст → оптимизация», не «10k знаков + 15 ключей»; 6 шагов; SERP-анализ до структуры | Мало GEO; нет чек-листа публикации | Шаблон «для клиента» без бизнес-контекста блога |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread агентства (обновл. 15.06.2026) | Кластеры из Вордстата (3–5 групп); правило «после H2 — сразу ответ»; ИИ для черновика + ручная правка; GEO/AEO блок | Длинный sales-narrative; часть истории алгоритмов — фон, не action | Копировать 20-минутную структуру 1:1; непроверенные «+X%» из кейсов |
| 4 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм (обновл. 05.02.2026) | 13 шагов «от ключа до публикации»; WordPress-оформление; таблица «что есть у конкурента → что сделать вам»; акцент на интент и поведение | Узкий WP-фокус; нет GEO-schema handoff | Хостинг/шаблоны CTA в теле |
| 5 | [promptsa.com/ru/blog/ai-seo-content-guide](https://promptsa.com/ru/blog/ai-seo-content-guide) | AI + SEO workflow | 12 шагов; EEAT-ошибки; FAQ из «People Also Ask»; отдельная оптимизация Title/Description | Англоязычная методика, адаптированная под RU; мало Яндекс-специфики | Слепое копирование промпт-шаблонов без fact-check |
| 6 | [impact-dl.ru/geo-otvety-ii-2026-chto-pomogaet-popast-v-citatu](https://impact-dl.ru/geo-otvety-ii-2026-chto-pomogaet-popast-v-citatu/) | GEO/AEO практика (2026) | Честная позиция: Schema/FAQ ≠ гарантия цитаты; AEO vs GEO; answer-first; доступ краулеров | Не учит писать SEO-текст с нуля | Обещания «добавим FAQ — попадёте в нейроответ» |

**Паттерн SERP (август 2026):** топ — «полный гайд 2026» с интентом, Wordstat, структурой H2–H3 и блоком про ИИ как помощника черновика. Отдельный кластер — GEO/AEO без пошагового writing workflow. H1 «которые читают люди» в выдаче почти не встречается — дифференциатор B01 актуален.

**Intent:** `how_to` — собрать семантику → структура → черновик для человека → техоптимизация → FAQ/schema → GEO-упаковка → чеклист перед публикацией. Вторичный: связать SEO и GEO в одном материале, не дублируя два проекта.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` недоступен в текущем Cloud Agent run (namespace not found). Вызов `wordstat_get_top_requests` выполнить не удалось. Точные объёмы спроса **не получены** — цифры ниже **не** подставлять в статью как «показы/мес».

**Действие для оператора:** подключить MCP `user-mcp-kv` или обновить токен Wordstat:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Запросы для повторного сбора (когда MCP доступен)

| Запрос | Назначение |
|--------|------------|
| как писать seo статьи | primary_query |
| seo текст для блога | secondary_1 |
| geo оптимизация статьи | secondary_2 |
| seo статья для сайта | LSI из SERP |
| как написать seo текст | LSI из SERP |
| структура seo статьи | LSI из SERP |

### LSI для writer (экспертная семантика из SERP + карточка B01, **без** Wordstat-частот)

- как писать seo статьи, seo текст для блога, seo статья для сайта  
- структура seo статьи, seo текст пример, написание seo статей  
- title description h1, семантическое ядро, lsi слова, яндекс вордстат  
- geo оптимизация статьи, generative engine optimization, answer-first  
- faq schema json-ld, blogposting, чеклист перед публикацией  
- сколько символов в seo статье, что такое geo в seo  

**SEO-стратегия (до получения Wordstat):** primary «как писать seo статьи» в H1/lead; secondary «seo текст для блога» и «geo оптимизация статьи» — в H2 и FAQ; LSI распределять по «островам смысла» (каждый H2 = самодостаточный блок).

*Смежный спрос (из research B04, 11.06.2026, MCP был доступен): «geo оптимизация контента» — 29 показов/мес; «geo оптимизация» — 981. Использовать только как контекст вторичного кластера, не смешивать с primary.*

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Нормальный порядок работы: спрос и задача страницы → текст для человека → SEO-доработка (не «N ключей → N знаков») | [Hardkod — SEO-статья 2026](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | 2026 | да |
| Заголовки H2/H3 должны отвечать на реальные вопросы, а не существовать ради ключа | [Hardkod — SEO-статья 2026](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | 2026 | да |
| Фразы из Вордстата группируют в 3–5 смысловых кластеров перед структурой | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| После каждого H2 — сразу содержательный ответ (answer-first) | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| Главный ключ — в H1, первом абзаце, 1–2 H2, title и description; LSI — естественно по тексту | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| SEO-статья 2026 — страница, закрывающая задачу пользователя (интент, структура, экспертность, поведение), а не «текст под ключи» | [OlegWeb — алгоритм SEO-статьи](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Для проверки спроса используют Яндекс Вордстат (показы, похожие запросы) | [OlegWeb — алгоритм SEO-статьи](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Google рекомендует JSON-LD как формат structured data; важнее полнота recommended properties, чем их количество | [Google Search Central — Structured Data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) | актуально на 2026 | да |
| AEO — удобство материала для прямого ответа; GEO — цитируемость бренда в генеративных ответах (шире контент + краулеры + упоминания) | [Impact DL — GEO 2026](https://impact-dl.ru/geo-otvety-ii-2026-chto-pomogaet-popast-v-citatu/) | 2026 | да |
| Продавать GEO только через «FAQ + Schema = нейроответ» в 2026 — некорректно; нужны ясный ответ, факты, доступ краулеров, свежесть | [Impact DL — GEO 2026](https://impact-dl.ru/geo-otvety-ii-2026-chto-pomogaet-popast-v-citatu/) | 2026 | да |
| Форматирование Q&A само по себе не улучшает «citation absorption» в AI-ответах; важны определения, цифры, сравнения, пошаговые процедуры | [arxiv 2604.25707 — GEO measurement](https://doi.org/10.48550/arxiv.2604.25707) | 2026 | да |
| Высоковлиятельные для AI страницы — модульные, с extractable evidence (definitions, numbers, comparisons, steps) | [arxiv 2604.25707 — GEO measurement](https://doi.org/10.48550/arxiv.2604.25707) | 2026 | да |

**Не использовать:** непроверенные «+140% трафика» (агентские кейсы); «микроразметка ×1,5–2 цитирование» без первичника; проценты из SEO-дашбордов без methodology page.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Единый workflow: интент → семантика → структура → черновик → мета → FAQ/schema → GEO-чанки → чеклист.

**Почему отличается от конкурентов:**
- Яндекс — канон SEO без GEO-практики для блога.
- GEO-гайды — не учат писать текст с нуля.
- Агентские longread — перегружены кейсами и CTA.
- H1 «которые читают люди» — фокус на **читабельность как SEO+GEO-сигнал** (острова смысла, answer-first, без воды).

**Режим B:** статья B01 — **эталон формата**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как (JSON-LD вне body)  
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи (40–60 слов) | Lead после H1 | «SEO-статья — …» |
| Определение GEO (40–60 слов) | Блок «SEO + GEO» | «GEO — …» |
| Conversational H2 | FAQ-зона | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, action |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA | Блок понятен без соседних |
| Schema handoff | meta / jsonld | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Что это и зачем блогу |
| internal link | Из карточки | `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.  
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — на странице; не дублировать дословно.  
5. **Какие schema для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.  
6. **Что такое llms.txt?** — файл-подсказка для AI-краулеров; дополнение к sitemap, не замена.  
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски и blockers для writer

- Не выдумывать Wordstat-частоты (MCP недоступен в этом прогоне).
- Не копировать структуру 1PS/Pikapuka 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Без эмодзи, без VPN/обход блокировок.
- Цифры только из таблицы фактов §3.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за один проход соберёт семантику в Вордстате, построит структуру longread с answer-first блоками, напишет черновик для людей, настроит Title/Description/H1, добавит FAQ и JSON-LD (BlogPosting + FAQPage), упакует материал под GEO (острова смысла, llms.txt) и пройдёт финальный чеклист перед публикацией.

**action_outline (для writer):**

1. **Проверить интент и SERP:** вбить primary query в поиск, зафиксировать тип страниц в топ-5 и обязательные подтемы (таблица конкурентов).
2. **Собрать семантику:** primary + 15–25 LSI в Вордстате/подсказках; сгруппировать в 3–5 кластеров → будущие H2.
3. **Собрать каркас:** H1 (один), H2 по кластерам, H3 при необходимости; после каждого H2 — тезис-ответ в первом абзаце.
4. **Написать черновик для человека:** короткие абзацы (3–5 строк), списки/таблицы, без переспама ключей; ИИ — только черновик с обязательной ручной правкой.
5. **Техоптимизация:** Title (~65 знаков, ≠ H1), Description, alt изображений, внутренние ссылки на `/` и смежные материалы.
6. **FAQ + schema:** 5–7 пар вопрос–ответ; BlogPosting + FAQPage в JSON-LD (не дублировать разметку в body ради «галочки»).
7. **GEO-слой:** определения SEO/GEO в lead; атомарные H2; упоминание llms.txt и доступа AI-краулеров; island test каждого блока.
8. **Финальный чеклист:** семантика закрыта, мета заполнены, schema валидна, ссылки проверены, объём 8,5–9,5k, текст читается без контекста соседних разделов.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (6) |
| Wordstat MCP | ⚠️ недоступен (LSI из SERP) |
| Таблица фактов с URL | ✅ (18 фактов) |
| utility_verdict + action_outline | ✅ |
| GEO hooks | ✅ |
| FAQ 5–7 | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
