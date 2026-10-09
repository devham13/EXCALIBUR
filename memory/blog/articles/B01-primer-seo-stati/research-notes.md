# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-10-09  
**disclaimer:** Все даты, версии и статистика проверены на 09.10.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch + research-serp.json, 09.10.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: семантика (Вордстат), H1–H4, естественность ключей, title/description, alt, перелинковка; «универсального объёма нет» | Нет GEO/нейропоиска; CTA на Директ | Коммерческий блок Директа; копировать структуру без GEO-слоя |
| 2 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Пошаговый how-to 2026 | 7 шагов от запросов до чек-листа; акцент «текст под запрос, не под ключи» | Мало schema/GEO; узкий бренд | Дублировать 7 H2 1:1 |
| 3 | [seotika.ru/kak-pisat-seo-stati](https://seotika.ru/kak-pisat-seo-stati/) | Агентский гайд 2026 | Lead = ответ в первых 100 словах; H2 как вопросы; ориентир 1500–3000 слов для информационки; плотность 1–2% | Жёсткие цифры объёма без оговорки SERP; agency tone | Цифры объёма как жёсткое правило для нашего longread |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread + ИИ (2026) | Кластер запросов → H2; «после каждого H2 — содержательный ответ»; LSI без насильного вставления | Уклон в массовую генерацию ИИ | Промо «сотни материалов за минуты» как главный угол |
| 5 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Чек-лист + E-E-A-T (2026) | Wordstat/Serpstat, Title ~65 знаков, Schema Article + FAQPage, Featured Snippet | Кейсы с непроверенными % роста | Непроверенную статистику в кейсах |
| 6 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Короткий принципиальный гайд (обнов. 09.10.2026) | Поведенческий сигнал: возврат в поиск = провал; LSI и «хвосты»; объём вторичен | Мало пошаговики, FAQ, schema, GEO | «Просто следуй принципам» без чек-листа |
| 7 | [leadstream.marketing/blog/geo-optimization-guide-2026](https://leadstream.marketing/blog/geo-optimization-guide-2026) | GEO-руководство (2025–2026) | Таблица SEO vs AEO vs GEO; lists/tables/FAQ для AI; E-E-A-T для цитирования | Не учит писать SEO-статью с нуля; часть stats без первичника | «40% профессионалов» без первичного источника как факт |
| 8 | [articleai.ru/…/kak-napisat-seo-statyu-v-2026…](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Конкурент из research-serp | Полный цикл семантика → публикация | Пересечение с 1ps/pikapuka | AI-first без «читают люди» |

**Паттерн SERP (окт. 2026):** доминируют «полный гайд 2026» (7–13 шагов, семантика, E-E-A-T, ИИ-помощь). Отдельный кластер — GEO/AEO. Запрос **«как писать seo статьи»** закрывают техникой; **H1 «которые читают люди»** слабо дифференцирован (meta-journal.ru уже в выдаче по H1 — наш опубликованный эталон).

**Intent:** `how_to` — собрать семантику → разобрать SERP → структура → черновик → мета → GEO/FAQ/schema → чек-лист перед публикацией. Вторичный: связать **SEO-текст для блога** и **GEO-оптимизацию статьи** в одном workflow.

**Пробел для Excalibur:** единый практический маршрут «для людей + для нейровыдачи» с **режимом B** (сама статья = образец longread 8,5–9,5k знаков) и **чек-листом 15–20 пунктов**, без agency-воды и без «контент-завода за минуты».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` недоступен в Cloud Agent (`MCP server does not exist`). Вызов `wordstat_get_top_requests` для primary_query **«как писать seo статьи»** и secondary **«seo текст для блога»**, **«geo оптимизация статьи»** не выполнен. Подключите MCP и при необходимости обновите OAuth-токен: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Точные показы в месяц в этой версии research-notes отсутствуют — не выдумывать цифры спроса в статье.**

### LSI и смежные формулировки (из SERP + WebSearch, без частотности)

| Кластер | Фразы для writer |
|---------|------------------|
| Core how-to | как писать seo статьи, как написать seo статью, seo текст для блога, seo копирайтинг |
| Семантика | семантическое ядро, интент запроса, lsi, вордстат, вторичные ключи |
| Структура | структура seo статьи, h1 h2 h3, lead-абзац, оглавление, чек-лист |
| Техника | title description, meta description, alt изображений, перелинковка |
| Качество | e-e-a-t, полнота ответа, читабельность, переспам ключей |
| GEO | geo оптимизация статьи, нейровыдача, faq schema, blogposting, llms.txt |

**SEO-стратегия (без Wordstat):** primary в H1/lead; secondary «seo текст для блога» — в блок про формат блога; «geo оптимизация статьи» — отдельный подблок внутри H2 «SEO + GEO», не подменять H1.

---

## 3. Таблица фактов (цифры только с URL; сверка fact-bank.md)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции в выдаче | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат (и смежные инструменты вебмастера) | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-текст в 2026 = полезный текст под запрос и его окружение, не «набор ключей» | [SEO Школа](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| Для информационной статьи в гайде Seotika ориентир **1500–3000 слов** (контекст: «оптимальный объём информационной статьи») | [Seotika](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да (с оговоркой: сверять с SERP; Excalibur longread 8,5–9,5k **знаков**) |
| Прямой ответ в первых **~100 словах** + H2 как подвопросы | [Seotika](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| После каждого H2 — содержательный ответ, не «заголовок ради SEO» | [1PS](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Title — ориентир **~65 знаков**, H1 не дублирует Title | [Pikapuka](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Schema: Article/BlogPosting + FAQPage для сниппета и структуры | [Pikapuka](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Если пользователь возвращается в поиск — сигнал низкого качества материала | [MaryProject](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 09.10.2026 | да |
| GEO — оптимизация для цитирования в генеративных AI; SEO — позиции и клики (табличное различие) | [LeadStream GEO 2026](https://leadstream.marketing/blog/geo-optimization-guide-2026) | 12.2025 | да |
| Списки, таблицы, FAQ и фактическая плотность повышают пригодность контента для AI-ответов (качественная формулировка, не % без источника) | [LeadStream GEO 2026](https://leadstream.marketing/blog/geo-optimization-guide-2026) | 12.2025 | да |

**Из fact-bank.md (можно, если уместно в блоке про автоматизацию — не обязательно для B01):** 51% маркетологов используют нейросети для аналитики, а не слепой штамповки ([mayai.ru/kontent-zavod…](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/), 2026-06-11).

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «40% профессионалов используют AI» (LeadStream без первичника); жёсткая «плотность 1–2%» как догма без оговорки про естественность (Seotika).

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **longread, который дочитывают люди**, и который **разбит на «острова смысла»** для нейровыдачи. Один workflow: интент → структура → черновик → мета → FAQ/schema → GEO-правки → чек-лист.

**Отличие от конкурентов:**
- Яндекс — канон SEO без GEO-hooks.
- GEO-гайды (LeadStream, digitalrocket) не ведут новичка от нуля до опубликованной SEO-статьи.
- Агентские гайды перегружены кейсами и ИИ-масштабированием.

**Режим B:** статья B01 — **эталон формата** (8 500–9 500 знаков текста, 5–7 FAQ, BlogPosting + FAQPage, перелинковка на `/`).

**H2-каркас (карточка B01):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread  
3. FAQ и schema  
4. Чеклист перед публикацией  

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок SEO+GEO | «GEO — …» |
| Conversational H2/FAQ | faq_hints | «Сколько символов…», «Что такое GEO…» |
| Атомарные H2 | Каждый раздел | Тезис в первом предложении |
| FAQ 5–7 | Конец | Ответ 2–4 предложения, действие |
| Schema | meta, не body | BlogPosting + FAQPage |
| llms.txt | Упоминание | Опционально после sitemap |
| cover_scene_hint | Cover | Редактор, блокнот, тёплый свет |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); для how-to longread Excalibur — 8 500–9 500 знаков при полноте ответа.  
2. **Что такое GEO в SEO?** — дополнение к SEO: цитирование в AI-ответах при сохранении индексируемой структуры.  
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (~65 знаков), H1 на странице.  
5. **Какие schema для блога?** — BlogPosting + FAQPage.  
6. **Что такое llms.txt?** — подсказка для AI-краулеров; не замена robots/sitemap.  
7. **Как проверить статью перед публикацией?** — чек-лист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель за одну сессию соберёт семантику по primary query, спроектирует структуру longread под интент, напишет черновик с lead и FAQ, заполнит Title/Description, добавит JSON-LD BlogPosting + FAQPage, внесёт GEO-правки (атомарные H2, определения) и пройдёт чек-лист из 15–20 пунктов перед публикацией.

**action_outline:**

1. **Зафиксировать интент:** primary «как писать seo статьи» + secondary из карточки; записать, какой результат должен получить читатель после статьи.  
2. **Собрать семантику:** Вордстат/вебмастер — кластер запросов, LSI, минус «мусорные» формулировки; выделить 5–7 подвопросов под H2.  
3. **Разобрать ТОП-5 SERP:** объём, структура, пробелы; таблица «что добавим мы» (SEO+GEO, чек-лист, режим B).  
4. **Собрать outline:** H1 один; H2 = подвопросы; после каждого H2 — прямой ответ; lead с определением в 40–60 слов.  
5. **Написать черновик «для людей»:** короткие абзацы, списки, таблица SEO vs GEO; без переспама; факты только из research/fact-bank.  
6. **Техника:** Title ~65 знаков, Description, alt; главный ключ в H1 и lead; внутренние ссылки (карточка: `/`).  
7. **FAQ + schema:** 5–7 пар вопрос–ответ; handoff для BlogPosting + FAQPage JSON-LD.  
8. **GEO-слой:** определения, conversational формулировки, island test по каждому H2; при необходимости упомянуть llms.txt.  
9. **Финальный чек-лист 15–20 пунктов** (семантика, мета, структура, FAQ, schema, ссылки, даты, читабельность) — только после этого публикация.

---

## 8. Риски для writer

- Не выдумывать Wordstat-показы и «рост трафика %» без URL.  
- Объём: **8 500–9 500** знаков текста (quality-blog).  
- Не копировать Pikapuka/Seotika H2 1:1.  
- Без эмодзи в article.html; CTA ≤ 3.  
- Цифры из fact-bank — только если релевантны теме (не обязательный блок про контент-завод).

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (см. §2) |
| Таблица фактов с URL | ✅ (15+) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 источников (Яндекс Direct, SEO Школа, Seotika, 1PS, Pikapuka, MaryProject 09.10.26, LeadStream GEO, articleai). Wordstat MCP user-mcp-kv недоступен — показы не получены; LSI из SERP. Угол — единый workflow SEO+GEO longread «для людей», режим B, 9 шагов action_outline, 7 FAQ, 15+ фактов с URL. Готов к writer.
===
