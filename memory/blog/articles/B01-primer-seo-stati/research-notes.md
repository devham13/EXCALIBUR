# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-08-07  
**disclaimer:** Все даты, версии и статистика проверены на 07.08.2026.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 7 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Авторитет; workflow тема → семантика → структура → текст → оптимизация; примеры «плохо/хорошо»; Wordstat, alt, мета, перелинковка | Нет GEO/нейропоиска; CTA Директа в конце | Блок про Директ; дублировать H1–H4 без GEO-слоя |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм (обнов. 05.02.2026) | 13 шагов от спроса до публикации в WordPress; таблица «что у конкурента / что сделать вам»; акцент на интент и поведение | Узкий фокус WP; мало GEO | Копировать 13 шагов 1:1 без сжатия |
| 3 | [tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | Формула 2026 | E-E-A-T-блок, форматы FAQ/гайд/сравнение/кейс; lead с прямым ответом | Коммерческий tone; без чек-листа публикации | Agency-CTA как основной вывод |
| 4 | [seojazz.ru/blog/tekstovaja-optimizacija-v-2026-godu](https://seojazz.ru/blog/tekstovaja-optimizacija-v-2026-godu-rabota-s-kontentom-dlja-uluchshenija-relevantnosti-i-relevantnye-tegi/) | AIO + GEO + E-E-A-T (2026) | Формулы Title/Description; answer-first для AI; GEO как дополнение SEO | Перегруз тегами; мало «с нуля для блога» | Keyword-наборы «купить/цена/лучший» без контекста |
| 5 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (май 2026) | Wordstat, Serpstat, чек-лист 10 шагов, Schema Article + FAQPage, Title ~65 знаков | Кейс «+140% трафика» без источника; agency-bias | Непроверенные проценты; 7-разделная структура 1:1 |
| 6 | [seo-vladimir.ru/blog/lsi-copywriting-seo-2026](https://seo-vladimir.ru/blog/lsi-copywriting-seo-2026/) | SEO-копирайтинг без мифов LSI | Покрытие интента, сущности, H1–H3, списки/таблицы, FAQ; лимит ключей | Мало про GEO и schema | Термин «LSI» как главный hook |
| 7 | [ddsi.ru/blog/kak-napisat-seo-tekst-polnoe-rukovodstvo-dlya-nachinayushhih](https://ddsi.ru/blog/kak-napisat-seo-tekst-polnoe-rukovodstvo-dlya-nachinayushhih/) | Пошаговый гайд для начинающих | 6 шагов с чек-листом, мета Title/Description, URL, перелинковка | Дата в title «2025»; поверхностный GEO | Устаревший year-tag в URL/title |

**Паттерн SERP (август 2026):** топ — «полный гайд 2026» с E-E-A-T, Wordstat, чек-листом и блоком про AI-ответы. Отдельный кластер — GEO/AIO-лонгриды (seojazz, trigub). Прямого совпадения с H1 «которые читают люди» в топе почти нет — пробел для дифференциации через **читабельность как SEO-фактор**.

**Intent:** how_to — пользователь хочет пошаговую систему: семантика → структура → текст → техника → проверка. Вторичный intent: связка SEO + GEO в одном материале для блога.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, регион 225, 07.08.2026)

⚠️ **WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` недоступен в Cloud-среде (MCP не сконфигурирован). Вызов `wordstat_get_top_requests` для «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи» не выполнен. **Точные объёмы спроса не получены — цифры ниже не приводятся.** Обновите MCP и токен Wordstat: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса

| Фраза | Показы/мес |
|-------|------------|
| как писать seo статьи | *не получено (MCP недоступен)* |
| seo текст для блога | *не получено* |
| geo оптимизация статьи | *не получено* |

### LSI для writer (из SERP + secondary_queries, без Wordstat)

- как писать seo статьи, seo текст для блога, seo статья для сайта, как написать seo статью  
- семантическое ядро, яндекс wordstat, сбор ключевых слов, тематические слова  
- структура longread, H1 H2 H3, title description, meta-теги, alt-тексты  
- E-E-A-T, интент запроса, переспам ключей, чек-лист перед публикацией  
- geo оптимизация статьи, generative engine optimization, FAQ schema, BlogPosting  
- сколько символов в seo статье, что такое geo в seo  
- внутренняя перелинковка, featured snippet, AI-ответы, llms.txt  

**SEO-стратегия (экспертная, без частот):** primary «как писать seo статьи» в H1/lead; secondary «seo текст для блога» и «geo оптимизация статьи» — в H2 и FAQ; вопросные формулировки из faq_hints — в FAQ-блок.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение → основная часть по шагам → заключение с следующим шагом для читателя | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья 2026 — страница, которая решает задачу пользователя (выбрать, настроить, сделать), а не «текст под ключи» | [olegweb.ru — алгоритм SEO-статьи](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Проверка спроса перед написанием — через Яндекс Вордстат (показы, похожие запросы) | [olegweb.ru — алгоритм SEO-статьи](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Title: ориентир 50–60 знаков; Description: 140–180 символов с естественным ключом | [seojazz.ru — текстовая оптимизация 2026](https://seojazz.ru/blog/tekstovaja-optimizacija-v-2026-godu-rabota-s-kontentom-dlja-uluchshenija-relevantnosti-i-relevantnye-tegi/) | 2026 | да |
| H2–H3: вопросные формулировки и LSI; для AIO — явные вопросы «Как…», «Сколько…» | [seojazz.ru — текстовая оптимизация 2026](https://seojazz.ru/blog/tekstovaja-optimizacija-v-2026-godu-rabota-s-kontentom-dlja-uluchshenija-relevantnosti-i-relevantnye-tegi/) | 2026 | да |
| Ключевое слово — не более 3–4 раз на 1000 знаков; остальное — синонимы и тематические слова | [seo-vladimir.ru — LSI-копирайтинг 2026](https://seo-vladimir.ru/blog/lsi-copywriting-seo-2026/) | 2026 | да |
| Title ~60–70 символов, Description ~150–160 символов; URL короткий и понятный | [ddsi.ru — SEO-текст для начинающих](https://ddsi.ru/blog/kak-napisat-seo-tekst-polnoe-rukovodstvo-dlya-nachinayushhih/) | 2025–2026 | да |
| H1 — с основным запросом и пользой; H2/H3 — подтемы и уточняющие вопросы | [ddsi.ru — SEO-текст для начинающих](https://ddsi.ru/blog/kak-napisat-seo-tekst-polnoe-rukovodstvo-dlya-nachinayushhih/) | 2025–2026 | да |
| Title ~65 знаков, с ключом и триггером (чек-лист, инструкция); H1 ≠ Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Schema.org: Article + FAQPage для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| GEO (Generative Engine Optimization) — оптимизация для цитирования в ответах AI, не замена SEO | [trigub.ru — GEO 2026](https://trigub.ru/geo-v-2026-godu/) | 2026 | да |
| Нейросети извлекают пассажи (passages) — каждый H2 = «остров смысла» с прямым ответом в начале | [mayai.ru — GEO чек-лист](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да |
| FAQ: 5–7 вопросов, ответ до ~80 слов; JSON-LD FAQPage | [mayai.ru — GEO чек-лист](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да |
| Основной запрос — в Title, H1, первом экране; дополнительные — естественно по тексту | [exlibris.ru — формула SEO-текста](https://exlibris.ru/academy/formula-seo-teksta-kak-vyvesti-blog-v-top-vydachi/) | 2026 | да |
| Главная задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [maryproject.ru — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**fact-bank.md:** прямых фактов по SEO-writing нет — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); «Princeton +30–40%» без arxiv в контексте написания текста; любые показы Wordstat без MCP.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды перегружены E-E-A-T-кейсами и CTA.
- H1 «которые читают люди» — слабо раскрыт в SERP; фокус: **читабельность как SEO-фактор** (структура, короткие абзацы, «острова смысла») + техника.

**Режим B:** сама статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (один контент, две цели)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

**Tone:** практично, по-человечески; без корпоративной воды и эмодзи (site-brief).

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-темы | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец longread | Ответ 2–4 предложения |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA для writer | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Что это и зачем для блога |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и конкуренты в SERP; для how-to longread — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом контенте.
3. **Нужно ли переспамить ключевые слова в 2026 году?** — нет; естественные вхождения + тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (~50–65 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt и нужен ли он блогу?** — файл для AI-краулеров; полезный сигнал, не замена sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски и blockers для writer

- Не выдумывать статистику и показы Wordstat.
- Не копировать структуру Pikapuka/olegweb 1:1.
- Объём: 8 500–9 500 знаков (quality-blog.md).
- Без эмодзи, без VPN/обход блокировок.
- Internal link: `/` по карточке.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику в Wordstat, построит структуру longread под интент, напишет текст с E-E-A-T и GEO-чанками, оформит Title/Description/FAQ/schema и пройдёт чеклист перед публикацией — получив SEO-статью, которую дочитывают люди и которую могут процитировать нейропоиски.

**action_outline:**

1. **Определить интент и спрос:** открыть топ-10 по primary query; зафиксировать формат (гайд/чек-лист); проверить фразы в Wordstat и подсказках.
2. **Собрать семантику:** primary + 5–10 secondary/LSI; один кластер на статью; выписать вопросы для FAQ.
3. **Собрать структуру:** H1 с пользой; H2–H3 по подзадачам; lead с прямым ответом; таблица или список там, где сравнение/шаги.
4. **Написать черновик «для людей»:** абзацы 3–5 строк; ключи естественно; без переспама; примеры и рекомендации «делать / не делать» в каждом H2.
5. **Добавить GEO-слой:** определения в первых абзацах H2; FAQ 5–7 с короткими ответами; упоминание llms.txt при необходимости.
6. **Техническая упаковка:** Title (50–65 зн.), Description (140–180 зн.), alt, внутренние ссылки 2–3, JSON-LD BlogPosting + FAQPage.
7. **Чеклист перед публикацией:** семантика закрыта, мета заполнены, schema валидна, нет воды и выдуманных цифр, текст проходит «island test».
8. **Публикация и контроль:** даты datePublished/dateModified; после выхода — проверка индексации и поведения; план обновления раз в квартал.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (7) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| Режим B описан | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
