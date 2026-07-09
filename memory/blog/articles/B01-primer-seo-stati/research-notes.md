# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата)  
**search_intent:** how_to  
**research_date:** 2026-07-09  
**disclaimer:** Все даты, версии и статистика проверены на 2026-07-09 (2026 год).

---

## Utility gate

| Проверка | Результат |
|----------|-----------|
| `excalibur_blog_utility_gate.py --topic-id B01` | **PASS** |
| `search_intent` | how_to |
| `article_mode` | B |

**utility_verdict:** PASS

**reader_outcome:** После прочтения читатель сможет самостоятельно пройти полный цикл создания SEO+GEO longread — от сбора семантики и answer-first структуры до мета, schema, финального чеклиста и отправки URL на индексацию.

**action_outline (workflow для writer):**

1. **Интент и семантика** — primary query «как писать seo статьи» + 10–15 подвопросов из SERP/Вордстата; классифицировать информационный vs коммерческий интент.
2. **Каркас** — H1 (главный запрос) → lead 40–60 слов с прямым ответом → H2 по подвопросам → FAQ в конце.
3. **Answer-first черновик** — под каждым H2 первые 2–3 предложения = самодостаточный ответ; абзацы 3–5 строк, списки и минимум одна таблица.
4. **Семантика без переспама** — primary в H1, первом абзаце, Title; LSI равномерно по тексту; не вставлять неестественные фразы.
5. **Читабельность + E-E-A-T lite** — автор/редакция, примеры, ссылки на источники; блок «SEO + GEO в одной статье» с определениями.
6. **Техника** — Title (~65 знаков, ≠ H1), Description, alt у изображений, внутренняя перелинковка на `/`.
7. **GEO-слой** — FAQ 5–7 пар, BlogPosting + FAQPage (JSON-LD вне body); упомянуть llms.txt как опциональный сигнал, не замену sitemap.
8. **Чеклист перед публикацией** — 15+ пунктов: семантика, мета, schema, CWV, индексация в Вебмастер/GSC.

---

## 1. Анализ спроса — Яндекс Вордстат

⚠️ **WORDSTAT MCP WARNING:** MCP-сервер `user-mcp-kv` недоступен в Cloud-окружении (вызов `wordstat_get_top_requests` невозможен). **Точные объёмы показов в месяц из API не получены.** Для восстановления доступа обновите токен через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (Яндекс Вордстат)

| Фраза | Показы в месяц | Примечание |
|-------|----------------|------------|
| как писать seo статьи | *не получено из API* | primary_query B01 |
| seo текст для блога | *не получено из API* | secondary_query |
| geo оптимизация статьи | *не получено из API* | secondary_query |
| как написать seo статью | *не получено из API* | вариант формулировки из SERP |
| seo текст для сайта | *не получено из API* | LSI из конкурентов |
| структура seo статьи | *не получено из API* | LSI |
| seo копирайтинг 2026 | *не получено из API* | LSI |
| семантическое ядро для статьи | *не получено из API* | LSI |
| e-e-a-t seo текст | *не получено из API* | LSI |
| title description seo | *не получено из API* | LSI |
| сколько символов в seo статье | *не получено из API* | FAQ-hint из карточки B01 |

### LSI-ключи для копирайтера (экспертная семантика по SERP WebSearch + research-serp.json, **без объёмов**)

- как писать seo тексты / seo-тексты 2026
- seo текст для блога / для сайта
- как написать seo статью пошагово
- структура seo статьи (H1, H2, H3)
- семантическое ядро, LSI-фразы, Wordstat
- seo копирайтинг, интент запроса
- title и description для статьи
- e-e-a-t / экспертность автора
- geo оптимизация статьи, нейропоиск, AI Overviews
- schema.org BlogPosting FAQPage HowTo
- llms.txt для блога
- answer-first / прямой ответ в первых 40–60 словах
- чеклист перед публикацией seo статьи
- core web vitals для блога
- что такое geo в seo (FAQ)

---

## 2. SERP-обзор (WebSearch Cursor, 2026-07-09)

**Запросы:** «как писать seo статьи 2026», «seo текст для блога 2026», «geo оптимизация статьи 2026», H1 из карточки.

| # | URL | Тип | Сильные стороны | Пробелы / не копировать |
|---|-----|-----|-----------------|-------------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон SEO-текста: структура H1–H4, Wordstat, естественность ключей, мета, «плохо/хорошо» | Нет GEO/нейропоиска; CTA Директа |
| 2 | [trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | Практический чеклист GEO (апр. 2026) | Answer-first, кластер 10–15 вопросов, Schema Article/FAQPage, CWV пороги | Часть цифр — авторская аналитика без первичника |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский гайд 2026 | Семантика, E-E-A-T, чек-лист, Title ~65 знаков, Featured Snippet | Непроверенные кейсы «+140%»; agency CTA |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | SEO-агентство 2026 | Пошаговая инструкция: интент → H1/H2 → ответ сразу после заголовка → финальная оптимизация | Длинный sales-narrative |
| 5 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Независимый how-to (фев. 2026) | 13 шагов от спроса до WordPress; интент, конкуренты, таблицы, чеклист | Фокус на WP, без GEO-блока |
| 6 | [gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | SEO+AI (июнь 2026) | «Люди + нейросети»: answer-first 40–60 слов, фактическая насыщенность | Узкий брендовый угол |
| 7 | [shipmint.kz/blog/llms-txt-schema-org-vidimost-dlya-ai-poiska](https://shipmint.kz/blog/llms-txt-schema-org-vidimost-dlya-ai-poiska) | Техразбор GEO (2025–2026) | Цитата Google про llms.txt; приоритет Schema.org | Регион KZ, не RU-фокус |

**Паттерн SERP 07.2026:** доминируют «полный гайд 2026» с чек-листом, E-E-A-T и answer-first. Отдельный кластер — GEO/нейропоиск. H1 «которые читают люди» почти не занят (bestseoserg.com, qvai.ru — слабее по глубине). **Intent:** how_to — пошаговая система «семантика → структура → текст → техника → проверка»; вторичный — связка SEO + GEO в одном материале.

**Дифференциация Excalibur:** единый workflow «для людей и для AI» без agency-воды; режим B — сама статья = эталон longread 8 500–9 500 знаков; акцент на читабельность как SEO/GEO-сигнал (острова смысла, FAQ, schema).

---

## 3. Таблица фактов (18 проверенных утверждений с URL)

| # | Факт | Источник | Дата | В текст |
|---|------|----------|------|---------|
| 1 | Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 2 | H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 3 | Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 4 | Семантику подбирают в Яндекс Вордстат; запросы различаются по намерению пользователя | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 5 | Title и Description влияют на сниппет и кликабельность в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 6 | SEO-текст: абзацы ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 7 | LCP — загрузка: хороший UX при появлении основного контента **в первые 2,5 секунды** | [Google Search Central — Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals) | актуально 2026 | да |
| 8 | INP — отзывчивость: ориентир **менее 200 мс** | [Google Search Central — Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals) | актуально 2026 | да |
| 9 | CLS — стабильность вёрстки: ориентир **менее 0,1** | [Google Search Central — Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals) | актуально 2026 | да |
| 10 | Google рекомендует people-first контент: после прочтения человек должен достичь цели без повторного поиска | [Google — Creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| 11 | E-E-A-T не отдельный «фактор ранжирования», но системы Google используют mix сигналов доверия и экспертизы | [Google — Creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| 12 | SEO может быть полезным, когда применяется к people-first контенту, а не search-engine-first | [Google — Creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| 13 | Первые **100 слов** после H1 — зона готового ответа для нейропоиска (практика чеклиста) | [Тригуб — чеклист для ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 17.04.2026 | да* |
| 14 | Кластер под статью: минимум **10–15** смежных вопросов из SERP/инструментов | [Тригуб — чеклист для ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 17.04.2026 | да |
| 15 | Schema.org для статей: Article + FAQPage; опционально HowTo | [Тригуб — чеклист для ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 17.04.2026 | да |
| 16 | Google (цит. Shipmint): **«We currently have no plans to support LLMs.txt»** — нет отдельного приоритета файла | [Shipmint — llms.txt vs Schema](https://shipmint.kz/blog/llms-txt-schema-org-vidimost-dlya-ai-poiska) | 2025–2026 | да |
| 17 | После каждого H2 — содержательный ответ сразу; H1 = главный запрос, H2 = подтемы кластера | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| 18 | В 2026 недостаточно «ключи + уникальность» — нужны интент, структура, полнота ответа, опыт автора, поведение на странице | [OlegWeb — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |

\* Практическая рекомендация эксперта; в тексте формулировать как методику, не как официальный порог поисковика.

**Не использовать без первичника:** «+140% трафика» (Pikapuka); «до 20% трафика из нейровыдачи» (Тригуб — внутренняя аналитика); «микроразметка ×1,5–2 цитирование» (агентские блоги).

**fact-bank.md:** прямых фактов по SEO-копирайтингу нет; таблица выше — первичный источник для B01.

---

## 4. Угол статьи (только практика)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска (GEO). Не «ещё один список ключей», а **единый workflow** A→B→C: интент → answer-first структура → инфостиль → FAQ/schema → финальный чеклист.

**H2-каркас (из карточки B01 + SERP):**

1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

**Внутри блоков (не обязательно отдельные H2):** Wordstat/семантика, Title/Description, E-E-A-T lite, llms.txt, индексация.

**Tone:** практично, по-человечески; без корпоративной воды и эмодзи (site-brief).

**Режим B:** статья B01 — эталон формата блога: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage.

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead после H1 | 40–60 слов |
| Определение GEO | Блок «SEO + GEO» | 40–60 слов |
| Conversational H2 | FAQ-темы | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, action |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Опциональный ориентир для AI-краулеров |
| Внутренняя ссылка | Из карточки | `/` |

---

## 6. FAQ-кандидаты (7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — дополнение к SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + LSI (Яндекс Директ).
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — на странице; не дублировать.
5. **Какие schema для SEO-статьи блога?** — BlogPosting/Article + FAQPage.
6. **Нужен ли llms.txt блогу?** — опциональный эксперимент; Google не даёт отдельного приоритета (Shipmint/Google quote).
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, CWV, индексация.

---

## 7. Риски для writer

- Цифры только из таблицы фактов §3; не выдумывать объёмы Wordstat.
- Не копировать структуру Pikapuka/1PS 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи; site_url — `/` или example.com по карточке.
- Google May 2026: не строить статью вокруг «GEO-трюков» (llms.txt как must-have, chunking ради AI) — фокус на people-first + структура.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| utility_verdict PASS | ✅ |
| reader_outcome + action_outline | ✅ |
| SERP ≥ 5 конкурентов (WebSearch 07.2026) | ✅ |
| Wordstat (попытка MCP) | ⚠️ API недоступен |
| LSI без выдуманных объёмов | ✅ |
| Факты с URL ≥ 15 | ✅ (18) |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
