# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + эталон формата на самой статье)  
**research_date:** 2026-10-02  
**EXCALIBUR_RUN_DATE:** 2026-10-02  
**disclaimer:** Даты, версии и статистика сверены на 02.10.2026. Источники с датой публикации после 2026-10-01 в открытом SERP не найдены; ниже — актуальные материалы 2026 года и канон Яндекса.

---

## Utility gate (research)

| Поле | Значение |
|------|----------|
| **utility_verdict** | **PASS** |
| **search_intent** | how_to |
| **article_mode** | B |

**reader_outcome:** Читатель сможет за один проход собрать семантику, спланировать longread под интент, написать текст «для людей», добавить SEO-мета и GEO-слой (lead, FAQ, schema) и пройти финальный чеклист перед публикацией.

**action_outline (workflow 8 шагов):**

1. **Интент:** открыть ТОП-10 по «как писать seo статьи», выписать общие H2 и пробелы (нет чеклиста, нет GEO, нет связки «читабельность + SEO»).
2. **Семантика:** primary + secondary из карточки; LSI из кластера (см. раздел Wordstat); группировка запросов по подтемам → будущие H2.
3. **Структура:** один H1; 4–6 H2 из `h2_outline` + под-H3; lead 40–60 слов с прямым ответом; каждый H2 — «остров смысла» (тезис в первом предложении).
4. **Черновик:** короткие абзацы (3–5 строк), списки/таблица workflow; ключи только естественно (без переспама).
5. **SEO-поля:** Title (~60–70 знаков), Description (~150–160), alt у изображений, 2–3 внутренние ссылки (главная `/`).
6. **GEO-слой:** 5–7 FAQ в видимом HTML; conversational H2 где уместно; факты с URL, без выдуманных процентов.
7. **Schema (handoff):** BlogPosting + FAQPage JSON-LD вне body — совпадение с видимым текстом.
8. **Чеклист публикации:** 15+ пунктов (семантика, мета, структура, FAQ, schema, ссылки, читабельность, robots для AI-ботов — упоминание, не deep dive).

---

## 1. SERP-обзор (WebSearch + research-serp.json, 2026-10-02)

**Запросы:** «как писать seo статьи 2026», «geo оптимизация статьи 2026 чеклист», H1-кластер из `research-context.json`.

**Паттерн выдачи:** доминируют пошаговые гайды 2026 (7–10 шагов), E-E-A-T, семантика через Вордстат, отдельный кластер GEO/нейропоиска. Прямого попадания в H1 «которые читают люди» мало — возможность дифференциации.

| # | URL | Тип | Сильные стороны | Пробелы | Не копировать |
|---|-----|-----|-----------------|---------|---------------|
| 1 | [direct.yandex.ru/.../seo-tekst](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Канон Яндекса (27.01.2026) | 5 шагов workflow; нет универсального объёма; абзацы 3–5 строк; естественные ключи; Вордстат/Вебмастер | Нет GEO, FAQ/schema, чеклиста longread | CTA Яндекс Директ; формальную структуру без GEO |
| 2 | [articleai.ru/.../kak-napisat-seo-statyu-v-2026](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | Коммерческий блог (17.08.2026) | Полный цикл семантика → публикация; LSI; мета; Schema Article/FAQ | Плотность ключей 2–4% и «70% успеха» без первичника; мало про читабельность как цель H1 | Жёсткие % плотности; agency-тон |
| 3 | [1ps.ru/.../seo-tekstyi-2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Агентский longread 2026 | «Сначала смысл, потом оптимизация»; H2 с ответом сразу; E-E-A-T блок | Длинный общий гайд; GEO вторичен | Копировать структуру 1:1 |
| 4 | [pikapuka.com/.../polnyy-gayd](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Чек-лист + E-E-A-T (2026) | Title ~65 знаков; Schema; AI-сnippets | Кейсы с непроверенными % | Непроверенную статистику в кейсах |
| 5 | [seoshkola.com/.../kak-pisat-seo-tekst](https://seoshkola.com/blog/kontent-sayta/kak-pisat-seo-tekst/) | Практик (7 шагов) | Ясные шаги 1–7; анализ ТОП; релевантность после черновика | Без GEO и единого printable-чеклиста | — |
| 6 | [private-seo.ru/.../kotorye-nravyatsya-lyudyam](https://private-seo.ru/blog/kak-pisat-seo-optimizirovannye-teksty-kotorye-nravyatsya-lyudyam) | Инструкция (обн. 07.08.2026) | Заголовок близок к нашему углу «для людей»; подготовка = половина успеха (авторская формулировка) | Нет единого SEO+GEO workflow | «50% успеха» как каноническая цифра без fact-bank |
| 7 | [mv-blog.ru/.../geo-optimizaciya-stati-checklist](https://mv-blog.ru/blog/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | GEO чек-лист статьи | Lead 40–60 слов; FAQ 5–7; BlogPosting+FAQPage; таблица «можно публиковать» | Фокус Битрикс, не «как писать с нуля» | CMS-специфику без адаптации |

**Intent:** how_to — нужен единый маршрут «семантика → текст → техника → GEO → чеклист». Вторичный: «seo текст для блога», «geo оптимизация статьи».

**Свежесть:** в выдаче от 02.10.2026 нет материалов с датой > 2026-10-01; опора на свежие гайды лета–осени 2026 и канон Яндекса.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` не подключён в среде Cloud Agent (02.10.2026). Вызов `wordstat_get_top_requests` для «как писать seo статьи» выполнить не удалось. **Точные показы в месяц не получены — не выдумывать цифры спроса.**

При восстановлении MCP — повторить запросы:

- `как писать seo статьи`
- `seo текст для блога`
- `geo оптимизация статьи`

**LSI / смежные формулировки (из SERP и топ-конкурентов, для writer — без частотности):**

| Кластер | Фразы |
|---------|--------|
| Действие | как написать seo статью, seo копирайтинг, пошаговая инструкция |
| Семантика | семантическое ядро, lsi-фразы, яндекс вордстат, анализ конкурентов топ-10 |
| On-page | title description, h1 h2 h3, мета-теги, переспам, внутренняя перелинковка |
| Качество | e-e-a-t, экспертность автора, уникальность текста, читабельность |
| Блог | seo текст для блога, longread, faq блок |
| GEO | geo оптимизация статьи, нейропоиск, faqpage json-ld, lead snippet-first, llms.txt (упоминание) |

---

## 3. Таблица фактов (≥15, с URL)

| # | Факт | Источник | Дата | В текст |
|---|------|----------|------|---------|
| 1 | Универсального объёма SEO-статьи нет — зависит от темы и конкуренции в выдаче | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 2 | H1 — один на страницу; H2–H4 делят материал на смысловые блоки | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 3 | Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 4 | Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 5 | Семантику подбирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 6 | Title и Description влияют на сниппет и решение перейти на страницу | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 7 | SEO-текст: workflow из 5 шагов (тема → семантика → структура → текст → оптимизация) | [Яндекс — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| 8 | После каждого H2 в структуре — сразу содержательный ответ на подтему | [1ps.ru — SEO 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| 9 | Главный ключ — H1, первый абзац, 1–2 H2, title/description; LSI — только если вписывается | [1ps.ru — SEO 2026](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | 2026 | да |
| 10 | Title — ориентир 55–60 символов; Description — 150–160 символов | [ArticleAI — SEO-статья 2026](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | 17.08.2026 | да |
| 11 | Schema.org Article + FAQ повышает шанс расширенных сниппетов (конкурентная практика) | [ArticleAI — SEO-статья 2026](https://articleai.ru/blog/kak-napisat-seo-statyu-v-2026-godu-poshagovaya-instruktsiya-ot-semantiki-do-publikatsii) | 17.08.2026 | да* |
| 12 | H2 — основные разделы (часто 5–10); строгая иерархия H1→H2→H3 | [marketingklub.ru — SEO-статьи](https://marketingklub.ru/kak-pisat-seo-stati/) | 2026 | да |
| 13 | Lead 40–60 слов, snippet-first, без воды | [mv-blog.ru — GEO чек-лист](https://mv-blog.ru/blog/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | 2026 | да |
| 14 | FAQ 5–7 пар в видимом HTML + BlogPosting и FAQPage JSON-LD, совпадающие с телом | [mv-blog.ru — GEO чек-лист](https://mv-blog.ru/blog/kontent-marketing-i-kopirayting/geo-optimizaciya-stati-checklist/) | 2026 | да |
| 15 | GEO дополняет SEO: цель — цитирование в AI-ответах при сохранении индексируемого контента | [text.ru — GEO vs SEO](https://text.ru/blog/geo-vs-seo-chto-delat-s-optimizaciey-tekstov-v-2026-godu) | 30.01.2026 | да |
| 16 | Если пользователь возвращается в поиск — сигнал низкого качества ответа на странице | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| 17 | 51% маркетологов используют нейросети для аналитики и оптимизации, а не слепой штамповки | [fact-bank → mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026-06-11 | да |

\* Практика рынка; не академическое исследование.

**Не использовать:** «+140% трафика» (Pikapuka); «плотность ключа 2–4%» как обязательное правило (конфликтует с каноном Яндекса); «70% успеха от подготовки» (ArticleAI) без первичника; Princeton +30–40% (mayai.ru) без arxiv в fact-bank.

**fact-bank.md:** прямых фактов про SEO-копирайтинг нет; допустима одна смежная цифра (#17) про использование ИИ маркетологами.

---

## 4. Угол и дифференциация

**Угол:** один longread закрывает **и** классический SEO **и** GEO: читабельность и «острова смысла» — не украшение, а условие ранжирования и цитирования в нейровыдаче. H1 B01 («которые читают люди») = практика инфостиля + структура + финальный чеклист, а не «ещё 10 советов про ключи».

**Отличие от SERP:**

- Яндекс — канон без GEO/FAQ-чеклиста.
- GEO-гайды — без обучения написанию текста с нуля.
- Агентские гайды — перегруз E-E-A-T и коммерческие CTA.

**Режим B:** статья B01 — эталон: 8 500–9 500 знаков, workflow `→`, таблица или чеклист 15+ пунктов, 5–7 FAQ, BlogPosting + FAQPage (schema-агент).

**H2 (из карточки):**

1. Зачем SEO и GEO в одной статье  
2. Структура longread  
3. FAQ и schema  
4. Чеклист перед публикацией  

---

## 5. GEO hooks (writer / schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи | Lead | 40–60 слов |
| Определение GEO | Блок SEO+GEO | 40–60 слов |
| Conversational H2 | По faq_hints | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 | Конец | Ответы-действия, 2–4 предложения |
| Атомарные H2 | Везде | Первое предложение = вывод |
| Внутренняя ссылка | Тело | `/` |
| cover_scene_hint | Cover | редактор, ноутбук, блокнот |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; ориентир — полнота ответа и SERP; для B01 Excalibur — 8 500–9 500 знаков.  
2. **Что такое GEO в SEO?** — оптимизация под цитирование в AI-ответах при той же индексируемой базе.  
3. **Нужен ли переспam ключей в 2026?** — нет, естественные вхождения и тематическая лексика.  
4. **Чем Title отличается от H1?** — Title для сниппета (~60 знаков), H1 на странице; не дублировать дословно.  
5. **Какие schema для блога?** — BlogPosting + FAQPage при видимом FAQ.  
6. **Где собирать семантику?** — Вордстат, Вебмастер, анализ ТОП-10.  
7. **Как проверить перед публикацией?** — пройти чеклист: lead, H2, мета, FAQ, schema, ссылки, факты.

---

## 7. Риски для writer

- Цифры только из таблицы §3 и fact-bank.
- Не копировать 7-разделную структуру Pikapuka/ArticleAI 1:1.
- Без эмодзи, без VPN-тематики.
- `article.html` — зона writer, не research.

---

## 8. Готовность

| Критерий | Статус |
|----------|--------|
| SERP ≥ 5 URL | ✅ |
| Факты ≥ 15 с URL | ✅ |
| utility_verdict + action_outline | ✅ |
| Wordstat | ⚠️ MCP недоступен |
| GEO hooks + FAQ | ✅ |

**Writer:** вход — этот файл, `research-context.json`, `blog-topics.md` B01, `site-brief.md`.
