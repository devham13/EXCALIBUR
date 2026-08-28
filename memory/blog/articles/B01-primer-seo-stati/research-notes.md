# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата на самой статье)  
**research_date:** 2026-08-28  
**disclaimer:** Все даты, версии и статистика проверены на 28.08.2026 (2026 год).

---

## 0. Utility gate

```text
python3 scripts/excalibur_blog_utility_gate.py --topic-id B01
→ topic B01: PASS
```

**utility_verdict:** PASS

**reader_outcome:** Читатель за один рабочий цикл соберёт семантику под один запрос, спроектирует структуру longread по ТОПу выдачи, напишет текст «для людей» с прямым ответом в первом экране, настроит Title/Description/H1, добавит FAQ и GEO-чанки для нейропоиска и пройдёт финальный чек-лист перед публикацией.

**action_outline (для writer):**

1. **Собрать семантику** — основной запрос + 5–20 смежных из Wordstat/подсказок; отсечь другой интент (инфо vs коммерция).
2. **Разобрать ТОП-10** — формат (гайд/каталог), медианный объём, повторяющиеся H2, таблицы, FAQ; зафиксировать пробелы.
3. **Составить каркас** — один H1, 4–8 H2 (каждый = подзадача + ответ), H3 для деталей; порядок «сначала ответ, потом нюансы».
4. **Написать черновик для человека** — lead 40–70 слов с прямым ответом; абзацы 3–5 строк; списки и таблицы вместо «полотна».
5. **Встроить SEO-слой** — ключ в H1, первом абзаце, 1–2 H2, Title/Description; LSI/синонимы без переспама.
6. **Добавить GEO-слой** — атомарные H2-блоки, FAQ 5–7 вопросов (ответ ≤80 слов), упоминание llms.txt как опции (не замена robots/sitemap).
7. **Подготовить мета и schema-handoff** — Title ≤60 символов, Description ≤160; BlogPosting + FAQPage (JSON-LD — отдельная роль schema).
8. **Проверить релевантность** — словарь темы vs ТОП; убрать воду и штампы; island test по каждому H2.
9. **Опубликовать и замерить** — переобход в Вебмастере/GSC; контроль позиций и поведения через 2–4 недели.

---

## 1. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` недоступен в текущей Cloud Agent-сессии (MCP не подключён). Инструмент `wordstat_get_top_requests` для `primary_query` «как писать seo статьи» вызвать не удалось.

**Что сделано вместо этого:** семантика и LSI восстановлены по WebSearch SERP (август 2026) + подсказки конкурентов. **Точные показы/мес по primary_query не утверждаем** — только после подключения Wordstat MCP или ручной проверки в Вордстате.

### Экспертная семантика (без цифр спроса — до Wordstat)

| Кластер | Фразы для writer |
|---------|------------------|
| Primary | как писать seo статьи, как написать seo статью, seo статья 2026 |
| LSI (контент) | seo текст для блога, seo копирайтинг, структура seo статьи, семантическое ядро, LSI, E-E-A-T |
| LSI (техника) | title description, h1 h2, перелинковка, alt-теги, текстовая релевантность |
| GEO/AEO | geo оптимизация статьи, нейровыдача, llms.txt, FAQ schema, прямой ответ в первых абзацах |
| PAA из SERP | сколько символов в seo статье; что такое geo в seo; можно ли писать seo текст с помощью ИИ |

*Смежные объёмы (сторонний Serpstat, UA-агентство, не primary): «seo тексты» ~390/мес, «seo копирайтинг» ~390/мес — [spilnoagency.com](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting), 2026. Использовать только как ориентир LSI, не как спрос по primary_query.*

---

## 2. SERP-обзор (WebSearch, 28.08.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|-----------------|------------------|---------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон: H1 один раз, H2–H4, естественные ключи, Wordstat, мета, перелинковка; примеры «плохо/хорошо» | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок про Директ; копировать H1–H4 без GEO |
| 2 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst) | Практик, 7 шагов (июль 2026) | Чёткий workflow: семантика → ТОП → структура → текст → мета → релевантность → контроль; чек-лист перед публикацией | Мало GEO; привязка к Seolity | 7 шагов 1:1; рекламу сервисов как «единственный путь» |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | GEO/AEO блок; первые 50 слов = прямой ответ; таблица SEO vs GEO; мета-элементы | Длинный, много про ИИ-генерацию | Непроверенные «+15–30% CTR» без первичника |
| 4 | [fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | Гайд 2026 | Плотность информации > длина; FAQ для ИИ; E-E-A-T; атомарные ответы | Agency tone | Шаблонные «мы №1» |
| 5 | [roiseo.ru/blog/struktura-seo-stati-dlya-bloga](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон структуры | Lead 40–70 слов; таблица «ошибка → проверка → решение»; FAQ для FAQPage | Узкий фокус на структуре, без семантики | Копировать таблицы дословно |
| 6 | [digitalrocket.ru/articles/llms-txt-2026-nuzhen-li-saytu](https://digitalrocket.ru/articles/llms-txt-2026-nuzhen-li-saytu/) | GEO/tech (2026) | Честная позиция: Google не использует llms.txt для ранжирования; приоритет — структура ответа, schema, E-E-A-T | Не про написание текста с нуля | Обещать рост AI-видимости только за llms.txt |
| 7 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский чек-лист | E-E-A-T, Schema Article+FAQPage, Title ~65 знаков | Кейсы с непроверяемыми % | «+140% трафика» и т.п. |

**Паттерн SERP (август 2026):** топ — «полный гайд 2026» с 5–9 шагами, E-E-A-T, Wordstat, чек-листом. Отдельный кластер — GEO/llms.txt. H1 «которые читают люди» в выдаче почти не занят — дифференциатор Excalibur.

**Intent:** `how_to` — пользователь хочет **пошаговую систему** (семантика → структура → текст → мета → проверка). Вторичный: связка **SEO + GEO** в одном материале, не два разрозненных проекта.

**Пробел для Excalibur:** единый workflow «читаемость для людей + упаковка для нейропоиска» с **чек-листом перед публикацией** и эталоном формата на самой статье B01 (режим B).

---

## 3. Таблица фактов (цифры только с URL)

| # | Факт | Источник | Дата | Можно в текст |
|---|------|----------|------|---------------|
| 1 | Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 2 | H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 3 | Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 4 | Семантику собирают в Яндекс Вордстат | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 5 | Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 6 | SEO-текст в 2026 — полезный текст, структура и словарь под конкретный запрос и его окружение | [SEO Школа — 7 шагов](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| 7 | Одна страница — один основной запрос + 5–20 дополнительных из одного смыслового кластера | [SEO Школа — 7 шагов](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| 8 | Title: до 55–60 символов; основной запрос ближе к началу; не дублировать H1 слово в слово | [SEO Школа — 7 шагов](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| 9 | Description: до 150–160 символов; конкретная польза; влияет на CTR сниппета | [SEO Школа — 7 шагов](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| 10 | Объём текста ориентируют на **медиану ТОП-10**, а не на абстрактные нормы | [SEO Школа — 7 шагов](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| 11 | Первые 3 результата выдачи получают около **55–60%** всех кликов | [Sostav — SEO 2026](https://www.sostav.ru/blogs/287906/82274) | 2026 | да |
| 12 | Более **70%** пользователей кликают по органической выдаче, игнорируя рекламу | [Sostav — SEO 2026](https://www.sostav.ru/blogs/287906/82274) | 2026 | да |
| 13 | Title — до **60–70** символов; Description — **150–160** символов | [Sostav — SEO 2026](https://www.sostav.ru/blogs/287906/82274) | 2026 | да |
| 14 | Средний объём контента в топ-10 по конкурентным запросам — **5000–10000+ слов** (лонгриды) | [Sostav — SEO 2026](https://www.sostav.ru/blogs/287906/82274) | 2026 | да (как ориентир SERP, не норма для всех тем) |
| 15 | E-E-A-T: Experience, Expertise, Authoritativeness, Trustworthiness — особенно для YMYL | [Sostav — SEO 2026](https://www.sostav.ru/blogs/287906/82274) | 2026 | да |
| 16 | Первый экран SEO-статьи для блога — ответ в **40–70 словах** | [ROI SEO — структура](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| 17 | Первые **30–50 слов** должны давать прямой ответ на главный запрос (без «в этой статье…») | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| 18 | H1 не должен совпадать с Title; Title влияет на CTR в выдаче | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| 19 | Google **не использует** llms.txt для ранжирования и AI Overviews (позиция Google, 2025–2026) | [Digital Rocket — llms.txt](https://digitalrocket.ru/articles/llms-txt-2026-nuzhen-li-saytu/) | 2026 | да |
| 20 | llms.txt предложен Jeremy Howard / Answer.AI в **сентябре 2024** | [Digital Rocket — llms.txt](https://digitalrocket.ru/articles/llms-txt-2026-nuzhen-li-saytu/) | 2026 | да |
| 21 | Для AI-видимости приоритетнее: прямой ответ в первых **80–120 словах**, schema Article/FAQPage, E-E-A-T, открытый robots.txt | [Digital Rocket — llms.txt](https://digitalrocket.ru/articles/llms-txt-2026-nuzhen-li-saytu/) | 2026 | да |
| 22 | Плотность информации важнее длины; ответ на запрос — как можно раньше | [FireSEO — SEO 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| 23 | Контент для ИИ: атомарные (самодостаточные) ответы; важную информацию не прятать во вкладки | [FireSEO — SEO 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |

**fact-bank.md:** записей по SEO-копирайтингу нет — использовать только таблицу выше.

**Не использовать без оговорки / первичника:** «Description +15–30% CTR» (1ps.ru); «+140% трафика» (Pikapuka); точные показы Wordstat по primary_query; «llms.txt обязателен для всех блогов».

---

## 4. Угол статьи (utility-only, дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чек-лист.

**Почему отличается от конкурентов:**
- Яндекс Direct — канон SEO без GEO-слоя.
- GEO-гайды (Digital Rocket, vc.ru) — про llms.txt/robots, но не учат писать текст с нуля.
- SEO Школа / 1ps — сильные step-by-step, но слабо раскрывают H1 «**которые читают люди**» как отдельный принцип (сканируемость, island test, инфостиль).

**Режим B:** сама статья B01 — **эталон**: 8 500–9 500 знаков текста, 5–7 FAQ, BlogPosting + FAQPage (schema — отдельная роль), атомарные H2, lead с определением.

**H2-каркас (из карточки + SERP):**
1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (handoff для schema-агента)
4. Чек-лист перед публикацией (15–20 пунктов)

**Подтемы внутри блоков:** Wordstat/кластер, Title/Description, E-E-A-T lite, llms.txt как опция, внутренняя перелинковка на `/`.

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead, 40–60 слов | «SEO-статья — …» |
| Определение GEO | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ hints из карточки | «Сколько символов…», «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец longread | Ответ 2–4 предложения, ≤80 слов |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA для writer | Блок понятен без соседних |
| llms.txt | GEO-блок | Опционально; Google не использует для ранжирования |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и медиана ТОП-10; для how-to longread Excalibur — 8 500–9 500 знаков текста.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI/тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (≤60 символов), H1 — на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage для блока вопросов.
6. **Нужен ли llms.txt блогу?** — опционально для AI-агентов разработки; не замена sitemap/robots; Google не использует для ранжирования.
7. **Как проверить статью перед публикацией?** — чек-лист: семантика, мета, структура, FAQ, schema-handoff, ссылки, читабельность.

---

## 7. Риски и blockers для writer

- Не выдумывать статистику Wordstat и CTR-кейсы.
- Не копировать структуру SEO Школы / Pikapuka 1:1.
- Объём текста: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Без эмодзи, без VPN/обход блокировок.
- Цифры только из таблицы фактов §3 или fact-bank.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate PASS | ✅ |
| SERP ≥ 3 конкурента (WebSearch) | ✅ |
| Wordstat MCP | ⚠️ недоступен — семантика по SERP |
| Таблица фактов ≥ 10 с URL | ✅ (23) |
| utility_verdict + action_outline | ✅ |
| GEO hooks + FAQ 5–7 | ✅ |
| H2 outline | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `memory/topics/blog-topics.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅
utility_verdict: PASS
wordstat: MCP user-mcp-kv недоступен — точные показы не получены
summary: SERP — 7 конкурентов (Яндекс Direct, SEO Школа, 1ps, FireSEO, ROI SEO, Digital Rocket, Pikapuka). Угол — единый how-to workflow SEO+GEO longread «для людей»: 9 шагов action_outline, 23 факта с URL, 7 FAQ. Wordstat — ⚠️ MCP offline. Готов к writer.
===
