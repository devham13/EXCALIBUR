# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата блога)  
**research_date:** 2026-10-04  
**disclaimer:** Все даты, версии и статистика проверены на 2026-10-04 (2026 год).

---

## 1. SERP-обзор (WebSearch Cursor, 04.10.2026 + research-serp.json)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: семантика → структура → текст → оптимизация; H1 один; переспам вреден; Вордстат; примеры «плохо/хорошо» | Нет GEO/нейропоиска; CTA Директа | Коммерческий блок Директа; копировать H1–H4 без GEO-слоя |
| 2 | [articleai.ru/.../kak-napisat-seo-statyu-v-2026...](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Агентский how-to 2026 | Пошаговый цикл до публикации; AI-выдача в подаче | Перегруз «ИИ-контентом»; мало «читабельности для людей» | Структуру 1:1; обещания «в топ за N дней» без источника |
| 3 | [pikapuka.com/.../kak-napisat-seo-tekst-samomu...](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Longread + E-E-A-T | Чек-лист 10 шагов; Title ~65 знаков; Article + FAQPage | Кейсы с непроверенными %; agency-tone | «+140% трафика» и копия 7 разделов |
| 4 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 7 шагов (обнов. 10.07.2026) | Чёткий цикл копирайтера; анализ ТОП ≥1 ч; «объём задаёт SERP» | Мало GEO/schema; продаёт курсы | Копировать только структуру шагов без дифференциации |
| 5 | [seotika.ru/kak-pisat-seo-stati/](https://seotika.ru/kak-pisat-seo-stati/) | Гайд агентства (21.06.2026) | Таблица «обычный текст vs SEO»; кластеризация; FAQ в SERP-паттерне | Ориентир 1500–3000 слов и плотность 1–2% — спорно для RU longread | Жёсткие «нормы объёма» без оговорки про SERP |
| 6 | [serpjet.ru/.../chek-list-idealnoj-seo-stati-v-2026...](https://serpjet.ru/blog/chek-list-idealnoj-seo-stati-v-2026-ot-semantiki-do-cta-zamenit-seo-spetsialista-4847/) | Чек-лист 2026 | Кластеры по интенту; промпт под нейросеть как ТЗ | Фокус на автоматизацию агентства, не на автора-новичка | Sales-narrative RAG/агентства |
| 7 | [divitio.ru/.../kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | Пошаговая инструкция | 5 шагов + финальный чек-лист; Title/Description цифры | Узкий бренд, мало GEO | — |
| 8 | [habr.com/ru/articles/1022684/](https://habr.com/ru/articles/1022684/) | SEO & GEO чеклисты (13.04.2026) | Таблицы SEO+GEO; FAQPage/HowTo для AI; answer-first | Часть метрик без первичника («+47% цитирования») | Цифры из Habr без верификации |
| 9 | [www.meta-journal.ru/2026/06/19/primer-seo-stati/](https://www.meta-journal.ru/2026/06/19/primer-seo-stati/) | Близкий H1 | Совпадение с нашим slug/H1 — риск каннибализации | — | Не дублировать title/H1 дословно с соседним URL |

**Паттерн SERP (окт. 2026):** доминируют «полный гайд / пошаговая инструкция 2026», E-E-A-T, семантика, чек-листы. Отдельный кластер — GEO-лонгриды (secondary «geo оптимизация статьи»). Запрос «как писать seo статьи» — **informational how_to**; пользователь ждёт воспроизводимый процесс, а не определение «что такое SEO-текст».

**Intent:** how_to — семантика → анализ выдачи → структура → текст → мета → FAQ/schema → проверка. Вторичный: **seo текст для блога** (формат и читабельность), **geo оптимизация статьи** (упаковка под нейроответы).

**Пробел для Excalibur B01:** мало материалов, где **читабельность = SEO** (короткие абзацы, lead, «острова смысла») **и** один чек-лист на SEO+GEO без раздувания про «контент-завод на ИИ». H1 «которые читают люди» почти не раскрыт у конкурентов.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` не подключён в среде Cloud Agent (инструмент `wordstat_get_top_requests` недоступен). Точные **показы/мес** не получены — **цифры спроса в статье не выдумывать**.

При восстановлении MCP проверить OAuth:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Семантика для writer (экспертно, без частот — до появления Wordstat)

| Тип | Фразы |
|-----|--------|
| Primary | как писать seo статьи |
| Secondary (карточка) | seo текст для блога, geo оптимизация статьи |
| LSI (SERP + конкуренты) | семантическое ядро, кластеризация запросов, структура h1 h2 h3, title description, e-e-a-t, lsi-слова, чек-лист seo статьи, faq schema, blogposting, нейровыдача, answer-first, переспам ключей, яндекс вордстат, анализ топ 10 |
| FAQ-хвост (карточка) | сколько символов в seo статье; что такое geo в seo |

**SEO-стратегия:** primary в H1 и lead; secondary — отдельные H2 или подблоки; long-tail — FAQ.

---

## 3. Таблица фактов (≥15, только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику подбирают через Яндекс Вордстат (и смежные инструменты) | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-текст в 2026 — полезный текст, структура и словарь под запрос и его окружение, не «ключ через два абзаца» | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| Перед написанием анализируют ТОП-10: тип страницы, объём, структура, форматы (таблицы, FAQ) | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| «Какой объём нужен» — ориентир медиана конкурентов в SERP, не абстрактная норма | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| Абзацы 3–5 строк; перечисления — списками; первый экран отвечает на запрос | [SEO Школа — гайд 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 10.07.2026 | да |
| SEO-статья в ТОП закрывает интент структурно; прямой ответ — в первых ~100 словах | [Seotika — гайд](https://seotika.ru/kak-pisat-seo-stati/) | 02.09.2026 | да |
| Один кластер запросов — одна страница; смешение информационного и коммерческого интента размывает релевантность | [Seotika — гайд](https://seotika.ru/kak-pisat-seo-stati/) | 02.09.2026 | да |
| Title — до ~60 символов, ключ в начале; Meta description — до ~155 символов | [Divitio — пошаговая инструкция](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| Главный ключ — H1, первый абзац и одно естественное вхождение ближе к концу | [Divitio — пошаговая инструкция](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да |
| В Wordstat для одной статьи часто выписывают 15–25 связанных фраз (от порога частотности по нише) | [Divitio — пошаговая инструкция](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да* |
| Google с августа 2023 сильно ограничил FAQ rich snippets для коммерческих/обычных сайтов | [Тригуб — FAQPage Schema](https://trigub.ru/seo-checklist/nastroit-faqpage-schema/) | 2026 | да |
| Для российского рынка FAQPage остаётся сигналом для Яндекс Нейро / Алисы AI (пары вопрос–ответ) | [Тригуб — FAQPage Schema](https://trigub.ru/seo-checklist/nastroit-faqpage-schema/) | 2026 | да |
| С 7 мая 2026 Google прекратил показ FAQ rich results в Search; тип Schema.org FAQPage остаётся, данные используют для понимания страницы | [Progress — SEO and GEO guide](https://www.progress.com/blogs/seo-and-geo-guide) | 2026 | да |
| Для GEO FAQPage в JSON-LD важен, т.к. LLM часто не исполняют JS для раскрывающихся FAQ | [Progress — SEO and GEO guide](https://www.progress.com/blogs/seo-and-geo-guide) | 2026 | да |
| GEO-оптимизация: FAQ с прямым ответом в первых ~30 словах; вопрос — формулировка частотного запроса | [GEO Scout — чек-лист 2026](https://geoscout.pro/ru/blog/geo-optimizaciya-pod-chatgpt-claude-perplexity-cheklist) | 2026 | да |
| На информационных страницах рекомендуют FAQ-блок (длинный хвост, SERP) | [Habr — SEO & GEO чеклисты](https://habr.com/ru/articles/1022684/) | 13.04.2026 | да |
| Title 50–60 символов, Description 150–160 — ориентир в SEO-чеклистах | [Habr — SEO & GEO чеклисты](https://habr.com/ru/articles/1022684/) | 13.04.2026 | да |
| Контент «answer-first»: ответ в первом абзаце | [Habr — SEO & GEO чеклисты](https://habr.com/ru/articles/1022684/) | 13.04.2026 | да |

\* Порог «от 50 показов» — рекомендация Divitio; в тексте формулировать как практику, не как правило Яндекса.

**fact-bank.md:** прямых фактов про SEO-копирайтинг нет — опираться на таблицу выше и site/llms контент блога.

**Не использовать без первичника:** «+140% трафика» (Pikapuka); «+35–70% / +47% к цитированию» (Habr без исследования); «плотность 1–2%» как универсальное правило (Seotika — только с оговоркой «ориентир агентства»).

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** один **workflow** «для людей и для выдачи»: интент → семантика → структура longread → текст с читабельностью → мета → **FAQ + schema** → **GEO-чанки** → **чек-лист 18+ пунктов** перед публикацией. SEO и GEO — не два проекта, а одна статья с двойной упаковкой.

**Три ключевых угла дифференциации:**
1. **Читабельность как ranking-signal:** короткие абзацы, lead 350–500 знаков, H2-«острова» — против «гайдов под ключи».
2. **SEO + GEO в одном чек-листе:** FAQPage/BlogPosting, answer-first, без отдельного «хайпового» GEO-лонгрида.
3. **Режим B — статья-эталон:** сама B01 демонстрирует формат (8,5–9,5k знаков, 5–7 FAQ, перелинковка на `/`).

**H2-каркас (карточка B01 + research):**
1. Зачем SEO и GEO в одной статье  
2. Структура longread (H1–H3, lead, списки, таблицы)  
3. FAQ и schema (JSON-LD, не дублировать JSON в body)  
4. Чек-лист перед публикацией (15–20 пунктов)

**Tone:** практично, по-человечески; без «в современном мире» и agency-case с выдуманными %.

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слov | Блок SEO+GEO | Generative Engine Optimization |
| Answer-first | Lead + каждый H2 | Первое предложение = тезис |
| FAQ 5–7 | Конец | 2–4 предложения, действие |
| Schema | meta/schema agent | BlogPosting + FAQPage |
| llms.txt | Упоминание 1 абзац | Сигнал для AI-краулеров, не замена sitemap |
| Internal link | Карточка | `/` |

**Целевые формулировки:** как писать seo статьи, seo текст для блога, geo оптимизация статьи, сколько символов в seo статье, что такое geo в seo.

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и медиана ТОПа; для how-to longread Excalibur — 8 500–9 500 знаков текста.  
2. **Что такое GEO в SEO?** — дополнение к SEO: цитирование в AI-ответах при той же полезной базе + структура.  
3. **Нужен ли переспам ключей в 2026?** — нет; естественные вхождения + LSI.  
4. **Чем Title отличается от H1?** — Title для сниппета (~50–60 знаков), H1 на странице; не дублировать дословно.  
5. **Какие schema для статьи блога?** — BlogPosting (Article) + FAQPage для блока вопросов.  
6. **Зачем FAQ, если Google убрал rich snippets?** — для понимания страницы и GEO (Яндекс Нейро, LLM без JS).  
7. **Как проверить статью перед публикацией?** — финальный чек-лист: семантика, мета, структура, FAQ, schema, ссылки, island-test.

---

## 7. Риски для writer

- Не выдумывать Wordstat-частоты до подключения MCP.  
- Не копировать Pikapuka/Seotika 1:1.  
- Объём: 8 500–9 500 знаков (`quality-blog.md`).  
- Min **5** нумерованных шагов + чеклист **10+** пунктов (utility gate статьи).  
- Цифры только из §3 или fact-bank.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель соберёт семантику под один интент, спроектирует структуру longread с lead и FAQ, напишет текст без переспама, оформит Title/Description, добавит BlogPosting + FAQPage для SEO и GEO, пройдёт чек-лист перед публикацией и отправит URL в Вебмастер для контроля.

**action_outline (8 шагов для writer):**

1. **Зафиксировать интент** (informational how-to) и один кластер: primary «как писать seo статьи» + secondary из карточки; отсечь коммерческие запросы.  
2. **Собрать семантику:** Вордстат/Вебмастер (когда MCP доступен), 15–25 LSI; таблица «запрос → H2/FAQ».  
3. **Разобрать ТОП-5–10:** формат, медиана объёма, обязательные H2, пробелы (читабельность, GEO).  
4. **Собрать outline:** один H1; H2 по подвопросам; lead 350–500 знаков с прямым ответом; таблица или список там, где в SERP есть формат.  
5. **Написать body:** абзацы 3–5 строк; ключи в H1, lead, 1× в конце; рекомендации «делать / не делать» в каждом H2.  
6. **Мета:** Title ~50–60 знаков (≠ H1), Description ~150–160; alt у изображений.  
7. **GEO-упаковка:** FAQ 5–7 с answer-first; атомарные H2; handoff schema — BlogPosting + FAQPage.  
8. **Чек-лист публикации:** island test, внутренние ссылки (2–3), schema/meta, отправка URL в Яндекс Вебmaster/GSC, план пересмотра через 2–4 недели.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы (скрипт) | PASS |
| SERP ≥ 3 конкурента | ✅ (9) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (21) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `memory/brief/site-brief.md`.
