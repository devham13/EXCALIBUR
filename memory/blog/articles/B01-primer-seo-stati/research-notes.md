# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата на самой статье)  
**research_date:** 2026-08-17  
**disclaimer:** Все даты, версии и статистика проверены на 2026-08-17 (2026 год).

---

## Utility gate

| Gate | Результат |
|------|-----------|
| Topic utility gate (`excalibur_blog_utility_gate.py --topic-id B01`) | PASS |
| `search_intent` | how_to |
| `article_mode` | B |

**utility_verdict:** PASS

**reader_outcome:** После прочтения читатель сможет собрать SEO-статью под один запрос: проверить спрос, определить интент, составить структуру H1–H3, написать текст без воды, добавить FAQ/schema и пройти финальный чек-лист перед публикацией — с учётом GEO-слоя для нейропоиска.

**action_outline (workflow для writer):**

1. Проверить спрос и интент по primary query в Вордстат + SERP (5–10 мин).
2. Разобрать топ-3 конкурента: какие подзадачи закрывают, где пробелы.
3. Собрать каркас: H1, 4–6 H2, H3 для шагов; lead 40–70 слов с прямым ответом.
4. Распределить ключи: primary в H1 и первом абзаце, secondary/LSI в H2 и тексте без переспама.
5. Написать body: короткие абзацы, списки, одна таблица «делать / не делать» или «SEO vs GEO».
6. Добавить блок FAQ (5–7 пар, ответы до 80 слов, с глаголом действия).
7. Заполнить Title (~60–70 знаков), Description (~150–160), alt у изображений.
8. Подготовить JSON-LD BlogPosting + FAQPage (в schema, не в body).
9. Пройти чек-лист перед публикацией: семантика, мета, структура, ссылки, читабельность, island test.

---

## 1. Яндекс Вордстат (спрос и LSI)

> ⚠️ **WORDSTAT MCP WARNING:** Сервер MCP `user-mcp-kv` недоступен в текущем Cloud Agent окружении (инструмент `wordstat_get_top_requests` не зарегистрирован). Точные показы в месяц **не получены**. Не использовать выдуманные цифры спроса.  
> Обновление токена (если MCP подключён локально): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Запросы для повторного прогона Wordstat (writer/QA)

| Запрос | Назначение |
|--------|------------|
| как писать seo статьи | primary_query |
| seo текст для блога | secondary |
| geo оптимизация статьи | secondary |
| как написать seo статью | вариация (частый в SERP) |
| структура seo статьи | LSI / структурный intent |
| чек-лист seo статьи | checklist intent |

### LSI-ключи из SERP (август 2026, без объёмов)

Семантическое ядро для копирайтера — из топа выдачи и secondary_queries:

- написание seo статей, seo текст, seo оптимизация статьи
- семантическое ядро, интент запроса, wordstat
- структура longread, заголовки h1 h2 h3, мета title description
- e-e-a-t, экспертность, уникальность текста
- faq блок, schema.org, json-ld, blogposting
- geo / generative engine optimization, нейропоиск, llms.txt
- внутренняя перелинковка, alt изображений, сниппет
- чек-лист перед публикацией, проверка текста

---

## 2. SERP-обзор (WebSearch, август 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|-----------------|------------------|---------------|
| 1 | [olegweb.ru — алгоритм SEO-статьи 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый гайд (13 шагов, обнов. 05.02.2026) | Полный цикл от спроса до WordPress; таблица «конкурент vs вы»; акцент на скрины и личный опыт | Узкая ниша «сделай сайт сам»; нет отдельного GEO-блока | 13 шагов 1:1; Telegram-CTA |
| 2 | [direct.yandex.ru — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: семантика, структура, естественность ключей, alt, мета; примеры «плохо/хорошо» | Нет GEO; CTA Директа | Коммерческий блок Директа |
| 3 | [tolk.digital — формула SEO-текстов 2026](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | Агентский how-to | E-E-A-T в структуре; 6-пунктовый чек-лист до публикации; форматы под intent | Sales CTA в конце; без schema/GEO | Шаблонные agency-формулировки |
| 4 | [marketingklub.ru — инструкция 2026](https://marketingklub.ru/kak-pisat-seo-stati/) | Чек-лист + структура | H1/H2/H3 иерархия; мета 60–70 / 150–160; printable checklist | Обобщённые нормы уникальности без первичника | Копировать чек-лист дословно |
| 5 | [roiseo.ru — структура SEO-статьи для блога](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон блоков | Таблица блоков (первый экран, ошибки, FAQ, schema); island-friendly | Мало про семантику/Wordstat | Agency-перелинковка на услуги |
| 6 | [likacloud.com — чек-лист SEO-страницы](https://www.likacloud.com/ru/guide/seo/seo-optimize-checklist/) | On-page checklist (обнов. 02.08.2026) | 8 пунктов предпроверки; критерии Title/Description/H1; first screen | Не про написание с нуля | Универсальный чек-лист без отбора под одну статью |
| 7 | [mv-blog.ru — GEO чек-лист](https://mv-blog.ru/blog/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | GEO + CMS | Lead 40–60 слов; FAQ в HTML; BlogPosting + FAQPage JSON-LD | Фокус Bitrix, не универсальный SEO-gайд | Обещания «гарантированное попадание в нейросеть» |

**Паттерн SERP:** топ — «полный гайд / чек-лист 2026» с E-E-A-T, Wordstat, мета и структурой. Отдельный кластер — GEO-лонгриды. H1 «которые читают люди» в топе почти не встречается — дифференциатор Excalibur.

**Intent:** how_to — пошаговая система: спрос → интент → структура → текст → техника → проверка. Вторичный: связка SEO + GEO в одном материале.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title — ориентир 60–70 символов, главный ключ ближе к началу | [Marketing Klub — SEO-статьи 2026](https://marketingklub.ru/kak-pisat-seo-stati/) | 2026 | да |
| Description — ориентир 150–160 символов | [Marketing Klub — SEO-статьи 2026](https://marketingklub.ru/kak-pisat-seo-stati/) | 2026 | да |
| В статье обычно 5–10 H2; ключи естественно в 2–3 заголовках H2 | [Marketing Klub — SEO-статьи 2026](https://marketingklub.ru/kak-pisat-seo-stati/) | 2026 | да |
| E-E-A-T: опыт, экспертиза, авторитетность, достоверность — критерии доверия к тексту | [Tolk — SEO-тексты 2026](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | 2026 | да |
| Перед публикацией: ответ в первых двух абзацах, польза, доверие, читабельность, без воды | [Tolk — SEO-тексты 2026](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | 2026 | да |
| Предпроверка страницы: индексация, один H1, уникальный Title, canonical, мобильная читаемость | [LikaCloud — SEO checklist](https://www.likacloud.com/ru/guide/seo/seo-optimize-checklist/) | 02.08.2026 | да |
| GEO-статья: прямой ответ 40–60 слов в lead; FAQ в исходном HTML; BlogPosting + FAQPage JSON-LD | [mv-blog — GEO чек-лист](https://mv-blog.ru/blog/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | 2026 | да |
| GEO (Generative Engine Optimization) — оптимизация под генеративные нейросети; дополняет SEO, не заменяет | [Click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| Шаблон SEO-статьи блога: первый экран с ответом, таблица, ошибки, чек-лист, FAQ, schema | [ROI SEO — структура](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |

**Не использовать без первичника:** «17% не кликают по ссылкам» (Click.ru без ссылки на исследование); «уникальность 90%+» как норма (Marketing Klub — без первичника); «+140% трафика» и прочие agency-кейсы.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**

- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды (Tolk, Marketing Klub) перегружены CTA и общими нормами.
- H1 «которые читают люди» слабо раскрыт в SERP — наш фокус: **читабельность как SEO-фактор** (структура, короткие абзацы, «острова смысла») + техника.

**Режим B:** статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (из карточки + research):**

1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи (40–60 слов) | Lead после H1 | «SEO-статья — …» |
| Определение GEO (40–60 слов) | Блок «SEO + GEO» | «GEO — …» |
| Conversational H2 | FAQ-соседние блоки | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | 2–4 предложения, действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в body | BlogPosting + FAQPage |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — дополнение к SEO: цель — цитирование в AI-ответах при базе индексируемого контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~60–70 знаков), H1 на странице; не дублировать.
5. **Какие schema нужны блогу?** — BlogPosting + FAQPage.
6. **Что такое llms.txt?** — файл для AI-краулеров; полезный сигнал, не замена sitemap.
7. **Как проверить статью перед публикацией?** — чек-лист: семантика, мета, структура, FAQ, schema, ссылки.

---

## 7. Риски для writer

- Не выдумывать показы Wordstat (MCP недоступен).
- Не копировать структуру olegweb (13 шагов) или Marketing Klub 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Без эмодзи, без VPN/обход блокировок.
- Цифры только из таблицы фактов §3.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate topic | ✅ PASS |
| utility_verdict + reader_outcome + action_outline | ✅ |
| SERP ≥ 5 конкурентов (свежий WebSearch) | ✅ |
| Wordstat (MCP) | ⚠️ недоступен; LSI из SERP |
| Таблица фактов с URL (15 строк) | ✅ |
| GEO hooks + FAQ 5–7 | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
