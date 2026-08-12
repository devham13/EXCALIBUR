# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата на самой статье)  
**research_date:** 2026-08-12  
**disclaimer:** Все даты, версии и статистика проверены на 12.08.2026.

---

## Utility gate

| Поле | Значение |
|------|----------|
| `utility_verdict` | **PASS** |
| `search_intent` | how_to |
| `article_mode` | B |
| Gate script | `python3 scripts/excalibur_blog_utility_gate.py --topic-id B01` → PASS |

**reader_outcome:** После прочтения читатель сможет за одну рабочую сессию собрать семантику, спланировать структуру SEO+GEO longread, написать черновик с FAQ/schema и пройти финальный чеклист перед публикацией в WordPress.

**action_outline (workflow для writer):**

1. Проверить интент запроса в SERP и выписать 3–5 смысловых кластеров (primary + LSI).
2. Собрать структуру H1 → H2 → H3: каждый H2 = подвопрос + ответ в первом абзаце.
3. Написать lead: боль → обещание → результат (без «в этой статье»).
4. Наполнить блоки: списки, таблицы, пример «плохо/хорошо», E-E-A-T lite (опыт, источники).
5. Добавить GEO-слой: атомарные чанки 60–100 слов, answer-first под каждым H2.
6. Сформировать FAQ 5–7 пар (короткие ответы-действия) + handoff для FAQPage schema.
7. Заполнить Title/Description/URL/alt; 3–5 внутренних ссылок.
8. Пройти чеклист 15–20 пунктов перед публикацией (мета, schema, читабельность, перелинковка).

---

## 1. SERP-обзор (WebSearch, 12.08.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread + краткая инструкция | Wordstat-кластеры, H1–H3, LSI без переспама, II как помощник | Длинный; GEO не выделен отдельным workflow | Копировать структуру 1:1 |
| 2 | [olegweb.ru — алгоритм 13 шагов](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый WP-гайд | 13 шагов от ключа до индексации; интент, SERP, WordPress | Уклон в «сделай сайт сам»; мало GEO | Дублировать 13 H2 как каркас |
| 3 | [direct.yandex.ru — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный Яндекс (янв. 2026) | Канон: объём, H1–H4, Wordstat, переспам, Title/Description | Нет GEO/нейропоиска | CTA Директа |
| 4 | [serptop.ru — гайд + чек-лист](https://serptop.ru/blog/kak-pisat-seo-teksty/) | Чек-лист + структура | Формула H1, lead 50–100 слов, meta ≤70/160, ЧПУ | Без GEO-слоя | Шаблонные формулы без контекста B2B |
| 5 | [seo-vladimir.ru — LSI 2026](https://seo-vladimir.ru/blog/lsi-copywriting-seo-2026/) | SEO-копирайтинг | Разбор мифа LSI → покрытие интента; списки/таблицы | Узкий региональный блог | Тезис «3–4 ключа на 1000 знаков» без оговорки |
| 6 | [bmg.by — SEO-чек-лист публикаций](https://bmg.by/blog/decisions/seo-checklist-for-content-and-ai-search/) | Чек-лист tech+content+AI | Рабочий список без воды; E-E-A-T, AI Mode | EN-контекст частично | Копировать чек-лист дословно |
| 7 | [habr.com/1042732 — GEO/AEO 2026](https://habr.com/ru/articles/1042732/) | GEO longread | RAG, answer-first, Schema; RU-рынок | Не учит писать SEO-текст с нуля | Encyclopedia-tone |
| 8 | [pawetta.com — GEO/AEO](https://pawetta.com/blog/geo-aeo-optimizaciya/) | Практика Яндекс vs Google | Answer-first + schema работают в обеих системах | Фокус на GEO, не на writing workflow | Паника «SEO мёртв» |

**Паттерн SERP (август 2026):** топ — «полный гайд 2026» (1ps, olegweb, pikapuka) + чек-листы (serptop, bmg). H1 «которые читают люди» слабо представлен; конкуренты давят на E-E-A-T и II, но редко связывают **читабельность + SEO + GEO** в одном actionable workflow для B2B-блога.

**Intent:** how_to — собрать семантику → структура → текст → мета/schema → проверка. Вторичный: «seo текст для блога», «geo оптимизация статьи».

**Пробел для Excalibur:** единый workflow «для людей и для нейропоиска» на русском, режим B, эталон longread 8 500–9 500 знаков; чеклист перед публикацией; без agency-CTA и непроверенных «+140% за 3 недели».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` недоступен в текущем Cloud Agent runtime (MCP не подключён). Вызов `wordstat_get_top_requests` для `как писать seo статьи` и secondary queries **не выполнен**. Точные объёмы спроса **не получены** — цифры в таблице ниже **не заполняются**.

**Действие для следующего прогона:** подключить MCP в `mcp.json` и повторить:
- `wordstat_get_top_requests` → `как писать seo статьи` (primary)
- `wordstat_get_top_requests` → `seo текст для блога`
- `wordstat_get_top_requests` → `geo оптимизация статьи`

При ошибке 401 обновить токен: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса

| Фраза | Показы/мес |
|-------|------------|
| как писать seo статьи | *MCP недоступен* |
| seo текст для блога | *MCP недоступен* |
| geo оптимизация статьи | *MCP недоступен* |
| как написать seo текст | *MCP недоступен* |
| seo копирайтинг | *MCP недоступен* |
| seo статья для сайта | *MCP недоступен* |

### LSI для writer (экспертная оценка по SERP + карточка B01; **не Wordstat**)

- как писать seo статьи, seo текст для блога, seo копирайтинг 2026  
- структура seo статьи, семантическое ядро, яндекс вордстат  
- title description h1, метатеги, перелинковка, alt текст  
- e-e-a-t, интент запроса, lsi слова, переспам ключей  
- geo оптимизация статьи, answer-first, faq schema, json-ld  
- чеклист перед публикацией, seo текст для wordpress  
- сколько символов в seo статье, что такое geo в seo  

**SEO-стратегия (до получения Wordstat):** primary в H1/lead; secondary «seo текст для блога» — в блок про формат longread; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье»; faq_hints из карточки — в FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Google: people-first контент — создан для людей, SEO применяется к такому контенту, а не «ради роботов» | [Google — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| E-E-A-T: experience, expertise, authoritativeness, trustworthiness; trust — ключевой | [Google — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| Нет лимита символов у `<title>`, но title link обрезается под ширину устройства | [Google — Title links](https://developers.google.com/search/docs/appearance/title-link) | актуально 2026 | да |
| Уникальный meta description на каждую страницу; дубли не помогают в выдаче | [Google — Snippets](https://developers.google.com/search/docs/appearance/snippet) | актуально 2026 | да |
| GEO (Generative Engine Optimization) — оптимизация видимости контента в ответах генеративных поисковых систем | [arxiv.org — GEO paper](https://arxiv.org/abs/2311.09735) | KDD 2024 | да |
| GEO-bench: методы Cite Sources, Quotation Addition, Statistics Addition дают **+30–40%** visibility (Position-Adjusted Word Count) | [arxiv.org — GEO paper](https://arxiv.org/abs/2311.09735) | KDD 2024 | да |
| На Perplexity.ai зафиксировано улучшение visibility до **37%** | [arxiv.org — GEO paper](https://arxiv.org/abs/2311.09735) | KDD 2024 | да |
| Keyword stuffing в GEO-контексте работает **хуже** baseline (≈ −10%) | [arxiv.org — GEO paper](https://arxiv.org/abs/2311.09735) | KDD 2024 | да |
| Princeton GEO: правильная структура, цитаты и статистика повышают видимость в AI-ответах до **40%** (цит. RU-гайд) | [melanina.ru — GEO-гайд](https://melanina.ru/guides/marketing/optimizaciya-sajta-pod-ai-poisk/) | 2026 | да (как вторичная цитата на arxiv) |
| Прямой ответ в начале раздела + schema работают и для Яндекс Нейро, и для Google AI Overviews | [pawetta.com — GEO/AEO](https://pawetta.com/blog/geo-aeo-optimizaciya/) | 2026 | да |
| Главная задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| Meta title ориентир ≤70 символов; description ≤160 — практический чек-лист (не официальный лимит Google) | [serptop.ru — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да (как практика, не как «правило Google») |

**fact-bank.md:** прямых фактов про SEO-writing нет — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели»; «AI обрабатывает 25% запросов» без первичника; «64% потери CTR» (generative-optimization.ru) без cross-check; точные % Wordstat.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Единый workflow: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → чеклист.

**Почему отличается от конкурентов:**
- Яндекс — канон SEO без GEO-слоя.
- 1ps/olegweb — длинные encyclopedia; у нас **компактный action-first** workflow + чеклист.
- GEO-гайды (Habr, pawetta) не учат писать текст с нуля.
- H1 «которые читают люди» — дифференциатор: **читабельность как SEO/GEO-фактор**.

**Режим B:** статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO — …» |
| Conversational H2 | FAQ-темы | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и SERP; для how-to в Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — дополнение к SEO: цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета, H1 на странице; не дублировать дословно.
5. **Какие schema для SEO-статьи блога?** — BlogPosting (Article) + FAQPage.
6. **Что такое llms.txt и нужен ли блогу?** — сигнал для AI-краулеров; не замена sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать статистику Wordstat и CTR.
- Не копировать 13 шагов olegweb / 7 разделов pikapuka 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Без эмодзи, без VPN; site_url — плейсхолдер или `/`.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (18) |
| utility_verdict + action_outline + reader_outcome | ✅ |
| GEO hooks + FAQ | ✅ |
| H2 outline | ✅ |

**Writer:** готов с оговоркой по Wordstat (LSI из SERP до подключения MCP).

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅
utility_verdict: PASS
wordstat: MCP user-mcp-kv недоступен — точные показы не получены; LSI из SERP
summary: SERP 8 конкурентов (1ps, olegweb, Яндекс Direct, serptop, seo-vladimir, bmg, Habr GEO, pawetta). Угол — единый workflow SEO+GEO longread «для людей»: интент → структура → FAQ/schema → чеклист. 18 фактов с URL, 7 FAQ, action_outline 8 шагов. Writer ready (Wordstat pending MCP).
===
