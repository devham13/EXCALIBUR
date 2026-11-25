# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + эталон формата на самой статье)  
**search_intent:** how_to  
**research_date:** 2026-10-06  
**disclaimer:** Все даты, версии и статистика проверены на 2026-10-06 (2026 год).

---

## Utility gate (research)

| Поле | Значение |
|------|----------|
| **utility_verdict** | **PASS** |
| **topic utility gate** | PASS (`scripts/excalibur_blog_utility_gate.py --topic-id B01`, 2026-10-06) |
| **reader_outcome** | Читатель пройдёт единый workflow от семантики до публикации: соберёт запросы, спланирует структуру longread, напишет текст «для людей», добавит FAQ/schema и GEO-чанки и проверит статью чек-листом перед выходом в индекс. |
| **action_outline** | 1) Зафиксировать primary query и интент (informational how-to). 2) Собрать 15–25 фраз в Яндекс Вордстат и сгруппировать по смыслу. 3) Разобрать TOP-5 SERP: формат, H2, объём, пробелы. 4) Составить каркас H1 → 5–8 H2 → H3 + lead с ответом в первых 40–100 словах. 5) Написать черновик (короткие абзацы, списки, таблица, без переспама). 6) Оформить Title (~60 знаков), Description (140–160), URL, alt, 3–5 внутренних ссылок. 7) Добавить FAQ (5–7 пар), JSON-LD BlogPosting + FAQPage, GEO-слой (атомарные H2, цифры с источниками). 8) Прогнать финальный чек-лист и назначить контроль позиций/AI-цитирования через 2–4 недели. |

---

## Яндекс Вордстат (спрос и LSI)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` не подключён в среде Cloud Agent (2026-10-06). Вызов `wordstat_get_top_requests` для «как писать seo статьи» **не выполнен** — **точные показы в месяц не получены**. Обновите токен и MCP: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Primary query:** `как писать seo статьи`  
**Secondary (карточка B01):** `seo текст для блога`, `geo оптимизация статьи`

**LSI-кластер для writer (из SERP/WebSearch, без подстановки частотности):**

| Группа | Фразы для естественных вхождений |
|--------|----------------------------------|
| Действие | как написать seo статью, как писать seo текст, seo статья пошагово |
| Формат | seo текст для блога, структура seo статьи, seo копирайтинг 2026 |
| Техника | title и description, мета-теги, семантическое ядро, вордстат |
| Качество | e-e-a-t, чек-лист seo статьи, переспам ключей |
| GEO | geo оптимизация статьи, нейровыдача, faq для ai, llms.txt |

После восстановления Wordstat — дополнить таблицу «Фраза | Показы/мес» и отсечь запросы с другим интентом (коммерция «заказать seo текст» → отдельные посадочные).

---

## 1. SERP-обзор (WebSearch + research-serp.json, 2026-10-06)

**Запросы проверки:** «как писать seo статьи 2026», «seo текст для блога чеклист», «geo оптimизация статьи 2026» (вторичный — мало выдачи по exact match; кластер GEO закрывают Habr/vc.ru/pawetta).

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|-----------------|------------------|---------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: интент, Wordstat, H1–H4, естественность ключей, 3–5 строк абзац, title/description, 5 шагов workflow | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа; «SEO = ключи» |
| 2 | [articleai.ru/.../kak-napisat-seo-statyu-v-2026...](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Агентский how-to 2026 | Семантика → публикация, акцент на AI-выдачу | Перегруз «ИИ пишет за вас» | Структура 1:1 |
| 3 | [seoshkola.com/.../kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Практический 7-шаговый гайд | Чёткие шаги + чек-лист перед публикацией; «текст под запрос, не под ключи» | Слабый GEO-слой | — |
| 4 | [seotika.ru/kak-pisat-seo-stati](https://seotika.ru/kak-pisat-seo-stati/) | SEO-агентство | Lead в 100 словах, иерархия H1→H2→H3, объём 1500–3000 слов как ориентир | Плотность ключей 1–2% — спорно vs Яндекс «по смыслу» | Слепое следование «плотности» |
| 5 | [roiseo.ru/.../struktura-seo-stati-dlya-bloga](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон блога | Таблица блоков (ответ → ошибки → чек-лист → FAQ), schema | Мало семантики/Wordstat | — |
| 6 | [habr.com/ru/articles/1030292](https://habr.com/ru/articles/1030292/) | GEO field guide | Chunking/RAG, GEO как надстройка SEO, метрики AI-referral | Не учит писать статью с нуля | Цифры «−20–40% органики» без контекста ниши |
| 7 | [pikapuka.com/.../kak-napisat-seo-tekst-samomu...](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Longread E-E-A-T | Чек-лист, schema Article+FAQ | Непроверенные кейсы с % | Кейсы без источника |

**Паттерн SERP 2026:** доминируют «полный гайд / пошаговая инструкция 2026» + чек-лист; отдельный кластер — GEO под LLM. H1 «которые читают люди» почти не занят — дифференциатор B01.

**Intent:** how_to — система «семантика → структура → текст → мета → FAQ/schema → GEO → проверка». Вторичный: связать SEO-текст блога с цитированием в AI-ответах.

---

## 2. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не «плотность» ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Workflow Яндекса: тема/конкуренты → семантика → структура → текст → оптимизация (5 шагов) | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Лид — прямой ответ в первых ~100 словах; H2 как ответы на вопросы | [Seotika — SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| Для информационных материалов в русскоязычных гайдах часто указывают ориентир **1500–3000 слов** (не норма, а ориентир по SERP) | [Seotika — SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да* |
| Title ≤60 символов, meta description 140–160 — типичный техчеклист перед публикацией | [Spilno Agency — SEO copywriting](https://spilnoagency.com.ua/ru/instructions-ru/seo-copywriting) | 2026 | да |
| 15–25 связанных фраз из Wordstat с порогом от ~50 показов/мес — практика сбора ядра | [Divitio — SEO-текст](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да* |
| Главный ключ — H1, первый абзац, один раз ближе к концу; без ручного подсчёта «плотности» | [Divitio — SEO-текст](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| В статье обычно **5–10 блоков H2**; ключи в 2–3 H2 естественно | [Marketing Klub — SEO-статьи](https://marketingklub.ru/kak-pisat-seo-stati/) | 2026 | да |
| GEO (Generative Engine Optimization) — оптимизация видимости в ответах generative engines; термин формализован в препринте **16.11.2023**, представлен на **ACM KDD 2024** | [vc.ru — Writing for GEO](https://vc.ru/id4616024/3174294-kak-pisat-stati-dlya-generativnogo-poiska-i-seo) | 2026 | да |
| RAG-системы извлекают **фрагменты (chunks)**, не страницы целиком — каждый H2-блок конкурирует отдельно | [Habr — GEO/AIO/AEO](https://habr.com/ru/articles/1030292/) | 2026 | да |
| Техническое SEO остаётся фундаментом; GEO — надстройка над индексируемым контентом | [Habr — GEO/AIO/AEO](https://habr.com/ru/articles/1030292/) | 2026 | да |
| В исследовании GEO-bench комбинация методов (statistics + citations + readability) давала до **~40%** прироста visibility (PA-WC) в экспериментах — не гарантия для любой ниши | [Habr — GEO доказательно](https://habr.com/ru/articles/989222/) | 2026 | да* |
| Title до 60 символов, description до 160, FAQPage + Article schema — базовый GEO-чеклист | [MayAI — GEO 2026](https://mayai.ru/geo-optimizaciya-sajta-2026/) | 2026 | да* |
| Главная задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| H1 должен отличаться от Title; Title ~65 знаков с триггером «инструкция/чек-лист» | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |

\* Ориентир агентского/медийного источника — в тексте помечать как рекомендацию, не как правило поисковика. Princeton GEO-bench — ссылаться на исследование, не обещать +40% каждому сайту.

**fact-bank.md:** прямых строк по SEO-копирайтингу нет; AI/контент-завод факты из bank **не смешивать** с этой статьёй без отдельного угла.

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); непроверенные «AI обрабатывает 25% запросов»; обещания ROI от GEO без кейса.

---

## 3. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один список ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → **финальный чек-лист**.

**Отличие от конкурентов:**
- Яндекс — канон без GEO; GEO-лонгриды не ведут новичка от нуля.
- Агентские гайды перегружены «ИИ напишет за вас» и кейсами.
- H1 «**которые читают люди**» — фокус на читабельности как SEO/GEO-сигнале (lead, «острова смысла», без воды).

**Режим B:** сама B01 — эталон: ~8,5–9,5k знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, перелинковка на `/`.

**Tone:** практично, по-человечески; без корпоративной воды и эмодзи.

**H2-каркас (writer):**
1. Зачем писать SEO-статью под людей и под AI (один контент, две цели)
2. Семантика и разбор SERP перед планом
3. Структура longread: H1–H3, lead, таблица, списки
4. Написание: инфостиль, ключи, E-E-A-T lite
5. Мета, URL, изображения, внутренние ссылки
6. FAQ, schema и GEO-чанки
7. Чек-лист перед публикацией (15+ пунктов)

---

## 4. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Первый абзац после H1 | 40–60 слов |
| Определение GEO | Блок «SEO + GEO» | 40–60 слов |
| Conversational H2 | «Что такое GEO в SEO?», «Сколько символов в SEO-статье?» | Вопрос в заголовке |
| FAQ 5–7 | Конец | Ответ 2–4 предложения, действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema | Не в body HTML | BlogPosting + FAQPage |
| llms.txt | Упоминание | Опциональный сигнал, не замена sitemap |
| Даты | Метаданные | datePublished / dateModified = дата публикации |

**AI-формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 5. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и TOP SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — надстройка: цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (~60 знаков), H1 на странице; не дублировать дословно.
5. **Какие schema для блога?** — BlogPosting (или Article) + FAQPage.
6. **Нужен ли llms.txt?** — полезный опциональный файл для AI-краулеров.
7. **Как проверить статью перед публикацией?** — чек-лист: семантика, мета, структура, FAQ, schema, ссылки, мобильная вёрстка.

---

## 6. Риски для writer

- Цифры только из таблицы фактов выше (+ quality-blog объём).
- Не копировать структуру Pikapuka/articleai 1:1.
- Без эмодзи, без VPN/обход блокировок.
- `site_url` example.com — плейсхолдер `/` по карточке.
- После восстановления Wordstat — writer/QA сверить primary с реальными показами.

---

## 7. Готовность к writer

| Критерий | Статус |
|----------|--------|
| utility_verdict + action_outline | ✅ |
| SERP ≥ 5 конкурентов (свежий WebSearch) | ✅ |
| Wordstat (точные показы) | ⚠️ MCP недоступен |
| Таблица фактов ≥ 15 с URL | ✅ |
| Угол + GEO hooks + FAQ | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + B01 в `blog-topics.md` + `site-brief.md`.
