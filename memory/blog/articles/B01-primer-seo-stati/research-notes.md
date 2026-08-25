# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + чеклист перед публикацией)  
**research_date:** 2026-08-25  
**disclaimer:** Все даты, версии и статистика проверены на 25.08.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch, 25.08.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: 5 шагов (тема → семантика → структура → текст → оптимизация); таблицы «плохо/хорошо»; Wordstat + Вебмастер; естественность ключей | Мало GEO/нейропоиска; CTA на Директ | Коммерческий блок Директа; «что такое SEO-текст» без чеклиста публикации |
| 2 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист 2026 (04.06.2026) | 9 критериев: E-E-A-T/ЭПОС, интент, ключи, структура, AI-выдача, мета, уникальность, перелинковка; answer-first | Agency CTA «обновим ваши статьи»; нет единого numbered workflow | Копировать 9 H2 1:1 |
| 3 | [fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | Агентский гайд (26.06.2026) | Плотность информации > длины; атомарные блоки; E-E-A-T → Experience; pillar/cluster; чек-лист перед публикацией; позиция про ИИ | Длинный sales-narrative; кейсы без первичников | Таблицу «ИИ vs эксперт» без адаптации; agency tone |
| 4 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Longread + чек-лист (май 2026) | Семантика, LSI, Serpstat; Title ~65 знаков; Schema Article + FAQPage; Featured Snippet | «+140% трафика за 3 недели» без источника | Непроверенные проценты; 7-разделная структура 1:1 |
| 5 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | FAQ, таблицы, экспертный контент под AI-выдачу | Перегруз про ИИ-генерацию | Шаблон «полный гайд с ИИ» без human-in-the-loop |
| 6 | [inkocoin.ru/kak-sozdavat-ii-kontent-kotoryi-ranzhiruetsya/](https://inkocoin.ru/kak-sozdavat-ii-kontent-kotoryi-ranzhiruetsya/) | How-to + fact-check | 3 шага проверки фактов; island-test логика; FAQ/перелинковка | Узкий фокус на ИИ-контент, не универсальный SEO-writing | Копировать блок про ИИ-детекторы как обязательный шаг |
| 7 | [iq-maxima.ru/blog-iq/seo-statya-v-2026-godu-kak-pisat-pod-poisk-i-neyrovydaychu/](https://iq-maxima.ru/blog-iq/seo-statya-v-2026-godu-kak-pisat-pod-poisk-i-neyrovydaychu/) | SEO + нейровыдача | Явная связка классического SEO и нейроответов | Мало пошаговой семантики «с нуля» | Agency positioning |
| 8 | [hubes.ru/blog/kak-napisat-seo-optimizirovannuyu-statyu](https://hubes.ru/blog/kak-napisat-seo-optimizirovannuyu-statyu) | Практический workflow | «Плотность информации важнее длины»; ИИ как черновик | Поверхностный чеклист | Generic советы без чеклиста 15+ пунктов |

**Паттерн SERP 08.2026:** доминируют «гайд/чек-лист 2026» с E-E-A-T (или ЭПОС), answer-first, FAQ и блоком про AI-выдачу. Запрос «как писать seo статьи» закрывают longread’ы агентств; **H1 «которые читают люди»** в топе почти не встречается — пробел для дифференциации через **читабельность + единый workflow SEO→GEO**.

**Intent:** `how_to` — пользователь хочет **пошаговую систему**: семантика → outline → текст → мета → schema → проверка. Вторичный intent: связать SEO-статью с GEO (цитирование в AI) без отдельного «энциклопедического» GEO-лонгрида.

**Пробел для Excalibur:** один **action-first workflow** (8–9 шагов) + **чеклист 15–20 пунктов** «перед публикацией», где сама статья B01 — эталон режима B (longread для людей + упаковка под нейропоиск).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` / инструмент `wordstat_get_top_requests` **недоступен** в текущем Cloud Agent run (`MCP server does not exist: user-mcp-kv`). Точные показы/мес **не получены** — цифры спроса в таблицу ниже **не включены** (не выдумывать).

**Действие для пайплайна:** подключить MCP и обновить токен через:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Запросы для повторного прогона Wordstat (region 225):**

| query_id | Фраза | Назначение |
|----------|-------|------------|
| primary | как писать seo статьи | primary_query карточки B01 |
| secondary_1 | seo текст для блога | вторичный intent |
| secondary_2 | geo оптimizaciya статьи | GEO-слой в longread |
| lsi_1 | как написать seo статью | wordform variant |
| lsi_2 | seo текст для сайта | commercial/info mix |
| lsi_3 | структура seo статьи | outline intent |
| lsi_4 | чек-лист seo текста | checklist intent |
| faq_1 | сколько символов в seo статье | faq_hints карточки |

### LSI для writer (из SERP + secondary_queries, без частотности)

- как написать seo статью / seo текст для блога / seo копирайтинг  
- структура seo статьи, семантическое ядро, яндекс вордstat  
- title description h1, перелинковка, alt-тексты  
- e-e-a-t, экспертность, ЭПОС (релевантность Яндекса)  
- чек-лист перед публикацией, answer-first, faq блок  
- geo оптимизация статьи, нейровыдача, AI Overviews, Поиск с Алисой AI  
- schema.org BlogPosting, FAQPage, featured snippet  

**SEO-стратегия (до получения Wordstat):** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блок про формат longread; «geo оптимизация статьи» — отдельный подблок внутри H2 «SEO + GEO в одной статье»; faq_hints — в FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| # | Факт | Источник | Дата | Можно в текст |
|---|------|----------|------|---------------|
| 1 | Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 2 | Абзацы — ориентир **3–5 строк**; перечисления — списками | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 3 | **H1 — один** на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 4 | Поисковики оценивают **смысл и полезность**, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 5 | Семантику собирают в **Яндекс Вордстат** и **Яндекс Вебмастер** | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 6 | **Title** и **Description** влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 7 | Базовый workflow: тема → семантика → структура → текст → оптимизация (**5 шагов**) | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 8 | В 2026 контент оценивают и классическая выдача, и **AI Overviews / Алиса AI / ChatGPT / Perplexity** | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| 9 | Google: **E-E-A-T** + people-first; Яндекс: **ЭПОС** (экспертность, полезность, оригинальность, содержательность) | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| 10 | Принцип 2026: **от главного ответа к деталям** — сначала суть, потом нюансы | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| 11 | Для цитирования в ChatGPT **не блокировать OAI-SearchBot** (отличать от GPTBot) | [Texterra — чек-лист SEO 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| 12 | **Плотность информации важнее длины**; прямой ответ — в начале, без «воды» | [FireSEO — SEO-текст 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| 13 | Для AI-выдачи нужны **атомарные, самодостаточные** блоки (чёткие H2, FAQ, без прятания смысла во вкладках) | [FireSEO — SEO-текст 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| 14 | E-E-A-T в 2026 смещён на **Experience (опыт)** — кейсы, «мы проверили», авторские скриншоты | [FireSEO — SEO-текст 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| 15 | Работает **кластер**: pillar longread + 5–10 узких статей с перелинковкой | [FireSEO — SEO-текст 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| 16 | Google/Яндекс **не запрещают ИИ** как таковой; санкции — за **scaled content abuse** без ценности | [FireSEO — SEO-текст 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 26.06.2026 | да |
| 17 | Title — ориентир **~65 знаков**, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| 18 | **H1 ≠ Title** — разные роли (сниппет vs заголовок на странице) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| 19 | **Schema.org: Article/BlogPosting + FAQPage** — для сниппета и структуры | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| 20 | Фактчекинг: **первоисточник → 2–3 независимых источника → ручная проверка цифр** | [Inkocoin — ИИ-контент и SEO](https://inkocoin.ru/kak-sozdavat-ii-kontent-kotoryi-ranzhiruetsya/) | 2026 | да |

**fact-bank.md:** прямых фактов по SEO-writing нет — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (Pikapuka); выдуманные частотности Wordstat; проценты AI-детекторов из Дзена без первичника.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **longread, который читают люди**, и который **можно процитировать** в нейропоиске. Не «ещё один список ключей», а **единый workflow A→I**: интент → Wordstat/SERP → outline → answer-first текст → мета → FAQ/schema → GEO-чанки → чеклист перед публикацией.

**Почему отличается от конкурентов:**

- Яндекс Direct — канон без GEO и без printable checklist.
- Texterra/FireSEO — сильные чек-листы, но размытый фокус «для людей» в H1.
- GEO-лонгриды (B04-кластер) не учат писать текст с нуля.
- H1 карточки B01 («**которые читают люди**») слабо представлен в SERP.

**Режим B:** сама статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead 40–60 слов с определением.

**H2-каркас (из `blog-topics.md` + research):**

1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: lead, H1–H3, списки, таблицы, «острова смысла»
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

**Подтемы внутри блоков:** Wordstat/семантика, Title/Description, E-E-A-T lite, перелинковка на `/`, llms.txt (упоминание, не замена sitemap).

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2/H3 | По faq_hints | «Сколько символов…», «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец longread | Ответ 2–4 предложения, action-first |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; абзац 3–4 предложения |
| Island test | QA | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Даты | meta/schema | datePublished / dateModified = дата прогона |
| Internal link | Из карточки | На `/` |
| Alt обложки | cover_scene_hint | «Редактор за ноутбуком…» |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при сохранении индексируемой структуры.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI/тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — на странице; не дублировать.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Как собрать семантику перед написанием?** — primary + 5–10 LSI в Wordstat; H2 из вопросов пользователей и пробелов SERP.
7. **Как проверить статью перед публикацией?** — чеклист: интент, мета, структура, факты, FAQ, schema, ссылки, читабельность.

---

## 7. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель сможет **от primary query в Wordstat до опубликованной SEO-статьи**: собрать семантику и outline по SERP, написать answer-first longread с FAQ и мета-тегами, добавить schema, упаковать блоки под GEO и пройти финальный чеклист перед публикацией.

**action_outline (how-to, 9 шагов):**

1. **Зафиксировать интент:** кто ищет «как писать seo статьи», какой формат ждёт (how-to), что сделает после прочтения.  
2. **Собрать семантику:** primary + 5–10 LSI в Wordstat/Вебмастер; выписать вопросы для FAQ из «Похожих запросов» и SERP.  
3. **Разобрать топ-5–10 SERP:** H2 конкурентов, объём, таблицы/FAQ; отметить **пробел** (что не закрыто — «читаемость + единый SEO+GEO workflow»).  
4. **Согласовать outline:** 4 H2 из карточки + подзаголовки H3; каждый H2 = подзадача + «делать / не делать».  
5. **Написать lead и черновик:** определение в 40–60 слов; далее блоки «тезис → ответ → рекомендация»; абзацы 3–5 строк.  
6. **Встроить SEO-технику:** Title (~65 зн.), Description, H1 ≠ Title; ключи естественно; 2–4 внутренние ссылки; alt по смыслу.  
7. **Добавить FAQ 5–7** и таблицу/список там, где ускоряет сканирование; проверить факты по таблице §3.  
8. **GEO-слой:** атомарные H2, answer-first; упомянуть llms.txt/AI-ботов в robots только как справку (без блокера B04).  
9. **Финальный чеклист 15–20 пунктов** → правки → handoff schema/cover; не публиковать без прохождения island-test.

---

## 8. Риски и blockers для writer

- Не выдумывать частотность Wordstat — MCP не ответил; в тексте ссылаться на [wordstat.yandex.ru](https://wordstat.yandex.ru/) без цифр спроса.
- Не копировать структуру Pikapuka/Texterra 1:1.
- Объём текста: **8 500–9 500** знаков (`quality-blog.md`).
- Min **5** нумерованных шагов в теле **или** чеклист **10+** пунктов (здесь — оба: workflow + чеклист).
- Без эмодзи в `article.html`; CTA ≤ 3.
- `internal_links` из карточки: `/`.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (LSI из SERP) |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| Режим B описан | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
