# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-10-13  
**disclaimer:** Все даты, версии и статистика проверены на 13.10.2026 (2026 год).

---

## Utility (Gate 2)

**utility_verdict:** PASS  

**reader_outcome:** Читатель сможет от запроса до публикации пройти единый workflow: интент и семантика → структура longread → черновик «для людей» → мета и перелинковка → FAQ/schema и GEO-чанки → финальный чеклист перед выкладкой.

**action_outline:**

1. Зафиксировать primary query и интент (информационный how-to); проверить спрос в Wordstat и подсказках SERP.
2. Разобрать топ-5–10 страниц выдачи: формат, глубина, FAQ, schema; выписать пробелы (читабельность + GEO в одном материале).
3. Собрать семантику: focus key, LSI, вопросы пользователей → кластер одной статьи; карта «запрос → H2/FAQ».
4. Составить структуру до текста: один H1, 4–7 H2, lead с прямым ответом в первых ~100 словах; после каждого H2 — содержательный абзац.
5. Написать черновик для человека: короткие абзацы (3–5 строк), списки, таблицы, примеры; ключи естественно, без переспама.
6. Добавить E-E-A-T lite: автор, факты со ссылками, свой опыт или мини-кейс; внутренние ссылки на смежные материалы.
7. Оформить Title (~60–70 знаков), Description (140–170), alt у изображений; H1 не дублирует Title слово в слово.
8. Собрать FAQ (5–7 пар) + JSON-LD BlogPosting и FAQPage; GEO-слой: атомарные «острова смысла», упоминание llms.txt при необходимости.
9. Пройти чеклист перед публикацией: интент закрыт, мета, schema, ссылки, мобильная читаемость, fact-check цифр.

---

## 1. SERP-обзор (WebSearch, 13.10.2026 + research-serp.json)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Авторитет; workflow тема → семантика → структура → текст → оптимизация; абзацы 3–5 строк; Wordstat/Вебмастер; anti-spam | Нет GEO/нейропоиска; CTA Директа | Блок про Директ как основной CTA |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 | «Сначала смысл, потом оптимизация»; H2 = подтема кластера; ИИ как инструмент | Длинный sales-narrative; мало про «читают люди» | Копировать структуру 1:1 |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-…](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский гайд 2026 | E-E-A-T, чек-лист, Schema Article + FAQPage, Title ~65 знаков | Непроверенные % в кейсах | Кейсовые цифры без источника |
| 4 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 2026 | 13 шагов от интента до индексации; WordPress-практика | Узкий фокус на WP; нет GEO-слоя | Дублировать 13 H2 как каркас статьи |
| 5 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Гайд для новичков 2026 | 7 шагов + чек-лист; «структура до текста» | Мало schema/GEO | — |
| 6 | [articleai.ru/blog/kak-napisat-seo-statyu-v-2026-…](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | SEO+GEO workflow 2026 | FAQ, schema, чеклист 18 пунктов (по SERP) | Продуктовый уклон | — |
| 7 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Короткий принцип | «Полный ответ на одной странице»; поведенческий сигнал | Мало actionable шагов | Вода «просто следуй принципам» |
| 8 | [meta-journal.ru/2026/06/19/primer-seo-stati/](https://www.meta-journal.ru/2026/06/19/primer-seo-stati/) | Близкий H1-intent | «Которые читают люди» в заголовке | Уклон в автоматизацию/промты | Обещания «статья за минуты» |

**Паттерн SERP (окт. 2026):** доминируют «полный гайд 2026» с семантикой, E-E-A-T, чек-листами и блоками про ИИ. Отдельный кластер — GEO/нейровыдача. H1 «которые читают люди» встречается редко; дифференциатор — **читабельность + один workflow SEO+GEO**, без «ключи ради ключей».

**Intent:** `how_to` — пошаговая система от семантики до публикации. Вторичный: связать **seo текст для блога** и **geo оптимизация статьи** в одном longread, не двумя статьями.

**Источники SERP:** Cursor WebSearch (13.10.2026); `research-serp.json` (preflight, 20 unique URLs) — сверено, актуально.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` / инструмент `wordstat_get_top_requests` **не подключены** в runtime Cloud Agent (отсутствуют в MCP catalog). Точные **показы в месяц не получены** — цифры спроса в текст статьи **не выдумывать**.

При восстановлении MCP — повторить вызовы для:

| Запрос | Назначение |
|--------|------------|
| как писать seo статьи | primary_query |
| seo текст для блога | secondary_1 |
| geo оптимизация статьи | secondary_2 |

**LSI для writer (из SERP + secondary, без частотности):**

- как написать seo статью, seo текст для сайта, seo копирайтинг, семантическое ядро, интент запроса  
- структура seo статьи, title description h1, перелинковка, e-e-a-t  
- seo статья 2026, нейровыдача, faq schema, llms.txt, geo в seo  

*Если позже API вернёт 401:* зафиксировать `⚠️ WORDSTAT AUTH WARNING` и [OAuth Яндекс](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40).

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата источника | Можно в текст |
|------|----------|----------------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции в выдаче | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title — практический ориентир ~60 знаков в десктопной выдаче | [SEO Writer — seo-tekst](https://ai-seowriter.ru/blog/seo-tekst) | 2026 | да |
| Description — ориентир 140–170 символов, без дословного дубля Title | [rahvalskiy.team — seo-текст](https://rahvalskiy.team/blog/kak-napisat-seo-tekst) | 2026 | да |
| H1 может отличаться от Title; не противоречить ему | [rahvalskiy.team — seo-текст](https://rahvalskiy.team/blog/kak-napisat-seo-tekst) | 2026 | да |
| SEO-статья: сначала спрос и задача страницы, потом текст, потом оптимизация | [hardkod.ru — seo-текст](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | 2026 | да |
| Вводный абзац — прямой ответ в первых 2–3 предложениях (релевантность и удержание) | [Seotika — seo-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| Иерархия заголовков H1 → H2 → H3 без пропуска уровней | [Seotika — seo-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| Google: контент создавать **для людей**, не ради манипуляции выдачей; E-E-A-T, trust — ключевой аспект | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 10.2026 | да |
| Google (окт. 2026): качество **main content** — Effort, Originality, Talent/skill, Accuracy (EOT/SA) | [Search Engine Roundtable](https://www.seroundtable.com/google-helpful-content-main-content-and-eot-sa-42218.html) | 10.2026 | да |
| AI-контент: обязательна ручная проверка фактов перед публикацией | [Google — AI content guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) (обновление отмечено 01.10.2026) | 10.2026 | да |
| GEO — дополнение SEO: цитирование в AI-ответах при базе индексируемого контента | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Нейросети извлекают passages; каждый H2 = «остров смысла» | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Первые ~100–150 слов — зона извлечения ответа для AI | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| llms.txt — предложен Jeremy Howard / Answer.AI (сент. 2024) | [Digital Impuls — GEO](https://digitalimpuls.ru/blog/geo-optimization-2026/) | 2026 | да |
| Главная задача статьи — полный ответ; возврат в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| Schema.org: Article/BlogPosting + FAQPage для блока вопросов | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «1,5–2× цитирование от schema» без первичника; «плотность ключей 1–2%» как универсальное правило (Seotika — только с оговоркой «ориентир агентства»); любые показы Wordstat без API.

**fact-bank.md:** прямых фактов по SEO-writing нет; таблица выше — для B01. Цифры из fact-bank про контент-заводы — **не смешивать** с этой статьёй без явной связи.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Отличие от SERP:**

- Яндекс — канон без GEO; GEO-гайды не учат писать с нуля.
- Агентские лонгриды — перегруз кейсами и CTA.
- H1 «которые читают люди» слабо раскрыт у конкурентов → фокус на **читабельность как SEO-фактор** (структура, lead, острова смысла) + техника.

**Режим B:** сама B01 — **эталон** формата: ~8,5–9,5k знаков, 5–7 FAQ, BlogPosting + FAQPage, перелинковка на `/`.

**H2-каркас (карточка + research):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как (JSON-LD вне body)  
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer / schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок SEO+GEO | «GEO — …» |
| Conversational H2 | FAQ-заготовки | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 | Конец | Ответ 2–4 предложения, действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema | meta/handoff | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Зачем блогу |
| internal_links | из карточки | `/` |

**Ключевые формулировки:** как писать seo статьи, seo текст для блога, geo оптимизация статьи.

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков текста.  
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.  
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (~60–70 знаков), H1 на странице; не дублировать дословно.  
5. **Какие schema для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.  
6. **Что такое llms.txt?** — сигнал для AI-краулеров; не замена sitemap.  
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Цифры только из §3; Wordstat — после подключения MCP.  
- Не копировать Pikapuka/olegweb структуру 1:1.  
- Объём 8 500–9 500 знаков (`shared/quality-blog.md`).  
- Без эмодзи; CTA ≤ 3.  
- `article.html` в этой сессии **не переписывать** — только writer по handoff.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента | ✅ |
| utility_verdict + action_outline | ✅ |
| Таблица фактов с URL | ✅ |
| Wordstat (точные показы) | ⚠️ MCP недоступен |
| GEO hooks + FAQ | ✅ |

**Writer:** вход — этот файл + `research-context.json` + `blog-topics.md` (B01) + `site-brief.md`.
