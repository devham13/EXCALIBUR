# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to + чеклист; longread как эталон формата)  
**research_date:** 2026-08-09  
**disclaimer:** Все даты, версии и статистика проверены на 09.08.2026.

---

## 1. SERP-обзор (WebSearch, 09.08.2026 — 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон: H1–H4, Wordstat, alt, мета, перелинковка; «нет универсального объёма»; естественность ключей | Нет GEO/нейропоиска; CTA Директа в конце | Блок про Директ; копировать структуру без GEO-слоя |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 2026 (13 шагов) | Интент → конкуренты → структура → WordPress → чек-лист; практика для владельца сайта | Длинный WordPress-уклон; мало GEO | 13 шагов 1:1; affiliate-блоки |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Кластеризация Wordstat, «смысл → оптимизация», правило ответа сразу после H2 | Перегруз про ИИ без human-in-the-loop | Структуру 1:1; «ИИ напишет всё» |
| 4 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский гайд (май 2026) | E-E-A-T, Schema Article+FAQ, Title ~65 знаков, AI-ответы | Непроверенные кейсы «+140%» | Непроверенные проценты; 7 разделов 1:1 |
| 5 | [serptop.ru/blog/kak-pisat-seo-teksty/](https://serptop.ru/blog/kak-pisat-seo-teksty/) | Гайд + чек-лист | Формула H1, каркас H2 (инструкция / ошибки / CTA), мета ≤70/160 | Мало GEO; общие формулировки | Сухой чеклист без «читают люди» |
| 6 | [hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | SEO+поведение 2026 | 7 шагов workflow; FAQ под сниппет; «текст для задачи читателя» | Мало техники schema/WordPress | Fear-narrative «рейт без E-E-A-T» |
| 7 | [bmg.by/blog/decisions/seo-checklist-for-content-and-ai-search/](https://bmg.by/blog/decisions/seo-checklist-for-content-and-ai-search/) | Чек-лист SEO + AI Mode | Рабочий список без воды: техника + контент + нейропоиск | Не учит писать с нуля | Копировать чеклист дословно |
| 8 | [habr.com/ru/amp/publications/987506/](https://habr.com/ru/amp/publications/987506/) | GEO/AEO технический гайд | Связка SEO→GEO; answer capsules; schema; zero-click контекст | Другой intent (GEO техника, не writing) | Цифры zero-click без первичника; dev-only код |

**Паттерн SERP:** топ — «полный гайд 2026» с пошаговым алгоритмом (8–13 шагов), Wordstat, E-E-A-T, чек-листом перед публикацией. Отдельный кластер — GEO-лонгриды. H1 «которые читают люди» в топе почти не встречается — пробел для акцента на **читабельность + GEO в одном workflow**.

**Intent:** `how_to` — пользователь хочет систему: проверить спрос → интент → структура → черновик → мета/schema → финальный чеклист. Вторичный intent: связать SEO-текст и GEO-оптимизацию **в одной статье**, не двумя проектами.

**Пробел для Excalibur BLOG:** B2B-практик (AI-автоматизация, контент-завод) объясняет writing **для людей и нейропоиска** одним чеклистом; human-in-the-loop при ИИ; без agency-воды и без «новостей про алгоритм».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 09.08.2026)

⚠️ **WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` недоступен в Cloud Agent окружении (`MCP server does not exist`). Вызов `wordstat_get_top_requests` для `как писать seo статьи`, `seo текст для блога`, `geo оптимизация статьи` **не выполнен**. Точные объёмы показов в месяц **не получены** — не выдумывать цифры спроса.

**Действие для пайплайна:** обновить MCP-токен и конфиг (`https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40`) — см. `.cursor/skills/excalibur-research/SKILL.md`. Writer использует LSI ниже; при появлении Wordstat — дополнить таблицу спроса.

### LSI и смежные запросы (из SERP + подсказки конкурентов, без частотности)

| Группа | Фразы для кластера |
|--------|-------------------|
| Primary | как писать seo статьи, как написать seo статью, как писать seo тексты |
| Семантика | seo текст для блога, seo копирайтинг, семантическое ядро, lsi фразы, wordstat |
| Структура | структура seo статьи, h1 h2 h3, title description, meta description |
| Качество | e-e-a-t, переспам ключевых слов, читабельность, инфостиль |
| GEO | geo оптимизация статьи, faq schema, answer capsule, нейропоиск |
| Финал | чеклист перед публикацией, внутренняя перелинковка, alt текст |

**SEO-стратегия writer:** primary «как писать seo статьи» — H1/lead; secondary «seo текст для блога», «geo оптимизация статьи» — отдельные H2; long-tail из таблицы — FAQ и подзаголовки.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Google: people-first content — для людей, не для манипуляции выдачей | [Google Search Central — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 09.08.2026 | да |
| Google: нет «предпочтительного» объёма текста для ранжирования | [Google Search Central — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 09.08.2026 | да |
| Google: SEO полезен, когда применён к people-first контенту, а не search-engine-first | [Google Search Central — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 09.08.2026 | да |
| Google: E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness); trust — ключевой | [Google Search Central — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 09.08.2026 | да |
| Google: Who / How / Why — рамка для оценки контента (автор, процесс создания, цель) | [Google Search Central — Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 09.08.2026 | да |
| Google: контент, созданный **главно** для манипуляции выдачей (в т.ч. массовая AI-генерация), — spam policy | [Google Search Central — AI content](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content) | 09.08.2026 | да |
| Title — ориентир до 60 символов, ключ в начале; не дублировать H1 дословно | [Divitio — SEO-текст](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Meta description — до ~155 символов; влияет на CTR, не на прямое ранжирование | [Divitio — SEO-текст](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Главный ключ — H1, первый абзац, 1–2 H2; LSI — естественно, без подсчёта плотности | [Divitio — SEO-текст](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| После каждого H2 — содержательный ответ сразу (правило для сниппетов и GEO) | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Финальный чеклист: Title ≤60, Meta 140–160, один H1, alt, 3–5 внутренних ссылок, Schema, CWV | [Spilno Agency — SEO copywriting 2026](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да |
| GEO — оптимизация под цитирование в ответах AI; дополняет SEO, не заменяет | [Habr — GEO/AEO гайд](https://habr.com/ru/amp/publications/987506/) | 2026 | да |
| FAQ 5–7 вопросов + FAQPage schema — практика для AI-выдачи | [geocopy.io — GEO optimization](https://www.geocopy.io/geo-optimization) | 2026 | да* |
| Главная задача — полный ответ; возврат в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

\* geocopy.io — вторичный EN-источник по citation signals; в тексте — «по исследованиям GEO-оптимизации», без точных % без arxiv/Princeton.

**Не использовать без оговорки:** «60–70% zero-click» (Habr без первичника); «+140% трафика» (Pikapuka); «плотность 1–2%» как жёсткое правило — только как ориентир Serpstat-гайда.

**fact-bank.md:** нет строк по SEO-writing — все цифры только из таблицы выше.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за одну сессию (60–90 мин) пройти **единый workflow** написания SEO-статьи 2026: спрос/интент → структура longread **для людей** → черновик → GEO-блоки (answer capsules, FAQ) → мета/schema → **чеклист 15+ пунктов** перед публикацией. Статья B01 — эталон формата (8 500–9 500 знаков).

**Почему отличается от конкурентов:**
- Яндекс — канон без GEO; GEO-гайды — без writing с нуля.
- Агентские longread'ы — кейсы и CTA без «читают люди».
- Excalibur: B2B-практик, human-in-the-loop при ИИ, SEO+GEO в одном материале.

**Tone (site-brief):** практично, без корпоративной воды; термины GEO/E-E-A-T — сразу «на пальцах».

**H2-каркас (из карточки B01 + research):**
1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO — …» |
| Answer capsule 40–60 слов | После каждого H2 | Прямой ответ |
| FAQ 5–7 пар | Конец | 2–4 предложения, действие |
| Island test | QA writer | Блок понятен отдельно |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и конкуренты; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — дополнение к SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (~60 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Можно ли писать SEO-статью только нейросетью?** — можно ускорить черновик; финал — человек (факты, тон, E-E-A-T); иначе spam policy Google.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать Wordstat-частотности (MCP недоступен).
- Не копировать Pikapuka/olegweb 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Min **5** нумерованных шагов + чеклист **10+** пунктов.
- Без эмодзи; CTA ≤ 3.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику по интенту, построит структуру longread с answer-блоками под GEO, напишет и отредактирует черновик «для людей», заполнит Title/Description/alt/перелинковку, добавит FAQ + schema и пройдёт финальный чеклист перед публикацией — без переспама и без отдельного «GEO-проекта».

**action_outline (для writer):**

1. **Проверить спрос и интент:** вбить `как писать seo статьи` в поиск; если топ — гайды, писать инструкцию; выпишите 15–25 фраз из Wordstat/подсказок (когда MCP доступен) и сгруппируйте в 3–5 кластеров.
2. **Разобрать ТОП-5 SERP:** структура, форматы (таблицы, FAQ), content gap — что добавить уникального (читабельность, B2B-угол).
3. **Собрать outline:** H1 с primary; 5–8 H2 (каждый = подзадача); под каждым H2 — тезис-ответ в первом абзаце.
4. **Написать lead:** боль + обещание результата + primary key в первых 100 словах; без «в этой статье мы рассмотрим».
5. **Черновик по блокам:** сначала смысл и примеры; затем LSI; главный ключ — H1, lead, 1–2 H2; без подсчёта плотности.
6. **Добавить E-E-A-T lite:** автор/редакция, 1–2 проверенных факта из таблицы §3, без выдуманных кейсов.
7. **Упаковать под GEO:** FAQ 5–7; answer capsules после H2; списки/таблицы где упрощают; handoff schema — BlogPosting + FAQPage.
8. **Техника on-page:** Title ≤60, Description 140–160, один H1, alt у изображений, 3–5 внутренних ссылок, ЧПУ slug.
9. **Финальный чеклист 15+ пунктов** (отдельный H2): семантика, мета, структура, FAQ, schema, ссылки, мобильность, proofread — printable logic.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен; LSI из SERP |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
