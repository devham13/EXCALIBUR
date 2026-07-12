# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**search_intent:** how_to  
**primary_query:** как писать seo статьи  
**research_date:** 2026-07-12  
**disclaimer:** Все даты, версии и статистика проверены на 12.07.2026 (2026 год).

---

## Utility gate (research)

**utility_verdict:** PASS  

**reader_outcome:** После прочтения читатель сможет самостоятельно написать и опубликовать SEO-статью для блога: собрать семантику в Вордстат, собрать структуру H1–H3 с lead-абзацами, написать текст без переспама, добавить FAQ/schema и пройти финальный чеклист перед публикацией (включая GEO-слой для нейропоиска).

**action_outline:**

1. Проверить интент запроса и тип статьи (информационный how-to vs коммерческий лендинг) по топ-5 SERP.
2. Собрать семантику: primary query + 5–10 вторичных и LSI-фраз в Яндекс Вордстат и подсказках Поиска; сгруппировать в 3–5 смысловых кластеров.
3. Разобрать конкурентов: какие H2 закрывают выдачу, где пробел (GEO, чеклист, FAQ, «для людей»).
4. Собрать каркас: H1 (один), H2 = подзадачи, lead 40–60 слов после каждого H2 с прямым ответом.
5. Написать черновик «сначала смысл»: абзацы 3–5 строк, списки, таблицы; ключи естественно в H1, первом абзаце, 1–2 H2, Title/Description.
6. Добавить E-E-A-T lite: автор, примеры, ссылки на первичные источники (Яндекс Директ, Вебмастер).
7. Упаковать для GEO: атомарные «острова смысла», FAQ 5–7 пар, BlogPosting + FAQPage (JSON-LD вне body).
8. Заполнить Title, Description, alt, URL, внутренние ссылки (3–5).
9. Пройти чеклист перед публикацией: семантика, мета, структура, уникальность, island test, schema.

---

## 1. Яндекс Вордстат (спрос и LSI)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в текущей cloud-среде (сервер не подключён). Вызов `wordstat_get_top_requests` для `как писать seo статьи`, `seo текст для блога`, `geo оптимизация статьи` выполнить не удалось. **Точные объёмы показов в месяц не получены.** Обновите токен и подключение MCP через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

| Фраза | Показы в месяц |
|-------|----------------|
| как писать seo статьи | *не получено — MCP недоступен* |
| seo текст для блога | *не получено — MCP недоступен* |
| geo оптимизация статьи | *не получено — MCP недоступен* |

**LSI-ключи для writer (из SERP WebSearch + research-serp.json, без выдуманных частот):**

| Кластер | LSI / смежные запросы |
|---------|------------------------|
| Написание | как написать seo статью, seo текст для сайта, seo копирайтинг, оптимизированная статья |
| Семантика | семантическое ядро, яндекс вордстат, lsi ключи, ключевые слова без переспама, поисковый интент |
| Структура | структура seo статьи, заголовки h1 h2 h3, title description, мета-теги, абзацы и списки |
| Качество | e-e-a-t, полезный контент, уникальность текста, переспам ключей, читабельность |
| GEO / AI | geo оптимизация, generative engine optimization, ai seo 2026, faq schema, llms.txt, нейропоиск |

**Рекомендация writer:** primary «как писать seo статьи» — в H1, lead, Title; secondary «seo текст для блога» — в блоке про формат longread; «geo оптимизация статьи» — отдельный подблок в H2 «SEO + GEO в одной статье».

---

## 2. SERP-обзор (WebSearch, июль 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|-----------------|------------------|---------------|
| 1 | [direct.yandex.ru/.../seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: Вордстат, H1–H4, переспам, Title/Description, alt, 4 шага workflow | Нет GEO; CTA Директа | Коммерческий блок Директа |
| 2 | [1ps.ru/.../seo-tekstyi-2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Краткая инструкция в начале; Wordstat; H2 = кластеры; «сначала смысл, потом ключи» | Длинный sales-narrative про ИИ | Дублировать структуру 1:1 |
| 3 | [olegweb.ru/.../kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый WP-гайд (13 шагов) | Интент → конкуренты → структура → Title/H1 таблица → чеклист | Перегруз шагами без GEO-слоя | 13 H2 «шаг за шагом» без группировки |
| 4 | [iconsult.agency/.../polniy-seo-cheklist-dlya-bloga](https://iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga-kak-pisat-stati-kotorye-privodyat-trafik/) | Чеклист 31 пункт | Фазы Research → Content → Optimization; AI Overviews | Англоязычный SERP-фокус | Копировать все 31 пункт в одну статью |
| 5 | [habr.com/.../1030292](https://habr.com/ru/articles/1030292/) | GEO/AEO field guide (2026) | SEO vs GEO; RAG; 40/35/25 распределение усилий; citations | Не учит писать текст с нуля | Непроверенные «−20–40% органики» без первичника в тексте |
| 6 | [gracie.digital/.../kontent-kotoryj-chitayut-lyudi](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | AI SEO + GEO (июнь 2026) | Answer-first 40–60 слов; факты каждые 150–200 слов | Узкий бренд-кейс | Цифры без URL в body |

**Паттерн SERP (июль 2026):** топ — «полный гайд 2026» с Wordstat, E-E-A-T, чек-листом; растёт кластер GEO/AI SEO. H1 «которые читают люди» в топе почти не встречается — дифференциатор Excalibur.

**Intent:** how_to — пошаговая система от семантики до публикации. Вторичный: связка SEO + GEO в одном материале для блога.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение → основная часть по шагам → заключение с next step | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Контент должен быть полезен людям в первую очередь, не роботам | [Яндекс Директ — SEO услуги](https://direct.yandex.ru/base/articles/seo-prodvizhenie-sajta-uslug) | 2026 | да |
| Черновик: раскрыть тему, ответить на вопросы, ключи в естественном контексте | [Яндекс Директ — SEO-копирайтинг](https://direct.yandex.ru/base/articles/chto-takoe-seo-kopirayting-i-kak-napisat-seo-tekst) | 2026 | да |
| H1 ≠ Title: Title для сниппета, H1 — на странице | [olegweb.ru — SEO-статья](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 2026 | да |
| После каждого H2 — содержательный ответ; сначала смысл, потом семантика | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Прямой ответ в первых 40–60 словах блока — зона извлечения для AI | [gracie.digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| GEO — надстройка над SEO, не замена; без индекса RAG не найдёт контент | [Хабр — GEO/AIO/AEO](https://habr.com/ru/articles/1030292/) | 2026 | да |
| Распределение усилий 2026 (экспертная оценка автора Habr): ~40% тех. SEO, ~35% GEO-контент, ~25% авторитет | [Хабр — GEO/AIO/AEO](https://habr.com/ru/articles/1030292/) | 2026 | да* |
| Princeton GEO: цитирование источников, статистика, цитаты экспертов повышают AI-видимость на 30–40% | [digitalapplied.com — GEO Guide 2026](https://www.digitalapplied.com/blog/geo-guide-generative-engine-optimization-2026) | 2026 | да* |
| Schema FAQPage + Article/HowTo помогает AI классифицировать контент | [Storyblok — GEO Explained](https://www.storyblok.com/mp/generative-engine-optimization-explained) | 2026 | да |
| Главная задача статьи — полный ответ; возврат в поиск = сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

\* Вторичный источник или экспертная оценка — в тексте формулировать осторожно («по данным исследований», «эксперты рекомендуют»), без точных % без arxiv/первичника.

**Не использовать:** «−20–40% органики» (Habr TL;DR без первичника); «Schema +30% CTR» (t-v.te.ua без источника); «+140% трафика» (агентские кейсы).

**fact-bank.md:** прямых фактов по SEO-написанию нет; опираемся на таблицу выше (Яндекс Директ — приоритет).

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Единый workflow: интент → семантика (Вордстат) → структура → инфостиль → FAQ/schema → GEO-чанки → чеклист.

**Отличие от конкурентов:**

- Яндекс — канон без GEO; GEO-гайды не учат писать с нуля.
- Агентские гайды — 13–31 шаг без группировки или перегруз ИИ/кейсами.
- H1 «которые читают люди» слабо раскрыт в SERP: наш фокус — **читабельность как SEO-фактор** + техника.

**Режим B:** статья B01 — этalon: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (из карточки):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как  
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead после H1 | 40–60 слов |
| Определение GEO | H2 «SEO + GEO» | 40–60 слов |
| Conversational H2 | «Что такое GEO в SEO?», «Сколько символов…» | Вопрос в заголовке |
| FAQ 5–7 | Конец | 2–4 предложения на ответ |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema | Вне body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Кратко: зачем блогу |
| Внутренняя ссылка | Из карточки | На `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + тематические слова (Яндекс Директ).
4. **Чем Title отличается от H1?** — Title для сниппета, H1 на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt и нужен ли он блогу?** — сигнал для AI-краулеров; не замена sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, island test.

---

## 7. Риски для writer

- Цифры спроса Вордстат — не выдумывать (MCP недоступен).
- Не копировать Pikapuka/olegweb 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Без эмодзи; site_url — плейсхолдер `/` по карточке.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate topic | ✅ PASS |
| utility_verdict + action_outline | ✅ |
| SERP ≥ 5 конкурентов (WebSearch) | ✅ |
| Таблица фактов с URL (17+) | ✅ |
| Wordstat MCP | ⚠️ недоступен |
| GEO hooks + FAQ | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
