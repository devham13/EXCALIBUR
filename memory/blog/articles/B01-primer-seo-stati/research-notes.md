# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + чеклист)  
**search_intent:** how_to  
**research_date:** 2026-07-12  
**disclaimer:** Все даты, версии и статистика проверены на 12.07.2026 (2026 год).

---

## Utility gate

| Поле | Значение |
|------|----------|
| Gate 0 (topic) | PASS — `python3 scripts/excalibur_blog_utility_gate.py --topic-id B01` |
| **utility_verdict** | **PASS** |
| **reader_outcome** | Читатель сможет самостоятельно собрать семантику, спланировать структуру SEO+GEO longread, написать текст «для людей», оформить мета/FAQ/schema и пройти финальный чеклист перед публикацией в блоге. |
| **action_outline** | 1) Проверить спрос и интент в Wordstat по primary query. 2) Разобрать топ SERP и выписать обязательные подтемы. 3) Собрать кластер ключей (primary + secondary + LSI). 4) Сверстать каркас H1–H3 + FAQ из вопросов пользователей. 5) Написать lead с прямым ответом в 40–60 слов и заполнить «острова смысла» (чанки 100–380 слов). 6) Встроить GEO-слой: факты, таблицы, автор, answer-first подзаголовки. 7) Заполнить Title/Description, alt, 3–5 внутренних ссылок. 8) Подготовить BlogPosting + FAQPage (JSON-LD вне body). 9) Пройти чеклист публикации (15+ пунктов). |

---

## 1. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в Cloud-среде прогона (сервер не подключён; вызов `wordstat_get_top_requests` завершился ошибкой «MCP server does not exist»). Точные показы в месяц **не получены** — цифры спроса в текст статьи не включать.

Обновите токен и подключение MCP через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Экспертная семантика (без объёмов — только для кластера writer)

Пока Wordstat недоступен, кластер собран из SERP (WebSearch 12.07.2026), `research-serp.json`, карточки B01 и подсказок конкурентов. **Writer:** после восстановления MCP перепроверить частотность в Wordstat.

| Группа | Фразы (LSI / secondary) |
|--------|-------------------------|
| Primary | как писать seo статьи, как написать seo статью, seo текст для блога |
| Структура | структура seo статьи, seo текст для сайта, longread seo, h1 h2 seo |
| Семантика | семантическое ядро seo, lsi фразы seo, распределение ключей по тексту |
| Техника | meta title description seo, alt теги seo, внутренняя перелинковка seo |
| Качество | e-e-a-t seo, seo копирайтинг 2026, чеклист seo статьи |
| GEO-слой | geo оптимизация статьи, что такое geo в seo, сколько символов в seo статье |
| Инструменты | яндекс вордстат seo, seo текст вордстат |

**SEO-стратегия для writer:** primary «как писать seo статьи» в H1 и lead; secondary «seo текст для блога» и «geo оптимизация статьи» — в H2 и FAQ; LSI — естественно по блокам, без переспама.

---

## 2. SERP-обзор (WebSearch + research-serp.json, 12.07.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [olegweb.ru/.../kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Практик, 13 шагов (фев. 2026) | Полный pipeline от темы до WordPress; интент, конкуренты, скриншоты, чек-лист | Уклон в WordPress-хостинг; GEO как побочный эффект | CTA на хостинг/шаблоны; 13 шагов 1:1 |
| 2 | [direct.yandex.ru/.../seo-tekst](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | 4 шага workflow; Wordstat/Вебмастер; H1–H4; абзацы 3–5 строк; без переспама | Нет GEO/нейропоиска; CTA Директ | Коммерческий блок Директа |
| 3 | [1ps.ru/.../seo-tekstyi-2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Агентский гайд 2026 | Wordstat → кластер → H2; E-E-A-T; Featured Snippet; ИИ как помощник | Длинный sales-narrative; перегруз инструментами | Копировать структуру 1:1 |
| 4 | [pikapuka.com/.../kak-napisat-seo-tekst](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Longread + чек-лист | 10 шагов, Schema Article+FAQ, Title ~65 знаков | Непроверенные % в кейсах | Кейсы «+140%» без источника |
| 5 | [blog.click.ru/.../geo-vs-seo](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | GEO+SEO 2026 | Чанки 100–380 слов; 40–60 слов lead; предложение 12–20 слов; Schema | Агентский CTA click.ru; часть stats без первичника в тексте | Цифры 17%/25% без первичника |
| 6 | [rosta-web.ru/.../seo-teksty-2026](https://rosta-web.ru/blog/seo-teksty-2026-strategiia-prodvizheniia-kontenta-v-poiske-gaid-primery/) | Стратегия + чек-лист ключей | Плотность 2–3%; Title 50–60 / Description 120–160; перелинковка | Кейс «+180%» без верификации; AI-хайп | Непроверенные кейсы трафика |
| 7 | [pr-cy.ru/.../seo-kopirayting](https://pr-cy.ru/news/p/8330-seo-kopirayting-effektivnye-priemy-kotorye-malo-kto-ispolzuet) | 6 приёмов + чек-лист (обн. 28.01.2026) | Интент > частотность; E-E-A-T; AI Overviews; Title с пользой | Старый каркас 2020, дополнен 2026 | Фокус на X/Twitter-цитаты |
| 8 | [maryproject.ru/.../kak-pravilno-pisat-stati-pod-seo](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Короткий гайд | «Полный ответ на одной странице»; поведенческий сигнал | Мало actionable шагов, нет GEO/schema | Вода «следуйте принципам» |

**Паттерн SERP:** топ — «полный гайд 2026» с Wordstat, E-E-A-T, чек-листом (olegweb, 1ps, pikapuka). Отдельный кластер — GEO-лонгриды (click.ru). H1 «которые читают люди» в выдаче почти не раскрыт: конкуренты говорят про «топ» и «ИИ», редко про **читабельность как SEO-фактор**.

**Intent:** how_to — пользователь хочет **пошаговую систему** от семантики до публикации. Вторичный: связать SEO и GEO в **одном** материале без двух отдельных проектов.

**Пробел для Excalibur:** единый workflow SEO+GEO для B2B-блога: longread 8,5–9,5k знаков, атомарные H2, FAQ/schema, чеклист 15+ пунктов; режим B — сама статья как эталон формата.

---

## 3. Таблица фактов (15+ утверждений с URL)

| # | Факт | Источник | Дата | Можно в текст |
|---|------|----------|------|---------------|
| 1 | Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 2 | H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 3 | Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 4 | Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 5 | Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 6 | Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 7 | SEO-статья должна решать задачу пользователя лучше страниц конкурентов, а не только содержать ключ | [olegweb — SEO-статья 2026](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | 05.02.2026 | да |
| 8 | Суть текста для ИИ-поиска — в первых 40–60 словах; каждый блок закрывает отдельный запрос | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| 9 | Смысловой блок для чанкинга — 100–380 слов с подзаголовком; предложение 12–20 слов; абзац 30–60 слов | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| 10 | ИИ режет текст на чанки ~96–380 русских слов для извлечения фактов | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| 11 | Плотность ключевых слов не должна превышать 2–3% (ориентир естественности) | [RostaWeb — SEO-тексты 2026](https://rosta-web.ru/blog/seo-teksty-2026-strategiia-prodvizheniia-kontenta-v-poiske-gaid-primery/) | 28.04.2026 | да |
| 12 | Title 50–60 символов с ключом в начале; Meta Description 120–160 символов | [RostaWeb — SEO-тексты 2026](https://rosta-web.ru/blog/seo-teksty-2026-strategiia-prodvizheniia-kontenta-v-poiske-gaid-primery/) | 28.04.2026 | да |
| 13 | Не более 5–7 внутренних ссылок на 1000 слов — иначе структура выглядит неестественно | [RostaWeb — SEO-тексты 2026](https://rosta-web.ru/blog/seo-teksty-2026-strategiia-prodvizheniia-kontenta-v-poiske-gaid-primery/) | 28.04.2026 | да |
| 14 | В 2026 приоритет — интент запроса и E-E-A-T, а не плотность ключей; AI Overviews усиливают zero-click | [PR-CY — SEO-копирайтинг](https://pr-cy.ru/news/p/8330-seo-kopirayting-effektivnye-priemy-kotorye-malo-kto-ispolzuet) | 28.01.2026 | да |
| 15 | Google в марте 2024 усилил борьбу с низкокачественным и неоригинальным контентом в выдаче | [PR-CY — SEO-копирайтинг](https://pr-cy.ru/news/p/8330-seo-kopirayting-effektivnye-priemy-kotorye-malo-kto-ispolzuet) | 28.01.2026 | да |
| 16 | GEO (Generative Engine Optimization) дополняет SEO: цель — видимость в ответах генеративных ИИ, база — индексируемый контент | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| 17 | Schema.org (Article, FAQPage) помогает ИИ распознавать структуру; не заменяет качество текста | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| 18 | GPTBot, PerplexityBot, Google-Extended не должны быть заблокированы в robots.txt без веской причины | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |

**fact-bank.md:** прямых фактов по SEO-написанию нет — использовать только таблицу выше.

**Не использовать без оговорки / первичника:** «каждый четвертый россиянин» и «17% не кликают» (click.ru без первичной ссылки в статье); «+180% трафика» (RostaWeb); «+140%» (Pikapuka); «микроразметка ×1,5–2» без arxiv/NP Digital primary.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от конкурентов:**
- Яндекс даёт канон SEO без GEO-слоя; GEO-гайды не учат писать текст с нуля.
- Агентские гайды перегружены кейсами и CTA.
- H1 «которые читают люди» слабо раскрыт в SERP — наш фокус: **читабельность как SEO-фактор** (структура, короткие абзацы, «острова смысла») + техника.

**Режим B:** статья B01 — **эталон формата**: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением, перелинковка на `/`.

**H2-каркас (из карточки B01 + research):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Первый абзац | 40–60 слов, прямой ответ |
| Определение GEO | Блок «SEO + GEO» | 40–60 слов |
| Conversational H2 | FAQ-зона | «Сколько символов…», «Что такое GEO в SEO?» |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис; island test |
| FAQ 5–7 | Конец | Ответ 2–4 предложения, action-first |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Внутренняя ссылка | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI, плотность ориентир до 2–3%.
4. **Чем Title отличается от H1?** — Title для сниппета (50–60 символов), H1 — на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt и нужен ли он блогу?** — опциональный сигнал для AI-краулеров; не замена sitemap/robots.txt.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Черновик чеклиста публикации (для writer, 15+ пунктов)

1. Primary query в H1 и первом абзаце естественно.  
2. Secondary queries закрыты отдельными H2 или FAQ.  
3. Lead: прямой ответ в 40–60 слов без «в этой статье».  
4. Каждый H2 — island test (понятен без соседних блоков).  
5. Абзацы 3–5 строк; списки/таблицы там, где перечисление.  
6. Title 50–60 символов, Description 120–160 — с пользой, не дубль H1.  
7. Alt у изображений с описанием сцены, не «image1».  
8. 3–5 внутренних ссылок по смыслу (не >5–7 на 1000 слов).  
9. FAQ 5–7 с короткими ответами-действиями.  
10. JSON-LD BlogPosting + FAQPage (отдельный файл, не в body).  
11. Автор/редакция указаны (E-E-A-T lite).  
12. Факты только из таблицы §3 — без выдуманных %.  
13. Нет эмодзи, длинных тире «—», ёлочек ««»».  
14. robots.txt не блокирует AI-краулеры без причины.  
15. Финальная вычитка: убрать воду, повторы, keyword stuffing.

---

## 8. Риски и blockers для writer

- Не выдумывать объёмы Wordstat — MCP недоступен.
- Не копировать структуру olegweb (13 шагов) или Pikapuka 1:1.
- Объём: 8 500–9 500 знаков (`shared/quality-blog.md`).
- Без VPN/обход блокировок; CTA ≤ 3.
- `site_url` — плейсхолдер `/` по карточке B01.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate PASS + action_outline | ✅ |
| SERP ≥ 5 конкурентов (свежий WebSearch) | ✅ |
| Wordstat (попытка MCP + warning) | ⚠️ сервер недоступен |
| Таблица фактов ≥ 15 с URL | ✅ |
| utility_verdict: PASS | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks + H2 outline | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
