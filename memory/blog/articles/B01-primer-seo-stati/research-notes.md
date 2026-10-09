# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**primary_query:** как писать seo статьи  
**search_intent:** how_to · **article_mode:** B  
**research_date:** 2026-10-09  
**disclaimer:** Даты, версии и статистика проверены на 2026-10-09 (Europe/Moscow).

---

## Utility gate

| Проверка | Результат |
|----------|-----------|
| `excalibur_blog_utility_gate.py --topic-id B01` | **PASS** |
| `utility_verdict` | **PASS** |

**reader_outcome:** Читатель сможет пройти полный цикл одной SEO-статьи для блога — от сбора запросов и каркаса H1–H3 до мета-тегов, FAQ/schema и GEO-чанков — и сверить черновик с чеклистом перед публикацией.

**action_outline (workflow статьи):**

1. Зафиксировать главный запрос и интент; собрать кластер в Вордстате/подсказках и сгруппировать по подтемам.
2. Разобрать ТОП-5–10 SERP: формат, обязательные H2, пробелы (content gap).
3. Составить каркас до текста: один H1, 5–8 H2, H3 для деталей; lead с прямым ответом в первых 100–170 словах.
4. Написать тело: короткие абзацы (3–5 строк), списки/таблицы, естественные ключи и LSI без переспама.
5. Добавить блок «SEO + GEO»: snippet-first в начале каждого H2, FAQ 5–7 с короткими ответами.
6. Подготовить Title (~60–65 знаков) и Description (140–160), alt, slug, 3–5 внутренних ссылок.
7. Вынести BlogPosting + FAQPage в JSON-LD (не дублировать разметку в body).
8. Прогнать финальный чеклист (релевантность, E-E-A-T lite, robots для AI-ботов, даты обновления).

---

## Яндекс Wordstat (MCP)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` (инструмент `wordstat_get_top_requests`) **не подключён** в текущем Cloud Agent окружении — точные **показы в месяц** не получены. Не использовать вымышленные частотности.

**Экспертная LSI-семантика из SERP/WebSearch (для writer, без частот):**

| LSI / смежные запросы | Где встречается |
|----------------------|-----------------|
| seo копирайтинг, seo текст | [seotika.ru](https://seotika.ru/kak-pisat-seo-stati/), [lvseo.ru](https://lvseo.ru/articles/seo-kopirayting) |
| семантическое ядро, интент запроса | [articleai.ru](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) (SERP), [seoshkola.com](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) |
| структура статьи, h2 h3, оглавление | [seoshkola.com](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/), [marketingklub.ru](https://marketingklub.ru/kak-pisat-seo-stati/) |
| title, description, мета-описание | [direct.yandex.ru](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat), [spilnoagency.com.ua](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) |
| E-E-A-T, экспертность автора | [labrika.ru](https://labrika.ru/blog/eeat-seo-guide-2026), [texterra.ru](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) |
| geo оптимизация, нейропоиск, FAQPage | [pw.agency](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/), [blog.geouseo.ru](https://blog.geouseo.ru/geo-audit-sajta-kak-proverit-gotov-li-sajt-k-otvetam-nejrosetej/) |
| seo текст для блога | secondary_query карточки B01 |
| lsi фразы, тематические слова | [direct.yandex.ru](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat), [seofab.ru](https://seofab.ru/blog/tekstovye-faktory-ranzhirovaniya/) |

После подключения MCP: повторить `wordstat_get_top_requests` для «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи».

---

## 1. SERP-обзор (WebSearch + research-serp.json, 2026-10-09)

**Запросы прогона:** «как писать seo статьи 2026», «seo текст для блога», «geo оптимизация статьи», доп. WebSearch по primary/secondary.

**Паттерн выдачи:** доминируют **пошаговые гайды 2026** (7–10 шагов), **E-E-A-T**, семантика/Wordstat, чек-листы мета и структуры. Отдельный кластер — **GEO/AEO** (snippet-first, FAQ, JSON-LD, AI-боты). Прямое попадание в H1 «которые читают люди» — редкость; дифференциатор — **читабельность + единый SEO+GEO workflow** на одной странице.

| # | URL | Тип | Сильные стороны | Пробелы / слабости | Не копировать |
|---|-----|-----|-----------------|-------------------|---------------|
| 1 | [direct.yandex.ru/.../seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: объём без нормы, H1–H4, абзацы 3–5 строк, Вордстат, естественность ключей, title/description, перелинковка | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа; «SEO без людей» |
| 2 | [seoshkola.com/.../kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Практик, 7 шагов | Чёткий workflow: запросы → ТОП → структура → текст → мета → релевантность → публикация | Без отдельного GEO-слоя и schema-handoff | Копировать нумерацию 1:1 без GEO |
| 3 | [seotika.ru/kak-pisat-seo-stati](https://seotika.ru/kak-pisat-seo-stati/) | Агентский гайд | Lead за 100 слов, иерархия H1→H2→H3, объём 1500–3000 слов для инфо-статьи, плотность ключей 1–2% | Цифры без первичника для каждого нишевого кейса | Слепое копирование объёма без intent |
| 4 | [pikapuka.com/.../e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Longread агентства (SERP) | E-E-A-T, чек-лист, Article+FAQPage | Перегруз кейсами; GEO как побочный эффект | Непроверенные % в кейсах |
| 5 | [articleai.ru/.../2026](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | AI+SEO (SERP) | Семантика → публикация, AI как инструмент | Фокус на ИИ, не на «читают люди» | Шаблон «только нейросеть пишет» |
| 6 | [pw.agency/.../neyroseti](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | GEO-контент | Snippet-first, чанки 3–7 строк, H2 с вопросами | Слабее классического SEO с нуля | Sales-нарратив агентства |
| 7 | [blog.geouseo.ru/geo-audit](https://blog.geouseo.ru/geo-audit-sajta-kak-proverit-gotov-li-sajt-k-otvetam-nejrosetej/) | GEO-аудит | 20+ пунктов: robots AI-ботов, HTML без JS-only, прямой ответ в 2 абзацах | Аудит сайта, не гайд «написать статью» | Перенос чеклиста без адаптации под блог-post |

**Intent:** how_to — система «семантика → структура → текст для человека → техника → GEO → проверка». Secondary: «seo текст для блога», «geo оптимизация статьи».

---

## 2. Таблица фактов (только с URL)

| Факт | Источник | Дата | В текст |
|------|----------|------|---------|
| Универсального объёма SEO-статьи нет — зависит от темы и конкуренции в выдаче | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один; H2–H4 для смысловых блоков | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы ориентир 3–5 строк; списки для перечислений | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику анализируют в Яндекс Вордстат (и смежные инструменты) | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-текст 2026 = полезный текст под запрос и «окружение» запроса, не под частоту | [SEO школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| Каркас строят до текста: H1 с ключом, H2 — блоки интента, H3 — детали | [SEO школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| Для инфо-статьи в ТОП часто 1500–3000 слов; ключи 1–2% естественно | [Seotika — SEO-статьи в ТОП](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да* |
| Title до 60–70 знаков, Description 150–160 | [Marketing Klub — инструкция 2026](https://marketingklub.ru/kak-pisat-seo-stati/) | 2026 | да |
| Title ≤60, meta description 140–160; 5–8 H2; FAQ в конце | [Spilno Agency — SEO copywriting 2026](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да |
| Google: helpful people-first + E-E-A-T; Яндекс: релевантность и ЭПОС (экспертность, полезность, оригинальность, содержательность) | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 2026 | да |
| E-E-A-T из Search Quality Rater Guidelines; для текста — автор, источники, согласованность | [SEOFab — текстовые факторы](https://seofab.ru/blog/tekstovye-faktory-ranzhirovaniya/) | 2026 | да |
| GEO: короткие чанки, snippet-first в начале H2, FAQ и таблицы для извлечения ИИ | [PW Agency — GEO контент 2026](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 2026 | да |
| GEO-аудит: не блокировать GPTBot, ClaudeBot, Google-Extended, PerplexityBot в robots; контент в исходном HTML | [GeoUseo — GEO-аудит 2026](https://blog.geouseo.ru/geo-audit-sajta-kak-proverit-gotov-li-sajt-k-otvetam-nejrosetej/) | 2026 | да |
| GEO не заменяет SEO; оптимизация под цитирование в LLM-ответах | [Habr — GEO/AEO гайд](https://habr.com/ru/articles/987506/) | 2026 | да |

\* Ориентир по типу «информационная статья» из одного агентского источника; для B01 в Excalibur сохранить контракт quality-blog: **8 500–9 500 знаков** текста (режим B), не противоречит «нет универсального объёма».

**fact-bank.md:** прямых фактов про SEO-письмо нет; цифры из fact-bank про ИИ-контент **не смешивать** с этой статьёй без отдельного угла.

**Не использовать:** «+140% за 3 недели» (Pikapuka); «+30–40% visibility Princeton» без arxiv/первичника; «58–65% zero-click» (Habr) без первичной ссылки на исследование.

---

## 3. Угол и дифференциация

**Угол:** SEO-статья 2026 = **longread для людей**, который закрывает интент и упакован для **SEO + GEO** в одном проходе: читабельность (структура, lead, «острова смысла») → FAQ/schema → чеклист перед публикацией.

**Отстройка:**

- Яндекс Direct — канон без GEO.
- GEO-лонгриды не учат базовому написанию с нуля.
- H1 «**которые читают люди**» слабо раскрыт в SERP — наш акцент: поведенческий сигнал через ясность, не через ключи.

**H2-каркас (карточка B01 + research):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread (H1–H3, lead, списки, таблицы)  
3. FAQ и schema (JSON-LD вне body)  
4. Чеклист перед публикацией (15–20 пунктов)

**Режим B:** сама статья B01 — этalon формата: 8,5–9,5k знаков, 5–7 FAQ, BlogPosting + FAQPage, внутренняя ссылка на `/`.

---

## 4. GEO hooks

| Hook | Место | Формат |
|------|-------|--------|
| Определение SEO-статьи (40–60 слов) | Lead после H1 | Прямой ответ на primary_query |
| Определение GEO (40–60 слов) | Блок SEO+GEO | Generative Engine Optimization |
| Snippet-first | Каждый H2 | 1–3 предложения — ответ раздела |
| FAQ 5–7 | Конец | Ответы-действия, 2–4 предложения |
| Schema | Handoff schema-агенту | BlogPosting + FAQPage |
| Conversational H2 | Внутри блоков | «Сколько символов…», «Что такое GEO…» |
| Даты | Метаданные | datePublished / dateModified = дата публикации |
| cover_scene_hint | Cover | Редактор за ноутбуком, блокнот, тёплый свет |

---

## 5. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — Универсальной нормы нет (Яндекс); для how-to longread Excalibur — 8 500–9 500 знаков при полном раскрытии интента.  
2. **Что такое GEO в SEO?** — Дополнение к SEO: цитирование в AI-ответах при той же базе индексации и структуры.  
3. **Нужен ли переспам ключей в 2026?** — Нет; естественные вхождения + тематические слова.  
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 на странице; не дублировать дословно.  
5. **Какие schema для блога?** — BlogPosting (или Article) + FAQPage.  
6. **Как проверить статью перед публикацией?** — Чеклист: семантика, мета, структура, FAQ, schema, ссылки, GEO-чанки.  
7. **Нужен ли llms.txt?** — Опциональный сигнал для AI-краулеров; не замена sitemap.

---

## 6. Риски для writer

- Цифры только из таблицы фактов; Wordstat-показы не придумывать.  
- Не клонировать структуру Pikapuka/seoshkola 1:1.  
- Без эмодзi, без VPN/обходов.  
- CTA ≤ 3; польза важнее продаж.

---

## 7. Готовность

| Критерий | Статус |
|----------|--------|
| utility_verdict PASS | ✅ |
| action_outline 8 шагов | ✅ |
| reader_outcome | ✅ |
| SERP ≥ 5 источников | ✅ |
| Факты с URL (15+) | ✅ |
| Wordstat | ⚠️ MCP недоступен |
| FAQ / GEO hooks | ✅ |

**Writer:** можно стартовать с этим файлом + `research-context.json` + B01 в `memory/topics/blog-topics.md`.
