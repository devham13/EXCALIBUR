# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-09-07  
**disclaimer:** Все даты, версии и статистика проверены на 07.09.2026 (2026 год).

---

## Utility gate

| Поле | Значение |
|------|----------|
| `utility_verdict` | **PASS** |
| `search_intent` | how_to |
| `article_mode` | B |
| Gate topic (B01) | PASS (`scripts/excalibur_blog_utility_gate.py`) |

**reader_outcome:** Читатель сможет самостоятельно написать и опубликовать SEO-статью для блога: собрать семантику, построить структуру longread, добавить FAQ/schema, упаковать блоки под GEO и пройти финальный чеклист перед публикацией.

**action_outline (workflow 8 шагов):**

1. Проверить спрос и интент запроса в Вордстате и SERP (информационный / коммерческий / практический).
2. Собрать семантический кластер: primary query + 15–25 LSI-фраз, сгруппировать в 3–5 смысловых блоков.
3. Разобрать топ-5 конкурентов: формат, глубина, FAQ, schema, пробелы — составить outline H1–H3.
4. Написать lead-абзац с прямым ответом (40–60 слов) и черновик по H2 (сначала смысл, потом ключи).
5. Добавить E-E-A-T lite: примеры, таблицы, списки, alt-теги; главный ключ — в H1, первый абзац, 1–2 H2, Title, Description.
6. Собрать FAQ (5–7 пар «вопрос → короткий ответ-действие») и GEO-чанки: атомарные абзацы 40–80 слов после каждого H2.
7. Прописать Title, Description, внутренние ссылки; подготовить BlogPosting + FAQPage JSON-LD (вне body).
8. Пройти чеклист перед публикацией: семантика, мета, структура, читабельность, schema, robots.txt для AI-краулеров.

---

## 1. Яндекс Вордстат (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в текущей Cloud-сессии (`MCP server does not exist: user-mcp-kv`). Инструмент `wordstat_get_top_requests` не вызван — **точные объёмы показов в месяц не получены**.

Обновите токен и подключение MCP через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

| Фраза | Показы в месяц |
|-------|----------------|
| как писать seo статьи | *не получено — MCP недоступен* |
| seo текст для блога | *не получено — MCP недоступен* |
| geo оптимизация статьи | *не получено — MCP недоступен* |

**LSI-ключи (экспертная оценка по SERP и конкурентам, не из API Вордстата):**

- как написать seo статью пошагово
- seo текст для сайта как писать
- seo копирайтинг 2026
- семантическое ядро для статьи
- структура seo статьи h1 h2
- title description для статьи
- lsi ключевые слова
- e-e-a-t в seo тексте
- faq schema для статьи
- geo оптимизация контента
- как писать для нейропоиска
- чеклист seo статьи перед публикацией
- интент запроса seo
- переспам ключевых слов
- внутренняя перелинковка блога

Writer: при появлении MCP — перезапросить `wordstat_get_top_requests` для primary и secondary queries и заменить оценочные LSI на данные таблицы.

---

## 2. SERP-обзор (WebSearch, 07.09.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Авторитет; workflow «тема → семантика → структура → текст → оптимизация»; H1 один раз; естественность ключей; Wordstat + Вебмастер | Нет GEO-слоя; CTA Директа | Блок про Директ; дублировать H1–H4 без GEO |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 2026 (13 шагов) | Полный цикл от спроса до WordPress; чек-лист 14 пунктов; FAQ; таблицы форматов контента | Фокус на WP-сайты, не на блог-формат Excalibur | Копировать 13 шагов 1:1 |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread агентства (2026) | Кластеры из Вордстата; сравнение «старый SEO vs 2026»; GEO-блок; мета-таблица Title/Description/H1 | Длинный sales-narrative; «+15–30% CTR» без первичника | Таблицу мета — адаптировать, не копировать блоки про ИИ-завод |
| 4 | [fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | SEO-агентство (2026) | Pillar + Cluster; атомарные ответы для ИИ; FAQ; интерактив (оглавление, аккордеоны) | Мало конкретного чеклиста публикации | Модель pillar/cluster — упомянуть, не раздувать |
| 5 | [habr.com/ru/articles/1042732](https://habr.com/ru/articles/1042732/) | GEO/AEO гайд 2026 | RAG-архитектура; Schema FAQPage/Article; robots.txt для AI-краулеров; Answer-First | Фокус GEO, не написание с нуля; часть цифр — вторичные | Цены GEO-кампаний; кейсы агентств |
| 6 | [exlibris.ru/academy/formula-seo-teksta-kak-vyvesti-blog-v-top-vydachi](https://exlibris.ru/academy/formula-seo-teksta-kak-vyvesti-blog-v-top-vydachi/) | Академия (2026) | План статьи до черновика; Article + FAQPage; перелинковка до публикации | Мало GEO; без универсального чеклиста | Agency CTA |

**Паттерн SERP:** топ — «полный гайд 2026» с пошаговым workflow, Wordstat, E-E-A-T, чек-листом. Отдельный кластер — GEO/AEO-лонгриды. H1 «которые читают люди» в выдаче встречается редко — дифференциатор Excalibur.

**Intent:** how_to — пользователь хочет систему «семантика → структура → текст → техника → проверка». Вторичный intent: связка SEO + GEO в одном материале для блога.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата источника | Можно в текст |
|------|----------|----------------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Главный ключ — в H1, первом абзаце, 1–2 H2, Title и Description; LSI — по тексту естественно | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| H1 не должен дословно совпадать с Title (может быть близок по смыслу) | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| После каждого H2 — сразу содержательный ответ (не откладывать суть) | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Семантический кластер — 3–5 смысловых групп из фраз Вордстата | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Для ИИ важны атомарные самодостаточные ответы; FAQ, списки, таблицы; не прятать суть во вкладки | [FireSEO — SEO-тексты 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| Pillar Content — большой обзорный гайд; Cluster — 5–10 узких статей со ссылками на pillar | [FireSEO — SEO-тексты 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| Если интент практический — нужны шаги, таблицы, чек-листы; теория без действий → возврат в поиск | [olegweb.ru — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 2026 | да |
| Перед публикацией — чеклист: Title, Description, H1, H2/H3, alt, внутренние ссылки, FAQ | [olegweb.ru — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 2026 | да |
| GEO/AEO: Schema.org Article, FAQPage, HowTo; robots.txt — не блокировать AI-краулеров | [Habr — GEO/AEO 2026](https://habr.com/ru/articles/1042732/) | 2026 | да |
| Answer-First: прямой ответ в первых 2–5 предложениях раздела (удобно для RAG-извлечения) | [Habr — GEO/AEO 2026](https://habr.com/ru/articles/1042732/) | 2026 | да |
| Оптимальный блок ответа для GEO — 40–80 слов | [trigub.ru — GEO 2026](https://trigub.ru/blog/geo-prodvizhenie-sayta/) | 2026 | да |
| Schema: Article для статей, FAQPage для блока вопросов (если блок реально на странице) | [exlibris.ru — формула SEO-текста](https://exlibris.ru/academy/formula-seo-teksta-kak-vyvesti-blog-v-top-vydachi/) | 2026 | да |

**Не использовать (нет первичника / не в fact-bank):** «+15–30% CTR от description» (1ps без источника); «+40% к ранжированию от статистики» (Habr, ссылка на Aggarwal — без arxiv в research); «HubSpot −70–80% трафика» (Habr, вторичный); «357% рост AI-переходов» (Habr/TechCrunch — только с первичником).

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды перегружены E-E-A-T-кейсами и CTA.
- H1 B01 («которые читают люди») — слабо раскрыт в SERP; фокус Excalibur: **читабельность как SEO-фактор** + техника.

**Режим B:** сама статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Первый абзац после H1 | 40–60 слов |
| Определение GEO | Блок «SEO + GEO» | 40–60 слов |
| Conversational H2 | FAQ-подтемы | «Что такое GEO в SEO?», «Сколько символов…» |
| FAQ 5–7 пар | Конец longread | 2–4 предложения, ответ-действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Кратко: что и зачем |
| E-E-A-T lite | Автор/редакция | Имя, роль, без выдуманных регалий |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и конкуренты; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета, H1 — на странице; не дублировать дословно.
5. **Какие schema для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt?** — файл-подсказка для AI-краулеров; не замена sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать статистику; только таблица фактов выше.
- Не копировать структуру olegweb (13 шагов) или 1ps 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Без эмодзи, без VPN/обход блокировок.
- Wordstat-показы — не указывать до получения MCP.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate topic | ✅ PASS |
| `utility_verdict` / `reader_outcome` / `action_outline` | ✅ |
| SERP ≥ 5 конкурентов (WebSearch 07.09.2026) | ✅ |
| Таблица фактов ≥ 15 с URL | ✅ |
| Wordstat MCP | ⚠️ недоступен — LSI оценочные |
| GEO hooks + FAQ 5–7 | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + B01 в `blog-topics.md` + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅
utility_verdict: PASS
wordstat: ⚠️ MCP user-mcp-kv недоступен — показы не получены; LSI оценочные из SERP
summary: SERP — 6 конкурентов (Яндекс Direct, olegweb, 1ps, FireSEO, Habr GEO, Ex Libris). Угол — единый workflow SEO+GEO longread «для людей»: 8 шагов action_outline, 18 фактов с URL, 7 FAQ. Готов к writer.
===
