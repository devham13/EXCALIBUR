# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (longread + демонстрация формата на самой статье)  
**research_date:** 2026-07-13  
**disclaimer:** Все даты, версии и статистика проверены на 13.07.2026.

---

## Utility gate (research)

**utility_verdict:** PASS  
**search_intent:** how_to  
**article_mode:** B  

**reader_outcome:** После гайда читатель сможет самостоятельно собрать семантику, спланировать структуру longread, написать читаемый SEO-текст с FAQ/schema и проверить его чеклистом перед публикацией — с учётом GEO-слоя для AI-выдачи.

**action_outline (workflow 7 шагов):**

1. **Интент и семантика** — определить тип запроса (информационный/коммерческий), собрать primary + LSI в Яндекс Вордстат и Вебмастер; выписать вопросы из «Похожих запросов».
2. **Анализ топ-10 SERP** — формат (гайд, чеклист, FAQ), глубина, пробелы конкурентов; зафиксировать минимальный набор блоков (таблица, списки, FAQ).
3. **Каркас longread** — один H1, H2 по подзадачам, lead 40–60 слов с прямым ответом; абзацы 3–5 строк, «один H2 — одна мысль».
4. **Черновик «сначала смысл»** — текст для людей, ключи естественно; E-E-A-T lite (автор, примеры, ссылки на первичные источники).
5. **Практические блоки** — чеклист 15+ пунктов, таблица SEO vs GEO, FAQ 5–7 пар с короткими ответами-действиями.
6. **Техника и GEO** — Title/Description, alt, URL, внутренние ссылки; BlogPosting + FAQPage (JSON-LD); атомарные чанки, answer-first; проверка robots.txt для AI-краулеров, упоминание llms.txt.
7. **Финальная проверка** — прогон чеклиста, уникальность, читаемость вслух, island test каждого H2.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 13.07.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Авторитет; пошаговый workflow; примеры «плохо/хорошо»; Wordstat, alt, мета, перелинковка; «нет универсального объёма» | Нет отдельного GEO-блока; CTA Директа | Коммерческий CTA; копировать H-структуру 1:1 |
| 2 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread 2026 | Семантика, E-E-A-T, чек-лист 10 шагов, Schema Article+FAQPage, Title ~65 знаков | Непроверенные % в кейсах; GEO как побочный эффект | Кейсовые цифры без первичника; 7 разделов 1:1 |
| 3 | [seomatik.ru/.../kak-podgotovit-effektivnye-seo-teksty-v-2026-godu](https://seomatik.ru/articles/seo/kak-podgotovit-effektivnye-seo-teksty-v-2026-godu-prakticheskoe-rukovodstvo-opytnogo-kopiraytera/) | Практический гайд копирайтера 2026 | «Сначала смысл, потом SEO»; анализ топ-10 и пробелов; H2/H3, введение 100–150 слов, schema, внутренние ссылки | Длинный narrative автора | Перегруз личным опытом без чеклиста |
| 4 | [hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | SEO-блог 2026 | 7-шаговый план; FAQ в конце; таблицы/списки «по делу»; интент > частотность | Мало GEO и llms.txt | Шаблонные формулировки «новые правила» |
| 5 | [iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga](https://iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga-kak-pisat-stati-kotorye-privodyat-trafik/) | Чеклист для блога | 31 пункт по фазам research → content → publish; Featured Snippet, PAA, AI-обзоры | Англоязычные термины; мало RU-специфики Яндекса | Копировать нумерацию 1:1 |
| 6 | [cpa.live/articles/razmetka-sajta-dlya-ai-vidimosti](https://cpa.live/articles/razmetka-sajta-dlya-ai-vidimosti/) | GEO + Schema 2026 | Article/FAQPage/Organization/Person; llms.txt; ссылка на Princeton GEO (KDD 2024) | Фокус на разметке сайта, не на написании статьи | Цифры «60–70%» без первичника в тексте статьи |

**Паттерн SERP (июль 2026):** доминируют «полный гайд 2026» с E-E-A-T, Wordstat, пошаговым планом и чеклистом. Отдельный кластер — GEO/AI-видимость. H1 «которые читают люди» в топе почти не встречается — дифференциатор Excalibur.

**Intent:** how_to — пользователь хочет систему «семантика → структура → текст → техника → проверка». Вторичный: связать SEO-текст для блога с GEO-оптимизацией статьи в одном материале.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP WARNING:** сервер `user-mcp-kv` не подключён в текущем Cloud Agent run (инструмент `wordstat_get_top_requests` недоступен). Точные показы/мес **не получены** — цифры спроса в таблице ниже **не указаны**. Для следующего прогона: подключите MCP и при необходимости обновите OAuth-токен через [https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40).

### Таблица спроса

| Фраза | Показы/мес |
|-------|------------|
| как писать seo статьи | *не получено — MCP недоступен* |
| seo текст для блога | *не получено — MCP недоступен* |
| geo оптимизация статьи | *не получено — MCP недоступен* |

### LSI для writer (экспертная семантика из SERP + карточка B01, без подстановки частот)

**Primary cluster:** как писать seo статьи, как написать seo текст, seo статья для сайта, seo текст для блога, seo копирайтинг 2026, структура seo статьи.

**Техника и мета:** title description seo, h1 h2 структура, meta description 150 символов, плотность ключевых слов, lsi запросы, семантическое ядро wordstat.

**Качество контента:** e-e-a-t, интент запроса, featured snippet, faq блок, чеклист seo статьи, уникальность текста, внутренние ссылки.

**GEO cluster:** geo оптимизация статьи, generative engine optimization, answer-first, llms.txt, schema.org faqpage, blogposting, ai краулеры robots.txt, атомарные чанки.

**SEO-стратегия для writer:** primary «как писать seo статьи» в H1/lead; secondary «seo текст для блога» и «geo оптимизация статьи» — в H2 и FAQ; long-tail «сколько символов в seo статье», «что такое geo в seo» — в FAQ (из faq_hints карточки).

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата источника | Можно в текст |
|------|----------|----------------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title — ориентир ~65 знаков, с ключом и триггером | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| H1 должен отличаться от Title | [Pikapuka — гайд SEO-статьи](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | 2026 | да |
| Первые 100–150 слов введения критичны для ответа на запрос | [Seomatik — SEO-тексты 2026](https://seomatik.ru/articles/seo/kak-podgotovit-effektivnye-seo-teksty-v-2026-godu-prakticheskoe-rukovodstvo-opytnogo-kopiraytera/) | 2026 | да |
| Title 50–60 символов, Description 150–160 — практические ориентиры | [hozyindachi.ru — SEO-тексты 2026](https://hozyindachi.ru/kak-pisat-seo-teksty-v-2026-godu-novye-pravila/) | 2026 | да |
| GEO — оптимизация попадания в генеративный ответ (AI Overviews), не замена SEO | [cpa.live — разметка для AI](https://cpa.live/articles/razmetka-sajta-dlya-ai-vidimosti/) | 2026 | да |
| Исследование GEO (Princeton et al., KDD 2024): топ-3 тактики дали +30–40% цитируемости в симуляции Bing Chat на 10 000 запросов | [cpa.live — разметка для AI](https://cpa.live/articles/razmetka-sajta-dlya-ai-vidimosti/) | 2026 | да* |
| Schema.org Article/BlogPosting, FAQPage, Organization, Person — базовый слой для LLM-видимости | [cpa.live — разметка для AI](https://cpa.live/articles/razmetka-sajta-dlya-ai-vidimosti/) | 2026 | да |
| Google рекомендует JSON-LD для структурированных данных | [cpa.live — разметка для AI](https://cpa.live/articles/razmetka-sajta-dlya-ai-vidimosti/) | 2026 | да |
| FAQ rich results в Google Search отключены 7 мая 2026; разметка FAQPage остаётся для понимания страниц и LLM | [cpa.live — разметка для AI](https://cpa.live/articles/razmetka-sajta-dlya-ai-vidimosti/) | 2026 | да |
| Главная задача статьи — полный ответ; возврат в поиск — сигнал низкого качества | [MaryProject — SEO-статьи](https://maryproject.ru/blog/kak-pravilno-pisat-stati-pod-seo/) | 2026 | да |
| Для how-to longread Excalibur — ориентир 8 500–9 500 знаков текста | [shared/quality-blog.md](shared/quality-blog.md) | редакция | да |

\* Упоминать исследование с оговоркой «по данным KDD 2024 / Princeton GEO paper», без раздувания до «гарантии топа».

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «40% пользователей на ИИ-поиске» (Dzen без первичника); «+30–55% видимости» (ozhgibesov.agency); «60–70% без schema» (Dzen/cpa без первичника в body).

---

## 4. Угол статьи (дифференциация)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Не «ещё один чек-лист ключей», а **единый workflow** (см. action_outline): интент → структура → инфостиль → FAQ/schema → GEO-чанки → финальный чеклист.

**Почему отличается:**
- Яндекс — канон SEO без GEO-слоя.
- GEO-гайды не учат писать текст с нуля.
- H1 «которые читают люди» — слабо раскрыт в SERP; фокус Excalibur: **читабельность как SEO-фактор** + техника.

**Режим B:** статья B01 — эталон формата: 8,5–9,5k знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2, lead с определением.

**H2-каркас (карточка + research):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как (JSON-LD, не в body)
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks (writer + schema)

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи 40–60 слов | Lead после H1 | «SEO-статья — …» |
| Определение GEO 40–60 слов | Блок SEO+GEO | «GEO — …» |
| Conversational H2 | FAQ-adjacent | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, действие |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Island test | QA | Блок автономен |
| Schema | schema.jsonld | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Зачем блогу |
| internal_links | Из карточки | `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — нет универсальной нормы; ориентир — полнота ответа и SERP; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — дополнение к SEO: цель — цитирование в AI-ответах при индексируемом структурированном контенте.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~50–65 знаков), H1 на странице; не дублировать.
5. **Какие schema для блога?** — BlogPosting + FAQPage.
6. **Что такое llms.txt?** — указатель приоритетных страниц для AI-краулеров; не замена sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Цифры только из таблицы фактов; Wordstat-показы — после подключения MCP.
- Не копировать Pikapuka 1:1.
- Объём 8 500–9 500 знаков; без эмодзи.
- Без оглавления с якорями в body (quality-blog).

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| SERP ≥ 3 конкурента | ✅ |
| Wordstat (попытка MCP) | ⚠️ MCP недоступен |
| Таблица фактов с URL | ✅ (17 фактов) |
| utility_verdict + action_outline + reader_outcome | ✅ |
| GEO hooks + FAQ | ✅ |
| Режим B | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B01 + `site-brief.md`.
