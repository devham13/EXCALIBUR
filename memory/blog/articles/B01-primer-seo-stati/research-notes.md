# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + эталон формата на самой статье)  
**research_date:** 2026-10-03  
**disclaimer:** Все даты, версии и статистика проверены на 03.10.2026 (2026 год).

---

## Utility (Gate 2)

**utility_verdict:** PASS

**reader_outcome:** Читатель за один цикл работы соберёт семантику под запрос, спроектирует outline longread под интент, напишет черновик с читаемой структурой и GEO-чанками, оформит Title/Description/FAQ, подготовит schema handoff и пройдёт финальный чеклист перед публикацией — без переспама и без «текста ради ключей».

**action_outline (для writer):**

1. **Интент и SERP:** зафиксировать primary query «как писать seo статьи», тип intent (how_to); открыть топ-5–10 URL, выписать must-have H2 и content gap (формат, FAQ, таблицы).
2. **Семантика:** собрать кластер в Яндекс Вордстат + Вебмастер; primary → H1/lead, secondary («seo текст для блога», «geo оптимизация статьи») → H2 и FAQ; LSI из топа SERP, не из «воды».
3. **Outline:** один H1, 4–6 H2 как подзадачи; под каждым H2 — тезис в первом предложении (island test); H3 только при необходимости; блок FAQ 5–7 вопросов.
4. **Lead и черновик:** в первых 2–3 предложениях прямой ответ + обещание результата; абзацы 3–5 строк, списки/таблица; после каждого H2 — рекомендация «делать / не делать».
5. **SEO + GEO слой:** таблица «SEO vs GEO для одной статьи»; атомарные чанки под нейровыдачу; упоминание llms.txt как опционального сигнала (не вместо sitemap).
6. **Мета и E-E-A-T lite:** Title (~60–65 знаков, ≠ H1), Description (~140–160); автор/редакция; факты только из таблицы ниже; даты публикации/обновления.
7. **Техника перед публикацией:** чеклист 15–18 пунктов (мета, один H1, alt, перелинковка, FAQ, schema JSON-LD в handoff, читабельность).
8. **После публикации:** отправить на индексацию, через 2–4 недели смотреть показы/клики/поведение; обновлять устаревшие факты.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 03.10.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Канон: семантика, Wordstat, H1–H4, естественные ключи, title/description, «нет универсального объёма» | Нет отдельного GEO-слоя; CTA Директа | Продвижение рекламы; клон структуры без дифференциатора «читают люди» |
| 2 | [yandex.ru/support/webmaster/ru/epos](https://yandex.ru/support/webmaster/ru/epos) | Справка Вебмастера (ЭПОС, 2025–2026) | Экспертность, полезность, оригинальность, содержательность; SEO для Алисы AI = те же принципы, опора на поиск | Не учит писать текст пошагово | Пересказ всего ЭПОС без workflow |
| 3 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread 2026 | Семантика, E-E-A-T, чек-лист, schema Article+FAQPage, AI-ответы | Кейсы с непроверяемыми %; перегруз «экспертностью» | Непроверенная статистика в кейсах; копия 7-разделной структуры 1:1 |
| 4 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-…](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Гайд 2026 + ИИ | Таблица E-E-A-T (Experience/Expertise/Authoritativeness/Trust); правило «после H2 — содержательный ответ» | Длинный коммерческий narrative | Шаблон «мы/наш опыт» без уникики |
| 5 | [seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 7 шагов для новичков 2026 | Чёткий workflow: запросы → топ → структура → текст → мета → релевантность → контроль | Мало GEO; узкий бренд | Подача «только под ключи» без human-first угла |
| 6 | [seotika.ru/kak-pisat-seo-stati/](https://seotika.ru/kak-pisat-seo-stati/) | SEO-агентство | Lead в первых 100 словах; иерархия H1→H2→H3; E-E-A-T через практику | Ориентир 1500–3000 слов и «плотность 1–2%» — спорно для Яндекса | Выдуманные проценты; agency CTA |
| 7 | [maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | Короткий гайд | «Полный ответ на одной странице»; сигнал качества — не возврат в поиск | Мало чек-листа и schema | Общие принципы без actionable шагов |
| 8 | [articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | AI-контент 2026 | Попадает в research-serp по всем свежим запросам | Пересечение с десятками «SEO 2026» клонов | Структура «семантика→ИИ→публикация» без угла читабельности |

**Паттерн SERP (октябрь 2026):** доминируют «полный гайд 2026» (articleai, 1ps, pikapuka, seoshkola) + официальный Яндекс. H1 карточки B01 («которые читают люди») встречается в выдаче (meta-journal в research-serp), но **слабо раскрыт** — большинство материалов про ключи и E-E-A-T, а не про **инфostиль, island test и единый SEO+GEO workflow**. Вторичный кластер «geo оптимизация статьи» уводит в Generative Engine Optimization (vc.ru, digitalrocket) — в B01 нужен **узкий блок** «GEO для одной статьи», не замена B04.

**Intent:** `how_to` — пользователь хочет **систему от запроса до чеклиста**; вторично — связка блога, AI-выдачи, FAQ/schema.

**Пробел Excalibur:** one longread = **читаемый текст для людей** + упаковка под Алису AI / AI Overviews; режим B — сама статья как эталон (8 500–9 500 знаков, 5–7 FAQ).

---

## 2. Яндекс Wordstat (MCP `user-mcp-kv`)

⚠️ **WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` не подключён в среде Cloud Agent (03.10.2026). Инструмент `wordstat_get_top_requests` не вызывался — **точные показы/мес в таблицу не заносятся**.

При восстановлении MCP повторить запросы:

- `как писать seo статьи` (primary)
- `seo текст для блога`
- `geo оптимизация статьи`
- смежные: `как написать seo статью`, `seo статья для блога`, `написание seo текстов`

**Экспертная семантика (без объёмов — только LSI для writer):**

| Кластер | Фразы для вкрапления |
|---------|----------------------|
| Core | как писать seo статьи, как написать seo статью, seo текст для блога, seo статья |
| Структура | структура seo статьи, заголовки h1 h2, title description, чеклист seo статьи |
| Семантика | семантическое ядро, яндекс вордстат, lsi слова, поисковый интент |
| Качество | e-e-a-t, полезность текста, переспам ключей, читаемость |
| GEO | geo оптимизация статьи, нейровыдача, faq для ai, schema faqpage |
| Блог | seo текст для блога, продвижение блога, longread |

**SEO-стратегия:** primary в H1/lead; «seo текст для блога» — отдельный H2 или подблок; «geo оптимизация статьи» — таблица SEO vs GEO + ссылка на hub B04, не каннибализация.

*Если при вызове Wordstat будет 401:* обновить токен через https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не «плотность» ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику подбирают в Яндекс Вордстат (и аналогах) | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| SEO-статья: введение → основная часть по шагам → заключение со следующим шагом | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Генеративные ответы в Поиске и Алиса AI опираются на результаты поиска; «принципиально новых требований» к качественному контенту нет | [Яндекс Вебмастер — ЭПОС](https://yandex.ru/support/webmaster/ru/epos) | 2025–2026 | да |
| Аспекты ранжирования сгруппированы в ЭПОС: экспертность, полезность, оригинальность, содержательность | [Яндекс Вебмастер — ЭПОС](https://yandex.ru/support/webmaster/ru/epos) | 2025–2026 | да |
| Этапы SEO: портрет пользователя → запросы и посадочные → техоптимизация → данные о сайте → ценность по ЭПОС | [Яндекс Вебмастер — ЭПОС](https://yandex.ru/support/webmaster/ru/epos) | 2025–2026 | да |
| Нет универсальной формулы плотности ключей; важнее семантическое покрытие и полнота ответа | [Яндекс — ключевые слова](https://yandex.ru/adv/edu/materials/direct-kak-podobrat-klyuchevye-frazy) | 2026 | да |
| SEO блога: глубина темы, логика, экспертиза авторов + техника (заголовки, перелинковка, скорость, мобильность) | [Яндекс — продвижение блога](https://yandex.ru/adv/edu/materials/prodvizhenie-bloga) | 2026 | да |
| Title — ориентир до ~60 символов; description 140–160; один H1; иерархия H1→H2→H3 | [Pawetta — SEO-текст 2026](https://pawetta.com/baza/seo-tekst-kak-pisat/) | 2026 | да (как практический ориентир, не «официальная норма») |
| Вводный абзац: прямой ответ в первых 2–3 предложениях; лид — зона быстрых ответов | [Seotika — SEO-статьи](https://seotika.ru/kak-pisat-seo-stati/) | 2026 | да |
| H2 — ответы на крупные вопросы; после каждого H2 нужен содержательный ответ (не «заголовок ради ключей») | [1ps.ru — SEO-тексты 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| E-E-A-T: Experience, Expertise, Authoritativeness, Trustworthiness — рамка качества (Experience добавлен в rater guidelines) | [Google Search Central via ai-seowriter.ru](https://www.ai-seowriter.ru/blog/seo-tekst) | 12.2022 / актуально 2026 | да |
| E-E-A-T не является отдельным «score» в ранжировании, но задаёт планку качества контента | [ai-seowriter.ru — SEO-текст](https://www.ai-seowriter.ru/blog/seo-tekst) | 2026 | да |
| Title до 60–70 символов; Description до 150–160; H2 обычно 5–10 на статью | [marketingklub.ru — SEO-статьи](https://marketingklub.ru/kak-pisat-seo-stati/) | 2026 | да (ориентир) |
| Workflow из 7 шагов: запросы → анализ топа → структура → текст → Title/Description → релевантность → публикация и контроль | [seoshkola.com — SEO-текст 2026](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | 2026 | да |
| Главная задача статьи — полный ответ; возврат пользователя в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| GEO (Generative Engine Optimization) дополняет SEO: цель — цитирование в AI-ответах при сохранении индексируемого контента | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да* |
| Нейросети извлекают пассажи; каждый H2 — «остров смысла»; front-loading в первых 100–150 словах | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да* |
| llms.txt предложен в сентябре 2024 (Jeremy Howard / Answer.AI) | [Digital Impuls — GEO](https://digitalimpuls.ru/blog/geo-optimization-2026/) | 2026 | да* |

\* GEO-факты — вторичные SEO-источники; для hub-страницы GEO см. B04 и arxiv GEO-bench.

**fact-bank.md:** нет строк, специфичных для «как писать seo статьи»; допустимо 1 краткая отсылка к контент-автоматизации (51% маркетологов используют нейросети для аналитики, не для слепой штамповки — [mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/)) только в блоке «ИИ как помощник, не автор».

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «плотность ключей 1–2%» как норма Яндекса; «AI обрабатывает 25% запросов» без первичника; выдуманные проценты из agency-кейсов.

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **longread, который хочется дочитать**, и который **можно процитировать** в нейровыдаче. Не «ещё один список ключей», а **единый workflow** (см. action_outline): интент → семантика → структура для людей → FAQ/schema → GEO-чанки → чеклист.

**Отличие от топ-SERP:**

- Яндекс и seoshkola дают канон без акцента на **читабельность как фактор удержания**.
- Pikapuka/1ps — E-E-A-T и ИИ, мало «island test» и таблицы SEO vs GEO в одном материале.
- H1 B01 закрывает gap «**которые читают люди**»: короткие абзацы, тезис в lead каждого H2, минимум agency-water.

**Режим B:** статья B01 — эталон: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage (schema — отдельная роль), перелинковка на `/` и hub B04.

**H2-каркас (карточка + research):**

1. Зачем одна статья закрывает и SEO, и GEO (таблица)
2. Структура longread: H1–H3, lead, списки, таблицы
3. Семантика и интент без переспама
4. FAQ и schema — что готовить writer vs schema-агент
5. Чеклист перед публикацией (15–18 пунктов)

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок SEO+GEO | «GEO — …» |
| Таблица SEO vs GEO | H2-1 | 5–6 строк |
| Workflow `→` | После lead | 8 шагов action_outline сжато |
| FAQ 5–7 | Конец | Ответы-действия, 2–4 предложения |
| Island test | QA/writer | Каждый H2 автономен |
| Conversational queries | FAQ | «Сколько символов…», «Что такое GEO…» |
| llms.txt | GEO-блок | Опционально, не обязателен |
| Internal | Тело | B04 geo hub, главная `/` |

**Ключи для AI-формулировок:** как писать seo статьи, seo текст для блога, geo оптимизация статьи, сколько символов в seo статье, что такое geo в seo.

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет (Яндекс); ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — дополнение: цитирование в AI при базе из индексируемого structured контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~60–65 знаков), H1 на странице; не дублировать.
5. **Какие schema нужны блоговой SEO-статье?** — BlogPosting + FAQPage (JSON-LD вне body).
6. **Что такое llms.txt?** — опциональный файл для AI-краулеров; не замена robots/sitemap.
7. **Как проверить статью перед публикацией?** — чеклист из action_outline п.7.

---

## 7. Риски и blockers для writer

- Цифры только из §3; Wordstat-объёмы не писать до появления MCP-данных.
- Не клонировать Pikapuka/1ps структуру 1:1.
- Объём 8 500–9 500 знаков (`quality-blog.md`).
- Без эмодзи, без VPN/обходов.
- CTA ≤ 3; не подменять чеклист рекламой.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента | ✅ |
| Таблица фактов с URL | ✅ (18+ строк) |
| Wordstat | ⚠️ MCP недоступен; LSI — экспертно |
| utility_verdict + action_outline | ✅ |
| GEO hooks + FAQ | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 в `memory/topics/blog-topics.md` + `shared/excalibur-article-writing-contract.md`.
