# Research notes — B06 «Как настроить Claude Code Routines: пошаговое руководство по расписанию, API и GitHub-триггерам»

**topic_id:** B06  
**slug:** claude-code-routines-nastrojka-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-08-16  
**disclaimer:** Все даты, версии и статистика проверены на 16.08.2026.

---

## 1. SERP-обзор (WebSearch, 16.08.2026)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | Официальная docs (EN) | Канон: триггеры, лимиты, troubleshooting `/schedule`, cloud environments | Английский; мало русских примеров для B2B без dev-бэкграунда | Сухой перевод без «на пальцах» |
| 2 | [code.claude.com/docs/ru/routines](https://code.claude.com/docs/ru/routines) | Официальная docs (RU) | Полный how-to на русском: триггеры, фильтры PR, API curl | Нет готовых «5 рутин для бизнеса» | Копировать структуру 1:1 |
| 3 | [claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code) | Официальный анонс | Дата запуска, лимиты Pro/Max/Team, use cases | News-формат, без пошаговой настройки всех триггеров | Новостной lead «вышло обновление» |
| 4 | [platform.claude.com/docs/en/api/claude-code/routines-fire](https://platform.claude.com/docs/en/api/claude-code/routines-fire) | API reference | Заголовки, ошибки 400/401/429, лимит `text` 65536 | Только API; без web UI и GitHub | Выдумывать поля ответа |
| 5 | [smyslokod.ru/guides/routines-v-claude-code](https://smyslokod.ru/guides/routines-v-claude-code) | RU longread | 5 готовых рутин, cloud environment, cron | Перегруз SEO-ключами; смешение с hooks | Структуру и промпты 1:1 |
| 6 | [www.builder.io/blog/claude-code-routines](https://www.builder.io/blog/claude-code-routines) | EN tutorial | Copy-paste промпты, gotchas `/web-setup` vs GitHub App | EN; dev-аудитория | Коммерческий bias Builder |
| 7 | [makerkit.dev/blog/tutorials/claude-code-routines-guide](https://makerkit.dev/blog/tutorials/claude-code-routines-guide) | EN guide 2026 | Decision framework: routine vs cron vs subagent | Нет русского; SaaS-уклон | Таблицу решений без адаптации под B2B RU |
| 8 | [nimbalyst.com/blog/claude-code-routines-practical-guide/](https://nimbalyst.com/blog/claude-code-routines-practical-guide/) | EN practical | Лимиты preview, когда routine не нужен | Продаёт Nimbalyst automations | Fear-mongering про лимиты |
| 9 | [qcode.cc/ru/claude-code-routines-guide](https://qcode.cc/ru/claude-code-routines-guide) | RU guide | Три триггера, лимиты тарифов | Мало troubleshooting API/GitHub | Дублировать без своего угла |
| 10 | [www.galson.pro/articles/claude-code-routines-avtomatizaciya-zadach](https://www.galson.pro/articles/claude-code-routines-avtomatizaciya-zadach) | RU обзор | «Без сервера», простой язык | Поверхностно про API headers | Новостной тон |

**Паттерн SERP:** топ — официальная docs Anthropic (EN/RU) + англоязычные гайды 2026 (Builder, Makerkit, Nimbalyst) + несколько русских longread'ов (smyslokod, qcode, galson). Запрос «claude code routines» почти полностью закрыт dev-контентом; русскоязычный **пошаговый** гайд с чек-листом production и отличиями от `/loop`, hooks и Desktop scheduled tasks — пробел для utility-only B2B-блога.

**Intent:** how_to — пользователь хочет **создать и запустить** первую облачную рутину: выбрать триггер (Schedule / API / GitHub), настроить промпт и репозиторий, проверить запуск и не упереться в лимиты.

**Пробел для статьи:** практик автоматизации на русском: от подготовки аккаунта до трёх типов триггеров с copy-paste curl, чек-лист production (сеть, cap, GitHub App), 5 готовых рутин под бизнес-рутину (review, triage, docs drift) — без news-формата «Anthropic выпустил…».

---

## 2. Яндекс Wordstat

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` не подключён в среде Cloud Agent (MCP catalog: только Cursor Automation Tools, cursor-cloud). Инструмент `wordstat_get_top_requests` недоступен.

**Fallback (семантика из SERP, без выдуманных цифр спроса):**

| Кластер запроса | Наблюдение по SERP | Роль в статье |
|-----------------|-------------------|---------------|
| `claude code routines` | Доминирует официальная docs + EN гайды | Primary в H1/lead |
| `настройка claude code routines` / `claude code рутины` | 2–3 русских longread в топ-10 | Secondary в H2 «создание первой рутины» |
| `/schedule claude code` | Смешение с `/loop` и Desktop scheduled tasks в SERP | Отдельный H2 «не путать с…» |
| `claude code github trigger` | Docs + GitHub Actions guides (другой продукт) | H2 GitHub + предупреждение про Claude GitHub App |
| `claude code api trigger` | Platform docs `/fire` + curl-примеры | H2 API с полным curl |

**LSI для writer (из SERP + docs, без Wordstat-цифр):**

- claude code routines настройка, research preview, claude.ai/code/routines  
- /schedule, /routines, cloud routine vs Desktop Local task  
- триггер schedule cron hourly nightly weekly, минимальный интервал 1 час  
- API trigger bearer token sk-ant-oat01, experimental-cc-routine-2026-04-01  
- GitHub trigger pull_request.opened, Claude GitHub App, /web-setup не ставит App  
- cloud environment network access Trusted Custom, setup script кеш  
- лимиты Pro 5 Max 15 Team 25 routines в день, one-off не в cap  
- connectors MCP Slack Linear, claude/ branch prefix  

**SEO-стратегия:** primary «claude code routines» + русские «рутины claude code», «настройка claude code routines» в подзаголовках; long-tail «github trigger», «api trigger», «/schedule» — в соответствующих H2 и FAQ.

**Действие для пайплайна:** обновить OAuth-токен Wordstat через [Yandex OAuth](https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40) и перепроверить спрос перед следующим прогоном.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Routines анонсированы 14 апреля 2026 в research preview | [claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code) | 14.04.2026 | да |
| Routine = сохранённая конфигурация: prompt + repo(s) + connectors, запуск в облаке Anthropic | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Три типа триггеров: Scheduled, API, GitHub; можно комбинировать на одной рутине | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Доступно на Pro, Max, Team, Enterprise с включённым Claude Code on the web | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Создание: [claude.ai/code/routines](https://claude.ai/code/routines), Desktop (New routine → Cloud), CLI `/schedule` | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Дневные лимиты запусков: Pro — 5, Max — 15, Team/Enterprise — 25 routines в день | [claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code) | 14.04.2026 | да |
| Routines расходуют subscription usage как интерактивные сессии | [claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code) | 14.04.2026 | да |
| One-off scheduled runs **не** считаются в дневной cap routines | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Минимальный интервал cron — **1 час**; более частые выражения отклоняются | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| `/schedule` в CLI создаёт **только** scheduled routines; API — только через web UI | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Алиас команды: `/routines` | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| GitHub trigger из CLI — с v2.1.225+; нужен предварительный install [Claude GitHub App](https://github.com/apps/claude) | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| `/web-setup` даёт clone access, но **не** ставит GitHub App и не включает webhooks | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| API POST: `https://api.anthropic.com/v1/claude_code/routines/{routine_id}/fire` | [platform.claude.com/docs/en/api/claude-code/routines-fire](https://platform.claude.com/docs/en/api/claude-code/routines-fire) | 16.08.2026 | да |
| Обязательный header: `anthropic-beta: experimental-cc-routine-2026-04-01`; без него — 400 | [platform.claude.com/docs/en/api/claude-code/routines-fire](https://platform.claude.com/docs/en/api/claude-code/routines-fire) | 16.08.2026 | да |
| Также обязательны: `Authorization: Bearer`, `anthropic-version: 2023-06-01`, `Content-Type: application/json` | [platform.claude.com/docs/en/api/claude-code/routines-fire](https://platform.claude.com/docs/en/api/claude-code/routines-fire) | 16.08.2026 | да |
| Bearer token prefix `sk-ant-oat01-`; показывается **один раз** при Generate token | [platform.claude.com/docs/en/api/claude-code/routines-fire](https://platform.claude.com/docs/en/api/claude-code/routines-fire) | 16.08.2026 | да |
| Path param `routine_id` в URL имеет prefix `trig_`, не `routine_` | [platform.claude.com/docs/en/api/claude-code/routines-fire](https://platform.claude.com/docs/en/api/claude-code/routines-fire) | 16.08.2026 | да |
| Поле `text` в body опционально, max **65536** символов | [platform.claude.com/docs/en/api/claude-code/routines-fire](https://platform.claude.com/docs/en/api/claude-code/routines-fire) | 16.08.2026 | да |
| Успешный ответ 200: `type: routine_fire`, `claude_code_session_id`, `claude_code_session_url` | [platform.claude.com/docs/en/api/claude-code/routines-fire](https://platform.claude.com/docs/en/api/claude-code/routines-fire) | 16.08.2026 | да |
| Каждый POST `/fire` создаёт **новую** сессию; idempotency key нет | [platform.claude.com/docs/en/api/claude-code/routines-fire](https://platform.claude.com/docs/en/api/claude-code/routines-fire) | 16.08.2026 | да |
| GitHub events: категории Pull request и Release; фильтры Author, Title, Base branch, Labels, Is draft и др. | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| События GitHub сверх hourly cap **отбрасываются**, не ставятся в очередь | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Routines принадлежат **личному** claude.ai аккаунту, не шарятся с командой | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Claude пушит в ветки с prefix `claude/` | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Зелёный статус run = нет infra-ошибки, **не** гарантия успеха задачи | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Team/Enterprise Owner может выключить Routines: [claude.ai/admin-settings/claude-code](https://claude.ai/admin-settings/claude-code) | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Локальные MCP из CLI `claude mcp add` **не** видны в routines; нужны connectors на claude.ai | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Default cloud environment: Trusted network + default allowlist доменов | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| `/schedule list`, `/schedule update`, `/schedule run` — управление из CLI | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | 16.08.2026 | да |
| Desktop **Local** scheduled task ≠ cloud Routine (Remote) | [code.claude.com/docs/ru/routines](https://code.claude.com/docs/ru/routines) | 16.08.2026 | да |

**fact-bank.md:** записей по Claude Code Routines нет — все цифры только из таблицы выше.

**Не путать в тексте:**
- **Routines** (облако, claude.ai) vs **`/loop` / scheduled-tasks** (локальная сессия CLI) vs **Desktop Local task** (машина пользователя) vs **GitHub Actions claude-code-action** (CI workflow, другой продуктовый слой).

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **30–45 минут** создать первую **облачную** рутину с одним триггером Schedule, затем добавить API или GitHub trigger, проверить run в claude.ai/code и пройти production-чек-лист (промпт, сеть, лимиты, GitHub App).

**Почему отличается от конкурентов:**
- Официальная docs — канон, но без B2B-сценариев «ночной triage / docs drift / deploy-check» на русском.
- EN-гайды не закрывают смешение `/schedule` с `/loop` и Desktop Local.
- RU-статьи часто начинаются с news «Anthropic выпустил» — utility-only lead = боль + результат.

**Tone:** Routine = «облачный сотрудник с будильником»; триггер = «когда его будить»; bearer token = «ключ от одной двери». Без снобизма Senior-dev; термины cron, webhook, bearer — сразу «на пальцах».

**H2-каркас (из карточки B06 + research):**
1. Routines vs hooks vs skills vs `/loop` vs Desktop Local — таблица «когда что»  
2. Подготовка: план Pro+, GitHub, CLAUDE.md, лимиты 5/15/25  
3. Первая рутина: web UI + альтернатива `/schedule`  
4. Schedule: presets, cron ≥1h, one-off  
5. API: Generate token, curl, headers, хранение секрета  
6. GitHub: install App, фильтры PR, типовая ошибка `/web-setup`  
7. Production-чек-лист: connectors, network Custom, cap, green status ≠ success  
8. 5 готовых рутин для копирования (review, dependency audit, changelog, triage, deploy-check)  
9. FAQ + чек-лист 10+ пунктов  

**Internal links (из карточки):** `/ustanovka-claude-code/`, `/claude-code-hooks-nastrojka-2026/`

---

## 5. Черновик 5 готовых рутин (для writer)

| # | Название | Триггер | Суть промпта (1 строка) |
|---|----------|---------|-------------------------|
| 1 | Nightly PR digest | Schedule weekdays 9:00 | Суммировать PR за сутки, пост в Slack connector |
| 2 | Weekly dependency audit | Schedule weekly | `npm audit` / lockfile diff, draft PR с фиксами |
| 3 | Docs drift | Schedule weekly | Скан merged PR vs docs repo, PR на обновление |
| 4 | Alert triage | API + `text` из мониторинга | Разбор stack trace, draft fix PR |
| 5 | PR opened review | GitHub `pull_request.opened` + filter base=main, draft=false | Чек-лист security/style, inline comments |

Промпты брать из [docs Example use cases](https://code.claude.com/docs/en/routines#example-use-cases) и адаптировать; не копировать smyslokod 1:1.

---

## 6. FAQ-кандидаты (из faq_hints + research)

1. **Как настроить Claude Code Routines?** — claude.ai/code/routines → New routine → prompt, repo, environment, trigger → Create; или `/schedule` для schedule-only.  
2. **Чем routines отличаются от hooks?** — hooks = локальные события CLI; routines = облачные автономные сессии с расписанием/API/GitHub.  
3. **Сколько запусков routines в день на Pro?** — до 5 (Max 15, Team/Ent 25); one-off в cap не входят.  
4. **Минимальный интервал cron?** — 1 час.  
5. **Почему GitHub trigger не срабатывает?** — не установлен Claude GitHub App ( `/web-setup` недостаточно).  
6. **Где взять API token повторно?** — нельзя; только Regenerate в UI.  
7. **Можно ли без ноутбука?** — да, routines в облаке Anthropic.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Routine 40–60 слов | Lead | «Claude Code Routine — …» |
| Таблица 3 триггеров | H2-4 | Schedule / API / GitHub + «когда выбирать» |
| Copy-paste curl `/fire` | H2-5 | Блок кода + пояснение headers |
| Workflow | H2-3–7 | Подготовка → create → trigger → Run now → проверка transcript |
| FAQ 5–7 | Конец | Ответы-действия |
| Чек-лист 10+ | H2-7 | Production перед «боем» |

**Целевые формулировки:** «claude code routines», «настройка claude code routines», «claude code github trigger», «claude code api trigger», «/schedule claude code».

---

## 8. Риски для writer

- Не выдумывать лимиты кроме 5/15/25 из официального блога; Nimbalyst пишет «может меняться» — дублировать оговорку research preview.  
- Не путать Routines API (`sk-ant-oat01-`) с Claude Platform API key (`x-api-key`).  
- Не обещать idempotency API — каждый POST = новая сессия.  
- Объём: 8 500–10 000 знаков; min **5** нумерованных шагов + чек-лист **10+**.  
- Без эмодзи; дефис вместо длинного тире; прямые кавычки.  
- Lead — не «Anthropic выпустил 14 апреля», а «настроите первую рутину за N шагов».

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель создаст облачную рутину в claude.ai/code/routines (или через `/schedule`), настроит минимум один триггер Schedule, при необходимости добавит API POST с bearer-токеном или GitHub trigger с установленным Claude GitHub App, проверит run в веб-UI и применит production-чек-лист по лимитам, сети и промпту.

**action_outline (для writer):**

1. **Проверить доступ:** план Pro/Max/Team/Ent, Claude Code on the web включён; Owner не отключил Routines в admin-settings.  
2. **Подключить GitHub** к claude.ai (`/web-setup` или OAuth в web) — для clone repos; для GitHub trigger позже — отдельно Claude GitHub App.  
3. **Создать первую рутину в web:** claude.ai/code/routines → New routine → имя, **self-contained prompt**, repo, Default/Custom environment, trigger Schedule (например nightly).  
4. **Или через CLI:** в сессии Claude Code выполнить `/schedule daily …`; убедиться, что routine появилась в web UI.  
5. **Настроить Schedule:** preset или cron ≥1h; для one-off — web UI (если CLI недоступен).  
6. **Добавить API trigger (web):** Edit → Add trigger → API → Generate token → сохранить URL + token → тест curl с beta-header.  
7. **Добавить GitHub trigger (web):** Install Claude GitHub App → event + filters → сохранить.  
8. **Run now** + открыть session transcript; не доверять только green status.  
9. **Production:** урезать connectors, Custom network если нужны свои домены, учесть daily cap 5/15/25, human review для PR/commits.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (10) |
| Wordstat MCP | ⚠️ unavailable (SERP fallback) |
| Таблица фактов с URL | ✅ (30 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.
