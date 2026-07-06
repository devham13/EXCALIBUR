# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата)  
**research_date:** 2026-07-06  
**disclaimer:** Все даты, версии и статистика проверены на 2026-07-06.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (янв. 2026) | Авторитет; workflow тема → Wordstat → структура → текст → мета; H1–H4; «плохо/хорошо»; без универсального объёма | Нет GEO/нейропоиска; CTA Директа | Блок про Директ; копировать H-структуру без GEO-слоя |
| 2 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм 13 шагов (февр. 2026) | От ключа до WordPress; интент, конкуренты, чек-лист публикации | Длинный список шагов без GEO; WP-специфика | 13 шагов 1:1; Telegram-CTA |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread 2026 | Wordstat, LSI, E-E-A-T, Schema Article+FAQ, Title ~65 знаков | Непроверенные кейсы «+140%»; agency tone | Проценты без источника; 7 разделов 1:1 |
| 4 | [gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | AI SEO + GEO (июнь 2026) | BLUF 40–60 слов; факты каждые 150–200 слов; «острова смысла» | Мало чек-листа публикации | Длинный narrative без actionable финала |
| 5 | [trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | Чек-лист под AI Overviews | Кластер 10–15 вопросов; lead-ответ; Schema FAQPage; Core Web Vitals | Уклон в услуги SEO | Коммерческий bias |
| 6 | [serptop.ru/blog/kak-pisat-seo-teksty](https://serptop.ru/blog/kak-pisat-seo-teksty/) | Гайд + чек-лист | Формула H1; meta Title/Description; структура H2-блоков | Слабый GEO-слой; общие формулировки | Шаблон «что это и зачем» без практики |
| 7 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | Семантика, E-E-A-T, Featured Snippet | Перегруз ИИ-инструментами | Копировать блок про «только ИИ» |
| 8 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Короткий принцип | «Полный ответ на одной странице»; LSI | Мало шагов, нет FAQ/schema | Thin content как основа |

**Паттерн SERP (июль 2026):** топ — «полный гайд 2026» с E-E-A-T, Wordstat, чек-листом (pikapuka, 1ps, olegweb). Растёт кластер **AI/GEO** (gracie, trigub, seohead). H1 «которые читают люди» слабо закрыт (qvai.ru — близкий угол, но поверхностно). Пробел: **единый workflow SEO+GEO для блога** с чек-листом перед публикацией и без agency-воды.

**Intent:** how_to — собрать семантику → структура → текст → мета → FAQ/schema → GEO-чанки → проверка. Вторичный: «seo текст для блога», «geo оптимизация статьи».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 06.07.2026)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в Cloud-среде (инструмент `wordstat_get_top_requests` не подключён). Точные показы в месяц **не получены**. Обновите MCP в Cursor IDE и повторите вызов; при 401 — [авторизация OAuth](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40).

**Запросы для повторного прогона Wordstat:**
- `как писать seo статьи` (primary)
- `seo текст для блога` (secondary)
- `geo оптимизация статьи` (secondary)
- смежные: `как написать seo статью`, `seo копирайтинг`, `seo текст для сайта`, `структура seo статьи`

### LSI-ключи для writer (из SERP + secondary_queries; **без подтверждённых показов**)

- как писать seo статьи, как написать seo статью, seo текст для блога, seo текст для сайта  
- seo копирайтинг, структура seo статьи, seo оптимизация текста, семантическое ядро  
- geo оптимизация статьи, generative engine optimization, нейропоиск, AI Overviews  
- e-e-a-t, featured snippet, schema.org FAQPage, BlogPosting, llms.txt  
- title description meta, внутренние ссылки, wordstat, интент запроса  
- сколько символов в seo статье, что такое geo в seo (faq_hints из карточки)

**SEO-стратегия (экспертная, до получения Wordstat):** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блок структуры longread; «geo оптимизация статьи» — в H2 «SEO + GEO в одной статье»; faq_hints — в FAQ.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и CTR | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title — ориентир ~65 знаков; H1 не дублирует Title | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Schema.org Article + FAQPage для сниппета и структуры | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| BLUF: прямой ответ в первых 40–60 словах блока | [Gracie Digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| Факты/статистика каждые 150–200 слов повышают цитируемость AI | [Gracie Digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| Кластер 10–15 смежных вопросов перед написанием | [Trigub — чек-лист AI](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 2026 | да |
| Core Web Vitals: LCP < 2,5 с, INP < 200 мс, CLS < 0,1 | [Trigub — чек-лист AI](https://trigub.ru/blog/chek-list-dlya-stati-kotoruyu-zametit-ii-neyropoisk-i-ai-overviews/) | 2026 | да |
| Meta Title до ~70 символов, Description до ~160 | [Serptop — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| Уникальность текста — ориентир не ниже 80% | [ADPASS — SEO-текст](https://adpass.ru/kak-napisat-seo-tekst/) | 2026 | да |
| Абзацы 3–4 строки; один подзаголовок на 1,5–2 тыс. знаков | [Brainbox — SEO-тексты](https://brainbox-marketing.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| GEO дополняет SEO: цель — цитирование в AI-ответах | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Первые 100–150 слов — ключевая зона для извлечения AI | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| Главная задача статьи — полный ответ; возврат в поиск = сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «AI обрабатывает 25% запросов» без первичника; «микроразметка ×1,5–2» без исследования.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, закрывающий запрос человека **и** упакованный для нейропоиска. Единый workflow: интент → Wordstat → структура → инфостиль → FAQ/schema → GEO-чанки → чеклист перед публикацией.

**Почему отличается:** Яндекс даёт SEO без GEO; GEO-гайды не учат писать с нуля; agency-лонгриды — вода и CTA. H1 «которые читают люди» — фокус на **читабельность как SEO+GEO фактор**.

**H2-каркас (из карточки B01):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как  
4. Чеклист перед публикацией (15–20 пунктов)

**Режим B:** сама статья B01 — эталон: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2.

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок «SEO + GEO» | «GEO — …» |
| Conversational H2 | FAQ-темы | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, action |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в body | BlogPosting + FAQPage |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом контенте.  
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 — на странице; не дублировать.  
5. **Какие schema для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.  
6. **Что такое llms.txt?** — опциональный файл для AI-краулеров; не замена sitemap.  
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику в Wordstat, определит интент, соберёт структуру longread с lead и атомарными H2, напишет текст без переспама, добавит FAQ и JSON-LD schema, применит GEO-приёмы (BLUF, факты, «острова смысла») и пройдёт чеклист перед публикацией в блог.

**action_outline:**

1. **Проверить спрос и интент:** в Wordstat ввести primary «как писать seo статьи» + secondary; выписать 10–15 смежных вопросов; открыть топ-5 SERP и зафиксировать, чего не хватает конкурентам.  
2. **Собрать структуру:** H1 (один) → lead с прямым ответом 40–60 слов → H2 по кластеру вопросов → H3 для деталей; минимум 1 таблица и 2 списка.  
3. **Написать черновик по BLUF:** под каждым H2 — тезис в первых 2 предложениях; абзацы 3–5 строк; факт или пример каждые 150–200 слов.  
4. **Оптимизировать мета:** Title ~65 знаков (ключ + польза), Description ~160, H1 ≠ Title; ключ в первом абзаце естественно.  
5. **Добавить FAQ 5–7:** короткие ответы-действия; вопросы из faq_hints и Wordstat-кластера.  
6. **Подготовить schema (handoff):** BlogPosting + FAQPage JSON-LD; даты datePublished/dateModified = дата публикации.  
7. **GEO-слой:** проверить «острова смысла» (блок понятен без соседних); упомянуть llms.txt опционально; внутренние ссылки на `/`.  
8. **Чеклист перед публикацией:** уникальность ≥80%, alt у изображений, перелинковка, Rich Results Test, отправка в Вебмастер/GSC.

---

## 8. Риски для writer

- Не выдумывать показы Wordstat — MCP не отдал данные.  
- Не копировать Pikapuka/olegweb 1:1.  
- Объём: 8 500–9 500 знаков.  
- Без эмодзи, без VPN.  
- Цифры только из таблицы фактов.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (17) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
