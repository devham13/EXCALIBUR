# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + эталон формата на самой статье)  
**research_date:** 2026-10-14  
**disclaimer:** Все даты, версии и статистика проверены на 14.10.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch + research-serp.json, 2026-10-14)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Авторитет; workflow «тема → семантика → структура → текст → мета»; нет универсального объёма; естественность ключей; H1 один раз; Вордстат | Нет GEO/нейровыдачи; CTA Директа | Коммерческий блок Директа; копировать H1–H4 без GEO-слоя |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Агентский гайд 2026 | «Сначала смысл, потом ключи»; H2 = подтема кластера; E-E-A-T lite; ИИ как помощник | Перегруз про ИИ; мало отдельного блока «читабельность» | Шаблон «7 разделов агентства» 1:1 |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-…](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Longread + чек-лист (2026) | Wordstat/Serpstat; Title ~65 знаков; Schema Article + FAQPage; AI-ответы | Кейсы с непроверенными %; GEO как побочный эффект E-E-A-T | «+140% трафика» и прочие цифры без первичника |
| 4 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Пошаговый гайд 2026 | 7 шагов от запроса до контроля после публикации; акцент «под запрос, не под ключи» | Слабее GEO; мало FAQ/schema | — |
| 5 | [serptop.ru/blog/kak-pisat-seo-teksty/](https://serptop.ru/blog/kak-pisat-seo-teksty/) | Руководство + чек-лист | Формула H1; блок «ошибки / как не делать»; техника (meta, ЧПУ, мультимедиа) | Длинный обзор, меньше «люди vs роботы» | — |
| 6 | [developers.google.com/search/docs/fundamentals/ai-optimization-guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | Официальный Google | SEO = база для generative AI; Schema не обязательна для AI Search; llms.txt Google Search игнорирует | Не учит писать текст с нуля; фокус Google, не Яндекс | Переоценивать llms.txt/«магическую» Schema для Google |

**Паттерн SERP (окт. 2026):** доминируют «полный гайд 2026» (семантика → структура → E-E-A-T → ИИ). Отдельный кластер — GEO-лонгриды (digitalrocket, leadstream, vc.ru). H1 «которые **читают люди**» в топе почти не встречается — окно для дифференциации через читабельность + единый workflow SEO+GEO.

**Intent:** `how_to` — пошаговая система от интента до чек-листа публикации. Вторичный: связать SEO-текст и GEO-упаковку в **одном** материале, не два проекта.

---

## 2. Yandex Wordstat (спрос)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` / `wordstat_get_top_requests` в среде прогона недоступен (namespace not found). Точные показы в месяц **не получены**. Для writer — опираться на LSI из SERP и карточки темы; после восстановления MCP пересобрать таблицу спроса.

**Экспертная семантика (без частотности, из SERP и secondary_queries):**

| Фраза (LSI / смежные) | Откуда |
|-----------------------|--------|
| как писать seo статьи | primary_query |
| seo текст для блога | secondary |
| geo оптимизация статьи | secondary |
| как написать seo статью пошагово | SERP titles |
| seo копирайтинг 2026 | SERP |
| e-e-a-t seo статья | Pikapuka, Google |
| структура seo статьи h2 h3 | Seotika, Serptop |
| title description seo | Yandex Direct, Divitio |
| faq schema blogposting | Pikapuka, ROI SEO |
| llms.txt блог | Google AI guide, GEO-кластер |
| нейровыдача яндекс контент | iq-maxima, GEO SERP |
| полезный контент people-first | Google Search Central |

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата источника | Можно в текст |
|------|----------|----------------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордstat (частотность, формулировки, интент) | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| E-E-A-T: Experience, Expertise, Authoritativeness, Trustworthiness; **Trust** — центральный критерий | [Google — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| E-E-A-T сам по себе не один «фактор ранжирования», но системы используют сигналы, связанные с E-E-A-T | [Google — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| Контент «в первую очередь для людей» согласован с тем, что вознаграждают core ranking systems | [Google — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| Structured data **не обязательна** для generative AI в Google Search; «специальной» Schema для AI нет | [Google — AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | актуально 2026 | да |
| llms.txt и подобные файлы Google Search **игнорирует** — не помогают и не вредят видимости в Google Search | [Google — AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | актуально 2026 | да |
| Schema по-прежнему полезна для rich results в классической выдаче | [Google — AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | актуально 2026 | да |
| Title — ориентир до ~60 символов, ключ в начале; не дублировать H1 дословно | [Divitio — SEO-текст](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Meta description — до ~155 символов, ключ + выгода (CTR, не прямой ranking) | [Divitio — SEO-текст](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Для одной страницы — 15–25 связанных фраз из Вордстата, сгруппированных по смыслу | [Divitio — SEO-текст](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Главный ключ — H1, первый абзац, 1–2 H2, title/description; без механического переспама | [Divitio — SEO-текст](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| SEO-текст в 2026 = полезный текст под **конкретный запрос** и его окружение, не «набивка ключей» | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| После каждого H2 — сразу содержательный ответ (правило структуры) | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Title ~65 знаков с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| BlogPosting/Article + FAQPage — типовая связка для блога с FAQ | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Нейросистемы извлекают **passages** — каждый H2 = автономный «остров смысла» | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| 51% маркетологов используют нейросети для аналитики и оптимизации, а не для слепой штамповки контента | [fact-bank → SurveyMonkey](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026-06-11 | да |

**Не использовать:** «+140% трафика» (Pikapuka); «+40% видимости GEO» без arxiv/Aggarwal в тексте; «Schema ×1,5–2 цитирование» без первичника; 39% ВЦИОМ / 20% Mediascope — только с первичником, не из агентских пересказов.

**fact-bank.md:** прямых строк про SEO-копирайтинг нет; допустимы только строки про ИИ-контент (SurveyMonkey 51%) как контекст «не писать шаблоном из ChatGPT».

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один список ключей», а **единый workflow**: интент → семантика → структура с answer-first → инфostиль → FAQ/schema → GEO-чанки → чеклист публикации.

**Отличие от SERP:**
- Яндекс Direct — канон без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды перегружены ИИ и кейсами; мало «читабельность как SEO-сигнал».
- H1 B01 («**которые читают люди**») слабо раскрыт конкурентами.

**Режим B:** статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage (schema-агент), атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (карточка + research):**
1. Зачем SEO и GEO в одной статье
2. Структура longread (H1–H3, lead, списки, таблицы)
3. FAQ и schema
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок SEO+GEO | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-зона | «Сколько символов…», «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; короткие абзацы |
| Google vs Яндекс | GEO-блок | llms.txt: Google игнорирует; для рунета — осторожно, не hype |
| Schema handoff | Не в body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — дополнение к SEO: цитирование в AI при базе индексируемого контента.
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 на странице; не дублировать.
5. **Какие schema для блога?** — BlogPosting/Article + FAQPage для видимого FAQ; для Google AI Search Schema не обязательна, но rich results — да.
6. **Нужен ли llms.txt блогу?** — для Google Search не влияет; дешёвый опцион для других систем; не замена sitemap/SEO.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель сможет от одного поискового интента дойти до опубликованной SEO-статьи: собрать семантику, собрать outline с answer-first, написать текст «для людей», добавить FAQ и передать schema, встроить GEO-чанки и пройти финальный чеклист перед публикацией.

**action_outline:**

1. **Зафиксировать интент и одну primary-страницу** — один главный запрос, что пользователь должен сделать после прочтения; отсечь запросы с другим intent (отдельные URL).
2. **Собрать семантику** — Вордstat: 15–25 фраз, кластеры LSI; secondary из карточки («seo текст для блога», «geo оптимизация статьи»).
3. **Разобрать TOP-5–10 SERP** — какие H2 закрывают конкуренты, где пробел «читабельность / люди».
4. **Собрать outline** — H1 → H2 → H3; после каждого H2 — тезис-ответ в первом абзаце; lead с прямым ответом в ~100 словах.
5. **Написать черновик** — короткие абзацы, списки/таблицы, без воды и переспама; E-E-A-T lite (автор, факты, ссылки).
6. **Добавить FAQ 5–7** — короткие ответы-действия; подготовить JSON-LD FAQPage (schema-агент).
7. **Оформить мета и медиа** — Title (~60–65 зн.), Description (~155 зн.), alt у изображений, внутренние ссылки (в т.ч. `/`).
8. **GEO-слой** — определения, «острова смысла», при необходимости упомянуть llms.txt без hype; опираться на Google AI guide для формулировок про Schema/llms.txt.
9. **Чеклист перед публикацией** — 15–20 пунктов: семантика, мета, структура, FAQ, schema handoff, перелинковка, proofread.

---

## 8. Риски для writer

- Цифры только из §3 и fact-bank.
- Не копировать структуру Pikapuka/1ps 1:1.
- Объём текста: 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи; без VPN/обходов.
- CTA ≤ 3; не подменять пользу.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента | ✅ |
| Таблица фактов с URL (≥15) | ✅ |
| utility_verdict + action_outline | ✅ |
| GEO hooks + FAQ 5–7 | ✅ |
| Wordstat | ⚠️ MCP недоступен |

**Writer:** готов. Вход: этот файл + `research-context.json` + B01 в `blog-topics.md` + `site-brief.md`.
