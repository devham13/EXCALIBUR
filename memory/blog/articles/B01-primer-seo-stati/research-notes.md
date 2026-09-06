# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-09-06  
**disclaimer:** Все даты, версии и статистика проверены на 2026-09-06 (2026 год).

---

## 0. Utility gate

| Gate | Результат |
|------|-----------|
| Topic utility gate (`excalibur_blog_utility_gate.py --topic-id B01`) | **PASS** |
| search_intent | how_to |
| article_mode | B |

**utility_verdict:** PASS

**reader_outcome:** Читатель за одну рабочую сессию соберёт семантику по интенту, построит структуру longread (H1–H3 + lead + FAQ), напишет черновик без переспама, добавит GEO-чанки и schema, пройдёт финальный чек-лист и опубликует SEO-статью, которую дочитывают люди и которую могут процитировать нейропоисковики.

**action_outline:**

1. **Определить интент и SERP-формат:** открыть топ-5 по «как писать seo статьи»; зафиксировать тип страницы (гайд, чек-лист, comparison); выписать подвопросы из PAA/«люди также ищут».
2. **Собрать семантику:** главный ключ + 15–25 смежных фраз (Wordstat/подсказки); сгруппировать в 3–5 кластеров; убрать запросы с другим intent.
3. **Построить каркас до текста:** H1 с главным ключом (≠ Title); 4–6 H2 по кластерам; под каждым H2 — тезис первым абзацем; спланировать FAQ 5–7 и таблицу/чек-лист.
4. **Написать lead и тело:** lead 40–60 слов — прямой ответ «что такое SEO-статья в 2026»; абзацы 3–5 строк; списки и таблицы вместо «полотна»; ключи естественно (H1, первый абзац, 1–2 H2, title/description).
5. **Добавить GEO-слой в тот же текст:** блок «SEO + GEO» с определением GEO; answer-first под H2; FAQ с ответами ≤80 слов; conversational заголовки («Сколько символов…», «Что такое GEO в SEO?»).
6. **Техника и E-E-A-T lite:** Title ~60–65 знаков, Description 140–160; alt у изображений; 3–5 внутренних ссылок; автор/дата на видимом месте; JSON-LD BlogPosting + FAQPage (в schema-роли, не в body).
7. **Чек-лист перед публикацией:** семантика закрыта, нет переспама, island test по H2, FAQ/schema, перелинковка, мобильная читаемость — 15–20 пунктов.
8. **Опционально llms.txt и robots.txt:** не блокировать AI-краулеры без причины; llms.txt — бонус после базового SEO.

---

## 1. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в среде Cloud Agent (2026-09-06). Инструмент `wordstat_get_top_requests` недоступен. **Точные объёмы спроса не получены** — не использовать выдуманные цифры показов.

**Экспертная семантика (SERP + конкуренты, для writer):**

| Фраза (LSI / secondary) | Примечание |
|-------------------------|------------|
| как писать seo статьи | primary_query |
| seo текст для блога | secondary |
| geo оптимизация статьи | secondary + GEO-блок |
| как написать seo текст самому | how-to variant |
| seo статья структура | structural intent |
| семантическое ядро для статьи | этап 2 workflow |
| title description seo | техблок |
| e-e-a-t seo текст | экспертность |
| чек-лист seo статьи | intent i8 (шаблон) |
| lsi слова seo | этап семантики |
| seo текст для людей | дифференциатор H1 |
| schema faqpage статья | техблок |
| сколько символов seo статья | FAQ из карточки |
| что такое geo в seo | FAQ из карточки |

*После подключения MCP:* повторить `wordstat_get_top_requests` для `как писать seo статьи`, `seo текст для блога`, `geo оптимизация статьи` и заменить таблицу на фактические показы/мес.

---

## 2. SERP-обзор (WebSearch, 2026-09-06)

`research-serp.json`: primary-запросы вернули **0 результатов** (утка DuckDuckGo) — SERP ниже только из **WebSearch Cursor**.

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|-----------------|------------------|---------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон SEO: интент, Wordstat, H1–H4, естественность ключей, мета, перелинковка; «нет универсального объёма» | Нет GEO/нейропоиска; CTA Директа | Блок про Директ; копировать структуру 1:1 без GEO |
| 2 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (09.05.2026) | Семантика → структура → E-E-A-T; Title ~65 знаков; Schema Article+FAQPage; чек-лист | Перегруз agency-кейсами; GEO как побочный эффект | Непроверенные % в кейсах; 7-разделная структура 1:1 |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii/) | Гайд 2026 + ИИ | Workflow «сначала смысл, потом оптимизация»; кластеры Wordstat; H2 = ответ сразу | Длинный sales-narrative | Копировать блоки про ИИ без human-in-the-loop |
| 4 | [serpjet.ru/blog/chto-takoe-kachestvennaja-seo-statja-v-2026-godu](https://serpjet.ru/blog/chto-takoe-kachestvennaja-seo-statja-v-2026-godu-razbiraem-na-primerah-kak-pisat-dlja-ljudej-i-robotov-4840/) | Примеры «плохо/хорошо» | Пирамида интента; H2 как обещание раздела; ИИ + anti-spam | Мало пошагового workflow | Шаблонные H2 без action |
| 5 | [divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | Пошаговая инструкция | 6 шагов: intent → семантика → структура → текст → мета → проверка; 15–25 фраз Wordstat | Нет GEO/schema deep-dive | — |
| 6 | [fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | Баланс SEO/читабельность | Акцент «для людей и роботов» | Поверхностный чек-лист | — |
| 7 | [mayai.ru/geo-optimizaciya-sajta-2026](https://mayai.ru/geo-optimizaciya-sajta-2026/) | GEO + SEO (RU) | Answer-first 40–80 слов; FAQPage; Princeton +30–40%; 74% топ-10 Google в ChatGPT | Фокус на сайт, не на «как писать статью» | Цены/CTA контент-завода |
| 8 | [fabrika-slov.com/seo-teksty-kak-pisat-stati-kotorye-popadayut-v-top-google-v-2026-godu](https://fabrika-slov.com/seo-teksty-kak-pisat-stati-kotorye-popadayut-v-top-google-v-2026-godu/) | Google-ориентир | План, семантика, чек-лист | Слабее RU/Яндекс-специфика | — |

**Паттерн SERP:** топ — «полный гайд 2026» с E-E-A-T, Wordstat, чек-листом. Отдельный кластер — GEO-лонгриды (secondary query). H1 «которые **читают люди**» слабо раскрыт — возможность Excalibur.

**Intent:** how_to — пошаговая система: семантика → структура → текст → GEO-упаковка → проверка. Вторичный: связка SEO + GEO в одном материале.

**Пробел для Excalibur:** единый **action-first workflow** «SEO для людей + GEO в одной статье» без agency-water; сама статья B01 = эталон режима B.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат (и Вебмастер) | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 должен отличаться от Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Title — ориентир ~65 знаков, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Schema.org: Article + FAQPage для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| Для одной статьи — 15–25 связанных фраз из Wordstat (частотность от ~50/мес) | [Divitio — пошаговая инструкция](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Главный ключ — в H1, первом абзаце и один раз ближе к концу; плотность вручную не считать | [Divitio — пошаговая инструкция](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Title 60–70 символов; Description 150–160 символов (ориентир для CTR) | [Sostav — SEO-продвижение 2026](https://www.sostav.ru/blogs/287906/82274) | 2026 | да |
| E-E-A-T: Experience, Expertise, Authoritativeness, Trust — фактор качества, особенно YMYL | [Sostav — SEO-продвижение 2026](https://www.sostav.ru/blogs/287906/82274) | 2026 | да |
| GEO: оптимальный answer-блок — **40–80 слов** для извлечения ИИ | [trigub.ru — GEO-продвижение](https://trigub.ru/blog/geo-prodvizhenie-sayta/) | 2026 | да |
| FAQPage JSON-LD — прямая подсказка для ИИ-моделей | [trigub.ru — GEO-продвижение](https://trigub.ru/blog/geo-prodvizhenie-sayta/) | 2026 | да |
| Princeton GEO-bench: cite sources / statistics — **+30–40%** visibility (цит. RU-гайд) | [mayai.ru — GEO чек-лист](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да (как вторичная цитата arxiv) |
| **74%** брендов из топ-10 Google присутствуют в ответах ChatGPT (цит. mayai) | [mayai.ru — GEO чек-лист](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да (как вторичная цитата) |
| Один абзац — одна мысль; длинные блоки — списками и таблицами | [digiuni.ru — SEO-текст 2026](https://digiuni.ru/kak-napisat-seo-tekst-kotoryj-ponravitsya-lyudyam-i-robotam-v-2026-godu/) | 2026 | да |
| Первый абзац после H1 — прямой ответ на главный вопрос (перевёрнутая пирамида) | [seojazz.ru — структура SEO-статьи](https://seojazz.ru/blog/opredelenie-5-punktov-universalnaja-struktura-seo-stati-dlja-rosta-trafika/) | 2026 | да |
| 51% маркетологов используют нейросети для аналитики и оптимизации, а не слепой штамповки | [fact-bank — SurveyMonkey via mayai](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026-06-11 | да |

**fact-bank.md:** прямых фактов про SEO-написание нет; использованы первичные SEO-источники + 1 строка из fact-bank (SurveyMonkey).

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); «сократите отказы на 25–40%» (digiuni — marketing); «40% пользователей на ИИ-поиске» (vc.ru без первичника); выдуманные показы Wordstat.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, закрывающий запрос человека **и** упакованный для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чек-лист.

**Дифференциация:**
- Яндекс — канон SEO без GEO; GEO-гайды не учат писать с нуля.
- Агентские гайды — E-E-A-T-кейсы и CTA.
- H1 «**которые читают люди**» — фокус на читабельность как SEO-фактор + «острова смысла» для GEO.

**Режим B:** статья B01 — **эталон**: 8,5–9,5k знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (один контент, две цели)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD в schema-роли)
4. Чек-лист перед публикацией (15–20 пунктов)

**Подтемы внутри блоков:** Wordstat/кластеры, Title/Description, E-E-A-T lite, llms.txt, AI-краулеры.

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-adjacent | «Сколько символов…», «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец longread | Ответ 2–4 предложения, ≤80 слов |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA | Блок понятен без соседних |
| Schema | schema-роль | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и конкуренты; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключевые слова в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt и нужен ли он блогу?** — опциональный сигнал для AI-краулеров; не замена sitemap/robots.txt.
7. **Как проверить статью перед публикацией?** — чек-лист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать статистику Wordstat и % из кейсов.
- Не копировать Pikapuka 1:1 (7 разделов).
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи в article.html.
- Internal link: `/` по карточке B01.
- Минимум **5** нумерованных шагов или чек-лист **10+** пунктов в теле.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| utility_verdict + reader_outcome + action_outline | ✅ |
| SERP ≥ 3 конкурента (WebSearch) | ✅ (8) |
| Wordstat MCP | ⚠️ unavailable |
| Таблица фактов с URL | ✅ (18 фактов) |
| GEO hooks | ✅ |
| FAQ 5–7 | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `blog-topics.md` + `site-brief.md`.
