# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата)  
**research_date:** 2026-07-10  
**disclaimer:** Все даты, версии и статистика проверены на 10.07.2026.

---

## Utility gate

| Поле | Значение |
|------|----------|
| `utility_verdict` | **PASS** |
| `search_intent` | how_to |
| `article_mode` | B |
| Gate 0 (topic) | PASS (`excalibur_blog_utility_gate.py --topic-id B01`) |

**reader_outcome:** Читатель сможет самостоятельно написать и подготовить к публикации SEO+GEO longread для блога: собрать семантику, собрать структуру H1–H3, написать читаемый текст с FAQ/schema и пройти финальный чеклист перед выкладкой.

**action_outline (workflow для writer):**

1. Проверить спрос и интент по `primary_query` в Яндекс Вордстат и Вебмастере; зафиксировать 5–10 LSI-фраз.
2. Разобрать ТОП-5 конкурентов в SERP: структура, глубина, пробелы (особенно GEO-слой и читабельность).
3. Собрать каркас: H1, 4 H2 из карточки B01, H3 под вторичные запросы, 5–7 FAQ.
4. Написать lead (40–60 слов) с прямым ответом на запрос; каждый H2 — атомарный «остров смысла».
5. Наполнить блоки: короткие абзацы, списки, таблица SEO vs GEO, факты только из таблицы ниже.
6. Заполнить Title (~65 знаков), Description, alt изображений; H1 не дублирует Title.
7. Подготовить handoff для schema: BlogPosting + FAQPage (JSON-LD, не в body).
8. Пройти чеклист публикации (15+ пунктов) перед выкладкой.

---

## 1. SERP-обзор (WebSearch, 10.07.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый how-to (обновлён 05.02.2026) | 13 шагов от темы до индексации; Wordstat; таблица «конкурент vs вы»; чек-лист; WordPress-практика | GEO/AEO как отдельный слой слаб; длинный sales-хвост Telegram/хостинг | Структуру 13 шагов 1:1; рекламные блоки Timeweb/Paradigma |
| 2 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Канон: H1–H4, абзацы 3–5 строк, Wordstat, Title/Description, естественность ключей | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа; копировать без GEO-слоя |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (май 2026) | Семантика, E-E-A-T, чек-лист 10 шагов, Schema Article+FAQPage, Title ~65 знаков | Кейсы с непроверенными %; GEO как побочный эффект | «+140% трафика» и agency-CTA без источника |
| 4 | [habr.com/ru/articles/1030292](https://habr.com/ru/articles/1030292/) | GEO/AEO полевое руководство (2026) | RAG-механика, chunking, 7 техник GEO, FAQ; Princeton GEO study | Не учит писать SEO-статью с нуля; часть цифр без первичника | Копировать «20–40% органики» без первичника; рекламу GPTunnel |
| 5 | [seo-performance.ru/article/kak-prodvigat-site-ai-otvet](https://seo-performance.ru/article/kak-prodvigat-site-ai-otvet/) | AEO/AI-ответы (2026) | Schema Article+FAQPage+HowTo+Table; H2-вопросы; короткий ответ в начале блока | Фокус на доработке старых статей, не на создании с нуля | Sales-narrative агентства |
| 6 | [adpass.ru/kak-napisat-seo-tekst](https://adpass.ru/kak-napisat-seo-tekst/) | Гайд по структуре блога | Содержание с якорями; 6–8K ЗБП для блога; H2/H3-иерархия | Мало GEO; устаревшие акценты на «тошноту» | Копировать объёмные требования без контекста темы |
| 7 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samomostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | ИИ в workflow; актуальный год в title | Перегруз ИИ-инструментами; слабая GEO-структура | Список нейросетей без actionable шагов |

**Паттерн SERP:** топ — «полный гайд 2026» с E-E-A-T, Wordstat, чек-листом (olegweb, pikapuka, 1ps). Отдельный кластер — GEO/AEO-лонгриды (Habr, seo-performance). Прямого совпадения с H1 «которые читают люди» в топе почти нет.

**Intent:** how_to — пользователь хочет пошаговую систему: семантика → структура → текст → техника → проверка. Вторичный intent: связка SEO + GEO в одном материале.

**Пробел для Excalibur B01:** единый workflow «для людей» + GEO-чанки в одном гайде; читабельность как SEO-фактор; режим B — сама статья как эталон (8 500–9 500 знаков, FAQ, schema).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

> **⚠️ WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` не подключён в Cloud Agent environment (10.07.2026). Вызов `wordstat_get_top_requests` для `как писать seo статьи` недоступен. Точные объёмы показов **не получены** — цифры ниже не указаны намеренно.
>
> Для восстановления: подключите MCP `user-mcp-kv` в `.cursor/mcp.json` или обновите OAuth-токен Wordstat: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (без показов — до подключения API)

| Кластер | Фразы для проверки в Wordstat | Роль в статье |
|---------|------------------------------|---------------|
| Primary | как писать seo статьи, как написать seo статью, как писать seo тексты | H1, lead, Title |
| Блог | seo текст для блога, seo статья для блога, структура статьи для блога | H2 «структура longread» |
| GEO/AEO | geo оптимизация статьи, что такое geo в seo, оптимизация под нейропоиск | H2 «SEO + GEO» |
| Техника | seo title description, schema faqpage, чеклист seo статьи | H2 «FAQ и schema», чеклист |
| Long-tail | сколько символов в seo статье, как писать seo статьи 2026, e-e-a-t seo текст | FAQ |

### LSI для writer (из SERP + secondary_queries)

- как писать seo статьи, seo текст для блога, geo оптимизация статьи  
- структура seo статьи, h1 h2 h3, lead-абзац, интент запроса  
- яндекс вордстат семантика, title description, перелинковка  
- e-e-a-t, читабельность, абзацы 3–5 строк, списки таблицы  
- faqpage blogposting schema, llms.txt, ai-ответы нейропоиск  
- чеклист перед публикацией, сколько символов в seo статье  

**SEO-стратегия (после Wordstat):** primary «как писать seo статьи» в H1/lead; secondary «seo текст для блога», «geo оптимизация статьи» — в H2 и FAQ; long-tail — в H3 и ответы FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| H1 — один на страницу; H2–H4 структурируют смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья 2026 — страница, закрывающая задачу пользователя, а не «текст под ключи» | [olegweb — как написать SEO-статью](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Алгоритм olegweb: 13 шагов от темы/Wordstat до индексации и чек-листа | [olegweb — как написать SEO-статью](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Для блога оптимальный объём — ориентир 6–8K ЗБП (знаков без пробелов) | [ADPASS — SEO-текст](https://adpass.ru/kak-napisat-seo-tekst/) | 2026 | да |
| Один подзаголовок H2/H3 на 1,5–2 тыс. ЗБП — ориентир читабельности | [ADPASS — SEO-текст](https://adpass.ru/kak-napisat-seo-tekst/) | 2026 | да |
| GEO — оптимизация под цитирование в LLM-поиске (ChatGPT Search, Perplexity, Google AI Overviews); не замена SEO | [Habr — GEO/AEO](https://habr.com/ru/articles/1030292/) | 2026 | да |
| RAG-системы извлекают фрагменты (chunks), не страницы целиком — каждый абзац конкурирует отдельно | [Habr — GEO/AEO](https://habr.com/ru/articles/1030292/) | 2026 | да |
| Структура «инвертированной пирамиды» (ответ → объяснение → детали) лучше для извлечения в RAG | [Habr — GEO/AEO](https://habr.com/ru/articles/1030292/) | 2026 | да |
| Schema.org: Article + FAQPage + HowTo + Table — комбинируются в одной статье | [SEO Performance — AI-ответы](https://seo-performance.ru/article/kak-prodvigat-site-ai-otvet/) | 2026 | да |
| H2-формулировки вопросами («что», «зачем», «как») + короткий ответ в первых 40–60 словах блока | [SEO Performance — AI-ответы](https://seo-performance.ru/article/kak-prodvigat-site-ai-otvet/) | 2026 | да |
| Princeton GEO study (2023) — первая академическая систематизация Generative Engine Optimization | [Habr — GEO/AEO](https://habr.com/ru/articles/1030292/) | 2026 | да |
| AI optimization: visibility измеряется citations в сгенерированных ответах, не только кликами | [Adobe — SEO in 2026](https://business.adobe.com/blog/seo-in-2026-fundamentals) | 2026 | да |
| Extractability: чёткая семантическая структура, self-contained факты, schema markup | [Adobe — SEO in 2026](https://business.adobe.com/blog/seo-in-2026-fundamentals) | 2026 | да |

**Не использовать в тексте (нет первичника / непроверено):** «+140% трафика за 3 недели» (Pikapuka); «сайты теряют 20–40% органики» (Habr TL;DR без первичника в тексте); «GEO +30–40% видимости» (Digital Applied без arxiv в body); «40% пользователей на ИИ-поиске» (Dzen без первичника).

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- olegweb/pikapuka перегружены шагами и agency-экспертизой.
- H1 «которые читают люди» слабо раскрыт в SERP — наш фокус: **читабельность как SEO-фактор** (структура, инфостиль, «острова смысла») + техника.

**Режим B:** статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (из карточки B01):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (для writer и schema)

| Hook | Где в статье | Формат |
|------|--------------|--------|
| Определение SEO-статьи | Первый абзац после H1 | 40–60 слов |
| Определение GEO | Блок «SEO + GEO» | 40–60 слов |
| Conversational H2 | «Что такое GEO в SEO?», «Сколько символов нужно в SEO-статье?» | Вопрос в заголовке |
| FAQ 5–7 пар | Конец longread | 2–4 предложения на ответ |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Что это и зачем блогу |
| Внутренняя ссылка | Из карточки | На `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; для how-to longread в Excalibur — 8 500–9 500 знаков текста.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключевые слова в 2026 году?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt и нужен ли он блогу?** — подсказка для AI-краулеров; не замена sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски и blockers для writer

- Не выдумывать статистику Wordstat — ждать MCP или писать без цифр спроса.
- Не копировать структуру Pikapuka/olegweb 1:1.
- Объём: 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи, без VPN/обход блокировок.
- Цифры только из таблицы фактов §3.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 5 конкурентов (WebSearch 10.07.2026) | ✅ |
| Wordstat (попытка MCP + WARNING) | ⚠️ MCP недоступен |
| Таблица фактов с URL (17 фактов) | ✅ |
| utility_verdict: PASS | ✅ |
| reader_outcome + action_outline | ✅ |
| GEO hooks + FAQ 5–7 | ✅ |
| Режим B + H2 outline | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
