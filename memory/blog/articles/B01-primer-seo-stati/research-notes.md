# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + демонстрация формата на самой статье)  
**research_date:** 2026-08-16  
**disclaimer:** Все даты, версии и статистика проверены на 16.08.2026.

---

## 1. SERP-обзор (WebSearch, август 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: семантика через Вордстат, H1 один, 3–5 строк в абзаце, естественные ключи, мета | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа; копировать структуру без GEO-слоя |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 | Кластеризация семантики; правило «ответ сразу после H2»; ИИ как черновик + редактура | Длинный sales-narrative; GEO побочно | 7-разделную структуру 1:1 |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-…](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский гайд (2026) | E-E-A-T, чек-лист 10 шагов, Schema Article+FAQPage, Title ~65 знаков | Кейсы с непроверенными «+140%» | Непроверенные проценты в кейсах |
| 4 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-…](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист 9 критериев (04.06.2026) | E-E-A-T/ЭПОС, BLUF («сначала ответ — потом детали»), AI Overviews + Алиса | Мало пошагового workflow «с нуля» | Формат «9 критериев» без единого action_outline |
| 5 | [tolk.digital/kak-pisat-seo-teksty-v-2026-godu-…](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | Практический гайд | 6 тестов качества текста; синонимы вместо переспама; форматы FAQ/гайд/сравнение | Поверхностный GEO | Шаблонные формулировки «формула успеха» |
| 6 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 13 шагов до WordPress | Полный pipeline: спрос → интент → SERP → структура → публикация | Узкий фокус на WP | Копировать 13 H2 как каркас |
| 7 | [habr.com/ru/articles/1067328](https://habr.com/ru/articles/1067328/) | Schema 2026 | FAQPage в Яндексе + LLM; Article/BlogPosting/Person; санкции за фейковые Review | Не учит писать текст | Таблицы schema 1:1 без контекста B01 |
| 8 | [impact-dl.ru/geo-otvety-ii-2026-…](https://impact-dl.ru/geo-otvety-ii-2026-chto-pomogaet-popast-v-citatu/) | GEO vs SEO | Честно: Schema/FAQ — гигиена, цитата = содержание + проверяемость | Мало про написание longread | Обещание «добавим FAQ — попадёте в нейроответ» |

**Паттерн SERP (август 2026):** топ — «полный гайд 2026» с E-E-A-T, Wordstat, чек-листом (1ps, pikapuka, texterra, tolk). Отдельный кластер — GEO-лонгриды. H1 «которые читают люди» слабо представлен: конкуренты говорят «для людей и роботов», но не связывают **читабельность** с **GEO-извлекаемостью** в одном workflow.

**Intent:** `how_to` — пользователь хочет пошаговую систему: семантика → структура → текст → техника → проверка. Вторичный: связка SEO + GEO в одном материале (`seo текст для блога`, `geo оптимизация статьи`).

**Пробел для Excalibur:** единый **action-first workflow** «для людей» — BLUF + атомарные H2 + FAQ/schema + финальный чеклист; без agency-кейсов и без «SEO = ключи».

**fact-bank.md:** нет фактов по SEO-копирайтингу — все цифры только из таблицы ниже.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` недоступен в текущем Cloud-прогоне (не найден среди подключённых серверов). Вызов `wordstat_get_top_requests` для «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи» **не выполнен**. Точные объёмы показов/мес **не получены** — не использовать выдуманные цифры спроса.

**Обновление токена (когда MCP доступен):** https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Семантическая карта (экспертная, без объёмов — до восстановления Wordstat)

| Кластер | Фразы для writer (LSI) | Где в статье |
|---------|------------------------|--------------|
| Primary | как писать seo статьи, как написать seo статью, seo текст для блога | H1, lead, Title |
| Семантика | семантическое ядро, кластер запросов, LSI, интент, Wordstat, поисковые подсказки | H2 «сбор семантики» |
| Структура | структура seo статьи, H1 H2 H3, чек-лист seo статьи, longread | H2 «структура» |
| Качество | E-E-A-T, ЭПОС, читабельность, BLUF, answer-first, без воды | H2 «текст для людей» |
| Техника | title description, meta-теги, перелинковка, alt, schema.org | H2 «техника» |
| GEO | geo оптимизация статьи, нейровыдача, FAQPage, BlogPosting, AI Overviews, Алиса AI | H2 «SEO + GEO» |
| FAQ-intent | сколько символов в seo статье, что такое geo в seo, нужен ли переспам ключей | FAQ-блок |

**SEO-стратегия (до Wordstat):** primary «как писать seo статьи» в H1/lead; secondary «seo текст для блога» — в блок про формат блога; «geo оптимизация статьи» — отдельный подблок, не подменяет primary в Title.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Базовый принцип 2026: сначала главный ответ, потом детали (BLUF) | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Google: helpful, people-first content + E-E-A-T; Яндекс: релевантность + ЭПОС | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| После каждого H2 — сразу содержательный ответ, не «в этой части мы рассмотрим…» | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Главный ключ — в H1, первом абзаце, 1–2 H2, Title и Description; LSI — органично по тексту | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Title — ориентир ~65 знаков с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| H1 должен отличаться от Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Schema.org: Article/BlogPosting + FAQPage для структуры и сниппета | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Короткие абзацы 3–5 строк; лучше 8 000 знаков без воды, чем 15 000 с повторами | [Sales Generator — SEO-тексты 2026](https://sales-generator.ru/blog/seo-teksty-2026/) | 2026 | да |
| Title ≤60 символов, Meta Description 140–160 — ориентир для финального чеклиста | [Divitio — SEO-текст пошагово](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| FAQPage в 2026: сниппеты в Яндексе + формат «вопрос — короткий ответ» для LLM | [Habr — микроразметка 2026](https://habr.com/ru/articles/1067328/) | 2026 | да |
| BlogPosting/Article + Person — сигналы авторства и свежести | [Habr — микроразметка 2026](https://habr.com/ru/articles/1067328/) | 2026 | да |
| В GEO 2026 цитату дают ясный ответ и проверяемые факты, а не «длинный FAQ ради разметки» | [Impact Digital Lab — GEO 2026](https://impact-dl.ru/geo-otvety-ii-2026-chto-pomogaet-popast-v-citatu/) | 2026 | да |
| Извлекаемый блок: 60–100 слов прямого ответа; предложения до 20–25 слов | [sergeisivkov.ru — контент для GEO](https://www.sergeisivkov.ru/blog/kontent-dlya-geo/) | 2026 | да |
| GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте | [pw.agency — GEO-оптимизация контента](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 2026 | да |

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); «Schema гарантирует нейроответ»; любые объёмы Wordstat без MCP.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → BLUF-текст → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды перегружены E-E-A-T-кейсами и CTA.
- H1 B01 («которые читают люди») — фокус на **читабельность как SEO+GEO фактор** (острова смысла, инфостиль, BLUF).

**Режим B:** сама статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (не два проекта, один контент)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

Подтемы внутри блоков: Wordstat, Title/Description, E-E-A-T lite, перелинковка, llms.txt (опционально).

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | «Что такое GEO в SEO?», «Сколько символов нужно в SEO-статье?» | Вопрос в заголовке |
| FAQ 5–7 пар | Конец longread | Ответ 2–4 предложения, actionable |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; 3–5 строк в абзаце |
| Island test | QA для writer | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` (главная) |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и топ SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключевые слова в 2026 году?** — нет; естественные вхождения + LSI/тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 — заголовок на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage для блока вопросов.
6. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность, BLUF-тест.

---

## 7. Риски для writer

- Не выдумывать статистику Wordstat и «рост трафика %» без источника.
- Не копировать структуру Pikapuka/1ps 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Минимум **5** нумерованных шагов в теле + чеклист **10+** пунктов.
- Без эмодзи, без VPN/обход блокировок.
- Internal link: `/` из карточки темы.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель определит интент запроса, соберёт семантическое ядро, построит структуру longread с BLUF-блоками, напишет SEO-текст для блога с E-E-A-T-сигналами, оформит Title/Description и FAQ со Schema, добавит GEO-слой (атомарные H2 + FAQPage) и пройдёт финальный чеклист перед публикацией.

**action_outline (how-to, 9 шагов):**

1. **Зафиксировать запрос и интент:** вбить primary query в поиск; определить тип выдачи (информационная/комmercial); записать 3–5 вопросов пользователя из подсказок и PAA.
2. **Собрать семантику:** Wordstat + подсказки → 15–25 фраз; сгруппировать в 3–5 кластеров (основная тема, уточнения, LSI, GEO).
3. **Разобрать топ-5 SERP:** выписать H2 конкурентов, must-have темы и content gap (что добавите вы — читабельность + GEO в одном workflow).
4. **Собрать скелет:** H1 с primary; 4–6 H2 по кластерам; FAQ 5–7; правило — после каждого H2 сразу прямой ответ (BLUF).
5. **Написать lead 60–100 слов:** определение + главный ответ на запрос без «в этой статье мы рассмотрим».
6. **Написать тело:** абзацы 3–5 строк; списки/таблица; E-E-A-T lite (автор, дата, пример/цифра с URL); ключи органично.
7. **Техника:** Title ≤60–65 символов (≠ H1), Description 140–160, alt, 2–3 внутренние ссылки, slug с ключом.
8. **GEO-слой:** атомарные чанки под H2; FAQ с короткими actionable ответами; JSON-LD BlogPosting + FAQPage (в schema, не в body).
9. **Финальный чеклист:** island test, BLUF test, переспам, факты с URL, schema handoff — только после ✅ публиковать.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен; семантика без объёмов |
| Таблица фактов с URL | ✅ (19 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
