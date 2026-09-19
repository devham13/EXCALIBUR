# Research notes — B06 «Сравнение n8n и Make.com: как выбрать платформу автоматизации для бизнеса в 2026 году»

**topic_id:** B06  
**slug:** sravnenie-n8n-make-2026  
**article_mode:** B (comparison + decision workflow)  
**research_date:** 2026-07-08  
**disclaimer:** Все даты, версии и статистика проверены на 08.07.2026.

---

## 1. SERP-обзор (WebSearch, 10 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [make.com/en/compare/make-vs-n8n](https://www.make.com/en/compare/make-vs-n8n) | Официальный comparison Make | Актуальные тарифы, Make Grid, AI Agents, сертификации | Явный bias в пользу Make; нет матрицы для РФ/152-ФЗ | Маркетинговые формулировки «clear choice» без чеклиста |
| 2 | [n8n.io/vs/make](https://n8n.io/vs/make/) | Официальный comparison n8n | Модель billing (execution vs credit), self-host, JS/Python | Bias в пользу n8n; мало бизнес-сценариев | Копировать one-sided narrative |
| 3 | [zapier.com/blog/n8n-vs-make](https://zapier.com/blog/n8n-vs-make/) | Независимый (конкурент) | Честно про «success tax» credits на сложных сценариях | Продвигает Zapier как «лучший» | Третий продукт вместо decision matrix |
| 4 | [2sync.com/blog/n8n-vs-make](https://2sync.com/blog/n8n-vs-make) | Longread EN (2026) | TCO-таблица, self-host vs cloud, AI | Нет русского контекста, 152-ФЗ | Цифры без перепроверки первичником |
| 5 | [aibotmanager.ru/make-vs-n8n](https://aibotmanager.ru/make-vs-n8n/) | RU comparison | Таблица параметров, пороги 50K/100K ops, 152-ФЗ | Часть цифр без первичника (экономия 150–200К ₽) | Непроверенные ROI-цифры |
| 6 | [arslanov-ai.ru/instrumenty/make-vs-n8n](https://arslanov-ai.ru/instrumenty/make-vs-n8n/) | RU longread | Сценарии, цены в $, DevOps-развилка | Перегруз «марафоном», мало чеклиста | Структуру 1:1 |
| 7 | [promaren.ru/blog/podborki/n8n-ili-make-2026](https://promaren.ru/blog/podborki/n8n-ili-make-2026/) | RU подборка | Кейсы малого бизнеса | Поверхностная таблица, мало шагов выбора | Короткий формат без 15-пунктового чеклиста |
| 8 | [mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-avtomatizaczii-v-2026](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-avtomatizaczii-v-2026/) | RU comparison | Контент-завод, TCO, Compute Units Make | Коммерческий угол контент-завода | Копировать без баланса |
| 9 | [automationatlas.io/guides/automation-tool-comparison-2026](https://automationatlas.io/guides/automation-tool-comparison-2026/) | Мульти-tool atlas | 12 параметров, decision matrix | n8n+Make теряются среди Zapier/PA | Слишком широкий охват |
| 10 | [virtua.cloud/learn/ru/concepts/n8n-vs-zapier-vs-make-stoimost-privatnost](https://www.virtua.cloud/learn/ru/concepts/n8n-vs-zapier-vs-make-stoimost-privatnost) | RU GDPR/приватность | Резиденция данных, VPS n8n в ЕС | Узкий угол (приватность), нет AI-агентов | Только privacy без operational matrix |

**Паттерн SERP:** топ — «n8n vs make 2026» comparison longread (EN + RU). Официальные страницы Make и n8n доминируют по branded-запросам. Русскоязычные статьи дают таблицы, но редко дают **пошаговый алгоритм выбора** + **15-пунктовый чеклист** + **6 сценариев бизнеса** в одном материале.

**Intent:** comparison — пользователь на пороге выбора платформы и хочет **зафиксировать решение** (план + тариф), а не «узнать что такое n8n». Вторичный intent: цена при масштабе, self-host vs SaaS, AI-агенты, compliance.

**Пробел для блога:** практическая **матрица решений** (6 сценариев → платформа), **расчёт credits vs executions** на примерах, честный угол интегратора Make/n8n, чеклист миграции с Zapier, internal links на B02 (n8n AI) и B03 (MCP).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 08.07.2026)

⚠️ **WORDSTAT AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в Cloud-среде (проверено 08.07.2026; в каталоге MCP только Cursor Automation Tools и cursor-cloud). Точные показы в месяц **не получены**. Обновите токен и подключите сервер: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Fallback: семантический кластер (без выдуманных цифр спроса)

| Кластер | Ключевые формулировки (из карточки + SERP) | Интент |
|---------|---------------------------------------------|--------|
| Head EN | n8n vs make, make vs n8n, n8n make comparison | Сравнение + выбор |
| Head RU | сравнение n8n и make, make или n8n, что выбрать n8n или make | Decision |
| Цена | n8n pricing, make pricing credits, стоимость автоматизации | TCO |
| Compliance | n8n self-hosted 152-ФЗ, make gdpr | Приватность |
| AI | n8n ai agent vs make ai agents, langchain n8n | AI-развилка |
| Объём | автоматизация бизнеса n8n, 100k operations | Масштаб |

### LSI для writer (приоритет вхождений)

- n8n vs make / сравнение n8n и make / make или n8n  
- workflow executions vs credits / operations  
- self-hosted n8n / Community Edition / Docker  
- Make Core Pro Teams / 3000+ apps / Make AI Agents / Make Grid  
- LangChain, RAG, MCP (n8n) vs Reasoning Panel (Make)  
- TCO, DevOps, 152-ФЗ, GDPR, Frankfurt EU  
- миграция с Zapier, чеклист выбора платформы  

**SEO-стратегия:** primary «n8n vs make» в H1/lead; secondary RU-формулировки в H2 и FAQ; long-tail «что выбрать n8n или make для малого бизнеса» в FAQ и матрице сценариев.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| n8n Cloud Starter: 20 €/мес (годовая оплата), 2 500 executions, 5 concurrent | [n8n.io/pricing](https://n8n.io/pricing/) | 08.07.2026 | да |
| n8n Cloud Pro: 50 €/мес, 10 000 executions, 20 concurrent | [n8n.io/pricing](https://n8n.io/pricing/) | 08.07.2026 | да |
| n8n Business: 667 €/мес, 40 000 executions, self-hosted, SSO/Git | [n8n.io/pricing](https://n8n.io/pricing/) | 08.07.2026 | да |
| Execution = один полный прогон workflow; шаги не тарифицируются отдельно | [n8n.io/pricing](https://n8n.io/pricing/) | 08.07.2026 | да |
| Community Edition: бесплатный self-hosted на GitHub | [n8n.io/pricing](https://n8n.io/pricing/) | 08.07.2026 | да |
| Hosted n8n: данные в EU (Frankfurt) | [n8n.io/pricing](https://n8n.io/pricing/) | 08.07.2026 | да |
| Business overage: 4 000 EUR за доп. пакет 300 000 executions | [n8n.io/pricing](https://n8n.io/pricing/) | 08.07.2026 | да |
| n8n: 1 000+ интеграций + HTTP/GraphQL; Make: 2 800+ pre-built (на странице n8n) | [n8n.io/vs/make](https://n8n.io/vs/make/) | 08.07.2026 | да |
| Make: 3 000+ app integrations (официальный pricing/compare) | [make.com/en/pricing](https://www.make.com/en/pricing) | 08.07.2026 | да |
| Make Free: 1 000 credits/мес, 2 active scenarios, интервал запуска от 15 мин | [make.com/en/pricing](https://www.make.com/en/pricing) | 08.07.2026 | да |
| Make Core: 12 $/мес (годовая оплата), 10 000 credits/мес | [make.com/en/pricing](https://www.make.com/en/pricing) | 08.07.2026 | да |
| Make Pro: 21 $/мес, 10 000 credits/мес + priority execution, variables | [make.com/en/pricing](https://www.make.com/en/pricing) | 08.07.2026 | да |
| Make Teams: 38 $/мес, 10 000 credits/мес + роли команды | [make.com/en/pricing](https://www.make.com/en/pricing) | 08.07.2026 | да |
| 1 module action в сценарии Make ≈ 1 credit (стандартные модули) | [make.com/en/pricing](https://www.make.com/en/pricing) | 08.07.2026 | да |
| С 27.08.2025 Make перешёл с Operations на Credits; AI-модули могут потреблять >1 credit | [n8n.io/vs/make](https://n8n.io/vs/make/) | 08.07.2026 | да |
| n8n: встроенный JS/Python на всех планах; Make Custom functions — Enterprise | [n8n.io/vs/make](https://n8n.io/vs/make/) | 08.07.2026 | да |
| Make API: от Core, лимит от 60 calls/min (на Free API нет) | [n8n.io/vs/make](https://n8n.io/vs/make/) | 08.07.2026 | да |
| Make: SOC 3, SOC 2 Type II, ISO 27001, GDPR | [make.com/en/compare/make-vs-n8n](https://www.make.com/en/compare/make-vs-n8n) | 08.07.2026 | да |
| n8n Cloud: SOC 2 Type II, GDPR (указано на compare Make) | [make.com/en/compare/make-vs-n8n](https://www.make.com/en/compare/make-vs-n8n) | 08.07.2026 | да (как заявление вендора) |
| Make Grid: визуальная оркестрация сценариев и AI Agents на paid-планах | [make.com/en/compare/make-vs-n8n](https://www.make.com/en/compare/make-vs-n8n) | 08.07.2026 | да |
| 10-step workflow × 1 000 runs/мес = 1 000 executions (n8n) vs до 10 000 credits (Make) | [zapier.com/blog/n8n-vs-make](https://zapier.com/blog/n8n-vs-make/) | 08.07.2026 | да (иллюстрация модели) |
| Make.com: 2 500+ нативных интеграций; тарификация Compute Units удорожает медиа | [fact-bank / mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 2026-06-11 | да |
| Self-hosted n8n снижает накладные на медиа; маржинальность контент-производства до +35% | [fact-bank / mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 2026-06-11 | да |
| Make: прототип контент-пайплайна на ~40% быстрее за счёт визуального отладчика | [fact-bank / mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 2026-06-11 | да |
| Human-in-the-loop 2.0 — стандарт для сложных задач (<2,5% полностью автономно) | [fact-bank / mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026-06-11 | да |

**Не использовать без первичника:** «экономия 150–200К ₽/год на 500K ops» (aibotmanager); «+300% YoY n8n» (vc.ru без первичника); цены Core $9 на [make.com/compare](https://www.make.com/en/compare/make-vs-n8n) — расходится с [pricing](https://www.make.com/en/pricing) ($12); брать **pricing** как канон.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** читатель **проходит decision workflow**: оценивает объём (credits vs executions), команду (DevOps да/нет), compliance и AI-сложность → заполняет **сравнительную таблицу** → сверяет **6 типовых сценариев** → выбирает платформу и тариф → проходит **чеклист из 15 пунктов** перед запуском/миграцией.

**Почему отличается от конкурентов:**
- Официальные compare-страницы — marketing one-sided.
- RU-статьи дают таблицы, но не связывают их с пошаговым алгоритмом и чеклистом из карточки B06.
- Блог: позиция практика внедрения AI-автоматизации (Make + n8n), язык для B2B без DevOps, internal links на гайды B02/B03.

**Tone:** честный comparison; без «n8n для всех» и без обесценивания self-host. CTA — мягко: аудит/внедрение, курс Make для no-code-аудитории (см. `memory/brief/conversion-map.md`).

**H2-каркас (из карточки + research):**
1. Критерии выбора в 2026: объём, команда, 152-ФЗ, ИИ-агенты  
2. Сравнительная таблица: цена, интеграции, self-hosted, Make AI Agents vs n8n AI Agent  
3. Когда выбрать Make.com: быстрый старт, Reasoning Panel, Make Grid  
4. Когда выбрать n8n: приватность, масштаб, LangChain/RAG/MCP  
5. Матрица решений: 6 типовых сценариев → платформа  
6. Чеклист 15 пунктов: выбор, пилот, миграция с Zapier  

**Internal links:** `/avtomatizaciya-n8n-ai-agents/`, `/podklyuchenie-mcp-cursor/`

---

## 5. Comparison-матрица (черновик для writer)

| Критерий | n8n | Make.com |
|----------|-----|----------|
| Модель billing | Per execution (весь workflow = 1 run) | Per credit (каждый модуль; AI может >1) |
| Старт cloud | Starter 20 €/мес, 2 500 runs | Free 1 000 credits; Core 12 $/мес, 10 000 credits |
| Self-host | Да, CE бесплатно + infra | Нет (cloud-only) |
| Интеграции | 1 000+ нативных + HTTP/community | 3 000+ maintained apps |
| Код в workflow | JS/Python на всех планах | Custom functions — Enterprise; no-code core |
| AI-агенты | AI Agent node, LangChain, RAG, MCP | Make AI Agents, Reasoning, Make Grid |
| Time-to-first workflow | 30 мин (cloud) / часы–дни (self-host) | 5–15 мин (простой сценарий) |
| Compliance РФ/EU | Self-host → контроль локации данных; cloud EU Frankfurt | Cloud Make; GDPR; данные на серверах Make |
| Поддержка | Forum; dedicated — Enterprise | Paid plans: tickets; Enterprise 24/7 |
| Лучший объём | Многошаговые частые runs; 100K+ ops | Простые короткие сценарии; до ~50K credits |

### 6 типовых сценариев → рекомендация (черновик)

| Сценарий | Вердикт | Почему |
|----------|---------|--------|
| CRM-лиды: форма → amoCRM → Telegram (4 модуля, 2K/мес) | Make | Мало шагов, быстрый старт, укладывается в Core |
| Контент-пайплайн с видео/медиа (высокий credit burn) | n8n self-host | Предсказуемые executions; fact-bank: маржа медиа |
| AI support-бот с RAG по регламентам | n8n | Нативный Vector Store + on-prem данные |
| Маркетинговая команда без DevOps, 5–10 сценариев | Make | SaaS, Make AI Agents, Grid для обзора |
| 152-ФЗ / персональные данные только on-prem | n8n self-host | Полный контроль хостинга |
| High-frequency polling (каждую минуту, 10+ модулей) | n8n cloud/self-host | Executions не штрафуют за число шагов |

---

## 6. FAQ-кандидаты (5–7)

1. **Что лучше n8n или Make в 2026?** — Зависит от объёма и команды: Make для no-code и коротких сценариев; n8n для сложных multi-step и self-host.
2. **n8n или Make для малого бизнеса?** — До ~10–50K операций/мес без compliance-требований чаще Make Free/Core; при росте и сложности — пересчитать credits.
3. **Чем отличается n8n от Make в 2026?** — Billing (execution vs credit), self-host, глубина AI/MCP у n8n; визуальный builder и 3 000+ apps у Make.
4. **Когда self-hosted n8n окупается?** — Когда credits/executions на Make растут быстрее стоимости VPS+админки; считать TCO на 12 мес.
5. **Можно ли мигрировать с Zapier на Make или n8n?** — Да; чеклист: инвентаризация zaps, пересчёт tasks→credits/executions, пилот 1 сценария.
6. **Как учитывать AI в тарифах Make после 2025?** — AI-модули могут списывать >1 credit; внешний API-ключ LLM ≈ 1 credit + оплата провайдеру.
7. **Нужен ли DevOps для n8n?** — Для CE self-host — да (Docker, бэкапы, обновления); n8n Cloud — как обычный SaaS.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «платформа автоматизации» 40–60 слов | Lead | Боль: счёт растёт от числа шагов |
| Сравнительная таблица 10+ строк | H2-2 | Цена, hosting, AI, compliance |
| Матрица 6 сценариев | H2-5 | Таблица с вердиктом |
| Workflow выбора | H2-1 | Критерии → ветвление |
| Чеклист 15 пунктов | H2-6 | Нумерованный список |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «n8n vs make», «сравнение n8n и make», «make или n8n», «что выбрать n8n или make», «автоматизация бизнеса n8n».

---

## 8. Риски для writer

- Канон цен Make: [make.com/en/pricing](https://www.make.com/en/pricing) (Core $12, не $9 с compare-страницы).
- Не выдумывать Wordstat-показы; указать в статье не нужно — только SEO-ключи из раздела 2.
- Comparison честный: сильные стороны обеих платформ.
- Объём по `shared/quality-blog.md`; utility gate статьи: таблица + ≥5 шагов + чеклист 10+ (карточка требует 15).
- Без эмодзи; fact-bank цифры — только с пометкой источника.
- Не копировать структуру arslanov-ai / aibotmanager 1:1.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель оценит свой кейс по объёму операций, команде и compliance, заполнит сравнительную таблицу n8n vs Make, выберет платформу и тариф по матрице из 6 сценариев и пройдёт чеклист из 15 пунктов перед пилотом или миграцией.

**action_outline (для writer):**

1. **Инвентаризировать 3–5 текущих или планируемых автоматизаций:** число модулей/шагов, частота запусков в месяц, есть ли AI/медиа.
2. **Пересчитать потребление:** для каждого сценария — credits (Make: модули × runs) vs executions (n8n: runs).
3. **Зафиксировать ограничения команды:** есть ли DevOps для Docker/PostgreSQL; срок «запустить за неделю» vs «строим на год».
4. **Проверить compliance:** нужен ли on-prem/152-ФЗ; достаточно ли EU-cloud (Frankfurt n8n / Make GDPR).
5. **Заполнить сравнительную таблицу** (раздел 5) и отметить критичные для бизнеса строки.
6. **Сопоставить кейс с матрицей 6 сценариев** — получить предварительный вердикт Make / n8n cloud / n8n self-host.
7. **Посчитать TCO на 12 месяцев:** подписка + VPS (если self-host) + часы админки + API LLM.
8. **Выбрать тариф:** Make Free/Core или n8n trial/Starter; заложить запас 20–30% по credits/executions.
9. **Пройти чеклист 15 пунктов** (пилот, webhooks, бэкапы, human-in-the-loop) и запустить один пилотный сценарий до продакшена.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (10) |
| Wordstat MCP | ⚠️ сервер недоступен (fallback семантика) |
| Таблица фактов с URL | ✅ (24 факта) |
| utility_verdict + action_outline | ✅ |
| Comparison matrix + 6 сценариев | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + `conversion-map.md`.
