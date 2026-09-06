# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**search_intent:** how_to  
**research_date:** 2026-09-06  
**disclaimer:** Все даты, версии и статистика проверены на 06.09.2026.

---

## Utility gate (research)

**utility_verdict:** PASS  

**reader_outcome:** После прочтения гайда читатель сможет самостоятельно собрать и опубликовать SEO+GEO longread по своей теме — от сбора семантики и структуры до FAQ/schema и финального чеклиста перед публикацией.

**action_outline (workflow для writer):**

1. Определить интент запроса и собрать семантический кластер (основной + 5–20 вторичных) через Wordstat и анализ выдачи.
2. Разобрать ТОП-10 конкурентов: формат, объём, повторяющиеся H2, пробелы.
3. Составить каркас H1 → H2 → H3: lead-ответ, блоки «объяснение → таблица → ошибки → чеклист».
4. Написать текст: короткий ответ в первых 40–70 словах, атомарные абзацы 150–190 слов, списки и таблицы.
5. Добавить GEO-слой: BLUF в каждом H2, FAQ 5–7 пар, цитируемые определения с источниками.
6. Подготовить Title (~65 знаков), Description, alt, внутренние ссылки; вынести BlogPosting + FAQPage в JSON-LD.
7. Пройти чеклист перед публикацией (семантика, мета, читабельность, schema, robots для AI-краулеров).

---

## 1. Яндекс Wordstat (спрос и LSI)

> ⚠️ **WORDSTAT MCP WARNING:** MCP-сервер `user-mcp-kv` недоступен в текущей Cloud-среде (namespace не подключён). Вызов `wordstat_get_top_requests` выполнить не удалось — **точные показы в месяц не получены**.  
> Для восстановления API: обновите OAuth-токен через [авторизацию Яндекс OAuth](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40) и проверьте MCP `user-mcp-kv` в настройках среды.

### Запросы для повторного прогона Wordstat (writer/QA)

| ID | Фраза | Назначение |
|----|-------|------------|
| primary | как писать seo статьи | главный ключ карточки B01 |
| secondary_1 | seo текст для блога | вторичный из карточки |
| secondary_2 | geo оптимизация статьи | GEO-кластер |
| lsi_1 | как написать seo статью | вариация формулировки |
| lsi_2 | seo копирайтинг 2026 | коммерческо-информационный хвост |
| lsi_3 | структура seo статьи | структурный intent |
| lsi_4 | тз для seo копирайтера | смежный workflow-intent |
| lsi_5 | чеклист seo текста | checklist-intent |

### LSI-кластер (экспертная семантика по SERP, без оценки частотности)

**Ядро (primary):** как писать seo статьи · seo текст · seo статья · seo копирайтинг · оптимизированная статья  

**Структура и процесс:** структура seo статьи · пошаговый гайд · техническое задание копирайтеру · семантическое ядро · кластеризация запросов · анализ конкурентов топ 10  

**On-page:** title description · h1 h2 h3 · lsi фразы · перелинковка · уникальность текста · alt изображений  

**GEO/AEO 2026:** geo оптимизация статьи · generative engine optimization · answer-first · bluf · чанкинг · faqpage schema · ai overviews · нейропоиск  

**FAQ-хвосты (из карточки B01):** сколько символов в seo статье · что такое geo в seo  

*Таблица «Фраза | Показы в месяц» будет заполнена после восстановления Wordstat MCP.*

---

## 2. SERP-обзор (WebSearch, 06.09.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|-----------------|------------------|---------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон SEO: семантика через Wordstat, H1–H4, естественность ключей, примеры «плохо/хорошо», мета и перелинковка | Нет GEO/нейропоиска; коммерческий CTA Директа | CTA Директа; «универсальный объём» без workflow |
| 2 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Пошаговый гайд (июль 2026) | 7 шагов от семантики до контроля после публикации; Wordstat; медиана объёма из ТОПа; чек-лист | GEO только косвенно; продвижение инструментов школы | Копировать 7 шагов 1:1 без GEO-слоя |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Кластеризация Wordstat, H2 с немедленным ответом, LSI без спама | Фокус на ИИ-генерации; длинный sales-narrative | Блоки про «полностью на ИИ» без human-in-the-loop |
| 4 | [roiseo.ru/blog/struktura-seo-stati-dlya-bloga](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон структуры (апр. 2026) | Lead 40–70 слов, таблица блоков, чек-лист, FAQ+schema, AI-citable формат | Мало про сбор семантики с нуля | Сухой шаблон без единого workflow SEO+GEO |
| 5 | [geo-course.ru/blog/kak-pisat-kontent-dlya-nejrosetej](https://geo-course.ru/blog/kak-pisat-kontent-dlya-nejrosetej/) | GEO-гайд (июнь 2026) | BLUF, чанкинг 150–190 слов, «золотой параграф», практические ДО/ПОСЛЕ | Часть цифр — вторичные (Wellows и др.) | Непроверенные мультипликаторы «×4,8» без первичника |
| 6 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский чек-лист 2026 | E-E-A-T, Schema Article+FAQPage, Title ~65 знаков | Непроверенные кейсы «+140%»; agency-CTA | Выдуманные проценты в кейсах |
| 7 | [habr.com/ru/articles/1042732](https://habr.com/ru/articles/1042732/) | GEO/AEO на Habr (2026) | Answer-First, различия нейросетей, TL;DR/FAQ | Не учит писать SEO-текст с нуля | Длинный обзор без пошагового чеклиста для новичка |

**Паттерн SERP:** два кластера — классические «как писать SEO-текст/статью 2026» (7 шагов, Wordstat, структура) и GEO/AEO-лонгриды (BLUF, чанки, schema). Прямого совпадения с H1 «которые читают люди» в топе мало — это наш дифференциатор.

**Intent:** how_to — пользователь хочет воспроизводимый workflow: семантика → структура → текст → мета → GEO → проверка. Вторичный intent: понять связку SEO + GEO в одном материале.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — он зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-текст в 2026 — полезный текст со структурой и словарём темы, а не «ключи через каждые два абзаца» | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| Рабочий цикл: 7 шагов — семантика → ТОП → структура → текст → Title/Description → релевантность → контроль после публикации | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| Ориентир объёма — медиана конкурентов в ТОПе, не абстрактная «норма в знаках» | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| Lead-ответ на первом экране — 40–70 слов | [ROI SEO — структура статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 22.04.2026 | да |
| Шаблон longread: lead → объяснение → таблица → пример → ошибки → чек-лист → FAQ | [ROI SEO — структура статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 22.04.2026 | да |
| FAQPage schema должна совпадать с видимым FAQ в HTML | [ROI SEO — структура статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 22.04.2026 | да |
| BLUF: главный ответ в первых ~200 словах; нейросети сканируют начало с повышенным весом | [GEO Course — BLUF и чанкинг](https://geo-course.ru/blog/kak-pisat-kontent-dlya-nejrosetej/) | 22.06.2026 | да |
| Целевой размер GEO-чанка — ~150–190 слов (покрывает Google AI Mode, Яндекс AI, Perplexity, ChatGPT RAG) | [GEO Course — BLUF и чанкинг](https://geo-course.ru/blog/kak-pisat-kontent-dlya-nejrosetej/) | 22.06.2026 | да |
| GEO-bench — 10 000 запросов; методы с цитатами, статистикой и quotations повышают visibility до 40% в generative answers | [Aggarwal et al., arXiv:2311.09735](https://arxiv.org/abs/2311.09735) | KDD 2024 | да |
| Keyword stuffing в эксперименте GEO хуже baseline | [Aggarwal et al., arXiv:2311.09735](https://arxiv.org/abs/2311.09735) | KDD 2024 | да |
| На live Perplexity.ai visibility improvements до 37% (тот же paper) | [Aggarwal et al., arXiv:2311.09735](https://arxiv.org/abs/2311.09735) | KDD 2024 | да |
| Title — ориентир ~65 знаков, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| H1 не дублирует Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «entity density ×4,8» (GEO Course / Wellows без первичника); «listicle 43,8% AI-цитирований» без первичника; любые показы Wordstat без API.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды перегружены E-E-A-T-кейсами и CTA.
- H1 «которые читают люди» слабо раскрыт в SERP — наш фокус: **читабельность как SEO-фактор** (lead, атомарные блоки, island test) + техника.

**Режим B:** статья B01 — эталон формата: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи (40–60 слов) | Lead после H1 | «SEO-статья — …» |
| Определение GEO (40–60 слов) | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-блоки | «Что такое GEO в SEO?», «Сколько символов…?» |
| FAQ 5–7 пар | Конец longread | 2–4 предложения, action-ответ |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; абзац 150–190 слов |
| Island test | QA | Блок понятен без соседних |
| Schema handoff | cover/schema agents | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Кратко: зачем блогу |
| Внутренняя ссылка | Из карточки | На `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и медиана ТОПа; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при сохранении индексируемого структурированного контента.
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt?** — Markdown-карта для AI-краулеров; дополнение к sitemap, не замена.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать статистику Wordstat и SERP.
- Не копировать структуру Pikapuka / SEO Школы 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Без эмодзи; site_url — `/` по карточке.
- Цифры GEO — только из arXiv:2311.09735 с пояснением «visibility в AI-ответе», не «+40% трафика».

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| utility_verdict PASS | ✅ |
| action_outline 5–9 шагов | ✅ (7) |
| reader_outcome | ✅ |
| SERP ≥ 3 конкурента | ✅ (7) |
| Таблица фактов с URL | ✅ (17) |
| Wordstat (MCP) | ⚠️ MCP недоступен — LSI из SERP |
| GEO hooks + FAQ | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
