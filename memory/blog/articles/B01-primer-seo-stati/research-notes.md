# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to + чеклист)  
**research_date:** 2026-08-11  
**disclaimer:** Все даты, версии и статистика проверены на 2026-08-11 (2026 год).

---

## 1. SERP-обзор (WebSearch, август 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Авторитет; 5 шагов (тема → семантика → структура → текст → оптимизация); «плохо/хорошо»; естественность ключей; Wordstat/Вебмастер | Нет GEO-слоя; CTA Директа; без printable-чеклиста | Блок про Директ; дублировать канон без практики |
| 2 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист 9 критериев (июн. 2026) | E-E-A-T + ЭПОС; answer-first; AI Overviews / Алиса AI; FAQ только под реальные вопросы | Agency tone; нет единого workflow «с нуля до publish» | Переспам «уникальность 99%» как цель |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Кластеры 3–5 групп; правило «ответ сразу после H2»; LSI без насилия | Длинный sales-narrative; ИИ как центр, не human-first | Копировать 7-разделную структу1:1 |
| 4 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский гайд + чек-лист | E-E-A-T, Schema Article+FAQPage, Title ~65 знаков | Непроверенные кейсы «+140%»; перегруз agency | Непроверенные проценты в кейсах |
| 5 | [tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | Формула E-E-A-T (2026) | Интент vs ключи; 6-пунктовый pre-publish чек; форматы под intent | Мало техники (meta, schema, GEO) | Agency CTA в конце |
| 6 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 13 шагов до WordPress | Полный pipeline от ключа до индексации | Узко под WP; нет GEO-блока | 13 H2 как каркас 1:1 |
| 7 | [www.ashmanov.com/education/articles/geo-prodvizhenie-kak-popast-v-otvety-ii-a-ne-tolko-v-vydachu](https://www.ashmanov.com/education/articles/geo-prodvizhenie-kak-popast-v-otvety-ii-a-ne-tolko-v-vydachu/) | GEO + SEO (2025–2026) | GEO не заменяет SEO; фрагмент = одна мысль; YandexGPT/Алиса | Фокус на услуги Ashmanov | Sales-блоки агентства |
| 8 | [gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | H1-близкий угол «для людей и ИИ» | Баланс читабельности и AI-выдачи | Мало пошаговой семантики | Дублировать заголовок без дифференциации |

**Паттерн SERP:** топ — «полный гайд 2026» (1ps, pikapuka, seomatik, iq-maxima) + официальный Яндекс + чек-листы (texterra, tolk). Отдельный кластер — GEO-лонгриды. **H1 «которые читают люди»** слабо закрыт: конкуренты говорят про E-E-A-T, но редко дают **единый workflow SEO+GEO в одной инструкции с printable-чеклистом**.

**Intent:** `how_to` — пользователь хочет пошаговую систему: интент → семантика → структура → черновик → meta/FAQ/schema → GEO-упаковка → финальная проверка. Вторичный: «seo текст для блога», «geo оптимизация статьи».

**Пробел для Excalibur:** B2B-автоматизатор пишет **одну SEO-статью за сессию** по workflow A→B→C; акцент «читают люди» = answer-first + короткие абзацы + island test; GEO — слой поверх готового текста, не отдельный проект.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в среде Cloud Agent (доступны только Cursor Automation Tools, cursor-cloud). Точные объёмы показов **не получены** — цифры спроса в текст не включать.

**Запросы для ручного прогона в Wordstat (редактору):**
- `как писать seo статьи` (primary)
- `seo текст для блога` (secondary)
- `geo оптimizaciya статьи` (secondary)
- смежные: `как написать seo статью`, `seo копирайтинг`, `структура seo статьи`, `чеклист seo статьи`

### LSI для writer (экспертная оценка по SERP + secondary_queries, без цифр)

| Группа | LSI-фразы |
|--------|-----------|
| Процесс | как написать seo статью, пошаговая инструкция, алгоритм написания, техническое задание копирайтеру |
| Семантика | семантическое ядро, LSI-слова, кластер запросов, интент, Wordstat, поисковое намерение |
| Структура | структура статьи, H1 H2 H3, longread, lead-абзац, оглавление, списки и таблицы |
| Качество | E-E-A-T, ЭПОС, полезность, читабельность, вода, переспам, уникальность |
| Техника | title description, meta-теги, alt-текст, перелинковка, микроразметка, schema.org |
| GEO-слой | geo оптимизация статьи, AI-выдача, нейроответ, FAQ для ИИ, answer-first, BlogPosting FAQPage |
| Блог | seo текст для блога, контент-план, статья для сайта, публикация в WordPress |

**SEO-стратегия:** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блок про формат блога; «geo оптimizaciya статьи» — отдельный H2 (не путать с локальной geo-SEO).

---

## 3. Таблица фактов (15+ утверждений с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Пошаговый канон Яндекса: тема и конкуренты → семантика → структура → текст → оптимизация | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-текст 2026: тест «можно ли сослаться как на лучший ответ по вопросу» | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Google — E-E-A-T; Яндекс — ЭПОС (экспертность, полезность, оригинальность, содержательность) | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Базовый принцип 2026: сначала главный ответ, потом детали и нюансы | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Один абзац — одна микротема; водянистые блоки удалять | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Контент 2026 должен быть понятен классической выдаче и AI (Google AI Overviews, Алиса AI, ChatGPT, Perplexity) | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| FAQ нужен только под реальные вопросы пользователя, не для «раздувания» объёма | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Основной ключ — в H1 и первом абзаце; синонимы вместо повторов | [Tolk — формула 2026](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | 2026 | да |
| Title — ориентир ~60–70 символов; Description — ~150–160 символов | [DDSI — SEO-текст для начинающих](https://ddsi.ru/blog/kak-napisat-seo-tekst-polnoe-rukovodstvo-dlya-nachinayushhih/) | 2025 | да |
| После каждого H2 — сразу содержательный ответ, не «вода» перед сутью | [1ps.ru — гайд 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Семантику группируют в 3–5 смысловых кластеров под H2 | [1ps.ru — гайд 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| GEO (Generative Engine Optimization) — не замена SEO, а комплексный подход; ИИ цитирует авторитетные источники из топа | [Ashmanov — GEO-продвижение](https://www.ashmanov.com/education/articles/geo-prodvizhenie-kak-popast-v-otvety-ii-a-ne-tolko-v-vydachu/) | 2025–2026 | да |
| Каждый фрагмент текста для GEO — одна мысль или ответ на конкретный вопрос | [Ashmanov — GEO-продвижение](https://www.ashmanov.com/education/articles/geo-prodvizhenie-kak-popast-v-otvety-ii-a-ne-tolko-v-vydachu/) | 2025–2026 | да |
| Для Яндекс GPT: H2–H4, списки, таблицы, микроразметка Schema | [Ashmanov — GEO-продвижение](https://www.ashmanov.com/education/articles/geo-prodvizhenie-kak-popast-v-otvety-ii-a-ne-tolko-v-vydachu/) | 2025–2026 | да |
| Главная задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**fact-bank.md:** фактов по SEO-написанию нет — использовать только таблицу выше.

**Не использовать без проверки:** «+140% трафика за 3 недели» (Pikapuka); произвольные «N символов = топ»; цифры Wordstat без MCP.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один список ключей», а **единый workflow за одну рабочую сессию**: интент → семантика → структура → черновик → meta/FAQ/schema → GEO-чанки → чеклист перед публикацией.

**Почему отличается от конкурентов:**
- Яндекс даёт канон без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды перегружены E-E-A-T-кейсами и CTA.
- H1 «которые читают люди» — слабо раскрыт в SERP; наш фокус: **читабельность как SEO-фактор** (answer-first, island test, короткие абзацы) + техника.

**Режим B:** сама статья B01 — **эталон формата**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (один контент, два канала)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

**Tone (site-brief):** практичный B2B, без корпоративной воды; каждый H2 = подзадача + «делать / не делать».

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO — …» |
| Conversational H2 | FAQ-блок | «Сколько символов…», «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, action |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Internal link | Из карточки | `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптimizaciya статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~60–70 символов), H1 — на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Как проверить статью перед публикацией?** — пройти чеклист: семантика, meta, структура, FAQ, schema, ссылки, читабельность.
7. **Можно ли писать SEO-статью только нейросетью?** — черновик да; финал — фактчек, опыт, структура (Texterra).

---

## 7. Черновик чеклиста для writer (15–20 пунктов)

1. Интент определён по топ-5 SERP (информационный / коммерческий).
2. Семантика: primary + 5–10 LSI из кластера.
3. H1 один, с главным запросом; Title ≠ H1.
4. Lead-абзац отвечает на запрос в первых 2–3 предложениях.
5. После каждого H2 — прямой ответ, не «вода».
6. Абзацы 3–5 строк; списки/таблицы где уместно.
7. Ключ в H1, первом абзаце, 1–2 H2 — естественно.
8. Title ~60–70 символов; Description ~150–160.
9. Alt у изображений описывает картинку, не ключи.
10. 3–5 внутренних ссылок по смыслу.
11. FAQ 5–7 реальных вопросов (не дубль H2).
12. JSON-LD BlogPosting + FAQPage (schema-агент).
13. Дата публикации/обновления видна или в meta.
14. Island test: каждый H2 самодостаточен.
15. GEO: answer-first в начале; фрагмент = одна мысль.
16. Нет переспама и шаблонных фраз («в современном мире»).
17. Орфография и факты проверены; цифры только с URL.
18. Pre-publish: «можно ли сослаться как на лучший ответ?» (Texterra-тест).

---

## 8. Риски для writer

- Не выдумывать статистику и объёмы Wordstat.
- Не копировать структуру Pikapuka/olegweb 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи в article.html.
- Не путать GEO (generative) с локальной geo-SEO.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за одну сессию соберёт семантику и структуру SEO-статьи, напишет черновик с answer-first блоками, добавит meta/FAQ/schema, пройдёт чеклист перед публикацией и поймёт, какие GEO-правки внести, чтобы текст читали люди и цитировали AI-выдачи.

**action_outline:**

1. **Определить интент:** открыть топ-5 по `primary_query`; зафиксировать тип контента (гайд/чеклист/сравнение) и обязательные блоки (FAQ, таблицы, списки).
2. **Собрать семантику:** primary + secondary из карточки; сгруппировать LSI в 3–5 кластеров под будущие H2 (Wordstat — когда доступен).
3. **Собрать каркас:** H1 = главный запрос; H2 = кластеры; правило «ответ сразу после H2»; lead с прямым ответом.
4. **Написать черновик для людей:** короткие абзацы (3–5 строк), один абзац — одна мысль; кейс/цифра/пример в каждом крупном блоке.
5. **Вписать ключи естественно:** H1, первый абзац, 1–2 H2, Title/Description; синонимы вместо повторов.
6. **Добавить FAQ и упаковку:** 5–7 реальных вопросов; Title ~60–70 символов; Description ~150–160; alt у медиа.
7. **GEO-слой:** проверить island test на H2; answer-first в начале; передать schema-агенту BlogPosting + FAQPage.
8. **Финальный чеклист:** пройти 18 пунктов (раздел 7); Texterra-тест «лучший ответ по вопросу»; перелинковка на `/`.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (21 факт) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
