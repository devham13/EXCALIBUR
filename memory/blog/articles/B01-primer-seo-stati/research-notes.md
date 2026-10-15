# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + чеклист)  
**research_date:** 2026-08-09  
**utility_gate (topic):** PASS  
**utility_verdict:** PASS  
**disclaimer:** Все даты, версии и статистика проверены на 2026-08-09 (2026 год).

---

## reader_outcome

После прочтения гайда читатель сможет **с нуля собрать и опубликовать SEO-статью для блога**: проверить спрос и интент, составить структуру H1–H3 с FAQ, написать читаемый текст с LSI, заполнить Title/Description/alt, добавить schema (BlogPosting + FAQPage) и пройти финальный чеклист перед публикацией — с учётом GEO-слоя для AI-выдачи.

---

## action_outline (workflow для writer)

1. **Проверить спрос и интент** — Wordstat/подсказки Яндекса; классифицировать запрос (how-to / commercial); выписать 3–5 смысловых кластеров LSI.
2. **Разобрать топ-5 SERP** — H1/H2 конкурентов, формат (гайд vs чек-лист), пробелы; не копировать структуру 1:1.
3. **Собрать каркас** — H1 с главным ключом; H2 как подзадачи; lead с прямым ответом в первых 80–100 словах; FAQ 5–7 вопросов в конце.
4. **Написать черновик** — короткие абзацы (3–5 строк), списки/таблицы, инфостиль без воды; ключ в H1, первом абзаце, 1–2 H2; LSI органично по тексту.
5. **Усилить E-E-A-T lite** — автор, дата, один реальный кейс/наблюдение; исходящие ссылки на авторитетные источники для цифр.
6. **Техническая упаковка** — Title (~60–65 знаков) ≠ H1; Description 140–160 знаков; alt у изображений; ЧПУ-slug; 3–5 внутренних ссылок.
7. **GEO-слой** — атомарные H2 («острова смысла»); ответ сразу после заголовка; JSON-LD BlogPosting + FAQPage (в meta, не в body).
8. **Финальный чеклист** — 15–20 пунктов: семантика, мета, структура, FAQ, schema, перелинковка, читабельность, robots.txt для AI-ботов не закрыт.

---

## 1. SERP-обзор (WebSearch Cursor, 2026-08-09)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон: семантика, H1–H4, естественность ключей, Wordstat, alt, мета, перелинковка; примеры «плохо/хорошо» | Нет GEO/нейропоиска; CTA Директа | Блок про Директ; «что такое SEO» без actionable шагов |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread агентства (апр./июн. 2026) | Кластеры 3–5 групп; «ответ сразу после H2»; ИИ + постобработка; история алгоритмов | Очень длинный; agency-tone; GEO как подраздел | Перегруз историей алгоритмов; sales-narrative |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-…](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский гайд (май 2026) | 10 шагов; E-E-A-T; Title ~65 знаков; Schema Article + FAQPage | Кейсы с непроверенными %; 7-разделная структура перегружена | «+140% трафика» без первичника |
| 4 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Практик WP (фев. 2026) | **13 пошаговых шагов** от темы до индексации; таблица «конкурент vs вы»; WordPress-оформление | Мало GEO; фокус на WP-хостинг affiliate | Affiliate CTA Timeweb/Paradigma |
| 5 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | SEO-агентство (2026) | Принцип «полный ответ на одной странице»; LSI и хвосты; поведенческий сигнал | Короткий (~1,5k знаков); нет чек-листа и schema | Вода «просто следуй принципам» |
| 6 | [blog.sape.ru/…/prompt-inzhiniring-v-2026-godu/](https://blog.sape.ru/blog/2026/07/17/kak-pisat-teksty-dlya-topa-vydachi-v-nejroseti-prompt-inzhiniring-v-2026-godu/) | GEO + SEO (июль 2026) | H1 50–65 символов; первые 80–100 слов = прямой ответ для AI; H2 как вопросы | Уклон в промпт-инжиниринг и SAPE | Копировать промпт-шаблоны 1:1 |
| 7 | [hubes.ru/blog/kak-napisat-seo-optimizirovannuyu-statyu](https://hubes.ru/blog/kak-napisat-seo-optimizirovannuyu-statyu) | How-to (2026) | Пошаговое руководство; структура + ключи + ИИ | Средняя глубина; мало дифференциации | Generic «полное руководство» |
| 8 | [mayai.ru/geo-optimizaciya-sajta-2026/](https://mayai.ru/geo-optimizaciya-sajta-2026/) | GEO-чеклист (2026) | FAQ 5–7 × ≤80 слов; robots.txt для AI-ботов; связка SEO→GEO | Фокус на GEO сайта, не на написании статьи | Цифры Princeton без arxiv в теле |

**Паттерн SERP (август 2026):** топ — «полный гайд 2026» с E-E-A-T, Wordstat, чек-листом (1ps, pikapuka, seomatik, hubes). Отдельный кластер — GEO/AI-поиск (sape, mayai, trigub). H1 «которые читают люди» слабо представлен (qvai.ru, bestseoserg.com — поверхностно).

**Intent:** `how_to` — пользователь хочет **пошаговую систему** от семантики до публикации. Вторичный: «seo текст для блога» (формат longread) и «geo оптимизация статьи» (как упаковать под AI-выдачу).

**Пробел Excalibur:** единый **workflow SEO + GEO в одной статье** с акцентом на **читабельность как фактор ранжирования** (острова смысла, инфостиль) — без agency-воды и без отдельного «GEO-only» гайда.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в текущем Cloud-окружении (MCP not found). Инструмент `wordstat_get_top_requests` не вызван. **Точные объёмы спроса (показы/мес) не получены** — в тексте статьи цифры Wordstat не использовать.

**Действие для пайплайна:** обновить токен / подключить MCP через [OAuth Yandex](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40) и `.cursor/mcp.json` (см. B03 «Подключение MCP в Cursor»).

### Семантика без цифр (экспертная оценка + SERP, для LSI writer)

**Primary cluster:** как писать seo статьи, как написать seo статью, seo статья для блога, структура seo статьи

**Secondary (из карточки B01):**
- seo текст для блога, seo текст как написать, seo копирайтинг 2026
- geo оптимизация статьи, geo seo текст, оптимизация под нейропоиск

**LSI для writer (из топа SERP + конкурентов):**
- семантическое ядро, Wordstat, поисковый интент, LSI-фразы, кластеризация запросов
- Title, meta description, H1, H2, H3, FAQ, микроразметка, Schema.org, BlogPosting, FAQPage
- E-E-A-T, инфостиль, перелинковка, alt-текст, ЧПУ, featured snippet, нейроответ
- generative engine optimization (GEO), answer-first, атомарный чанк, llms.txt
- чек-лист перед публикацией, переспам, уникальность, поведенческие факторы

**SEO-стратегия (без частотностей):** primary «как писать seo статьи» — в H1/lead; «seo текст для блога» — в блок структуры longread; «geo оптимизация статьи» — отдельный H2 + FAQ; faq_hints («сколько символов», «что такое geo в seo») — в FAQ.

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
| Семантику группируют в **3–5 смысловых кластеров**; после каждого H2 — содержательный ответ | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| H1 должен **отличаться от Title** | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Title — ориентир **~65 знаков**, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Schema.org: **Article + FAQPage** для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| H1 оптимален **50–65 символов**; для AI-выдачи заголовок = сигнал прямого ответа | [SAPE — промпт-инжинiring SEO/GEO 2026](https://blog.sape.ru/blog/2026/07/17/kak-pisat-teksty-dlya-topa-vydachi-v-nejroseti-prompt-inzhiniring-v-2026-godu/) | 17.07.2026 | да |
| Первые **80–100 слов** должны содержать прямой развёрнутый ответ на основной вопрос (GEO) | [SAPE — промпт-инжинiring SEO/GEO 2026](https://blog.sape.ru/blog/2026/07/17/kak-pisat-teksty-dlya-topa-vydachi-v-nejroseti-prompt-inzhiniring-v-2026-godu/) | 17.07.2026 | да |
| Title **≤60** символов, meta description **140–160**, **3–5** внутренних ссылок | [Spilno Agency — SEO-копирайтинг 2026](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да |
| Информационные SEO-тексты — ориентир **1500–4000 слов** (зависит от жанра) | [Pawetta — SEO-копирайтинг 2026](https://pawetta.com/blog/seo-kopirayting/) | 2026 | да |
| Главная задача статьи — **полный ответ**; возврат в поиск = сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 09.08.2026 | да |
| FAQ-блок: **5–7** вопросов, ответ **до 80 слов** — формат для AI-цитирования | [MayAI — GEO чек-лист 2026](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да |
| AI-боты (GPTBot, PerplexityBot и др.) не должны быть заблокированы в robots.txt без причины | [MayAI — GEO чек-лист 2026](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да |

**fact-bank.md:** нет строк по SEO-написанию — все цифры только из таблицы выше.

**Не использовать:** «+140% трафика» (Pikapuka); keyword density %; любые показы Wordstat без MCP.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается:**
- Яндекс Direct — канон SEO без GEO-практики для блога.
- GEO-гайды (mayai, trigub) не учат писать текст с нуля.
- Агентские гайды (1ps, pikapuka) перегружены E-E-A-T-кейсами и CTA.
- H1 «которые читают люди» — слабо раскрыт в SERP; наш фокус: **читабельность = SEO + GEO**.

**H2-каркас (из карточки B01):**
1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

**Объём (quality-blog):** 8 500–9 500 знаков текста.

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO — Generative Engine Optimization…» |
| Conversational H2 | FAQ-блоки | «Сколько символов…», «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, ≤80 слов |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом контенте.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 — на странице.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting + FAQPage.
6. **Что такое llms.txt?** — опциональный файл для AI-краулеров; не замена sitemap.
7. **Как проверить статью перед публикацией?** — чеклист из action_outline п. 8.

---

## 7. Риски для writer

- Не выдумывать статистику Wordstat и кейсы с %.
- Не копировать структуру Pikapuka/1ps 1:1.
- Без эмодзи; CTA ≤ 3.
- Цифры только из таблицы фактов §3.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| utility_verdict: PASS | ✅ |
| action_outline 5–9 шагов | ✅ (8) |
| reader_outcome | ✅ |
| SERP ≥ 3 конкурента | ✅ (8) |
| Таблица фактов с URL | ✅ (17) |
| Wordstat (MCP) | ⚠️ недоступен |
| GEO hooks + FAQ | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅
utility_verdict: PASS
utility_gate_topic: PASS
wordstat: MCP user-mcp-kv недоступен — показы не получены
summary: SERP 8 конкурентов (WebSearch 2026-08-09): Яндекс Direct, 1PS, Pikapuka, olegweb, MaryProject, SAPE, hubes, MayAI. Угол — единый how-to workflow SEO+GEO longread «для людей»: читабельность, атомарные чанки, FAQ/schema, чеклист 15–20. 17 фактов с URL, 7 FAQ, action_outline 8 шагов. Готов к writer.
===
