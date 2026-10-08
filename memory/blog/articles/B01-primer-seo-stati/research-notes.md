# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-10-08  
**disclaimer:** Все даты, версии и статистика проверены на 08.10.2026 (2026 год).

**utility_gate (topic):** PASS (`scripts/excalibur_blog_utility_gate.py --topic-id B01`)

---

## 1. SERP-обзор (WebSearch, октябрь 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [seoshkola.com/.../kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Пошаговый гайд 2026 | 7 шагов от семантики до контроля после публикации; чек-лист; акцент «текст под запрос, не под ключи» | Мало GEO/нейропоиска; без связки «читаемость = поведение» | Длинные авторские истории вместо actionable блоков |
| 2 | [seotika.ru/kak-pisat-seo-stati](https://seotika.ru/kak-pisat-seo-stati/) | Агентский гайд ТОП | Lead 100 слов, H2 как вопросы, объём 1500–3000 слов для info, таблицы/FAQ | Цифры плотности ключей без первичника; перегруз «в ТОП» | Копировать 12-шаговую структуру 1:1 |
| 3 | [pawetta.com/baza/seo-tekst-kak-pisat](https://pawetta.com/baza/seo-tekst-kak-pisat/) | База знаний | Ориентиры объёма по типам страниц (знаки); Title ~60, Description 140–160; иерархия H1–H3 | Мало про AI-цитирование | Жёсткие нормы объёма без оговорки «зависит от SERP» |
| 4 | [olegweb.ru/.../kak-napisat-seo-statyu](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | WP-практик | 13 шагов до индексации; интент, SERP, WordPress-оформление | Длинный narrative; GEO — побочно | Весь WP-стек как обязательный для всех |
| 5 | [roiseo.ru/.../struktura-seo-stati-dlya-bloga](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | Шаблон блога | Модуль: ответ 40–70 слов → таблица → ошибки → чек-лист → FAQ | Узкий SEO-агентский tone | Thin template без workflow семантики |
| 6 | [b2b.yandex.ru/adv/edu/.../seo-tekst](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный RU-канон | H1 один раз; H2–H4 по смыслу; введение с пользой; ключи естественно | Нет GEO-слоя | — |
| 7 | [tapbox.ru/blog/geo-prodvizhenie](https://tapbox.ru/blog/geo-prodvizhenie) | GEO + SEO (сент. 2026) | Яндекс: ответы Алисы опираются на поиск; 46,5 млн/мес быстрыми ответами (апр. 2026); ЭПОС | Фокус GEO, не «как писать с нуля» | Продажа услуг агентства |
| 8 | [direct.yandex.ru/base/articles/seo-tekst](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Яндекс Директ (янв. 2026) | Wordstat, alt, мета, переспам вреден, абзацы 3–5 строк | CTA Директа | Коммерческий хвост |

**Паттерн SERP:** доминируют **7–13 шаговых гайдов 2026** (семантика → SERP → структура → текст → мета → публикация). Отдельный кластер — **GEO/AEO** (snippet-first, FAQ, schema). Пробел: мало материалов, где **H1 «которые читают люди»** = явный workflow **читабельность + SEO + GEO в одном longread** для B2B-блога без «набивки ключей».

**Intent:** `how_to` — собрать запросы, разобрать топ, собрать outline, написать lead и тело, оформить мета/FAQ/schema, проверить перед публикацией. Вторичный: **seo текст для блога**, **geo оптимизация статьи** в том же материале.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` недоступен в текущем окружении Cloud Agent (namespace не подключён). Вызов `wordstat_get_top_requests` не выполнен. **Точные показы в месяц не получены** — не использовать выдуманные частотности.

**Действие для пайплайна:** подключить MCP Wordstat в Cursor ([инструкция OAuth](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40)) и повторить запросы:

- `как писать seo статьи`
- `seo текст для блога`
- `geo оптимизация статьи`

**LSI для writer (из SERP и secondary_queries, без частотностей):**

- как написать seo статью, seo текст для сайта/блога, структура seo статьи, seo текст 2026  
- title description для статьи, переспам ключевых слов, LSI-слова, семантическое ядро  
- geo оптимизация статьи, snippet-first, FAQPage, BlogPosting, E-E-A-T, чек-лист перед публикацией  
- как писать для людей, инфостиль, поведенческие факторы (полнота ответа)

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Google продвигает контент, полезный **людям**, а не написанный «под ранжирование» | [Google Search Central — helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content?hl=ru) | актуально 2026 | да |
| Универсального объёма SEO-текста нет — зависит от темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир **3–5 строк**; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| **H1 — один** на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Переспам ключей **вреден**; важны смысл и полезность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в **Яндекс Вордстат** и Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение с пользой, основная часть по шагам, заключение со следующим действием | [Яндекс B2B — SEO-текст](https://b2b.yandex.ru/adv/edu/materials/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 2026 | да |
| Информационная статья — ориентир **4000–8000 знаков** (полнее конкурентов); гайд — от **10 000 знаков** | [Pawetta — SEO-текст 2026](https://pawetta.com/baza/seo-tekst-kak-pisat/) | 2026 | да (как ориентир типа страницы) |
| Title до **~60 символов**, description **140–160** с ключом | [Pawetta — SEO-текст 2026](https://pawetta.com/baza/seo-tekst-kak-pisat/) | 2026 | да |
| Для информационной статьи в топе часто **1500–3000 слов** при полном раскрытии интента | [Seotika — SEO-статьи в ТОП](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да (диапазон рынка) |
| Lead: прямой ответ в **первых 100 словах** / 2–3 предложениях | [Seotika — SEO-статьи в ТОП](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| Для одной страницы — **15–25 связанных фраз** из Вордстат (частотность от ~50/мес в методике) | [Divitio — SEO-текст](https://divitio.ru/blog/kak-samomu-napisat-seo-tekst-poshagovaya-instruktsiya/) | 2026 | да (метод, не норма объёма) |
| Пошаговые инструкции: **повелительное наклонение**, один шаг — одно действие | [SEO Jazz — step-by-step](https://seojazz.ru/blog/step-by-step-kak-oformljat-poshagovye-instrukcii-chtoby-ih-brali-v-otvety/) | 2026 | да |
| Модуль блога: ответ **40–70 слов** на первом экране, затем таблица, ошибки, чек-лист, FAQ | [ROI SEO — структура](https://roiseo.ru/blog/struktura-seo-stati-dlya-bloga/) | 2026 | да |
| GEO надстроено над SEO: ответы Алисы AI строятся **с опорой на результаты поиска** | [Tapbox — GEO](https://tapbox.ru/blog/geo-prodvizhenie) | 30.09.2026 | да |
| Быстрыми ответами Алисы AI пользуются **46,5 млн** человек в месяц (данные Яндекса, апр. 2026) | [Tapbox — GEO](https://tapbox.ru/blog/geo-prodvizhenie) | 30.09.2026 | да |
| Google (10.07.2026): оптимизация под AI Overviews / AI Mode — это **SEO**; «хаки AEO/GEO» часто не работают | [Tapbox — GEO](https://tapbox.ru/blog/geo-prodvizhenie) | 30.09.2026 | да (цит. справки Google) |
| Snippet-first: начинать H2 с **1–3 предложений**-резюме; абзацы **3–7 строк** (чанки) | [PW Agency — GEO контент 2026](https://pw.agency/blog_new/seo/kak-pisat-stati-kotorye-neyroseti-budut-rekomendovat-polzovatelyam/) | 2026 | да |
| Schema **FAQPage**, **HowTo**, **Article** — сигналы для AI и сниппетов | [Zvonko — GEO](https://www.zvonkooo.ru/blog/geo-optimizatsiya-otvety-ai/) | 28.04.2026 | да |
| **51%** маркетологов используют нейросети для **аналитики и оптимизации**, а не слепой штамповки | [mayai.ru — контент-завод](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026-06-11 | да (fact-bank) |

**Не использовать без первичника:** «+40% visibility GEO» (vc.ru без arxiv в тексте); «80% шансов в ИИ» (PW Agency); жёсткая «плотность 1–2%» как норма.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** SEO-статья 2026 = **один workflow для человека и нейропоиска**: интент → семантика (Wordstat) → разбор SERP → outline H2/H3 → lead с ответом → тело с чанками и infostyle → мета + FAQ + schema → **GEO-слой** (snippet-first, FAQPage) → финальный чек-лист. H1-крючок «**которые читают люди**» = измеримые решения: короткие абзацы, повелительные шаги, таблицы, без воды и переспама.

**Почему отличается от конкурентов:**

- Классические гайды (Seoshkola, Olegweb) почти не связывают **читабельность** с **AI-цитированием**.
- GEO-статьи (Tapbox, Zvonko) не учат **писать longread с нуля** для блога.
- Excalibur B01 — **эталон формата**: сама статья демонстрирует модуль ROI SEO + utility-only (режим B).

**Tone (site-brief):** практичный B2B, без «мы лидеры рынка»; ИИ — помощник редактора, не замена фактов.

**H2-каркас (карточка B01 + SERP):**

1. Зачем SEO и GEO в одной статье (один контент — два канала)
2. Структура longread: lead, H1–H3, списки, таблицы
3. FAQ и schema (BlogPosting + FAQPage — в meta, не в body HTML)
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead, 40–60 слов | «SEO-статья — …» |
| Определение GEO | Блок SEO+GEO | Generative Engine Optimization |
| Snippet-first | Каждый H2 | 1–3 предложения до деталей |
| FAQ 5–7 | Конец | Ответ-действие, 2–4 предложения |
| Island test | QA | H2 понятен без соседних |
| Даты meta | schema handoff | datePublished / dateModified = дата прогона |
| internal_links | карточка | `/` |
| cover_scene_hint | cover | редактор, блокнот, тёплый свет |

**AI-формулировки:** как писать seo статьи; seo текст для блога; geo оптимизация статьи; сколько символов в seo статье; что такое geo в seo.

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и SERP; для how-to longread Excalibur — **8500–9500 знаков** текста.
2. **Что такое GEO в SEO?** — дополнение: цитирование в AI-ответах при базе индексации и структуры.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~60 символов), H1 на странице; не дублировать дословно.
5. **Какие schema для блога?** — BlogPosting + FAQPage.
6. **Как писать шаги, чтобы их брали в быстрые ответы?** — нумерация, повелительное наклонение, один шаг — одно действие.
7. **Как проверить статью перед публикацией?** — чек-лист: семантика, мета, структура, FAQ, schema, ссылки, мобильная читаемость.

---

## 7. Риски для writer

- Цифры только из §3 и fact-bank; Wordstat — после подключения MCP.
- Не копировать 13 шагов Olegweb / 7 шагов Seoshkola 1:1.
- Объём текста: **8500–9500** знаков (`shared/quality-blog.md`).
- Без эмодзи; без VPN/обходов.
- **Не писать article.html** на шаге research.

---

## 8. Utility (Gate 2)

**utility_verdict:** PASS

**reader_outcome:** Читатель за один цикл подготовит SEO-longread для блога: соберёт семантику, построит структуру по SERP, напишет lead и модульные блоки, оформит Title/Description и FAQ со schema, добавит GEO-приёмы (snippet-first, чанки) и пройдёт финальный чек-лист перед публикацией.

**action_outline:**

1. Зафиксировать **primary_query**, интент и 15–25 смежных фраз (Wordstat + подсказки; отсечь чужой intent).
2. Разобрать **топ-5–10 URL** в SERP: общие H2, таблицы, FAQ, пробелы.
3. Собрать **outline** (H1 + H2/H3); каждый H2 = подзадача + «делать / не делать».
4. Написать **lead**: ответ на запрос в первых 2–3 предложениях + обещание результата.
5. Наполнить разделы: **списки, таблица, пример**; ключи естественно (H1, lead, 1–2 H2, мета).
6. Добавить блок **FAQ 5–7** и JSON-LD **BlogPosting + FAQPage** (handoff schema).
7. Включить **GEO-слой**: snippet-first в начале H2, абзацы 3–7 строк, автор/даты.
8. Пройти **чек-лист публикации** (мета, alt, перелинковка, Rich Results, читаемость на мобильном).

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента | ✅ (8) |
| Таблица фактов с URL | ✅ (18) |
| Wordstat MCP | ⚠️ повторить после подключения |
| utility_verdict + action_outline | ✅ |
| GEO hooks + FAQ | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
