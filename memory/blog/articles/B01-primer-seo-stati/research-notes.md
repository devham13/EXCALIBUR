# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата на самой статье)  
**research_date:** 2026-10-15  
**disclaimer:** Все даты, версии и статистика проверены на 2026-10-15 (2026 год).

---

## Utility gate (research)

- **utility_verdict:** PASS  
- **search_intent:** how_to  
- **article_mode:** B  

**reader_outcome:** Читатель сможет пройти полный цикл одной SEO-статьи: собрать семантику и разобрать ТОП, собрать структуру longread под людей, добавить GEO-слой (lead, FAQ, schema), заполнить мета и опубликовать по чек-листу без переспама ключей.

**action_outline (workflow для writer):**

1. Зафиксировать главный запрос и 5–15 LSI; отсечь запросы с другим интентом (Вордстат / подсказки Поиска).  
2. Разобрать ТОП-10: формат (гайд vs лендинг), глубина H2, пробелы, которые можно закрыть сильнее.  
3. Собрать каркас: один H1, 4–6 H2 из карточки темы + под-H3; lead с прямым ответом в первых 2–4 предложениях.  
4. Написать тело: абзацы 3–5 строк, списки/таблицы, естественные ключи + тематический словарь; блок «SEO + GEO в одной статье».  
5. Добавить FAQ 5–7 пар (короткие ответы-действия) и внутреннюю ссылку на `/`.  
6. Подготовить Title (~55–65 символов) и Description (~150–160), alt у изображений, отличие H1 от Title.  
7. Вынести BlogPosting + FAQPage в JSON-LD (не дублировать разметку в видимом HTML).  
8. Прогнать финальный чек-лист (семантика, мета, структура, FAQ/schema, ссылки, читабельность, доступ AI-краулеров).  

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` недоступен в среде Cloud Agent (namespace не подключён). Точные **показы в месяц** по фразе «как писать seo статьи» **не получены**. Обновите токен и перезапустите research:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Семантика без объёмов (SERP + secondary_queries, для LSI writer)

| Фраза / кластер | Роль в статье | Источник подбора |
|-----------------|---------------|------------------|
| как писать seo статьи | primary, H1/lead | карточка B01 |
| seo текст для блога | secondary, H2/LSI | карточка B01, SERP |
| geo оптимизация статьи | secondary, блок SEO+GEO | карточка B01, SERP |
| как написать seo статью | синоним primary | WebSearch/SERP окт. 2026 |
| seo копирайтинг 2026 | LSI | articleai.ru, 1ps.ru в SERP |
| семантическое ядро для статьи | LSI, шаг 1 | Яндекс Директ, seoshkola.com |
| e-e-a-t seo текст | LSI, доверие | Google Search Central |
| title description seo статья | LSI, техблок | marketingklub.ru, Яндекс Директ |
| faq schema seo статья | LSI, GEO-hooks | roiseo.ru, seo-akademiya.by |
| сколько символов в seo статье | FAQ (faq_hints) | карточка B01 |
| что такое geo в seo | FAQ (faq_hints) | карточка B01, GEO-кластер SERP |

**Таблица «Фраза | Показы/мес»** — заполнить после успешного `wordstat_get_top_requests` для primary и «seo текст для блога».

---

## SERP-обзор (WebSearch Cursor, 15.10.2026 + research-serp.json)

**Запросы:** «как писать seo статьи 2026», «Как писать SEO-статьи, которые читают люди 2026», «seo текст для блога 2026», «geo оптимизация статьи 2026».

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|-----------------|------------------|---------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: объём без нормы, H1 один, абзацы 3–5 строк, Вордстат, anti-spam, Title/Description | Нет GEO/нейропоиска; CTA Директа | Коммерческий хвост; структура 1:1 |
| 2 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Практик, 7 шагов (обн. 10.07.2026) | Чёткий цикл: запросы → ТОП → структура → текст → мета → QA → контроль | Мало GEO/schema; привязка к курсам | Продажу обучения как ядро |
| 3 | [articleai.ru/.../kak-napisat-seo-statyu-v-2026](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | AI+SEO гайд 2026 | Семантика → публикация, AI в цикле | Перегруз «ИИ вместо автора» | Обещания «топ и ответы ИИ» без процесса QA |
| 4 | [pikapuka.com/.../polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread | E-E-A-T, чек-лист, schema | Кейсы с % без первичника | Непроверенную статистику |
| 5 | [olegweb.ru/.../kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | WP-практик, 13 шагов | Интент, WordPress, мета, перелинковка | Длинная линейка шагов без GEO-слоя | 13 H2 «как есть» |
| 6 | [marketingklub.ru/kak-pisat-seo-stati](https://marketingklub.ru/kak-pisat-seo-stati/) | Инструкция + чек-лист | Иерархия H1–H3, Title 60–70, Description 150–160 | Слабый блок GEO | Жёсткие «5–10 H2» без контекста темы |
| 7 | [www.meta-journal.ru/2026/06/19/primer-seo-stati](https://www.meta-journal.ru/2026/06/19/primer-seo-stati/) | Совпадение с H1 бренда | Заголовок «которые читают люди» | Конкурирует с нашим slug/H1 | — |
| 8 | [roiseo.ru/blog/razmetka-voprosov-otvetov-ii-poisk](https://roiseo.ru/blog/razmetka-voprosov-otvetov-ii-poisk/) | Schema + GEO (30.07.2026) | FAQPage vs Article; отмена FAQ rich results 07.05.2026; краулеры | Не учит писать текст с нуля | Обещание FAQ-сниппета в Google |
| 9 | [developers.google.com/search/docs/fundamentals/creating-helpful-content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Официальный Google | People-first, E-E-A-T (trust), main content quality, anti AI-spam | Нет пошагового RU-чек-листа | Выдуманный «идеальный объём» |

**Паттерн SERP (окт. 2026):** доминируют «полный гайд 2026» (7–13 шагов), семантика, E-E-A-T, часть материалов — AI-конвейер. Отдельный кластер — GEO-оптимизация статьи (digitalrocket, leadstream, vc.ru). **Пробел:** мало материалов, где **читабельность longread** и **единый workflow SEO+GEO** (lead → атомарные H2 → FAQ/schema → чек-лист) без агентского sales и без «только ИИ».

**Intent:** how_to — собрать систему написания одной статьи. Вторичный: связать «seo текст для блога» с «geo оптимизация статьи» в одном материале (карточка B01).

**Сверка с fact-bank.md:** прямых фактов про SEO-копирайтинг в банке нет; для B01 опираемся на первичные источники ниже. Факты про AI-контент-завод из fact-bank в эту статью **не тащить** (другая тема).

---

## Таблица фактов (≥15, с URL)

| # | Факт | Источник | Дата | В текст |
|---|------|----------|------|---------|
| 1 | Универсального объёма SEO-статьи нет — зависит от темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 2 | H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 3 | Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 4 | Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 5 | Семантику собирают в Яндекс Вордстат (и смежные инструменты) | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 6 | Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 7 | SEO-текст в 2026: полнота ответа и тематический словарь важнее «ключ через абзац» | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| 8 | На одну страницу — группа близких запросов; разный интент («купить» vs «как выбрать») — разные URL | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| 9 | Title: ориентир 60–70 символов, ключ ближе к началу; Description: 150–160 символов | [Marketing Klub](https://marketingklub.ru/kak-pisat-seo-stati/) | 2026 | да |
| 10 | H2 обычно 5–10; ключи в 2–3 H2 без фанатизма; иерархия H1→H2→H3 без пропусков | [Marketing Klub](https://marketingklub.ru/kak-pisat-seo-stati/) | 2026 | да |
| 11 | E-E-A-T не отдельный «фактор ранжирования»; trust — центральный; контент для людей, не для манипуляции выдачей | [Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 15.10.2026 | да |
| 12 | Google: нет предпочтительного word count; писать объём ради мифа не нужно | [Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 15.10.2026 | да |
| 13 | Качество main content (effort, originality, skill, accuracy) — критично для оценки страницы | [Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 15.10.2026 | да |
| 14 | Массовая AI-генерация без oversight — low effort; AI-контент для манипуляции ранжированием — spam policy | [Google — AI content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 15.10.2026 | да |
| 15 | 7 мая 2026 Google прекратил FAQ rich results в выдаче; тип FAQPage в Schema.org остаётся | [ROI SEO / FAQ разметка](https://roiseo.ru/blog/razmetka-voprosov-otvetov-ii-poisk/) | 30.07.2026 | да |
| 16 | FAQPage уместен для видимых редакционных Q&A; текст JSON-LD должен совпадать с HTML | [ROI SEO](https://roiseo.ru/blog/razmetka-voprosov-otvetov-ii-poisk/) | 30.07.2026 | да |
| 17 | Для AI-поиска важнее индексируемость и доступ краулеров (Googlebot, OAI-SearchBot, PerplexityBot), чем «магия» схемы | [ROI SEO](https://roiseo.ru/blog/razmetka-voprosov-otvetov-ii-poisk/) | 30.07.2026 | да |
| 18 | GEO (Generative Engine Optimization) — оптимизация под цитирование в генеративных ответах; SEO остаётся базой индексации | [КлиентЛаб — GEO](https://klientlab.ru/blog/geo-optimizatsiya-sajta/) | 2026 | да |

**Не использовать:** «+140% трафика за 3 недели» и прочие % из агентских кейсов без первичника; Princeton GEO-bench +30–40% — только если writer ссылается на arxiv (см. B04), в B01 достаточно качественного GEO без цифр bench.

---

## Угол и дифференциация

**Главный угол:** SEO-статья 2026 = **longread для людей**, упакованный для поиска и нейровыдачи: один workflow «семантика → структура → текст → мета → FAQ/schema → чек-лист», акцент на **читабельность** (острова смысла, lead, FAQ) как часть SEO, не «набивка ключей».

**Отличие от SERP:**

- Яндекс Директ — канон SEO без GEO и без чек-листа Excalibur.  
- GEO-гайды — не учат писать статью с нуля.  
- AI-гайды — смещают фокус на генерацию без human QA.  
- H1 «которые читают люди» слабо раскрыт у конкурентов (кроме meta-journal.ru).

**Режим B:** статья B01 — эталон формата блога: ~8 500–9 500 знаков текста, 5–7 FAQ, BlogPosting + FAQPage в JSON-LD, 4 H2 из карточки + практика внутри блоков.

**H2-каркас (карточка B01):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread (H1–H3, lead, списки, таблицы)  
3. FAQ и schema (JSON-LD, синхрон с видимым FAQ)  
4. Чеклист перед публикацией (15–20 пунктов)

---

## GEO hooks (writer / schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead после H1 | 40–60 слов, прямой ответ |
| Определение GEO | H2 «SEO + GEO» | 40–60 слов |
| Conversational подзаголовки | Внутри H2 | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 | Перед CTA | Ответ 2–4 предложения, actionable |
| Атомарные H2 | Каждый раздел | Первое предложение = тезис |
| Schema | schema.jsonld | BlogPosting + FAQPage, author из registry |
| AI-краулеры | Чек-лист / GEO | robots.txt осознанно, не блокировать по умолчанию |
| llms.txt | Упоминание | Опционально, не замена sitemap |
| internal_links | `/` | из карточки |

---

## FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); ориентир — полнота vs ТОП; для how-to longread блога — ~8 500–9 500 знаков текста.  
2. **Что такое GEO в SEO?** — дополнение к SEO: цитирование в AI-ответах при индексируемом структурированном контенте.  
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + тематический словарь.  
4. **Чем Title отличается от H1?** — Title для сниппета (~55–65 символов), H1 на странице; не дублировать дословно.  
5. **Какие schema для статьи блога?** — BlogPosting (или Article) + FAQPage при видимом FAQ.  
6. **Нужен ли FAQPage после отмены FAQ-сниппетов Google?** — для Google rich FAQ нет с 07.05.2026; блок и разметка полезны для людей, Яндекса и AI-парсинга при совпадении с HTML.  
7. **Как проверить статью перед публикацией?** — чек-лист: интент, мета, H-структура, FAQ, schema, ссылки, факты, мобильность.

---

## Риски для writer

- Цифры спроса Wordstat — только после MCP; сейчас не выдумывать показы.  
- Не копировать 7- или 13-шаговые структуры конкурентов 1:1.  
- Без эмодзи; без VPN; CTA ≤ 3; длинное тире «—» и ёлочки — по site-brief.  
- Объём текста: 8 500–9 500 знаков (`shared/quality-blog.md`).

---

## Готовность

| Критерий | Статус |
|----------|--------|
| utility_verdict + action_outline | ✅ |
| SERP ≥ 3 (фактически 9) | ✅ |
| Факты с URL (18) | ✅ |
| Wordstat (точные показы) | ⚠️ MCP недоступен |
| GEO hooks + FAQ | ✅ |
| Writer-ready | ✅ |
