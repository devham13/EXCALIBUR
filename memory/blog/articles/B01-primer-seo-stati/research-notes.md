# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-08-26  
**disclaimer:** Все даты, версии и статистика проверены на 26.08.2026 (2026 год).

---

## Utility gate

| Проверка | Результат |
|----------|-----------|
| Gate 0 (`excalibur_blog_utility_gate.py --topic-id B01`) | **PASS** |
| `search_intent` | `how_to` |
| `article_mode` | B |
| `utility_verdict` | **PASS** |

**reader_outcome:** После гайда читатель сможет самостоятельно пройти полный цикл — от проверки спроса и разбора SERP до структуры longread, черновика «для людей», SEO/GEO-упаковки (FAQ, schema) и финального чеклиста перед публикацией.

**action_outline (workflow для writer):**

1. **Спрос и интент** — primary query в Wordstat/Вебмастер; классифицировать intent (информационный how-to); выписать 5–10 LSI из «похожих» и подсказок SERP.
2. **Разбор конкурентов** — ТОП-5–10: формат (гайд/чек-лист), глубина, пробелы; не копировать структуру 1:1.
3. **Каркас до текста** — H1 (один) + 4–6 H2 по кластерам; под каждым H2 — answer-first абзац; H3 только для деталей.
4. **Черновик для людей** — короткие абзацы (3–5 строк), списки/таблицы, один кейс или цифра с URL; без «воды» и переспама ключей.
5. **Семантика и мета** — ключ в H1, первом абзаце, 1–2 H2; Title ≠ H1 (~60–65 знаков); Description ~140–160 знаков с обещанием результата.
6. **GEO-слой** — атомарные блоки под AI-выдачу; FAQ 5–7 пар (ответ 2–4 предложения); упоминание llms.txt и robots для AI-ботов — без подмены SEO.
7. **Техника** — alt у изображений, внутренние ссылки, BlogPosting + FAQPage (JSON-LD вне body).
8. **Финальный чеклист** — 15–20 пунктов: intent закрыт, мета, schema, читабельность, island test по H2.

---

## 1. SERP-обзор (WebSearch, 26.08.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | 5 шагов workflow; Wordstat + Вебмастер; примеры «плохо/хорошо»; естественность ключей; alt, мета, перелинковка | Нет GEO/нейропоиска; CTA Директа | Блок про Директ; канон H1–H4 без GEO-слоя |
| 2 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (май 2026) | Интент, LSI, Wordstat; E-E-A-T; Title ~65 знаков; Schema Article + FAQPage | Кейсы с непроверенными %; перегруз agency-tone | «+140% трафика» и др. цифры без первичника |
| 3 | [fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | Агентство (июнь 2026) | Плотность информации > длина; answer-first; атомарные ответы для AI; pillar/cluster; чек-лист E-E-A-T; позиция Яндекс/Google по ИИ-контенту | Длинный narrative; мало пошагового «с нуля» для блога | Таблицу «ИИ vs эксперт» 1:1 как единственный аргумент |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Практик (2026) | Пошагово «сначала смысл, потом оптимизация»; H2 = подтема + ответ сразу; промпты для ИИ | Фокус на ИИ-генерации, не на «читают люди» | Структуру 1:1; блок «пишите только с ИИ» |
| 5 | [serpjet.ru/blog/chek-list-idealnoj-seo-stati-v-2026-ot-semantiki-do-cta-zamenit-seo-spetsialista-4847/](https://serpjet.ru/blog/chek-list-idealnoj-seo-stati-v-2026-ot-semantiki-do-cta-zamenit-seo-spetsialista-4847/) | Чек-лист + SaaS (2026) | Кластеры по intent; промпт vs «плохой промпт»; H1–H3 как воронка | Sales SerpJet; цифры «70% экономии» без первичника | Коммерческий CTA как ядро статьи |
| 6 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм (2026) | 13 шагов от ключа до WordPress; таблицы/списки; чек-лист перед публикацией | Узкий WP-контекст; GEO слабо | WP-only шаги без адаптации под generic CMS |
| 7 | [pawetta.com/baza/seo-tekst-kak-pisat/](https://pawetta.com/baza/seo-tekst-kak-pisat/) | База знаний (2026) | LSI из SERP; Title ≤60, Description 140–160; H2-вопросы под быстрые ответы Яндекса | Мало GEO; коммерческий уклон | Жёсткие нормы «сколько ключей» без контекста intent |
| 8 | [iq-maxima.ru/blog-iq/seo-statya-v-2026-godu-kak-pisat-pod-poisk-i-neyrovydaychu/](https://iq-maxima.ru/blog-iq/seo-statya-v-2026-godu-kak-pisat-pod-poisk-i-neyrovydaychu/) | SEO + нейровыдача (2026) | Связка классического SEO и AI-выдачи | Agency tone; часть тезисов без первичника | Копировать «нейровыдача заменит SEO» |

**Паттерн SERP (август 2026):** доминируют «полный гайд / чек-лист 2026» с E-E-A-T, Wordstat, answer-first и блоками под AI-выдачу. Запрос «как писать seo статьи» закрывают длинные инструкции; **H1 «которые читают люди»** в топе почти не встречается — дифференциатор Excalibur.

**Intent:** `how_to` — пошаговая система: семантика → структура → текст → мета/schema → GEO-чанки → проверка. Вторичные: `seo текст для блога` (формат и инфостиль), `geo оптимизация статьи` (упаковка под цитирование в AI).

**Пробел для Excalibur:** единый **практический workflow** «SEO + GEO в одной статье» с акцентом на **читабельность** (инфостиль, острова смысла), а не на переспам или agency-кейсы.

---

## 2. Яндекс Wordstat (MCP `user-mcp-kv`)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в текущем Cloud Agent окружении (`MCP server does not exist: user-mcp-kv`). Вызов `wordstat_get_top_requests` для primary и secondary queries **не выполнен**. Точные показы/мес **не получены** — цифры ниже не приводятся.

**Действие для пайплайна:** подключить MCP `user-mcp-kv` в environment + обновить OAuth-токен Wordstat:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Запросы для повторного прогона Wordstat

| query_id | Фраза | Назначение |
|----------|-------|------------|
| primary | как писать seo статьи | главный спрос |
| secondary_1 | seo текст для блога | LSI, H2 «формат блога» |
| secondary_2 | geo оптимизация статьи | GEO-блок |
| longtail | как написать seo статью | вариация (Pikapuka/SERP) |
| longtail | seo статья чеклист | intent checklist |
| longtail | структура seo статьи | H2-кандидат |

### LSI для writer (экспертная семантика по SERP + карточка B01; **без объёмов**)

- как писать seo статьи, как написать seo статью, seo текст для блога  
- семантическое ядро, wordstat, яндекс вебмастер, поисковый интент  
- h1 h2 h3, title description, мета-теги, перелинковка, alt-текст  
- lsi-слова, релевантность, переспам, инфостиль, чек-лист перед публикацией  
- e-e-a-t, личный опыт, кейс, answer-first, featured snippet  
- geo оптимизация статьи, generative engine optimization, нейровыдача, faq schema  
- blogposting, faqpage, llms.txt, pillar content, cluster content  

**SEO-стратегия (до получения Wordstat):** primary «как писать seo статьи» — H1/lead/Title; secondary «seo текст для блога» — блок инфостиля; «geo оптимизация статьи» — отдельный H2 «SEO + GEO»; faq_hints из карточки — в FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| # | Факт | Источник | Дата | Можно в текст |
|---|------|----------|------|---------------|
| 1 | Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 2 | Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 3 | H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 4 | Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 5 | Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 6 | Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 7 | Workflow Яндекса: тема → семантика → структура → текст → оптимизация (5 шагов) | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 8 | H1 должен отличаться от Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| 9 | Title — ориентир ~65 знаков, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| 10 | Schema.org: Article + FAQPage для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| 11 | В 2026 плотность информации важнее длины; ответ на запрос — в начале, без «воды» | [FireSEO — SEO-текст 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| 12 | Для AI-выдачи нужны атомарные, самодостаточные ответы; важную информацию не прятать во вкладки | [FireSEO — SEO-текст 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| 13 | Работает кластерный подход: pillar-гайд + 5–10 cluster-статей с перелинковкой | [FireSEO — SEO-текст 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| 14 | Яндекс и Google не запрещают ИИ-текст, если он полезен; массовая генерация без ценности — спам | [FireSEO — SEO-текст 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| 15 | Title до ~60 символов; Description 140–160 символов; LSI из топа выдачи | [Pawetta — SEO-текст](https://pawetta.com/baza/seo-tekst-kak-pisat/) | 2026 | да |
| 16 | После каждого H2 — сразу содержательный ответ; сначала смысл, потом оптимизация | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| 17 | GEO — оптимизация под цитирование в ответах генеративных систем; SEO остаётся базой индексации | [mayai.ru — GEO чек-лист](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да |
| 18 | FAQ-блок: 5–7 вопросов, ответы до ~80 слов; JSON-LD FAQPage | [mayai.ru — GEO чек-лист](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да |

**Не использовать (нет первичника / slop):** «+140% трафика за 3 недели» (Pikapuka); «экономия 70% времени менеджера» (SerpJet); медицинский кейс «−34% трафика / +41% бренд» (TenChat); «статья SerpJet с 15 000 до 500 ₽» без верификации.

**fact-bank.md:** прямых фактов по SEO-писательству нет; опираться на таблицу выше.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow** (см. action_outline): интент → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Отстройка от SERP:**
- Яндекс Direct — канон SEO без GEO.
- FireSEO / iq-maxima — AI/GEO, но слабее про «читают люди» как метод.
- Agency-гайды — перегруз E-E-A-T-кейсами и CTA.
- H1 карточки B01 («которые читают люди») — **редко в топе**; наш фокус: читабельность = SEO + GEO сигнал.

**Режим B:** статья B01 — **эталон** longread: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (из `blog-topics.md` + research):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как (JSON-LD вне body)  
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи (40–60 слов) | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO (40–60 слов) | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-adjacent | «Сколько символов…», «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец | 2–4 предложения, answer-first |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA | Блок понятен без соседних |
| Schema | meta/handoff | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Зачем блогу, не вместо sitemap |
| internal_links | из карточки | `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (факт #1); ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков текста.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемой базе (факт #17).
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI (факты #4, #16).
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 на странице; не дублировать (факты #8, #9, #15).
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage (факты #10, #18).
6. **Можно ли писать SEO-статью с помощью ИИ?** — да, если добавлена экспертиза и нет массового спама (факт #14).
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски и blockers для writer

- **Wordstat:** показы/мес не верифицированы — не выдумывать частотности; после подключения MCP обновить раздел 2.
- Не копировать структуру Pikapuka/SerpJet 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Цифры только из таблицы фактов §3.
- Без эмодзи, без VPN/обход блокировок.
- `site_url` example.com — плейсхолдер `/` по карточке.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate PASS | ✅ |
| `utility_verdict: PASS` | ✅ |
| `reader_outcome` + `action_outline` | ✅ |
| SERP ≥ 5 конкурентов (WebSearch 26.08.2026) | ✅ |
| Таблица фактов с URL (18 строк) | ✅ |
| Wordstat MCP | ⚠️ сервер недоступен |
| GEO hooks + FAQ 5–7 | ✅ |
| Режим B + H2 outline | ✅ |

**Writer:** готов при условии не использовать неподтверждённые частотности Wordstat. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.

---

**utility_verdict:** PASS
