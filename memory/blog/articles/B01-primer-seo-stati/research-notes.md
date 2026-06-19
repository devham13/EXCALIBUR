# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-06-19  
**disclaimer:** Все даты, версии и статистика проверены на 19.06.2026.

**utility_verdict:** PASS  
**reader_outcome:** Читатель сможет собрать семантику, выстроить структуру longread, написать текст «для людей», добавить FAQ/schema и пройти финальный чеклист перед публикацией, включая базовый GEO-слой для нейропоиска.  
**action_outline:**
1. Определить интент запроса и собрать семантику в Wordstat/Вебмастер (primary + LSI + вопросы).  
2. Проанализировать 3–5 конкурентов в SERP: структура, пробелы, что не копировать.  
3. Составить outline: H1, H2–H3 как подзадачи, lead с ответом в первых 1–2 абзацах.  
4. Написать черновик: короткие абзацы, списки/таблицы, один H2 = один «остров смысла».  
5. Вписать ключи естественно (H1, lead, 1–2 H2, Title/Description); без переспама.  
6. Добавить FAQ (5–7 пар) + JSON-LD BlogPosting/FAQPage; alt, мета, внутренние ссылки.  
7. GEO-проверка: island test, answer-first, llms.txt/robots для AI-краулеров; финальный чеклист 15+ пунктов.

---

## 1. SERP-обзор (WebSearch Cursor, 19.06.2026; дополнено research-serp.json)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон: workflow тема → семантика → структура → текст → оптимизация; примеры «плохо/хорошо»; Wordstat, alt, мета, перелинковка; нет универсального объёма | Нет GEO/нейропоиска; CTA Директа | Блок про Директ; копировать H1–H4 без GEO-слоя |
| 2 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (май 2026) | Семантика, E-E-A-T, чек-лист 10 шагов, Schema Article + FAQPage, Title ~65 знаков, AI-ответы | Кейсы с непроверенными %; GEO как побочный эффект E-E-A-T | «+140% трафика»; структуру 7 разделов 1:1 |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread + ИИ (2026) | 7 факторов SEO-копирайтинга 2026, пошаговая инструкция, промпты для ИИ, FAQ/нейроответы | Очень длинный; перегруз SEO-терминами | Копировать промпт-блоки без контекста Excalibur |
| 4 | [qvai.ru/media/kak-pisat-seo-stati](https://qvai.ru/media/kak-pisat-seo-stati) | Близкий H1 (июнь 2026) | Прямое попадание в «которые читают люди»; принцип «сначала люди, потом роботы»; структура + ошибки | Короткий (~1,5k), без чеклиста, FAQ, schema, GEO | Thin контент как эталон объёма |
| 5 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | SEO-агентство (обновлено 19.06.2026) | «Полный ответ на одной странице»; LSI и хвосты; поведенческий сигнал (не возвращаться в поиск) | Мало actionable шагов и техники GEO | «Просто следуй принципам» без workflow |
| 6 | [blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | GEO + текст (2026) | Чанкинг, H1–H3 иерархия, нормы абзаца/блока (12–20 слов, 30–60 слов, 100–380 слов) | Коммерческий bias click.ru; часть статистики без первичника в сниппете | Цифры 25%/17% без cross-check первичника |
| 7 | [companies.rbc.ru/news/cA4bgStBGq/klyuchevyie-trendyi-seo-2026](https://companies.rbc.ru/news/cA4bgStBGq/klyuchevyie-trendyi-seo-2026/) | РБК Компании (2026) | Answer-first: первые 800–1000 символов по делу; экспертиза, актуализация раз в квартал | Обзор трендов, не пошаговый гайд | Новостной tone без инструкции |
| 8 | [seojazz.ru/blog/tekstovaja-optimizacija-v-2026-godu](https://seojazz.ru/blog/tekstovaja-optimizacija-v-2026-godu-rabota-s-kontentom-dlja-uluchshenija-relevantnosti-i-relevantnye-tegi/) | Текстовая оптимизация 2026 | Формулы Title (50–60 знаков) и Description (140–180); AIO, вопросные H2 | Узкий фокус на теги, не на полный workflow статьи | Копировать формулы без адаптации к H1 B01 |

**Паттерн SERP:** топ — «полный гайд SEO-текстов 2026» (1ps, pikapuka, seomatik, hozyindachi) + отдельный кластер GEO-лонгридов. Прямое совпадение с H1 «которые читают люди» — [qvai.ru](https://qvai.ru/media/kak-pisat-seo-stati), но материал короткий. Почти никто не даёт **единый workflow SEO+GEO longread** с чеклистом 15+ пунктов и режимом B «статья как эталон формата блога».

**Intent:** how_to — пошаговая система: семантика → структура → текст → техника → FAQ/schema → GEO-чанки → проверка. Вторичный: «seo текст для блога», «geo оптимизация статьи» в одном материале.

**Пробел для Excalibur:** практический гайд для B2B-аудитории (маркетолог/РОП без SEO-отдела): читабельность как фактор ранжирования + техника + демонстрация на самой статье B01; связка с B04 (GEO чеклист сайта), B03 (MCP Wordstat в Cursor).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** Токен Wordstat / `MCP_KV_TOKEN` недоступен в окружении Cloud Agent (вызов `wordstat_get_top_requests` на сервере `user-mcp-kv` не выполнен). Обновите токен через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Статус wordstat:** FAILED (нет авторизации MCP-KV; точные показы в месяц не получены).

### Семантическая оценка без объёмов (SERP + конкуренты, не Wordstat)

| Кластер | Запросы для writer (без показов) |
|---------|-----------------------------------|
| Primary | как писать seo статьи, как написать seo статью, seo статья для сайта |
| Secondary | seo текст для блога, seo текст для блога как писать |
| GEO | geo оптимизация статьи, оптимизация статьи под нейросети, как попасть в ответы ии |
| LSI | семантическое ядро, lsi-фразы, e-e-a-t, title description, faq schema, featured snippet, answer-first, llms.txt |
| Вопросные | сколько символов в seo статье, что такое geo в seo, чем title отличается от h1 |

**SEO-стратегия (без Wordstat):** primary в H1/lead; secondary и faq_hints в H2/FAQ; GEO-блок — «geo оптимизация статьи» без путаницы с локальной «географией».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата источника | Можно в текст |
|------|----------|----------------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Главная задача статьи — полный ответ; если пользователь возвращается в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 19.06.2026 | да |
| Пишите для людей, оптимизируйте для поисковиков — в таком порядке | [qvai.ru — SEO-статьи](https://qvai.ru/media/kak-pisat-seo-stati) | 01.06.2026 | да |
| Title — ориентир ~65 знаков, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| H1 должен отличаться от Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Schema.org: Article + FAQPage для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Title: 50–60 знаков; Description: 140–180 знаков, 1–2 предложения | [SEO Jazz — текстовая оптимизация 2026](https://seojazz.ru/blog/tekstovaja-optimizacija-v-2026-godu-rabota-s-kontentom-dlja-uluchshenija-relevantnosti-i-relevantnye-tegi/) | 2026 | да |
| Первые 800–1000 символов — максимально по делу, без длинных вступлений (answer-first) | [РБК Компании — тренды SEO 2026](https://companies.rbc.ru/news/cA4bgStBGq/klyuchevyie-trendyi-seo-2026-kak-prodvigat-sajtyi-kogda-v-poiske-pravit-ai/) | 2026 | да |
| ИИ режет текст на чанки; размер чанка в поиске фактов ~128–515 токенов (≈96–380 русских слов) | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| Нормы читаемости для ИИ: предложение 12–20 слов; абзац 30–60 слов; смысловой блок 100–380 слов с подзаголовком | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| GEO (Generative Engine Optimization) — оптимизация для цитирования в ответах AI, не замена SEO | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Нейросети извлекают пассажи (passages); каждый H2-блок = «остров смысла» | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Первые 100–150 слов страницы — ключевая зона для извлечения ответа AI | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Стандарт llms.txt предложен в сентябре 2024 (Jeremy Howard / Answer.AI) | [Digital Impuls — GEO 2026](https://digitalimpuls.ru/blog/geo-optimization-2026/) | 2026 | да |
| В 2026 в SEO-текстах важны полезность и экспертность, а не тошнота/заспамленность | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |

**Не использовать в тексте (нет в fact-bank / непроверено):** «+140% трафика за 3 недели» (Pikapuka); «25% россиян daily AI» и «17% не кликают» (click.ru без первичника в проверенном фрагменте); «микроразметка +1,5–2× цитирование» (Digital Impuls); любые показы Wordstat без успешного MCP-вызова.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Единый workflow: интент → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- qvai.ru близок по H1, но без глубины и чеклиста.
- Агентские гайды перегружены E-E-A-T-кейсами и CTA.

**Режим B:** статья B01 — эталон: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (карточка + research):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

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
| Даты | Метаданные | datePublished / dateModified = 2026-06-19 |
| llms.txt | Упоминание в GEO-блоке | Что это и зачем для блога |
| E-E-A-T lite | Автор/редакция | Имя, роль, без выдуманных регалий |
| Внутренняя ссылка | Из карточки | На `/` (главная) |
| Alt обложки | Cover | «Редактор за ноутбуком…» (cover_scene_hint) |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и конкуренты в SERP; для how-to longread в Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах, база — индексируемый и структурированный контент.
3. **Нужно ли переспамить ключевые слова в 2026 году?** — нет; естественные вхождения + LSI/тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (~50–65 знаков), H1 — заголовок на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage для блока вопросов.
6. **Что такое llms.txt и нужен ли он блогу?** — файл для AI-краулеров; полезный сигнал, не замена sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски и blockers для writer

- Не выдумывать статистику и Wordstat-показы; только таблица фактов выше.
- Не копировать структуру Pikapuka/1ps 1:1.
- Объём текста: 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи, без VPN/обход блокировок.
- site_url — плейсхолдер или `/` по карточке.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ AUTH FAILED |
| Таблица фактов с URL | ✅ (19) |
| action_outline + reader_outcome | ✅ |
| utility_verdict PASS | ✅ |
| GEO hooks | ✅ |
| FAQ-кандидаты 5–7 | ✅ |
| Режим B описан | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `blog-topics.md` + `site-brief.md`.
