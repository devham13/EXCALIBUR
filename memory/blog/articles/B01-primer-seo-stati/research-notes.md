# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to + чеклист)  
**search_intent:** how_to  
**research_date:** 2026-09-10  
**disclaimer:** Все даты, версии и статистика проверены на 10.09.2026.

---

## Utility gate

| Проверка | Результат |
|----------|-----------|
| `excalibur_blog_utility_gate.py --topic-id B01` | PASS |
| `search_intent` | how_to |
| `article_mode` | B |

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт SEO-статью для блога по единому workflow: семантика в Wordstat → структура longread → текст «для людей» → FAQ/schema → GEO-чанки → финальный чеклист перед публикацией.

**action_outline:**

1. Определить интент запроса и формат выдачи (гайд, чек-лист, FAQ) по ТОП-5 SERP.
2. Собрать семантику в Яндекс Вордстат: primary + 15–25 LSI-фраз, сгруппировать в 3–5 кластеров.
3. Составить структуру H1 → lead (ответ в 40–70 словах) → H2 по кластерам → FAQ.
4. Написать черновик «сначала смысл»: короткие абзацы, списки, таблица, без переспама ключей.
5. Заполнить Title, Description, alt; H1 не дублировать Title дословно.
6. Добавить BlogPosting + FAQPage (JSON-LD), внутренние ссылки.
7. Упаковать GEO-слой: BLUF в первых 100–150 словах, атомарные H2-блоки, llms.txt (упоминание).
8. Пройти чеклист перед публикацией (15+ пунктов): факты, мета, schema, читабельность, индексация.

---

## 1. SERP-обзор (WebSearch, 10.09.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Авторитет; workflow тема → семантика → структура → текст; «плохо/хорошо»; Wordstat, alt, мета; абзацы 3–5 строк | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа; канон H1–H4 без GEO |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-...](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 | Кластеризация Wordstat; «сначала смысл, потом оптимизация»; H2 с ответом сразу после заголовка | Длинный; блок про ИИ без human-in-the-loop | Копировать 10+ разделов 1:1 |
| 3 | [texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu...](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | Чек-лист 9 критериев (июн 2026) | E-E-A-T + ЭПОС; AI Overviews, Алиса AI; intent-first | Agency tone; чек-лист без пошагового «с нуля» | Продажи Texterra как основной CTA |
| 4 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 13 шагов WordPress (2026) | Полный алгоритм от ключа до индексации; таблицы, списки | Мало GEO; привязка к WP | 13 H2 под копирку |
| 5 | [roiseo.ru/blog/struktura-seo-stati-dlya-bloga/](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон SEO-статьи блога | Answer-first 40–70 слов; таблица + ошибки + чек-лист + FAQ | Узкий SEO-агентский угол | Шаблон блоков без контекста B2B AI-блога |
| 6 | [trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-...](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | GEO + AI Overviews | Первые 100 слов = ответ для ИИ; FAQPage; структура how-to | Фокус на AI, не на базовое написание SEO | Agency checklist как единственный каркас |
| 7 | [geo-course.ru/blog/kak-pisat-kontent-dlya-nejrosetej/](https://geo-course.ru/blog/kak-pisat-kontent-dlya-nejrosetej/) | BLUF + чанкинг | «Золотой параграф» ~190 слов; Summary Box; H2-вопросы | Не учит семантику/Wordstat с нуля | Цифры без первичника в кейсах |
| 8 | [developers.google.com/search/docs/appearance/structured-data/intro-structured-data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) | Google Search Central | JSON-LD recommended; markup = explicit clues; Rich Results Test | EN; не про копирайтинг | Кейсы CTR (+25%, +35%) как «гарантия» для reader |

**Паттерн SERP:** топ — «полный гайд 2026» (1ps, Pikapuka, olegweb) + чек-листы (Texterra, ROI SEO) + GEO-кластер (trigub, geo-course). H1 «которые читают люди» в топе почти не встречается — дифференциатор Excalibur.

**Intent:** how_to — пошаговая система от семантики до публикации. Вторичный: связка SEO + GEO в одном материале для блога.

**Пробел для Excalibur:** единый workflow «читаемость = SEO-фактор» + GEO-чанки + чеклист 15+ пунктов; режим B — сама статья как эталон формата (8 500–9 500 знаков, 5–7 FAQ, schema).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в Cloud Agent run (namespace отсутствует в каталоге MCP). Вызов `wordstat_get_top_requests` невозможен. Точные показы в месяц **не получены** — в тексте статьи не указывать выдуманные частотности.

**Fallback (семантика из SERP + конкурентов, без цифр спроса):**

| Кластер | LSI-фразы для writer |
|---------|----------------------|
| Primary | как писать seo статьи, как написать seo статью, seo текст для блога |
| Семантика | яндекс вордстат, lsi слова, ключевые слова, семантическое ядро, поисковый интент |
| Структура | структура seo статьи, h1 h2 h3, title description, longread, чек-лист |
| Качество | e-e-a-t, эпос, переспам, уникальность смысловая, полезность |
| GEO | geo оптимизация статьи, нейропоиск, ai overviews, bluf, llms.txt, faq schema |
| FAQ-intent | сколько символов в seo статье, что такое geo в seo |

**Действие writer:** в блоке про семантику дать инструкцию «откройте wordstat.yandex.ru → введите primary query → выпишите 15–25 фраз от 50 показов/мес» без подстановки конкретных чисел из research.

**OAuth (если MCP восстановят):** https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| После каждого H2 сразу давать содержательный ответ | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Сначала смысл, потом оптимизация ключей | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| SEO-текст 2026 должен быть понятен человеку, поисковику и AI (Google AI Overviews, Алиса AI, ChatGPT, Perplexity) | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Google: helpful, people-first content; Яндекс: ЭПОС (экспертность, полезность, оригинальность, содержательность) | [Texterra — чек-лист 2026](https://texterra.ru/blog/seo-tekst-kak-pravilno-optimizirovat-statyu-i-drugoy-kontent-dlya-sayta.html) | 04.06.2026 | да |
| Title — до ~60 символов; главный ключ в начале; не дублировать H1 дословно | [Divitio — пошаговая инструкция](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Первый экран: H1 + краткий ответ 40–70 слов | [ROI SEO — структура статьи](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| Первые 100 слов после H1 — готовый ответ для ИИ | [trigub.ru — чек-лист для ИИ](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 2026 | да |
| BLUF: прямой ответ в первых 100–200 словах; «золотой параграф» ~190 слов на H2 | [geo-course.ru — BLUF](https://geo-course.ru/blog/kak-pisat-kontent-dlya-nejrosetej/) | 2026 | да |
| Google рекомендует JSON-LD для structured data | [Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) | 10.12.2025 | да |
| Structured data не должна описывать невидимый пользователю контент | [Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) | 10.12.2025 | да |
| GEO (Generative Engine Optimization) — оптимизация под цитирование в AI-ответах, не замена SEO | [pawetta.com — GEO 2026](https://pawetta.com/blog/geo-optimizaciya/) | 2026 | да |
| Princeton GEO (Aggarwal et al., 2023): cite sources / statistics могут повышать visibility в AI-выдаче | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да (без точного % без arxiv) |
| Главная задача статьи — полный ответ; возврат в поиск = сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «микроразметка ×1,5–2 цитирование» без первичника; HubSpot −70–80% как универсальный прогноз.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Единый workflow, не «ещё один чек-лист ключей».

**Отличия от конкурентов:**
- Яндекс — канон SEO без GEO; GEO-гайды не учат писать с нуля.
- Агентские гайды перегружены CTA и непроверенными кейсами.
- H1 «которые читают люди» — слабо раскрыт в SERP; фокус: **читабельность как SEO-фактор** + техника.

**Режим B:** статья B01 — **эталон формата**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как
4. Чеклист перед публикацией (15–20 пунктов)

**Tone:** практично, B2B без воды (site-brief); без эмодзи; дефис вместо длинного тире в тексте статей.

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-блоки | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | 2–4 предложения, action-ответ |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema | meta / jsonld | BlogPosting + FAQPage, не в body |
| llms.txt | GEO-блок | Что это и зачем блогу |
| internal_links | из карточки | На `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и конкуренты; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом контенте.
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~60 символов), H1 на странице; не дублировать.
5. **Какие schema для блога?** — BlogPosting + FAQPage.
6. **Что такое llms.txt?** — файл для AI-краулеров; полезный сигнал, не замена sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать Wordstat-частотности (MCP недоступен).
- Не копировать Pikapuka/olegweb 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Цифры только из таблицы фактов §3.
- Без VPN, эмодзи, выдуманного ROI.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate topic | ✅ PASS |
| SERP ≥ 5 конкурентов | ✅ (8) |
| Wordstat | ⚠️ MCP unavailable, LSI fallback |
| Таблица фактов ≥ 15 | ✅ (18) |
| action_outline | ✅ (8 шагов) |
| reader_outcome | ✅ |
| utility_verdict | ✅ PASS |
| GEO hooks + FAQ | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + B01 в `blog-topics.md` + `site-brief.md`.
