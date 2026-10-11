# Research notes — B06 «Сравнение Make, Zapier и n8n в 2026: как выбрать платформу автоматизации для бизнеса»

**topic_id:** B06  
**slug:** sravnenie-make-zapier-n8n-2026  
**article_mode:** B (comparison + чек-листы + migration how-to)  
**research_date:** 2026-10-11  
**disclaimer:** Все даты, версии и статистика проверены на 11.10.2026.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [automationatlas.io/guides/zapier-vs-make-vs-n8n-comparison](https://automationatlas.io/guides/zapier-vs-make-vs-n8n-comparison/) | EN, data-driven 2026 | Параллельный 90-day test, pricing at scale, MCP/AI | Мало РФ/152-ФЗ; EN-only | Цифры без перепроверки по первичникам |
| 2 | [blog.leadup.guru/ru/n8n-vs-make-vs-zapier](https://blog.leadup.guru/ru/n8n-vs-make-vs-zapier) | RU comparison | Оплата из РФ, AI-агенты, таблица критериев | Слабая миграция Make→n8n | Пересказ без чек-листа compliance |
| 3 | [atlasceo.ru/build/atlas-619-zapier-vs-make-vs-n8n-chto-vybrat-biznesu-v-2026-godu](https://atlasceo.ru/build/atlas-619-zapier-vs-make-vs-n8n-chto-vybrat-biznesu-v-2026-godu/) | RU business | TCO, «российские реалии» | Длинный sales-тон | Структура 1:1 |
| 4 | [prog.academy/ru/blog/n8n-vs-make-vs-zapier-2026](https://prog.academy/ru/blog/n8n-vs-make-vs-zapier-2026) | RU AI-angle | MCP, data residency | Узкий AI-фокус | Bias «только n8n» |
| 5 | [zapier.com/blog/n8n-vs-make](https://zapier.com/blog/n8n-vs-make/) | Официальный блог Zapier | Billing models (tasks vs credits vs executions) | Zapier в центре; нет self-host n8n depth | Маркeting Zapier без блока РФ |
| 6 | [make.com/en/compare/make-vs-n8n](https://www.make.com/en/compare/make-vs-n8n) | Официальный Make | Таблица цен Make vs n8n Cloud, 3 500+ apps | One-sided; n8n self-host TCO упрощён | Копировать аргументы Make без баланса |
| 7 | [itoq.ru/blog/n8n-ili-make-chto-vybrat-dlya-avtomatizacii-biznesa-v-2026](https://itoq.ru/blog/n8n-ili-make-chto-vybrat-dlya-avtomatizacii-biznesa-v-2026) | RU Make vs n8n | Чек-лист 15 пунктов, матрица сценариев | Нет Zapier в тройке | — |
| 8 | [doit.software/blog/n8n-vs-make-vs-zapier](https://doit.software/blog/n8n-vs-make-vs-zapier) | EN three-way | Sales/marketing automation angle | Слабо про РФ и миграцию | — |

**Паттерн SERP:** доминируют таблицы «цена + интеграции + self-host»; русскоязычные статьи добавляют «Zapier недоступен / оплата из РФ», но редко дают **пошаговую миграцию Make→n8n** и **compliance-чек-лист 152-ФЗ** в одном материале.

**Intent:** comparison — выбрать платформу под объём, данные, AI и команду; вторично — миграция и альтернатива Zapier для РФ.

**Пробел для «Ковчег»:** decision tree + 4 критерия из карточки B06, честная позиция практика Make (Артур): когда Make быстрее, когда n8n self-host обязателен, Zapier — legacy/миграция; план миграции с blueprint + parallel run; internal link на B02.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

**⚠️ WORDSTAT MCP UNAVAILABLE:** в этом Cloud Agent run namespace `user-mcp-kv` и инструмент `wordstat_get_top_requests` не подключены. **Точные показы/мес не получены** — в тексте статьи не использовать выдуманные объёмы спроса.

**Семантика из SERP + secondary_queries (LSI для writer, без частот):**

- n8n vs make vs zapier / сравнение make n8n zapier  
- make или n8n что выбрать / n8n vs make 2026  
- zapier альтернатива для россии / make вместо zapier  
- тарифы make credits / zapier tasks / n8n executions  
- self-hosted n8n docker / 152-фз персональные данные автоматизация  
- миграция make на n8n blueprint  
- make ai agents / n8n ai agent node / mcp  

**SEO-стратегия:** primary EN-запрос в H2-синонимах + RU secondary в подзаголовках; акцент на «Россия 2026», «чек-лист», «миграция».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| n8n Cloud Starter: **20 €/мес** (годовая оплата); Pro **50 €/мес**; Business **667 €/мес** | [n8n.io/pricing](https://n8n.io/pricing/) | 11.10.2026 | да |
| n8n: **execution** = один полный прогон workflow, независимо от числа шагов | [n8n.io/pricing](https://n8n.io/pricing/) | 11.10.2026 | да |
| n8n Community Edition: self-hosted, исходники на GitHub | [n8n.io/pricing](https://n8n.io/pricing/) | 11.10.2026 | да |
| n8n Cloud: данные hosted-планов в **EU (Frankfurt)** | [n8n.io/pricing](https://n8n.io/pricing/) | 11.10.2026 | да |
| n8n Cloud trial: **14 дней**, карта не нужна (Starter/Pro trial) | [n8n.io/pricing](https://n8n.io/pricing/) | 11.10.2026 | да |
| n8n: **500+** интеграций (nodes) на сайте продукта | [n8n.io](https://n8n.io/) | 11.10.2026 | да |
| n8n stable **2.42.6** (beta 2.43.3) — актуальная ветка на дату docs | [docs.n8n.io/hosting/installation/docker](https://docs.n8n.io/hosting/installation/docker/) | 11.10.2026 | да |
| Make Free: **1 000 credits/мес**, min interval **15 мин**, max **2** active scenarios | [make.com/en/pricing](https://www.make.com/en/pricing) | 11.10.2026 | да |
| Make: **3 500+** standard apps; hosting **AWS (EU/North America)** | [make.com/en/pricing](https://www.make.com/en/pricing) | 11.10.2026 | да |
| Make: billing unit — **credits** (с **27 августа** credits как единица; большинство модулей = 1 credit) | [make.com/en/pricing](https://www.make.com/en/pricing) | 11.10.2026 | да |
| Make: **Router** и error-handler модули **не** списывают credits | [make.com/en/pricing](https://www.make.com/en/pricing) | 11.10.2026 | да |
| Make Core **$9/мес**, **10 000 credits**; Pro **$16**; Teams **$29** (стартовые пакеты credits) | [make.com/en/compare/make-vs-n8n](https://www.make.com/en/compare/make-vs-n8n) | 11.10.2026 | да |
| Make Cloud Starter n8n-compare: n8n Cloud **$20/mo, 2 500 executions** (официальная таблица Make) | [make.com/en/compare/make-vs-n8n](https://www.make.com/en/compare/make-vs-n8n) | 11.10.2026 | да |
| Make AI Agents (beta) и MCP server — на **всех** тарифах в pricing matrix | [make.com/en/pricing](https://www.make.com/en/pricing) | 11.10.2026 | да |
| Blueprint Make: export **JSON** (modules, settings, mapped values); connections **не** входят | [help.make.com/blueprints](https://help.make.com/blueprints) | 11.10.2026 | да |
| Zapier: **9 000+** apps; модель **plan + task tier** | [zapier.com/pricing](https://zapier.com/pricing) | 11.10.2026 | да |
| Zapier Free: **100 tasks/mo**; two-step Zaps на Free | [zapier.com/pricing](https://zapier.com/pricing) | 11.10.2026 | да |
| Zapier Pro annual entry tier: **750 tasks/mo за $19.99/mo** (при годовой оплате) | [zapier.com/pricing](https://zapier.com/pricing) | 11.10.2026 | да |
| Zapier: task = успешный шаг; **не** считаются triggers, polling, Paths/Filter/Delay и др. built-in tools | [zapier.com/pricing](https://zapier.com/pricing) | 11.10.2026 | да |
| Zapier Service и контент: инфраструктура в **США**; доступ из других стран — на риск пользователя | [zapier.com/legal/terms-of-service](https://zapier.com/legal/terms-of-service) | 11.10.2026 | да |
| Zapier ToS: пользователь **не** должен быть резидентом/находиться в стране под **действующими санкциями США** | [zapier.com/legal/terms-of-service](https://zapier.com/legal/terms-of-service) | 11.10.2026 | да |
| Make.com **>2 500** нативных интеграций; тарификация **Compute Units** для тяжёлых медиа/AI (контекст TCO) | [fact-bank / mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 11.06.2026 | да (с оговоркой «по mayai») |
| Self-hosted n8n vs облако: снижение накладных на медиа, рост маржи контент-производства до **35%** (кейс mayai) | [fact-bank / mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 11.06.2026 | да (кейс, не универсальная норма) |

**Не использовать без первичника:** «Zapier заблокирован с сентября 2024» только из vc.ru/dtf (допустимо как **практический контекст РФ** с оговоркой + опора на ToS/оплату); расчёты «$5 VPS = вся автоматизация» без вашего TCO-шаблона; «8 000 интеграций Zapier» vs «9 000+» — в статье брать **9 000+** с zapier.com/pricing.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** пройти **4 критерия выбора** (объём/тарификация, ПДн и 152-ФЗ, роль AI, техресурс), заполнить **сравнительную таблицу** (Make / Zapier / n8n Cloud / n8n self-host), выбрать платформу по **матрице ситуаций**; при смене Make→n8n — выполнить **миграцию без простоя** (blueprint → n8n, parallel run, смена webhook).

**Почему отличается от конкурентов:** связка comparison + compliance РФ + migration playbook; голос практика Make-клуба (не «n8n для всех»).

**Tone:** решения «делать / не делать» в каждом H2; Zapier — честно как legacy для РФ-команды.

**H2-каркас:** из `blog-topics.md` B06 (6 блоков) + FAQ из faq_hints.

**Conversion:** CTA курс Make [kv-ai.ru/obuchenie-po-make](https://kv-ai.ru/obuchenie-po-make) — max 2×, когда выбор = Make/no-code; internal `/avtomatizaciya-n8n-ai-agents/` после выбора n8n.

---

## 5. Comparison-матрица (черновик для writer)

| Критерий | Zapier | Make (cloud) | n8n Cloud | n8n self-hosted |
|----------|--------|--------------|-----------|-----------------|
| Единица оплаты | Tasks (успешные шаги) | Credits (модули) | Executions (весь workflow) | CE: лицензия $0 + infra |
| Старт цены (официально) | Free 100 tasks; Pro от $19.99/750 tasks | Free 1k credits; Core от $9/10k credits | от 20 €/мес Starter | VPS + DevOps |
| Интеграции | 9 000+ apps | 3 500+ apps | 500+ nodes + HTTP | то же |
| Self-host / РФ-local data | Нет | Нет | Нет (EU Frankfurt) | Да (ваш DC/VPS в РФ) |
| AI / MCP | Agents, MCP (tasks) | AI Agents, MCP server (все планы) | AI Agent node, MCP (Cloud) | Полный контроль, local LLM |
| Доступ из РФ (2026) | ToS/sanctions + US hosting; оплата RU-картой проблемна | Работает; данные EU/US AWS | Cloud EU; оплата как у SaaS EU | Полный контроль |
| Когда выбирать | Legacy, уже оплаченный западный стек | No-code, ветвления, быстрый старт | AI + managed без своего сервера | ПДн, объём, кастом API, AI depth |

**Billing-пример для writer (один кейс, не выдумывать цифры сверх таблицы):** сценарий на **4 шага**, **1 000 запусков/мес** → Zapier ≈ 4 000 tasks; Make ≈ 4 000 credits (если каждый модуль = 1 credit); n8n ≈ **1 000 executions**. Ссылка на модели: [zapier.com/pricing](https://zapier.com/pricing), [make.com/en/pricing](https://www.make.com/en/pricing), [n8n.io/pricing](https://n8n.io/pricing).

---

## 6. Миграция Make → n8n (факты для H2-4)

| Шаг | Действие | Источник |
|-----|----------|----------|
| Export | Make: ⋮ → **Export blueprint** → `.json` | [help.make.com/blueprints](https://help.make.com/blueprints) |
| Convert | Blueprint **не** импортируется в n8n напрямую; нужен ручной rebuild или сторонний конвертер + review | [n8n community converter thread](https://community.n8n.io/t/built-an-automated-converter-from-make-com-blueprints-to-n8n/298391) |
| Credentials | После import в n8n — **переподключить все credentials** (как и в Make после blueprint) | [help.make.com/blueprints](https://help.make.com/blueprints) |
| Parallel | Держать Make и n8n параллельно, сравнить выходы, затем сменить **webhook URLs** | [agentbrisk.com migrate guide](https://agentbrisk.com/blog/how-to-migrate-from-make-to-n8n/) |
| Self-host setup | Docker `n8nio/n8n`, volume, Postgres для prod | [docs.n8n.io/hosting/installation/docker](https://docs.n8n.io/hosting/installation/docker/) |

**Риск для writer:** конвертеры (n8nconvert.io и др.) — **не официальные**; помечать как опциональный ускоритель, не как гарантию паритета.

---

## 7. FAQ-кандидаты (5–7)

1. **Make или n8n для малого бизнеса в РФ?** — Make если нет DevOps и сценарии умеренные; n8n self-host если ПДн/объём/кастом API.
2. **Работает ли Zapier из России в 2026?** — опираться на ToS (sanctions), US hosting, проблемы оплаты; для новых проектов в РФ — Make/n8n.
3. **Почему n8n дешевле Make на больших объёмах?** — execution vs credits; self-host без лимита runs (infra отдельно).
4. **Можно ли перенести сценарий Make одной кнопкой?** — только blueprint JSON + ручная/полуавтоматическая сборка в n8n.
5. **Где хранятся данные Make и n8n Cloud?** — Make AWS EU/NA; n8n Cloud EU Frankfurt; self-host — где развернёте.
6. **Что насчёт 152-ФЗ?** — для ПДн граждан РФ типовой путь — **локализация** (self-host/VPS в РФ или российский провайдер); облако EU/US — юридическая оценка с DPO (не давать юр.гарантий в статье).
7. **Нужен ли Zapier в 2026?** — только если уже embedded в процессы и есть легальная оплата/доступ; иначе Make/n8n.

---

## 8. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «платформа автоматизации» 40–60 слов | Lead | Сравнение трёх моделей billing |
| Таблица 4 колонки | H2-2 | Make / Zapier / n8n Cloud / self-host |
| Decision matrix | H2-3 | «Если… → платформа» |
| Workflow миграции | H2-4 | Make live → export → n8n test → cutover |
| Чек-лист compliance 10+ пунктов | H2-5 | ПДн, webhook, логи |
| FAQ | Конец | Ответы-действия |

**Целевые формулировки:** «n8n vs make vs zapier», «сравнение make n8n zapier 2026», «zapier альтернатива россия», «make или n8n что выбрать», «миграция make n8n».

---

## 9. Риски для writer

- Цены — только из раздела 3; пересчитывать кейсы через tasks/credits/executions явно.
- Zapier в РФ — формулировки «риск / ToS / оплата», не категоричное «100% заблокирован» без официального status-анонса Zapier.
- Utility gate статьи: comparison-таблица + **≥10 пунктов чек-листа** + **≥5 нумерованных шагов** (миграция или «первая автоматизация»).
- Internal link: `/avtomatizaciya-n8n-ai-agents/` (B02).
- Без эмодзи; дефис вместо длинного тире.

---

## 10. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель по чек-листу из 4 критериев выберет Make, n8n Cloud или n8n self-hosted (и поймёт, когда Zapier не рассматривается), заполнит сравнительную таблицу под свой объём операций и при необходимости выполнит миграцию с Make на n8n через export blueprint, тестовый прогон и параллельный запуск без простоя.

**action_outline (для writer):**

1. **Зафиксировать профиль:** число сценариев, шагов на run, запусков/мес, есть ли ПДн РФ, нужны ли AI-агенты/MCP, есть ли DevOps.
2. **Пересчитать billing** в трёх единицах (tasks / credits / executions) на одном эталонном сценарии writer'а из раздела 5.
3. **Пройти чек-лист 4 критериев** (объём, 152-ФЗ/хранение, AI, техресурс) — отметить «Make / n8n Cloud / self-host / Zapier legacy».
4. **Заполнить таблицу сравнения** (раздел 5) и выбрать строку матрицы «ваша ситуация → платформа».
5. **Если выбран Make:** зарегистрировать Free, собрать первый сценарий ≤1 000 credits; CTA курс Make при нехватке no-code навыков.
6. **Если выбран n8n Cloud:** trial 14 дней, один workflow, проверить EU residency; link B02 для AI-агента.
7. **Если self-host:** Docker + volume (+ Postgres для prod), checklist security (backup, HTTPS, encryption key).
8. **Если миграция с Make:** export blueprint → rebuild/конвертер → credentials → parallel 3–7 дней → смена webhooks → отключить Make.
9. **Compliance РФ:** чек-лист где проходят ПДн, логи, subprocessors; эскалация к юристу при облаке EU/US.

---

## 11. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| Comparison + migration + РФ | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + `conversion-map.md`.
