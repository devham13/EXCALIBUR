# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to + чеклист; эталон формата на самой статье)  
**research_date:** 2026-07-10  
**disclaimer:** Все даты, версии и статистика проверены на 10.07.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Авторитет; 5 шагов от темы до публикации; Wordstat/Вебмастер; примеры «плохо/хорошо»; естественность ключей | Нет GEO/нейропоиска; CTA Директа; без универсального чек-листа перед публикацией | Коммерческий блок Директа; копировать H1–H4 1:1 |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Практик, 13 шагов (2026) | Интент → конкуренты → структура → WordPress → проверка; скриншоты, таблицы | Длинный, узко под WP; GEO как побочный эффект | 13-шаговую структуру 1:1 |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | Wordstat → кластер → «смысл, потом оптимизация»; примеры вхождений | Перегруз agency-тоном; ИИ как центр, не читабельность | Шаблонные формулировки agency |
| 4 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-…](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Longread + чек-лист 10 шагов | E-E-A-T, Schema Article+FAQ, Title ~65 знаков | Непроверенные кейсы «+140%»; GEO не отдельный слой | Проценты без источника |
| 5 | [gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi…](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | AI SEO 2026 | Answer-first 40–60 слов; факты каждые 150–200 слов; GEO vs keyword density | Мало про семантику/Wordstat для новичка | Длинный разогрев перед сутью |
| 6 | [trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii…](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | Чек-лист под ИИ (апр. 2026) | 10–15 вопросов в кластер; lead 100 слов; списки/таблицы; Schema | Уклон в услуги SEO; цифры «−20% трафика» — внутренняя аналитика автора | Коммерческий bias |
| 7 | [digitalrocket.ru/articles/podgotovka-sajta-k-ai-poisku-2026](https://digitalrocket.ru/articles/podgotovka-sajta-k-ai-poisku-2026/) | Техчек-лист AI-поиск | Article+FAQPage+HowTo; robots.txt для AI-ботов; Rich Results Test | Фокус на сайт, не на написание одной статьи | 30 техшагов без writer-workflow |
| 8 | [qvai.ru/media/kak-pisat-seo-stati](https://qvai.ru/media/kak-pisat-seo-stati) | Близкий H1-intent | Заголовок «которые читают люди»; структура, ключи | Короче и слабее по глубине и GEO | Thin content |

**Паттерн SERP (июль 2026):** топ — «полный гайд 2026» (1ps, pikapuka, seomatik, hozyindachi) + официальный Яндекс Direct. Отдельный кластер — GEO/нейропоиск (trigub, gracie, digitalrocket). **Пробел:** мало материалов, где **единый how-to** ведёт от Wordstat до публикации **и** сразу учитывает читабельность + GEO-чанки без agency-воды. H1 «которые читают люди» слабо раскрыт в топе.

**Intent:** `how_to` — пользователь хочет пошаговую систему: спрос → семантика → структура → текст → мета → FAQ/schema → проверка. Вторичный: связка SEO + GEO в одном материале (`seo текст для блога`, `geo оптимизация статьи`).

**Дифференциация Excalibur:** workflow «для людей и ИИ» за одну сессию; режим B — сама статья как эталон longread 8,5–9,5k знаков; чеклист 15–20 пунктов; без непроверенных кейсов агентств.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** Сервер MCP `user-mcp-kv` недоступен в среде Cloud Agent (не подключён в mcp.json). Инструмент `wordstat_get_top_requests` не вызван. **Точные показы в месяц не получены.** Обновите токен и подключение: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (без цифр спроса — только из SERP и карточки темы)

**Primary:** `как писать seo статьи`  
**Secondary (карточка):** `seo текст для блога`, `geo оптимизация статьи`

### LSI для writer (из SERP, подсказок и хвостов конкурентов)

| Кластер | LSI-фразы |
|---------|-----------|
| Действие | как написать seo статью, написание seo текстов, seo тексты 2026, подготовить seo текст |
| Структура | структура seo статьи, заголовки h1 h2, lead-абзац, чеклист seo статьи |
| Семантика | семантическое ядро, яндекс вордстат, ключевые слова, lsi слова, интент запроса |
| Мета | title description, метатеги, сниппет, meta title 60 символов |
| Качество | e-e-a-t, уникальность текста, переспам ключей, читабельность |
| GEO/ИИ | geo оптимизация статьи, нейропоиск, ai overviews, answer-first, schema faqpage |
| Техника | внутренняя перелинковка, alt изображений, микроразметка, blogposting |

**SEO-стратегия (без Wordstat-цифр):** primary в H1, lead и title; secondary — отдельные H2 или FAQ; LSI распределить по H2 без переспама; для GEO-блока — `geo оптимизация статьи`, `llms.txt` (с оговоркой об ограниченной пользе для поисковых ИИ).

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность; должны отличаться друг от друга и от H1 | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Description — уникальный, грамотный, без злоупотребления ключами; Яндекс может подставить другой текст в сниппет | [Яндекс — метатеги](https://yandex.ru/adv/edu/materials/chto-takoe-metategi) | 2026 | да |
| Title — ориентир 50–60 символов (до ~70); ключ в начале | [Brainbox — SEO-тексты](https://brainbox-marketing.ru/blog/kak-pisat-seo-teksty/) | 2025 | да |
| Meta description — ориентир 70–160 символов; влияет на CTR, не прямой фактор ранжирования | [slsew.ru — метатеги](https://slsew.ru/nevidimyj-fundament-seo-kak-zagolovki-i-metategi-vliyayut-na-poziczii-sajta/) | 2026 | да |
| Основной текст how-to — ориентир от 800 слов; уникальный, с LSI | [seohead.pro — метатеги](https://seohead.pro/blog/seo-optimizatsiya-kontenta-metategov-strategiya-ustoychivogo/) | 2026 | да |
| Главная задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| Для нейропоиска: прямой ответ в первых **40–120 словах** после H1/H2 | [gracie.digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| Кластер семантики: минимум **10–15** смежных вопросов из подсказок и «люди также спрашивают» | [trigub.ru — чек-лист ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 19.04.2026 | да |
| На статью — минимум один список и одна таблица или блок сравнения | [trigub.ru — чек-лист ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 19.04.2026 | да |
| JSON-LD Article + FAQPage (+ HowTo для инструкций) — базовая микроразметка для AI-поиска 2026 | [digitalrocket.ru — AI-поиск](https://digitalrocket.ru/articles/podgotovka-sajta-k-ai-poisku-2026/) | 2026 | да |
| Валидировать разметку в Google Rich Results Test и валидаторе Яндекса | [digitalrocket.ru — AI-поиск](https://digitalrocket.ru/articles/podgotovka-sajta-k-ai-poisku-2026/) | 2026 | да |
| GEO (Generative Engine Optimization): методы Cite Sources, Statistics Addition дают **+30–40%** visibility в Princeton GEO-bench | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Keyword stuffing в GEO-контексте хуже baseline (≈ **−10%**) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Ahrefs (май 2026): **97%** файлов llms.txt из ~38 000 валидных **не получили ни одного запроса** | [pressaff.com — Ahrefs llms.txt](https://pressaff.com/articles/97-of-files-llms-txt-we-havent-received-any-requests/) | 2026 | да |
| Джон Мюллер (Google): llms.txt «не для поиска», «временный костыль» для coding-инструментов | [pressaff.com — Ahrefs llms.txt](https://pressaff.com/articles/97-of-files-llms-txt-we-havent-received-any-requests/) | 2026 | да |
| llms.txt предложен Джереми Ховардом (Answer.AI) в сент. 2024 | [habr.com/ru/articles/1027740](https://habr.com/ru/articles/1027740/) | 2026 | да |
| Для AI-видимости приоритет: Schema.org + answer-first + robots.txt/sitemap, не llms.txt как «SEO-фактор» | [habr.com/ru/articles/1027740](https://habr.com/ru/articles/1027740/) | 2026 | да |
| Вордстат: фраза длиннее **8 слов** не обрабатывается; операторы `""` и `!` для точной частотности | [ashmanov.com — Wordstat](https://www.ashmanov.com/education/articles/kak-polzovatsya-yandeks-vordstat-instruktsiya-s-primerami/) | 2026 | да |

**fact-bank.md:** нет фактов по SEO-написанию — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); «−20% трафика без ИИ» (trigub — внутренняя аналитика); «llms.txt +30–60% видимости» (нет первичника для файла); цифры ВЦИОМ/Mediascope из agency-блогов без первичника.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Единый workflow за **60–90 минут**: интент → Wordstat-кластер → структура → текст (answer-first) → мета → FAQ/schema → GEO-чанки → чеклист перед публикацией.

**Почему отличается от конкурентов:**
- Яндекс Direct — канон без GEO и без финального чек-листа.
- GEO-гайды (trigub, digitalrocket) не учат писать текст с нуля.
- Agency-longread'ы (1ps, pikapuka) — вода и непроверенные кейсы.
- H1 «которые читают люди» — наш фокус: **читабельность как SEO-фактор** (короткие абзацы, острова смысла, без переспама).

**Режим B:** статья B01 — **эталон**: 8,5–9,5k знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (карточка + research):**
1. Зачем SEO и GEO в одной статье (один контент, две цели)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

**Подтемы внутри блоков:** Wordstat, Title/Description, E-E-A-T lite, llms.txt (опционально), внутренняя перелинковка.

---

## 5. Черновик чек-листа (15–20 пунктов для writer)

1. Проверить primary_query в Wordstat; собрать 10–15 смежных вопросов.  
2. Разобрать топ-5 SERP: интент, пробелы, что добавить.  
3. Составить outline: H1 → lead (ответ 40–120 слов) → 4–6 H2.  
4. H1 один; Title ≠ H1; Title ~50–60 символов с ключом.  
5. Description 70–160 символов, польза + мягкий CTA.  
6. После каждого H2 — прямой ответ в первых 2 предложениях.  
7. Абзацы 3–5 строк; минимум 1 список и 1 таблица.  
8. Ключи естественно: H1, lead, 1–2 H2, title/description — без переспама.  
9. LSI и тематические слова по тексту.  
10. Добавить личный опыт/пример (E-E-A-T lite).  
11. 3–5 внутренних ссылок по смыслу.  
12. Alt у изображений; файлы латиницей.  
13. FAQ 5–7 вопросов; ответы 2–4 предложения, actionable.  
14. JSON-LD BlogPosting + FAQPage (валидатор Google + Яндекс).  
15. GEO: атомарные чанки; факты со ссылками; llms.txt — опционально.  
16. Проверка орфографии, уникальности, мобильной вёрстки.  
17. datePublished / dateModified в schema = дата прогона.

---

## 6. FAQ-кандидаты (7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс Direct); ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при сохранении индексируемого структурированного контента.  
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + LSI; переспам вреден и для GEO (Princeton: −10%).  
4. **Чем Title отличается от H1?** — Title для сниппета (~50–60 символов), H1 — на странице; не дублировать.  
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage для блока вопросов.  
6. **Нужен ли llms.txt блогу?** — опционально; 97% файлов не получают запросов (Ahrefs, май 2026); приоритет — HTML + Schema + sitemap.  
7. **Как проверить статью перед публикацией?** — пройти чеклист раздела 5: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | По faq_hints | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец longread | Короткий actionable ответ |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` |
| Alt обложки | Cover | cover_scene_hint из карточки |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 8. Риски для writer

- Не выдумывать статистику; только таблица фактов §3.  
- Не копировать структуру Pikapuka/olegweb 1:1.  
- Объём: 8 500–9 500 знаков (`quality-blog.md`).  
- Без эмодзи в article.html.  
- Wordstat-цифры не писать до подключения MCP.  
- llms.txt — с оговоркой Ahrefs/Habr, не как обязательный SEO-фактор.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за одну сессию соберёт семантику в Wordstat, построит структуру SEO-статьи с answer-first lead, напишет читаемый текст с метатегами и FAQ, внедрит BlogPosting+FAQPage schema, пройдёт чеклист из 15–20 пунктов и опубликует материал, готовый и для поиска, и для цитирования в нейроответах.

**action_outline (how-to, 8 шагов):**

1. **Проверить спрос и интент:** ввести `как писать seo статьи` в Wordstat (оператор `""`); выписать 10–15 смежных вопросов; открыть топ-5 SERP и зафиксировать тип контента (гайд/чеклист).  
2. **Собрать семантический кластер:** primary + secondary (`seo текст для блога`, `geo оптимизация статьи`) + LSI из §2; сгруппировать по H2.  
3. **Составить структуру:** H1 с главным ключом; lead 40–120 слов с прямым ответом; 4–6 H2; план FAQ 5–7.  
4. **Написать черновик:** короткие абзацы 3–5 строк; после каждого H2 — тезис в первых 2 предложениях; список + таблица; E-E-A-T lite (пример/наблюдение).  
5. **Оптимизировать мета и ключи:** Title ~50–60 символов (≠ H1); Description 70–160; естественные вхождения в lead и 1–2 H2; без переспама.  
6. **Добавить FAQ и перелинковку:** 5–7 пар вопрос–ответ; 3–5 внутренних ссылок; alt у медиа.  
7. **Упаковать для GEO:** атомарные чанки; факты с URL; JSON-LD BlogPosting + FAQPage; валидаторы Google и Яндекса; llms.txt — только как опция.  
8. **Финальная проверка:** чеклист §5; орфография; уникальность; мобильная вёрстка; даты в schema.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (AUTH WARNING) |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| Чеклист 15–20 пунктов | ✅ |
| FAQ 5–7 | ✅ (7) |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `blog-topics.md` + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 конкурентов (Яндекс Direct, olegweb, 1ps, pikapuka, gracie, trigub, digitalrocket, qvai). Wordstat MCP недоступен (⚠️ AUTH WARNING). Угол — единый how-to SEO+GEO longread «для людей»: Wordstat → структура → answer-first → мета/FAQ/schema → чеклист 15–20. 22 факта с URL, 8 шагов action_outline, 7 FAQ. Готов к writer.
===
