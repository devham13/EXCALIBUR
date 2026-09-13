# Research notes — B06 «Сравнение n8n, Make и Zapier для ИИ-автоматизации: что выбрать в 2026 году»

**topic_id:** B06  
**slug:** sravnenie-n8n-make-zapier-2026  
**article_mode:** B (comparison + decision matrix)  
**research_date:** 2026-09-13  
**disclaimer:** Все даты, версии и статистика проверены на 13.09.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch + research-serp.json, 10 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [automationatlas.io/guides/zapier-vs-make-vs-n8n-comparison](https://automationatlas.io/guides/zapier-vs-make-vs-n8n-comparison/) | EN comparison 2026 | TCO, self-hosted, AI-агенты, оплата из РФ, таблица решений | Узкий фокус на EN-аудиторию | Копировать таблицу без пересчёта под RU-кейсы |
| 2 | [atlasceo.ru/build/atlas-26-zapier-vs-make-vs-n8n](https://atlasceo.ru/build/atlas-26-zapier-vs-make-vs-n8n-polnoe-sravnenie-dlya-biznesa-2026) | RU longread | TCO, кейсы интеграций, прогноз 2026 | Мало пошаговой матрицы выбора | Sales-CTA агентства вместо DIY-матрицы |
| 3 | [blog.nooka.pro/n8n-vs-make-zapier](https://blog.nooka.pro/n8n-vs-make-zapier/) | RU comparison | 8 критериев, MCP, data-residency | Bias в сторону n8n | Непроверенные цифры «доступность в РФ» |
| 4 | [blog.leadup.guru/ru/n8n-vs-make-vs-zapier](https://blog.leadup.guru/ru/n8n-vs-make-vs-zapier) | RU для AI-команд | ROI, сценарии внедрения | Нет единого калькулятора объёма | Обещания «40+ внедрений» без методики |
| 5 | [easytarget.com.ua/ru/blog/make-vs-zapier-vs-n8n-2026](https://easytarget.com.ua/ru/blog/make-vs-zapier-vs-n8n-2026/) | RU/UA | AI-агенты, MCP, 8 критериев | Перегруз новостным углом | Новостной lead без action |
| 6 | [mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | RU n8n vs Make | Матрица 6 сценариев, чеклист 15 пунктов | Только две платформы, без Zapier | Контент-завод bias; не копировать структуру 1:1 |
| 7 | [vladlyamin.ru/blog/n8n-vs-zapier-vs-make-com](https://vladlyamin.ru/blog/n8n-vs-zapier-vs-make-com-chto-vybrat-dlya-malogo-biznesa-v-2026) | RU SMB | Цены 2026, оплата из России | Слабый блок по AI Agent node | Устаревшие «операции» без credits |
| 8 | [gptmag.ru/make-vs-zapier-vs-n8n-2026](https://gptmag.ru/make-vs-zapier-vs-n8n-2026/) | RU no-code | 4 параметра выбора, таблица тарифов | Free n8n Cloud указан как 200 runs (устарело) | Цифры без первичника |
| 9 | [zapier.com/blog/zapier-vs-make](https://zapier.com/blog/zapier-vs-make/) | Официальный comparison | Credits vs tasks, 9000+ apps, hands-on 2026 | Нет n8n; продаёт Zapier | Маркетинг Zapier без баланса |
| 10 | [parseur.com/blog/zapier-n8n-make](https://parseur.com/blog/zapier-n8n-make) | EN three-way | Billing units, таблица 9 критериев, TCO math | Нет RU-контекста и ИИ-матрицы | Копировать таблицу без адаптации |

**Паттерн SERP:** доминируют comparison-longread «Zapier vs Make vs n8n 2026» с таблицами цен и AI-углом (MCP, agents). Отдельный кластер — «n8n или Make» без Zapier. Пробел: **единая матрица выбора под ИИ-автоматизацию** (агенты, RAG, LLM-расходы) + **пошаговый пересчёт одного эталонного сценария** в tasks/credits/executions — редко делают честно.

**Intent:** comparison — читатель хочет выбрать платформу для ИИ-автоматизации, а не «узнать что такое n8n». Вторичные: n8n или make что лучше; make vs zapier 2026; доступность/данные для RU-бизнеса.

**Дифференциатор для блога:** таблица **15 параметров** + **матрица 6 бизнес-сценариев** + **калькулятор одного workflow** (4–10 шагов × N прогонов) → конкретная рекомендация «берите X / не берите Y».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

**Статус:** MCP-сервер `user-mcp-kv` недоступен в текущей среде Cloud Agent (namespace не подключён).

Точные объёмы спроса по фразе «сравнение n8n make zapier» **не получены**. Writer использует LSI из SERP и secondary_queries карточки B06; при появлении Wordstat — дополнить таблицу спроса.

### LSI-ключи (экспертная семантика из SERP, без цифр Wordstat)

| Кластер | Фразы |
|---------|-------|
| Сравнение | сравнение n8n make zapier, n8n vs make vs zapier 2026, make vs zapier vs n8n |
| Выбор | n8n или make что лучше, что выбрать для бизнеса, какую платформу выбрать |
| Цена/TCO | make vs zapier цена 2026, n8n self-hosted стоимость, credits vs tasks vs executions |
| AI | ai agent n8n, make ai agents, zapier ai by zapier, mcp n8n make zapier, langchain n8n |
| RU-контекст | автоматизация для бизнеса россия, self-hosted n8n, оплата make из россии |
| Миграция | заменить zapier на n8n, migrate make to n8n, перенос сценариев |

---

## 3. Таблица фактов (цифры только с URL)

| # | Факт | Источник | Дата | Можно в текст |
|---|------|----------|------|---------------|
| 1 | n8n Cloud Starter: **20 €/мес** (годовая оплата), **2 500 executions**, 5 concurrent | [n8n.io/pricing](https://n8n.io/pricing/) | 13.09.2026 | да |
| 2 | n8n Cloud Pro: **50 €/мес**, **10 000 executions**, 20 concurrent | [n8n.io/pricing](https://n8n.io/pricing/) | 13.09.2026 | да |
| 3 | n8n Business: **667 €/мес**, **40 000 executions**, SSO/SAML, Git version control | [n8n.io/pricing](https://n8n.io/pricing/) | 13.09.2026 | да |
| 4 | n8n: **execution = один полный прогон workflow**, шаги внутри не умножают счёт | [n8n.io/pricing](https://n8n.io/pricing/) | 13.09.2026 | да |
| 5 | Community Edition: **self-hosted бесплатно** (GitHub), unlimited users & workflows | [n8n.io/pricing](https://n8n.io/pricing/) | 13.09.2026 | да |
| 6 | Hosted n8n: данные в **EU (Frankfurt)** | [n8n.io/pricing](https://n8n.io/pricing/) | 13.09.2026 | да |
| 7 | n8n Cloud AI Assistant credits: **2 300/мес** (Starter), до **13 700/мес** (Pro) | [n8n.io/pricing](https://n8n.io/pricing/) | 13.09.2026 | да |
| 8 | Один workflow run с AI Agent = **1 execution** (1000 email summaries = 1 run, если в одном workflow) | [community.n8n.io](https://community.n8n.io/t/costs-and-limitations-of-ai-agents-on-cloud-n8n/234147) | 10.12.2025 | да |
| 9 | Make Free: **1 000 credits/мес**, **2 active scenarios**, интервал расписания **15 мин** | [make.com/en/pricing](https://www.make.com/en/pricing) | 13.09.2026 | да |
| 10 | Make Core/Pro/Teams (paid): базово **10 000 credits/мес**; тарифы отличаются фичами, не объёмом | [make.com/en/pricing](https://www.make.com/en/pricing) | 13.09.2026 | да |
| 11 | Make: **3 000+ standard apps**, **350+ AI apps** | [make.com/en/pricing](https://www.make.com/en/pricing) | 13.09.2026 | да |
| 12 | Make: с **27.08.2025** billing unit — **credits** (ранее operations); для non-AI apps **1 operation = 1 credit** | [help.make.com/credits](https://help.make.com/credits) | 11.09.2026 | да |
| 13 | Make AI features: credits по **tokens + operations** (Make AI Provider) или operations + оплата провайдеру (custom key) | [help.make.com/credits](https://help.make.com/credits) | 11.09.2026 | да |
| 14 | Make AI Agents и MCP Server доступны на тарифах (Make AI Provider — all plans) | [make.com/en/pricing](https://www.make.com/en/pricing) | 13.09.2026 | да |
| 15 | Zapier Free: **100 tasks/мес**, two-step Zaps, unlimited Zap workflows | [zapier.com/pricing](https://zapier.com/pricing) | 13.09.2026 | да |
| 16 | Zapier Pro 750: **$19.99/мес** (annual), **750 tasks** | [zapier.com/pricing](https://zapier.com/pricing) | 13.09.2026 | да |
| 17 | Zapier Team 2 000: **$69/мес** (annual), **2 000 tasks**, до **25 users** | [zapier.com/pricing](https://zapier.com/pricing) | 13.09.2026 | да |
| 18 | Zapier: **9 000+ apps** | [zapier.com/pricing](https://zapier.com/pricing) | 13.09.2026 | да |
| 19 | Zapier billing: **1 successful step = 1 task**; Filters, Paths, Formatter **не считаются** в task limit | [zapier.com/blog/zapier-pricing](https://zapier.com/blog/zapier-pricing/) | 13.09.2026 | да |
| 20 | AI by Zapier: multipliers **1x / 3x / 5x** tasks по tier модели; tool calls умножаются | [help.zapier.com](https://help.zapier.com/hc/en-us/articles/46425475442829-AI-by-Zapier-model-tier-pricing) | 13.09.2026 | да |
| 21 | Zapier MCP: **2 tasks** за успешный tool call | [docs.zapier.com/mcp/features/usage](https://docs.zapier.com/mcp/features/usage) | 13.09.2026 | да |
| 22 | Pay-per-task: лимит **3×** plan allowance (plan + overage) | [help.zapier.com](https://help.zapier.com/hc/en-us/articles/15279018245901-How-pay-per-task-billing-works-in-Zapier) | 13.09.2026 | да |
| 23 | Make.com: **2 500+** нативных интеграций; тарификация Compute Units удорожает video/media (fact-bank) | [mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 11.06.2026 | да (контекст, не primary для «3000+») |
| 24 | Self-hosted n8n vs облачный Make: снижение накладных на медиа, **+35% маржи** контент-производства (кейс) | [mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 11.06.2026 | да (как кейс, не универсальная цифра) |
| 25 | Базовая автоматизированная ИИ-система: **~$150/мес** API + no-code (Make/n8n) | [mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 11.06.2026 | да (диапазон бюджета) |

**Эталонный пересчёт (writer строит таблицу):** workflow из **5 шагов**, **2 000 прогонов/мес** → Zapier ≈ **10 000 tasks**, Make ≈ **10 000 credits** (если каждый модуль = 1 credit), n8n Cloud ≈ **2 000 executions**. LLM API оплачивается отдельно на всех трёх.

**Не использовать без первичника:** «Zapier заблокирован в РФ» (только как паттерн SERP + осторожная формулировка); «Make не принимает карты РФ» — вторичные блоги; точные $ Core/Pro Make — указывать диапазон annual/monthly со ссылкой на make.com/en/pricing.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** читатель **пересчитывает свой объём**, заполняет **сводную таблицу 15 параметров** и по **матрице 6 сценариев** выбирает одну платформу (или пару: n8n + Make) для **ИИ-автomatизации в 2026** — без «вечного а что лучше».

**Почему отличается от конкурентов:**
- Большинство статей — пересказ тарифов; мало **единого калькулятора** tasks/credits/executions на одном кейсе.
- AI-фокус: не «есть ли AI», а **глубина** (LangChain/agents/RAG/MCP vs AI Actions vs Make AI Agents).
- Позиция блога: практик автоматизации; честно — Zapier для простых связок EN-рынка, Make для no-code команды, n8n для агентов/self-host/compliance.

**Tone:** без fanboy n8n и без dismiss Make. Каждый H2 = критерий + **рекомендация** (брать / не брать).

**H2-каркас (из карточки B06):**
1. Критерии выбора платформы автоматизации с ИИ в 2026
2. n8n: self-hosted, AI Agent node, стоимость, типовые сценарии
3. Make.com: облако, AI-модули, credits, интеграции
4. Zapier: простота, AI Actions, tasks, ограничения
5. **Сводная таблица: 15 параметров**
6. **Матрица выбора: 6 сценариев + когда мигрировать**

**Internal link:** `/avtomatizaciya-n8n-ai-agents/` (из карточки)

---

## 5. Черновик таблицы 15 параметров (для writer)

| # | Параметр | n8n | Make | Zapier |
|---|----------|-----|------|--------|
| 1 | Billing unit | Execution (весь run) | Credit (обычно 1 модуль = 1) | Task (обычно 1 step = 1) |
| 2 | Free tier | CE self-host ∞ runs; Cloud trial 1000 exec | 1000 credits, 2 scenarios | 100 tasks, 2-step Zaps |
| 3 | Entry paid | 20 €/мес, 2500 exec | Paid от Core (~$9–16/mo annual) | $19.99/mo, 750 tasks |
| 4 | Self-host | ✅ CE + license Business | ❌ | ❌ |
| 5 | Data residency | Где хостите / EU cloud | Cloud Make (EU) | US/EU cloud |
| 6 | Integrations | All nodes + community + HTTP | 3000+ apps | 9000+ apps |
| 7 | Visual builder | Node canvas | Scenario canvas (лучше ветвления) | Linear Zaps |
| 8 | Custom code | JS/Python nodes | Make Code (dynamic credits) | Code step (limited) |
| 9 | AI agents depth | Native AI Agent, LangChain, vector stores | Make AI Agents, AI Toolkit | AI by Zapier, Agents add-on |
| 10 | MCP | MCP Client/Server nodes | Make MCP Server | Zapier MCP (2 tasks/call) |
| 11 | Multi-step cost at scale | Низкий (executions) | Средний (credits) | Высокий (tasks) |
| 12 | AI billing predictability | Executions + LLM API; AI Assistant credits on cloud | Dynamic credits for AI Provider | 1x/3x/5x task multipliers |
| 13 | Team / SSO | Business+ / Enterprise | Teams / Enterprise | Team 25 seats / Enterprise |
| 14 | Learning curve | Круче | Средняя | Самая низкая |
| 15 | Best for AI automation 2026 | Агенты, RAG, self-host, high volume | No-code AI scenarios, CRM/SMM | Быстрые 2–5 step связки, max apps |

---

## 6. Матрица выбора (6 сценариев)

| Сценарий | Рекомендация | Не брать |
|----------|--------------|----------|
| 1. «2–3 простые связки CRM ↔ почта, <500 runs» | **Make** (Free/Core) или Zapier если EN-рынок | n8n self-host (overkill) |
| 2. «ИИ-агент с RAG, памятью, 10+ tools, compliance» | **n8n** (self-host или Cloud Pro) | Zapier (нет agent framework) |
| 3. «No-code команда, визуальные ветки, AI без DevOps» | **Make** Pro + custom LLM key | n8n без техподдержки |
| 4. «10k+ multi-step runs/мес, tight budget» | **n8n** self-host или Cloud | Zapier (task wall) |
| 5. «Максимум SaaS-интеграций, zero ops, US/EU SaaS OK» | **Zapier** Team | n8n (ops burden) |
| 6. «MCP: AI-клиент дергает автоматизации» | **n8n MCP** или **Make MCP**; Zapier MCP — если уже на Zapier (2 tasks/call) | — |

**Миграция:** Make/Zapier → n8n когда TCO tasks/credits > executions + нужен self-host; n8n → Make когда нет ресурса на Docker/patches.

---

## 7. FAQ-кандидаты (из карточки + research)

1. **n8n или Make что лучше для малого бизнеса?** — Make если нет DevOps; n8n CE если есть VPS и >3k multi-step runs.
2. **Можно ли заменить Zapier на n8n?** — да, через HTTP/webhooks + community nodes; миграция по одному workflow.
3. **Есть ли AI в Make.com?** — Make AI Agents, AI Toolkit, AI Provider на всех планах; credits для AI динамические.
4. **Что дешевле на 5000 прогонов 8-шагового workflow?** — n8n ≈5000 exec; Make ≈40k credits; Zapier ≈40k tasks — пересчитать в статье.
5. **Нужен ли self-host для ИИ-агентов?** — нет, но self-host даёт контроль данных и снимает execution cap.
6. **Zapier vs Make в 2026?** — Zapier: tasks + 9000 apps + проще; Make: credits + canvas + дешевле на объёме.
7. **Скрытые costs?** — LLM API на всех; Make AI Provider tokens; Zapier AI 5x default Premium tier.

---

## 8. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «ИИ-автоматизация на no-code» 40–60 слов | Lead | Сразу после H1 |
| Таблица 15 параметров | H2-5 | Markdown/HTML table |
| Матрица 6 сценариев | H2-6 | Table + «если → то» |
| Калькулятор эталонного workflow | H2-1 или H2-5 | Числовой пример с формулой |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | schema agent | BlogPosting + FAQPage |

**Целевые формулировки:** сравнение n8n make zapier, n8n или make что лучше, make vs zapier 2026, ai автоматизация make n8n.

---

## 9. Риски для writer

- Цены Make USD — сверять на [make.com/en/pricing](https://www.make.com/en/pricing) в день публикации; не фиксировать устаревшие «operations».
- Не копировать atlasceo/gptmag 1:1.
- Объём: 8 500–9 500 знаков (quality-blog).
- Comparison: min **таблица 15 параметров** + **матрица 6 сценариев** + **чеклист 10+ пунктов** перед выбором (utility gate статьи).
- RU-доступность — только осторожно, без категоричных блокеров без primary source.
- Internal link на B02 `/avtomatizaciya-n8n-ai-agents/` где уместно.

---

## 10. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель пересчитает свой месячный объём в tasks/credits/executions на эталонном ИИ-workflow, заполнит таблицу 15 параметров, выберет n8n, Make или Zapier по матрице 6 сценариев и зафиксирует план миграции или пилота на free tier.

**action_outline (для writer):**

1. **Зафиксировать 1–2 ключевых ИИ-сценария** (лиды, support-бот, контент-pipeline) и число прогонов/мес.
2. **Посчитать шаги** в каждом сценарии (trigger + actions + AI nodes).
3. **Перевести объём** в три единицы: Zapier tasks, Make credits, n8n executions — одна таблица «один кейс — три счёта».
4. **Добавить LLM API** (~$50–150/мес baseline из fact-bank) отдельной строкой TCO.
5. **Заполнить таблицу 15 параметров** (раздел 5) с рекомендацией по каждому блоку H2.
6. **Пройти матрицу 6 сценариев** (раздел 6) и выбрать primary + optional secondary platform.
7. **Пилот:** зарегистрировать free tier выбранной платформы, собрать MVP одного сценария за 1–2 часа.
8. **Чеклист 10+ пунктов** перед оплатой: data residency, SSO, AI billing, concurrency, webhook limits, миграция credentials.
9. **Зафиксировать решение** в 3 строках: платформа, тариф, дата пересмотра через 90 дней.

---

## 11. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | ✅ PASS |
| SERP ≥ 3 конкурента | ✅ (10) |
| Wordstat MCP | ⚠️ недоступен (не блокер) |
| Таблица фактов с URL | ✅ (25 фактов) |
| utility_verdict + action_outline | ✅ |
| Comparison table + matrix | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + `fact-bank.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B06
article_dir: memory/blog/articles/B06-sravnenie-n8n-make-zapier-2026
status: ✅ PASS
utility_verdict: PASS
wordstat: ⚠️ MCP user-mcp-kv недоступен — LSI из SERP
summary: SERP — 10 конкурентов (automationatlas, atlasceo, nooka, leadup, mayai, vladlyamin, gptmag, zapier.com, parseur). Угол — comparison: таблица 15 параметров + матрица 6 сценариев + пересчёт tasks/credits/executions на эталонном ИИ-workflow. 25 фактов с URL (n8n/make/zapier pricing официально). 9 шагов action_outline, 7 FAQ. Готов к writer.
===
