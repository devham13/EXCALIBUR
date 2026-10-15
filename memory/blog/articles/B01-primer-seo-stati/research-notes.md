# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-08-15  
**disclaimer:** Все даты, версии и статистика проверены на 15.08.2026.

---

## 1. SERP-обзор (WebSearch, август 2026 — 6 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Авторитет; пошаговый workflow; примеры «плохо/хорошо»; Wordstat, alt, мета, перелинковка; нет универсального объёма | Нет GEO/нейропоиска; CTA Директа в конце | Коммерческий блок Директа; копировать канон без GEO-слоя |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Практический longread (13 шагов) | Полный цикл от темы до WordPress; интент, конкуренты, чек-лист перед публикацией | Длинный; WordPress-специфика; GEO — побочно | 13 шагов 1:1; непроверенные кейсы |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | Кластеризация семантики; «сначала смысл, потом оптимизация»; LSI без переспама | Перегруз про ИИ; мало про GEO-структуру | Шаблон «полное руководство» без дифференциации |
| 4 | [tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | Формула + E-E-A-T | Lead с ответом; форматы под intent (FAQ, гайд, сравнение); дата обновления | Короткий; нет printable чек-листа | Agency-tone «мы делаем за вас» |
| 5 | [serptop.ru/blog/kak-pisat-seo-teksty](https://serptop.ru/blog/kak-pisat-seo-teksty/) | Гайд + чек-лист | Формула H1; каркас H2 (инструкция, ошибки, CTA); правила ключей без «плотности %» | Мало schema/GEO; agency CTA | Структура Serptop 1:1 |
| 6 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread | E-E-A-T, Schema Article+FAQPage, Title ~65 знаков | Кейсы «+140%» без первичника; 7 разделов agency-style | Непроверенные проценты; копировать структуру 1:1 |

**Паттерн SERP (август 2026):** топ — «гайд/алгоритм 2026» с E-E-A-T, Wordstat, пошаговым workflow. Прямого совпадения с H1 «которые читают люди» мало: конкуренты фокусируются на «SEO-текст» и «ключи», а не на **читабельности как SEO-факторе** + связке SEO+GEO в одном материале.

**Intent:** `how_to` — пользователь хочет **пошаговую систему**: интент → семантика → структура → текст → мета/schema → проверка. Вторичный intent: понять, как упаковать статью и для людей, и для нейропоиска (GEO).

**Пробел для Excalibur:** единый workflow «SEO + GEO longread для людей» с **чеклистом 15–20 пунктов** и демонстрацией формата на самой статье B01 (режим B).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер MCP `user-mcp-kv` недоступен в Cloud Agent окружении (вызов `wordstat_get_top_requests` невозможен). Точные объёмы спроса из Wordstat API **не получены**. Для обновления данных: настройте MCP в `.cursor/mcp.json` и авторизуйте Wordstat через [OAuth Яндекса](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40), затем перезапустите research.

**Ручная проверка (writer/QA):** [wordstat.yandex.ru](https://wordstat.yandex.ru/) → запросы `"как писать seo статьи"`, `seo текст для блога`, `geo оптimizaciya статьи` (регион 225).

### Экспертная семантика (без точных показов MCP)

| Кластер | LSI-фразы для writer |
|---------|----------------------|
| Primary | как писать seo статьи, как написать seo статью, seo текст для блога |
| Структура | структура seo статьи, заголовки h1 h2, title description seo |
| Процесс | семантическое ядро для статьи, seo копирайтинг, чеклист seo статьи |
| GEO-слой | geo оптимизация статьи, e-e-a-t, faq schema, нейропоиск |
| PAA / FAQ | сколько символов в seo статье, что такое geo в seo, нужен ли переспам ключей |

### Вторичный спрос (Serpstat g_ru, не Wordstat MCP)

Источник: [spilnoagency.com.ua — SEO копирайтинг 2026](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) — **использовать только с оговоркой «по данным Serpstat»**, не как Wordstat.

| Фраза | Показы/мес (Serpstat) |
|-------|----------------------|
| seo тексты | 390 |
| seo копирайтинг | 390 |
| seo текст это | 480 |

**SEO-стратегия:** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — во 2-м H2; «geo оптимизация статьи» — в блоке SEO+GEO; faq_hints («сколько символов», «что такое geo») — в FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title — до 70 символов, с главным ключом в начале | [Seospravka — чек-лист meta](https://seospravka.ru/wiki/chek-listy/chek-list-proverki-meta-tegov-i-zagolovka-h1) | 2026 | да |
| Description — до 160 символов, не дублирует Title | [Serptop — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| На странице один H1; H1 не дублирует Title полностью | [Seospravka — чек-лист meta](https://seospravka.ru/wiki/chek-listy/chek-list-proverki-meta-tegov-i-zagolovka-h1) | 2026 | да |
| H2 — один под-вопрос; H3 — шаги/пункты; если читать только заголовки — понятна логика | [LikaCloud — SEO checklist](https://www.likacloud.com/ru/guide/seo/seo-optimize-checklist/) | 2026 | да |
| 3–8 содержательных внутренних ссылок на релевантные страницы | [LikaCloud — SEO checklist](https://www.likacloud.com/ru/guide/seo/seo-optimize-checklist/) | 2026 | да |
| How-to инструкция — ориентир 1200–2500 слов (Serpstat, не универсальная норма) | [Spilno Agency — SEO copywriting](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да (с оговоркой) |
| Title ≤60 символов, meta 140–160 — практический ориентир для блога | [Spilno Agency — SEO copywriting](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да (ориентир) |
| Яндекс оценивает качество страниц метрикой **Проксима** (релевантность, полезность, оригинальность, удобство) | [Яндекс Вебмастер — search-quality](https://yandex.ru/support/webmaster/ru/search-quality) | актуально 2026 | да |
| **Профицит** — метрика полезности выдачи по взаимодействиям пользователя с Поиском | [Яндекс Вебмастер — search-quality](https://yandex.ru/support/webmaster/ru/search-quality) | актуально 2026 | да |
| Отчёт «Качество контента» в Вебмастере: уникальность, структура, поведение (время, глубина) | [SearchIndustrial — Вебмастер 2025](https://searchindustrial.ru/blog/seo/obzor-novykh-instrumentov-yandeks-vebmastera/) | 2025 | да |
| GEO — оптимизация для цитирования в AI-ответах; дополняет SEO, не заменяет | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Answer-first: первые 2–3 предложения после H2 — прямой ответ на вопрос заголовка | [PW Agency — GEO контент 2026](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 2026 | да |
| FAQ-блок 5–8 вопросов; ответ до ~80 слов — формат, удобный для LLM | [GEO Course — BLUF](https://geo-course.ru/blog/kak-pisat-kontent-dlya-nejrosetej/) | 2026 | да |
| Schema.org Article + FAQPage — гигиенический минимум для блога 2026 | [Pikapuka — SEO-гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |

**fact-bank.md:** прямых фактов про SEO-статьи нет — все цифры только из таблицы выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); Serpstat-цифры как «Wordstat»; «GEO заменяет SEO».

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды перегружены E-E-A-T-кейсами и CTA.
- H1 B01 («которые читают люди») слабо раскрыт в SERP — наш фокус: **читабельность как SEO-фактор** + техника.

**Режим B:** сама статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок SEO+GEO | «GEO — …» |
| Conversational H2 | «Что такое GEO в SEO?» | Вопрос в заголовке |
| FAQ 5–7 пар | Конец | Короткий ответ 2–4 предложения |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA для writer | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптimizaciya статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом контенте.
3. **Нужно ли переспамить ключевые слова в 2026 году?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~60–70 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.
7. **Можно ли писать SEO-статьи через ИИ?** — да, с редактурой: убрать воду, добавить экспертизу и факты.

---

## 7. Черновик чеклиста (15–20 пунктов для writer)

1. Primary query в H1 и первом абзаце — естественно.  
2. Один H1; иерархия H2→H3 без пропусков.  
3. Lead: боль + обещание результата (не «в этой статье»).  
4. После каждого H2 — прямой ответ в 1–3 предложениях.  
5. Абзацы 3–5 строк; списки/таблицы там, где перечисление.  
6. Title 55–65 символов; Description 140–160; H1 ≠ Title.  
7. Alt у каждого изображения.  
8. 3–5 внутренних ссылок (из карточки: `/`).  
9. FAQ 5–7 вопросов с короткими ответами.  
10. JSON-LD BlogPosting + FAQPage (schema-агент).  
11. Нет переспама ключей; LSI из раздела Wordstat.  
12. E-E-A-T lite: автор, дата обновления.  
13. GEO: атомарные «острова смысла» в каждом H2.  
14. Проверка читабельности: island test + so-what test.  
15. Финальный проход: опечатки, битые ссылки, мобильная вёрстка.

---

## 8. Риски для writer

- Не выдумывать Wordstat-показы — только экспертная семантика до перезапуска MCP.
- Не копировать структуру Pikapuka/Serptop 1:1.
- Объём: 8 500–9 500 знаков (quality-blog.md).
- Без эмодзи в article.html.
- Минимум **5** нумерованных шагов в action_outline + чеклист **15+** пунктов.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель сможет написать и подготовить к публикации SEO-статью для блога: от проверки интента и разбора конкурентов до структуры H1–H3, текста без воды, мета-тегов, FAQ, schema и финального чеклиста с GEO-упаковкой.

**action_outline:**

1. **Проверить интент:** ввести primary query в поиск; зафиксировать тип контента в топ-5 (гайд, чек-лист, агентский longread).  
2. **Собрать семантику:** Wordstat/Вебмастер — кластер 3–5 подтем + LSI; исключить нерелевантные «хвосты».  
3. **Составить каркас:** H1 с primary query; 4–6 H2 по подтемам; под каждым H2 — тезис первым предложением.  
4. **Написать lead:** определение + обещание результата за 40–60 слов; primary key в первых 100 словах.  
5. **Наполнить блоки:** короткие абзацы, списки, таблица «SEO vs GEO»; личный опыт/пример без выдуманных цифр.  
6. **Добавить FAQ 5–7:** вопросы из PAA; ответы 2–4 предложения, actionable.  
7. **Оформить мета:** Title, Description, alt; 3–5 внутренних ссылок; H1 ≠ Title.  
8. **Подключить schema:** BlogPosting + FAQPage (отдельный агент); datePublished/dateModified.  
9. **Пройти чеклист 15–20 пунктов** перед публикацией и исправить 🔴 блокеры (переспам, вода, нет ответа после H2).

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (6) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| Чеклист 15+ | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
