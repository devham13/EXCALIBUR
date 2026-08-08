# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата на самой статье)  
**research_date:** 2026-08-08  
**disclaimer:** Все даты, версии и статистика проверены на 2026-08-08 (2026 год).

---

## 1. SERP-обзор (WebSearch Cursor, август 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Авторитет; workflow тема → семантика → структура → текст → оптимизация; примеры «плохо/хорошо»; Wordstat, alt, мета, перелинковка | Нет GEO/нейропоиска; CTA Директа; мало про «читаемость как фактор» | Блок про Директ; копировать H1–H4 без GEO-слоя |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 2026 (13 шагов + чек-лист) | От ключа до WordPress; интент, конкуренты, мета, внутренние ссылки; printable checklist | Нет GEO; фокус на WP-сайты | 13 шагов 1:1; личный бренд автора как CTA |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (май 2026) | Wordstat/Serpstat, E-E-A-T, Title ~65 знаков, Schema Article+FAQPage, Featured Snippet | Кейсы без первичника; GEO — побочный эффект E-E-A-T | Непроверенные «+140%»; 7-разделная структура 1:1 |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | Кластеры 3–5 групп; «сначала смысл, потом оптимизация»; island test для E-E-A-T | Длинный sales-narrative; ИИ как центр | Шаблонные ИИ-промпты без редактуры |
| 5 | [tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | Формула 2026 | Lead = прямой ответ; синонимы вместо переспама; типы контента (FAQ, гайд, сравнение) | Короткий; мало техники и schema | Обобщения без чек-листа |
| 6 | [blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | SEO vs GEO vs AEO | Чанки 128–515 токенов; «один абзац = одна мысль»; Schema для ИИ | Коммерческий click.ru; смешение AEO/GEO | Цифры без первичника как «факт рынка» |
| 7 | [gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | Близкий угол к H1 | «Читают люди и понимают нейросети»; dual SEO+AI | Узкий бренд; мало пошаговой семантики | Заголовок и angle — не копировать дословно |
| 8 | [serpjet.ru/blog/chek-list-idealnoj-seo-stati-v-2026-ot-semantiki-do-cta](https://serpjet.ru/blog/chek-list-idealnoj-seo-stati-v-2026-ot-semantiki-do-cta-zamenit-seo-spetsialista-4847/) | Чек-лист 2026 | Интент-кластеры, H2 с пользой, FAQ, CTA по контексту | Продаёт SerpJet; checklist без «первой статьи с нуля» | Agency tone |

**Паттерн SERP (август 2026):** топ — «полный гайд / инструкция 2026» с E-E-A-T, Wordstat, чек-листом (1ps, olegweb, pikapuka, serpjet). Отдельный кластер — GEO/AEO (click.ru, gracie). Прямого совпадения с H1 «которые читают люди» мало — **пробел для Excalibur**: how-to + **читабельность как SEO/GEO-фактор** (инфостиль, атомарные H2, answer-first) в одном workflow.

**Intent:** `how_to` — пользователь хочет **систему от запроса до публикации**: интент → семантика → структура → текст → мета/schema → GEO-упаковка → финальный чек-лист. Вторичный: «seo текст для блога», «geo оптимизация статьи».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в Cloud Agent окружении (сервер не подключён; вызов `wordstat_get_top_requests` невозможен). Точные объёмы спроса **не получены**. Обновите токен и подключение через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса

| Фраза | Показы/мес |
|-------|------------|
| как писать seo статьи | *не получено — MCP недоступен* |
| seo текст для блога | *не получено* |
| geo оптimizaciya статьи | *не получено* |

### LSI для writer (экспертная семантика из SERP + secondary_queries, **без выдуманных частот**)

**Primary cluster:** как писать seo статьи, как написать seo статью, seo текст для блога, seo копирайтинг, seo статья для сайта, оптимизированная статья  

**Process cluster:** семантическое ядро, поисковый интент, wordstat, lsi слова, структура статьи h1 h2, title description, перелинковка, чек-лист seo статьи  

**Quality cluster:** e-e-a-t, инфостиль, переспам ключей, уникальность текста, featured snippet, answer-first  

**GEO cluster:** geo оптимизация статьи, geo в seo, ai выдача, нейропоиск, schema faqpage, llms.txt  

**PAA / FAQ hints (из SERP):** сколько символов в seo статье; что такое geo в seo; нужен ли переспам; чем title отличается от h1; можно ли писать с помощью ии  

**SEO-стратегия:** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блок про блог/longread; «geo оптимизация статьи» — отдельный H2 (не путать с локальной geo-SEO); faq_hints — в FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 должен отличаться от Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Title — ориентир ~65 знаков, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Schema.org: Article + FAQPage для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Title — 50–60 символов; Meta Description — 120–160 символов | [DTF — техSEO чек-лист блога](https://dtf.ru/id3181146/4572172-tekhnicheskoe-seo-dlya-bloga-chek-list) | 2026 | да |
| На странице должен быть **один** H1 с основным ключом | [DTF — техSEO чек-лист блога](https://dtf.ru/id3181146/4572172-tekhnicheskoe-seo-dlya-bloga-chek-list) | 2026 | да |
| Каждый четвёртый россиянин уже пользуется нейросетями ежедневно | [Click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да (как вторичная цитата в статье Click) |
| 17% людей при поиске информации довольствуются ответом ИИ и не кликают по ссылкам в выдаче | [Click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да (как вторичная цитата) |
| ИИ режет текст на чанки ~128–515 токенов (≈96–380 русских слов) для извлечения фактов | [Click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| SEO, AEO и GEO — три измерения одной поисковой реальности; SEO остаётся фундаментом | [Click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| После каждого H2 сразу давать содержательный ответ (правило из практики 2026) | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Главный ключ — в H1, первом абзаце, 1–2 H2, title и description; LSI — равномерно | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Финальный чек-лист SEO-копирайтинга: Title ≤60 символов, meta 140–160, один H1, alt, 3–5 внутренних ссылок, schema, CWV | [Spilno Agency — SEO copywriting 2026](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да |
| Главная задача статьи — полный ответ на запрос; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| 74% брендов из топ-10 Google присутствуют в ответах ChatGPT (Seer Interactive, цит. в RU-гайдах) | [mayai.ru — GEO чек-лист](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да (как вторичная цитата) |

**fact-bank.md:** прямых фактов по SEO-статьям нет — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); точные частоты Wordstat без MCP; «GEO заменяет SEO»; локальная geo-SEO как синоним Generative Engine Optimization.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чек-лист (15–20 пунктов).

**Почему отличается от конкурентов:**
- Яндекс — канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- olegweb/pikapuka — длинные, но без акцента «читают люди» как измеримой техники.
- H1 карточки B01 слабо раскрыт в SERP; наш фокус: **читабельность = структура + инфостиль + атомарные H2**.

**Режим B:** сама статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, lead с определением, внутренняя ссылка на `/`.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

**Подтемы внутри блоков:** Wordstat/интент, Title/Description, E-E-A-T lite, answer-first, llms.txt (опционально).

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ hints | «Сколько символов…», «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец longread | Ответ 2–4 предложения, action-first |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; island test |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Опционально, не вместо sitemap |
| E-E-A-T lite | Автор | Имя, роль из registry |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и конкуренты в SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе из индексируемого структурированного контента.
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + LSI/синонимы.
4. **Чем Title отличается от H1?** — Title для сниппета (50–65 знаков), H1 — заголовок на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Можно ли писать SEO-статью только через ИИ?** — для черновика да; финал — редактура, факты, уникальный опыт (иначе шаблон не ранжируется).
7. **Как проверить статью перед публикацией?** — чек-лист: семантика, мета, один H1, FAQ, schema, 3–5 внутренних ссылок, читабельность.

---

## 7. Риски для writer

- Не выдумывать статистику Wordstat и «рост %» из агентских кейсов.
- Не копировать структуру Pikapuka/olegweb 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Минимум **5** нумерованных шагов в теле + чек-лист **15–20** пунктов.
- Без эмодзи в article.html; CTA ≤ 3.
- Internal link: `/` по карточке темы.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику по primary_query, построит структуру longread с answer-first блоками, напишет и отредактирует текст под людей и поиск, заполнит Title/Description и FAQ со schema, добавит GEO-упаковку (атомарные H2, опционально llms.txt) и пройдёт финальный чек-лист перед публикацией SEO-статьи в блог.

**action_outline:**

1. **Определить интент и primary key:** вбить «как писать seo статьи» в выдачу; классифицировать intent (informational how-to); выбрать один главный ключ и 15–25 LSI из подсказок/конкурентов (Wordstat — когда доступен).
2. **Разобрать ТОП-5 SERP:** выписать общие H2, пробелы (нет GEO, нет чек-листа, слабый lead); зафиксировать уникальный угол «читают люди».
3. **Собрать структуру:** H1 с ключом; 4–6 H2 по карточке; под каждым H2 — тезис в первом предложении; план FAQ 5–7 из faq_hints.
4. **Написать draft:** lead = боль + прямой ответ; абзацы 3–5 строк; списки/таблицы; инфостиль без воды; один реальный пример/наблюдение (E-E-A-T lite).
5. **Оптимизировать семантику:** ключ в H1, первом абзаце, 1–2 H2, title, description; LSI равномерно; проверить на переспам «на слух».
6. **Техника и schema:** Title 50–65 символов, description 120–160; один H1; alt у изображений; JSON-LD BlogPosting + FAQPage (handoff schema-агенту); 3–5 внутренних ссылок.
7. **GEO-слой:** answer-first в начале; FAQ с ответами ≤80 слов; island test каждого H2; упоминание llms.txt как опции.
8. **Финальный чек-лист:** пройти 15–20 пунктов (семантика, мета, структура, FAQ, schema, ссылки, мобильная читабельность) — только после «да» публиковать.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (19 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `blog-topics.md` + `site-brief.md`.
