# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-08-10  
**disclaimer:** Все даты, версии и статистика проверены на 10.08.2026.

---

## 1. Анализ спроса Яндекс Вордстат

**Попытка вызова:** `wordstat_get_top_requests` на сервере `user-mcp-kv` для запросов:
- primary: «как писать seo статьи»
- secondary: «seo текст для блога», «geo оптимизация статьи»

**Результат:** сервер `user-mcp-kv` **недоступен** в Cloud Agent среде (2026-08-10). Точные объёмы показов не получены.

> ⚠️ **WORDSTAT MCP WARNING:** MCP-сервер `user-mcp-kv` не подключён к текущему прогону. Обновите MCP в `environment.json` и авторизуйте токен Wordstat через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40  
> **Не использовать в тексте выдуманные цифры частотности.** Ниже — семантический кластер из SERP и конкурентов (без объёмов).

### Семантический кластер (экспертная оценка по SERP, без Wordstat API)

| Фраза / кластер | Интент | Роль в статье |
|-----------------|--------|---------------|
| как писать seo статьи | how_to | primary_query, H1/lead |
| как написать seo статью | how_to | синоним primary, Title/H2 |
| seo текст для блога | how_to | secondary, блок «семантика» |
| seo текст для сайта | how_to | LSI, примеры |
| как писать seo тексты 2026 | how_to | freshness-маркер |
| структура seo статьи | how_to | H2 «структура longread» |
| семантическое ядро для статьи | how_to | шаг 1 action_outline |
| geo оптимизация статьи | how_to | secondary, блок SEO+GEO |
| answer-first / snippet-first | how_to | GEO-hook |
| чеклист seo статьи перед публикацией | checklist | финальный H2 |
| title description для seo статьи | how_to | техблок |
| schema faqpage для статьи | how_to | H2 FAQ/schema |

### LSI для writer (из топа SERP, без объёмов Wordstat)

- интент запроса, анализ конкурентов в выдаче, кластеризация ключей  
- H1–H3, lead-абзац, списки, таблицы, FAQ-блок  
- E-E-A-T / ЭПОС (экспертность, полезность, оригинальность, содержательность)  
- Title, Description, alt-теги, ЧПУ, внутренняя перелинковка  
- BlogPosting / Article + FAQPage JSON-LD  
- GEO: атомарные чанки 40–80 слов после H2, нейровыдача, Поиск с Алисой  
- llms.txt (опционально), robots.txt для AI-краулеров  
- проверка перед публикацией: уникальность, мобильная вёрстка, факты  

**SEO-стратегия:** primary «как писать seo статьи» в H1/lead; secondary «seo текст для блога» и «geo оптимизация статьи» — отдельные H2-блоки без переспама; conversational FAQ закрывает faq_hints из карточки B01.

---

## 2. SERP-обзор (WebSearch, август 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон: семантика через Вордстат/Вебмастер, H1–H4, естественность ключей, 3–5 строк в абзаце, Title/Description, перелинковка | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок про рекламу; копировать структуру без GEO-слоя |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Агентский гайд 2026 | Кластеры 3–5 тем, snippet-first после H2, «сначала смысл — потом ключи», примеры с/без ИИ | Длинный sales-narrative; ИИ как центр, не workflow | Шаблон «полное руководство» 1:1; необоснованные кейсы |
| 3 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм (обнов. февр. 2026) | 13 шагов от спроса до WordPress; интент, конкуренты, E-E-A-T, мета, FAQ | Фокус на WP-хостинг/Timeweb; мало GEO | Affiliate-блоки хостинга; дублировать все 13 H2 |
| 4 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист 9 критериев (июнь 2026) | E-E-A-T + ЭПОС Яндекса; AI Overviews и Алиса; answer-first; без «уникальности 99%» | Мало пошагового workflow «с нуля» | Копировать 9 критериев как единственную структуру |
| 5 | [serptop.ru/blog/kak-pisat-seo-teksty](https://serptop.ru/blog/kak-pisat-seo-teksty/) | Гайд + чек-лист | Формула H1, lead 50–100 слов, skeleton H2, мета ≤70/160, ЧПУ | Устаревшие ориентиры по «плотности %» | Keyword density % как главный KPI |
| 6 | [text.ru/blog/kak-popast-v-ii-poisk-v-2026-poshagovyy-plan-promty](https://text.ru/blog/kak-popast-v-ii-poisk-v-2026-poshagovyy-plan-promty) | GEO + SEO (2026) | Топ-30 органики как база для AI; answer-first 100 слов; H2-вопросы; Schema FAQPage | Узкий фокус «попасть в нейровыдачу», не writing | Цифры «2–3 дня / 3–8 недель» без первичника |
| 7 | [megagroup.ru/blog/kak-sozdavat-seo-stati-theory-2026](https://megagroup.ru/blog/kak-sozdavat-seo-stati-theory-2026) | Теория + подготовка | Три шага подготовки: аудитория, ключи, конкуренты; H1 как ответ | Слабый финальный чеклист | «Theory» без actionable финала |

**Паттерн SERP (август 2026):** топ — «гайд 2026» с пошаговым алгоритмом, E-E-A-T, Wordstat, чек-листом перед публикацией. Отдельный кластер — GEO/нейропоиск (answer-first, FAQ, Schema). H1 «которые читают люди» в топе почти не встречается — **дифференциатор Excalibur**.

**Intent:** `how_to` — пользователь хочет систему: семантика → структура → текст → техника → проверка. Вторичный intent: связать SEO и GEO в одном материале без двух отдельных проектов.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — он зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на странице; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-текст в 2026: качество, проверяемость, E-E-A-T; не механическое насыщение ключами | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Яндекс оценивает контент по ЭПОС: экспертность, полезность, оригинальность, содержательность | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Контент должен быть понятен человеку, поисковой системе и AI-системам (AI Overviews, Алиса, ChatGPT, Perplexity) | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| После каждого H2 — содержательный ответ сразу (snippet-first) | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Главный ключ — в H1, первом абзаце, 1–2 H2, Title и Description; LSI — органично | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| SEO-статья 2026 — страница, закрывающая задачу пользователя (выбрать, настроить, сделать), не «текст под ключи» | [OlegWeb — алгоритм SEO-статьи](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Meta title — ориентир ≤70 символов; meta description — ≤160; один H1 | [SerpTop — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| Lead: основной ключ в первых 50–100 словах; H1 = ключ + обещание пользы | [SerpTop — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| Для попадания в AI-ответы нужна база в органике (топ-30) + answer-first + Schema FAQPage | [Text.ru — нейропоиск 2026](https://text.ru/blog/kak-popast-v-ii-poisk-v-2026-poshagovyy-plan-promty) | 2026 | да* |
| FAQ-ответы для GEO — 40–60 слов, прямые формулировки | [РБК Компании — GEO 2026](https://companies.rbc.ru/news/VVWJGhIKsz/geo-prodvizhenie-kak-popast-v-nejrovyidachu-i-ii-otvetyi-v-2026-godu/) | 2026 | да |

\* Цифры сроков «2–3 дня / 3–8 недель» из Text.ru — **не использовать** без первичника.

**Не использовать:** «+140% трафика»; keyword density 1–2% как универсальное правило; «микроразметка ×1,5–2 цитирование» без arxiv/первичника.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс Direct даёт канон SEO без GEO-слоя.
- GEO-гайды (Text.ru, РБК) не учат писать текст с нуля.
- Агентские гайды (1PS, SerpTop) перегружены общими правилами без «читабельности как фактора».
- H1 B01 («которые читают люди») слабо раскрыт в SERP — наш фокус: **структура + инфостиль + «острова смысла»** как SEO/GEO-сигнал.

**Режим B:** статья B01 — **эталон формата**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (карточка B01 + research):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO — …» |
| Conversational H2 | FAQ-подобные подзаголовки | «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец longread | 2–4 предложения на ответ |
| Атомарные чанки | Каждый H2 | Тезис в первом предложении |
| Schema | meta/handoff | BlogPosting + FAQPage |
| Internal link | Из карточки | `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~65–70 знаков), H1 — на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt и нужен ли он блогу?** — опциональный сигнал для AI-краулеров; не замена sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику в Вордстат/Вебмастер, спроектирует структуру longread с answer-first блоками, напишет текст без переспама, добавит FAQ и JSON-LD, пройдёт чеклист перед публикацией и получит материал, готовый и для людей, и для нейровыдачи.

**action_outline:**

1. **Проверить спрос и интент:** ввести primary query в [Яндекс Вордстат](https://wordstat.yandex.ru/) и [Вебмастер](https://webmaster.yandex.ru/); зафиксировать информационный/коммерческий intent; выписать 5–10 LSI из «похожих запросов».
2. **Разобрать топ-5 SERP:** структура H2, форматы (таблицы, FAQ, видео), пробелы — что добавить в свою статью.
3. **Собрать outline:** H1 с primary; 4–6 H2 по подзадачам; под каждым H2 — тезис в первом предложении (snippet-first).
4. **Написать lead и body:** ответ на главный вопрос в первых 100 словах; абзацы 3–5 строк; списки/таблица где упрощают сканирование; ключи органично, без переспама.
5. **Добавить SEO+GEO слой:** блок «зачем GEO в той же статье»; FAQ 5–7 вопросов; чанки 40–80 слов после H2 для AI-извлечения.
6. **Заполнить мета и медиа:** Title (~65–70 зн.), Description (~140–160 зн.), alt у изображений, ЧПУ, 2–3 внутренние ссылки.
7. **Подготовить schema (handoff):** BlogPosting + FAQPage JSON-LD; datePublished/dateModified; автор без выдуманных регалий.
8. **Пройти чеклист перед публикацией:** факты с URL, нет воды, island test по H2, мобильная вёрстка, ссылки рабочие.

---

## 8. Риски для writer

- Не выдумывать частотность Wordstat — MCP недоступен в этом прогоне.
- Не копировать 13 шагов OlegWeb или 9 критериев Texterra 1:1.
- Объём: 8 500–9 500 знаков (quality-blog).
- Без эмодзи в article.html; без VPN/обход блокировок.
- Internal link: `/` из карточки B01; hub для B04 — `/geo-optimizaciya-sajta-2026/` (когда опубликован).

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (7) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (15) |
| action_outline 5–9 шагов | ✅ (8) |
| reader_outcome | ✅ |
| GEO hooks + FAQ | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
