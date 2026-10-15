# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата)  
**research_date:** 2026-10-08  
**disclaimer:** Все даты, версии и статистика проверены на 08.10.2026 (2026 год).

**Utility gate (topic):** PASS (`search_intent: how_to`, `article_mode: B`)

---

## 1. SERP-обзор (WebSearch, 08.10.2026)

Источник: нативный WebSearch + сверка с `research-serp.json`. Приоритет — свежие гайды 2026 с пошаговой структурой.

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: интент, семантика (Wordstat/Вебмастер), H1–H4, абзацы 3–5 строк, alt, Title/Description; «нет универсального объёма» | Нет GEO/нейровыдачи; CTA Директа в конце | Блоки про запуск Директа как основной CTA; копировать структуру 1:1 |
| 2 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Практик, 7 шагов (2026) | Чёткий workflow: запросы → ТОП → структура → текст → мета → релевантность → публикация; чек-лист в конце | Мало GEO; личный tone «как я пишу» | Дублировать 7 H2 без дифференциации |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (2026) | E-E-A-T, Wordstat/Serpstat, чек-лист, Schema Article+FAQPage, Title ~65 знаков | Кейсы с непроверяемыми %; перегруз «agency expertise» | Непроверенные «+140% трафика»; клон 7-разделной структуры |
| 4 | [articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | AI+SEO гайд (2026) | Полный цикл семантика → публикация; акцент на AI-выдачу | Уклон в генерацию через ИИ без human-in-the-loop | Обещания «топ без редактуры» |
| 5 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread + ИИ (2026) | Правило «после каждого H2 — содержательный ответ»; LSI без насильного вписывания | Длинный sales-narrative про ИИ | Копировать блоки про «полный цикл на нейросети» как единственный путь |
| 6 | [seotika.ru/kak-pisat-seo-stati](https://seotika.ru/kak-pisat-seo-stati/) | SEO-агентство (2026) | Lead = ответ в первых 100 словах; H2 как вопросы; таблицы/FAQ; GEO/AEO в контексте | Ориентир «1500–3000 слов» и «плотность 1–2%» без первичника для всех ниш | Использовать плотность ключей как жёсткую норму |
| 7 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Короткий принципиальный гайд | «Полный ответ на одной странице»; LSI; поведенческий сигнал (не возвращаться в поиск) | Мало чек-листа, schema, GEO | Формулировки «просто следуй принципам» без шагов |
| 8 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | WordPress-практик, 13 шагов (2026) | От спроса до индексации; мета, alt, внутренние ссылки, чек перед публикацией | Перегруз шагами WP без GEO-слоя | 13 H2 верхнего уровня 1:1 |

**Паттерн SERP (октябрь 2026):** доминируют «полный гайд 2026» (7–13 шагов) + отдельный кластер «SEO + ИИ». H1 «которые читают люди» слабо закрыт — возможность Excalibur: **читабельность + GEO-чанки** в одном workflow, не «ещё один список ключей».

**Intent:** `how_to` — собрать семантику → outline → lead → текст → мета → FAQ/schema → чеклист. Вторичный: связать **SEO-текст для блога** и **geo оптимизация статьи** без путаницы с локальной «гео-SEO».

**Пробел для Excalibur:** единый **action-first** гайд «от Wordstat до BlogPosting+FAQPage» с **чеклистом 15–18 пунктов** и режимом B (сама статья = эталон 8,5–9,5k знаков).

---

## 2. Яндекс Wordstat (MCP `user-mcp-kv`, 08.10.2026)

**⚠️ WORDSTAT MCP WARNING:** сервер `user-mcp-kv` / инструмент `wordstat_get_top_requests` **не подключён** в этом Cloud Agent run (namespace отсутствует в каталоге MCP). Точные **показы/мес** по фразам **не получены** — цифры ниже **не заполнялись**, чтобы не искажать спрос.

**Запросы для повторного прогона (когда MCP доступен):**

| Запрос | Роль |
|--------|------|
| как писать seo статьи | primary_query |
| seo текст для блога | secondary_1 |
| geo оптимизация статьи | secondary_2 |
| как написать seo статью | LSI (частый синоним в SERP) |
| seo копирайтинг как писать | LSI |
| структура seo статьи | LSI (информационный хвост) |
| сколько символов в seo статье | FAQ (из карточки B01) |
| что такое geo в seo | FAQ (из карточки B01) |

**Обновление токена (при 401 от API):**  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### LSI для writer (из SERP + secondary, без частот)

- как писать seo статьи / seo текст для блога / seo статья 2026  
- семантическое ядро, Wordstat, кластеризация, интент запроса  
- структура longread, H1 один, H2–H3, lead-абзац, island test  
- Title, Description, alt-текст, внутренняя перелинковка  
- FAQ, BlogPosting, FAQPage, JSON-LD  
- geo оптимизация статьи, generative engine optimization, нейровыдача, answer-first  
- E-E-A-T lite, expert content, human-in-the-loop (при упоминании ИИ — из fact-bank)  
- чеклист перед публикацией, релевантность, переспам  

**SEO-стратегия (до появления цифр Wordstat):** primary в H1/lead; secondary «seo текст для блога» — в блок про формат блога; «geo оптимизация статьи» — отдельный H2 «SEO + GEO в одной статье», не в title целиком (риск смешения с site-level GEO B04).

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы SEO-текста — ориентир **3–5 строк**; списки для перечислений | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| **H1 — один** на страницу; H2–H4 для смысловых блоков | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают **смысл и полезность**, не плотность ключей; переспам вреден | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в **Яндекс Вордстат** и **Яндекс Вебмастер** | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на **сниппет и кликабельность** | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| К каждому изображению — **alt-текст**; файлы — латиницей (пример в гайде) | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантическое ядро: Wordstat, подсказки, кластеризация по смыслу | [Яндекс — семантическое ядро](https://direct.yandex.ru/base/articles/semanticheskoe-yadro-sajta) | 2026 | да |
| Контент должен быть **полезен людям в первую очередь**, ключи — органично | [Яндекс — SEO услуги](https://direct.yandex.ru/base/articles/seo-prodvizhenie-sajta-uslug) | 2026 | да |
| SEO-статья в ТОП закрывает **интент**; lead — прямой ответ в первых ~**100 словах** | [Seotika — SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да (агентский источник) |
| Title — до **~60 символов**, description **140–160** (ориентир для рунета) | [Pawetta — SEO-текст](https://pawetta.com/baza/seo-tekst-kak-pisat/) | 2026 | да (ориентир, не SLA) |
| Информационная статья — ориентир **4000–8000 знаков** vs конкуренты в SERP | [Pawetta — SEO-текст](https://pawetta.com/baza/seo-tekst-kak-pisat/) | 2026 | да (ориентир по типу страницы) |
| GEO (Generative Engine Optimization) — оптимизация видимости в **ответах генеративных поисковиков** | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| GEO-bench: **10 000** запросов; методы с цитатами/статистикой — до **+40%** visibility (Position-Adjusted Word Count) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| На Perplexity.ai — улучшение visibility до **37%** (эксперименты авторов) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Keyword stuffing в GEO-экспериментах — **хуже baseline** (~−10%) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Главная задача статьи — **полный ответ**; возврат в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| **51%** маркетологов используют нейросети для **аналитики и оптимизации**, не для слепой штамповки | [fact-bank → mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026-06-11 | да |
| Human-in-the-loop: автономные системы завершают менее **2,5%** сложных неструктурированных задач без человека | [fact-bank → mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026-06-11 | да |

**Не использовать без оговорки:** «плотность ключей 1–2%» (Seotika); «+140% трафика за 3 недели» (Pikapuka); любые показы Wordstat без MCP/API.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **longread для человека**, упакованный для **нейропоиска**: один workflow от Wordstat до чеклиста; H1-карточки «**которые читают люди**» = читабельность (структура, lead, короткие абзацы, «острова смысла») + техника (мета, FAQ, schema), а не переспам.

**Почему отличается от конкурентов:**

- Яндекс — канон SEO без GEO-слоя; GEO-гайды (B04) — не учат писать текст с нуля.  
- Агентские лонгриды — E-E-A-T-кейсы и CTA; у нас — **DIY-инструкция + чеклист 15–18 пунктов**.  
- ИИ-гайды — «генерация без редактуры»; Excalibur — **human-in-the-loop** (fact-bank).  
- Режим **B**: эта статья — **эталон** пайплайна Excalibur (research → writer → QA → schema).

**Tone (site-brief):** практично, по-человечески; без корпоративной воды и эмодзи в `article.html`.

**H2-каркас (из `blog-topics.md` + research):**

1. Зачем SEO и GEO в одной статье (не два проекта)  
2. Структура longread: H1–H3, lead, списки, таблицы  
3. FAQ и schema — зачем и как (JSON-LD вне body)  
4. Чеклист перед публикацией (15–18 пунктов)  

**Внутри блоков (не обязательно отдельные H2 верхнего уровня):** Wordstat/кластер, Title/Description, E-E-A-T lite, llms.txt (упоминание), перелинковка на `/`.

---

## 5. Черновик чеклиста (15–18 пунктов для writer)

1. Primary query и 5–10 secondary зафиксированы (Wordstat/Вебмастер).  
2. ТОП-5–10 SERP разобран: формат, H2, пробелы.  
3. Outline: один H1, 4–7 H2, H3 по необходимости.  
4. Lead: прямой ответ + польза в первых 2–3 предложениях.  
5. После каждого H2 — содержательный абзац-ответ (не «вода»).  
6. Абзацы 3–5 строк; списки/таблицы там, где перечисления.  
7. Ключи естественно: H1, lead, 1–2 H2, Title/Description — без переспама.  
8. Title (~60–65 знаков) **≠** H1.  
9. Description с обещанием и ключом.  
10. Alt у каждого значимого изображения.  
11. FAQ **5–7** пар; ответы 2–4 предложения, action-first.  
12. BlogPosting + FAQPage JSON-LD (текст FAQ = видимый HTML).  
13. Внутренняя ссылка на `/` (карточка темы).  
14. Island test по каждому H2.  
15. Проверка ссылок, дат, fact-bank / research-notes.  
16. GEO: определение термина 40–60 слов + answer-first в lead.  
17. datePublished / dateModified актуальны.  
18. Объём body **8 500–9 500** знаков (quality-blog), если SERP не требует иначе.

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы (Яндекс); ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.  
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + тематические слова (Яндекс + GEO-bench).  
4. **Чем Title отличается от H1?** — Title для сниппета, H1 на странице; не дублировать.  
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.  
6. **Что такое llms.txt и нужен ли он блогу?** — опциональный сигнал для AI-краулеров; не замена sitemap/robots.  
7. **Как проверить статью перед публикацией?** — чеклист из раздела 5 + link-verify + slop/utility gate.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ hints | «Сколько символов…», «Что такое GEO…» |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema handoff | Не в HTML body | BlogPosting + FAQPage |
| Цитаты/цифры с URL | Тело | Princeton +40%, keyword stuffing −10% — с оговоркой «исследование 2023» |
| Internal link | Из карточки | `/` |
| cover_scene_hint | Cover | редактор, ноутбук, блокнот |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи».

---

## 8. Риски для writer

- Не выдумывать **показы Wordstat** — MCP не был доступен на research; Fact Check Box не ссылаться на «подтверждено Вордстатом» с цифрами до повторного research.  
- Не копировать Pikapuka/olegweb структуру 1:1.  
- Объём: 8 500–9 500 знаков body.  
- Без эмодзи в article.html.  
- Цифры только из раздела 3 и fact-bank.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику в Wordstat, построит outline longread под интент, напишет lead и блоки H2 с FAQ, заполнит Title/Description, подготовит BlogPosting+FAQPage и пройдёт чеклист из 15–18 пунктов перед публикацией — с GEO-чанками в той же статье.

**action_outline:**

1. **Зафиксировать запрос:** primary «как писать seo статьи» + secondary из карточки; выписать 5–10 фраз из Wordstat (когда MCP доступен) или из подсказок/ТОП SERP.  
2. **Разобрать интент и ТОП-5 SERP:** формат, заголовки, объём, чего не хватает (читабельность, GEO).  
3. **Собрать outline:** H1 один; H2 по карточке B01; под каждым H2 — тезис-ответ.  
4. **Написать lead** (350–500 знаков): определение SEO-статьи + обещание workflow.  
5. **Написать тело:** абзацы 3–5 строк, списки/таблица SEO vs GEO; ключи естественно; блок «SEO + GEO в одной статье».  
6. **Добавить FAQ 5–7** и мета (Title ≠ H1, Description).  
7. **Подготовить schema-handoff:** BlogPosting + FAQPage (writer/schema-агент).  
8. **Пройти чеклист** (раздел 5) + island test; при использовании ИИ — human-in-the-loop правки.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (без выдуманных цифр) |
| Таблица фактов с URL | ✅ (18) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| Чеклист 15–18 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов с оговоркой по Wordstat — в Fact Check Box не утверждать точные показы до повторного вызова MCP. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
