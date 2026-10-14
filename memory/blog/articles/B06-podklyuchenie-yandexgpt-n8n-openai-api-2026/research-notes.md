# Research notes — B06 «Как подключить YandexGPT к n8n через OpenAI-совместимый API: пошаговая инструкция для РФ»

**topic_id:** B06  
**slug:** podklyuchenie-yandexgpt-n8n-openai-api-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-10-14  
**disclaimer:** Все даты, версии и статистика проверены на 14.10.2026.

---

## 1. SERP-обзор (WebSearch Cursor, 14.10.2026 + research-serp.json)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [nikolaymatrosov.ru/2025-09-13-Use-Yandex-GPT-in-n8n](https://nikolaymatrosov.ru/2025-09-13-Use-Yandex-GPT-in-n8n/) | RU text how-to (сент. 2025) | Короткий канон: SA → API-ключ → OpenAI credential → AI Agent + `yandexgpt/latest` | Нет troubleshooting 401/404; scope `foundationModels` vs `languageModels` без пояснения | Копировать 1:1 без блока «если не работает» |
| 2 | [exlnt.team/.../yandex_gpt_n8n...](https://exlnt.team/ru/blog/posts/2025/06/yandex_gpt_n8n_kak_podklyuchit_rossijskuyu_llm_k_populyarnomu_instrumentu_sozdaniya_ai_agentov) | RU longread (июнь 2025) | Tools AI Agent, роль `ai.models.user`, scope `yc.ai.languageModels.execute`, мотивация vs HTTP | Устаревший акцент на прокси; нет 152-ФЗ / B2B approve | Длинную «историю поиска решения» |
| 3 | [agentpoint.ru/guides/n8n-ai-automation](https://agentpoint.ru/guides/n8n-ai-automation) | RU business guide (окт. 2026) | OpenAI-совместимость с мая 2025, кейсы approve, self-host + ПДн | FAQ противоречит body («только HTTP» vs OpenAI-нода); мало IAM | Продажу Bundle AgentPoint как главный CTA |
| 4 | [noltis.ru/blog/n8n-ai-gigachat-yandexgpt-2026](https://noltis.ru/blog/n8n-ai-gigachat-yandexgpt-2026/) | RU обзор 2026 | Контекст GigaChat + YandexGPT в одном workflow | Не узкий how-to по credential | Обзорный формат без чеклиста |
| 5 | [gist.github.com/lukinvit/e3c885ab...](https://gist.github.com/lukinvit/e3c885ab15816ca279cc153813e946ed) | Шпаргалка dev | Сводка нескольких LLM в n8n | Без пошаговых скринов для no-code | Сырой gist как единственная структура |
| 6 | [github.com/RomanAverin/n8n-nodes-yandexgpt](https://github.com/RomanAverin/n8n-nodes-yandexgpt) | Community node | SA JSON, folder ID, модели lite/rc | Не официальный путь; установка community nodes | Выдавать community за «единственный» способ |
| 7 | YouTube / Rutube / VK (MKZYZ4IXChk, c674b5de..., и др.) | Видео 2025–2026 | Визуальный walkthrough, Telegram-каналы | Нет текста для SEO; дубли в SERP | Пересказ видео без таблицы ошибок |
| 8 | [yandex.cloud/en/docs/tutorials/serverless/create-ai-agent-function](https://yandex.cloud/en/docs/tutorials/serverless/create-ai-agent-function) | Официальный tutorial YC | Канон IAM: `ai.languageModels.user`, scope `yc.ai.languageModels.execute`, `BASE_URL=https://ai.api.cloud.yandex.net/v1`, model URI `gpt://<folder>/yandexgpt/latest` | Не про n8n | Сухой перенос Cloud Functions без n8n UI |

**Паттерн SERP (октябрь 2026):** выдача **перегружена видео** (Rutube/YouTube/VK) и 2–3 текстовыми гайдами. Текстовый how-to с **чеклистом IAM + troubleshooting OpenAI credential** в топе почти не закрыт. Запрос узкий (long-tail), но intent сильный у интеграторов и no-code в РФ.

**Intent:** how_to — получить API-ключ Yandex Cloud, завести **OpenAI API credential** в n8n с правильным Base URL, подключить **OpenAI Chat Model** к **AI Agent**, прогнать тестовый prompt. Вторичный: выбор lite vs full, community node vs OpenAI-нода, ПДн/152-ФЗ, связка с CRM/Telegram (approve).

**Пробел для блога:** B2B-язык «на пальцах», **чеклист до старта**, таблица **двух Base URL** (`llm.api` vs `ai.api`), блок **типичных ошибок** (401, 404, красный тест credentials при рабочем chat), сравнение трёх путей из карточки B06, internal link на B02 (AI Agent) и B03 (MCP).

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

**⚠️ WORDSTAT MCP UNAVAILABLE:** в текущем Cloud Agent run namespace `user-mcp-kv` / инструмент `wordstat_get_top_requests` **не подключён** (MCP catalog empty). Точные показы в месяц **не получены** — в тексте статьи **не выдумывать** цифры спроса.

**Экспертная семантика (без объёмов, для LSI writer):**

| Кластер | Фразы для H2/H3/FAQ |
|---------|---------------------|
| Core | подключить yandexgpt к n8n, yandex gpt n8n, yandexgpt openai api n8n |
| Cloud / IAM | сервисный аккаунт yandex cloud, api-ключ yandex cloud, ai.languageModels.user |
| n8n | openai credential n8n base url, ai agent n8n yandexgpt, openai chat model |
| Модели | yandexgpt/latest, yandexgpt-lite/latest, gpt://folder_id/yandexgpt |
| Troubleshooting | n8n openai 401 yandex, connection tested successfully, base url /v1 |

**SEO-стратегия:** primary «подключить yandexgpt к n8n» в H1/lead; secondary из карточки — в подзаголовках; head «n8n» / «yandexgpt» — через контекст и internal links, не размывать H1.

---

## 3. Таблица фактов (цифры и утверждения только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Yandex Cloud Foundation Models можно вызывать через интерфейс, совместимый с OpenAI API; в n8n используют credential типа **OpenAI API** | [nikolaymatrosov.ru](https://nikolaymatrosov.ru/2025-09-13-Use-Yandex-GPT-in-n8n/) | 13.09.2025 | да |
| Роли SA для доступа к LLM: минимум **`ai.languageModels.user`**; для списка моделей часто добавляют **`ai.models.viewer`** | [nikolaymatrosov.ru](https://nikolaymatrosov.ru/2025-09-13-Use-Yandex-GPT-in-n8n/) | 13.09.2025 | да |
| Scope API-ключа в гайде Matrosov: **`yc.ai.foundationModels.execute`** | [nikolaymatrosov.ru](https://nikolaymatrosov.ru/2025-09-13-Use-Yandex-GPT-in-n8n/) | 13.09.2025 | да (с оговоркой про альтернативный scope ниже) |
| Base URL в популярных n8n-гайдах: **`https://llm.api.cloud.yandex.net/v1`** | [nikolaymatrosov.ru](https://nikolaymatrosov.ru/2025-09-13-Use-Yandex-GPT-in-n8n/), [exlnt.team](https://exlnt.team/ru/blog/posts/2025/06/yandex_gpt_n8n_kak_podklyuchit_rossijskuyu_llm_k_populyarnomu_instrumentu_sozdaniya_ai_agentov) | 2025 | да |
| Официальный tutorial AI Studio для OpenAI SDK: **`BASE_URL=https://ai.api.cloud.yandex.net/v1`**, model **`gpt://<folder_ID>/yandexgpt/latest`** | [yandex.cloud create-ai-agent-function](https://yandex.cloud/en/docs/tutorials/serverless/create-ai-agent-function) | 2026 | да |
| Scope API-ключа в официальном tutorial: **`yc.ai.languageModels.execute`** | [yandex.cloud create-ai-agent-function](https://yandex.cloud/en/docs/tutorials/serverless/create-ai-agent-function) | 2026 | да |
| Роль SA в официальном tutorial: **`ai.languageModels.user`** | [yandex.cloud create-ai-agent-function](https://yandex.cloud/en/docs/tutorials/serverless/create-ai-agent-function) | 2026 | да |
| Доступные scopes API-ключа включают **`yc.ai.languageModels.execute`** (Text Generation) и **`yc.ai.foundationModels.execute`** (широкий AI Studio) | [yandex.cloud API key docs](https://yandex.cloud/en/docs/iam/concepts/authorization/api-key) | 2026 | да |
| Endpoint сервиса **`ai-foundation-models`** в каталоге YC: **`ai.api.cloud.yandex.net:443`** | [yandex.cloud endpoints](https://yandex.cloud/ru/docs/api-design-guide/concepts/endpoints) | 2026 | да |
| Классический REST completion (не OpenAI-path): **`POST https://llm.api.cloud.yandex.net/foundationModels/v1/completion`** | [langchain-yandex chat_models.ts](https://github.com/langchain-ai/langchainjs-community/blob/main/libs/langchain-yandex/src/chat_models.ts) | 2026 | да (для блока HTTP Request / legacy) |
| С **мая 2025** Yandex Foundation Models заявлены как поддерживающие **OpenAI-совместимый API** для n8n (смена base URL) | [agentpoint.ru](https://agentpoint.ru/guides/n8n-ai-automation) | 12.10.2026 | да |
| В n8n **Base URL** в OpenAI credential — только **корень API** (обычно до **`/v1`**), не полный путь `/chat/completions` | [community.n8n.io OpenAI authorization](https://community.n8n.io/t/openai-node-authorization-is-not-working/300779) | 2026 | да |
| Тест credential OpenAI в n8n часто бьёт в **`/models`**; у части провайдеров тест красный, а **chat/completions** работает | [community.n8n.io](https://community.n8n.io/t/openai-node-authorization-is-not-working/300779), [ofox.ai n8n base url](https://ofox.ai/blog/n8n-custom-api-base-url-2026/) | 2026 | да |
| Поле **Base URL** для OpenAI-нод вынесено в credentials (fix в релизах **n8n 1.74.x**) | [n8n issue ADO-2887 / 1.74.1](https://github.com/n8n-io/n8n/issues/12356) | 2025 | да |
| Community-пакет **`n8n-nodes-yandexgpt`**: SA JSON, **Folder ID**, endpoint по умолчанию **`https://llm.api.cloud.yandex.net`** | [github.com/RomanAverin/n8n-nodes-yandexgpt](https://github.com/RomanAverin/n8n-nodes-yandexgpt) | 2026 | да |
| Модели в OpenAI-режиме: **`yandexgpt/latest`**, **`yandexgpt-lite/latest`** (и варианты без `/latest` в community node) | [nikolaymatrosov.ru](https://nikolaymatrosov.ru/2025-09-13-Use-Yandex-GPT-in-n8n/), [RomanAverin/n8n-nodes-yandexgpt](https://github.com/RomanAverin/n8n-nodes-yandexgpt) | 2025–2026 | да |
| exlnt.team рекомендует доп. роль **`ai.models.user`** для корректного списка моделей в n8n (не всегда в оф. доке) | [exlnt.team](https://exlnt.team/ru/blog/posts/2025/06/yandex_gpt_n8n_kak_podklyuchit_rossijskuyu_llm_k_populyarnomu_instrumentu_sozdaniya_ai_agentov) | 06.2025 | да (как community-практика) |
| Переход на self-hosted n8n может снизить накладные расходы и поднять маржинальность контент-производства до **35%** (контекст cost stack) | [fact-bank / mayai.ru n8n vs make](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 11.06.2026 | да (осторожно, не как цена YandexGPT) |
| Базовый стек API LLM + no-code (Make/n8n) — порядка **$150/мес** (контекст бюджета автоматизации) | [fact-bank / mayai.ru](https://mayai.ru/kontent-zavod-avtomatizacziya-cherez-ii-razbiraem-otzyvy/) | 11.06.2026 | да (не путать с тарифом Yandex Cloud) |

**Не использовать без первичника Yandex Billing:** «5 минут на всё», «бесплатно навсегда», конкретные ₽/1K tokens YandexGPT в 2026 — в research нет актуального прайса; writer даёт ссылку на биллинг YC без цифр.

**Writer: согласовать два Base URL в статье**

| Вариант | Base URL | Когда пробовать |
|---------|----------|-----------------|
| A (большинство n8n-гайдов) | `https://llm.api.cloud.yandex.net/v1` | Первый выбор по карточке B06 |
| B (официальный AI Studio / VS Code tutorial) | `https://ai.api.cloud.yandex.net/v1` | Если A даёт 404 или пустой список моделей; model ID `gpt://<folder>/yandexgpt/latest` |

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за один проход настроить **YandexGPT как Chat Model** для **AI Agent** в n8n через **OpenAI credential** (без кастомного HTTP на MVP), проверить ответ модели и собрать **минимальный business-workflow** с **human approve** перед записью в CRM/Telegram.

**Отличие от SERP:**

- Видео не дают чеклист IAM и матрицу ошибок.
- exlnt/nikolay — для разработчиков; нет связки с **152-ФЗ / ПДн** и approve-step.
- agentpoint — широкий обзор; FAQ устарел про «только HTTP».

**Tone:** B2B no-code; SA, scope, Base URL — с расшифровкой; без «импортозамещение ради лозунга».

**H2-каркас (из карточки + research):**

1. Чеклист перед стартом (каталог, SA, роли, scope, где хранить ключ)
2. Credential OpenAI в n8n: Base URL, тест, 401/403/404
3. AI Agent + Chat Model: модели lite vs latest, folder/project при необходимости
4. Первый workflow: заявка → классификация → черновик → approve → Telegram/CRM
5. Сравнение: OpenAI credential vs community node vs HTTP Request

**Internal links (карточка):** `/avtomatizaciya-n8n-ai-agents/` (B02), `/podklyuchenie-mcp-cursor/` (B03)

---

## 5. Сравнение путей подключения (черновик для writer)

| Критерий | OpenAI credential + Base URL | Community `n8n-nodes-yandexgpt` | HTTP Request (native FM API) |
|----------|-------------------------------|---------------------------------|------------------------------|
| Сложность | Низкая | Средняя (install community) | Высокая |
| AI Agent + Tools + Memory | Да (рекомендуемый путь) | Да (нативная нода) | Частично / вручную |
| Function calling | Через OpenAI-compatible stack | Заявлено в node | Ручная сборка |
| Обновления API | Зависит от совместимости YC | Зависит от maintainer | Полный контроль |
| Когда выбирать | **Default для статьи** | Нужны SA JSON / folder в UI node | Legacy, кастомные заголовки, нестандартный auth |

---

## 6. FAQ-кандидаты (5–7)

1. **Нужен ли отдельный community node для YandexGPT?** — Нет для MVP: достаточно OpenAI credential + правильный Base URL; node — опция при желании нативной ноды.
2. **Какой scope у API-ключа?** — Минимум `yc.ai.languageModels.execute`; в части гайдов встречается `yc.ai.foundationModels.execute` — указать оба и проверить в консоли при 403.
3. **Какую модель выбрать: lite или latest?** — lite для классификации/черновиков; latest/rc для сложных ответов; проверить latency и billing в YC.
4. **Почему credential «красный», а workflow отвечает?** — Тест `/models` не поддержан; проверять реальным Chat/AI Agent run.
5. **Можно ли гнать ПДн клиентов в YandexGPT?** — Юридическая оценка + договор/DPA YC; для чувствительных данных — self-host n8n в РФ, минимизация полей в prompt, approve перед отправкой.
6. **Чем отличается `llm.api` от `ai.api`?** — Разные поколения/маршруты AI Studio; таблица из раздела 3, порядок A → B при ошибках.
7. **Как связать с CRM?** — После approve — нода Bitrix24/amoCRM; ключи только в credentials (см. agentpoint security block).

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение «OpenAI-совместимый YandexGPT в n8n» 40–60 слов | Lead | «Это значит, что…» |
| Чеклист 10+ пунктов | H2-1 | Перед стартом |
| Таблица путей подключения | H2-5 | Comparison |
| Workflow ASCII | H2-4 | Webhook → AI Agent → Approve → CRM |
| FAQ 5–7 | Конец | Ответы-действия |
| Troubleshooting table | H2-2 | Симптом → причина → fix |

**Целевые формулировки:** «подключить yandexgpt к n8n», «yandexgpt openai api n8n», «сервисный аккаунт yandex cloud n8n», «yandex gpt ai agent».

---

## 8. Риски для writer

- Не выдумывать Wordstat-показы и тарифы YandexGPT за 1K tokens.
- Явно описать **два Base URL** и **два scope**, не оставлять reader в тупике при 403.
- Base URL **без** хвоста `/chat/completions`.
- Без эмодзи; дефис вместо длинного тире; прямые кавычки (site-brief).
- Min **5** нумерованных шагов + чеклист 10+ + comparison (utility gate статьи).
- Объём ориентир: 8 500–9 500 знаков (`quality-blog`).
- CTA ≤ 3; не подменять пошаговку продажами.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст сервисный аккаунт и API-ключ в Yandex Cloud, настроит в n8n credential **OpenAI API** с корректным Base URL, подключит **YandexGPT** к **AI Agent**, получит первый ответ модели и соберёт простой сценарий с **approve** перед отправкой черновика в Telegram или CRM.

**action_outline (для writer):**

1. **Чеклист:** аккаунт Yandex Cloud, каталог (folder ID), billing активен, n8n Cloud или self-host готов.
2. **IAM:** создать SA с ролями `ai.languageModels.user` (+ `ai.models.viewer` / при необходимости `ai.models.user` по exlnt).
3. **API-ключ:** scope `yc.ai.languageModels.execute` (fallback `yc.ai.foundationModels.execute`); сохранить secret один раз; только n8n Credentials.
4. **n8n Credentials → OpenAI API:** имя «Yandex GPT», API Key, Base URL **`https://llm.api.cloud.yandex.net/v1`**; Save; если тест красный — перейти к шагу 8.
5. **Workflow:** Chat Trigger (или Webhook тестовой «заявки») → **AI Agent** → sub-node **OpenAI Chat Model** с credential из шага 4.
6. **Model:** `yandexgpt-lite/latest` для MVP-классификации или `yandexgpt/latest` для качества; System Message: роль, формат JSON/текста, запрет выдумывать факты.
7. **Execute:** отправить тестовый prompt; в Logs проверить request/response; при 401/403 — роли/scope; при 404 — сменить Base URL на **`https://ai.api.cloud.yandex.net/v1`** и model URI `gpt://<folder>/yandexgpt/latest`.
8. **Troubleshooting:** таблица симптомов (401, 403, 404, пустой model list, красный credential test); HTTP Request sanity-check `POST .../v1/chat/completions` по community-рекомендациям.
9. **Business-chain:** добавить ветку **approve** (Telegram/Email) перед write-нодой CRM; упомянуть 152-ФЗ при ПДн; internal link B02 для углубления AI Agent.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS (research-context) |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ unavailable (без выдуманных цифр) |
| Таблица фактов с URL | ✅ (18 фактов) |
| utility_verdict + action_outline | ✅ |
| Comparison 3 путей | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 в `memory/topics/blog-topics.md` + `site-brief.md`.
