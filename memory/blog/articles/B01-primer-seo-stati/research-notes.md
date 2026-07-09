# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how_to / longread-эталон)  
**research_date:** 2026-07-07  
**disclaimer:** Все даты, версии и статистика проверены на 2026-07-07 (2026 год).

---

## 1. Utility gate

```bash
python3 scripts/excalibur_blog_utility_gate.py --topic-id B01
# → PASS (search_intent: how_to, article_mode: B)
```

**utility_verdict:** PASS

**reader_outcome:** Читатель пройдёт полный цикл от запроса до публикации: проверит спрос, разберёт SERP, соберёт семантику, построит структуру H1–H3, напишет текст с прямым ответом в lead, добавит E-E-A-T, FAQ/schema и GEO-чанки — и проверит материал по чеклисту перед публикацией.

**action_outline (8 шагов для writer):**

1. **Интент и спрос:** определить тип запроса (how_to); в Wordstat проверить primary «как писать seo статьи» и 3–5 LSI; зафиксировать кластер из 3–5 смысловых групп.
2. **SERP-разбор:** открыть топ-5 по «как писать seo статьи 2026»; выписать H2 конкурентов; найти пробел (читабельность + GEO в одном workflow).
3. **Структура:** H1 = главный запрос; 4–6 H2 по карточке темы; после каждого H2 — прямой ответ в первом абзаце; FAQ 5–7 вопросов в конце.
4. **Lead 40–60 слов:** определение + что получит читатель; без «в этой статье мы рассмотрим».
5. **Черновик по блокам:** один H2 = одна подзадача + рекомендация «делать / не делать»; абзацы 3–5 строк; списки и таблицы там, где упрощают действие.
6. **E-E-A-T lite:** автор с ролью; минимум один проверяемый факт со ссылкой; без выдуманных кейсов и процентов.
7. **Техника:** Title (~60 знаков) ≠ H1; Description 140–160 знаков; alt у изображений; 2–3 внутренние ссылки; JSON-LD BlogPosting + FAQPage (в schema, не в body).
8. **GEO-слой и финал:** атомарные чанки (island test); опционально llms.txt; чеклист 15+ пунктов перед публикацией; объём longread 8 500–9 500 знаков.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` недоступен в текущей Cloud-среде (MCP не подключён). Точные показы/мес **не получены**. Обновите токен и MCP через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Что сделать writer/редактору вручную:** в [wordstat.yandex.ru](https://wordstat.yandex.ru/) проверить primary и secondary; использовать операторы `"как писать seo статьи"` и `!как !писать !seo !статьи` для точной частотности ([PromoPult — гайд Wordstat](https://blog.promopult.ru/seo/yandeks-wordstat.html)).

### Экспертная семантическая карта (LSI из SERP + WebSearch, без выдуманных показов)

| Кластер | LSI-фразы для вкрапления |
|---------|--------------------------|
| Действие | как написать seo статью, как писать seo тексты, пошаговая инструкция seo |
| Формат | seo текст для блога, seo текст для сайта, seo копирайтинг, структура seo статьи |
| Семантика | семантическое ядро, wordstat, lsi запросы, ключевые слова без переспама |
| Качество | e-e-a-t, читаемость, тексты для людей, переспам ключей |
| Техника | title description, meta-теги, h1 h2 h3, внутренняя перелинковка, alt текст |
| GEO / AI | geo оптимизация статьи, ai seo, llms.txt, schema.org faqpage, нейропоиск |

**SEO-стратегия:** primary «как писать seo статьи» — в H1, lead, Title; «seo текст для блога» — во 2-м H2; «geo оптимизация статьи» — в блоке SEO+GEO; faq_hints («сколько символов», «что такое geo в seo») — в FAQ.

---

## 3. SERP-обзор (WebSearch Cursor, 07.07.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Не копировать |
|---|-----|-----|-----------------|------------------|---------------|
| 1 | [direct.yandex.ru/.../seo-tekst](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | 5 шагов workflow; примеры плохо/хорошо; Wordstat; естественность ключей; 3–5 строк в абзаце | Нет GEO/AI-слоя; CTA Директа | Блок про Директ; «что такое SEO» без actionable шагов |
| 2 | [olegweb.ru/.../kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм (13 шагов) | Интент → SERP → структура → WordPress → мета → перелинковка | Длинный narrative; GEO вторичен | 13 H2 1:1; WP-специфика как обязательная |
| 3 | [1ps.ru/.../seo-tekstyi-2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | Wordstat-кластеры 3–5 групп; E-E-A-T; Featured Snippet | Перегруз ИИ-инструментами; agency tone | Обещания «топ за N недель» без источника |
| 4 | [pikapuka.com/.../kak-napisat-seo-tekst](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Чек-лист longread | Semantics → E-E-A-T → Schema Article+FAQ | Непроверенные кейсы (+140% трафика) | Кейсы без URL; 7 разделов 1:1 |
| 5 | [dobromarketing.ru/kak-pisat-seo-teksty](https://dobromarketing.ru/kak-pisat-seo-teksty/) | Гайд «для людей и роботов» | Близкий intent к H1 B01 | Мало GEO/schema | Thin checklist |
| 6 | [gracie.digital/.../kontent-kotoryj-chitayut-lyudi](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | GEO+SEO практика (июнь 2026) | 40–60 слов lead; факты каждые 150–200 слов; island H2/H3; чек-лист GEO | Agency CTA; Brandlight 70%→20% — вторичный источник | Коммерческий аудит в конце |
| 7 | [action-market.ru/.../seo-kopirajting](https://action-market.ru/blog/marketing/kontent-marketing/seo-kopirajting-kak-pisat-teksty-kotorye-chitayut-lyudi-i-nahodyat-poiskoviki/) | Структура + E-E-A-T | Перевёрнутая пирамида; H2-каркас how_to | Мало техники публикации | Декоративные H2 без действия |
| 8 | [hozyindachi.ru/.../novye-pravila](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | Правила 2026 | 7 шагов workflow; FAQ для сниппета | Generic SEO-вода | «Новые правила» без таблицы фактов |

**Паттерн SERP:** топ — longread «полный гайд 2026» с Wordstat, E-E-A-T, чек-листом. Отдельный кластер — GEO-лонгриды. **Пробел:** мало материалов, где **читабельность** (инфостиль, island test) и **единый workflow SEO→GEO** даны как одна инструкция с чеклистом перед публикацией — это угол B01.

**Intent:** how_to — пользователь хочет **систему действий**, не определение «что такое SEO-текст».

---

## 4. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Пошаговый workflow: тема → семантика → структура → текст → оптимизация | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Прямой ответ на главный вопрос — в первых **40–60 словах** блока | [Gracie Digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| GEO-контент: статистика/конкретика примерно каждые **150–200 слов** со ссылкой на источник | [Gracie Digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| Каждый H2/H3 должен быть понятен **в отрыве** от остального текста (island) | [Gracie Digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| Title — до **60** символов с основным запросом; Meta Description — **140–160** символов | [YoSiteUp — AI SEO Workflow 2026](https://yositeup.com/ru-ua/blog/ai-seo-workflow-2026-research-to-publication) | 2026 | да |
| Для how-to longread ориентир **2500–3000 слов** при полноте ответа (EN-гайд; адаптировать под RU longread 8,5–9,5k знаков) | [YoSiteUp — AI SEO Workflow 2026](https://yositeup.com/ru-ua/blog/ai-seo-workflow-2026-research-to-publication) | 2026 | да (как ориентир объёма) |
| E-E-A-T: Experience, Expertise, Authoritativeness, Trustworthiness — критерии качества контента Google | [Brainbox — SEO-тексты 2025](https://brainbox-marketing.ru/blog/kak-pisat-seo-teksty/) | 2025 | да |
| H1 один раз; иерархия H2 → H3 без пропусков уровней | [Brainbox — SEO-тексты 2025](https://brainbox-marketing.ru/blog/kak-pisat-seo-teksty/) | 2025 | да |
| Основной ответ — в начале (перевёрнутая пирамида); далее детали и примеры | [Action Market — SEO-копирайтинг](https://action-market.ru/blog/marketing/kontent-marketing/seo-kopirajting-kak-pisat-teksty-kotorye-chitayut-lyudi-i-nahodyat-poiskoviki/) | 2026 | да |
| GEO (Generative Engine Optimization) — оптимизация для цитирования в ответах AI; Schema.org — базовый слой | [CPA.live — разметка AI-видимости](https://cpa.live/articles/razmetka-sajta-dlya-ai-vidimosti/) | 2026 | да |
| llms.txt — карта приоритетов для LLM в корне `/llms.txt` (Markdown); **не заменяет** robots.txt | [CPA.live — разметка AI-видимости](https://cpa.live/articles/razmetka-sajta-dlya-ai-vidimosti/) | 2026 | да |
| Google заявил: **«We currently have no plans to support LLMs.txt»** — приоритет Schema.org | [Shipmint — llms.txt vs Schema](https://shipmint.kz/blog/llms-txt-schema-org-vidimost-dlya-ai-poiska) | 2025–2026 | да |
| JSON-LD — предпочтительный формат разметки для AI-парсинга | [Predicta Digital — GEO 2026](https://predictadigital.com.au/blog/llms-txt-mcp-schema-geo-2026/) | 2026 | да |
| Keyword stuffing в GEO-контексте работает **хуже** baseline (≈ −10%) | [arxiv.org/html/2311.09735](https://arxiv.org/html/2311.09735) | 11.2023 | да |
| Главная задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| Семантику группируют в **3–5** смысловых кластеров перед структурой H2 | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |

**fact-bank.md:** прямых фактов по SEO-письму нет — использовать только таблицу выше.

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «overlap Google/AI 70%→20%» без оговорки «по оценке Brandlight, цит. Gracie»; «llms.txt обязателен» — противоречит Google/Shipmint.

---

## 5. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Дифференциация:**
- Яндекс — канон SEO без GEO-слоя.
- GEO-гайды не учат писать текст с нуля.
- H1 «которые читают люди» слабо раскрыт в SERP — наш фокус: **читабельность как SEO-фактор** + техника.

**H2-каркас (из blog-topics.md + research):**
1. Зачем SEO и GEO в одной статье (не два проекта)
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD вне body)
4. Чеклист перед публикацией (15–20 пунктов)

**Объём:** 8 500–9 500 знаков текста (quality-blog). **Tone:** практично, без корпоративной воды и эмодзи.

---

## 6. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | H2 «SEO + GEO» | «GEO — …» |
| Island test | Каждый H2 | Первое предложение = тезис |
| FAQ 5–7 | Конец | Короткие ответы-действия |
| Schema handoff | Не в body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Опционально, не приоритет vs Schema |
| Internal link | Из карточки | На `/` |

**Целевые формулировки:** «как писать seo статьи», «seo текст для блога», «geo оптимизация статьи», «сколько символов в seo статье», «что такое geo в seo».

---

## 7. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI; переспам вреден (Яндекс, Princeton GEO).
4. **Чем Title отличается от H1?** — Title для сниппета (~60 знаков), H1 — на странице; не дублировать дословно.
5. **Какие schema нужны для SEO-статьи блога?** — BlogPosting (или Article) + FAQPage.
6. **Что такое llms.txt и нужен ли он блогу?** — опциональная карта для LLM; Schema.org важнее; Google не поддерживает llms.txt как стандарт.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, island test, читабельность.

---

## 8. Риски для writer

- Не выдумывать показы Wordstat — MCP недоступен.
- Не копировать Pikapuka/olegweb 1:1.
- Цифры только из таблицы фактов §4.
- Без эмодзи в article.html.
- CTA ≤ 3; не подменять пользу.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | ✅ PASS |
| utility_verdict + reader_outcome + action_outline | ✅ |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (LSI из SERP) |
| Таблица фактов с URL | ✅ (20 фактов) |
| GEO hooks + FAQ 5–7 | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
