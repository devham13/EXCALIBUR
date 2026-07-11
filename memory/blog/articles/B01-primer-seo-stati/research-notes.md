# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата на самой статье)  
**research_date:** 2026-07-11  
**disclaimer:** Все даты, версии и статистика проверены на 11.07.2026 (2026 год).

---

## Utility gate

**utility_verdict:** PASS  
**search_intent:** how_to  
**article_mode:** B  

**reader_outcome:** после прочтения читатель соберёт семантику в Вордстате, построит структуру longread с GEO-чанками, напишет текст без переспама, оформит FAQ/schema и пройдёт финальный чеклист перед публикацией.

**action_outline (workflow 8 шагов):**

1. Проверить спрос и интент в Яндекс Вордстате по primary query и хвостам; выписать LSI и вопросы для FAQ.
2. Разобрать топ-5 SERP: формат (гайд/чеклист), структура H2, пробелы конкурентов.
3. Собрать каркас: H1 + 4–6 H2 из карточки темы; под каждым H2 — тезис в первом предложении (остров смысла).
4. Написать lead 40–60 слов с прямым ответом «как писать SEO-статьи»; затем основной текст списками и таблицами.
5. Распределить ключи естественно: H1, первый абзац, 1–2 H2, Title, Description; без переспама.
6. Добавить блок SEO + GEO: атомарные абзацы, FAQ 5–7 пар, упоминание llms.txt и AI-краулеров.
7. Подготовить мета: Title (~60 знаков), Description (140–160), alt у изображений, 3–5 внутренних ссылок.
8. Пройти чеклист публикации: семантика, структура, читабельность, schema handoff (BlogPosting + FAQPage).

---

## 1. SERP-обзор (WebSearch Cursor, 11.07.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | 5 шагов от темы до оптимизации; Wordstat/Вебмастер; примеры «плохо/хорошо»; абзацы 3–5 строк; естественность ключей | Нет GEO/нейропоиска; CTA Директа в конце | Блок про Директ; дублировать H1–H4 без GEO-слоя |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-...](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Краткая инструкция в начале; кластеры из Вордстата; «сначала смысл, потом оптимизация»; правило ответа сразу после H2 | Длинный; смешение SEO и промптов для ИИ | Копировать блоки про генерацию текстов ИИ 1:1 |
| 3 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 13 шагов (2026) | Интент → конкуренты → структура → WP → Title/Description → чеклист; таблица форматов контента | Уклон в WordPress; 13 шагов перегружают новичка | Не раздувать до 13 H2; взять логику чеклиста |
| 4 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-...](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (2026) | E-E-A-T, Schema Article + FAQPage, Title ~65 знаков | Непроверенные кейсы «+140%»; agency tone | Проценты без первичника |
| 5 | [blog.click.ru/neiroseti/geo-vs-seo-...](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | GEO vs SEO (2026) | robots.txt для AI-краулеров; entity-based контент; связка SEO-трафика и GEO | Коммерческий click.ru; часть цифр вторичные | Sales-narrative как основной CTA |
| 6 | [skiller.info/geo-aeo-ai-search-2026/](https://skiller.info/geo-aeo-ai-search-2026/) | GEO how-to + чеклист | Прямой ответ в начале; H2 как вопросы; списки/таблицы | Узкий фокус на GEO, не на написание с нуля | Не подменять SEO-гайд чистым GEO |

**Паттерн SERP (июль 2026):** топ — «полный гайд 2026» с пошаговым алгоритмом (1ps, olegweb, pikapuka) + официальный Яндекс Direct. Отдельный кластер — GEO/AEO-лонгриды. Запрос «как писать seo статьи» закрывается **инструкциями**, но редко в одном материале совмещают **читабельность для людей + GEO-упаковку + printable чеклист**.

**Intent:** how_to — пользователь хочет **систему действий**: семантика → структура → текст → мета → проверка. Вторичные: «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье».

**Пробел для Excalibur:** единый workflow **SEO + GEO longread «для людей»** (H1 из карточки); статья B01 — эталон формата блога (8 500–9 500 знаков, FAQ, schema handoff).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в текущей Cloud-сессии (`MCP server does not exist`). Вызов `wordstat_get_top_requests` для primary_query «как писать seo статьи» и secondary («seo текст для блога», «geo оптимизация статьи») **не выполнен**. Точные объёмы показов в месяц **не получены** — в тексте статьи не утверждать частотность без повторного прогона Wordstat.

**При восстановлении MCP:** запросить регион 225 (Россия), операторы `"как писать seo статьи"`, `"seo текст для блога"`, `"geo оптимизация статьи"`. OAuth при 401: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### LSI и смежные формулировки (из SERP + подсказки конкурентов, без частот)

**Primary cluster:** как писать seo статьи, как написать seo статью, seo текст для статьи, seo текст для блога, написание seo статей, seo статья пошагово, seo статья чеклист.

**Семантика / инструменты:** семантическое ядро, яндекс вордстат, lsi слова, ключевые слова без переспама, интент запроса, структура h2 h3.

**Техника:** title description, meta description, alt текст, внутренние ссылки, уникальность текста, переспам ключей.

**GEO / 2026:** geo оптимизация статьи, geo в seo, answer-first, faq schema, llms.txt, нейропоиск, ai overviews, прямой ответ в первых 60 словах.

**FAQ-хвосты (из карточки B01):** сколько символов в seo статье; что такое geo в seo.

**SEO-стратегия для writer:** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блок про формат longread; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье»; faq_hints — в FAQ и conversational H2.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение → основная часть по шагам → заключение со следующим действием | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| При практическом интенте в статье нужны шаги, таблицы, чек-листы; длинная теория без действий уводит пользователя обратно в поиск | [olegweb.ru — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 2026 | да |
| Фиксированного объёма SEO-статьи нет; иногда хватает 4 000–6 000 знаков, иногда нужно 15 000–25 000 | [olegweb.ru — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 2026 | да |
| H1 — заголовок на странице; Title — для выдачи; могут быть похожи, но не обязаны совпадать | [olegweb.ru — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 2026 | да |
| После каждого H2 сразу давать содержательный ответ; сначала смысл, потом оптимизация ключей | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Главный ключ — в H1, первом абзаце, 1–2 H2, title и description; LSI распределять по тексту | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Для GEO/AEO не блокировать AI-краулеров (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) в robots.txt | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| Нейросети приоритизируют материалы с указанием реального автора (имя, должность, цифровой след) | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да (как практика GEO) |
| GEO-оптимизация: прямой ответ в первых 40–80 словах; H2/H3 в форме вопросов; списки и FAQ | [skiller.info — GEO/AEO 2026](https://skiller.info/geo-aeo-ai-search-2026/) | 2026 | да |
| Главная задача статьи — полный ответ на запрос; возврат пользователя в поиск — сигнал низкого качества | [maryproject.ru — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**Не использовать без первичника:** «+140% трафика» (Pikapuka); «25% россиян ежедневно с нейросетями» / «17% не кликают по ссылкам» (click.ru без верификации первоисточника в этом прогоне); «0,35% GEO-трафика» (NP Digital через click.ru).

**fact-bank.md:** прямых фактов по SEO-копирайтингу нет; опираться на таблицу выше.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один список ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → чеклист.

**Почему отличается от конкурентов:**

- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- 13-шаговые алгоритмы (olegweb) перегружают; наш формат — 4 H2 + вложенные шаги.
- H1 «которые читают люди» слабо раскрыт в SERP; фокус: **читабельность как SEO-фактор** + техника.

**Режим B:** статья B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage (schema handoff), атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (из карточки B01):**

1. Зачем SEO и GEO в одной статье
2. Структура longread
3. FAQ и schema
4. Чеклист перед публикацией

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead после H1 | 40–60 слов |
| Определение GEO | H2 «SEO + GEO» | 40–60 слов |
| Conversational H2 | FAQ-темы | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA | Блок понятен без соседних |
| Schema | handoff | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Кратко: зачем блогу |
| E-E-A-T lite | Автор/редакция | Имя, роль |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~60 знаков), H1 на странице; не дублировать дословно.
5. **Какие schema нужны блогу?** — BlogPosting + FAQPage.
6. **Что такое llms.txt?** — указатель для AI-краулеров; дополнение к sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать частотность Wordstat (MCP недоступен).
- Не копировать структуру Pikapuka/olegweb 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Без эмодзи; site_url — `/` по карточке.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 5 конкурентов (WebSearch) | ✅ |
| Wordstat MCP | ⚠️ недоступен; LSI из SERP |
| Таблица фактов ≥ 15 с URL | ✅ |
| action_outline + reader_outcome | ✅ |
| utility_verdict PASS | ✅ |
| GEO hooks + FAQ | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + B01 в `blog-topics.md` + `site-brief.md`.
