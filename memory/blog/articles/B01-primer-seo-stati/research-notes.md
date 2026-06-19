# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-06-19  
**disclaimer:** Все даты, версии и статистика проверены на 19.06.2026.

---

## 1. SERP-обзор TOP-5 (WebSearch, июнь 2026)

**Primary query:** «как писать seo статьи» / «как писать seo статьи 2026»  
**Secondary:** «seo текст для блога 2026», «geo оптимизация статьи 2026»  
**Intent:** how_to — пошаговая система от семантики до публикации + связка SEO+GEO.

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [pikapuka.com/.../kak-napisat-seo-tekst-samomu](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (май 2026) | Wordstat → E-E-A-T → Featured Snippet; чек-лист 10 шагов; Title ~65 знаков; Schema Article+FAQPage; интент i1/i8 | Кейсы с непроверенными %; GEO только как следствие E-E-A-T | Непроверенные метрики трафика; 7-разделную структуру 1:1 |
| 2 | [1ps.ru/.../seo-tekstyi-2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Платформа копирайтеров (2026) | Очень длинный гайд: семантика, ИИ, BLUF, чек-листы; актуальный год в URL | Перегруз инструментами и промптами; слабый акцент «для людей» | Шаблон «100 инструментов»; дубли блоков про ИИ без human-first угла |
| 3 | [direct.yandex.ru/.../seo-tekst](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Авторитет; 5 шагов workflow; примеры плохо/хорошо; абзацы 3–5 строк; Wordstat; alt, мета, перелинковка | Нет GEO/нейропоиска; CTA Директа в конце | Коммерческий блок Директа; копировать H-структуру без GEO-слоя |
| 4 | [seomatik.ru/.../kak-podgotovit-effektivnye-seo-teksty-v-2026](https://seomatik.ru/articles/seo/kak-podgotovit-effektivnye-seo-teksty-v-2026-godu-prakticheskoe-rukovodstvo-opytnogo-kopiraytera/) | SEO-блог (2026) | Практика копирайтера; E-E-A-T, кластеры, AI-оптимизация | Меньше FAQ/schema; типовой agency-tone | Формулировки «эксперт с N лет» без доказательств |
| 5 | [bestseoserg.com/.../kak-pisat-seo-teksty.html](https://bestseoserg.com/blog/kak-pisat-seo-teksty.html) | Нишевый гайд (2026) | **Близкий intent к H1** «которые читают люди»; план, семантика, чек-лист | Уже в SERP, но слабее по GEO и schema | Заголовок 1:1; короткий объём без longread-глубины |

**Паттерн SERP (19.06.2026):** доминируют «полный гайд 2026» (Pikapuka, 1ps, seomatik, hozyindachi). Официальный Яндекс — якорь доверия. Отдельный кластер по secondary «geo оптimization» — audit4seo, digitalimpuls, click.ru (GEO vs SEO). **Пробел:** мало материалов, где SEO-writing и GEO-упаковка **один workflow** с фокусом на читабельность, а не на ключи.

**Secondary SERP «geo оптимизация статьи»:** audit4seo.ru, blog.click.ru, trigub.ru — атомарные чанки, Answer-first, Schema.org, llms.txt. Их техники нужно встроить в блоки B01, не вынося GEO в отдельную «новостную» статью.

---

## 2. Яндекс Wordstat (спрос и LSI)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в Cloud runtime (инструмент `wordstat_get_top_requests` не вызван; токен/конфиг не подключены). Точные объёмы показов в месяц **не получены**. Обновите токен через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без цифр спроса — для writer до восстановления Wordstat):**

| Кластер | LSI / смежные формулировки из SERP |
|---------|-------------------------------------|
| Primary | как написать seo статью, seo текст для сайта, seo копирайтинг 2026, написание seo текстов |
| Структура | семантическое ядро, wordstat, title, meta description, h1 h2, переспам, lsi-слова |
| Качество | e-e-a-t, инфостиль, featured snippet, полезность, интент |
| GEO | geo оптимизация, answer-first, ai overviews, faqpage, schema.org, llms.txt, нейроответ |

**Рекомендация writer:** после публикации прогнать primary + secondary в Wordstat и уточнить H2/FAQ под реальные «хвосты».

---

## 3. Таблица фактов (15 утверждений с URL)

| # | Факт | Источник | Дата | Можно в текст |
|---|------|----------|------|---------------|
| 1 | Универсального объёма SEO-статьи не существует — он зависит от сложности темы и конкуренции в выдаче | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 2 | Абзацы SEO-текста — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 3 | H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 4 | Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 5 | Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 6 | Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 7 | H1 должен отличаться от Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| 8 | Title — ориентир ~65 знаков, с ключом и триггером (чек-лист, инструкция) | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| 9 | Микроразметка Schema.org типов Article и FAQPage улучшает сниппет и структуру для роботов | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 09.05.2026 | да |
| 10 | GEO (Generative Engine Optimization) дополняет SEO — цель цитирования в AI-ответах, база — индексируемый контент | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| 11 | Нейросети извлекают пассажи (passages), не страницы целиком — каждый H2 = самодостаточный «остров смысла» | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| 12 | Первые 100–150 слов страницы — ключевая зона для извлечения ответа AI | [audit4seo — GEO 2026](https://audit4seo.ru/blog/geo-optimizaciya-2026) | 2026 | да |
| 13 | Смысловой блок для ИИ — ориентир 100–380 слов (2–6 абзацев) с отдельным подзаголовком H2/H3 | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| 14 | Суть блока должна быть в первых 40–60 словах (Answer-first / front-loading) | [click.ru — GEO vs SEO](https://blog.click.ru/neiroseti/geo-vs-seo-kak-optimizirovat-teksty-dlya-poiska-i-ii-otvetov/) | 2026 | да |
| 15 | Title: 50–60 знаков; Description: 140–180 знаков; H1 не дублирует Title дословно | [SEOJazz — текстовая оптимизация 2026](https://seojazz.ru/blog/tekstovaja-optimizacija-v-2026-godu-rabota-s-kontentom-dlja-uluchshenija-relevantnosti-i-relevantnye-tegi/) | 14.01.2026 | да |

**Не использовать без первичника:** «+140% трафика» (Pikapuka); «AI обрабатывает 25% запросов» (audit4seo); «Aggarwal +40%» — только как отсылка к исследованию без точного процента.

**Сверка с fact-bank.md:** прямых фактов про SEO-writing в fact-bank нет; для B01 опираемся на таблицу выше. Факты fact-bank про ИИ-контент-заводы — не смешивать с телом B01.

---

## 4. Угол статьи (utility + дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow**: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается от TOP-5:**
- Яндекс даёт канон SEO без GEO; GEO-гайды не учат писать текст с нуля.
- Агентские гайды (Pikapuka, 1ps) перегружены инструментами и непроверенными кейсами.
- H1 «которые читают люди» слабо раскрыт у bestseoserg — наш фокус: **читабельность как SEO-фактор** + техника.

**Режим B:** статья B01 — эталон формата: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage (schema отдельным агентом), атомарные H2, lead с определением, перелинковка на `/`.

---

## 5. action_outline (writer)

1. **Определить интент** — information how_to; выписать primary + 2 secondary из карточки B01; проверить TOP-3 SERP на пробелы.
2. **Собрать семантику** — Wordstat/Webmaster (или LSI из §2 до восстановления MCP); кластер: «как писать seo статьи», «seo текст для блога», «geo в seo».
3. **Спроектировать каркас** — H1 из карточки; 4 H2 из blog-topics + lead 40–60 слов с определением SEO-статьи; H2 как вопросы где уместно.
4. **Написать body** — инфостиль, абзацы ≤4 строк, Answer-first после каждого H2; блок «SEO + GEO в одной статье» с определением GEO.
5. **Добавить FAQ** — 5–7 пар (объём символов, GEO, переспам, Title vs H1, schema, llms.txt, чеклист перед публикацией).
6. **Техника on-page** — Title 50–65 зн., Description 140–180 зн., alt обложки, внутренняя ссылка на `/`.
7. **GEO-упаковка** — атомарные чанки 100–380 слов; island test; упоминание llms.txt и FAQPage (разметку не в body).
8. **Финальный чеклист** — 15–20 пунктов printable logic в §4 карточки B01.
9. **Self-QA** — только факты из §3; объём 8 500–9 500 знаков; без эмодзи и выдуманной статистики.

---

## 6. reader_outcome

После прочтения и прохождения чеклиста читатель **самостоятельно напишет и опубликует SEO-longread**, который:
- закрывает информационный интент без переспама ключей;
- имеет структуру H1–H3, lead, списки/таблицы, FAQ;
- готов к цитированию в AI-выдаче (GEO-чанки, Answer-first, schema-handoff);
- проходит финальную проверку по чеклисту перед публикацией в блоге.

---

## 7. GEO hooks, FAQ-кандидаты, риски

**GEO hooks:** определения SEO/GEO в lead; conversational H2; FAQ 5–7; island test; BlogPosting+FAQPage (schema agent); datePublished 2026-06-19.

**FAQ-кандидаты:** см. предыдущий прогон — объём символов; что такое GEO; переспам; Title vs H1; schema; llms.txt; чеклист перед публикацией.

**Риски writer:** не выдумывать Wordstat-цифры; не копировать Pikapuka 1:1; site_url — `/` по карточке.

---

## 8. Готовность

| Критерий | Статус |
|----------|--------|
| SERP TOP-5 (WebSearch 2026) | ✅ |
| Wordstat (MCP) | ⚠️ WARNING — нет данных |
| Факты 15+ с URL | ✅ |
| action_outline | ✅ |
| reader_outcome | ✅ |
| utility_verdict | **PASS** |

**utility_verdict:** PASS — тема how_to, практический workflow, reader_outcome измерим.

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
