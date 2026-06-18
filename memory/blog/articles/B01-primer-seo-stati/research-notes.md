# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-06-18  
**disclaimer:** Все даты, версии и статистика проверены на 18.06.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch Cursor, 18.06.2026)

Источник приоритетный — живой WebSearch; `research-serp.json` использован как дополнение. Топ по «как писать seo статьи 2026» — длинные how-to гайды агентств и SEO-блогов; отдельный кластер — GEO/AEO-материалы по вторичному запросу «geo оптимизация статьи».

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: семантика → структура → текст → мета; H1 один; абзацы 3–5 строк; естественные ключи; Wordstat + Вебмастер | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа; копировать H1–H4 без GEO-слоя |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-...](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Агентский longread 2026 | Семантические кластеры (3–10 запросов на страницу); answer-first после H2; гибрид ИИ + фактчек; E-E-A-T | Перегруз agency-tone; длинный sales-narrative | Копировать 7-разделную структуру 1:1 |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-...](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский чек-лист (май 2026) | Wordstat/Serpstat; Title ~65 знаков; Schema Article + FAQPage | Непроверенные кейсы «+140%» | Цифры без первичника |
| 4 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Практик WordPress (2026) | 12 шагов от ключа до публикации; скриншоты; чек-лист перед публикацией | Мало GEO; узкий фокус WP | Дублировать 12 H2 без сжатия |
| 5 | [blog.click.ru/neiroseti/geo-vs-seo-...](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | GEO+SEO гайд (2026) | Чанки 100–380 слов; lead 40–60 слов; предложения 12–20 слов; кластер вопросов | Не учит писать статью с нуля | Таблицу SEO vs GEO — адаптировать, не копировать |
| 6 | [text.ru/blog/kak-popast-v-ii-poisk-2026-...](https://text.ru/blog/kak-popast-v-ii-poisk-v-2026-poshagovyy-plan-promty) | GEO-практика (11.06.2026) | Answer-first 100 слов; H2-вопросы; TL;DR 40–60 слов после H2; НЧ 100–2000 показов | Кейсы Text Завода; WordPress bias | Непроверенные «93 000 кликов» как универсальный прогноз |
| 7 | [mayai.ru/geo-seo-optimizaciya-neyropoisk/](https://mayai.ru/geo-seo-optimizaciya-neyropoisk/) | Чек-лист GEO SEO (2026) | P0/P1 техника; FAQPage + Article; llms.txt optional; answer-first 40–80 слов | Фокус на сайт, не на одну статью | Копировать 15-пунктовый чек-лист целиком |
| 8 | [qvai.ru/media/kak-pisat-seo-stati](https://qvai.ru/media/kak-pisat-seo-stati) | Близкий H1-intent | «Читают люди и любят поиск» — попадание в H1 карточки | Слабее по глубине и schema | Thin content |

**Паттерн SERP:** доминируют «полный гайд 2026» (семантика, E-E-A-T, ИИ-черновик + редактура). H1 «которые читают люди» слабо закрыт — конкуренты говорят про топ/ключи, не про **читабельность как SEO-фактор**. Вторичный кластер GEO растёт, но редко связан с пошаговым написанием текста.

**Intent:** `how_to` — пользователь хочет **систему**: интент → семантика → структура → текст → мета → FAQ/schema → GEO-упаковка → чеклист. Вторичный: «seo текст для блога», «geo оптимизация статьи».

**Пробел для Excalibur:** единый workflow **SEO + GEO в одном longread** с акцентом на читаемость (инфостиль, острова смысла) и эталоном формата в самой статье (режим B).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен на текущем Cloud worker (`Server "user-mcp-kv" not found`; в secrets нет `MCP_KV_TOKEN`). Вызов `wordstat_get_top_requests` для «как писать seo статьи» **не выполнен**. Точные показы в месяц **не получены** — не использовать выдуманные цифры спроса.

**Действие для ops:** добавить MCP KV в worker и обновить OAuth-токен Wordstat:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Семантические LSI (экспертная оценка по SERP + secondary_queries; без объёмов)

**Primary-кластер «как писать seo статьи»:**
- как написать seo статью / seo текст самому
- seo копирайтинг, seo текст для сайта, seo текст для блога
- структура seo статьи, семантическое ядро для статьи
- заголовки h1 h2 для seo текста
- title description для статьи
- как писать seo тексты в 2026 году

**Вторичный «seo текст для блога»:**
- seo тексты для блога структура
- longread для блога, статья для блога seo
- перелинковка в блоге, объём seo статьи блога

**Вторичный «geo оптимизация статьи»:**
- geo оптимизация контента, generative engine optimization
- answer-first структура, llms.txt, schema.org FAQPage HowTo
- нейровыдача, ai overviews, попасть в ответы нейросетей
- сколько символов в seo статье, что такое geo в seo (из faq_hints)

**SEO-стратегия writer:** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блок структуры longread; «geo оптимизация статьи» — в H2 «SEO + GEO в одной статье»; faq_hints — в FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл, не плотность ключей; переспам вреден | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Одна страница закрывает один смысловой кластер — обычно 3–10 связанных запросов | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| После каждого H2 — содержательный ответ в первых абзацах (answer-first) | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Смысловой блок для ИИ — ориентир 100–380 слов с подзаголовком | [Click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| Lead-абзац: суть темы в первых 40–60 словах | [Click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| Предложение — ориентир 12–20 слов; абзац — 30–60 слов | [Click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| Для нейровыдачи: прямой ответ в первых ~100 словах; H2 как вопросы; TL;DR 40–60 слов после раздела | [Text.ru — ИИ-поиск 2026](https://text.ru/blog/kak-popast-v-ii-poisk-v-2026-poshagovyy-plan-promty) | 11.06.2026 | да |
| Алиса AI берёт **5** источников из **топ-30** органики по запросу | [Text.ru — ИИ-поиск 2026](https://text.ru/blog/kak-popast-v-ii-poisk-v-2026-poshagovyy-plan-promty) | 11.06.2026 | да |
| **44,2%** ИИ-цитат — из первых **30%** текста страницы | [Text.ru — ИИ-поиск 2026](https://text.ru/blog/kak-popast-v-ii-poisk-v-2026-poshagovyy-plan-promty) | 11.06.2026 | да (как вторичная цитата) |
| GEO-оптимизация контента может дать **+30–40%** visibility (Princeton GEO-bench, 10 000 запросов) | [cpa.live — разметка AI](https://cpa.live/articles/razmetka-sajta-dlya-ai-vidimosti/) | 2026 | да (как исследование KDD 2024) |
| FAQ rich results перестали показываться в Google Search **7 мая 2026**; FAQPage остаётся валидным для парсинга и LLM | [cpa.live — разметка AI](https://cpa.live/articles/razmetka-sajta-dlya-ai-vidimosti/) | 2026 | да |
| llms.txt — optional карта pillar-страниц в корне; Google не требует для AI Overviews | [mayai.ru — GEO SEO](https://mayai.ru/geo-seo-optimizaciya-neyropoisk/) | 2026 | да |
| Answer-first для GEO: **40–80** слов прямого ответа под заголовком | [mayai.ru — GEO SEO](https://mayai.ru/geo-seo-optimizaciya-neyropoisk/) | 2026 | да |
| Schema минимум: Organization + Article/BlogPosting + FAQPage JSON-LD | [mayai.ru — GEO SEO](https://mayai.ru/geo-seo-optimizaciya-neyropoisk/) | 2026 | да |
| Title — ориентир ~65 знаков, с ключом; H1 ≠ Title | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Главная задача статьи — полный ответ; возврат в поиск = сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «93 000 кликов» (Text.ru) как универсальный прогноз; «90% просадок из-за schema» без первичника; цифры ВЦИОМ/Mediascope из агентских блогов без cross-check.

**fact-bank.md:** прямых фактов по SEO-написанию нет — опора на источники выше.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается:**
- Яндекс даёт канон SEO без GEO-слоя.
- GEO-гайды не учат писать текст с нуля.
- H1 «которые читают люди» слабо раскрыт в SERP — наш фокус: **читабельность как SEO-фактор** (структура, короткие абзацы, острова смысла).

**Режим B:** статья B01 — **эталон** формата: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (из карточки):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок SEO+GEO | «GEO — …» |
| Conversational H2 | По faq_hints | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, action |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Optional, не замена sitemap |
| Внутренняя ссылка | CTA | На `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting + FAQPage.
6. **Что такое llms.txt и нужен ли он блогу?** — optional карта для AI-краулеров.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать Wordstat-показы (MCP недоступен).
- Не копировать структуру Pikapuka/1PS 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Минимум 5 нумерованных шагов или чеклист 10+ пунктов.
- Без эмодзи; CTA ≤ 3.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантический кластер в Вордстат, спроектирует структуру longread с answer-first блоками, напишет SEO-текст для блога с естественными ключами, добавит FAQ и подготовит handoff для BlogPosting + FAQPage, пройдёт чеклист перед публикацией и поймёт, какие GEO-приёмы (чанки, llms.txt) встроить в ту же статью без второго проекта.

**action_outline:**

1. **Зафиксировать интент и кластер:** primary «как писать seo статьи» + secondary «seo текст для блога», «geo оптимизация статьи»; в Вордстат — 3–10 связанных запросов на одну страницу.
2. **Разобрать SERP:** открыть топ-5 конкурентов; выписать обязательные подтемы и пробел (читабельность / единый SEO+GEO workflow).
3. **Собрать структуру:** H1 с главным ключом; 4 H2 из карточки; H3 по подвопросам; lead 40–60 слов с прямым ответом.
4. **Написать черновик по блокам:** после каждого H2 — answer-first 2–3 абзаца; абзацы 3–5 строк; списки и таблица где уместно; ключи естественно.
5. **Добавить GEO-слой в тот же текст:** чанки 100–380 слов; TL;DR после ключевых H2; упоминание llms.txt как optional; без keyword stuffing.
6. **Подготовить FAQ 5–7:** короткие ответы-действия; включить faq_hints (символы, GEO в SEO).
7. **Оформить мета:** Title ~65 знаков ≠ H1; Description с триггером; alt у изображений; внутренняя ссылка на `/`.
8. **Чеклист перед публикацией:** семантика, уникальность смысла, перелинковка, даты, schema handoff (BlogPosting + FAQPage), island test по каждому H2.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (см. §2) |
| Таблица фактов с URL | ✅ (18 фактов) |
| utility_verdict + action_outline | ✅ |
| GEO hooks + FAQ | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
