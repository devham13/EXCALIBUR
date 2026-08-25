# Research notes — B06 «Как настроить Cursor Subscriptions: мониторинг PR и Slack-тредов cloud-агентами»

**topic_id:** B06  
**slug:** cursor-subscriptions-nastrojka-2026  
**article_mode:** B (workflow / how-to)  
**research_date:** 2026-08-25  
**disclaimer:** Все даты, версии и статистика проверены на 25.08.2026.

---

## 1. SERP-обзор (WebSearch, 25.08.2026)

**Важно:** по запросу `cursor subscriptions` выдача на 90% — **тарифы Cursor Pro/Ultra** (vc.ru, pikabu, cursor.com/pricing), а не фича **Subscriptions** (event-driven мониторинг PR/Slack). Наш how-to закрывает **продуктовый пробел**: практический workflow по релизу **19.08.2026**.

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | Официальный changelog | Канон: Subscriptions, /goal, subagents, steering | Нет пошагового setup | Сухой пересказ без чек-листа |
| 2 | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | Официальная docs | Таблица интеграций, 180 дней, CI autofix, /subscribe | EN; нет связки GitHub+Slack в одном сценарии | Копировать таблицы 1:1 без русского workflow |
| 3 | [cursor.com/docs/integrations/slack](https://cursor.com/docs/integrations/slack) | Официальная docs Slack | Install flow, @cursor команды, routing rules | Не объясняет Subscriptions vs Automations | — |
| 4 | [learncursor.dev/.../cloud-agent-automations](https://www.learncursor.dev/learn/cursor-agents/cloud-agent-automations) | EN how-to (авг. 2026) | Чёткое **Automations vs Subscriptions** | Англ.; нет security checklist | Структуру 1:1 |
| 5 | [ai-tldr.dev/releases/cursor-agent-subscriptions](https://ai-tldr.dev/releases/cursor-agent-subscriptions/) | Release digest | Quick facts, FAQ по /goal и subagents | Короткий; без dashboard steps | — |
| 6 | [explainx.ai/.../cursor-event-driven-cloud-agents](https://www.explainx.ai/blog/cursor-event-driven-cloud-agents-isolated-vms-august-2026) | Аналитика | Контекст Automations (март 2026) + subscriptions | Много «новостного» тона | News-формат |
| 7 | [byteiota.com/cursor-automations-tutorial-2026-setup-guide](https://byteiota.com/cursor-automations-tutorial-2026-setup-guide/) | Setup Automations | Multi-repo, dashboard | Про Automations, не Subscriptions | Путать с нашей темой |
| 8 | [shtruzel.ru/.../cursor-agent-mode-kak-ispolzovat-2026](https://shtruzel.ru/articles/cursor-agent-mode-kak-ispolzovat-2026) | RU обзор Agent mode | Cloud Agents, субагенты | Subscriptions — одним абзацем | Уход в общий обзор Cursor |

**Паттерн SERP:** англоязычные release-notes + 1–2 аналитики; **русского пошагового гайда по Subscriptions нет**. Запрос `cursor subscriptions` в Яндексе перехватывают статьи про **оплату подписки** — в title/lead writer обязан дизамбiguировать: «Subscriptions = мониторинг событий cloud-агентами, не тариф Cursor Pro».

**Intent:** workflow — читатель хочет **настроить** cloud agent, который **сам просыпается** на PR/Slack/cron, чинит CI и не требует ручного re-prompt.

**Пробел для «Ковчег»:** единый русский workflow A→B→C: Dashboard (GitHub + Slack + spend limit) → первый cloud agent с subscription на PR → мониторинг Slack-треда → /goal + /autopilot (/babysit) + чек-лист безопасности. Internal link: [B03 MCP](/podklyuchenie-mcp-cursor/).

---

## 2. Яндекс Wordstat

⚠️ **WORDSTAT MCP UNAVAILABLE:** сервер `user-mcp-kv` / инструмент `wordstat_get_top_requests` **не подключён** в runtime Cloud Agent (namespace отсутствует в MCP catalog). Точные показы в месяц **не получены** — цифры ниже **не использовать в тексте статьи** как статистику.

### Экспертная оценка спроса (WebSearch + SERP, без API)

| Фраза | Оценка / комментарий |
|-------|----------------------|
| cursor subscriptions | **Высокий шум:** в выдаче доминирует intent «купить/оплатить Cursor» (vc.ru, pikabu, pricing). Продуктовый intent Subscriptions — низкая видимость в RU. |
| cursor cloud agents | Средний; растёт после релизов 2026 (vc.ru, Habr). Ближе к нашей теме. |
| cursor automations | Низкий–средний EN; русскоязычных how-to мало. |
| cursor subscriptions slack | Очень низкий; закрывается официальной docs + EN блогами. |
| cursor cloud agents pr | Низкий; смешан с GitHub Copilot cloud agent (Habr). |
| настройка cursor cloud agents | Потенциальный long-tail RU; прямых конкурентов по Subscriptions нет. |
| cursor /goal | Микро-intent; community + changelog. |
| cursor babysit pr / cursor autopilot | Микро-intent; forum.cursor.com про rename /babysit → /autopilot. |

### LSI для writer (SERP + docs, не Wordstat)

- cursor subscriptions мониторинг PR, cloud agent wake on event  
- cursor slack @cursor check back, subscription slack thread  
- cursor automations vs subscriptions, cursor.com/automations  
- /goal fix flaky tests, /subscribe skill, /loop cron  
- /autopilot PR watch (/babysit alias), /in-cloud subagent VM  
- spend limit cloud agents, GitHub integration dashboard  
- autofix CI GitHub Actions, @cursor autofix off  
- secrets cloud agent environment, routing rules slack  

**SEO-стратегия:** в H1/lead явно «**Cursor Subscriptions (фича cloud agents)**»; primary `cursor subscriptions` — с уточнением в subtitle; secondary в H2: `cursor cloud agents pr`, `cursor subscriptions slack`, `/goal`, `babysit`/`autopilot`. Не конкурировать с vc.ru по «оплате Cursor из России».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| 19 августа 2026 Cursor выпустил Subscriptions: cloud agents мониторят PR, Slack-треды и scheduled tasks | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Subscriptions доступны **только для cloud agents** («for now») | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Cloud agents **автоматически подписываются** на PR, которые сами создали; чинят CI и отвечают на bot-комментарии | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Пример Slack-подписки: `@cursor check back in an hour and keep going until that feedback is in` | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Команда `/goal` задаёт long-lived objective до полного выполнения (пример: fix flaky tests, CI green) | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Subagents запускаются на **изолированных VM** с отдельной копией проекта и clean context | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Steering: follow-up ждёт **следующий tool call**, не прерывает текущее действие | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |
| Подписка оформляется промптом («open a PR and keep it green until merge») или skill **`/subscribe`** | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | 25.08.2026 | да |
| GitHub events: PR activity (comments, reviews, lifecycle), CI на branch | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | 25.08.2026 | да |
| Slack events: replies in thread, channel messages, new public channels | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | 25.08.2026 | да |
| Linear events: issue state/comments | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | 25.08.2026 | да |
| Timers: one-off delay или recurring cron; также built-in **`/loop`** | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | 25.08.2026 | да |
| Subscription max **180 days**; agent отписывается, когда wait завершён | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | 25.08.2026 | да |
| Bursts coalesce: несколько событий подряд → один wake, agent re-reads source | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | 25.08.2026 | да |
| Auto-fix CI: только **GitHub Actions** | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | 25.08.2026 | да |
| Auto-fix **не срабатывает**, если: новый human commit; follow-up пользователю; тот же failing check на base; уже **10** CI-failure follow-ups на PR | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | 25.08.2026 | да |
| Отключить autofix на PR: коммент `@cursor autofix off`; включить: `@cursor autofix on` | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | 25.08.2026 | да |
| Auto-fix CI failures на **Teams**; для non-Teams «coming soon» — можно явно попросить agent мониторить PR | [cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities) | 25.08.2026 | да |
| Cloud Agents доступны на **всех paid планах** Cursor | [cursor.com/help/ai-features/cloud-agents](https://cursor.com/help/ai-features/cloud-agents) | 25.08.2026 | да |
| При первом запуске cloud agents просят установить **spend limit** | [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent) | 25.08.2026 | да |
| GitHub: Connect на [cursor.com/dashboard/integrations](https://cursor.com/dashboard/integrations), scope All или Selected repos | [cursor.com/docs/integrations/github](https://cursor.com/docs/integrations/github) | 25.08.2026 | да |
| Slack setup: Connect → install app → connect repo provider → **enable usage-based pricing** → privacy | [cursor.com/docs/integrations/slack](https://cursor.com/docs/integrations/slack) | 25.08.2026 | да |
| Slack: `@Cursor help` — список команд; `@Cursor agent [prompt]` — новый agent в треде | [cursor.com/docs/integrations/slack](https://cursor.com/docs/integrations/slack) | 25.08.2026 | да |
| **Automations** — standing rules на [cursor.com/automations](https://cursor.com/automations); каждый trigger → **новый** cloud agent run | [cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations) | 25.08.2026 | да |
| **Subscription** — running agent **держит** подписку на PR/thread до done (stateful) | [learncursor.dev/.../cloud-agent-automations](https://www.learncursor.dev/learn/cursor-agents/cloud-agent-automations) | 2026 | да (secondary, ссылается на changelog) |
| `/babysit` переименован в **`/autopilot`** на desktop; `/babysit` — search alias | [forum.cursor.com/t/babysit-disappeared/167381](https://forum.cursor.com/t/babysit-disappeared/167381) | 2026 | да (community + staff) |
| ce-babysit-pr skill: watch PR until merge-ready (review, CI, base movement) | [cursor.com/marketplace/skills/ce-babysit-pr](https://cursor.com/marketplace/skills/ce-babysit-pr) | 25.08.2026 | да |
| Custom Mode: skill pinned в чате через `/` → ⌥⏎ (Mac) / Alt+Enter (Win) | [cursor.com/changelog/08-19-26](https://cursor.com/changelog/08-19-26) | 19.08.2026 | да |

**fact-bank.md:** записей по Cursor Subscriptions нет — все цифры только из таблицы выше.

**Не использовать без оговорки:** «500 000 пользователей Cursor» из pikabu/vc.ru (не в fact-bank); цены Pro $20/Teams $40 — только если writer добавит блок «минимальный план для cloud agents», со ссылкой на cursor.com/pricing, не как фокус статьи.

---

## 4. Subscriptions vs Automations (writer must-have)

| | **Automations** | **Subscriptions** |
|---|-----------------|-------------------|
| Где настраивается | [cursor.com/automations](https://cursor.com/automations) — UI правило | В **running cloud agent** (промпт или `/subscribe`) |
| Модель | One-shot: событие → **новый** agent run | Stateful: agent **спит** и **просыпается** на том же thread/PR |
| Когда брать | Cron digest, triage каждого нового PR, webhook | «Доведи **этот** PR до merge», «жди ответ в **этом** Slack-треде» |
| Связка | Можно стартовать automation, agent внутри возьмёт subscription | `/goal` + subscription на PR = длинная задача без ручного чата |

---

## 5. Угол статьи (utility-only, режим B)

**Главный угол:** за **30–45 минут** подключить GitHub + Slack + spend limit, запустить **первый cloud agent** с **subscription на PR**, проверить wake-on-CI/review, затем настроить **мониторинг Slack-треда** и связать с **`/goal`** или **`/autopilot`** для merge-ready PR без babysitting в чате.

**Почему отличается от конкурентов:**
- Официальный changelog — анонс, не setup.
- RU-SERP по `cursor subscriptions` = оплата, не фича.
- EN automations-гайды не дают русский security checklist и не связывают PR + Slack + /goal в одном workflow.

**Tone:** «Subscription = будильник для cloud agent: PR прокомментировали — agent проснулся и продолжил». Без hype «агент заменит команду».

**H2-каркас (из карточки B06 + research):**
1. Subscriptions vs Automations после 19.08.2026  
2. GitHub, Slack, spend limit перед первым run  
3. Автоподписка на PR: CI + bot comments  
4. Slack-тред: `@cursor check back…` и wake-on-reply  
5. `/goal`, `/in-cloud`, `/autopilot` (/babysit)  
6. Чек-лист безопасности: secrets, repo scope, Test run, Run History  

**Internal links:** B03 MCP (`/podklyuchenie-mcp-cursor/`) — team MCP для cloud agents.

---

## 6. FAQ-кандидаты (из faq_hints + research)

1. **Чем Subscriptions отличается от Automations?** — Automations = правило в UI, новый run на каждый trigger; Subscription = agent держит watch на конкретном PR/thread.  
2. **Как попросить Cursor следить за pull request?** — Cloud agent с промптом «open PR and keep green until merge» или `/subscribe`; авто-подписка на PR, созданные agent.  
3. **Может ли Cursor мониторить Slack-тред?** — Да, cloud agent + Slack integration; пример `@cursor check back in an hour…`.  
4. **Нужен ли Teams для auto-fix CI?** — Auto-fix CI failures officially Teams-only (на момент docs); иначе явный prompt `@cursor fix CI`.  
5. **Работают ли Subscriptions в локальном Agent?** — Нет, только cloud agents.  
6. **Сколько живёт subscription?** — До 180 дней или пока agent не решит, что wait окончен.  
7. **/babysit или /autopilot?** — Desktop: `/autopilot`; `/babysit` — alias; skill ce-babysit-pr в Marketplace.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение Subscriptions 40–60 слов | Lead | «Cursor Subscriptions — …» (не тариф!) |
| Таблица Subscriptions vs Automations | H2-1 | См. раздел 4 |
| Workflow ASCII | H2-2–4 | Dashboard → Cloud Agent → PR subscription → Slack wake |
| Таблица GitHub/Slack/Linear events | H2-3 | Из capabilities docs |
| Чек-лист безопасности 10+ пунктов | H2-6 | secrets, scope, spend limit, autofix off |
| FAQ 5–7 | Конец | Ответы-действия |
| HowTo schema steps | handoff schema | Из action_outline |

---

## 8. Риски для writer

- **Дизамбiguация:** «subscriptions» ≠ «подписка Pro»; в первых 100 словах — про event monitoring.  
- Не выдумывать UI-скриншоты dashboard — описывать пути URL (`/dashboard/integrations`, `/dashboard/cloud-agents`, `/dashboard/spending`).  
- `/babysit` и `/autopilot` — упомянуть оба + forum rename.  
- Auto-fix CI: оговорка Teams-only из официальной docs.  
- Min **5** нумерованных шагов + чеклист **10+** (utility gate статьи).  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Без эмодзи; CTA ≤ 3.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель подключит GitHub и Slack в Cursor Dashboard, выставит spend limit, запустит cloud agent с subscription на PR (auto-fix CI и review comments), настроит wake-on-reply в Slack-треде и при необходимости закрепит long-running задачу через `/goal` или PR-watching через `/autopilot`, пройдя чек-лист безопасности перед production repo.

**action_outline (для writer):**

1. **Проверить план:** paid Cursor (Pro+); открыть [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents) — раздел Environments доступен.  
2. **Integrations:** [dashboard/integrations](https://cursor.com/dashboard/integrations) → Connect **GitHub** (All или Selected repos) → Connect **Slack** → install app → connect repo provider → **enable usage-based pricing** → confirm privacy.  
3. **Spend limit:** [dashboard/spending](https://cursor.com/dashboard/spending) → включить on-demand → задать monthly limit **до** первого cloud run.  
4. **Environment:** создать cloud environment (repo, secrets, Test run / Build) — secrets только через Dashboard, не в промпте.  
5. **Первый PR subscription:** запустить cloud agent (web/agents или `@cursor` в Slack) с промптом «implement X, open PR, keep it green until merge» или `/subscribe` + цель; убедиться, что agent **auto-subscribed** на свой PR.  
6. **Проверить wake-on-CI:** дождаться failing check или симулировать; agent должен re-wake (лимит 10 autofix follow-ups); при необходимости `@cursor autofix off` на тестовом PR.  
7. **Slack thread subscription:** в треде с agent — `@cursor check back in an hour and keep going until that feedback is in` (или свой критерий done); проверить wake при новом reply.  
8. **Long-running objective:** в cloud chat — `/goal fix all flaky tests and make CI green` (или свой DoD); опционально Custom Mode + `/loop` для recurring check-ins.  
9. **PR babysitting:** `/autopilot` (alias `/babysit`) или skill ce-babysit-pr для watch до merge-ready; steering mid-run — follow-up без прерывания tool call.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ unavailable (fallback SERP) |
| Таблица фактов с URL | ✅ (28 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B06
article_dir: memory/blog/articles/B06-cursor-subscriptions-nastrojka-2026
status: ✅ PASS
utility_verdict: PASS
summary: SERP — 8 источников (changelog 19.08.2026, capabilities, Slack docs, learncursor, ai-tldr, explainx, byteiota, shtruzel). Wordstat MCP недоступен — семантика через WebSearch; primary «cursor subscriptions» = pricing noise, угол — event Subscriptions. 28 фактов с URL, таблица vs Automations, 9 шагов action_outline, 7 FAQ. Internal: B03 MCP. Готов к writer.
===
