# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + демонстрация формата на самой статье)  
**research_date:** 2026-10-05  
**disclaimer:** Все даты, версии и статистика проверены на 05.10.2026 (2026 год).

---

## Utility (Gate 1 + Gate 2)

**utility_verdict:** PASS  

**reader_outcome:** Читатель сможет пройти полный цикл — от выбора запроса и разбора SERP до черновика, мета-тегов, FAQ/schema и финального чек-листа — и опубликовать SEO-статью, которую дочитывают люди и которую могут процитировать нейропоиск, без переспама и «воды».

**action_outline (workflow для writer):**

1. Зафиксировать **primary query**, интент (how-to) и цель страницы; проверить спрос в [Яндекс Вордстат](https://wordstat.yandex.ru/) и подсказки в [Вебмастере](https://webmaster.yandex.ru/).
2. Разобрать **топ-5–10 URL** в выдаче: структура H2/H3, FAQ, медиа, пробелы; выписать 15–25 смежных запросов и LSI.
3. Собрать **каркас**: один H1, 4–7 H2 (каждый = подзадача + «делать / не делать»), H3 по необходимости; lead с прямым ответом в первых 2–3 предложениях.
4. Написать **черновик для людей**: абзацы 3–5 строк, списки, таблица сравнения SEO vs GEO; ключи и LSI — только естественно.
5. Добавить **E-E-A-T lite**: автор/редакция, дата, ссылки на первоисточники; без выдуманных процентов и кейсов.
6. Упаковать **GEO-слой** на том же тексте: атомарные H2-чанки, FAQ 5–7, answer-first в начале секций; BlogPosting + FAQPage (schema — отдельная роль).
7. Заполнить **Title / Description / alt**; внутренние ссылки; проверить мобильность и скорость.
8. Пройти **чек-лист 15–20 пунктов** перед публикацией и отправить URL на индексацию.

**utility_gate (тема):** PASS (`research-context.json`, `excalibur_blog_utility_gate.py --topic-id B01`).

---

## 1. SERP-обзор (WebSearch + research-serp.json, 05.10.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|-----------------|------------------|---------------|
| 1 | [direct.yandex.ru/.../seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | 5 шагов workflow; H1 один раз; нет «универсального объёма»; переспам вреден; Вордстат + Вебмастер; alt, мета, перелинковка | Нет GEO/нейропоиска; CTA Директа | Блоки про Директ; формальная иерархия H1–H4 без практики «островов смысла» |
| 2 | [articleai.ru/.../kak-napisat-seo-statyu-v-2026...](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Агентский how-to 2026 | Семантика → публикация; AI-выдача | Перегруз «нейросетями»; мало отличия от десятка клонов в SERP | Обещания «топ + ответы ИИ» без методики проверки |
| 3 | [pikapuka.com/.../polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Longread + чек-лист | E-E-A-T, Schema Article/FAQ, Title ~65 знаков | Кейсы с +% без первичника | 7-разделную структуру 1:1; непроверенные цифры трафика |
| 4 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Короткий гайд 2026 | «Полный ответ на одной странице»; поведенческий сигнал | Мало чек-листа и schema | «Просто следуй принципам» без шагов |
| 5 | [olegweb.ru/.../kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 2026 | 13 нумерованных шагов до индексации; WordPress | Длинный линейный список без GEO-слоя | Дублировать нумерацию 1:1 |
| 6 | [developers.google.com/.../creating-helpful-content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Канон Google | People-first, E-E-A-T, качество main content (Effort/Originality/Accuracy) | Не про Яндекс и RU-инструменты | Выдавать за «единственный чек-лист SEO» |
| 7 | [iq-maxima.ru/.../seo-statya-v-2026-godu-kak-pisat-pod-poisk-i-neyrovydaychu/](https://iq-maxima.ru/blog-iq/seo-statya-v-2026-godu-kak-pisat-pod-poisk-i-neyrovydaychu/) | SEO + нейровыдача | Явная связка поиск + AI | Agency tone | Sales-нарратив |
| 8 | [vc.ru/marketing/3102749-geo-optimizaciya...](https://vc.ru/marketing/3102749-geo-optimizatsiya-kak-prodvigat-sayt-v-neyrosetyah) | GEO-кластер (secondary intent) | Объясняет Generative Engine Optimization | Не учит писать текст с нуля | Путать GEO (generative) с локальной «гео-SEO» |

**Паттерн SERP (окт. 2026):** доминируют «полный гайд 2026» (семантика → структура → E-E-A-T → публикация). Отдельный кластер — GEO/нейровыдача. H1 «…которые читают люди» слабо занят; возможность — **читабельность + people-first** как явный SEO-фактор и **один workflow SEO+GEO** без второго проекта.

**Intent:** `how_to` — пошаговая система для блога/сайта. Secondary: «seo текст для блога», «geo оптимизация статьи» (упаковка того же longread для AI-цитирования).

---

## 2. Яндекс Wordstat (MCP `user-mcp-kv`)

⚠️ **WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` не подключён в среде Cloud Agent (инструмент `wordstat_get_top_requests` недоступен). **Точные показы в месяц не получены — цифры спроса в текст статьи не включать.**

При восстановлении MCP / токена — повторить вызов для:

- `как писать seo статьи` (primary)
- `seo текст для блога`, `geo оптимизация статьи` (secondary)

OAuth (если 401): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### LSI и смежные формулировки (из SERP + карточки темы, без оценки частотности)

**Для primary / H2–lead:** как написать seo статью, seo статья 2026, seo текст для сайта, seo копирайтинг, пошаговая инструкция seo статьи.

**Семантика и структура:** семантическое ядро, сбор ключевых слов, интент запроса, LSI, структура статьи h1 h2, title description, мета-теги, перелинковка, alt текст.

**Качество текста:** переспам ключей, полнота ответа, инфостиль, чек-лист перед публикацией, уникальность смысла (не «уникальность текста ради %»).

**GEO / AI (secondary):** geo оптимизация статьи, generative engine optimization, нейровыдача, faq для seo, schema faqpage, answer-first, фрагменты для ai.

**FAQ-кандидаты из intent (writer):** сколько символов в seo статье; что такое geo в seo; нужен ли переспам ключей; чем title отличается от h1; какие schema для блога.

---

## 3. Таблица фактов (≥15; цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику и запросы подбирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Нет универсальной «формулы плотности» ключей; важнее семантическое покрытие и полнота ответа | [Яндекс — ключевые фразы](https://yandex.ru/adv/edu/materials/direct-kak-podobrat-klyuchevye-frazy) | 17.03.2026 | да |
| Переспам и бессмысленные тексты — пример нарушений при SEO | [Яндекс — ключевые фразы](https://yandex.ru/adv/edu/materials/direct-kak-podobrat-klyuchevye-frazy) | 17.03.2026 | да |
| Google ранжирует контент, созданный **для людей**, а не для манипуляции выдачей | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 10.2026 | да |
| **Trust** — главный аспект E-E-A-T; E-E-A-T сам по себе не один «фактор ранжирования» | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 10.2026 | да |
| Google **не** задаёт предпочтительный word count для статей | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 10.2026 | да |
| Качество **main content** оценивают по Effort, Originality, Talent/skill, Accuracy | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 10.2026 | да |
| Контент, после которого пользователь **снова ищет** в Google, — сигнал низкой полезности (people-first vs search-first) | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 10.2026 | да |
| SEO допустим, когда помогает **обнаружить** people-first контент, а не подменяет его | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально на 10.2026 | да |
| Главная задача SEO-статьи — полный ответ на запрос; возврат в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| Title — ориентир ~65 знаков с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| H1 не дублирует Title — разные роли (страница vs сниппет) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Schema.org Article + FAQPage поддерживают сниппет и структуру вопросов | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| GEO (Generative Engine Optimization) — оптимизация видимости в ответах генеративных систем, не замена классического SEO | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Keyword stuffing в GEO-bench даёт **хуже baseline** (≈ −10% visibility) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Методы с источниками/цитатами/статистикой в GEO-bench дают **+30–40%** visibility (метрика PAWC) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |

**fact-bank.md:** прямых строк про SEO-письмо нет; для B01 опираться на таблицу выше. Строки fact-bank про ИИ-контент-завод **не** смешивать с how-to SEO-статьи без явной связи.

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «1500–3000 слов» / «плотность 1–2%» (Seotika — без первичника Google); «56% AI vs поиск» (LeadStream) в теле B01; любые **показы Wordstat** до успешного MCP.

---

## 4. Угол статьи (дифференциация, режим B)

**Главный угол:** одна SEO-статья 2026 = **longread для человека**, упакованный **одним проходом** под поиск и нейроцитирование: интент → каркас → инфостиль → FAQ/schema → чек-лист. Акцент H1 — **«которые читают люди»**: короткие абзацы, «острова смысла» в H2, answer-first, без переспама.

**Отличие от SERP:** Яндекс Direct — канон без GEO; GEO-гайды — без письма с нуля; агентства — кейсы и CTA. Excalibur B01 — **meta-гайд**: сам материал = образец (8 500–9 500 знаков, FAQ, schema handoff).

**H2-каркас (карточка + research):**

1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: lead, H1–H3, списки, таблицы
3. FAQ и schema (JSON-LD — вне body)
4. Чек-лист перед публикацией (15–20 пунктов)

**Tone:** практично, по-человечески; каждый H2 — подзадача + рекомендация «делать / не делать».

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи (40–60 слов) | Lead | «SEO-статья — …» |
| Определение GEO (40–60 слов) | Блок SEO+GEO | Generative Engine Optimization |
| Conversational H2 | По faq_hints | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 | Конец | Ответ 2–4 предложения, action |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA | Блок понятен без контекста |
| Schema | Handoff schema-роли | BlogPosting + FAQPage |
| Внутренняя ссылка | Карточка | `/` |
| cover_scene_hint | Cover | редактор, ноутбук, блокнот |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота vs SERP; для Excalibur how-to — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — дополнение: цитирование в AI-ответах при базе индексируемого structured контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; семантическое покрытие и естественные вхождения.
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 на странице.
5. **Какие schema нужны блогу?** — BlogPosting (или Article) + FAQPage.
6. **Как проверить статью перед публикацией?** — чек-лист из action_outline шаг 8.
7. **Можно ли писать SEO-статью только под роботов?** — нет (people-first; Google/Yandex акцент на пользу).

---

## 7. Риски для writer / GEO QA

- Без Wordstat MCP — **не** писать «X показов/мес» в Fact Check Box.
- Не копировать Pikapuka/olegweb структуру 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Цифры только из §3 или fact-bank после пополнения.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | ✅ PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (21) |
| utility_verdict + action_outline + reader_outcome | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅ PASS
utility_verdict: PASS
summary: SERP 8 URL (Яндекс Direct, articleai, Pikapuka, MaryProject, olegweb, Google Search Central, iq-maxima, vc.ru GEO). Wordstat MCP недоступен — LSI из SERP без показов. Угол — единый people-first workflow SEO+GEO longread, 8 шагов action_outline, 21 факт с URL. Готов к writer.
===
