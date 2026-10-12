# Research notes — B06 «Как настроить интеграцию amoCRM и n8n: заявки из Telegram и webhook без программиста»

**topic_id:** B06  
**slug:** integraciya-amocrm-n8n-2026  
**article_mode:** B (how-to + чеклист)  
**research_date:** 2026-10-12  
**disclaimer:** Все даты, версии и статистика проверены на 12.10.2026.

---

## 1. SERP-обзор (WebSearch, приоритет над research-serp.json)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [golubef.ru/blog/n8n-amocrm-integraciya](https://golubef.ru/blog/n8n-amocrm-integraciya) | Обзор сценариев | Таблица кейсов (заявка→сделка, статус, задачи, Telegram) | Мало OAuth/webhook guard, нет чеклиста prod | Общие фразы без пошаговых скриншотов/полей |
| 2 | [osipenkov.ru/amocrm-telegram-n8n-status](https://osipenkov.ru/amocrm-telegram-n8n-status/) | Практический how-to | amoМаркет WEBHOOKS → n8n Webhook → Telegram; import JSON | Только исходящий сценарий (статус), нет inbound lead | Копировать workflow 1:1 |
| 3 | [nodbot.ru/integrations/amocrm](https://nodbot.ru/integrations/amocrm/) | Production blueprint | Inbound normalize, dedupe, webhook loop guard, мониторинг 401/429 | Коммерческий контекст Nodbot | Продажный тон вместо DIY |
| 4 | [dzen.ru/a/ak5aIcpc2E9VDSDk](https://dzen.ru/a/ak5aIcpc2E9VDSDk) | Глубокий гайд | Community node, Redirect URL, leads/complex, типичные OAuth-ошибки | Цифры Wordstat без первичника MCP | Непроверенные объёмы спроса из статьи |
| 5 | [kalinkindev.ru/blog/n8n-scenario-leads-amocrm](https://kalinkindev.ru/blog/n8n-scenario-leads-amocrm/) | HTTP-only сценарий | Webhook → Set → search contact → `/leads/complex`, Error Trigger | Без Telegram trigger | Узкая структура без сравнения Make |
| 6 | [apimonster.ru/connector/bundle/n8n/amocrm](https://apimonster.ru/connector/bundle/n8n/amocrm/) | Коннектор SaaS | «Без программиста» через посредника | Не n8n-native, платная прослойка | Продавать ApiMonster вместо n8n |
| 7 | [new.amocrm.ru/developers/...](https://www.amocrm.ru/developers/content/crm_platform/webhooks-format) | Официальная дока | Формат x-www-form-urlencoded, установка в amoМаркет | Не про n8n | Сухой пересказ API без workflow |
| 8 | [docs.n8n.io/.../webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/) | Официальная дока n8n | Test vs Production URL, auth, 16MB payload | Нет amoCRM | — |

**Паттерн SERP:** смесь обзоров «n8n + amoCRM», один сильный кейс «статус → Telegram», мало единого гайда «OAuth + inbound webhook/Telegram + outbound webhook + антидубли + prod-чеклист» на одной странице. Конкуренты часто уводят в ApiMonster/Make или продают интеграцию.

**Intent:** `how_to` — настроить связку самому: credentials, заявка в воронку, уведомление менеджеру, без дублей и петель webhook.

**Пробел для блога:** один сквозной workflow (вход + выход), официальные лимиты amoCRM, честно про community node vs HTTP Request, чеклист Activate/HTTPS; internal links: Docker n8n, AI agents, Make vs n8n.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` не подключён в среде Cloud Agent (12.10.2026). Вызов `wordstat_get_top_requests` для `интеграция amoCRM n8n` и secondary queries **не выполнен**. Точные показы/мес **не использовать** в тексте статьи до повторного прогона с MCP.

**Семантика без цифр (экспертная оценка для LSI writer):**

- Primary: интеграция amoCRM n8n, n8n amocrm, подключить amocrm к n8n  
- Inbound: webhook n8n заявка с сайта, telegram trigger n8n, создать лид amocrm  
- Outbound: webhook amocrm смена статуса, уведомления amocrm telegram  
- Troubleshooting: oauth amocrm 401, redirect url, n8n не создаёт лид, 429 amocrm  

---

## 3. Таблица фактов (цифры и утверждения только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Встроенного официального узла amoCRM в n8n нет; типичный community-пакет — `n8n-nodes-amocrm` | [npmjs.com/package/n8n-nodes-amocrm](https://www.npmjs.com/package/n8n-nodes-amocrm) | 12.10.2026 | да |
| Версия `n8n-nodes-amocrm` на npm: 0.0.17, последнее обновление пакета 24.05.2025 | [npm view n8n-nodes-amocrm](https://www.npmjs.com/package/n8n-nodes-amocrm) | 12.10.2026 | да |
| Community node: OAuth — скопировать Redirect URL из credential n8n → «Redirect Link» внешней интеграции amoМаркет; Integration ID + Secret → n8n → Connect my account | [github.com/yatolstoy/n8n-node-amocrm](https://github.com/yatolstoy/n8n-node-amocrm) | 12.10.2026 | да |
| Установка community node (self-hosted): Settings → Community Nodes → Install → имя npm-пакета; только Owner/Admin | [docs.n8n.io/.../gui-installation](https://docs.n8n.io/integrations/community-nodes/installation-and-management/gui-installation) | 12.10.2026 | да |
| n8n Cloud: установка **только verified** community nodes; произвольный npm — self-host или HTTP Request | [community.n8n.io/t/n8n-community-node-installation-issue-n8n-cloud/276359](https://community.n8n.io/t/n8n-community-node-installation-issue-n8n-cloud/276359) | 12.10.2026 | да |
| Webhook node: Test URL при Listen/Execute; Production URL регистрируется при **активном** workflow | [docs.n8n.io/.../webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/) | 12.10.2026 | да |
| Максимальный payload входящего webhook n8n: 16MB (на self-host настраивается `N8N_PAYLOAD_SIZE_MAX`) | [docs.n8n.io/.../webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/) | 12.10.2026 | да |
| amoCRM API: не более **7** запросов/с на интеграцию, до **50** запросов/с на аккаунт | [amocrm.ru/developers/content/api/recommendations](https://www.amocrm.ru/developers/content/api/recommendations) | 12.10.2026 | да |
| Превышение лимита → HTTP **429**; при многократном нарушении блокировка → **403** на все запросы API | [amocrm.ru/developers/content/api/recommendations](https://www.amocrm.ru/developers/content/api/recommendations) | 12.10.2026 | да |
| Пакетное создание/изменение: максимум **250** сущностей в запросе; рекомендация amoCRM — **≤50** | [amocrm.ru/developers/content/api/recommendations](https://www.amocrm.ru/developers/content/api/recommendations) | 12.10.2026 | да |
| Код ошибки 429 в справочнике amoCRM: «превышено допустимое количество запросов в секунду» | [amocrm.ru/developers/content/crm_platform/error-codes](https://www.amocrm.ru/developers/content/crm_platform/error-codes) | 12.10.2026 | да |
| Код 403: аккаунт заблокирован за неоднократное превышение RPS | [amocrm.ru/developers/content/crm_platform/error-codes](https://www.amocrm.ru/developers/content/crm_platform/error-codes) | 12.10.2026 | да |
| `POST /api/v4/leads/complex` — сделка + контакт (+ компания) в одном запросе; до **50** сделок за запрос | [amocrm.ru/developers/content/crm_platform/leads-api](https://www.amocrm.ru/developers/content/crm_platform/leads-api) | 12.10.2026 | да |
| На одну сделку в complex — не более **1** контакта и **1** компании; до **40** custom fields на сущность | [amocrm.ru/developers/content/crm_platform/leads-api](https://www.amocrm.ru/developers/content/crm_platform/leads-api) | 12.10.2026 | да |
| Исходящие webhook amoCRM из amoМаркет: POST **x-www-form-urlencoded**, структура `{entity:{action:{...}}}}` | [amocrm.ru/developers/content/crm_platform/webhooks-format](https://www.amocrm.ru/developers/content/crm_platform/webhooks-format) | 12.10.2026 | да |
| Подписка на webhook через API: `POST /api/v4/webhooks` с `destination` + `settings` (напр. `add_lead`) | [new.amocrm.ru/developers/content/crm_platform/webhooks-api](https://new.amocrm.ru/developers/content/crm_platform/webhooks-api) | 12.10.2026 | да |
| Webhooks через API доступны с расширенного/профессионального тарифа amoCRM | [amocrm.ru/developers/content/crm_platform/webhooks-format](https://www.amocrm.ru/developers/content/crm_platform/webhooks-format) | 12.10.2026 | да |
| В аккаунте amoCRM — не более **100** webhook-подписок (API) | [github.com/MissiaL/amo-crm-api/.../webhooks.md](https://raw.githubusercontent.com/MissiaL/amo-crm-api/refs/heads/main/references/webhooks.md) | 12.10.2026 | да (вторичный, сверить с primary API doc) |
| Self-hosted n8n + Telegram: webhook Telegram требует **HTTPS**; задаётся `WEBHOOK_URL` при старте | [pinggy.io/blog/n8n_telegram_integration_with_pinggy](https://pinggy.io/blog/n8n_telegram_integration_with_pinggy/) | 12.10.2026 | да |
| Альтернатива OAuth: private integration + long-lived access token (subdomain + domain amocrm.ru/kommo.com) | [libraries.io/npm/@zenland-dev/n8n-nodes-amocrm](https://libraries.io/npm/@zenland-dev%2Fn8n-nodes-amocrm) | 12.10.2026 | да |
| Базовая автоматизация на no-code (Make, n8n) ~$150/мес API+платформы (контекст TCO, не amo-специфика) | [fact-bank / mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 2026-06-11 | да |
| Self-hosted n8n vs облачные SaaS: снижение накладных на медиа/объём до ~35% маржи (контекст выбора self-host) | [fact-bank / mayai.ru](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 2026-06-11 | да |

**Не использовать без MCP Wordstat:** любые «N показов/мес» по запросам amoCRM/n8n из сторонних статей (в т.ч. Дзен).

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** собрать **два рабочих контура** в n8n без кода: (A) заявка с сайта или Telegram → нормализация → contact+lead в amoCRM; (B) смена статуса сделки в amoCRM → фильтр → Telegram менеджеру; закрыть OAuth, prod webhook URL, антидубли и защиту от петли.

**Отличие от SERP:** один материал закрывает inbound+outbound + prod-чеклист; опирается на доку amoCRM/n8n, не на посредников.

**H2-каркас (из карточки B06):**

1. Когда amoCRM + n8n выгоднее Make/Zapier для РФ-бизнеса в 2026  
2. OAuth / credentials: subdomain, Redirect URL, 401/403  
3. Inbound: Webhook или Telegram → телефон/UTM → contact + lead (`/leads/complex` или node)  
4. Outbound: amoМаркет WEBHOOKS → фильтр статуса → Telegram  
5. Антидубли и webhook guard (idempotency, loop)  
6. Чеклист prod: Activate, HTTPS, тестовая воронка, мониторинг  

**Internal links (карточка):** `/ustanovka-n8n-docker-vps-2026/`, `/avtomatizaciya-n8n-ai-agents/`, `/sravnenie-make-zapier-n8n-2026/`

---

## 5. Workflow-схемы (для writer)

**Inbound:**

`Источник (Webhook POST / Telegram Trigger)` → `Set/Code: имя, phone E.164, UTM, source` → `HTTP: GET /api/v4/contacts?query=phone` (опц.) → `If дубль` → `amoCRM Create Complex / HTTP POST /leads/complex` → `Respond 200`

**Outbound:**

`amoCRM amoМаркет Webhook (status_lead / update_lead)` → `n8n Webhook (Production URL, workflow Active)` → `IF pipeline_id + status_id` → `Telegram Send Message` → `Stop` (не менять сделку обратно без guard)

---

## 6. FAQ-кандидаты (ответы-действия)

1. **Как подключить amoCRM к n8n?** — внешняя интеграция в amoМаркет + credential в n8n (OAuth или long-lived token); community node `n8n-nodes-amocrm` на self-host.  
2. **Нужен ли программист?** — нет для типового webhook/Telegram сценария; нужен админ amoCRM и HTTPS для self-hosted n8n.  
3. **Почему n8n не создаёт лид?** — проверить OAuth, `pipeline_id`/`status_id`, тело `/leads/complex`, Executions и код 401/422.  
4. **Test или Production URL?** — amoCRM шлёт только на Production при **Active** workflow.  
5. **Что при 429?** — Wait + Retry, снизить RPS (<7/с на интеграцию), batch ≤50.  
6. **Как не плодить дубли?** — search contact + complex с включённым контролем дублей для интеграции.  
7. **n8n Cloud и amo node?** — если пакет не verified — HTTP Request + OAuth2 credential.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «интеграция amoCRM и n8n» 40–60 слов | Lead | no-code мост CRM ↔ мессенджеры/сайт |
| Таблица inbound vs outbound блоков | H2-3/4 | Блок \| Задача \| Проверка |
| Чеклист 10+ пунктов prod | H2-6 | Маркированный список |
| FAQ 5–7 | Конец | Короткие шаги |
| Workflow `→` | H2-3 | ASCII или список |

---

## 8. Риски для writer

- Не выдумывать Wordstat-цифры (MCP недоступен).  
- Community nodes — предупредить о unverified code (docs n8n).  
- Не обещать официальный amoCRM node.  
- Redirect URL — посимвольное совпадение https/слэш.  
- Объём и slop: `shared/quality-blog.md`, min 5 шагов + чеклист 10+.  
- CTA ≤ 3, не подменять инструкцию.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель подключит amoCRM к n8n (OAuth или token), настроит приём заявок с webhook/Telegram в воронку amoCRM, отправку уведомлений о смене статуса в Telegram и пройдёт чеклист вывода workflow в production без дублей и webhook-петель.

**action_outline (для writer):**

1. **Выбрать хостинг n8n:** Cloud (только verified nodes / HTTP) или self-host с HTTPS и `WEBHOOK_URL` для Telegram.  
2. **Создать внешнюю интеграцию** в amoМаркет: scopes на leads/contacts; скопировать Integration ID, Secret, subdomain.  
3. **Credential в n8n:** вставить ключи, Redirect URL 1:1 в amoCRM, Connect my account до зелёного статуса (или long-lived token).  
4. **Установить `n8n-nodes-amocrm`** (self-host) или собрать **HTTP Request + OAuth2** (Cloud).  
5. **Inbound workflow:** Webhook/Telegram Trigger → нормализация phone/email/UTM → `POST /api/v4/leads/complex` с `pipeline_id`/`status_id` тестовой воронки.  
6. **Проверить Executions:** id сделки, merged-флаг, отсутствие 401/422/429.  
7. **Outbound workflow:** amoМаркет +WEBHOOKS → Production URL n8n → IF по статусу → Telegram (BotFather token + chat_id).  
8. **Webhook guard:** не обновлять ту же сделку из того же workflow; idempotency по entity id + timestamp.  
9. **Prod-чеклист:** Activate workflow, HTTPS, Header auth на публичном webhook, Error Workflow / алерт в Telegram, нагрузочный тест ≤7 rps.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.
