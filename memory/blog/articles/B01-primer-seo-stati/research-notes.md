# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to / longread-эталон)  
**research_date:** 2026-10-13  
**disclaimer:** Все даты, версии и статистика проверены на 13.10.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch, октябрь 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон по структуре H1–H4, объёму «по конкуренции», естественным ключам, Wordstat, alt, абзацам 3–5 строк | Нет GEO/нейропоиска; мало пошагового «от нуля до публикации» | Коммерческий финал про Директ; дублировать только канон, не CTA |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Правило «после каждого H2 — содержательный ответ»; смысл → семантика; списки/таблицы | Длинный sales-narrative; ИИ-блок без human-in-the-loop для B2B | Копировать структуру 1:1; обещания «ИИ заменит редактора» |
| 3 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Пошаговый гайд 2026 | «Сначала каркас H2–H3, потом текст»; Title 55–60, Description ~140; порядок блоков от главного к второстепенному | Мало GEO; тошнота/уникальность как KPI без контекста ниши | Жёсткие SEO-метрики без оговорок |
| 4 | [hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | Практик 2026 | Порядок: спрос → ТОП → структура → черновик для человека → SEO-доводка; H1 ≠ Title | Нет чеклиста публикации и schema | Старт с «10 000 знаков и 15 ключей» как нормы |
| 5 | [roiseo.ru/blog/struktura-seo-stati-dlya-bloga](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон блога | Модуль: ответ 40–70 слов → объяснение → таблица → ошибки → чек-лист → FAQ → автор/дата | Узко про «структуру», без семантики и GEO | Agency CTA в каждом блоке |
| 6 | [seotika.ru/kak-pisat-seo-stati](https://seotika.ru/kak-pisat-seo-stati/) | SEO-агентство 2026 | Лид = прямой ответ; H2 как вопросы; иерархия H1→H2→H3 | «1500–3000 слов» и «плотность 1–2%» без привязки к нише Excalibur | Цифры объёма как универсальная норма |
| 7 | [pw.agency/.../kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | GEO + контент 2026 | Snippet-First под H2; чанки 3–7 строк; E-E-A-T + FAQ | «+80% шансов» без первичника; agency tone | Непроверенные проценты |
| 8 | [anyseo.io/blog/geo-optimizaciya](https://anyseo.io/blog/geo-optimizaciya) | GEO с первоисточниками (09.2026) | GEO-bench Aggarwal; keyword stuffing хуже baseline; Google/Yandex docs | Фокус GEO, не «как написать статью с нуля» | Перегруз научным слоем в intro |

**Паттерн SERP:** топ — пошаговые гайды 2026 (семантика → структура → текст → мета) + отдельный кластер «статьи для ИИ». H1 «…которые читают люди» в выдаче почти не встречается: конкуренты продают «ТОП» и «SEO-текст», а не **читабельность + один workflow SEO+GEO**.

**Intent:** `how_to` — собрать запрос → outline → текст для человека → мета → проверка. Вторичный: «seo текст для блога», «geo оптимизация статьи» — в одном материале, не двумя проектами.

**Пробел для Excalibur:** единый **action-first** pipeline для B2B-блога (8,5–9,5k знаков по quality-blog): longread, который **сам демонстрирует** формат (режим B), с чеклистом перед публикацией и GEO-чанками без отдельного «GEO-курса».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в текущем Cloud Agent run (MCP не подключён). Вызов `wordstat_get_top_requests` для «как писать seo статьи» выполнить не удалось. **Точные показы в месяц не получены** — в статье не утверждать частотность без повторного прогона Wordstat.

**Экспертная семантика (LSI из SERP + карточка B01, без цифр спроса):**

| Кластер | Фразы для writer |
|---------|------------------|
| Primary | как писать seo статьи, seo текст для блога, написать seo статью |
| Структура | структура seo статьи, h1 h2 h3, title description, seo текст для сайта |
| Качество | seo текст 2026, полезный контент, интент запроса, lsi слова |
| GEO | geo оптимизация статьи, snippet-first, faq schema, нейропоиск |
| FAQ-intent | сколько символов в seo статье, что такое geo в seo |

**После восстановления MCP:** повторить `wordstat_get_top_requests` для primary + secondary; при 401 — [OAuth Yandex](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40).

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи нет — зависит от сложности темы и конкуренции в выдаче | [Яндекс B2B — SEO-текст](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс B2B — SEO-текст](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир **3–5 строк**; списки для перечислений | [Яндекс B2B — SEO-текст](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают **смысл и полезность**, не плотность ключей; переспам вреден | [Яндекс B2B — SEO-текст](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в **Яндекс Вордстат** (и смежные инструменты) | [Яндекс B2B — SEO-текст](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс B2B — SEO-текст](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| К изображениям добавляют **alt** — краткое описание для ПС и доступности | [Яндекс B2B — SEO-текст](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение (польза), основная часть по шагам, заключение со следующим шагом | [Яндекс B2B — SEO-текст](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| После каждого H2 — **содержательный ответ**, не «заголовок ради ключа» | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Каркас из H2–H3 собирают **до** написания абзацев | [SEO школа — как писать SEO-текст](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| Title — ориентир **55–60 символов**, основной запрос ближе к началу | [SEO школа](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| Description — ориентир **~140 символов**, ключ + выгода | [SEO школа](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| Порядок работы: спрос → ТОП → **структура** → черновик для человека → SEO-доводка | [Hardkod — SEO-текст 2026](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | 2026 | да |
| H1 можно сформулировать **естественнее**, не дублируя Title слово в слово | [Hardkod](https://www.hardkod.ru/blog/kak-napisat-kachestvennyj-seo-tekst) | 2026 | да |
| Модуль блога: **40–70 слов** ответа на первом экране, затем таблица/ошибки/чек-лист/FAQ | [ROI SEO — структура](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| Лид: **прямой ответ** в первых 2–3 предложениях; H2 — крупные вопросы пользователя | [Seotika — SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| Snippet-First: под H2 — резюме **1–3 предложения**, отвечающие на вопрос блока | [PW Agency — GEO контент 2026](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 2026 | да |
| GEO-bench: **10 000** запросов, 25 доменов; переписывание источников под GEO замеряли на видимость в ответе | [anyseo — GEO](https://anyseo.io/blog/geo-optimizaciya) | 09.2026 | да |
| Приём «добавить вхождений ключа» дал visibility **17,8** vs baseline **19,5** (хуже без правок) | [anyseo — GEO / Aggarwal et al.](https://anyseo.io/blog/geo-optimizaciya) | 09.2026 | да |
| Google: **нет дополнительных требований** для AI Overviews; страница должна быть **проиндексирована** и eligible для сниппета (док. обновлена 10.12.2025, цит. anyseo) | [anyseo — GEO](https://anyseo.io/blog/geo-optimizaciya) | 09.2026 | да |
| Яндекс Нейро: факты из **веб-источников** со ссылками; рекомендация — **высокое ранжирование** в Поиске и контент под вопросы (цит. anyseo → блог для вебмастеров) | [anyseo — GEO](https://anyseo.io/blog/geo-optimizaciya) | 09.2026 | да |
| Для Алисы/нейроответов **топ органической выдачи** критичен для попадания в источники | [Habr — GEO нейросети](https://habr.com/ru/articles/1081126/) | 2026 | да |
| Оптимальный блок ответа для извлечения ИИ — **40–80 слов** (отраслевая практика, trigub; согласуется с FAQ-форматом) | [trigub.ru — GEO-продвижение](https://trigub.ru/blog/geo-prodvizhenie-sayta/) | 2026 | да (как ориентир) |

**fact-bank.md:** прямых фактов про SEO-копирайтинг нет; для B01 — только таблица выше + editorial norm Excalibur **8 500–9 500** знаков (`shared/quality-blog.md`, не SERP-цифра).

**Не использовать без оговорки:** «+80% в выдачу ИИ» (PW); «1500–3000 слов» как норма для всех (Seotika); «+140% трафика» (старые agency-кейсы); точная частотность Wordstat без MCP.

---

## 4. Угол статьи (utility-only)

**Главный угол:** одна SEO-статья 2026 = **longread для человека** + **техупаковка под нейропоиск** в одном проходе. Фокус H1: **читабельность** (структура, lead, «острова смысла» под H2) как конкурентное преимущество, а не «ещё 15 ключей».

**Почему не как конкуренты:**
- Яндекс — канон без GEO-слоя и без чеклиста публикации.
- Agency-гайды — KPI тошноты/объёма и CTA.
- GEO-статьи не учат писать текст с нуля.
- Сама статья B01 — **эталон режима B** (демонстрация формата на себе).

**H2-каркас (карточка + research):**
1. Зачем SEO и GEO в одной статье (один контент, две цели: клик + цитирование)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema (BlogPosting + FAQPage — handoff schema-агенту)
4. Чеклист перед публикацией (15–20 пунктов)

**Tone (site-brief):** практики B2B AI-автоматизации; без воды, эмодзи, выдуманного ROI.

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO — …» |
| Snippet-first под каждым H2 | Тело | 1–3 предложения → детали |
| FAQ 5–7 | Конец | Ответы 40–80 слов, action |
| Island test | Writer QA | Блок понятен без соседних |
| Internal link | Карточка | `/` (главная) |

**Целевые формулировки:** как писать seo статьи, seo текст для блога, geo оптимизация статьи, сколько символов в seo статье, что такое geo в seo.

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); для how-to longread Excalibur — **8 500–9 500** знаков текста.
2. **Что такое GEO в SEO?** — дополнение: цель — цитирование в AI-ответах при сохранении классического SEO.
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + LSI; переспам ухудшает и UX, и GEO-bench baseline.
4. **Чем Title отличается от H1?** — Title для сниппета (~55–60 символов), H1 на странице; не дублировать дословно.
5. **Какие schema для статьи блога?** — BlogPosting (или Article) + FAQPage для блока вопросов.
6. **Как связать SEO-текст и нейропоиск?** — answer-first блоки, FAQ, факты с источниками; SEO-ранжирование остаётся базой для Яндекс Нейро.
7. **Как проверить статью перед публикацией?** — чеклист: интент, outline, мета, перелинковка, FAQ, schema, читабельность.

---

## 7. Риски для writer

- Не выдумывать Wordstat-частотность (MCP недоступен).
- Не копировать структуру 1ps/Seotika 1:1.
- Объём **8 500–9 500** знаков (quality-blog).
- Без эмодзи в article.html; без VPN-тематики.
- Цифры только из раздела 3.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за один цикл работы соберёт семантику и outline по ТОП выдачи, напишет черновик longread «для людей» с lead и snippet-first блоками под H2, оформит Title/Description/H1, добавит FAQ под schema и пройдёт чеклист перед публикацией так, чтобы материал был готов и к органическому SEO, и к GEO-извлечению.

**action_outline:**

1. **Зафиксировать интент:** по primary query записать, что пользователь должен *сделать* после прочтения (how_to); выписать 5–7 подвопросов из SERP/PAA.
2. **Семантика:** собрать кластер в Wordstat + 3–5 LSI из ТОП-10; отметить «обязательные» H2 по конкурентам и 1–2 пробела (свой угол).
3. **Outline до текста:** H1, 4–6 H2 из карточки, H3 при необходимости; под каждым H2 — тезис ответа в 1–2 предложения.
4. **Lead и тело:** в первых 2–3 предложениях прямой ответ; абзацы 3–5 строк; таблица или список там, где в ТОПе сравнения/шаги.
5. **GEO-слой:** под каждым H2 — snippet-first (1–3 предложения); FAQ 5–7 с ответами 40–80 слов; факты с URL, не «голые» цифры.
6. **Мета:** Title ~55–60 символов, Description ~140; H1 ≠ Title; ключ в lead естественно.
7. **Медиа и связи:** alt у изображений; 2–4 внутренние ссылки (главная `/` + релевантные статьи кластера SEO/GEO при наличии).
8. **Schema-handoff:** передать schema-агенту пары FAQ + метаданные BlogPosting (не вставлять JSON-LD в body writer'ом, если контракт такой).
9. **Чеклист публикации:** пройти 15–20 пунктов (семантика, мета, структура, FAQ, перелинковка, дата/автор, preview сниппета).

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md` + `shared/quality-blog.md`.
