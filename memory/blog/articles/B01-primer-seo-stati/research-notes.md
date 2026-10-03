# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата на самой статье)  
**research_date:** 2026-10-03  
**disclaimer:** Все даты, версии и статистика проверены на 03.10.2026 (2026 год).

**Utility gate темы:** PASS (`search_intent: how_to`, `article_mode: B`, `python3 scripts/excalibur_blog_utility_gate.py --topic-id B01`).

---

## 1. SERP-обзор (WebSearch, 03.10.2026)

Приоритет — живой WebSearch; `research-serp.json` использован как дополнение (6 запросов, 19 уникальных URL).

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон по SEO-тексту: семантика, Wordstat, H1–H4, вода/переспам, Title/Description, alt, ссылки; примеры «плохо/хорошо» | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок про Директ; копировать структуру 1:1 |
| 2 | [olegweb.ru/.../kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Практик, 13 шагов (2026) | Полный цикл до WordPress: интент, конкуренты, мета, чек перед публикацией | Длинный; GEO — вскользь | 13 H2 как зеркало без дифференциации |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-...](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread + ИИ (2026) | Семантика, LSI, постобработка ИИ, структура H2 | Уклон в «автоматизацию минутами» | Хайп про массовую генерацию без HITL |
| 4 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-...](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский гайд E-E-A-T | Чек-лист, Schema Article + FAQPage, Title ~65 знаков | Кейсы с непроверяемыми % | Agency tone и «+140% за 3 недели» |
| 5 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 7 шагов для новичков | Чёткий workflow: запросы → SERP → структура → контроль после публикации | Мало GEO; без универсального чек-листа 15+ | Слишком короткий финальный чек |
| 6 | [seotika.ru/kak-pisat-seo-stati](https://seotika.ru/kak-pisat-seo-stati/) | SEO-гайд | Lead «ответ в 100 словах», иерархия H2/H3, FAQ | Ориентир 1500–3000 слов и «плотность 1–2%» без первичника | Цифры плотности как жёсткое правило |
| 7 | [articleai.ru/blog/kak-napisat-seo-statyu-v-2026-...](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Инструкция 2026 | Семантика → публикация, AI-углы | Пересекается с 1ps/агентствами | Дублирующая 7-ступенчатая структура |
| 8 | [developers.google.com/search/docs/fundamentals/creating-helpful-content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Официальный Google | People-first, E-E-A-T, trust, YMYL; «why» контента | Не про русскоязычный Wordstat | Пересказ документа без практики |

**Паттерн SERP (2026):** доминируют «полный гайд 2026» (семантика → структура → текст → мета → E-E-A-T). Отдельный кластер — «SEO + ИИ». H1 «которые читают люди» слабо закрыт: конкуренты говорят про «людей и роботов», но редко связывают **читабельность** с **GEO-чанками** в одном workflow.

**Intent:** `how_to` — пошаговая система написания longread для блога с техникой (Title, FAQ, schema) и слоем GEO. Вторичные: `seo текст для блога`, `geo оптimизация статьи`.

**Пробел Excalibur:** единый **action-first** гайд «SEO + GEO в одной статье» с чек-листом 15–20 пунктов и демонстрацией формата на самой публикации B01 (режим B).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` / инструмент `wordstat_get_top_requests` **не подключён** в среде Cloud Agent на 2026-10-03 (namespace отсутствует в MCP-каталоге). Точные показы/мес **не получены** — в тексте статьи **не выдумывать** частотность.

При восстановлении MCP вызвать:

- `primary_query`: «как писать seo статьи»
- `secondary_queries`: «seo текст для блога», «geo оптимизация статьи»

Авторизация при 401: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### LSI и смежные формулировки (экспертная семантика без объёмов — до Wordstat)

| Кластер | Фразы для writer |
|---------|------------------|
| Ядро | как писать seo статьи, как написать seo статью, seo текст для блога |
| Структура | структура seo статьи, заголовки h1 h2 seo, seo longread |
| Техника | title description seo, meta description статья, внутренние ссылки seo |
| Качество | e-e-a-t seo текст, полезный контент seo, seo текст без переспама |
| GEO | geo оптимизация статьи, faq schema seo, нейропоиск статья 2026 |
| FAQ-intent | сколько символов в seo статье, что такое geo в seo |

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковые системы оценивают смысл и полезность, а не количество повторов ключей; переспам вреден | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику подбирают в Яндекс Вордстат (частотность и формулировки) | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-тексты без дополнительной ценности для пользователя (запросный спам, переоптимизация, скрытый текст) — нарушение для Яндекса | [Яндекс Вебмастер — SEO-тексты](https://yandex.ru/support/webmaster/ru/threat/seo-text) | актуально 2026 | да |
| Яндекс оценивает релевантность, полезность, оригинальность, удобство потребления контента (метрика качества страниц «Проксима» и др.) | [Яндекс — Качество поиска](https://yandex.ru/support/webmaster/ru/search-quality) | актуально 2026 | да |
| Сайт должен быть ориентирован на интересы пользователей, а не только на поисковые системы | [Яндекс — советы вебмастерам](https://yandex.ru/support/webmaster/yandex-indexing/webmaster-advice.html) | актуально 2026 | да |
| Основная суть документа должна быть понятна на первом экране; крупная логическая разбивка текста | [Яндекс — представление информации](https://yandex.ru/support/webmaster/ru/recommendations/presentation) | актуально 2026 | да |
| Контент создают **прежде всего для людей**; «why» — помочь посетителю, а не гнаться за роботами | [Google — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| E-E-A-T: **доверие (Trust)** — ключевой аспект; E-E-A-T сам по себе не один «фактор ранжирования», но используется mix сигналов | [Google — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| Для YMYL-тем Google усиливает требования к E-E-A-T | [Google — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| Качество **основного контента (main content)** критично; оцениваются Effort, Originality, Talent/skill, Accuracy | [Google — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) (обновление док., цит. [Search Engine Roundtable](https://www.seroundtable.com/google-helpful-content-main-content-and-eot-sa-42218.html)) | 2026 | да |
| Title — ориентир ≤60 символов; meta description — ориентир 140–160 символов (техчек перед публикацией) | [Spilno Agency — SEO copywriting 2026](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да* |
| SEO-статья в ТОП закрывает интент структурно; **прямой ответ в первых ~100 словах** повышает релевантность | [Seotika — SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да* |
| 7 мая 2026 Google **прекратил показ FAQ rich results** в SERP; тип **FAQPage** в Schema.org остаётся (важен для AI-видимости) | [ROI SEO — FAQPage](https://roiseo.ru/blog/razmetka-voprosov-otvetov-ii-poisk/) | 2026 | да |
| FAQPage JSON-LD должен **дословно совпадать** с видимым FAQ на странице | [artvision — Schema.org для GEO](https://artvision.pro/geo-optimizaciya/schema-org-dlya-nejrosetej/) | 2026 | да* |
| GEO (Generative Engine Optimization) — оптимизация под цитирование в ответах LLM; база — индексируемый структурированный контент | [Habr — GEO/AEO гайд](https://habr.com/ru/articles/987506/) | 2026 | да* |
| Answer-first: определения и ответы FAQ **до ~60–80 слов** — формат, удобный для извлечения в AI-ответы | [Habr — GEO/AEO](https://habr.com/ru/articles/987506/) | 2026 | да (как практический ориентир) |

\* Вторичный SEO-источник; для спорных цифр (объём 1500–3000 слов, «плотность 1–2%» у Seotika) — **не использовать** без cross-check.

**fact-bank.md:** фактов по SEO-писательству нет — опираться на таблицу выше.

**Не использовать:** «+140% трафика» (Pikapuka); «цитирование ×2,7» без первичного исследования; точные показы Wordstat (MCP недоступен).

---

## 4. Угол статьи (utility-only)

**Главный угол:** SEO-статья 2026 = **longread для человека**, который **в одном проходе** закрывает запрос, технику (мета, ссылки, schema) и **GEO-слой** (answer-first, FAQ, JSON-LD) — без отдельного «GEO-проекта».

**Дифференциация:**

- Яндекс Direct — канон SEO без GEO-hooks.
- Агентские гайды — E-E-A-T-кейсы и CTA.
- H1 карточки («**которые читают люди**») — фокус на инфостиле, «островах смысла» под passage/AI extraction.

**Режим B:** статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage (schema — отдельная роль), чек-лист 15–20 пунктов.

**H2-каркас (из `blog-topics.md` + SERP):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread (H1–H3, lead, списки, таблицы)  
3. FAQ и schema — зачем и как (JSON-LD вне body)  
4. Чеклист перед публикацией (15–20 пунктов)

**Tone:** практично, по-человечески; без корпоративной воды (site-brief).

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | Generative Engine Optimization |
| Conversational H2/FAQ | faq_hints | «Сколько символов…», «Что такое GEO в SEO?» |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; короткие абзацы |
| Island test | QA | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Даты | Метаданные | datePublished / dateModified = дата публикации |
| Internal link | Карточка B01 | `/` |
| cover_scene_hint | Cover | Редактор за ноутбуком, блокнот, тёплый свет |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при сохранении индексации и структуры.  
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + тематические слова (Яндекс/Google).  
4. **Чем Title отличается от H1?** — Title для сниппета (~≤60 симв.), H1 — на странице; не дублировать дословно.  
5. **Какие schema нужны блоговой SEO-статье?** — BlogPosting (или Article) + FAQPage для блока вопросов.  
6. **Нужен ли FAQ, если Google убрал FAQ-сниппеты?** — да для структуры и AI-видимости; rich results в SERP не гарантированы.  
7. **Как проверить статью перед публикацией?** — чек-лист: интент, семантика, мета, структура, FAQ/schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать Wordstat-частотность и «рынок %» без URL.  
- Не копировать 7/13-шаговые структуры конкурентов 1:1.  
- Объём текста: 8 500–9 500 знаков (`quality-blog.md`).  
- Минимум **5** нумерованных шагов в теле + чек-лист **15–20** пунктов.  
- Без эмодzi в `article.html`.  
- Цифры только из раздела 3 или `fact-bank.md`.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику и интент, спроектирует структуру longread с answer-first lead, напишет текст без переспама, оформит Title/Description и FAQ, подготовит handoff для BlogPosting + FAQPage и пройдёт чек-лист из 15–20 пунктов перед публикацией — с учётом GEO-слоя в той же статье.

**action_outline:**

1. **Зафиксировать запрос и интент:** primary «как писать seo статьи» + 5–10 смежных фраз (Wordstat/Вебмастер, когда доступны); определить тип intent (информационный how-to).  
2. **Разобрать ТОП-5 SERP:** формат, H2, таблицы/FAQ, пробелы; выписать must-have подтемы.  
3. **Собрать outline:** один H1, 4–6 H2 по карточке B01; под каждым H2 — тезис первым предложением; план FAQ 5–7.  
4. **Написать lead (100–150 слов):** прямой ответ «как писать SEO-статьи в 2026» + обещание результата (чек-лист/schema).  
5. **Написать основной текст:** короткие абзацы, списки, 1 таблица «SEO vs GEO» или «до/после»; ключи естественно; блок E-E-A-T lite (опыт, источники).  
6. **Добавить FAQ:** ответы 2–4 предложения, actionable; совпадение текста с будущим FAQPage JSON-LD.  
7. **Техника:** Title ≤60 симв., Description 140–160, alt, 3–5 внутренних ссылок (в т.ч. `/`), slug латиницей.  
8. **GEO-слой:** answer-first под H2, дата обновления, упоминание schema/FAQ для AI (без обещания сниппета).  
9. **Финальный чек-лист 15–20 пунктов** (island test, вода, переспам, мета, FAQ, schema handoff) — отметить перед publish.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (18) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + `research-serp.json` + карточка B01 в `memory/topics/blog-topics.md` + `memory/brief/site-brief.md`.
