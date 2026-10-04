# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to + чеклист)  
**search_intent:** how_to  
**research_date:** 2026-10-04  
**disclaimer:** Все даты, версии и статистика проверены на 2026-10-04 (2026 год).

---

## Utility (Gate 2)

**utility_verdict:** PASS  

**reader_outcome:** Читатель сможет за один рабочий цикл — от сбора семантики в Вордстате до финального чеклиста — подготовить и опубликовать SEO-longread для блога с FAQ, мета-тегами и JSON-LD, который закрывает интент людей и пригоден для цитирования в нейропоиске.  

**action_outline (workflow статьи):**

1. Зафиксировать **primary query** и интент; в Яндекс Вордстат собрать кластер (основной запрос + 5–20 хвостов и вопросов), отсечь запросы с другим намерением.  
2. Разобрать **ТОП-10** по запросу: тип страниц, медианный объём, повторяющиеся H2, наличие таблиц/FAQ/видео; выписать обязательные смысловые блоки и пробелы конкурентов.  
3. Собрать **каркас** до текста: один H1, H2 как подзадачи how-to, H3 для шагов; после каждого H2 — сразу содержательный ответ (answer-first).  
4. Написать **lead** (40–100 слов) с прямым ответом на запрос; черновик по блокам — короткие абзацы 3–5 строк, списки, одна таблица «ошибка → что делать».  
5. Встроить ключи **естественно** (основной — H1, первый абзац, 1–2 H2, Title/Description); проверить тематическую полноту (LSI из ТОПа), без переспама.  
6. Оформить **технику:** Title ~55–60 символов (не дублировать H1), Description ~150–160 символов, alt у изображений, 2–3 релевантные внутренние ссылки, canonical.  
7. Добавить **GEO-слой:** 5–7 FAQ в видимом HTML; BlogPosting + FAQPage JSON-LD; блоки по 40–60 слов, пригодные для сниппета/AI.  
8. Пройти **чеклист 15–18 пунктов** перед публикацией; после выкладки — контроль в Яндекс Вебмастер / Метрике (показы, CTR, поведение).

---

## 1. SERP-обзор (WebSearch Cursor, 04.10.2026 + research-serp.json)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|-----------------|------------------|---------------|
| 1 | [direct.yandex.ru/.../seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон требований: объём без «магической цифры», H1–H4, Вордстат, естественные ключи, Title/Description, alt | Нет отдельного GEO-блока; CTA в экосистему Директа | Коммерческий финал; структура 1:1 |
| 2 | [seoshkola.com/.../kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Практик, 7 шагов (обнов. 10.07.2026) | Чёткий цикл: семантика → ТОП → структура → мета → релевантность; Title 55–60 / Description 150–160 | Упор на платные инструменты (Seolity, Арсенкин) | Продажу сервисов как единственный путь |
| 3 | [olegweb.ru/.../kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | How-to + WordPress (2026) | 13 шагов, интент, E-E-A-T, таблицы/списки, чек-лист перед публикацией | Длинный WP-фокус; GEO — фоном | 13 H2 без сжатия в 4 блока карточки B01 |
| 4 | [seotika.ru/kak-pisat-seo-stati](https://seotika.ru/kak-pisat-seo-stati/) | Агентский гайд (21.06.2026) | Lead с ответом в 100 словах; таблица «обычный текст vs SEO»; объём 1500–3000 слов как ориентир для info | Плотность ключей 1–2% — спорная метрика; agency tone | Непроверенные кейсы агентства |
| 5 | [1ps.ru/.../seo-tekstyi-2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Семантические кластеры, E-E-A-T, постобработка ИИ-текста | Перегруз про «минуты на статью» и автomation-hype | Обещания скорости без QA |
| 6 | [pikapuka.com/.../e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Чек-лист 10 шагов (2026) | Schema Article + FAQPage; Featured Snippet / AI-ответы | Кейсы «+140%» без первичника | 7-разделную структуру 1:1 |
| 7 | [articleai.ru/.../poshagovaya-instruktsiya](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Пошаговая инструкция 2026 | Семантика → публикация; акцент на ИИ в цикле | Мало про «читают люди» vs роботы | AI-first narrative |
| 8 | [mv-blog.ru/.../geo-optimizaciya-stati-checklist](https://mv-blog.ru/blog/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | GEO чек-лист статьи | Snippet-first lead 40–60 слов, FAQ в HTML, BlogPosting + FAQPage, таблица «можно публиковать» | Контекст 1С-Битрикс | CMS-специфику как универсальный стандарт |

**Паттерн SERP (октябрь 2026):** доминируют **пошаговые гайды 2026** (7–13 шагов), **чек-листы**, **E-E-A-T**, **FAQ + schema**. Отдельный кластер — **GEO/AEO** (lead, FAQ, JSON-LD). Запрос «**как писать seo статьи**» почти не закрывает H1 «**которые читают люди**»: конкуренты говорят про ТОП и ключи, реже — про **читабельность + GEO в одном workflow**.

**Intent:** how_to — собрать семантику → понять интент → структура → текст → мета → проверка → публикация. Вторичные: **seo текст для блога** (формат блога, чек-лист контент-фазы), **geo оптимизация статьи** (snippet-first, FAQ, schema на уровне одной статьи).

**Пробел для Excalibur:** один **практический longread-шаблон** «SEO + GEO на одной странице» с **4 H2 из карточки**, **18-пунктовым чеклистом** и **самодемонстрацией формата** (режим B); меньше agency/water, больше «что сделать / не делать» в каждом блоке.

---

## 2. Яндекс Wordstat (MCP `user-mcp-kv`)

⚠️ **WORDSTAT MCP WARNING:** в Cloud Agent сессии namespace `user-mcp-kv` **не подключён** (инструмент `wordstat_get_top_requests` недоступен). Вызов API не выполнен; **точные показы в месяц не получены** — цифры спроса в текст статьи **не добавлять**.

При восстановлении MCP проверить запросы:

- `как писать seo статьи` (primary)  
- `seo текст для блога`, `geo оптимизация статьи` (secondary)  
- смежные из SERP: `как написать seo статью`, `seo копирайтинг`, `seo текст`, `структура seo статьи`, `чеклист seo статьи`

**LSI для writer (из SERP + WebSearch, без частотности):**

- как написать seo статью, seo текст для блога, seo копирайтинг 2026  
- семантика, яндекс вордстат, интент запроса, lsi-слова, кластер запросов  
- title description, h1 h2 h3, longread, чеклист перед публикацией  
- e-e-a-t, экспертность автора, перелинковка, alt-текст  
- geo, generative engine optimization, faqpage, json-ld, snippet-first, нейропоиск  

**SEO-стратегия (без Wordstat-цифр):** primary в H1/lead/Title; secondary — в H2 и FAQ; «geo оптимизация статьи» — отдельный подблок в H2 «SEO + GEO», не подменять H1.

---

## 3. Таблица фактов (≥15, только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир **3–5 строк**; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают **смысл и полезность**, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику подбирают в **Яндекс Вордстат** (и смежные инструменты вебмастера) | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на **сниппет и кликабельность** | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-текст 2026 — полезный текст, структура и словарь под **конкретный запрос и окружение**, не «ключ через два абзаца» | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| Алгоритмы учитывают **интент**, тематическую полноту, поведение (дочитывание, возврат в выдачу), отсутствие переспама | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| Title — ориентир **до 55–60 символов**; Description — **до 150–160**; Title не дублирует H1 дословно | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| SEO-статья в ТОП закрывает **интент структурированно**; прямой ответ — в **первых ~100 словах** | [Seotika — гайд](https://seotika.ru/kak-pisat-seo-stati/) | 02.09.2026 | да |
| Для информационной статьи ориентир **1500–3000 слов** (если ТОП — longread); объём сверять с медианой конкурентов | [Seotika — гайд](https://seotika.ru/kak-pisat-seo-stati/) | 02.09.2026 | да* |
| Иерархия заголовков **H1 → H2 → H3** без «перепрыгивания»; H2 — крупные вопросы пользователя | [Seotika — гайд](https://seotika.ru/kak-pisat-seo-stati/) | 02.09.2026 | да |
| Контент-архитектура 2026: **pillar → hub → cluster** + внутренние ссылки; GEO/AEO — структурированные ответы под generative/voice | [PW Agency — SEO 2026](https://pw.agency/blog_new/seo/seo-2026-intent-karty-i-kontent-arkhitektura-vmesto-klyuchevykh-slov/) | 2026 | да |
| GEO (Generative Engine Optimization) — оптимизация видимости контента в **ответах generative engines** | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | KDD 2024 | да |
| GEO-bench: **10 000** запросов; методы с **цитатами, цитированием источников и статистикой** дают до **+40%** visibility (Position-Adjusted Word Count); на Perplexity.ai — до **37%** | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | KDD 2024 | да |
| Keyword stuffing в GEO-экспериментах **хуже baseline** (~−10%) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | KDD 2024 | да |
| GEO-чеклист статьи: lead **40–60 слов**, **5–7 FAQ** в видимом HTML, **BlogPosting + FAQPage** JSON-LD, **2–3** внутренние ссылки | [mv-blog.ru — GEO checklist](https://mv-blog.ru/blog/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | 2026 | да |
| Шаблон SEO-статьи блога: первый экран — ответ **40–70 слов**; блоки «ошибки», **чек-лист**, **FAQ** под FAQPage | [roiseo.ru — структура](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |

\* Ориентир Seotika — не универсальная норма; приоритет — полнота ответа и медиана ТОПа (согласовано с Яндекс Директ).

**Сверка с `memory/brief/fact-bank.md`:** прямых строк про SEO-статьи нет; для B01 использовать таблицу выше. Fact-bank применим для **смежных** тем (ИИ-контент, автоматизация) — в B01 не смешивать без запроса карточки.

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «1–2% плотность ключей» как жёсткое правило; цифры Wordstat без API; «56% AI vs search» (LeadStream) без cross-check первичника.

---

## 4. Угол и дифференциация

**Главный угол:** SEO-статья 2026 = **инструкция для человека**, упакованная так, чтобы **поиск и нейросеть** могли извлечь ответы: интент → каркас longread → инфostиль → FAQ/schema → **GEO-чанки** → **чеклист 15–18 пунктов**.

**Отстройка:**

- Яндекс — канон SEO без GEO-слоя на уровне одной статьи.  
- GEO-чеклисты — про CMS/сайт, не про «как писать с нуля».  
- Агентские гайды — длинные воронки и непроверенные кейсы.  
- H1 «**которые читают люди**» — через **короткие абзацы, answer-first, island test**, а не через «ещё ключей».

**Режим B:** сама статья B01 — **эталон** longread Excalibur (~8 500–9 500 знаков текста по quality-blog), BlogPosting + FAQPage, 5–7 FAQ из `faq_hints`.

**H2-каркас (карточка B01):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread  
3. FAQ и schema  
4. Чеклист перед публикацией  

**Tone:** практично, по-человечески; каждый H2 = подзадача + рекомендация (делать / не делать).

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead после H1 | 40–60 слов, standalone |
| Определение GEO | H2 «SEO + GEO» | 40–60 слов |
| Answer-first | Первые 100 слов + начало каждого H2 | Прямой ответ, без «в этой статье» |
| Conversational H2/H3 | FAQ hints | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 | Конец | Ответ 2–4 предложения, действие |
| JSON-LD | schema role | BlogPosting + FAQPage (не в body) |
| Внутренняя ссылка | CTA | На `/` (карточка) |
| Alt обложки | cover | `cover_scene_hint` из карточки |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и медиана ТОПа; для how-to longread Excalibur — ~8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе из индексируемого структурированного контента.  
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + тематический словарь (LSI).  
4. **Чем Title отличается от H1?** — Title для сниппета (~55–60 симв.), H1 на странице; смысл общий, формулировки разные.  
5. **Какие schema нужны блоговой SEO-статье?** — BlogPosting (или Article) + FAQPage при видимом FAQ.  
6. **Как оптимизировать статью под GEO?** — snippet-first lead, FAQ в HTML, факты с источниками, JSON-LD, атомарные H2.  
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer / QA

- Цифры только из §3; Wordstat — после подключения MCP.  
- Не копировать структуру Pikapuka / Seotika 1:1.  
- Без эмодзи; CTA ≤ 3.  
- `site_url` example.com — ссылки по карточке (`/`).  
- Island test и So what test на каждый H2 (`shared/editorial-utility-only.md`).

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| utility_verdict + action_outline | ✅ |
| SERP ≥ 3 конкурента (свежий WebSearch) | ✅ |
| Таблица фактов ≥ 15 URL | ✅ |
| Wordstat (MCP) | ⚠️ недоступен |
| GEO hooks + FAQ | ✅ |
| H2 из карточки | ✅ |

**Writer:** вход — этот файл + `research-context.json` + `memory/topics/blog-topics.md` (B01) + `memory/brief/site-brief.md`.
