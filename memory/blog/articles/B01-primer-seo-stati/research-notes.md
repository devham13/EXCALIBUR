# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата)  
**research_date:** 2026-08-10  
**disclaimer:** Все даты, версии и статистика проверены на 10.08.2026.

---

## 1. SERP-обзор (WebSearch, август 2026 — 7 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | «Сначала смысл, потом оптимизация»; H1→H2 из кластера вопросов; LSI без переспама; короткие абзацы | Очень длинный; ИИ-блок может увести от «ручного» workflow | Копировать структуру 1:1; обещания «ИИ напишет за вас» как главный CTA |
| 2 | [olegweb.ru/…/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм (13 шагов, обнов. 02.2026) | Wordstat на старте; интент; разбор сильного конкурента; WP-оформление; финальный чек-лист | Мало GEO/AEO; хостинг/шаблоны в сайдбаре | Affiliate-блоки Timeweb/Paradigma; 13 H2 «шагов» без единого workflow |
| 3 | [direct.yandex.ru/base/articles/seo-tekst…](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: объём без нормы, H1 один, 3–5 строк в абзаце, естественные ключи, Wordstat | Нет GEO; CTA Директа | Коммерческий хвост про рекламу |
| 4 | [fireseo.ru/blog/kak-pravilno-napisat-seo…](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | Агентский гайд GEO+SEO | Answer-first; атомарные чанки; pillar/cluster; FAQ; E-E-A-T с опытом | Agency tone; мало пошаговой семантики | «Плотность информации» без конкретного чек-листа |
| 5 | [iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga…](https://iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga-kak-pisat-stati-kotorye-privodyat-trafik/) | SEO-чеклист для блога (4 фазы) | Topic research → content → optimization → AI-overviews; Featured Snippet | EN-ориентиры; мало RU-специфики Яндекс | 31 пункт без приоритетов 🔴🟡🟢 |
| 6 | [ddsi.ru/blog/kak-napisat-seo-tekst…](https://ddsi.ru/blog/kak-napisat-seo-tekst-polnoe-rukovodstvo-dlya-nachinayushhih/) | 6 шагов для начинающих | Title 60–70 символов, Description 150–160; URL без параметров; чек-лист в шаге 6 | Поверхностный GEO; дата «2025» в сниппете | Устаревший year в title без refresh |
| 7 | [blog.click.ru/neiroseti/geo-vs-seo…](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | GEO vs SEO 2026 | Чанки 128–515 токенов; «один абзац = одна мысль»; SEO+AEO+GEO как три измерения | Фокус на GEO, не на написании с нуля | Цифры «25% россиян / 17%» без первичника в тексте без оговорки |

**Паттерн SERP (август 2026):** топ — «полный гайд 2026» с 8–13 шагами, E-E-A-T, Wordstat, чек-листом. Отдельный кластер — GEO/AEO-лонгриды (click.ru, fireseo). H1 «которые читают люди» в топе почти не встречается — **пробел для дифференциации**: читабельность как измеримый workflow, не абстрактный совет.

**Intent:** `how_to` — пользователь хочет **систему от ключа до публикации**: спрос → интент → структура → текст → мета → schema/FAQ → проверка. Вторичный: связка **SEO + GEO в одном материале** (`seo текст для блога`, `geo оптимизация статьи`).

**Пробел для Excalibur:** единый **action-first workflow** (не 13 разрозненных «шагов» и не encyclopedia GEO) + **чеклист 15–20 пунктов** + сама статья B01 как **эталон режима B** (8 500–9 500 знаков, FAQ, JSON-LD).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, регион 225, 10.08.2026)

⚠️ **WORDSTAT MCP WARNING:** MCP-сервер `user-mcp-kv` **недоступен** в среде Cloud Agent (не подключён в конфигурации MCP). Вызов `wordstat_get_top_requests` для `как писать seo статьи`, `seo текст для блога`, `geo оптимизация статьи` **не выполнен**. Точные объёмы спроса **не получены** — цифры ниже **не указаны намеренно**.

**Действие для пайплайна:** подключите MCP-KV в environment и обновите OAuth-токен:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Запросы для повторного прогона Wordstat

| Запрос | Роль |
|--------|------|
| как писать seo статьи | primary_query |
| seo текст для блога | secondary_1 |
| geo оптимизация статьи | secondary_2 |
| как написать seo статью | вариант формулировки (SERP) |
| seo статья для сайта | LSI-кластер |
| seo копирайтинг | LSI-кластер |
| структура seo статьи | LSI / FAQ |
| сколько символов в seo статье | faq_hint из карточки |
| что такое geo в seo | faq_hint из карточки |

### LSI для writer (экспертная семантика из SERP + карточка B01; **без объёмов**)

- как писать seo статьи, seo текст для блога, seo статья для сайта  
- семантическое ядро, LSI-фразы, интент запроса, Wordstat, Яндекс Вебмастер  
- структура longread, H1 H2 H3, lead-абзац, title, description, meta  
- E-E-A-T, личный опыт, кейс, скриншот, чек-лист перед публикацией  
- geo оптимизация статьи, answer-first, атомарные чанки, FAQPage, BlogPosting  
- перелинковка, внутренние ссылки, alt-тексты, pillar/cluster  
- сколько символов в seo статье, что такое geo в seo  

**SEO-стратегия (до получения Wordstat):** primary «как писать seo статьи» в H1/lead; «seo текст для блога» — в блок про инфостиль; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье»; faq_hints — в FAQ-блок.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир 3–5 строк | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья должна решать задачу пользователя лучше страниц конкурентов, а не только содержать ключ | [olegweb.ru — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Для проверки спроса используют Яндекс Вордстат (показы, похожие запросы) | [olegweb.ru — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| Title — ориентир ~60–70 символов; Description — ~150–160 символов | [ddsi.ru — SEO-текст](https://ddsi.ru/blog/kak-napisat-seo-tekst-polnoe-rukovodstvo-dlya-nachinayushhih/) | 2026 | да |
| URL — короткий, понятный, без параметров вида `?id=123` | [ddsi.ru — SEO-текст](https://ddsi.ru/blog/kak-napisat-seo-tekst-polnoe-rukovodstvo-dlya-nachinayushhih/) | 2026 | да |
| Ответ на вопрос пользователя — как можно быстрее, в начале текста (answer-first) | [fireseo.ru — SEO 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| Контент для ИИ: самодостаточные (атомарные) блоки; важное не прятать во вкладки/аккордеоны | [fireseo.ru — SEO 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| Pillar Content + 5–10 cluster-статей — рабочая модель тематического кластера | [fireseo.ru — SEO 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| E-E-A-T в 2026: акцент на Experience — личный опыт, тесты, скриншоты | [fireseo.ru — SEO 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| H1 — главный запрос; H2 закрывают подтемы; после каждого H2 — содержательный ответ | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Главный ключ — H1, первый абзац, 1–2 H2, title, description; LSI — естественно по тексту | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| SEO, AEO, GEO — три измерения одной поисковой реальности; SEO остаётся фундаментом | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| ИИ режет текст на чанки ~128–515 токенов (≈96–380 русских слов) для извлечения фактов | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| Правило для цитируемости: «один абзац = одна мысль»; у смыслового блока — свой подзаголовок | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| AEO — попадание в zero-click ответы Поиска с Алисой / Google AI Overview со ссылками на источники | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |

**fact-bank.md:** прямых фактов про SEO-writing нет — использовать только таблицу выше.

**Не использовать без оговорки:** «25% россиян ежедневно пользуются нейросетями, 17% не кликают по ссылкам» (click.ru — вторичная статистика без первичника в статье); «+140% трафика за 3 недели» (агентские кейсы); любые объёмы Wordstat без MCP-прогона.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один список ключей», а **единый workflow A→B→C**: интент → структура → инфостиль → FAQ/schema → GEO-чанки → **чеклист перед публикацией**.

**Почему отличается от конкурентов:**
- Яндекс — канон SEO без GEO-слоя в одном workflow.
- olegweb — 13 шагов + affiliate; мало GEO.
- GEO-гайды (click, fireseo) не учат писать текст с нуля для блога.
- H1 «**которые читают люди**» — слабо раскрыт в SERP; наш фокус: **читабельность как SEO+GEO фактор** (структура, island-test, короткие абзацы).

**Режим B:** сама B01 — **эталон**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (из карточки + research):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как (JSON-LD, не в body)  
4. Чеклист перед публикацией (15–20 пунктов)  

**Tone (site-brief):** практично, B2B без воды; редакция бренда; без эмодзи в article.html.

---

## 5. GEO hooks (для writer и schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи (40–60 слов) | Lead после H1 | «SEO-статья — …» |
| Определение GEO (40–60 слов) | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2/FAQ | FAQ | «Сколько символов…?», «Что такое GEO в SEO?» |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; island test |
| Schema handoff | meta, не body | BlogPosting + FAQPage |
| Внутренняя ссылка | CTA-блок | На `/` (главная) |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого контента.  
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI (Яндекс Директ).  
4. **Чем Title отличается от H1?** — Title для сниппета (~60–70 символов), H1 на странице; не дублировать дословно.  
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.  
6. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.  
7. **Как собрать семантику для seo текста блога?** — Wordstat + анализ SERP + вторичные запросы из подсказок.

---

## 7. Черновик чек-листа (15–20 пунктов для writer)

1. Primary query зафиксирован; secondary и LSI выписаны.  
2. Интент определён (informational how-to).  
3. Топ-3–5 конкурентов разобраны: структура, пробелы.  
4. H1 один; H2–H3 закрывают подтемы; после каждого H2 — ответ сразу.  
5. Lead: боль + что получит читатель + результат (не «в этой статье»).  
6. Абзацы 3–5 строк; списки/таблица где уместно.  
7. Главный ключ в H1, первом абзаце, 1–2 H2, title, description — естественно.  
8. Title ~60–70 символов; Description ~150–160.  
9. URL короткий, без `?id=`.  
10. Блок «SEO + GEO»: answer-first, атомарные чанки.  
11. FAQ 5–7 вопросов; ответы 2–4 предложения, ≤80 слов.  
12. JSON-LD BlogPosting + FAQPage (schema-агент).  
13. Alt у изображений; автор/дата видимы.  
14. Внутренняя ссылка на `/` и при необходимости hub-статьи.  
15. Island test по каждому H2.  
16. Нет воды, переспама, выдуманной статистики.  
17. Финальная вычитка: орфография, факты по research-notes.

---

## 8. Риски для writer

- Не выдумывать объёмы Wordstat — MCP не прогнан.  
- Не копировать 13 шагов olegweb или 7 разделов Pikapuka 1:1.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Без эмодзи в article.html; без VPN/обход блокировок.  
- Цифры только из раздела 3 или fact-bank.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель проверит спрос и интент, соберёт семантику и структуру longread, напишет SEO-текст с GEO-чанками и FAQ, заполнит title/description, подготовит schema и пройдёт чеклист из 15–20 пунктов перед публикацией в WordPress.

**action_outline:**

1. **Проверить спрос и интент:** вбить primary query в поиск; открыть Wordstat (когда доступен MCP) и топ-5 URL; зафиксировать тип контента (гайд/how-to) и список подвопросов.  
2. **Разобрать конкурентов:** для 3–5 страниц из SERP выписать H2, объём, форматы (чек-лист, FAQ, таблицы), что добавить сильнее них (опыт, скрины, чек-лист).  
3. **Собрать семантику и скелет:** primary + secondary + LSI; H1, 4–6 H2, FAQ-вопросы; lead-абзац с определением SEO-статьи.  
4. **Написать черновик по блокам:** сначала смысл (ответ после каждого H2), короткие абзацы 3–5 строк; затем естественно встроить ключи.  
5. **Добавить GEO-слой:** answer-first в lead; блок «SEO + GEO»; атомарные чанки (island test); 5–7 FAQ с короткими ответами.  
6. **Оптимизировать мета и URL:** title ~60–70 символов, description ~150–160; slug без параметров; H1 ≠ title дословно.  
7. **Подготовить schema и перелинковку:** BlogPosting + FAQPage (JSON-LD); alt; 1–2 внутренние ссылки; дата публикации/обновления.  
8. **Пройти чеклист перед публикацией** (раздел 7) и опубликовать в CMS.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (7) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks + чек-лист | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `blog-topics.md` + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
status: ✅
utility_verdict: PASS
wordstat: ⚠️ MCP user-mcp-kv недоступен — объёмы не получены
summary: SERP — 7 конкурентов (1ps.ru, olegweb, Яндекс Direct, fireseo, iconsult, ddsi, click.ru). Угол — единый workflow SEO+GEO longread «для людей»: читабельность, атомарные чанки, FAQ/schema, чеклист 15–20 пунктов. 20 фактов с URL, 8 шагов action_outline, 7 FAQ. Готов к writer.
===
