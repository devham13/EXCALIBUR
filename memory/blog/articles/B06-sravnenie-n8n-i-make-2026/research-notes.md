# Research notes — B06 «Сравнение n8n и Make.com: что выбрать для автоматизации бизнеса в 2026 году»

**topic_id:** B06  
**slug:** sravnenie-n8n-i-make-2026  
**article_mode:** B (comparison + чеклист решения)  
**research_date:** 2026-09-07  
**disclaimer:** Все даты, версии и статистика проверены на 07.09.2026.

---

## 1. SERP-обзор (WebSearch, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [mayai.ru/n8n-ili-make-com…](https://mayai.ru/avtomatizacziya-proczessov-n8n-ili-make-com-chto-vybrat-v-2026/) | Comparison + чеклист (наш домен) | Таблица, 6 сценариев, чеклист 15 пунктов, CTA «пересчитать объём» | Уже есть на mayai.ru — нужен свежий угол «Ковчег» без дубля 1:1 | Копировать структуру без дифференциации; непроверенные «65% вакансий» из другой статьи mayai |
| 2 | [aibotmanager.ru/make-vs-n8n](https://aibotmanager.ru/make-vs-n8n/) | Comparison RU (2026) | Таблица цен, порог 50K/100K ops, 152-ФЗ, LangChain | Цифры экономии «150–200K ₽/год» без методики | Копировать рублёвые savings без расчётной формулы для читателя |
| 3 | [ai-uchi.ru/tools/make-com-n8n…](https://ai-uchi.ru/tools/make-com-n8n-avtomatizatsiia-bez-koda-ai-2026/) | Comparison + AI (2026) | Таблица функций, RAG/MCP, сценарии «берите X если» | Число интеграций (3 000 vs 700) расходится с официальными источниками | Жёсткий bias «n8n всегда лучше для AI» без TCO-калькулятора |
| 4 | [cipherprojects.com/n8n-vs-make…](https://www.cipherprojects.com/blog/posts/n8n-vs-make-automation-platform-comparison/) | Deep comparison EN (март 2026) | Точные тарифы, migration map Make→n8n, per-execution vs per-step | Нет 152-ФЗ, нет RU-контекста блокировок | Копировать EN-структуру без адаптации под RU-бизнес |
| 5 | [happyfox.com/compare/n8n-vs-make](https://www.happyfox.com/compare/n8n-vs-make/) | Comparison EN (2026) | Credits transition Aug 2025, hidden AI costs, Series C n8n | Affiliate-тон, нет чеклиста | Цифры valuation без бизнес-контекста для SMB |
| 6 | [flow-masters.ru/blog/n8n-vs-make-vs-zapier](https://flow-masters.ru/blog/n8n-vs-make-vs-zapier/) | Трёхстороннее RU | Доступность из РФ, self-host, ФЗ-152 | Zapier уводит фокус; цены Make «$16–29» устарели | Тройное сравнение — размывает H1 |
| 7 | [omidsaffari.com/blog/n8n-vs-make](https://omidsaffari.com/blog/n8n-vs-make) | Pricing math EN (2026) | Точка перелома ~5,6 шагов/запуск, live annual rates | Только EN, нет compliance RU | Копировать crossover без пояснения формулы |
| 8 | [claudelab.ru/journal/guides/n8n-ili-make](https://claudelab.ru/journal/guides/n8n-ili-make) | SMB guide RU | Простой язык для малого бизнеса | Поверхностная таблица, мало AI/MCP | Generic «выберите по вкусу» |

**Паттерн SERP:** топ — «n8n или Make 2026» с таблицей цен и сценариями «берите X если…». Сильный кластер — AI-агенты, self-host, credits Make. Слабое место конкурентов: нет **пошагового калькулятора TCO** + **12-вопросного чеклиста** в одной статье с гибридной схемой 2026.

**Intent:** comparison — читатель хочет **принять решение** (платформа + тариф), а не «узнать что такое n8n». Вторичный intent: self-hosted vs cloud, AI/RAG, 152-ФЗ, стоимость на объёме.

**Пробел для «Ковчег»:** практик Make (Артур) даёт честное сравнение с **формулой расчёта**, таблицей критериев, чеклистом 12 вопросов и гибридом n8n+Make — без фанатизма «только n8n».

---

## 2. Яндекс Wordstat

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` (инструмент `wordstat_get_top_requests`) **не подключён** в текущей Cloud-сессии. Вызов через GetDynamicTools — namespace не найден.

**Действие для пайплайна:** обновить OAuth-токен и MCP при необходимости:  
https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (без точных показов — API недоступен):**

| Кластер | Ожидаемый intent | LSI для writer |
|---------|------------------|----------------|
| Head | n8n, make com, integromat | n8n make сравнение, make vs n8n |
| Comparison | n8n или make, что выбрать | n8n или make com что выбрать, сравнение make и n8n |
| Self-host | n8n self hosted | n8n docker, n8n cloud, self hosted или make |
| Pricing | n8n цена, make тарифы | make credits, n8n executions, стоимость автоматизации |
| AI | n8n ai agent, make ai agents | langchain n8n, mcp n8n, rag n8n |
| Compliance RU | автоматизация 152 фз | данные на своих серверах, n8n self hosted россия |

**SEO-стратегия writer:** primary «n8n или make» в H1/lead; secondary «make vs n8n 2026», «n8n self hosted или make», «сравнение make и n8n» — в H2/H3 и FAQ. После восстановления Wordstat — перепроверить точные показы и подставить в meta/lead.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| n8n Cloud Starter: **20 €/мес** (годовая оплата), **2 500 executions**, unlimited steps | [n8n.io/pricing](https://n8n.io/pricing/) | 07.09.2026 | да |
| n8n Cloud Pro: **50 €/мес**, **10 000 executions** | [n8n.io/pricing](https://n8n.io/pricing/) | 07.09.2026 | да |
| n8n Business: **667 €/мес**, **40 000 executions**, self-hosted | [n8n.io/pricing](https://n8n.io/pricing/) | 07.09.2026 | да |
| **Execution** = один полный прогон workflow, **не каждый шаг** | [n8n.io/pricing](https://n8n.io/pricing/) | 07.09.2026 | да |
| Community Edition: self-hosted на GitHub, без cloud-лимита executions в лицензии | [n8n.io/pricing](https://n8n.io/pricing/) | 07.09.2026 | да |
| Hosted n8n: данные в **EU (Frankfurt)** | [n8n.io/pricing](https://n8n.io/pricing/) | 07.09.2026 | да |
| n8n trial Cloud: до **1 000 executions**, карта не нужна (Starter/Pro trial) | [n8n.io/pricing](https://n8n.io/pricing/) | 07.09.2026 | да |
| Make с **27.08.2025** перешёл с operations на **credits** (конверсия 1:1) | [help.make.com/coming-soon-credits…](https://help.make.com/coming-soon-credits-as-new-billing-unit-in-make) | 07.09.2026 | да |
| Стандартные модули Make: **1 credit = 1 operation**; AI-модули — **динамическое** списание (tokens, file size, runtime) | [help.make.com/coming-soon-credits…](https://help.make.com/coming-soon-credits-as-new-billing-unit-in-make) | 07.09.2026 | да |
| Make Free: **1 000 credits/мес**, 2 active scenarios | [cipherprojects.com](https://www.cipherprojects.com/blog/posts/n8n-vs-make-automation-platform-comparison/) | 07.09.2026 | да (перекрёстно с help.make) |
| Make Core: **$9/мес**, **10 000 credits**; Pro **$16**, Teams **$29** (10K credits, различаются фичи) | [cipherprojects.com](https://www.cipherprojects.com/blog/posts/n8n-vs-make-automation-platform-comparison/) | 07.09.2026 | да |
| Make **нельзя self-host** — только cloud SaaS | [cipherprojects.com](https://www.cipherprojects.com/blog/posts/n8n-vs-make-automation-platform-comparison/) | 07.09.2026 | да |
| n8n native nodes **400+** + community **600+**; Make native apps **1 500+** | [cipherprojects.com](https://www.cipherprojects.com/blog/posts/n8n-vs-make-automation-platform-comparison/) | 07.09.2026 | да |
| n8n: AI Agent node, LangChain, memory, vector stores, tool-routing | [cipherprojects.com](https://www.cipherprojects.com/blog/posts/n8n-vs-make-automation-platform-comparison/) | 07.09.2026 | да |
| n8n instance-level **MCP server** + MCP Client Tool / MCP Server Trigger nodes | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 07.09.2026 | да |
| Make AI Provider / AI Toolkit: credits по tokens + operations; сторонние OpenAI/Anthropic — Make credits за ops + оплата провайдеру за tokens | [help.make.com/credits](https://help.make.com/credits) | 07.09.2026 | да |
| Self-hosted n8n на VPS: **~$5–15/мес** server only (Community) | [cipherprojects.com](https://www.cipherprojects.com/blog/posts/n8n-vs-make-automation-platform-comparison/) | 07.09.2026 | да |
| Точка перелома цены: при **~5,6+ billable actions/run** n8n Pro выгоднее Make Core на 10K credits | [omidsaffari.com/blog/n8n-vs-make](https://omidsaffari.com/blog/n8n-vs-make) | 07.09.2026 | да (как ориентир, дать формулу читателю) |
| Make.com: **2 500+** нативных интеграций; тарификация с учётом compute для медиа/AI | [fact-bank / mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 2026-06-11 | да |
| Self-hosted n8n снижает накладные на медиа; **+35% маржи** у контент-агентств (кейс) | [fact-bank / mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 2026-06-11 | да (как кейс, не как универсальная статистика) |
| Make: прототип пайплайна **на 40% быстрее** за счёт визуального отладчика | [fact-bank / mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 2026-06-11 | да |
| Базовый ИИ-завод: **~$150/мес** API + no-code (Make/n8n) | [fact-bank](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026-06-11 | да |
| Курс Make kv-ai.ru: **5 800 ₽/мес**, 159+ уроков | site-brief | 07.09.2026 | да (единственный верифицированный CTA-продукт) |

**Не использовать без первичника:** «экономия 90%», «500 000+ users Make», «$180M Series C n8n» (happyfox — вторичный); «12% cloud outages 2025» (mayai.ru без источника); абсолютные «150–200K ₽/год» без формулы.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** читатель **пересчитывает свой объём**, заполняет **таблицу сравнения n8n vs Make** по 6 критериям (self-host, 152-ФЗ, AI, интеграции, лимиты, цена), проходит **чеклист 12 вопросов** и фиксирует решение: Make / n8n Cloud / n8n self-hosted / **гибрид**.

**Почему отличается от конкурентов:**
- Большинство статей — статичная таблица «n8n лучше для dev». Мало **actionable калькулятора**: runs × steps → credits vs executions.
- «Ковчег»: практик Make честно говорит «берите Make если…», даёт гибрид (Make фронт + n8n бэкенд), CTA на обучение Make для non-DevOps аудитории.

**Tone:** по-человечески; execution, credits, MCP, LangChain, 152-ФЗ — сразу «на пальцах». Без войны платформ.

**H2-каркас (из карточки B06 + research):**
1. Критерии выбора: self-hosting, 152-ФЗ, AI-агенты, стоимость операций
2. Таблица сравнения n8n vs Make (интеграции, LangChain, MCP, лимиты, цены)
3. Сценарии «берите Make»: маркетинг, быстрый старт, малые объёмы
4. Сценарии «берите n8n»: AI/RAG, большие данные, local LLM, compliance
5. Гибрид 2026: n8n для пайплайнов + Make для SaaS-интеграций
6. Чек-лист решения: 12 вопросов + FAQ

---

## 5. action_outline (writer)

1. **Посчитать месячный объём:** сколько раз в месяц запускается типовой сценарий (runs) и сколько модулей/шагов в среднем (steps).
2. **Перевести в billing-единицы:** Make credits ≈ runs × steps; n8n cloud = runs (executions); self-hosted n8n = runs без лимита + VPS.
3. **Сверить с тарифами 09.2026:** Make Free/Core/Pro vs n8n Starter/Pro vs VPS $5–40.
4. **Проверить compliance:** нужны ли данные на своих серверах (152-ФЗ, NDA) → если да, self-hosted n8n или on-prem agent Make Enterprise.
5. **Оценить AI-сложность:** RAG/мультиагент/MCP/local LLM → n8n; простые GPT-вызовы в SaaS-связке → Make.
6. **Оценить команду:** есть ли DevOps/Docker → если нет, Make или n8n Cloud; если да — Community Edition.
7. **Прогнать один pilot-сценарий** (webhook → CRM → уведомление) на выбранной платформе за 1–2 часа.
8. **Заполнить чеклист 12 вопросов** из H2 и зафиксировать решение в одном предложении.
9. **Если объём растёт:** спланировать гибрид (Make для триггеров/SaaS, n8n для тяжёлых пайплайнов) или миграцию по migration map.

---

## 6. reader_outcome

После статьи читатель **пересчитает TCO на своём объёме**, заполнит сравнительную таблицу и **выберет платформу и тариф** (Make / n8n Cloud / n8n self-hosted / гибрид) с обоснованием по 152-ФЗ, AI и бюджету — без «вечного а что лучше».

---

## 7. utility_verdict

**utility_verdict:** PASS

**Обоснование:** search_intent = comparison, article_mode = B; action_outline из 9 шагов; reader_outcome = конкретное решение + тариф; угол = таблица + калькулятор + чеклист, не обзор «что такое n8n».

---

## 8. Риски и blockers для writer / QA

| Риск | Митигация |
|------|-----------|
| Wordstat без точных показов | Не выдумывать «X показов/мес»; после восстановления MCP — дополнить |
| Make pricing page блокирует bot | Опираться на help.make.com + cipherprojects + cross-check |
| Разные цифры интеграций (400 vs 1200 vs 3000) | В таблице: «400+ native (n8n.io/docs) / 1500+ apps (Make help)» с footnote |
| Compliance 152-ФЗ | Формулировка «self-hosted даёт контроль локации данных; юридическую оценку — с юристом» |
| Cannibalization mayai.ru | Новый угол: калькулятор TCO + 12 вопросов + гибрид; не копировать mayai 1:1 |

**Handoff writer:** primary_query «n8n или make»; secondary из research-context; CTA max 3 (kv-ai.ru, telegram, pilot checklist).

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B06
article_dir: memory/blog/articles/B06-sravnenie-n8n-i-make-2026
status: ✅ PASS
utility_verdict: PASS
utility_gate_topic: PASS
wordstat: ⚠️ MCP user-mcp-kv недоступен — точные показы не получены
summary: SERP — 8 конкурентов (mayai.ru, aibotmanager, ai-uchi, cipherprojects, happyfox, flow-masters, omidsaffari, claudelab). Угол — comparison с TCO-калькулятором (runs×steps→credits vs executions), таблица 6 критериев, сценарии Make/n8n, гибрид 2026, чеклист 12 вопросов. 20 фактов с URL (n8n.io/pricing, help.make.com credits). action_outline 9 шагов. Готов к writer.
===
