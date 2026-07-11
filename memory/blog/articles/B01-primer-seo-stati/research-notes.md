# Research notes — B01 «Как писать SEO-статьи, которые читают люди»

**topic_id:** B01  
**slug:** primer-seo-stati  
**article_mode:** B (how-to longread + эталон формата)  
**research_date:** 2026-07-11  
**disclaimer:** Все даты, версии и статистика проверены на 11.07.2026.

---

## Utility gate (research)

| Поле | Значение |
|------|----------|
| **utility_verdict** | PASS |
| **search_intent** | how_to |
| **article_mode** | B |
| **reader_outcome** | Читатель сможет собрать семантику, спланировать структуру longread, написать читаемый SEO-текст с FAQ/schema и пройти финальный чеклист перед публикацией, включая GEO-слой для нейропоиска. |
| **action_outline** | 1) Определить интент и разобрать топ-5 SERP. 2) Собрать primary + LSI в Вордстат/Вебмастер. 3) Построить H1–H3-каркас с «островами смысла». 4) Написать lead с прямым ответом в 40–60 словах. 5) Заполнить блоки: списки, таблицы, факты с URL. 6) Добавить FAQ 5–7 пар + JSON-LD BlogPosting/FAQPage. 7) Упаковать GEO-чанки (front-loading, llms.txt, robots для AI-ботов). 8) Заполнить Title/Description/alt и перелинковку. 9) Пройти чеклист публикации (15+ пунктов). |

---

## 1. Яндекс Вордстат (спрос и LSI)

⚠️ **WORDSTAT MCP WARNING:** Сервер `user-mcp-kv` недоступен в текущем Cloud-окружении (инструмент `wordstat_get_top_requests` не зарегистрирован). Точные показы в месяц **не получены** — цифры спроса в статье не использовать. Обновите MCP и токен через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Ручная проверка:** primary_query и LSI собирать в [Яндекс Вордстат](https://wordstat.yandex.ru/) и [Яндекс Вебмастер](https://webmaster.yandex.ru/) перед написанием (канон: [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat), 27.01.2026).

### Семантический кластер (LSI из SERP + WebSearch, без объёмов)

| Фраза | Роль | Источник кластера |
|-------|------|-------------------|
| как писать seo статьи | primary | карточка B01 |
| seo текст для блога | secondary | карточка B01 |
| geo оптимизация статьи | secondary | карточка B01 |
| как написать seo статью пошагово | LSI | [olegweb.ru](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) |
| seo тексты 2026 | LSI | [1ps.ru](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) |
| семантическое ядро вордстат | LSI | [Яндекс Директ](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) |
| структура seo статьи h1 h2 | LSI | [serptop.ru](https://serptop.ru/blog/kak-pisat-seo-teksty/) |
| чеклист seo статьи перед публикацией | LSI | [iconsult.agency](https://iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga-kak-pisat-stati-kotorye-privodyat-trafik/) |
| e-e-a-t seo текст | LSI | [olegweb.ru](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) |
| контент для людей и нейросетей | LSI | [gracie.digital](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) |
| generative engine optimization | LSI (GEO) | [arxiv.org/abs/2311.09735](https://arxiv.org/abs/2311.09735) |
| сколько символов в seo статье | FAQ-hint | карточка B01 |
| что такое geo в seo | FAQ-hint | карточка B01 |

---

## 2. SERP-обзор (WebSearch, июль 2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | Официальный гайд Яндекса (27.01.2026) | Авторитет; 4 шага workflow; H1–H4; абзацы 3–5 строк; Вордстат + Вебмастер; Title/Description; примеры плохо/хорошо | Нет GEO/нейропоиска; CTA на Директ | Коммерческий блок Директа; копировать H-иерархию без GEO-слоя |
| 2 | [1ps.ru/blog/texts/2026/seo-tekstyi-2026-...](https://1ps.ru/blog/texts/2026/seo-tekstyi-2026-kak-pisat-samostoyatelno-i-s-pomoshhyu-ii-%E2%80%93-polnoe-rukovodstvo/) | Longread 2026 | Кластеризация Вордстата; H2 = подтема; «сначала смысл, потом оптимизация»; ИИ как инструмент | Длинный sales-narrative; мало про schema | Перегруз ИИ-блоками без human-in-the-loop |
| 3 | [olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/](https://olegweb.ru/sdelai-sajt-sam/kak-napisat-seo-statyu/) | Пошаговый алгоритм (13 шагов) | Интент → SERP → структура → текст → WordPress → мета → чеклист | WordPress-специфика; нет GEO-чанков | 13 шагов 1:1; скриншоты WP |
| 4 | [gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi...](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | AI SEO + читабельность (июнь 2026) | Близкий угол к H1 B01; ответ в 40–60 словах; «острова смысла» после H3; факты каждые 150–200 слов | Мало чеклиста публикации | Копировать структуру без чеклиста Excalibur |
| 5 | [iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga...](https://iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga-kak-pisat-stati-kotorye-privodyat-trafik/) | SEO-чеклист для блога | Фазы research → content → on-page; H2–H4; E-E-A-T; внутренняя перелинковка | Англоязычные метрики (Flesch); нет GEO | Дословный чеклист 31 пункта |
| 6 | [vc.ru/seo/2975086-geo-optimizatsiya-dlya-biznesa](https://vc.ru/seo/2975086-geo-optimizatsiya-dlya-biznesa) | GEO 2026 | H2/H3 как вопросы; Core Web Vitals (LCP, INP, CLS); мониторинг цитирования | Фокус на бренд/бизнес, не на написании текста | Sales GEO без how-to написания |
| 7 | [pikapuka.com/blog/kak-napisat-seo-tekst-samomu...](https://pikapuka.com/blog/kak-napisat-seo-tekst-samomu-polnyy-gayd-ot-semantiki-do-e-e-a-t) | Агентский longread (май 2026) | E-E-A-T; Schema Article+FAQ; Title ~65 знаков | Непроверенные кейсы (+140% трафика) | Проценты без источника |

**Паттерн SERP (июль 2026):** топ — «полный гайд 2026» с Вордстатом, структурой H1–H4, чеклистом. Растёт кластер «контент для людей + AI». H1 «которые читают люди» слабо закрыт конкурентами — дифференциатор B01.

**Intent:** how_to — пошаговая система от семантики до публикации. Вторичный: связка SEO + GEO в одном материале.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Универсального объёма SEO-статьи не существует — зависит от сложности темы и конкуренции | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| H1 — один на страницу; H2–H4 для смысловых блоков | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Абзацы — ориентир 3–5 строк; списки для перечислений | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Поисковики оценивают смысл и полезность, не плотность ключей; переспам вреден | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Семантику собирают в Яндекс Вордстат и Яндекс Вебмастер | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title и Description влияют на сниппет и кликабельность | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Главная задача SEO-статьи — полный ответ на поисковый запрос | [Яндекс Директ — SEO-текст](https://direct.yandex.ru/base/articles/seo-tekst-chto-eto-i-kak-pravilno-pisat) | 27.01.2026 | да |
| Title — ориентир 50–60 символов с главным ключом | [serptop.ru — SEO-тексты](https://serptop.ru/blog/kak-pisat-seo-teksty/) | 2026 | да |
| Meta Description — 140–160 символов с призывом | [iconsult.agency — чеклист](https://iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga-kak-pisat-stati-kotorye-privodyat-trafik/) | 2026 | да |
| Прямой ответ на главный вопрос — в первых 40–60 словах блока | [gracie.digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| Каждый подраздел (H2/H3) должен работать как самодостаточный «остров смысла» | [gracie.digital — AI SEO 2026](https://gracie.digital/blog/2026/06/19/kontent-kotoryj-chitayut-lyudi-i-ponimayut-nejroseti-kak-pisat-stati-v-2026-chtoby-popast-i-v-google-i-v-ai-vydachu/) | 19.06.2026 | да |
| GEO (Generative Engine Optimization) — оптимизация видимости контента в ответах генеративных поисковиков | [arxiv.org/abs/2311.09735](https://arxiv.org/abs/2311.09735) | 2023 (KDD 2024) | да |
| Методы GEO (цитаты, статистика, цитирование источников) могут повысить видимость в AI-ответах до ~40% (бенчмарк GEO-bench, 10 000 запросов) | [arxiv.org/abs/2311.09735](https://arxiv.org/abs/2311.09735) | 2023 (KDD 2024) | да |
| Core Web Vitals: LCP до 2,5 с, INP до 200 мс, CLS до 0,1 (ориентиры) | [vc.ru — GEO 2026](https://vc.ru/seo/2975086-geo-optimizatsiya-dlya-biznesa) | 2026 | да* |
| Внутренняя перелинковка: 2–5 релевантных ссылок на другие материалы сайта | [iconsult.agency](https://iconsult.agency/blog/polniy-seo-cheklist-dlya-bloga-kak-pisat-stati-kotorye-privodyat-trafik/) | 2026 | да |
| Объём how-to longread в Excalibur BLOG: 8 500–9 500 знаков текста | [shared/quality-blog.md](shared/quality-blog.md) | канон проекта | да |

\* Вторичный источник (vc.ru); в тексте — «ориентиры Google» без жёсткого норматива.

**Не использовать:** «+140% трафика за 3 недели» (Pikapuka); «CTR +30% от schema» без первичника; «40% пользователей на ИИ-поиск» (Дзен без первичника).

---

## 4. Угол статьи (практический how-to)

**Главный угол:** SEO-статья 2026 = **читаемый longread**, который закрывает запрос человека **и** упакован для нейропоиска. Единый workflow: интент → семантика → структура → инфостиль → FAQ/schema → GEO-чанки → чеклист публикации.

**Дифференциация:**
- Яндекс — канон SEO без GEO-слоя.
- GEO-гайды (vc.ru, audit4seo) не учат писать текст с нуля.
- H1 «которые читают люди» — фокус на читабельность как SEO/GEO-фактор (короткие абзацы, «острова смысла», lead без воды).

**Режим B:** статья B01 — эталон формата: 8 500–9 500 знаков, 5–7 FAQ, BlogPosting + FAQPage, атомарные H2.

**H2-каркас (из карточки B01):**
1. Зачем SEO и GEO в одной статье
2. Структура longread: H1–H3, lead, списки, таблицы
3. FAQ и schema — зачем и как
4. Чеклист перед публикацией (15–20 пунктов)

---

## 5. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение SEO-статьи (40–60 слов) | Lead после H1 | «SEO-статья — …» |
| Определение GEO (40–60 слов) | Блок «SEO + GEO» | «GEO (Generative Engine Optimization) — …» |
| Conversational H2 | FAQ-зона | «Сколько символов…», «Что такое GEO…» |
| FAQ 5–7 пар | Конец | Ответ 2–4 предложения, actionable |
| Атомарные чанки | Каждый H2 | Первое предложение = тезис |
| Schema | meta, не body | BlogPosting + FAQPage |
| llms.txt | GEO-блок | Кратко: зачем блогу |
| Внутренняя ссылка | По карточке | На `/` |

---

## 6. FAQ-кандидаты (5–7)

1. **Сколько символов должно быть в SEO-статье?** — универсальной нормы нет; для how-to longread Excalibur — 8 500–9 500 знаков.
2. **Что такое GEO в SEO?** — GEO дополняет SEO: цель — цитирование в AI-ответах при базе индексируемого структурированного контента.
3. **Нужно ли переспамить ключи в 2026?** — нет; естественные вхождения + LSI.
4. **Чем Title отличается от H1?** — Title для сниппета (~50–60 символов), H1 — на странице; не дублировать.
5. **Какие schema нужны блогу?** — BlogPosting + FAQPage.
6. **Что такое llms.txt?** — файл-указатель для AI-краулеров; дополнение к sitemap.
7. **Как проверить статью перед публикацией?** — чеклист: семантика, мета, структура, FAQ, schema, ссылки, читабельность.

---

## 7. Риски для writer

- Не выдумывать показы Вордстата (MCP недоступен).
- Не копировать Pikapuka/olegweb 1:1.
- Цифры только из таблицы фактов §3.
- Без эмодзи; CTA ≤ 3.

---

## 8. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate topic PASS | ✅ |
| utility_verdict + action_outline + reader_outcome | ✅ |
| SERP ≥ 5 конкурентов (WebSearch 2026) | ✅ |
| Таблица фактов с URL (15+) | ✅ |
| LSI-кластер (без фейковых объёмов) | ✅ |
| GEO hooks + FAQ 5–7 | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + B01 в `blog-topics.md` + `site-brief.md`.
