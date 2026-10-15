# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата на самой статье)  
**research_date:** 2026-10-10  
**disclaimer:** Все даты, версии и статистика проверены на 10.10.2026 (Europe/Moscow).

---

## Utility (Gate 2)

**utility_verdict:** PASS  

**reader_outcome:** Читатель сможет пройти полный цикл — от сбора семантики в Вордстате до публикации SEO-longread с FAQ, schema и GEO-упаковкой «островов смысла», и проверить материал финальным чеклистом без переспама ключей.

**action_outline (workflow для writer):**

1. Зафиксировать **интент** (how_to) и **primary query** «как писать seo статьи»; выписать вторичные: «seo текст для блога», «geo оптимизация статьи».
2. Собрать **семантику** в [Яндекс Вордстат](https://wordstat.yandex.ru/) + подсказки из ТОП-SERP; кластеризовать запросы под будущие H2.
3. Разобрать **ТОП-5–7 конкурентов** (структура, пробелы, FAQ, schema); задать дифференциатор «для людей + GEO в одном материале».
4. Составить **каркас longread**: H1 (из карточки), 4 H2 из `blog-topics.md`, lead 40–60 слов с определением SEO-статьи; атомарные абзацы 3–5 строк.
5. Написать **тело**: инфостиль, LSI, списки/таблица, блок «SEO + GEO» (определение GEO, llms.txt, прямой ответ в начале разделов).
6. Добавить **FAQ 5–7** пар (ответы-действия) + handoff на BlogPosting + FAQPage (schema — отдельная роль).
7. Настроить **мета**: Title ~55–65 знаков (≠ H1), Description 150–160 знаков; alt у изображений; 2–4 осмысленные внутренние ссылки.
8. Прогнать **чеклист 15–20 пунктов** перед публикацией (семантика, читабельность, ссылки, schema, GEO-чанки).

---

## Яндекс Wordstat (MCP)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` / инструмент `wordstat_get_top_requests` **недоступен** в среде Cloud Agent (namespace не подключён). Точные **показы в месяц** не получены — **цифры спроса в таблицу ниже не вносить**. После подключения MCP повторить вызов для: `как писать seo статьи`, `seo текст для блога`, `geo оптимизация статьи`.

**Ссылка на обновление OAuth (при 401):** https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**LSI / смежные формулировки (из SERP 10.10.2026 и live-страниц, без оценки частотности):**

| Фраза (кандидат) | Откуда | Назначение в тексте |
|------------------|--------|---------------------|
| как написать seo статью / seo статья 2026 | SERP primary | синоним primary, Title/H2 |
| seo копирайтинг | articleai.ru | LSI в блоке написания |
| семантическое ядро, wordstat | Яндекс Direct, Pikapuka | шаг 2 workflow |
| title, description, мета-теги | конкуренты, Яндекс Direct | техблок |
| e-e-a-t / экспертный контент | Pikapuka, Google RU | доверие, автор |
| schema.org Article / FAQPage | Pikapuka, articleai | FAQ + schema handoff |
| внутренняя перелинковка, ЧПУ | Pikapuka, articleai | техоптимизация |
| geo / generative engine optimization | pawetta.com, SERP secondary | H2 «SEO + GEO» |
| llms.txt, AI-боты robots.txt | pawetta.com | GEO-hooks |
| инфостиль, главред | Pikapuka | «читают люди» |
| featured snippet / AI-ответы | Pikapuka | мотивация структуры |

---

## SERP-обзор (2026-10-10)

Источники: `research-serp.json` (preflight) + live fetch (articleai.ru, pikapuka.com, direct.yandex.ru, maryproject.ru, pawetta.com). WebSearch Cursor на момент research вернул ошибку — приоритет у JSON + WebFetch.

**Primary «как писать seo статьи 2026» — повторяющиеся домены:** 1ps.ru, articleai.ru, pikapuka.com, maryproject.ru, iskr.ai, iq-maxima.ru, serpjet.ru, seo-prodvizhenie-biznesa.ru.

**Secondary «geo оптимизация статьи 2026»:** digitalrocket.ru, leadstream.marketing, aksanov.digital, spat.by, vc.ru, pawetta.com — отдельный кластер GEO-гайдов.

| # | URL | Тип | Сильные стороны | Пробелы / слабости | Не копировать |
|---|-----|-----|-----------------|-------------------|---------------|
| 1 | [direct.yandex.ru/.../seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | 5 шагов workflow; нет универсального объёма; H1–H4; Wordstat; переспам вреден; абзацы 3–5 строк; Title/Description | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок про Рекламу; клон структуры без GEO |
| 2 | [articleai.ru/.../poshagovaya-instruktsiya](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | SaaS-блог (17.08.2026) | Полный цикл семантика→публикация; интент; LSI; мета; Schema Article; мониторинг GSC/Вебмастер | Жёсткие «2–4% плотности», «ВЧ от 10k» без первичника; перегруз метриками | Непроверенные пороги частотности; формула «70% успеха на подготовке» |
| 3 | [pikapuka.com/.../e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (2026) | Wordstat/Serpstat; H1≠Title; ~65 знаков Title; E-E-A-T; Featured Snippet; чек-лист | Кейс «+140% за 3 недели» без аудита | Проценты кейсов; 7-разделная структура 1:1 |
| 4 | [maryproject.ru/.../kak-pravilno-pisat-stati-pod-seo](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Агентство (обнов. 10.10.2026) | Полный ответ на одной странице; LSI/хвосты; структура; антипереспам | Мало пошаговики, FAQ, schema, GEO | Общие принципы без чеклиста |
| 5 | [pawetta.com/blog/geo-optimizaciya](https://pawetta.com/blog/geo-optimizaciya/) | GEO-практик (11.07.2026) | GEO на SEO; llms.txt; robots для AI-ботов; «ответ в первых 2–3 предложениях» | Фокус GEO, не обучение писать с нуля | Кейсовые цифры pawetta без верификации в fact-bank |
| 6 | [1ps.ru/.../seo-tekstyi-2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | SEO-медиа | ИИ в цикле, E-E-A-T, семантика | Пересечение с articleai/pikapuka | AI-hype без actionable отличий |

**Intent:** `how_to` — пошаговая система «семантика → структура → текст → техника → GEO-слой → проверка». Вторичный: связать **SEO-текст для блога** и **GEO оптимизацию статьи** без двух отдельных проектов.

**Дифференциация Excalibur B01:** H1 «**которые читают люди**» слабо закрыт в SERP (meta-journal.ru / dzen — поверхностно). Угол: **читабельность как SEO-фактор** (инфостиль, острова смысла, lead) + единый workflow SEO+GEO + режим B (сама статья = эталон 8 500–9 500 знаков).

---

## Таблица фактов (только с URL; fact-bank без SEO-тем — опора на первичные/официальные)

| # | Факт | Источник | Дата | В текст |
|---|------|----------|------|---------|
| 1 | Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 2 | H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 3 | Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 4 | Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 5 | Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 6 | Title и Description влияют на сниппет и кликабельность | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 7 | Главная задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [MaryProject](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 10.10.2026 | да |
| 8 | H1 должен отличаться от Title; Title — ориентир ~65 знаков с ключом и триггером | [Pikapuka](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| 9 | Микроразметка Schema.org типов Article и FAQPage улучшает сниппет | [Pikapuka](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| 10 | Google ранжирует people-first контент: полезные материалы для людей (self-assessment) | [Google Search Central RU](https://developers.google.com/search/docs/fundamentals/creating-helpful-content?hl=ru) | актуально 2026 | да |
| 11 | GEO (Generative Engine Optimization) — оптимизация под цитирование в ответах нейросетей | [Pawetta — GEO](https://pawetta.com/blog/geo-optimizaciya/) | 11.07.2026 | да |
| 12 | GEO опирается на SEO: нейросети берут страницы из обычной выдачи — без топа нечего цитировать | [Pawetta — GEO](https://pawetta.com/blog/geo-optimizaciya/) | 11.07.2026 | да |
| 13 | Для GEO: прямой ответ в первых 2–3 предложениях раздела; структура «вопрос — ответ» | [Pawetta — GEO](https://pawetta.com/blog/geo-optimizaciya/) | 11.07.2026 | да* |
| 14 | Уникальность текста перед публикацией — ориентир ≥90% (сервисы проверки) | [ArticleAI](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | 17.08.2026 | да* |
| 15 | Description — ориентир 150–160 символов с пользой для клика | [ArticleAI](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | 17.08.2026 | да* |

\* Вторичный SEO-блог — использовать как практический ориентир, не как статистику рынка.

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); пороги «ВЧ 10 000+» / «плотность 2–4%» без первичника (ArticleAI); «~40% эффекта» от lead-абзаца (Pawetta) без исследования; цифры из `fact-bank.md` про контент-заводы — **вне темы B01**.

---

## Угол и H2-каркас (карточка B01 + research)

**Главный угол:** одна SEO-статья 2026 = **longread для человека**, упакованный для классического поиска **и** нейровыдачи (GEO-чанки, FAQ, schema).

**H2 (верхний уровень):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread (H1–H3, lead, списки, таблицы)  
3. FAQ и schema (JSON-LD вне body)  
4. Чеклист перед публикацией (15–20 пунктов)

**Подтемы внутри блоков:** Wordstat/интент, Title/Description, инфостиль, E-E-A-T lite, llms.txt, перелинковка на `/`.

**Режим B:** объём текста **8 500–9 500 знаков**; 5–7 FAQ; cover_scene_hint: редактор за ноутбуком.

---

## GEO hooks (writer / schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead после H1 | 40–60 слов |
| Определение GEO | H2 «SEO + GEO» | 40–60 слов |
| Conversational подзаголовки | Внутри H2 | «Сколько символов…», «Что такое GEO…» |
| FAQ | Конец | 2–4 предложения, действие |
| Атомарные H2 | Везде | 1-й абзац = тезис |
| Island test | QA | Блок понятен отдельно |
| datePublished / dateModified | meta | 2026-10-10 |

---

## FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс Direct); для how-to в Excalibur — 8 500–9 500 знаков при полноте ответа.  
2. **Что такое GEO в SEO?** — слой поверх SEO: цитирование в AI-ответах при индексируемом structured-контенте.  
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + LSI (Яндекс Direct, MaryProject).  
4. **Чем Title отличается от H1?** — Title для сниппета (~55–65 знаков), H1 на странице; не дублировать.  
5. **Какие schema для блога?** — BlogPosting/Article + FAQPage.  
6. **Зачем llms.txt?** — сигнал для AI-краулеров; дополнение к sitemap, не замена SEO.  
7. **Как проверить перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## Риски для writer

- Цифры спроса Wordstat — **только после MCP**; сейчас не утверждать показы.  
- Не клонировать Pikapuka/ArticleAI структурой 1:1.  
- Без эмодзи; CTA ≤ 3; внутренняя ссылка на `/` из карточки.  
- `site_url` example.com — плейсхолдер или `/`.

---

## Готовность к writer

| Критерий | Статус |
|----------|--------|
| utility_verdict + action_outline | ✅ |
| SERP ≥ 3 конкурента | ✅ |
| Факты с URL (≥10) | ✅ |
| Wordstat MCP | ⚠️ недоступен |
| GEO hooks + FAQ | ✅ |
| Режим B | ✅ |

**Writer:** вход — этот файл, `research-context.json`, `research-serp.json`, карточка B01, `memory/brief/site-brief.md`.
