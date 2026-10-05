# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата на самой статье)  
**research_date:** 2026-10-05  
**disclaimer:** Все даты, версии и статистика проверены на 05.10.2026 (Europe/Moscow).

---

## 1. SERP-обзор (WebSearch 05.10.2026 + research-serp.json)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | 5 шагов от семантики до оптимизации; H1–H4; «нет универсального объёма»; Вордстат/Вебмастер; alt, title/description, перелинковка; примеры «плохо/хорошо» | Нет GEO/нейропоиска; CTA Директа | Блоки про Директ; копировать H-структуру 1:1 без GEO-слоя |
| 2 | [articleai.ru/.../kak-napisat-seo-statyu-v-2026...](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Коммерческий longread 2026 | Семантика → публикация; AI-угол | Перегруз продуктом | Sales-first lead |
| 3 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026...](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | Кластеры, «сначала смысл — потом ключи», E-E-A-T | Длинный коммерческий хвост | Шаблон «7 разделов агентства» без дифференциации |
| 4 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu...](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Чек-лист + E-E-A-T | Title ~65 знаков; Article + FAQPage; AI-ответы | Непроверенные кейсы с % | Кейсы «+140% за 3 недели» |
| 5 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Короткий SEO-гайд | «Полный ответ на одной странице», поведенческий сигнал | Мало чек-листа/schema/GEO | Вода «просто следуй принципам» |
| 6 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Пошаговый how-to 2026 | 7 шагов + чек-лист; «текст под запрос, не под ключи» | Без GEO | — |
| 7 | [roiseo.ru/blog/struktura-seo-stati-dlya-bloga/](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон структуры блога | Первый экран 40–70 слов; таблица/ошибки/чек-лист/FAQ; Article + BreadcrumbList | Узкий фокус на шаблон | Копировать таблицу блоков 1:1 |
| 8 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 13 шагов до WordPress | Интент, конкуренты, мета, внутренние ссылки | Длинный WP-специфичный хвост | 13 H2 как каркас 1:1 |
| 9 | [trigub.ru/seo-checklist/nastroit-faqpage-schema/](https://trigub.ru/seo-checklist/nastroit-faqpage-schema/) | Техчек-лист FAQPage | RU-контекст: FAQPage для Яндекс Нейро/Алисы; требования к видимому FAQ | Уклон в услуги | Обещать FAQ-сниппет в Google для всех |
| 10 | [kashirinweb.ru/optimizaciya-sajta-pod-nejroseti/](https://kashirinweb.ru/optimizaciya-sajta-pod-nejroseti/) | GEO/AEO + SEO | «SEO — база»; FAQPage не заменяет видимый Q&A; без спец-schema для gen AI | Длинный обзор | Паника «SEO мёртв» |

**Паттерн SERP (окт. 2026):** доминируют **пошаговые гайды «SEO-текст/статья 2026»** (articleai, 1ps, pikapuka, seoshkola, olegweb) + **официальный Яндекс Direct**. Отдельный кластер по secondary «geo оптимизация статьи» — GEO-лонгриды (vc.ru, leadstream, audit4seo), не учат писать текст с нуля. **H1 «которые читают люди»** почти не занят — дифференциатор через читабельность + единый workflow SEO+GEO.

**Intent:** `how_to` — собрать семантику → структура → черновик → мета/schema → чеклист → публикация. Вторичный: встроить **GEO** (FAQ, атомарные H2) без второго проекта.

**Пробел для Excalibur:** один **action-first** longread: «для людей» (инфостиль, острова смысла) + **18-пунктовый чеклист** + FAQ/schema handoff; режим B — **сама статья = эталон** (8 500–9 500 знаков по quality-blog).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` / инструмент `wordstat_get_top_requests` **не доступен** в cloud-сессии 05.10.2026 (namespace не подключён). Точные **показы в месяц не получены** — в тексте статьи **не указывать** числа спроса, пока Wordstat не обновят (при 401: [OAuth Yandex](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40)).

**Семантика для writer (без частотности, из карточки + SERP):**

| Кластер | Фразы |
|---------|--------|
| Primary | как писать seo статьи, как написать seo статью, seo статья для блога |
| Secondary | seo текст для блога, seo текст как написать |
| GEO | geo оптимизация статьи, seo и geo в одной статье, что такое geo в seo |
| FAQ / long-tail | сколько символов в seo статье, чек-лист seo статьи, структура seo статьи для блога |

**LSI (из топа выдачи и Яндекс Direct):** семантическое ядро, Яндекс Вордстат, LSI/тематические слова, title и description, alt-текст, перелинковка, E-E-A-T, FAQPage, BlogPosting, нейровыдача, answer-first, интент запроса.

---

## 3. Таблица фактов (цифры только с URL; fact-bank.md по SEO пуст)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 структурируют смысловые блоки | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир **3–5 строк**; списки для перечислений | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают **смысл и полезность**, не плотность ключей; переспам вреден | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в **Яндекс Вордстат** и **Яндекс Вебмастер** | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| К каждому изображению — **alt-текст**; файлы латиницей | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение → основная часть по шагам → заключение с **следующим шагом** | [Яндекс Direct — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Частотность запросов проверяют в Вордstat с учётом **региона** | [Яндекс Direct — семантическое ядро](https://direct.yandex.ru/base/articles/semanticheskoe-yadro-sajta) | 2026 | да |
| Кластеризация — группировка ключей по смыслу; **отдельная страница на кластер** | [Яндекс Direct — семантическое ядро](https://direct.yandex.ru/base/articles/semanticheskoe-yadro-sajta) | 2026 | да |
| Title — ориентир **~65 знаков**, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| H1 не дублирует Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Schema.org: **Article + FAQPage** для структуры и сниппета | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Первый экран: ответ на вопрос в **40–70 словах** | [ROI SEO — структура статьи для блога](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| SEO-статья блога: блоки «ошибки», **чек-лист**, FAQ под FAQPage | [ROI SEO — структура статьи для блога](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| Title **≤60** символов, meta description **140–160** — типичный техчек-лист | [Spilno Agency — SEO copywriting 2026](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да |
| Главный ключ — H1, первый абзац, 1–2 H2; LSI — естественно, без подсчёта «плотности» | [divitio.ru — SEO-текст](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Если пользователь **возвращается в поиск** — сигнал низкого качества ответа | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| GEO (Generative Engine Optimization) — оптимизация для **цитирования в AI-ответах**, не замена SEO | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Нейросети извлекают **passages** — каждый H2 = самодостаточный «остров смысла» | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| **Первые 100–150 слов** — зона извлечения ответа AI | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Google с **августа 2023** ограничил FAQ rich results в основном **гос./мед.** сайтами; для RU — FAQPage всё ещё сигнал для **Яндекс Нейро/Алисы** | [trigub.ru — FAQPage schema](https://trigub.ru/seo-checklist/nastroit-faqpage-schema/) | 2026 | да |
| Google **7 мая 2026** отключил FAQ rich results; для gen AI **спец. schema не обязательна** — цитируется **видимый** Q&A | [seoscore.tools — FAQ Schema 2026](https://seoscore.tools/ru/blog/faq-schema-markup/) | 2026 | да |
| База GEO/AEO — **классическое SEO**; FAQPage корректен, если совпадает с видимым FAQ | [KashirinWeb — оптимизация под нейросети](https://kashirinweb.ru/optimizaciya-sajta-pod-nejroseti/) | 2026 | да |
| Princeton GEO (arxiv): добавление **источников/цитат/статистики** повышает visibility в generative engines; keyword stuffing **хуже** baseline | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |

**Не использовать без оговорки:** «+140% трафика» (Pikapuka); «плотность ключей 1–2%» как жёсткое правило (Seotika — устаревший KPI vs Яндекс Direct); «FAQPage обязателен для ChatGPT» как гарантия (KashirinWeb/seoscore); «микроразметка ×1,5–2 цитирование» без первичника.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **longread для человека**, упакованный под поиск и **нейровыдачу** в **одном workflow**: интент → семантика → каркас H2 → черновик (инфостиль) → FAQ + JSON-LD → GEO-чанки → **чеклист 15–18 пунктов** перед публикацией.

**Почему отличается от конкурентов:**
- Яндекс — канон без GEO; GEO-гайды — без «как написать с нуля».
- Агентские лонгриды — E-E-A-T-кейсы и CTA.
- H1 «**которые читают люди**» — фокус на **читабельность как SEO/GEO-фактор** (3–5 строк, lead, острова смысла).

**H2-каркас (карточка B01 + research):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread (H1–H3, lead, списки, таблицы)  
3. FAQ и schema (BlogPosting + FAQPage — в schema, не в body как JSON)  
4. Чеклист перед публикацией (15–18 пунктов)

**Режим B:** статья B01 — **эталон** формата блога (8 500–9 500 знаков, 5–7 FAQ, перелинковка на `/`).

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2/FAQ | FAQ | «Сколько символов…», «Что такое GEO в SEO?» |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; 3–4 предложения в абзаце |
| Island test | QA | Блок понятен без соседних |
| Schema handoff | schema-агент | BlogPosting + FAQPage |
| llms.txt | Упоминание | Опционально после базового SEO |
| Alt обложки | cover_scene_hint | «Редактор за ноутбуком…» |

**Целевые формулировки:** как писать seo статьи, seo текст для блога, geo оптимизация статьи, сколько символов в seo статье, что такое geo в seo.

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс Direct); ориентир — полнота ответа и SERP; для how-to longread Excalibur — **8 500–9 500** знаков.  
2. **Что такое GEO в SEO?** — дополнение к SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.  
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + LSI (Яндекс Direct).  
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 на странице; не дублировать.  
5. **Какие schema для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage для блока вопросов.  
6. **Нужен ли llms.txt блогу?** — опциональный сигнал; не замена sitemap/robots.  
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Цифры только из раздела 3; fact-bank по SEO пуст.  
- Не копировать Pikapuka/olegweb структуру 1:1.  
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).  
- Min **5** нумерованных шагов в теле + чеклист **15–18** пунктов.  
- Без эмодзи в article.html; CTA ≤ 3.  
- internal_links: `/` (главная).

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику под один запрос, спроектирует longread с lead и FAQ, напишет черновик без переспама, заполнит Title/Description, подготовит handoff для BlogPosting + FAQPage и пройдёт чеклист из 15–18 пунктов перед публикацией — с учётом GEO (атомарные H2, видимый FAQ).

**action_outline:**

1. **Зафиксировать интент:** primary «как писать seo статьи» + 2 secondary; one page = one intent (карточка B01).  
2. **Собрать семантику:** Вордstat + подсказки + 5 URL из SERP → 15–25 фраз и LSI; кластер не смешивать с «geo оптимизация сайта» (другая статья B04).  
3. **Разобрать ТОП-5:** формат (шаги/чек-лист), H2-карта, content gap (читабельность + GEO в одном workflow).  
4. **Собрать каркас:** H1 из карточки; 4 H2 из outline; под каждым H2 — тезис в первом предложении; lead **40–70 слов** с прямым ответом.  
5. **Написать черновик:** абзацы 3–5 строк; таблица или список; главный ключ в H1 и lead; без keyword stuffing (Яндекс Direct).  
6. **Добавить FAQ 5–7:** короткие ответы-действия; пары вопрос–ответ **видимы** на странице (совпадение с FAQPage).  
7. **Мета и медиа:** Title ≤60–65 знаков, Description 140–160; alt у изображений; 2–4 внутренние ссылки (в т.ч. `/`).  
8. **GEO-слой:** проверить island test на каждом H2; первые 100–150 слов — определение + польза; опционально упомянуть llms.txt.  
9. **Финальный чеклист 15–18 пунктов** (семантика, мета, H-иерархия, FAQ, schema handoff, ссылки, proofread) → публикация → через 2–4 недели — позиции/поведение в Мetrica.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (10) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (24 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
