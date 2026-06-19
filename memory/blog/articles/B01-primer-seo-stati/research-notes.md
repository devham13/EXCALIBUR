# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-06-19  
**disclaimer:** Все даты, версии и статистика проверены на 19.06.2026. Предпочтительные источники — после 01.06.2026.

---

## Utility gate

| Поле | Значение |
|------|----------|
| **utility_verdict** | **PASS** |
| **search_intent** | how_to |
| **article_mode** | B |

**reader_outcome:** После гайда читатель сможет самостоятельно пройти единый workflow SEO+GEO longread — от интента и семантики в Wordstat до структуры с «островами смысла», FAQ, JSON-LD и финального чеклиста перед публикацией.

**action_outline (8 шагов):**

1. **Интент и цель** — зафиксировать, что пользователь хочет сделать (how-to / чеклист), и какой результат обещает статья.
2. **Семантика** — собрать primary + secondary + LSI в Яндекс Вордстат и Вебмастер; сгруппировать в один тематический кластер на страницу.
3. **SERP-разбор** — изучить ТОП-10 по главному запросу: структура, форматы, пробелы; составить outline H2/H3 под полный ответ.
4. **Каркас longread** — H1 (один), lead-абзац с определением, H2-чанки с answer-first (2–3 предложения сразу под заголовком).
5. **Текст для людей** — короткие абзацы (3–5 строк), списки/таблицы, естественные ключи без переспама; E-E-A-T lite (автор, опыт, факты с URL).
6. **Мета и техника** — Title (~50–65 знаков, ≠ H1), Description, alt, 3–5 внутренних ссылок, URL-slug.
7. **FAQ + GEO-слой** — 5–7 пар вопрос–ответ; BlogPosting + FAQPage в JSON-LD (не в body); упоминание llms.txt как опционального эксперимента.
8. **Чеклист перед публикацией** — 15–20 пунктов: семантика, мета, структура, читабельность, schema, ссылки, island test.

---

## 1. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` не подключён в Cloud-окружении (`wordstat_get_top_requests` недоступен). Точные объёмы показов **не получены**. Обновите токен и подключите MCP через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (без цифр показов — только для ориентира writer)

| Кластер | Фразы | Интент |
|---------|-------|--------|
| Primary | как писать seo статьи, как написать seo статью, seo текст для блога | how_to |
| Secondary | geo оптимизация статьи, оптимизация под ai overviews, seo копирайтинг 2026 | how_to + GEO |
| LSI (из SERP + конкурентов) | семантическое ядро, wordstat, e-e-a-t, title description, schema faqpage, lsi, интент, чеклист, featured snippet, llms.txt, атомарные чанки, answer-first | информационный |

**Writer:** в тексте ссылаться на [wordstat.yandex.ru](https://wordstat.yandex.ru/) и [webmaster.yandex.ru](https://webmaster.yandex.ru/) как на инструменты сбора семантики; **не** указывать показы/мес без данных Wordstat.

---

## 2. SERP-обзор (WebSearch, 19.06.2026)

Источник: нативный WebSearch + сверка с `research-serp.json`. Приоритет — гайды 2026, how-to, чеклисты.

| # | URL | Тип | Дата | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|------|-----------------|------------------|---------------|
| 1 | [direct.yandex.ru/.../seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса | 27.01.2026 | Канон: workflow, H1–H4, Wordstat, естественность ключей, абзацы 3–5 строк, нет универсального объёма | Нет GEO/нейропоиска; CTA Директа | Блок про Директ; дублировать H-иерархию без GEO |
| 2 | [pikapuka.com/.../kak-napisat-seo-tekst-samomu](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread | 09.05.2026 | Семантика, E-E-A-T, чек-лист 10 шагов, Title ~65 знаков, Schema Article+FAQ | Кейсы с непроверенными %; GEO побочно | «+140% трафика»; структура 1:1 |
| 3 | [qvai.ru/media/kak-pisat-seo-stati](https://qvai.ru/media/kak-pisat-seo-stati) | Короткий гайд | 01.06.2026 | **H1 совпадает с карточкой B01**; принцип «для людей → для роботов»; тест читабельности без ключей | Мало техники: нет Wordstat, schema, GEO, чеклиста | Короткий формат без глубины |
| 4 | [habr.com/ru/articles/1030292](https://habr.com/ru/articles/1030292/) | GEO/AIO/AEO longread | 30.04.2026 | RAG-механика, FAQPage, GEO как надстройка SEO (40/35/25), извлекаемость | Не учит писать SEO-статью с нуля | Цифры «20–40% органики» без первичника в тексте |
| 5 | [olegweb.ru/.../kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый how-to | 05.02.2026 | 13+ шагов, WordPress, чеклист, интент → конкуренты → структура | Узкий уклон в WP; без GEO-блока | WP-only narrative как универсальный |
| 6 | [hozyindachi.ru/.../novye-pravila](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | SEO-гайд 2026 | 2026 | Кластеры семантики, AI Overview/Алиса, плотность ключа ≤2%, 7-шаговый план | Много коммерческих CTA | Плотность 2% как жёсткая норма без оговорки Яндекса |
| 7 | [trigub.ru/.../optimizatsiya-pod-ai-overviews](https://trigub.ru/blog/optimizatsiya-pod-ai-overviews-razbor-gayda-google-2026/) | Разбор гайда Google | 18.05.2026 | Позиция Google: GEO=AEO — то же SEO; прямой ответ под H2; mythbusting llms.txt | Фокус на Google, не на написании текста | Продавать llms.txt как приоритет |
| 8 | [audit4seo.ru/blog/geo-optimizaciya-2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | GEO-гайд | 2026 | SEO vs GEO, атомарные чанки, front-loading | Отдельно от SEO-writing | Непроверенные % AI-трафика |

**Паттерн SERP (июнь 2026):** доминируют «полный гайд 2026» (1ps, pikapuka, seomatik, hozyindachi) + кластер GEO-лонгридов. Заголовок «которые читают люди» в топе представлен слабо (qvai.ru — короткая статья без workflow). **Пробел для Excalibur:** единый практический workflow SEO+GEO с акцентом на **читабельность как фактор удержания** и эталоном самой статьи B01.

**Intent:** how_to — пошаговая система: семантика → структура → текст → мета → FAQ/schema → GEO-упаковка → чеклист. Вторичный: связать SEO и GEO в одном материале без дублирования двух проектов.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата источника | Можно в текст |
|------|----------|----------------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 должен отличаться от Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Title — ориентир ~65 знаков, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Schema.org: Article + FAQPage для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Пишите для людей, оптимизируйте для поисковиков — в таком порядке | [qvai.ru — SEO-статьи для людей](https://qvai.ru/media/kak-pisat-seo-stati) | 01.06.2026 | да |
| Тест качества: без ключей текст остаётся полезным | [qvai.ru — SEO-статьи для людей](https://qvai.ru/media/kak-pisat-seo-stati) | 01.06.2026 | да |
| GEO — надстройка над SEO, не замена; без индекса RAG не возьмёт контент | [Habr — GEO/AIO/AEO](https://habr.com/ru/articles/1030292/) | 30.04.2026 | да |
| Распределение усилий 2026 (автор Habr): ~40% тех. SEO, ~35% GEO-контент, ~25% авторитет | [Habr — GEO/AIO/AEO](https://habr.com/ru/articles/1030292/) | 30.04.2026 | да* |
| Google: оптимизация под генеративный поиск = то же SEO, не отдельная дисциплина GEO/AEO | [Trigub — гайд Google 2026](https://trigub.ru/blog/optimizatsiya-pod-ai-overviews-razbor-gayda-google-2026/) | 18.05.2026 | да |
| Прямые ответы в 1–2 предложениях после H2 — измеримый приём для AI-цитирования | [Trigub — гайд Google 2026](https://trigub.ru/blog/optimizatsiya-pod-ai-overviews-razbor-gayda-google-2026/) | 18.05.2026 | да |
| Google не считает structured data обязательным условием AI-видимости | [Trigub — гайд Google 2026](https://trigub.ru/blog/optimizatsiya-pod-ai-overviews-razbor-gayda-google-2026/) | 18.05.2026 | да |
| Первый абзац должен отвечать на главный вопрос без «воды» | [hozyindachi.ru — SEO-тексты 2026](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | 2026 | да |
| Title 50–60 символов, Description 140–155 — тех. ориентиры | [hozyindachi.ru — SEO-тексты 2026](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | 2026 | да |
| Главная задача — полный ответ; возврат в поиск = сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 10.06.2026 | да |
| GEO (Generative Engine Optimization) — оптимизация для цитирования в AI-ответах | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Нейросети извлекают пассажи (passages), не страницы целиком — H2 = «остров смысла» | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |

\* Оценочная рамка одного автора; в тексте — «по оценкам практиков 2026», не как официальная норма.

**Не использовать в тексте (нет в fact-bank / непроверено):** «+140% трафика за 3 недели» (Pikapuka); «сайты теряют 20–40% органики» (Habr без первичника); «65% zero-click» (SparkToro вторично); «микроразметка ×1,5–2 цитирование»; «плотность ключа строго 2%» как универсальное правило.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска в **одном workflow**. Не «ещё один чек-лист ключей», а связка: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды перегружены E-E-A-T-кейсами и CTA.
- qvai.ru совпадает по H1, но без Wordstat, schema и чеклиста.
- **Фокус B01:** читабельность (структура, инфостиль, island test) + техника в одном материале.

**Режим B:** сама статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (не два проекта)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

**Tone:** практично, по-человечески, без корпоративной воды и эмодзи (site-brief).

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи (40–60 слов) | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO (40–60 слов) | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | Внутри блоков | «Что такое GEO в SEO?», «Сколько символов…» |
| FAQ 5–7 пар | Конец longread | Ответ 2–4 предложения, actionable |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; answer-first |
| Island test | QA | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Опциональный эксперимент, не приоритет над Schema |
| E-E-A-T lite | Автор/редакция | Имя, роль из registry |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и конкуренты в SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при сохранении индексируемого полезного контента.
3. **Нужно ли переспамить ключевые слова в 2026 году?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~50–65 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt и нужен ли он блогу?** — карта контента для части AI-агентов; полезный сигнал, не замена sitemap и Schema.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски и blockers для writer

- Не выдумывать статистику и показы Wordstat; только таблица фактов выше.
- Не копировать структуру Pikapuka (7 разделов) 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Без эмодзи, без VPN/обход блокировок.
- Цифры из `memory/brief/fact-bank.md` для B01 не добавлены — использовать только таблицу §3.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat (попытка MCP) | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + reader_outcome + action_outline | ✅ |
| Угол + дифференциация | ✅ |
| GEO hooks | ✅ |
| FAQ-кандидаты 5–7 | ✅ |
| Режим B описан | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `blog-topics.md` + `site-brief.md`.
