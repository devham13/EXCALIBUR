# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата)  
**research_date:** 2026-08-06  
**disclaimer:** Все даты, версии и статистика проверены на 06.08.2026.

---

## 1. SERP-обзор (WebSearch, август 2026 — 7 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 13 шагов (2026) | Полный workflow: спрос → интент → SERP → структура → ключи → intro → E-E-A-T → WordPress → мета → перелинковка → QA | Много шагов «размазано»; GEO/нейропоиск — побочно; привязка к WP | Копировать 13 H2 1:1; непроверенные кейсы трафика |
| 2 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист 9 критериев (июн 2026) | E-E-A-T + ЭПОС; интент; «ответ сначала, детали потом»; блок AI-выдачи; robots.txt для OAI-SearchBot | Нет пошагового «с нуля» для новичка; agency tone | Коммерческий CTA агентства |
| 3 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: семантика, структура H1–H4, естественность ключей, Wordstat, alt, мета | Нет GEO-слоя; промо Директа в конце | Блок про Директ; «что такое SEO» без actionable depth |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread + ИИ (2026) | Смысл → оптимизация; LSI; примеры; FAQ | Перегруз про ИИ-генерацию; длинный sales-narrative | Копировать структуру 1:1; «уникальность 99%» как KPI |
| 5 | [tolk.digital/kak-pisat-seo-teksty-v-2026-godu](https://tolk.digital/kak-pisat-seo-teksty-v-2026-godu-formula-kotoraya-rabotaet/) | Формула 2026 | Lead = ответ; H1 + первый абзац с ключом; форматы под интент (FAQ, гайд, сравнение) | Мало техники schema/GEO | Agency CTA |
| 6 | [hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | How-to 7 шагов | «Текст помогает решить задачу»; FAQ для сниппета; workflow 7 пунктов | Поверхностный GEO; generic SEO | Thin checklist без примеров |
| 7 | [searchengineland.com/what-is-generative-engine-optimization-geo-444418](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) | GEO framework (EN, 2026) | SEO vs GEO; self-contained paragraphs; entity clarity; метрики цитирования | Фокус на brand GEO, не на процесс написания статьи | Копировать EN-структуру без адаптации под RU-блог |

**Паттерн SERP (август 2026):** топ — «гайд/чек-лист SEO-текста 2026» с E-E-A-T, Wordstat, структурой H2–H3. Отдельный кластер — GEO-лонгриды. Прямого попадания в H1 «которые **читают люди**» мало: конкуренты говорят про «люди и роботы», но не связывают **читабельность** с **GEO-чанками** в одном workflow.

**Intent:** `how_to` — пользователь хочет **пошаговую систему** от семантики до публикации. Вторичный intent: понять, как в одной статье совместить SEO и GEO (нейроответы).

**Пробел для Excalibur:** единый **action-first workflow** «для людей + для AI-выдачи»: интент → longread-структура → атомарные H2 → FAQ/schema → финальный чек-лист 15–20 пунктов. Статья B01 — **эталон** формата блога (режим B).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в текущей Cloud-сессии (MCP не подключён). Вызов `wordstat_get_top_requests` для «как писать seo статьи» **не выполнен**. Точные объёмы спроса **не получены** — в тексте статьи цифры показов не использовать.

**Действие для пайплайна:** подключите MCP `user-mcp-kv` в Cursor IDE и обновите OAuth-токен Wordstat:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса

| Фраза | Показы/мес |
|-------|------------|
| *данные не получены — MCP недоступен* | — |

### LSI для writer (из SERP + secondary_queries, без объёмов)

**Primary cluster:** как писать seo статьи, как написать seo статью, seo текст для блога, seo текст для сайта, seo статья 2026, seo копирайтинг

**Семантика и структура:** семантическое ядро, lsi слова, поисковый интент, структура статьи h1 h2, title description, meta description, перелинковка, alt текст

**Качество и доверие:** e-e-a-t, экспертность автора, полезный контент, переспам ключей, уникальность текста, чек-лист перед публикацией

**GEO / AI-выдача:** geo оптимизация статьи, generative engine optimization, нейроответ, ai overviews, алиса ai, faq schema, llms.txt, answer-first, атомарные блоки

**FAQ-intent (из карточки B01):** сколько символов в seo статье, что такое geo в seo

**SEO-стратегия (без Wordstat-цифр):** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блок про формат блога; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье»; FAQ закрывает faq_hints.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — он зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Google **не** имеет предпочтительного word count для ранжирования | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| Контент должен быть people-first: после прочтения человек достигает цели, а не ищет снова | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness); trust — ключевой | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| SEO при people-first контенте — помощь discovery, не search-engine-first | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | актуально 2026 | да |
| Яндекс ЭПОС: экспертность, полезность, оригинальность, содержательность | [Texterra — чек-лист SEO-текста 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Базовый принцип 2026: сначала главный ответ, потом детали и нюансы | [Texterra — чек-лист SEO-текста 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Страница для AI-выдачи: короткий прямой ответ в начале; H2/H3 понятны без контекста; факты с источниками | [Texterra — чек-лист SEO-текста 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Для ChatGPT-поиска не блокировать OAI-SearchBot в robots.txt (отличать от GPTBot) | [Texterra — чек-лист SEO-текста 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Alt описывает содержимое картинки, а не дублирует ключи | [Texterra — чек-лист SEO-текста 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Алгоритм написания: спрос → интент → SERP → структура → ключи → intro → E-E-A-T → мета → перелинковка → QA | [OlegWeb — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 2026 | да |
| Главный ключ — в H1, первом абзаце, 1–2 H2, title и description (естественно) | [1PS — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| GEO (Generative Engine Optimization) — практика позиционирования контента для цитирования в AI-ответах; не замена SEO | [Search Engine Land — GEO](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) | 2026 | да |
| GEO-контент: self-contained paragraphs — один абзац = одна извлекаемая идея | [Search Engine Land — GEO](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418) | 2026 | да |
| Title — ориентир до ~60 символов с ключом; Description — 140–160 символов (industry practice) | [YoSiteUp — AI SEO Workflow 2026](https://yositeup.com/ru-ua/blog/ai-seo-workflow-2026-research-to-publication) | 2026 | да (как ориентир, не жёсткая норма Google) |
| Вступление how-to: прямой ответ 40–60 слов в первом абзаце | [YoSiteUp — AI SEO Workflow 2026](https://yositeup.com/ru-ua/blog/ai-seo-workflow-2026-research-to-publication) | 2026 | да (best practice) |

**fact-bank.md:** прямых фактов про SEO-письмо нет — использовать только таблицу выше.

**Не использовать без оговорки:** «+140% трафика за 3 недели» (агентские кейсы); «плотность ключей 1–2%» как универсальное правило; любые показы Wordstat без MCP-данных; «GEO заменяет SEO».

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **longread, который читают люди**, и который **одновременно** готов к AI-выдаче. Не «ещё один список ключей», а **единый workflow**: интент → структура → инфостиль → FAQ/schema → GEO-чанки → чек-лист перед публикацией.

**Почему отличается от конкурентов:**
- Яндекс Direct — канон SEO без GEO и без «читабельности как фактора».
- OlegWeb/1PS — длинные алгоритмы без связки «остров смысла = GEO».
- GEO-гайды не учат писать текст с нуля.
- H1 «которые читают люди» — слабо раскрыт в SERP; наш фокус: **структура + короткие абзацы + answer-first** = и UX, и цитируемость.

**Tone (site-brief):** практично, B2B без воды; редакция бренда; без эмодзи в article.html.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье (один контент, две цели)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

**Режим B:** сама статья B01 — эталон: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead 40–60 слов.

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Первый абзац после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-adjacent | «Сколько символов…», «Что такое GEO в SEO?» |
| FAQ 5–7 пар | Конец longread | Ответ 2–4 предложения, action-first |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; абзац 3–5 строк |
| Island test | QA для writer | Блок понятен без соседних |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` (главная) |
| Alt обложки | Cover | «Редактор за ноутбуком…» (cover_scene_hint) |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс Direct); ориентир — полнота ответа и конкуренты в SERP; для how-to longread Excalibur — 8 500–9 500 знаков текста.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключевые слова в 2026 году?** — нет; естественные вхождения + LSI/тематические слова.
4. **Чем Title отличается от H1?** — Title для сниппета (~60 символов), H1 — заголовок на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage для блока вопросов.
6. **Что такое llms.txt и нужен ли он блогу?** — опциональный файл для AI-краулеров; не замена sitemap/robots.txt.
7. **Как проверить статью перед публикацией?** — чек-лист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Черновик чек-листа (15–20 пунктов для writer)

1. Primary query зафиксирован; secondary из карточки темы вписаны в план H2.  
2. Просмотрен топ-5 SERP: формат (гайд/FAQ/сравнение) совпадает с интентом.  
3. Один H1; H2–H3 без пропусков уровней.  
4. Lead: прямой ответ 40–60 слов с primary query.  
5. Каждый H2 начинается с тезиса (GEO-чанк / island test).  
6. Абзацы 3–5 строк; списки для 3+ пунктов.  
7. Главный ключ в H1, первом абзаце, 1–2 H2 — естественно.  
8. LSI и синонимы без переспама.  
9. Title ≤60 символов; Description 140–160; H1 ≠ Title.  
10. Alt у изображений описывает содержимое, не ключи.  
11. 3–5 осмысленных внутренних ссылок (из карточки: `/`).  
12. FAQ 5–7 вопросов с короткими action-ответами.  
13. JSON-LD BlogPosting + FAQPage (schema-агент, не в body).  
14. Автор/редакция и дата обновления видны или в meta.  
15. Факты только из research / fact-bank; нет выдуманных %.  
16. Island test: каждый H2 полезен отдельно.  
17. So what test: каждый абзац отвечает «что делать».  
18. CTA ≤ 3; не подменяет пользу.  
19. Нет эмодзи, длинных тире «—», ёлочек ««»».  
20. Финальная вычитка: орфография, битые ссылки, мобильная читаемость.

---

## 8. Риски для writer

- Не выдумывать показы Wordstat — MCP не отработал.  
- Не копировать структуру OlegWeb (13 шагов) или Pikapuka 1:1.  
- Объём текста: 8 500–9 500 знаков (`quality-blog.md`).  
- Min **5** нумерованных шагов в теле + чек-лист **15–20** пунктов.  
- Без VPN/обход блокировок; site_url — `/` по карточке.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель сможет от идеи до публикации пройти полный цикл SEO-статьи 2026: проверить спрос и интент, собрать структуру longread под людей и AI-выдачу, написать текст с E-E-A-T-сигналами, оформить мета/FAQ/schema и проверить материал чек-листом перед публикацией.

**action_outline:**

1. **Проверить спрос и интент:** primary query в Вордстат/Вебмастер (когда MCP доступен); открыть топ-5 SERP и зафиксировать формат ответа (гайд, FAQ, сравнение).  
2. **Собрать семантический кластер:** primary + secondary из карточки B01 + LSI из SERP; распределить по будущим H2.  
3. **Построить структуру longread:** один H1, 4–6 H2 из карточки, H3 для деталей; lead-план 40–60 слов с прямым ответом.  
4. **Написать черновик «сначала смысл»:** короткие абзацы, списки, таблицы; после каждого H2 — содержательный первый абзац (GEO-чанк).  
5. **Добавить E-E-A-T lite:** автор/редакция, примеры, ссылки на первоисточники; убрать воду (island/so what test).  
6. **Оптимизировать без переспама:** ключ в H1, lead, 1–2 H2, title/description; синонимы по тексту.  
7. **Оформить FAQ + schema-handoff:** 5–7 пар вопрос–ответ; передать schema-агенту BlogPosting + FAQPage.  
8. **Техника публикации:** title, description, alt, внутренние ссылки, дата обновления; robots.txt не блокирует OAI-SearchBot без причины.  
9. **Финальный чек-лист 15–20 пунктов** (раздел 7) — только после этого publish.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (7) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| Чек-лист 15–20 черновик | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 7 конкурентов (OlegWeb, Texterra, Яндекс Direct, 1PS, Tolk, hozyindachi, Search Engine Land). Wordstat MCP недоступен (user-mcp-kv). Угол — единый workflow SEO+GEO longread «для людей»: интент → структура → GEO-чанки → FAQ/schema → чек-лист 15–20. 20 фактов с URL, 9 шагов action_outline, 7 FAQ. Готов к writer.
===
