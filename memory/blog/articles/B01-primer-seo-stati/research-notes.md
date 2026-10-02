# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**search_intent:** how_to  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-10-02  
**utility_gate (topic):** PASS (`python3 scripts/excalibur_blog_utility_gate.py --topic-id B01`)  
**disclaimer:** Все даты, версии и статистика проверены на 02.10.2026 (2026 год). Окно свежести источников: после 2026-07-04.

---

## Utility (Gate 2)

**utility_verdict:** PASS  

**reader_outcome:** Читатель сможет по одному workflow собрать SEO-longread под «как писать seo статьи»: семантика и интент → структура H1–H3 → текст «для людей» → мета и внутренние ссылки → FAQ/schema → GEO-чанки → финальный чеклист перед публикацией.

**action_outline (workflow для статьи и для читателя):**

1. Зафиксировать primary/secondary query и интент (информационный how-to); выписать 5–7 подвопросов из SERP и подсказок.
2. Разобрать TOP-5 URL в выдаче: какие H2 обязательны, где пробел (читабельность + GEO в одном материале).
3. Собрать каркас: H1 из карточки, 4 H2 из `blog-topics.md`, внутри — семантика, Title/Description, E-E-A-T lite.
4. Написать lead: прямой ответ на запрос в первых 2–3 предложениях, без «в этой статье».
5. Раскрыть каждый H2 по правилу «сначала содержательный ответ под заголовком», короткие абзацы, списки/таблицы.
6. Вписать ключи естественно: H1, lead, 1–2 H2, Title, Description; LSI из блока ниже — без переспама.
7. Добавить FAQ 5–7 пар + JSON-LD BlogPosting + FAQPage (schema — отдельная роль, не в body).
8. Упаковать GEO: атомарные чанки под H2, Snippet-first, island test; упомянуть llms.txt и доступность HTML для краулеров.
9. Прогнать чеклист 15–20 пунктов (мета, ссылки, alt, читабельность, факты только из таблицы ниже).

---

## 1. SERP-обзор (WebSearch, 2026-10-02)

Источник приоритетный: **WebSearch Курсора** + сверка с `research-serp.json` (36 уникальных URL по 6 запросам). Дата среза: 02.10.2026.

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|-----------------|------------------|---------------|
| 1 | [direct.yandex.ru/.../seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: композиция, H1–H4, объём без «магической цифры», Вордстат/семантика, мета, alt, перелинковка | Нет отдельного блока GEO/нейроответов; CTA на Директ | Коммерческий блок Директа; формальные H2 без практики GEO |
| 2 | [1ps.ru/.../seo-tekstyi-2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 + ИИ | Кластер вопросов → H2; «после H2 сразу ответ»; E-E-A-T, LSI без насильного вхождения | Уклон в AI-генерацию; длинный монолит | Копировать структуру 1:1; обещания «ИИ за вас» без human-in-the-loop |
| 3 | [pikapuka.com/.../polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский гайд + чек-лист | Семантика, E-E-A-T, Schema Article/FAQ, Title ~65 зн. | Кейсы с непроверяемыми %; GEO вторичен | Непроверенные проценты в кейсах |
| 4 | [olegweb.ru/.../kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм (13 шагов) | От интента до WordPress, таблицы/списки, чек перед публикацией | Мало GEO; привязка к WP | 13 H2 «как у автора» без адаптации под H1 B01 |
| 5 | [vebdisain.ru/.../kak-pisat-seo-teksty](https://vebdisain.ru/seo-i-veb-dizajn/seo-v-yandekse/kak-pisat-seo-teksty) | Фокус Яндекс 2026 | Разбор «плохого SEO-текста» (спам, переоптимизация, скрытый текст); Title/Description/URL; чек-лист | Эмодзи в заголовках; нет schema/GEO deep dive | Эмодзи в H2; драматизация без actionable GEO |
| 6 | [articleai.ru/.../poshagovaya-instruktsiya](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Инструкция «семантика → публикация» | Связка топ + AI-ответы; актуальный год в заголовке | Перегруз AI-инструментами | Product-led narrative вместо универсального workflow |
| 7 | [habr.com/ru/articles/1081126](https://habr.com/ru/articles/1081126/) | GEO / Habr | Чёткое SEO vs GEO; Алиса ↔ топ Яндекса; конкретика для цитирования | Не учит писать SEO-статью с нуля | Переносить B2B-кейсы без адаптации |

**Паттерн SERP 2026:** доминируют «полный гайд 2026» (семантика → структура → E-E-A-T → чек-лист) и отдельный кластер GEO. Запрос «которые **читают люди**» слабо закрыт заголовками конкурентов — возможность B01.

**Intent:** how_to — нужен **единый процесс**, а не энциклопедия «что такое SEO». Вторичный intent: «seo текст для блога», «geo оптимизация статьи» — встроить в один longread, не отдельной новостью.

**Сверка fact-bank.md:** прямых фактов про SEO-письмо в банке нет; для B01 опираемся на первичные/авторитетные URL ниже. Факты про ИИ-конвейер из fact-bank — **не** смешивать с SEO-гайдом без запроса карточки.

---

## 2. Яндекс Wordstat (спрос и LSI)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` / инструмент `wordstat_get_top_requests` **недоступен** в текущей Cloud-среде (namespace не подключён). Точные **показы в месяц** не получены. После подключения MCP повторить вызов для:

- `как писать seo статьи`
- `seo текст для блога`
- `geo оптимизация статьи`

При 401 токена: `https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40`

**LSI и смежные формулировки (из SERP + [семантика Яндекс](https://direct.yandex.ru/base/articles/semanticheskoe-yadro-sajta), без выдуманных частот):**

| Фраза (LSI / смежный запрос) | Откуда | Назначение в тексте |
|------------------------------|--------|---------------------|
| как написать seo статью | SERP primary cluster | H2, lead, FAQ |
| seo текст для блога | secondary_query B01 | подзаголовок / абзац про блог |
| seo копирайтинг | Яндекс Direct | синоним в lead |
| структура seo статьи | 1ps, Seotika | H2 «структура longread» |
| семантическое ядро / кластеризация | Яндекс Direct | блок семантики |
| e-e-a-t / экспертность автора | Pikapuka, FireSEO | E-E-A-T lite |
| geo оптимизация / generative engine optimization | secondary_query, Habr, FireSEO | H2 «SEO + GEO» |
| title description meta | Яндекс, vebdisain | чеклист |
| faq schema json-ld | Pikapuka | H2 FAQ и schema |
| snippet-first / атомарный абзац | FireSEO, pw.agency | GEO-hooks |
| яндекс вордстат | Яндекс Direct | инструмент (ссылка wordstat.yandex.ru) |
| переспам ключевых слов | Яндекс Direct, vebdisain | FAQ «нужен ли переспам» |
| llms.txt | GEO-кластер SERP | упоминание в GEO-блоке |

---

## 3. Таблица фактов (цифры и нормы — только с URL)

| Факт | Источник | Дата источника | Можно в текст |
|------|----------|----------------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции; критерий — полнота ответа | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение → основная часть → заключение с понятным следующим шагом | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику анализируют через Яндекс Вордstat и смежные инструменты; важна частотность по региону | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Не гнаться за максимумом вхождений — материал должен закрывать потребности пользователя | [Яндекс — семантическое ядро](https://direct.yandex.ru/base/articles/semanticheskoe-yadro-sajta) | 2026 | да |
| Кластеризация — группировка ключей по смыслу; под кластер — отдельная страница/блок | [Яндекс — семантическое ядро](https://direct.yandex.ru/base/articles/semanticheskoe-yadro-sajta) | 2026 | да |
| Ключи вписывают органично; польза для людей важнее роботов | [Яндекс — SEO услуги](https://direct.yandex.ru/base/articles/seo-prodvizhenie-sajta-uslug) | 2026 | да |
| Абзацы лучше короткие; списки улучшают восприятие | [Яндекс — SEO-копирайтинг](https://direct.yandex.ru/base/articles/chto-takoe-seo-kopirayting-i-kak-napisat-seo-tekst) | 2026 | да |
| После каждого H2 в сильных гайдах сразу дают содержательный ответ на подтему | [1ps.ru — SEO 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Главный ключ — H1, первый абзац, 1–2 H2, title и description; LSI — по тексту | [1ps.ru — SEO 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| Плотность информации важнее длины; ответ — как можно раньше в тексте | [FireSEO — SEO 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| Для AI-выдачи — атомарные, самодостаточные ответы; H2/H3, списки, FAQ | [FireSEO — SEO 2026](https://fireseo.ru/blog/kak-pravilno-napisat-seo-optimizirovannyj-tekst-v-2026-godu/) | 2026 | да |
| Лид: прямой ответ в первых 2–3 предложениях; отсюда часто берут быстрый ответ | [Seotika — SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| Иерархия H1 → H2 → H3 без пропуска уровней | [Seotika — SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| Главная задача — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| Title ~65 знаков с ключом и триггером (чек-лист, инструкция) — отраслевой ориентир | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| H1 не дублирует Title дословно | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Schema Article/FAQPage поддерживает сниппет и структуру | [Pikapuka — гайд](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| GEO — оптимизация под генеративные ответы; цель — цитирование, не замена SEO | [Habr — GEO](https://habr.com/ru/articles/1081126/) | 2026 | да |
| Для локального RU: Алиса опирается на классический топ Яндекса — SEO остаётся фундаментом GEO | [Habr — GEO](https://habr.com/ru/articles/1081126/) | 2026 | да |
| Snippet-First: начало блока H2 — резюме 1–3 предложения, отвечающее на вопрос раздела | [PW Agency — GEO контент](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 2026 | да |
| Абзацы 3–7 строк, одна законченная мысль — удобнее для цитирования ИИ | [PW Agency — GEO контент](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 2026 | да |
| Проблемные SEO-тексты у Яндекса: запросный спам, переоптимизация, скрытый текст (вторичный пересказ документации) | [vebdisain.ru — SEO Яндекс](https://vebdisain.ru/seo-i-veb-dizajn/seo-v-yandekse/kak-pisat-seo-teksty) | 29.08.2026 | да* |

\* Формулировка про нарушения — через пересказ vebdisain; в тексте B01 лучше опираться на канон [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) про естественность и пользу.

**Не использовать:** «+140% трафика» (Pikapuka); «60% прироста GEO от текста» (GenOptima via sergeisivkov — без первичника в fact-bank); «AI-поиск >20% трафика к концу 2026» (aksanov.digital — прогноз без верификации); любые показы Wordstat без MCP.

**Объём статьи Excalibur (редакция, не SERP):** 8 500–9 500 знаков текста — `shared/quality-blog.md`.

---

## 4. Угол статьи (практика, дифференциация)

**Главный угол:** SEO-статья 2026 = **longread, который дочитывают люди**, и который **можно процитировать** в нейроответах. Один workflow: интент → структура → инфостиль → FAQ/schema → GEO-чанки → чеклист.

**Отличие от SERP:**

- Официальный Яндекс — без GEO-слоя; GEO-гайды — без «писать с нуля для блога».
- H1 B01 («**которые читают люди**») — связка читабельности (абзацы, lead, «острова смысла») с техникой SEO/GEO.
- Режим **B:** сама статья B01 — эталон формата (FAQ 5–7, BlogPosting + FAQPage, перелинковка на `/`).

**Tone:** практично, по-человечески; без эмодзи и корпоративной воды (`site-brief`).

**H2-каркас (из карточки B01):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread  
3. FAQ и schema  
4. Чеклист перед публикацией  

Внутри блоков: Wordstat/семантика, Title/Description, E-E-A-T lite, llms.txt, robots/AI-краулеры — без раздувания числа H2 верхнего уровня.

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи (~40–60 слов) | Lead | «SEO-статья — …» |
| Определение GEO (~40–60 слов) | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational подзаголовки | FAQ / H3 | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 | Конец | Ответ 2–4 предложения, действие |
| Snippet-first под каждым H2 | Body | 1–3 предложения сразу под H2 |
| Island test | QA | Блок автономен |
| BlogPosting + FAQPage | schema role | JSON-LD, не в body |
| datePublished / dateModified | meta | 2026-10-02 (run date) |
| llms.txt | GEO-блок | Зачем блогу |
| internal link | `/` | из карточки |
| cover alt | cover | `cover_scene_hint` из карточки |

**AI-формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи».

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); для how-to в Excalibur — 8 500–9 500 знаков при полноте ответа.  
2. **Что такое GEO в SEO?** — дополнение к SEO: цитирование в AI-ответах при индексируемом структурированном контенте.  
3. **Нужен ли переспам ключей в 2026?** — нет; органичные вхождения + LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (~65 зн.), H1 на странице; не дублировать.  
5. **Какие schema для блога?** — BlogPosting + FAQPage.  
6. **Что такое llms.txt?** — сигнал для AI-краулеров; не замена sitemap.  
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Цифры только из §3; Wordstat-показы — после MCP.  
- Не копировать 13 шагов olegweb / 7 разделов Pikapuka 1:1.  
- Без эмодзи; без VPN/обходов.  
- `example.com` / `/` по карточке для internal links.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| utility_verdict PASS + action_outline | ✅ |
| SERP ≥ 5 конкурентов (WebSearch 2026-10-02) | ✅ |
| Таблица фактов ≥ 15 строк с URL | ✅ |
| LSI (Wordstat — pending MCP) | ⚠️ LSI из SERP |
| GEO hooks + FAQ | ✅ |
| Режим B | ✅ |

**Writer:** вход — этот файл, `research-context.json`, карточка B01, `site-brief.md`, `shared/excalibur-article-writing-contract.md`.
