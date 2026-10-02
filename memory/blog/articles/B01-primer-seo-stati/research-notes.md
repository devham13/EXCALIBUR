# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата на самой статье)  
**research_date:** 2026-10-02  
**disclaimer:** Все даты, версии и статистика проверены на 02.10.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch Cursor, 02.10.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: интент, Wordstat, H1–H4, объём без «магической цифры», естественность ключей, мета, перелинковка | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок про Директ; копировать H-иерархию без GEO-слоя |
| 2 | [seo-prodvizhenie-biznesa.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila](https://seo-prodvizhenie-biznesa.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | How-to 2026 | Акцент «намерение, не ключ»; структура как следствие пользы; таблицы/списки по делу | Мало schema/GEO; типовой agency-tone | Длинные «новые правила» без чеклиста публикации |
| 3 | [seotika.ru/kak-pisat-seo-stati](https://seotika.ru/kak-pisat-seo-stati/) | Гайд «в ТОП» | Lead за 100 слов; H2 как вопросы; ориентир 1500–3000 слов для info; плотность 1–2% с оговоркой | Цифры объёма без привязки к нише; перегруз SEO-школой | Копировать 1:1 блок про «SEO Школу» и жёсткий объём |
| 4 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 13 шагов | Полный цикл до WordPress; чеклист 15 пунктов; E-E-A-T через опыт | Узкий фокус WP; GEO минимально | 13 шагов 1:1 — сжать в 7–9 для нашего workflow |
| 5 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 7 шагов + чеклист | Вордстат в шаге 1; структура до текста; Title ~60, Description ~160 | Коммерция курсов; без GEO-hooks | Переспам бренда «SEO Школа» |
| 6 | [divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 5 шагов | 15–25 фраз из Wordstat; кластеры; минимум вхождений главного ключа | Старый UX; слабый GEO | Шаблон «уникальность 100%» |
| 7 | [roiseo.ru/blog/struktura-seo-stati-dlya-bloga](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон блоков блога | Таблица блоков: lead 40–70 слов, ошибки, чеклист, FAQ + schema | Мало про семантику | Копировать таблицу блоков без адаптации под H1 B01 |
| 8 | [trigub.ru/geo-v-2026-godu](https://trigub.ru/geo-v-2026-godu/) | GEO + SEO 2026 | Article/FAQPage/HowTo/Person; «острова смысла» для AI | Не учит писать текст с нуля | Sales narrative агентства |

**Паттерн SERP (окт. 2026):** доминируют «пошаговый гайд 2026» + чеклист; отдельный кластер — GEO/AEO. Заголовок «которые читают люди» встречается (meta-journal.ru в research-serp.json), но слабо отделён от generic «как написать seo-статью».

**Intent:** `how_to` — собрать семантику → разобрать ТОП → структура → текст для людей → мета/schema → GEO-упаковка → чеклист перед публикацией. Вторичный: «seo текст для блога», «geo оптимизация статьи».

**Пробел для Excalibur B01:** единый workflow **SEO + GEO** с акцентом на **читабельность** (lead, короткие абзацы, island test) и **демонстрация на самой статье** (режим B), без agency-кейсов с непроверенными +140%.

---

## 2. Яндекс Wordstat (MCP `user-mcp-kv`)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` недоступен в среде Cloud Agent (namespace не подключён; вызов `wordstat_get_top_requests` невозможен). Точные **показы в месяц** не получены. Обновите токен и подключите MCP в Cursor: [oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40) — см. `skills/excalibur-research/SKILL.md`.

### Таблица спроса

| Фраза | Показы/мес |
|-------|------------|
| как писать seo статьи | *не получено — MCP недоступен* |
| seo текст для блога | *не получено — MCP недоступен* |
| geo оптимизация статьи | *не получено — MCP недоступен* |

### LSI и смежные запросы (экспертная семантика по SERP + конкурентам; **не** Wordstat)

**Кластер «написание»:** как написать seo статью, seo текст для сайта, seo копирайтинг 2026, пошаговая инструкция seo текста, чеклист seo статьи.  
**Кластер «структура»:** структура seo статьи, h1 h2 h3, оглавление, lead абзац, faq блок.  
**Кластер «семантика»:** семантическое ядро, lsi слова, яндекс вордстат, кластеризация запросов, поисковый интент.  
**Кластер «техника»:** title description, meta description 160 символов, alt изображений, внутренние ссылки, schema article faqpage.  
**Кластер «GEO»:** geo оптимизация, generative engine optimization, e-e-a-t, нейровыдача, ai overviews, llms.txt, faqpage json-ld.

**SEO-стратегия writer:** primary «как писать seo статьи» в H1/lead; secondary «seo текст для блога» — в блок про формат блога; «geo оптимизация статьи» — отдельный подблок или H2 «SEO + GEO в одном материале».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику подбирают в Яндекс Вордстат; учитывают намерение запроса | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Для информационной статьи в ТОП часто ориентируются на 1500–3000 слов, но решает полнота ответа | [Seotika — как писать SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да (как ориентир конкурентов, не норма) |
| Lead: прямой ответ в первых 100 словах / 2–3 предложениях | [Seotika — как писать SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| Title — ориентир до ~60 символов; Description — до ~160 | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| Из Wordstat для одной страницы — 15–25 связанных фраз, сгруппированных по смыслу | [Divitio — пошаговая инструкция](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Главный ключ — H1, первый абзац, одно вхождение ближе к концу (естественно) | [Divitio — пошаговая инструкция](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Блоки блога: lead 40–70 слов, таблица, пример, ошибки, чеклист, FAQ | [ROI SEO — структура](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| FAQPage JSON-LD: текст в schema должен совпадать с видимым FAQ на странице | [sitegeo.ru — чеклисты GEO/AEO](https://sitegeo.ru/) | 2026 | да |
| Базовый набор schema для статей: Article/BlogPosting, FAQPage, HowTo, Person, Organization | [trigub.ru — GEO 2026](https://trigub.ru/geo-v-2026-godu/) | 2026 | да |
| GEO — дополнение SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте | [Habr — GEO/AIO/AEO](https://habr.com/ru/articles/1030292/) | 2026 | да |
| Ответы FAQ для AI: 40–80 слов, начинаются с прямого утверждения | [sitegeo.ru — чеклисты GEO/AEO](https://sitegeo.ru/) | 2026 | да |
| Чеклист перед публикацией: интент, структура H2/H3, мета, alt, внутренние ссылки, FAQ (15+ пунктов у конкурентов) | [olegweb.ru — алгоритм](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 2026 | да |

**fact-bank.md:** фактов по SEO-написанию нет — использовать только таблицу выше.  
**Не использовать:** «+140% трафика» (Pikapuka); «AI 25% запросов» без первичника; «микроразметка ×1,5–2 цитирование» без исследования.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **longread для людей**, который закрывает интент и упакован для **GEO** (атомарные H2, FAQ, schema). Не «набивка ключей», а **workflow из 7–9 шагов** от семантики до чеклиста публикации.

**Дифференциация:** H1 «**которые читают люди**» — связать читабельность (lead, абзацы, island test) с поведенческими и GEO-сигналами; сама B01 — эталон (8 500–9 500 знаков, BlogPosting + FAQPage).

**H2-каркас (из карточки B01):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread (H1–H3, lead, списки, таблицы)  
3. FAQ и schema  
4. Чеклист перед публикацией  

**Tone:** практично, без корпоративной воды и эмодзи (site-brief).

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок SEO+GEO | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | Середина | «Что такое GEO в SEO?», «Сколько символов…» |
| FAQ 5–7 | Конец | Ответы 2–4 предложения, action-first |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema | schema-агент | BlogPosting + FAQPage (не в body HTML writer) |
| llms.txt | Упоминание | Для AI-краулеров блога |
| internal_links | Карточка | `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и ТОП; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цитирование в AI-ответах при структурированном контенте.  
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + тематический словарь.  
4. **Чем Title отличается от H1?** — Title для сниппета (~60 символов), H1 на странице; не дублировать дословно.  
5. **Какие schema нужны блогу?** — BlogPosting + FAQPage; для инструкций — HowTo.  
6. **Что такое llms.txt?** — файл-подсказка для AI-краулеров; дополнение к sitemap.  
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, мобильная версия.

---

## 7. Риски для writer

- Не выдумывать Wordstat-цифры до подключения MCP.  
- Объём текста: 8 500–9 500 знаков (`shared/quality-blog.md`).  
- Минимум 5 нумерованных шагов + чеклист 10+ пунктов (utility gate статьи).  
- Не копировать структуру Pikapuka/olegweb 1:1.  
- Цифры только из таблицы фактов §3.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за один проход соберёт семантику под один запрос, разберёт ТОП, соберёт структуру H2/H3 с lead и FAQ, напишет текст без переспама, заполнит Title/Description и alt, добавит FAQ + schema (BlogPosting/FAQPage), проверит материал по чеклисту и опубликует SEO-статью, которую дочитывают люди и которую могут цитировать нейропоисковики.

**action_outline (для writer):**

1. **Зафиксировать primary query** («как писать seo статьи») и интент how_to; выписать 5–20 вторичных фраз (Wordstat/Вебмастер) и отсечь запросы с другим намерением.  
2. **Разобрать ТОП-5–10:** формат (гайд/чеклист), обязательные подтемы, пробелы — записать skeleton H2/H3 до написания текста.  
3. **Собрать структуру longread:** один H1, 4–7 H2 из карточки + подвопросы; lead с прямым ответом в 40–100 словах; места под таблицу, список, блок ошибок.  
4. **Написать черновик «для людей»:** короткие абзацы, один H1, без переспама; главный ключ в H1, lead и одно естественное вхождение в конце; LSI из §2.  
5. **Добавить E-E-A-T lite:** пример из практики, цифры только из §3, автор/редакция, дата обновления.  
6. **Упаковать GEO:** атомарные H2 (тезис в первом предложении); FAQ 5–7 с ответами 40–80 слов; при необходимости HowTo-логика в шагах.  
7. **Заполнить мета и медиа:** Title ~60 символов, Description ~160; alt у изображений; 3–5 внутренних ссылок (карточка: `/`).  
8. **Schema handoff:** BlogPosting + FAQPage JSON-LD (текст FAQ = видимый блок) — для schema-агента, не дублировать сырым JSON в body без контракта.  
9. **Финальный чеклист** (10+ пунктов): интент, H2/H3, вода, мета, FAQ, schema, ссылки, мобильная читаемость — только после PASS публиковать.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (см. §2) |
| Таблица фактов с URL | ✅ (17) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `memory/topics/blog-topics.md` + `memory/brief/site-brief.md`.
