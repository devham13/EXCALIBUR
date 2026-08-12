# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-08-12  
**disclaimer:** Все даты, версии и статистика проверены на 12.08.2026.

---

## 1. SERP-обзор (WebSearch, август 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Авторитет; 4 шага (тема → семантика → структура → текст); примеры «плохо/хорошо»; H1–H4, alt, мета, перелинковка; Wordstat/Вебмастер | Нет GEO/нейропоиска; CTA Директа в конце | Коммерческий блок Директа; копировать H-структуру без GEO-слоя |
| 2 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист редакции (04.06.2026) | **9 критериев** SEO-текста 2026; E-E-A-T + ЭПОС Яндекса; answer-first; AI-выдача (AI Overviews, Алиса AI); robots.txt для OAI-SearchBot | Чек-лист «размазан» по H2, нет единого printable workflow | Agency CTA «обновим ваши статьи» как основной угол |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread + ИИ (обновл. 15.06.2026) | Правило «после каждого H2 — содержательный ответ»; кластеры семантики; GEO/AEO-блок; FAQ в конце | Длинный sales-narrative 1PS; смешение SEO-текста и SEO-статьи без компактного чеклиста | Cookie-баннер-тон; копировать 20-минутную структуру 1:1 |
| 4 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Практик WordPress (2026) | **13 шагов** от ключа до индексации; интент, SERP, структура, WP-оформление | Мало про GEO/AI-чанки; без schema-handoff | Дублировать 13 H2 как каркас нашей статьи |
| 5 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (2026) | E-E-A-T, Wordstat/Serpstat, Schema Article+FAQPage, Title ~65 знаков | Непроверенные кейсы «+140% трафика» | Проценты без первичника |
| 6 | [roiseo.ru/blog/struktura-seo-stati-dlya-bloga/](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон структуры | Первый экран: ответ **40–70 слов**; блоки «ошибки → чек-лист → FAQ» | Узкий фокус на структуре, без семантики/Wordstat | Копировать таблицу блоков без контекста |
| 7 | [developers.google.com/search/docs/fundamentals/creating-helpful-content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Официальный Google | People-first content; self-assessment questions; E-E-A-T; SEO ≠ search-engine-first | EN, без RU-специфики Яндекса | Переводить дословно без адаптации |
| 8 | [tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | Формула + self-test (2026) | 6 вопросов самопроверки текста; LSI через синонимы; форматы (FAQ, гайд, сравнение) | Короткий, без полного workflow | — |

**Паттерн SERP (август 2026):** топ — «полный гайд 2026» с E-E-A-T, семантикой, чек-листом и блоком про AI-выдачу. Прямого совпадения с H1 «которые **читают люди**» мало: конкуренты говорят про «полезность», но редко связывают **читабельность** (инфостиль, короткие абзацы, island-test) с SEO и GEO в одном workflow.

**Intent:** `how_to` — пользователь хочет **пошаговую систему**: проверить спрос → интент → структура → черновик → мета/schema → GEO-упаковка → финальный чеклист. Вторичный intent: понять связку **SEO + GEO** в одном материале (secondary_query «geo оптимизация статьи»).

**Пробел для Excalibur:** единый **action-first workflow** «от Wordstat до публикации» с акцентом на **longread для людей** (не переспам, не вода) + минимальный GEO-слой (answer-first, FAQ/schema) — без agency-CTA и без «новостей SEO 2026».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` **не подключён** в среде Cloud Agent (инструмент `wordstat_get_top_requests` недоступен). Точные объёмы спроса **не получены**. Не выдумывать цифры показов.

**Действие для оператора:** подключить MCP и обновить OAuth-токен Wordstat:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (без Wordstat-цифр — для writer до повторного research)

**Primary:** как писать seo статьи  

**Secondary (из карточки B01):** seo текст для блога, geo оптимизация статьи  

**LSI из SERP и конкурентов (вписывать естественно):**
- seo копирайтинг, seo longread, структура seo статьи, семантическое ядро, яндекс вордстат
- title и description, h1 h2 структура, e-e-a-t, эпос (экспертность полезность оригинальность содержательность)
- lsi ключи, переспам ключевых слов, чек-лист seo статьи, как написать seo текст самому
- faq schema, blogposting json-ld, ai overviews, алиса ai, нейровыдача, answer-first
- внутренняя перелинковка, alt текст изображений, индексация статьи

**SEO-стратегия (без частот):** primary в H1/lead/Title; «seo текст для блога» — в блок про формат longread; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье», не подменять H1.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — он зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир **3–5 строк**; перечисления — списками | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают **смысл и полезность**, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в **Яндекс Вордстат** и **Яндекс Вебмастер** | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Google: контент для **людей**, не для манипуляции выдачей; SEO допустимо, если помогает discovery **people-first** контента | [Google Search Central — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| E-E-A-T: **Trust** — главный столп; Experience добавлен в дек. 2022 | [Google Search Central — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| В 2026 контент оценивают и классическая выдача, и **AI Overviews / AI Mode (Google)**, **Поиск с Алисой AI (Яндекс)**, ChatGPT, Perplexity | [Texterra — чек-лист SEO-текста 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Яндекс **ЭПОС**: экспертность, полезность, оригинальность, содержательность + релевантность запросу | [Texterra — чек-лист SEO-текста 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Базовый принцип 2026: **от главного ответа к деталям** — сначала суть, потом нюансы | [Texterra — чек-лист SEO-текста 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Для AI-выдачи: короткий прямой ответ в начале; H2/H3 понятны без контекста; даты публикации/обновления | [Texterra — чек-лист SEO-текста 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Для ChatGPT-поиска **не блокировать OAI-SearchBot** в robots.txt (отличать от GPTBot) | [Texterra — чек-лист SEO-текста 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| После каждого H2 — **содержательный ответ**, не «заголовок ради ключей» | [1PS.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| Главный ключ: H1, первый абзац, 1–2 H2, title, description; LSI — по тексту, без насильных вхождений | [1PS.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 15.06.2026 | да |
| Первый экран SEO-статьи блога: H1 + **ответ 40–70 слов** на главный вопрос | [ROI SEO — структура статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| Алгоритм написания SEO-статьи: интент → SERP → структура → текст → мета → публикация (13 шагов у практика) | [OlegWeb — SEO-статья](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 2026 | да |
| Title — ориентир **~65 знаков**, с ключом и триггером (чек-лист, инструкция); H1 ≠ Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Schema.org **Article/BlogPosting + FAQPage** — для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |

**fact-bank.md:** прямых фактов по SEO-статьям нет — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); любые показы Wordstat без MCP; «микроразметка ×1,5–2 цитирование» без arxiv/первичника.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один список ключей», а **единый workflow**: интент → семантика → структура → черновик → мета → FAQ/schema → GEO-чанки → **чеклист перед публикацией**.

**Почему отличается от конкурентов:**
- Яндекс Direct — канон без GEO и без printable чеклиста.
- Texterra — 9 критериев, но без сквозного «сделай сам за одну статью».
- 1PS/Pikapuka — agency/продуктовый narrative и непроверенные кейсы.
- H1 «**которые читают люди**» — слабо раскрыт в SERP; наш фокус: **читабельность как SEO-фактор** (короткие абзацы, island-test, инфостиль) + техника.

**Tone (site-brief):** практично, по-человечески; без корпоративной воды и эмодзи в article.html.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (не два проекта)
2. Структура longread: H1–H3, lead 40–70 слов, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

**Режим B:** сама статья B01 — **эталон** формата: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2.

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO — …» |
| Conversational H2 | «Что такое GEO в SEO?», «Сколько символов…?» | Вопрос в заголовке |
| FAQ 5–7 пар | Конец longread | Ответ 2–4 предложения, action |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA для writer | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI/синонимы.
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны блогу?** — BlogPosting (или Article) + FAQPage.
6. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.
7. **Можно ли писать SEO-статью с ИИ?** — да, если добавлен человеческий опыт, факты с источниками и редакторская проверка (Google people-first).

---

## 7. Риски для writer

- Не выдумывать статистику Wordstat и кейсы с процентами.
- Не копировать 13 шагов OlegWeb или 9 H2 Texterra 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи в article.html.
- CTA ≤ 3; не подменять пользу.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику в Wordstat/Вебмастере, определит интент по SERP, составит структуру longread с lead-ответом 40–70 слов, напишет черновик без переспама, заполнит Title/Description, добавит FAQ и JSON-LD, пройдёт чеклист из 15–20 пунктов и опубликует статью, которую смогут процитировать и поиск, и AI-выдача.

**action_outline:**

1. **Проверить спрос и интент:** primary query в Wordstat/Вебмастере; открыть топ-5 SERP — какой формат (гайд, чек-лист, сравнение) и что не закрыто конкурентами.
2. **Собрать семантику:** primary + 5–10 LSI/вторичных; сгруппировать в кластеры под будущие H2; не включать фразы, которые ломают язык.
3. **Собрать структуру:** один H1; H2 = подзадачи из action_outline; lead с прямым ответом **40–70 слов**; места под таблицу, чек-лист, FAQ.
4. **Написать черновик «для людей»:** короткие абзацы 3–5 строк; после каждого H2 — содержательный ответ; личный опыт/пример; убрать воду (island test).
5. **Встроить ключи естественно:** primary в H1, первом абзаце, 1–2 H2, Title; LSI по тексту; проверить отсутствие переспама.
6. **Оформить мета и медиа:** Title ~65 знаков ≠ H1; Description с пользой; alt у изображений по содержанию, не по ключам; 2–4 осмысленные внутренние ссылки.
7. **Добавить FAQ (5–7) и GEO-упаковку:** короткие ответы-действия; answer-first в начале блоков; handoff schema (BlogPosting + FAQPage) — не в body.
8. **Пройти чеклист перед публикацией:** E-E-A-T/автор, даты, факты с URL, schema, robots (OAI-SearchBot не блокировать без причины), отправка на индексацию.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (18 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 конкурентов (Яндекс Direct, Texterra, 1PS, OlegWeb, Pikapuka, ROI SEO, Google SC, Tolk). Wordstat MCP недоступен — цифры спроса не получены; LSI из SERP. Угол — единый workflow SEO+GEO longread «для людей»: lead 40–70 слов, island-test, FAQ/schema, чеклист 15–20. 18 фактов с URL, 8 шагов action_outline, 7 FAQ. Готов к writer.
===
