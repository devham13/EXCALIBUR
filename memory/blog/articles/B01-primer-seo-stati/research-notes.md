# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + демонстрация формата на самой статье)  
**research_date:** 2026-10-04  
**disclaimer:** Все даты, версии и статистика проверены на 04.10.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch Cursor, 04.10.2026 + сверка с research-serp.json)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Авторитет; workflow тема → семантика → структура → текст; примеры «плохо/хорошо»; Wordstat; alt, мета, перелинковка | Нет GEO/нейропоиска; CTA Директа | Коммерческий хвост; копировать H1–H4 без GEO-слоя |
| 2 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Пошаговый гайд 2026 (7 шагов) | Чёткий алгоритм: запросы → TOP → структура → текст → Title/Description → релевантность → контроль после публикации | Без schema/GEO и чек-листа 15+ | Дублировать 7 H2 1:1 |
| 3 | [seotika.ru/kak-pisat-seo-stati](https://seotika.ru/kak-pisat-seo-stati/) | Агентский longread (обновл. 09.2026) | Семантика, кластеры, интент, FAQ; «ответ в первых 100 словах»; таблицы | Agency bias; «1500–3000 слов» и «1–2% плотности» — эвристика, не норма Яндекса | Непроверенные кейсы агентства |
| 4 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | WordPress how-to (13 шагов) | Полный цикл до WP: интент, конкуренты, E-E-A-T, мета, внутренние ссылки | Узко под WP; нет GEO-блока | 13 шагов как скелет 1:1 |
| 5 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | Семантика, E-E-A-T, примеры; актуальный год в URL | Акцент на ИИ-генерацию без human-in-the-loop | Обещания «минуты на статью» |
| 6 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Чек-лист + E-E-A-T | Schema Article + FAQPage; Title ~65 знаков | Кейсы с процентами без первичника | Копировать 7-разделную структуру |
| 7 | [articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-…](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Пошаговая инструкция 2026 | Семантика → публикация; AI-выдача | Продуктовый угол AI-сервиса | Sales под «полностью на ИИ» |
| 8 | [www.meta-journal.ru/2026/06/19/primer-seo-stati](https://www.meta-journal.ru/2026/06/19/primer-seo-stati/) | Близкий H1 «которые читают люди» | Прямое попадание в формулировку H1 карточки B01 | Меньше глубины, чем у seotika/1ps | Конкурирует за тот же title-intent |
| 9 | [roiseo.ru/blog/struktura-seo-stati-dlya-bloga](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон структуры блога | Таблица блоков: lead 40–70 слов, чек-лист, FAQ, schema | Узкий SEO-агентский контекст | Шаблон таблицы можно адаптировать, не копировать |
| 10 | [blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | SEO + GEO для текстов (2026) | Развод SEO/AEO/GEO; чанки 128–515 токенов; практика для ИИ | CTA click.ru; часть цифр — медиа-опросы | Паника «SEO мёртв» |

**Паттерн SERP (октябрь 2026):** доминируют longread «как написать SEO-статью в 2026» (7–13 шагов, семантика, E-E-A-T, чек-лист). Отдельный кластер — GEO vs SEO для текстов. H1 «…которые читают люди» встречается (meta-journal, qvai), но реже, чем «SEO-текст/статья 2026».

**Intent:** `how_to` — пользователь хочет **повторяемый workflow**: спрос → интент → структура → черновик → мета → проверка → публикация. Вторичные: «seo текст для блога» (шаблон блоков), «geo оптимизация статьи» (слой поверх SEO, не отдельный жанр).

**Пробел для Excalibur:** объединить **канон Яндекса** + **читабельность как KPI** (острова смысла, lead, инфостиль) + **минимальный GEO-слой** (FAQ, schema, answer-first) в одном longread-эталоне (режим B), без agency-кейсов и без «генерации за минуты».

---

## 2. Яндекс Wordstat (MCP `user-mcp-kv`)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` в среде Cloud Agent **не подключён** (namespace недоступен). Вызов `wordstat_get_top_requests` для `как писать seo статьi` и secondary queries **не выполнен**. Точные показы в месяц **не получены** — в тексте статьи **нельзя** указывать частотность без повторного прогона Wordstat.

**Действие для команды:** подключить MCP и обновить токен при 401:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Семантика без цифр спроса (LSI из SERP + подсказки конкурентов, не Wordstat)

Использовать writer'у как кластер и подзаголовки; **после появления Wordstat** — сверить частоты и отсечь нерелевант:

| Группа | Фразы (LSI / long-tail) |
|--------|-------------------------|
| Core | как писать seo статьи, как написать seo статью, seo статья для сайта, seo текст для блога |
| Процесс | семантическое ядро, интент запроса, структура seo статьи, title description h1, внутренние ссылки |
| Качество | e-e-a-t, текстовая релевантность, lsi слова, переспам ключей, читабельность |
| GEO/AEO | geo оптимизация статьи, нейровыдача, faq schema, answer-first, ai выдача |
| Инструменты | яндекс вордстат, вебмастер, rich results test |

**SEO-стратегия (до Wordstat):** primary «как писать seo статьи» в H1/lead; secondary «seo текст для блога» — блок структуры шаблона; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одном материале», не подменять H1.

---

## 3. Таблица фактов (цифры только с URL; fact-bank.md по SEO пуст)

| # | Факт | Источник | Дата | Можно в текст |
|---|------|----------|------|---------------|
| 1 | Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 2 | H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 3 | Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 4 | Поисковые системы оценивают смысл и полезность, а не количество повторов ключей; переспам вреден | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 5 | Семантику подбирают в Яндекс Вордстат (частотность, формулировки, интент) | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 6 | Title и Description влияют на сниппет и кликабельность | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 7 | SEO-текст в 2026 — полезный текст, структура и словарь под запрос и его окружение, не «ключ через два абзаца» | [SEO школа — как писать SEO-текст](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| 8 | Рабочий каркас: собрать запросы → проанализировать TOP → структура → текст → Title/Description → проверка релевантности → контроль после публикации (7 шагов) | [SEO школа — как писать SEO-текст](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| 9 | Title — ориентир до 55–60 символов; основной запрос ближе к началу | [SEO школа — как писать SEO-текст](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| 10 | Description — ориентир до 140–160 символов, один ключ, выгода | [SEO школа — как писать SEO-текст](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| 11 | SEO-статья в TOP закрывает интент; прямой ответ — в первых ~100 словах | [Seotika — как писать SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 21.06.2026 | да |
| 12 | Один кластер запросов — одна страница; смешение информационного и коммерческого интента на одной URL размывает релевантность | [Seotika — как писать SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 21.06.2026 | да |
| 13 | Иерархия заголовков H1 → H2 → H3 без «перепрыгивания» уровней | [Seotika — как писать SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 21.06.2026 | да |
| 14 | Для блога: на первом экране — H1, вступление и ответ на вопрос **40–70 слов**; далее объяснение, таблица, пример, ошибки, чек-лист, FAQ | [ROI SEO — структура SEO-статьи для блога](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| 15 | Сбор семантики: 15–25 связанных фраз; отсечь запросы с другим намерением | [Divitio — SEO-текст пошагово](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| 16 | Главный ключ — H1, первый абзац, один раз ближе к концу; вспомогательные — по одному в H2 | [Divitio — SEO-текст пошагово](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| 17 | **25%** россиян ежедневно пользуются нейросетями; **17%** при поиске довольствуются ответом ИИ без кликов по ссылкам (медиа-материал click.ru) | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 17.06.2026 | да (как вторичный источник, не ВЦИОМ) |
| 18 | ИИ режет текст на чанки порядка **128–515 токенов** (~96–380 русских слов) для извлечения фактов | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 17.06.2026 | да |
| 19 | SEO, AEO и GEO — три слоя одной стратегии: SEO — индекс; AEO — ответы в выдаче с AI Overview/Алисой; GEO — видимость в автономных ИИ-чатах | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 17.06.2026 | да |
| 20 | Keyword stuffing в экспериментах GEO снижает visibility примерно на **10%** относительно baseline | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| 21 | Методы Cite Sources / Quotation / Statistics Addition в GEO-bench дают **+30–40%** visibility (Position-Adjusted Word Count) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |

**Не использовать без оговорки:** «1500–3000 слов» и «плотность 1–2%» (Seotika) как универсальная норма — противоречит канону Яндекса про отсутствие универсального объёма; можно упомянуть как **эвристику агентств**, не как правило. Кейсы «+140% за 3 недели», «статья за минуты на ИИ» — не verified.

**fact-bank.md:** релевантных SEO-фактов нет; цифры только из таблицы выше.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** one workflow **SEO + читабельность + минимальный GEO** — одна статья закрывает запрос человека и упакована для фрагментов в AI-выдаче. Фокус H1: **«которые читают люди»** = структура, lead, короткие абзацы, острова смысла, без переспама.

**Дифференциация:**
- Яндекс Direct — канон без GEO и без чек-листа 15+.
- Агентские гайды — перегруз кейсами и «плотностью ключей».
- GEO-лонгриды не учат писать текст с нуля.
- Excalibur B01 = **эталон longread** (8,5–9,5k знаков по quality-blog) с FAQ + schema handoff.

**H2-каркас (карточка B01 + research):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread (lead, H2/H3, таблицы, списки)  
3. FAQ и schema (JSON-LD вне body)  
4. Чеклист перед публикацией (15–20 пунктов)

**Tone:** практично, по-человечески; без корпоративной воды и эмодзи в article.html.

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи (40–60 слов) | Lead после H1 | «SEO-статья — …» |
| Определение GEO (40–60 слов) | H2 «SEO + GEO» | Generative Engine Optimization |
| Answer-first | Lead + каждый H2 | Первое предложение = тезис |
| FAQ 5–7 | Конец | Ответы-действия, 2–4 предложения |
| Schema | meta handoff | BlogPosting + FAQPage |
| Island test | QA | H2 понятен без соседних |
| llms.txt | упоминание | Опционально после sitemap/schema |
| Internal link | карточка | `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); ориентир — полнота ответа и медиана TOP; для how-to longread Excalibur — 8 500–9 500 знаков текста.  
2. **Что такое GEO в SEO?** — дополнение к SEO: структура и факты для цитирования в AI-ответах при сохранении индексируемого HTML.  
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + тематическая лексика (канон Яндекса; переспам вреден и в GEO-экспериментах).  
4. **Чем Title отличается от H1?** — Title для сниппета (~55–60 символов), H1 на странице; не дублировать слово в слово.  
5. **Какие schema нужны блогу?** — BlogPosting (или Article) + FAQPage для блока вопросов.  
6. **С чего начать семантику?** — Wordstat + подсказки + TOP-10; один кластер — одна URL.  
7. **Как проверить статью перед публикацией?** — чеклист: интент, структура, мета, alt, ссылки, FAQ, schema, читабельность.

---

## 7. Риски для writer

- Не выдумывать Wordstat-частоты до подключения MCP.  
- Не копировать структуру Seotika/Pikapuka 1:1.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Цифры — только из §3.  
- Без эмодзи в article.html.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантический кластер под один интент, спроектирует структуру longread с lead-ответом, напишет и оптимизирует черновик (Title, Description, заголовки, перелинковка), добавит FAQ и GEO-«острова смысла», пройдёт чек-лист перед публикацией и получит материал, который читают люди и могут процитировать AI-выдачи.

**action_outline:**

1. **Семантика:** в Wordstat (после доступа MCP) и подсказках собрать 15–25 фраз; выделить focus key и вопросы для FAQ; отсечь чужой интент.  
2. **Интент и SERP:** открыть TOP-10 по «как писать seo статьи»; зафиксировать тип страниц, медианную глубину, общие H2 конкурентов и пробелы.  
3. **Структура до текста:** один H1; 4–7 H2 из карточки + подвопросы; под каждым H2 — тезис в первом предложении; план таблицы/списка/FAQ.  
4. **Lead:** за 40–70 (до ~100) слов дать прямой ответ «как писать» и обещание результата (workflow + чек-лист).  
5. **Черновик тела:** короткие абзацы 3–5 строк; LSI естественно; E-E-A-T lite (автор, пример, ссылка на источник факта).  
6. **ТехSEO текста:** Title/Description, alt, URL; главный ключ в H1 и lead без переспама; внутренние ссылки на `/` и hub.  
7. **GEO-слой:** FAQ 5–7; атомарные блоки под чанки; исходящие ссылки на авторитетные источники цифр; handoff JSON-LD BlogPosting + FAQPage.  
8. **Финальный чек-лист:** интент закрыт, island test, мета, schema, нет воды/штампов, даты research актуальны.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (10) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (21) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| Режим B | ✅ |

**Writer:** готов с оговоркой по Wordstat (LSI из §2 до появления цифр). Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅ PASS
utility_verdict: PASS
summary: SERP (WebSearch 04.10.2026) — 10 URL: Яндекс Direct, SEO школа, Seotika, olegweb, 1ps, Pikapuka, articleai, meta-journal, ROI SEO, click.ru GEO. Wordstat MCP недоступен — LSI без показов. Угол — единый workflow SEO+читабельность+GEO longread, режим B. 21 факт с URL, 8 шагов action_outline, 7 FAQ. Готов к writer.
===
