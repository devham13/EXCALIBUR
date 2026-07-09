# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to + чеклист)  
**research_date:** 2026-07-06  
**disclaimer:** Все даты, версии и статистика проверены на 06.07.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch, июль 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон workflow: тема → семантика (Wordstat) → структура → текст → мета; абзацы 3–5 строк; естественность ключей | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа; «что такое SEO» без actionable чеклиста |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Кластеризация Wordstat (3–5 групп); answer-first после H2; Title 50–60 символов | Длинный sales-narrative агентства; часть цифр из «нашего опыта» без первичника | Копировать структуру 1:1; непроверенные «+3–5 позиций за 2–4 недели» |
| 3 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 13 шагов, WP (обнов. 05.02.2026) | Полный цикл от спроса до публикации в WordPress; чек-лист; скриншоты, таблицы | Фокус на WP-блогах; мало GEO-слоя | 13 шагов как копипаста; Telegram-CTA |
| 4 | [serptop.ru/blog/kak-pisat-seo-teksty](https://serptop.ru/blog/kak-pisat-seo-teksty/) | Гайд + чек-лист RU | Шаблон H1–H2; семантика через Wordstat; meta/alt/ЧПУ; ориентиры по ключам | Agency CTA; нет единого SEO+GEO workflow | Формулы заголовков без адаптации под H1 карточки |
| 5 | [habr.com/ru/articles/1022684](https://habr.com/ru/articles/1022684/) | SEO & GEO чеклисты (таблицы) | Контент + семантика + E-E-A-T + GEO-формат в одном месте; приоритеты 🔴🟡🟢 | Не учит писать текст с нуля; фокус на сайте целиком | Таблицы 1:1 без контекста B01 |
| 6 | [habr.com/ru/articles/1042732](https://habr.com/ru/articles/1042732/) | GEO/AEO longread 2026 | Answer-First 2–5 предложений; RAG-логика; Schema FAQPage/Article; цифры Grows Memo | Encyclopedia, не how-to по копирайтингу | Agency tone; длинные кейсы без шагов |
| 7 | [gracie.digital/blog/2026/06/19](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | AI SEO июнь 2026 | 40–60 слов прямого ответа; факты каждые 150–200 слов; атомарные H2/H3 | Узкий бренд; мало про семантику/Wordstat | Копировать «150–200 слов» как жёсткую норму без оговорки |
| 8 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 10 шагов + E-E-A-T (май 2026) | Title ~65 знаков; Schema Article+FAQPage; Featured Snippet | Кейсы «+140%» без верификации | 7-разделную структуру 1:1 |

**Паттерн SERP:** топ «как писать seo статьи 2026» — длинные гайды (1ps, olegweb, pikapuka) + официальный Яндекс + чеклисты (serptop, Habr 1022684). Отдельный кластер — GEO-лонгриды (1042732). H1 «которые читают люди» в топе почти не встречается — пробел для дифференциации через **читабельность + единый workflow SEO+GEO**.

**Intent:** `how_to` — пользователь хочет пошаговую систему: проверить спрос → интент → структура → текст → мета → FAQ/schema → финальный чеклист. Вторичный: связка **seo текст для блога** и **geo оптимизация статьи** в одном материале.

**Пробел для Excalibur:** мало кто даёт **один компактный workflow (7–9 шагов)** + **чеклист 15–20 пунктов** + **GEO-чанки** без agency-water и без «новостей про алгоритмы». Угол B01: longread, который **сам является эталоном** (режим B).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в сессии Cloud Agent (в каталоге MCP только Cursor Automation Tools). Инструмент `wordstat_get_top_requests` **не вызван** — точные показы в месяц **не получены**.

Для восстановления доступа к Wordstat API обновите OAuth-токен:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса

| Фраза | Показы/мес |
|-------|------------|
| как писать seo статьи | *не получено — MCP недоступен* |
| seo текст для блога | *не получено — MCP недоступен* |
| geo оптимизация статьи | *не получено — MCP недоступен* |

### Экспертная семантика (без объёмов; для writer до подключения Wordstat)

**Primary-кластер:** как писать seo статьи, как написать seo статью, как писать seo тексты, seo статья для сайта, пошаговая инструкция seo статьи.

**Secondary (из карточки B01):** seo текст для блога, seo текст для блога как писать, статья для блога seo.

**GEO-слой:** geo оптимизация статьи, geo в seo, оптимизация статьи под нейросети, answer-first, schema faqpage.

**LSI из SERP + подсказок конкурентов:** семантическое ядро, структура seo статьи, title и description, h1 h2 h3, lsi фразы, e-e-a-t, чеклист перед публикацией, сколько символов в seo статье, уникальность текста, внутренняя перелинковка, alt изображений, микроразметка article.

**SEO-стратегия для writer:** primary «как писать seo статьи» в H1/lead/title; «seo текст для блога» — в блок про формат блога; «geo оптимизация статьи» — в H2 про SEO+GEO; faq_hints («сколько символов», «что такое geo») — в FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир **3–5 строк**; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| **Один H1** на страницу; H2–H4 для смысловых блоков без пропуска уровней | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в **Яндекс Вордстат** и **Яндекс Вебмастер** | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Фразы из Wordstat группируют в **3–5 смысловых групп** (кластер) | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| После каждого H2 — **содержательный ответ** сразу, без «разогрева» | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Title для статей — ориентир **50–60 символов** с основным запросом | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Фиксированного объёма нет: иногда **4 000–6 000** знаков достаточно, иногда нужна инструкция **15 000–25 000** знаков | [olegweb.ru — SEO-статья](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| SEO-статья 2026 = страница, закрывающая задачу пользователя (выбрать, настроить, сравнить), не «текст под ключи» | [olegweb.ru — SEO-статья](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Meta title — ориентир **≤70 символов** с основным ключом | [serptop.ru — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| Основной ключ: H1 + первый абзац + 2–3 естественных вхождения в тексте (ориентир для ~2000 знаков) | [serptop.ru — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| Контент: H2/H3, списки, таблицы; ответ на вопрос в **первом абзаце** раздела | [habr.com/ru/articles/1022684](https://habr.com/ru/articles/1022684/) | 2026 | да |
| Answer-First: прямой ответ в **первых 2–5 предложениях** раздела | [habr.com/ru/articles/1042732](https://habr.com/ru/articles/1042732/) | 2026 | да |
| **44,2%** цитат LLM приходится на первые **30%** текста страницы (Grows Memo, февр. 2026, цит. Habr) | [habr.com/ru/articles/1042732](https://habr.com/ru/articles/1042732/) | 2026 | да |
| Прямой ответ на вопрос темы — в первых **40–60 словах** блока (без воды) | [gracie.digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| GEO-контент: конкретика и цифры примерно каждые **150–200 слов** со ссылками на источники | [gracie.digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| Schema.org **FAQPage**, **Article**, **Organization** — гигиенический минимум для GEO 2026 | [habr.com/ru/articles/1042732](https://habr.com/ru/articles/1042732/) | 2026 | да |
| Google и Яндекс рекомендуют микроразметку **JSON-LD** (Schema.org) | [1ps.ru — Schema.org](https://1ps.ru/blog/sites/schemaorg/) | 2026 | да |
| Главная задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [maryproject.ru — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**fact-bank.md:** прямых фактов по SEO-копирайтингу нет — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); «обновление статьи +3–5 позиций за 2–4 недели» (1ps — только «по опыту»); «+40% к ранжированию» из Habr без первичника Princeton/arxiv; «60% трафика с телефонов» (1ps) без cross-check.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один список ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → чеклист перед публикацией.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO-слоя в одном how-to.
- GEO-гайды (Habr 1042732) не учат писать текст с нуля.
- Агентские гайды (1ps, Pikapuka) перегружены CTA и непроверенными кейсами.
- H1 «которые читают люди» слабо раскрыт в SERP — наш фокус: **читабельность как SEO-фактор** (структура, «острова смысла», answer-first).

**Режим B:** сама статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (один контент, две цели)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-подсказки | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец longread | Ответ 2–4 предложения, действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + LSI (Яндекс Директ).
4. **Чем Title отличается от H1?** — Title для сниппета (50–70 символов), H1 — заголовок на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.
7. **Как писать seo текст для блога, а не для карточки товара?** — информационный интент, longread, перелинковка hub→spoke, без коммерческого переспама.

---

## 7. Черновик чеклиста (15–20 пунктов для writer)

1. Проверить спрос и интент по primary_query (Wordstat + SERP).
2. Собрать 3–5 смысловых групп LSI из Wordstat/подсказок.
3. Один H1 с главным ключом; Title 50–70 символов, не копия H1.
4. Lead: боль + обещание результата + ключ в первых 50–100 словах.
5. После каждого H2 — прямой ответ в 2–5 предложениях (answer-first).
6. Абзацы 3–5 строк; списки и таблицы там, где есть перечисления.
7. Ключ в H1, первом абзаце, 1–2 H2 естественно; без переспама.
8. FAQ 5–7 реальных вопросов; ответы короткие и actionable.
9. JSON-LD BlogPosting + FAQPage (в schema, не в body).
10. Alt у изображений; уникальные визуалы или схемы, не сток «для галочки».
11. Внутренняя перелинковка на `/` и смежные материалы.
12. Дата публикации/обновления видима + в schema dateModified.
13. Проверка: island test каждого H2 (понятен без контекста).
14. Убрать воду, канцелярит, следы ИИ-штампов.
15. Финальный прогон: мета, уникальность, битые ссылки, мобильная читаемость.

---

## 8. Риски и blockers для writer

- Не выдумывать статистику Wordstat — MCP недоступен.
- Не копировать структуру Pikapuka/olegweb 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи в article.html; без VPN/обход блокировок.
- Минимум **5** нумерованных шагов в теле + чеклист 15+ пунктов.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за одну сессию соберёт семантику по primary_query, построит структуру longread с answer-first блоками, напишет и оформит SEO-статью для блога (мета, H1–H3, FAQ, JSON-LD), пройдёт чеклист из 15+ пунктов перед публикацией и поймёт, какие GEO-правки добавить, чтобы статью цитировали нейросети.

**action_outline:**

1. **Проверить спрос и интент:** вбить «как писать seo статьи» в Яндекс/Google; зафиксировать тип выдачи (гайды/how-to); выписать H2 конкурентов из топ-5.
2. **Собрать семантику:** Wordstat + подсказки → 3–5 кластеров LSI; выбрать primary и secondary из карточки B01.
3. **Собрать структуру:** H1 = запрос + польза; 4–6 H2 по кластерам; под каждым H2 — тезис ответа в первых 2–5 предложениях.
4. **Написать lead и черновик:** lead с ключом в первых 50–100 словах; абзацы 3–5 строк; списки/таблицы для шагов.
5. **Встроить ключи без переспама:** H1, первый абзац, 1–2 H2, Title/Description; LSI по смыслу, не по плотности.
6. **Добавить GEO-слой:** answer-first в каждом H2; FAQ 5–7; факты со ссылками; блок «SEO + GEO в одной статье».
7. **Оформить технику:** Title 50–70 символов, Description с выгодой; alt; внутренние ссылки; даты публикации/обновления.
8. **Подготовить schema:** BlogPosting + FAQPage (JSON-LD отдельным артефактом).
9. **Финальный чеклист:** пройти 15 пунктов из раздела 7; island test; убрать воду и ИИ-штампы.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (21 факт) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks + чеклист | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `blog-topics.md` + `site-brief.md`.
