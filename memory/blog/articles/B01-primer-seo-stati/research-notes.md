# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to + чеклист)  
**research_date:** 2026-07-11  
**disclaimer:** Все даты, версии и статистика проверены на 2026-07-11 (2026 год).

---

## 1. SERP-обзор (WebSearch, 11.07.2026 — 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Авторитет; 4 шага (тема → семантика → структура → текст); примеры «плохо/хорошо»; Wordstat, alt, мета, перелинковка | Нет GEO/нейропоиска; CTA Директа в конце | Коммерческий блок Директа; копировать H1–H4 1:1 без GEO-слоя |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Практик, 13 шагов (обнов. 05.02.2026) | Полный цикл от спроса до WordPress; интент; анализ конкурентов; чек-лист перед публикацией; скриншоты | Длинный sales-блок хостинга; мало про schema/GEO отдельным блоком | Telegram-CTA как основной финал; дублировать 13 шагов без сжатия |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread 2026 | Семантика, E-E-A-T, чек-лист 10 шагов, Schema Article + FAQPage, Title ~65 знаков | Кейсы без первичника; GEO как побочный эффект E-E-A-T | Непроверенные «+140% трафика»; структура 7 разделов 1:1 |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | «Сначала смысл, потом оптимизация»; кластер вопросов → H2; LSI без насилия | Перегруз про ИИ-генерацию; agency tone | Копировать блок «пишите с ChatGPT» как главный угол |
| 5 | [trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | Чек-лист под ИИ (апр. 2026) | Кластер 10–15 вопросов; answer-first; Schema FAQPage/Article; Core Web Vitals | Уклон в услуги SEO-агентства; цифра «−20% трафика» без первичника | Коммерческий bias; копировать 50+ пунктов без приоритетов |
| 6 | [iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga-kak-pisat-stati-kotorye-privodyat-trafik/](https://iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga-kak-pisat-stati-kotorye-privodyat-trafik/) | SEO-чеклист блога (31 пункт) | Фазы Research → Content → Optimization; Featured Snippet; E-E-A-T | EN-ориентиры (Google PAA); мало RU-нейропоиска | Копировать западный чеклист без адаптации под Яндекс |
| 7 | [dobromarketing.ru/kak-pisat-seo-teksty/](https://dobromarketing.ru/kak-pisat-seo-teksty/) | Баланс «для людей и роботов» | Читабельность как фактор; близко к H1 B01 | Мало пошаговики и schema | Thin content без actionable чеклиста |
| 8 | [mayai.ru/geo-seo-optimizaciya-neyropoisk/](https://mayai.ru/geo-seo-optimizaciya-neyropoisk/) | GEO-чеклист (смежный intent) | Answer-first 40–80 слов; FAQPage; связка SEO→GEO | Другой primary intent (GEO сайта, не написание статьи) | Каннибализация с B04; не делать GEO главным H2 |

**Паттерн SERP:** топ — «полный гайд 2026» (Яндекс Direct, olegweb, pikapuka, 1ps) + отдельный кластер GEO/ИИ-чеклистов (trigub, mayai). Запрос «как писать seo статьи» закрывают длинные инструкции, но **слабо раскрыт угол «которые читают люди»** — читабельность как измеримый workflow, а не лозунг.

**Intent:** `how_to` — пользователь хочет **пошаговую систему**: проверить спрос → интент → структура → текст → мета/schema → GEO-упаковка → финальный чеклист. Вторичные: «seo текст для блога», «geo оптимизация статьи».

**Пробел для Excalibur:** единый **workflow SEO + GEO** в одной статье для автоматизатора/редактора: писать для человека (инфостиль, «острова смысла») и одновременно упаковывать под нейропоиск — без agency-воды и без отдельного «учебника GEO».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 11.07.2026)

⚠️ **WORDSTAT AUTH WARNING:** Сервер MCP `user-mcp-kv` недоступен в среде Cloud Agent (ошибка: server not found). Инструмент `wordstat_get_top_requests` не вызван. Точные объёмы спроса **не получены**. Обновите токен и MCP в локальной среде: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса

| Фраза | Показы/мес |
|-------|------------|
| как писать seo статьи | *не получено — MCP недоступен* |
| seo текст для блога | *не получено — MCP недоступен* |
| geo оптимизация статьи | *не получено — MCP недоступен* |

*Writer: после восстановления MCP перепроверить primary + secondary в Wordstat (регион 225) перед финальной оптимизацией мета.*

### LSI для writer (из SERP + конкурентов, без выдуманных показов)

- как писать seo статьи, как написать seo статью, структура seo статьи  
- seo текст для блога, seo копирайтинг, seo текст для сайта  
- семантическое ядро, яндекс вордстат, lsi слова, интент запроса  
- title description h1, метатеги, перелинковка, alt изображений  
- e-e-a-t, экспертность автора, читабельность, уникальность текста  
- geo оптимизация статьи, answer-first, нейропоиск, faqpage schema  
- чеклист seo статьи, проверка перед публикацией, featured snippet  

**SEO-стратегия (семантика без объёмов):** primary «как писать seo статьи» — в H1, lead, Title; secondary «seo текст для блога» — в блок про структуру longread; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье», не каннибализировать B04.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья 2026 — страница, которая решает задачу пользователя (выбрать, настроить, сделать), а не «текст под ключи» | [olegweb.ru — SEO-статья](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Практический интент «как написать SEO-статью» требует шагов, примеров, таблиц и чек-листа, а не длинной теории | [olegweb.ru — SEO-статья](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Для ИИ-выдачи собирают кластер из **10–15** смежных вопросов перед написанием | [trigub.ru — чек-лист ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 19.04.2026 | да |
| Первые **100 слов** после H1 — ключевая зона для извлечения ответа AI | [trigub.ru — чек-лист ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 19.04.2026 | да |
| На статью — минимум один список и одна таблица или блок карточек | [trigub.ru — чек-лист ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 19.04.2026 | да |
| Core Web Vitals: LCP **< 2,5 с**, INP **< 200 мс**, CLS **< 0,1** | [trigub.ru — чек-лист ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 19.04.2026 | да |
| Schema.org: обязательно Article + FAQPage; опционально HowTo | [trigub.ru — чек-лист ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 19.04.2026 | да |
| Answer-first: после H2 — **40–80 слов** прямого ответа, затем детали | [mayai.ru — GEO SEO](https://mayai.ru/geo-seo-optimizaciya-neyropoisk/) | 06.2026 | да |
| GEO SEO не заменяет SEO: без индекса страница не попадёт в RAG-цепочку нейропоиска | [mayai.ru — GEO SEO](https://mayai.ru/geo-seo-optimizaciya-neyropoisk/) | 06.2026 | да |
| **44,2%** AI-цитат берутся из первых **30%** текста страницы | [text.ru — нейровыдача 2026](https://text.ru/blog/kak-popast-v-ii-poisk-v-2026-poshagovyy-plan-promty) | 2026 | да |
| Для нейровыдачи нужны топ-**30** органической выдачи + формат «ответ сначала» + Schema.org | [text.ru — нейровыдача 2026](https://text.ru/blog/kak-popast-v-ii-poisk-v-2026-poshagovyy-plan-promty) | 2026 | да |
| Суть текста должна быть отражена в первых **40–60 словах** (GEO vs SEO) | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| H1 должен отличаться от Title; Title — ориентир **~65 знаков** с ключом | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 05.2026 | да |
| Главная задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**fact-bank.md:** нет строк по SEO-написанию — все цифры только из таблицы выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); «−20% трафика без ИИ» (trigub без первичника); «Schema повышает CTR на 30%» (t-v.te.ua без первичника); точные показы Wordstat — до восстановления MCP.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один список ключей», а **единый workflow**: интент → кластер вопросов → структура → инфостиль → FAQ/schema → GEO-чанки → чеклист 15–20 пунктов.

**Почему отличается от конкурентов:**
- Яндекс Direct — канон SEO без GEO-слоя и без акцента на читабельность как процесс.
- olegweb/pikapuka — длинные гайды с agency/affiliate CTA; мало «островов смысла» для ИИ.
- GEO-гайды (trigub, mayai/B04) не учат писать текст с нуля.
- H1 «которые читают люди» слабо раскрыт в SERP — наш фокус: **читабельность = структура + инфостиль + answer-first**, не лозунг.

**Режим B:** сама статья B01 — **эталон** формата: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как  
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (для writer и schema)

| Hook | Где в статье | Формат |
|------|--------------|--------|
| Определение SEO-статьи в 40–60 слов | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO в 40–60 слов | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | Подзаголовки | «Сколько символов…», «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец longread | Ответ 2–4 предложения, action-first |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; answer-first 40–80 слов |
| Island test | QA для writer | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексации и структуры.  
3. **Нужно ли переспамить ключевые слова в 2026 году?** — нет; естественные вхождения + LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 на странице; не дублировать.  
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.  
6. **Как упаковать статью под нейропоиск?** — кластер 10–15 вопросов, answer-first после H2, FAQ, таблица/список.  
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Черновик чеклиста (15–20 пунктов для writer)

1. Primary query проверен в Wordstat / SERP (спрос и формулировки).  
2. Интент определён: практический how-to, не «что такое».  
3. Кластер 10–15 подвопросов → черновик H2/H3.  
4. Lead: прямой ответ 40–60 слов после H1.  
5. H1 один; Title ≠ H1; ключ в Title и первом абзаце.  
6. Каждый H2: answer-first 40–80 слов, затем детали.  
7. Абзацы 3–5 строк; списки там, где перечисления.  
8. Минимум 1 таблица + 1 список на статью.  
9. Ключи вписаны естественно — без переспама.  
10. Alt у изображений; файлы латиницей.  
11. Внутренние ссылки 2–3 на релевантные материалы.  
12. FAQ 5–7 с короткими ответами-действиями.  
13. JSON-LD BlogPosting + FAQPage (в schema, не в body).  
14. datePublished / dateModified актуальны.  
15. Island test: каждый H2 самодостаточен для ИИ-цитаты.  
16. Проверка читабельности: убрана вода и канцелярит.  
17. CTA ≤ 3, не подменяет пользу.  
18. Финальный прогон: мета, ссылки, орфография.

---

## 8. Риски и blockers для writer

- Не выдумывать статистику Wordstat и CTR; только таблица фактов.  
- Не копировать структуру Pikapuka/olegweb 1:1.  
- Объём: 8 500–9 500 знаков (`quality-blog.md`).  
- Без эмодзи в article.html.  
- Не каннибализировать B04 (GEO сайта) — только слой «упаковка одной статьи».  
- Internal link: `/` из карточки темы.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель сможет от проверки спроса до публикации собрать SEO-статью: определить интент, построить структуру из кластера вопросов, написать читаемый текст без переспама, упаковать блоки под нейропоиск (answer-first, FAQ, schema) и проверить материал по чеклисту из 15–20 пунктов.

**action_outline:**

1. **Проверить спрос и интент:** открыть Wordstat и топ-5 SERP по «как писать seo статьи»; зафиксировать практический интент и подвопросы.  
2. **Собрать кластер:** выписать 10–15 смежных вопросов → черновик H1 + H2/H3 в Docs/Notion.  
3. **Написать lead:** 40–60 слов прямого ответа на главный запрос сразу после H1.  
4. **Заполнить структуру:** по каждому H2 — answer-first 40–80 слов, затем примеры/таблица/список; абзацы 3–5 строк.  
5. **Вплести семантику:** primary в H1, первом абзаце, Title; secondary и LSI — в подзаголовках и тексте без переспама.  
6. **Добавить FAQ и перелинковку:** 5–7 вопросов с ответами-действиями; 2–3 внутренние ссылки.  
7. **Оформить мета и медиа:** Title (~65 знаков) ≠ H1; Description; alt у изображений.  
8. **Подготовить schema:** BlogPosting + FAQPage JSON-LD (отдельно от body).  
9. **Финальный чеклист:** пройти 15–20 пунктов (раздел 7); исправить воду, дубли, битые ссылки — затем публикация.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (AUTH WARNING) |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| Чеклист 15–20 | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `blog-topics.md` + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅ PASS
utility_verdict: PASS
wordstat: ⚠️ MCP user-mcp-kv недоступен — точные показы не получены; LSI из SERP
summary: SERP — 8 конкурентов (Яндекс Direct, olegweb, pikapuka, 1ps, trigub, iconsult, dobromarketing, mayai/GEO). Угол — единый workflow SEO+GEO longread «для людей»: читабельность, answer-first, FAQ/schema, чеклист 15–20. 20 фактов с URL, 9 шагов action_outline, 7 FAQ. Готов к writer.
===
