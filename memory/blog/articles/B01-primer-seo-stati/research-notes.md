# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-10-16  
**disclaimer:** Все даты, версии и статистика проверены на 16.10.2026 (Europe/Moscow).

---

## 1. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** namespace `user-mcp-kv` в среде Cloud Agent недоступен (MCP не подключён). Вызов `wordstat_get_top_requests` для `как писать seo статьи`, `seo текст для блога`, `geo оптимизация статьи` **не выполнен**. Точные показы/мес **не получены** — в тексте статьи не использовать выдуманные цифры спроса.

Обновление токена (если MCP снова включат): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Семантика без объёмов (SERP + подсказки конкурентов, для LSI writer)

| Фраза / кластер | Примечание |
|-----------------|------------|
| как писать seo статьи / как написать seo статью | primary_query, how_to |
| seo текст для блога / seo-текст для сайта | secondary_1 |
| geo оптимизация статьи / seo и geo в одной статье | secondary_2, связка с B04 |
| структура seo статьи, семантическое ядро, вордстат | инструментальный слой |
| title description seo, h1 h2 seo, чек-лист seo статьи | техблок |
| e-e-a-t seo текст, seo копирайтинг 2026 | доверие + свежесть |
| faq schema seo, blogposting json-ld | schema-блок |
| bluf / прямой ответ в начале, нейровыдача | GEO-hooks |

**SEO-стратегия (без Wordstat):** primary в H1/lead; secondary — отдельные H2 или FAQ; «geo оптимизация статьи» — подраздел «SEO + GEO в одном материале», не подменять H1.

---

## 2. SERP-обзор (WebSearch Cursor, 16.10.2026 + сверка с research-serp.json)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|-----------------|------------------|---------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: семантика (Вордстат), H1–H4, абзацы 3–5 строк, alt, title/description, переспам вреден, нет универсального объёма | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа; «SEO-текст = ключи» без human-first |
| 2 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 7 шагов + чек-лист (2026) | Структура до текста; релевантность после черновика; практичный workflow | Мало GEO/schema | Дублировать 7 H2 1:1 |
| 3 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 13 шагов, WordPress (2026) | Интент, SERP-разбор, E-E-A-T, внутренние ссылки | Длинный WP-уклон; GEO вторичен | 13-шаговую структуру без сжатия |
| 4 | [private-seo.ru/blog/kak-pisat-seo-optimizirovannye-teksty-kotorye-nravyatsya-lyudyam](https://private-seo.ru/blog/kak-pisat-seo-optimizirovannye-teksty-kotorye-nravyatsya-lyudyam) | 6 шагов (обнов. 28.09.2026) | «Порядок: спрос → выдача → структура → слова»; операторы Вордстата | Мало FAQ/schema | — |
| 5 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread + ИИ (2026) | BLUF после H2; LSI; ИИ как черновик | Перегруз pro-ИИ без human-in-the-loop | «100% ИИ без редактуры» |
| 6 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист 2026 (04.06.2026) | E-E-A-T, AI Overviews, Алиса AI, 9 критериев качества | Agency tone | 9 критериев списком без своего угла |
| 7 | [articleai.ru/.../kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Пошаговая инструкция (SERP) | Семантика → публикация | Продуктовый bias | — |
| 8 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Чек-лист + schema (2026) | FAQPage, Title ~65 знаков, E-E-A-T | Непроверенные кейсы (+140% и т.п.) | Кейсовые проценты без URL |
| 9 | [searchengineland.com/guide/how-to-write-for-seo](https://searchengineland.com/guide/how-to-write-for-seo) | EN reference 2026 | Extractability, snippet-first, семантические заголовки | EN, не RU-специфика Яндекса | Копировать EN формулировки дословно |
| 10 | [yoast.com/seo-friendly-blog-post](https://yoast.com/seo-friendly-blog-post/) | Blog SEO + AI visibility | Meta title 55–60 символов; answer-first; intent | Плагин Yoast как CTA | — |

**Паттерн SERP (окт. 2026):** доминируют «полный гайд 2026» (7–13 шагов), чек-листы, связка SEO + ИИ. H1 «которые **читают люди**» слабо закрыт — конкуренты говорят «для людей и роботов», но редко делают **читабельность** (инфостиль, island test, BLUF) центральной осью + **единый workflow SEO+GEO** в одной статье-эталоне.

**Intent:** `how_to` — собрать семантику → разобрать SERP → структура → черновик → мета → GEO-слой (FAQ/schema) → чек-лист перед публикацией.  
**Пробел Excalibur:** одна статья = **инструкция + живой образец** (режим B): longread 8,5–9,5k знаков с FAQ, JSON-LD, перелинковкой на B04.

---

## 3. Таблица фактов (цифры только с URL; fact-bank — при совпадении)

| Факт | Источник | Дата | В текст |
|------|----------|------|---------|
| Универсального объёма SEO-статьи нет — зависит от темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир **3–5 строк**; списки для перечислений | [Яндекс Директ](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| **H1** один; **H2–H4** для смысловых блоков | [Яндекс Директ](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают **смысл**, не плотность ключей; переспам вреден | [Яндекс Директ](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику смотрят в **Яндекс Вордстат** и **Яндекс Вебмастер** | [Яндекс Директ](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| **Title** и **Description** влияют на сниппет и клик | [Яндекс Директ](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| К изображениям — **alt**; файлы латиницей | [Яндекс Директ](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| В 2026 контент должен быть полезен **классической выдаче, AI Overviews, Алисе AI, ChatGPT, Perplexity** | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Подсчёт ключей и «уникальность 99%» сами по себе **не работают** | [Texterra](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Meta title — ориентир **~55–60 символов**, ключ ближе к началу | [Yoast — SEO-friendly blog post](https://yoast.com/seo-friendly-blog-post/) | 2026 | да |
| SEO-friendly пост 2026: **answer-first**, цитируемые предложения для AI | [Yoast](https://yoast.com/seo-friendly-blog-post/) | 2026 | да |
| Контент для сниппетов/LLM: **front-load** ответ, короткие абзацы, семантические H2/H3 | [Search Engine Land — How to write for SEO 2026](https://searchengineland.com/guide/how-to-write-for-seo) | 2026 | да |
| Google **прекратил показ FAQ-аккордеона** в выдаче с **7 мая 2026**; блок FAQ на странице и разметка для **Яндекса/GEO** остаются уместны | [SEO-акademiya.by — микроразметка статей](https://seo-akademiya.by/blog/kontent/mikrorazmetka-dlya-statey/) | 2026 | да |
| JSON-LD **FAQPage**: текст в разметке **дословно** совпадает с видимым FAQ | [smart-d-m.ru — FAQPage для GEO](https://smart-d-m.ru/schema-org-faqpage-dlya-geo.html) | 2026 | да |
| Минимум schema для блога: **Article/BlogPosting + FAQPage + Organization** | [citerank.ru — Schema.org для GEO](https://citerank.ru/blog/schema-org-for-geo) | 2026 | да |
| **51%** маркетологов используют нейросети для **аналитики и оптимизации**, а не для слепой штамповки | [mayai.ru — fact-bank → SurveyMonkey](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026-06-11 | да |
| Автономные ИИ завершают **&lt;2,5%** сложных неструктурированных задач без человека — **human-in-the-loop** норма | [mayai.ru — fact-bank](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026-06-11 | да |
| Если пользователь **возвращается в поиск** после страницы — сигнал низкого качества ответа | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**Не использовать без первичника:** «плотность ключей 1–2%» (Seotika); «+140% трафика за 3 недели» (Pikapuka); «1–10 млн доменов FAQPage» без cross-check; любые **показы Wordstat** — MCP недоступен.

**fact-bank.md:** прямых строк про SEO-копирайтинг нет; допустимы только строки таблицы выше + fact-bank (SurveyMonkey, human-in-the-loop).

---

## 4. Угол и дифференциация (utility-only)

**Главный угол:** SEO-статья 2026 = **longread для человека**, упакованный для **поиска и нейровыдачи** в **одном проходе** (не «SEO сначала, GEO потом»). Фокус H1: **«которые читают люди»** — короткие абзацы, BLUF, island test, без воды; техника (мета, schema, FAQ) — как **финальный слой**, а не замена смысла.

**Отличие от SERP:**
- Яндекс Direct — канон без GEO и без «эталон-статьи».
- 7–13 шагов у конкурентов — encyclopedia; у нас **8 шагов action_outline** + **чек-лист 15–20 пунктов** в теле.
- ИИ-гайды — без акцента на редактуре; у нас **ИИ = черновик**, финал — человек (fact-bank 2,5% / 51%).

**Режим B:** сама B01 — образец: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage (meta, не в body HTML writer), internal `/`, линк на B04 при упоминании GEO сайта.

**H2-каркас (карточка + research):**
1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: H1–H3, lead, BLUF, списки/таблицы
3. FAQ и schema — зачем и как (видимый FAQ + JSON-LD)
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слov | H2 «SEO + GEO» | Generative Engine Optimization |
| BLUF | Каждый H2 | 1-е предложение = ответ |
| FAQ 5–7 | Конец | 2–4 предложения, ≤80 слов |
| Conversational H2/FAQ | faq_hints | «Сколько символов…», «Что такое GEO в SEO?» |
| Schema handoff | QA/schema agent | BlogPosting + FAQPage |
| Island test | Writer QA | H2 понятен отдельно |
| llms.txt | Одна фраза | опционально, не вместо sitemap |

**Целевые формулировки:** как писать seo статьи; seo текст для блога; geo оптимизация статьи.

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); ориентир — полнота vs SERP; для B01 longread — **8 500–9 500** знаков текста.
2. **Что такое GEO в SEO?** — дополнение: оптимизация под цитирование в AI-ответах при той же индексируемой базе.
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (~55–60 символов), H1 на странице; не дублировать дословно.
5. **Какие schema нужны блогу?** — BlogPosting/Article + FAQPage при видимом FAQ.
6. **Можно ли отдать текст нейросети без правок?** — риск ошибок; human-in-the-loop; ИИ — черновик/структура.
7. **Как проверить статью перед публикацией?** — чек-лист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать **Wordstat** и любые «N показов/мес».
- Не копировать Pikapuka/olegweb **структуру 1:1**.
- Объём **8 500–9 500** знаков (`quality-blog.md`).
- Без эмодзi в article.html; CTA ≤ 3.
- Цифры только из §3 или fact-bank.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику под один запрос, разберёт топ выдачи, составит структуру H1–H3 с BLUF, напишет черновик без переспама, оформит Title/Description и alt, добавит FAQ и подготовит данные для BlogPosting/FAQPage, пройдёт чек-лист перед публикацией и поймёт, какие 3–5 правок усилят статью под нейровыдачу.

**action_outline (для writer, 8 шагов):**

1. **Спрос:** зафиксировать primary + 5–10 LSI (Вордстат/Вебмастер или ручной SERP); сгруппировать по intent (инфо/коммерция).
2. **SERP:** открыть топ-5–10; выписать формат (гайд/чек-лист/сравнение), среднюю глубину, пробелы (FAQ, таблицы, даты).
3. **Структура:** H1 = h1 карточки; H2 по `h2_outline`; под каждым H2 — тезис BLUF + 3–5 буллетов содержания.
4. **Черновик:** lead с прямым ответом; абзацы 3–5 строк; списки/таблица; E-E-A-T lite (опыт, пример, источник).
5. **Ключи:** главный ключ в H1, первом абзаце, 1–2 H2, title; LSI по тексту; без переспама (Яндекс Direct).
6. **Мета и медиа:** Title ~55–60 символов, description с пользой; alt у изображений; H1 ≠ Title.
7. **GEO-слой:** FAQ 5–7 (ответы-действия); каждый H2 как «остров смысла»; перелинковка `/`, при GEO — отсылка к B04.
8. **Pre-publish:** чек-лист 15–20 пунктов (семантика, интент закрыт, FAQ, schema handoff, ссылки, орфография, mobile); план обновления `dateModified`.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы (B01) | PASS |
| SERP ≥ 3 конкурента | ✅ (10) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (18) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks + режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + `memory/topics/blog-topics.md` (B01) + `memory/brief/site-brief.md`.
