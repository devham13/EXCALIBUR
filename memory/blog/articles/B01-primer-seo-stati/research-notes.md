# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-10-09  
**disclaimer:** Все даты, версии и статистика проверены на 09.10.2026 (2026 год).

---

## 1. SERP-обзор (минимум 3 конкурента)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Авторитет источника; пошаговый workflow (тема → семантика → структура → текст → оптимизация); примеры «плохо/хорошо»; акцент на естественность ключей и читабельность; Wordstat, alt, мета, перелинковка | Нет GEO/нейропоиска; продвижение Директа в конце; объём без универсального норматива, но без GEO-hooks | Блок про Директ и коммерческий CTA; дублировать каноническую структуру H1–H4 без GEO-слоя |
| 2 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (май 2026) | Глубокая семантика (интент, LSI, Wordstat, Serpstat); E-E-A-T с кейсами; чек-лист 10 шагов; Schema Article + FAQPage; Title ~65 знаков; Featured Snippet / AI-ответы | Кейс «+140% трафика за 3 недели» без верифицируемого источника; перегруз agency-экспертизой; GEO как побочный эффект E-E-A-T, не отдельный блок | Непроверенные проценты в кейсах; копировать 7-разделную структуру 1:1 |
| 3 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | SEO-агентство (апр./июн. 2026) | Короткий, понятный принцип «полный ответ на одной странице»; LSI и «хвосты»; поведенческий сигнал (не возвращаться в поиск) | Мало практики: нет чек-листа, FAQ, schema, GEO; короткий объём (~1,5k знаков) | Формулировки «просто следуй принципам» без actionable шагов |
| 4 | [audit4seo.ru/blog/geo-optimizaciya-2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | GEO-гайд (2026) | Атомарные чанки, front-loading, conversational queries, llms.txt, Schema; сравнение SEO vs GEO; ссылка на Aggarwal et al. | Фокус на GEO, не на написании SEO-статьи; часть цифр без первичного источника | Таблицу SEO vs GEO можно адаптировать, не копировать блоки про AI-трекеры |
| 5 | [digitalimpuls.ru/blog/geo-optimization-2026/](https://digitalimpuls.ru/blog/geo-optimization-2026/) | GEO-агентство (2026) | Share of Voice, Citation Share; AI-краулеры (GPTBot, ClaudeBot и др.); llms.txt (сент. 2024, Jeremy Howard); интеграция SEO+GEO | Коммерческий кейс ASHA; цены GEO; длинный sales-narrative | Прайсы и демо-страницы агентства; непроверенные «1,5–2×» без источника |

**Паттерн SERP:** топ — «полный гайд 2026» с E-E-A-T, Wordstat, чек-листом. Отдельный кластер — GEO-лонгриды. Прямого совпадения с H1 «которые читают люди» в топе почти нет (bestseoserg.com — близкий заголовок, но слабее по глубине).

**Intent:** how_to — пользователь хочет пошаговую систему: собрать семантику → структура → текст → техника → проверка. Вторичный intent: понять связку SEO + GEO в одном материале.

**SERP refresh (WebSearch, 09.10.2026):** в топе усилились пошаговые гайды 2026 с явным чеклистом — [SEO Школа (7 шагов)](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/), [Private SEO (обнов. 28.09.2026)](https://private-seo.ru/blog/kak-pisat-seo-optimizirovannye-teksty-kotorye-nravyatsya-lyudyam), [OlegWeb (13 шагов до WordPress)](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/), [1PS.ru — SEO+ИИ 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/), [Seotika — структура ТОП 2026](https://seotika.ru/kak-pisat-seo-stati/). Официальный якорь — [Яндекс B2B — SEO-текст](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat). GEO-кластер: [Sergei Sivkov — формула GEO-абзаца](https://www.sergeisivkov.ru/blog/kontent-dlya-geo/), [Click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizovat-teksty-dlya-poiska-i-ii-otvetov/). Пробел для B01 сохраняется: мало материалов, где **один workflow** связывает «читают люди» + SEO-технику + GEO-чанки без agency-sales.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 09.10.2026)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` недоступен в среде Cloud Agent (namespace не подключён). Вызов `wordstat_get_top_requests` для `как писать seo статьи`, `seo текст для блога`, `geo оптимизация статьи` **не выполнен** — **точные показы в месяц не получены**. Обновите токен и подключите MCP: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса

| Фраза | Показы/мес |
|-------|------------|
| как писать seo статьи | — (MCP недоступен) |
| seo текст для блога | — |
| geo оптимизация статьи | — |

### LSI для writer (из SERP WebSearch + карточка B01, без подстановки цифр Вордстат)

- как писать seo текст / seo статью в 2026, пошаговый гайд, чек-лист перед публикацией  
- seo текст для блога, longread, структура H1 H2 H3, lead-абзац, первые 100 слов  
- title description h1, естественные ключи, LSI, переспам, тошнота, уникальность  
- geo оптимизация статьи, generative engine optimization, FAQPage schema, атомарные абзацы  
- wordstat яндекс, семантика, интент, топ выдачи, внутренние ссылки, alt изображений  

**SEO-стратегия (экспертная, до появления Wordstat):** primary «как писать seo статьи» — H1/lead; secondary «seo текст для блога» — блок про longread и читабельность; «geo оптимизация статьи» — отдельный H2-workflow, не отдельная статья.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата источника | Можно в текст |
|------|----------|----------------|---------------|
| Универсального объёма SEO-статьи не существует — он зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 должен отличаться от Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Title — ориентир ~65 знаков, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Schema.org: Article + FAQPage для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| GEO (Generative Engine Optimization) — оптимизация для цитирования в ответах AI, не замена SEO | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Нейросети извлекают пассажи (passages), не страницы целиком — каждый H2-блок = «остров смысла» | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Первые 100–150 слов страницы — ключевая зона для извлечения ответа AI | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Стандарт llms.txt предложен в сентябре 2024 (Jeremy Howard / Answer.AI) | [Digital Impuls — GEO 2026](https://digitalimpuls.ru/blog/geo-optimization-2026/) | 2026 | да |
| Алиса AI встроена в основную выдачу Яндекса с осени 2024 | [Digital Impuls — GEO 2026](https://digitalimpuls.ru/blog/geo-optimization-2026/) | 2026 | да |
| 39% россиян хотя бы раз пробовали нейросети (ВЦИОМ, август 2024) | [Digital Impuls — GEO 2026](https://digitalimpuls.ru/blog/geo-optimization-2026/) | 2026 | да* |
| ~20% месячной интернет-аудитории РФ — пользователи ChatGPT (Mediascope, август 2024) | [Digital Impuls — GEO 2026](https://digitalimpuls.ru/blog/geo-optimization-2026/) | 2026 | да* |
| Главная задача статьи — полный ответ на запрос; если пользователь возвращается в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 10.06.2026 | да |
| SEO-текст в 2026 — полезный текст под конкретный запрос: семантика → структура → написание → Title/Description → проверка → публикация и контроль (7 шагов) | [SEO Школа — как писать SEO-текст](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| Title — ориентир до 55–60 символов; основной запрос ближе к началу; Description — до ~160 символов, один ключ, выгода | [SEO Школа — как писать SEO-текст](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| Порядок работы: сначала спрос и выдача, потом структура, затем текст; иначе «гладкий» текст без позиций | [Private SEO — пошаговая инструкция](https://private-seo.ru/blog/kak-pisat-seo-optimizirovannye-teksty-kotorye-nravyatsya-lyudyam) | 28.09.2026 | да |
| SEO-статья: введение (зачем читать), основная часть по шагам, заключение со следующим шагом; H1 один раз | [Яндекс B2B — SEO-текст](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 2026 | да |
| Лид — прямой ответ в первых 2–3 предложениях; H2 как ответы на подвопросы (часто попадают в сниппет/PAA) | [Seotika — SEO-статьи в ТОП](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| GEO-абзац для цитирования: самодостаточный блок ~60–100 слов; структура «ответ → пояснение → вывод» | [Sergei Sivkov — контент для GEO](https://www.sergeisivkov.ru/blog/kontent-dlya-geo/) | 2026 | да* |

\* Вторичный источник (агентский блог со ссылкой на ВЦИОМ/Mediascope). В тексте — «по данным исследований 2024 года» без точной цифры, если QA не найдёт первичник.

\* Sivkov ссылается на кампании GenOptima — проценты «60% / 25% / 15%» **не использовать** без первичника.

**Не использовать в тексте (нет в fact-bank / непроверено):** «+140% трафика за 3 недели» (Pikapuka); «AI обрабатывает 25% запросов» (audit4seo без первичника); «микроразметка повышает цитирование в 1,5–2 раза» (Digital Impuls без первичника); «Aggarwal +40% видимости» — можно упомянуть как исследование, без точного % без arxiv.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему это отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды перегружены E-E-A-T-кейсами и CTA.
- H1 из карточки B01 («которые читают люди») — слабо раскрыт в SERP; наш фокус: **читабельность как SEO-фактор** (структура, инфостиль, «острова смысла») + техника.

**Режим B — как применить:** сама статья B01 — **эталон**: 8,5–9,5k знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead-абзац с определением, внутренняя перелинковка на `/`.

**Tone (site-brief):** практично, по-человечески, редакция бренда; без корпоративной воды и эмодзи.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (не два проекта, один контент)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов, printable logic)

Дополнительные подтемы для глубины (внутри блоков, не отдельные H2 верхнего уровня): семантика/Wordstat, Title/Description, E-E-A-T lite, llms.txt, AI-краулеры в robots.txt.

---

## 5. GEO hooks (для writer и schema)

| Hook | Где в статье | Формат |
|------|--------------|--------|
| Определение SEO-статьи в 40–60 слов | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO в 40–60 слов | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | «Что такое GEO в SEO?», «Сколько символов нужно в SEO-статье?» | Вопрос в заголовке |
| FAQ 5–7 пар | Конец longread | Короткий ответ 2–4 предложения |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; 3–4 предложения в абзаце |
| Island test | QA для writer | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Даты | Метаданные | datePublished / dateModified = 2026-10-09 |
| llms.txt | Упоминание в GEO-блоке | Что это и зачем для блога |
| E-E-A-T lite | Автор/редакция | Имя, роль, без выдуманных регалий |
| Внутренняя ссылка | Из карточки | На `/` (главная) |
| Alt обложки | Cover | «Редактор за ноутбуком…» (cover_scene_hint) |

**Целевые AI-формулировки для вкрапления:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и конкуренты в SERP; для how-to longread в Excalibur — 8 500–9 500 знаков текста.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах, база — индексируемый и структурированный контент.
3. **Нужно ли переспамить ключевые слова в 2026 году?** — нет; естественные вхождения + LSI/тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — заголовок на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage для блока вопросов.
6. **Что такое llms.txt и нужен ли он блогу?** — файл для AI-краулеров; полезный сигнал, не замена sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски и blockers для writer

- Не выдумывать статистику; использовать только таблицу фактов выше.
- Не копировать структуру Pikapuka (7 разделов) 1:1.
- Объём текста: 8 500–9 500 знаков (quality-blog.md).
- Без эмодзи, без VPN/обход блокировок.
- site_url example.com — в ссылках использовать плейсхолдер или `/` по карточке.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за один проход соберёт семантику под запрос, спланирует longread (H1–H3 + lead), напишет текст «для людей» с техникой SEO, добавит FAQ/schema и GEO-чанки и проверит материал чеклистом перед публикацией.

**action_outline (для writer):**

1. **Интент и спрос:** зафиксировать primary «как писать seo статьи»; собрать кластер (Wordstat/Вебмастер + 3–5 LSI из SERP); отсечь запросы без how-to интента.  
2. **Разбор топ-5 SERP:** выписать общие H2, форматы (списки, таблицы, FAQ), пробелы (читабельность + GEO в одном workflow).  
3. **Outline:** H1 из карточки; 4 опорных H2 из `blog-topics.md`; под каждым H2 — тезис в первом предложении (island test).  
4. **Lead и черновик:** ответ на запрос в первых 2–3 абзацах; абзацы 3–5 строк; списки/таблицы; ключи естественно (H1, lead, 1–2 H2), без переспама.  
5. **Мета и медиа:** Title ~55–60 зн., Description ~150–160 зн., H1 ≠ Title; alt у изображений; внутренняя ссылка на `/`.  
6. **GEO-слой:** атомарные блоки 60–100 слов под H2; FAQ 5–7 пар; BlogPosting + FAQPage (schema — отдельная роль).  
7. **Чеклист публикации:** семантика, мета, структура, уникальность, ссылки, FAQ/schema handoff, финальный island/so-what test.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (5 + refresh 2026) |
| Wordstat MCP | ⚠️ недоступен (AUTH/namespace) |
| Таблица фактов с URL | ✅ (22+ факта) |
| utility_verdict + action_outline | ✅ |
| GEO hooks | ✅ |
| FAQ-кандидаты 5–7 | ✅ |
| Режим B описан | ✅ |
| H2 outline | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `blog-topics.md` + `site-brief.md`.
