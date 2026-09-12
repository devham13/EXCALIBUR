# Research notes — B06 «Как настроить Claude Code в CI/CD: пошаговая инструкция для GitHub Actions и headless-режима»

**topic_id:** B06  
**slug:** nastrojka-claude-code-ci-cd-2026  
**article_mode:** B (how-to + checklist)  
**research_date:** 2026-09-12  
**disclaimer:** Все даты, версии и статистика проверены на 12.09.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) | Официальная дока | Канон: `/install-github-app`, interactive vs automation mode, секреты, OIDC/WIF, `claude_args`, troubleshooting | Английский; мало про bare `-p` в generic CI | Сухой перевод без чеклиста «что делать / не делать» |
| 2 | [code.claude.com/docs/ru/github-actions](https://code.claude.com/docs/ru/github-actions) | Официальная RU | Локализованный quick setup, права GitHub App | Нет GitLab + headless в одном месте | Дублировать структуру docs 1:1 |
| 3 | [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) | Официальная дока | `-p`, `--bare`, `--allowedTools`, `--permission-mode`, JSON-вывод | Нет GitHub Actions YAML целиком | Вырезать security-блок без контекста CI |
| 4 | [code.claude.com/docs/en/gitlab-ci-cd](https://code.claude.com/docs/en/gitlab-ci-cd) | Официальная beta-дока | Готовый `.gitlab-ci.yml`, OIDC Bedrock/Vertex, `--max-turns`, cost tips | Beta; интеграция от GitLab, не Anthropic | Обещать GA-фичи как стабильные |
| 5 | [github.com/anthropics/claude-code-action](https://github.com/anthropics/claude-code-action) | Официальный репозиторий | Mode detection, cloud providers, setup/usage guides | Технический README, не how-to для B2B | Копировать marketing bullets без практики |
| 6 | [aiforanything.io/.../claude-code-github-actions-cicd-integration-guide-2026](https://aiforanything.io/blog/claude-code-github-actions-cicd-integration-guide-2026) | Англ. longread 2026 | PR review workflow, `CLAUDE.md` как CI policy | Англ.; возможны устаревшие checkout@v4 | Цены/лимиты без первичника |
| 7 | [hidekazu-konishi.com/.../claude_code_cicd_and_headless_automation](https://hidekazu-konishi.com/entry/claude_code_cicd_and_headless_automation.html) | Глубокий гайд (июнь 2026) | Headless + guardrails + exit codes + cost caps | Очень длинный EN; перегруз для ЦА блога | Структуру 1:1; англоязычный тон |
| 8 | [continuumcode.ai/guides/claude-code-github-actions](https://continuumcode.ai/guides/claude-code-github-actions/) | Security-focused | `pull_request_target` риск, OAuth vs API key, bot loops | Не официальный источник | Утверждения без сверки с docs Anthropic |

**Паттерн SERP:** топ — официальные docs Anthropic/GitLab + англоязычные гайды 2026. Русскоязычный how-to, который **сшивает** GitHub Action + headless `claude -p` + GitLab job + чеклист безопасности — редок.

**Intent:** `how_to` — DevOps/техлид хочет **запустить** Claude Code в пайплайне (Actions или GitLab), выбрать режим (App vs `-p`), настроить секреты и ограничить риски.

**Пробел для блога:** один практический гайд на русском: «сначала выбери путь → настрой секреты → минимальный workflow → hardening → отладка», с internal links на MCP Cursor и n8n-агентов.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT MCP UNAVAILABLE:** namespace `user-mcp-kv` не подключён в среде Cloud Agent (инструмент `wordstat_get_top_requests` недоступен). **Точные объёмы показов не получены** — таблица ниже не заполнена.

При восстановлении MCP повторить запросы:
- `claude code ci cd` (primary)
- `claude code github actions`
- `claude code headless`
- `claude code gitlab ci`
- `настройка claude code`

### Семантический fallback (SERP + secondary_queries, без цифр спроса)

| Кластер | LSI / смежные формулировки |
|---------|---------------------------|
| CI/CD интеграция | claude code ci cd, claude code в пайплайне, claude code github actions, claude code gitlab ci |
| Headless CLI | claude -p, claude --print, headless режим claude code, claude --bare |
| GitHub | anthropics/claude-code-action, install-github-app, @claude mention, ANTHROPIC_API_KEY, CLAUDE_CODE_OAUTH_TOKEN |
| Безопасность | --allowedTools, --permission-mode dontAsk, --max-turns, --max-budget-usd, pull_request_target |
| Конфиг | CLAUDE.md в CI, --output-format json, claude_args, timeout job |
| GitLab beta | mcp__gitlab, AI_FLOW_INPUT, masked CI/CD variables, OIDC Bedrock/Vertex |

**SEO-стратегия для writer:** primary «claude code ci cd» в H1/lead; secondary в H2 — «github actions», «headless», «gitlab ci»; русские якоря «настройка claude code», «как запустить claude code в ci».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Headless-режим: флаг `-p` / `--print` запускает Claude Code без интерактива; exit 0 при успехе, non-zero при ошибке | [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) | 12.09.2026 | да |
| `--bare` пропускает hooks, skills, plugins, MCP, auto memory и CLAUDE.md — быстрее и воспроизводимее в CI | [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) | 12.09.2026 | да |
| `--bare` рекомендован для scripted/SDK вызовов; станет default для `-p` в будущем релизе | [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) | 12.09.2026 | да |
| В bare mode для Anthropic API нужен `ANTHROPIC_API_KEY` в env; OAuth/subscription login не используется | [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) | 12.09.2026 | да |
| `--output-format json` возвращает `total_cost_usd` и breakdown по моделям (оценка на клиенте) | [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) | 12.09.2026 | да |
| Piped stdin в `-p` ограничен 10 MB | [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) | 12.09.2026 | да |
| `--max-turns` ограничивает agentic turns в print mode; при превышении — ошибка | [code.claude.com/docs/en/cli-reference](https://code.claude.com/docs/en/cli-reference) | 12.09.2026 | да |
| `--max-budget-usd` — hard cap на spend API в print mode (v2.1.217+) | [code.claude.com/docs/en/cli-reference](https://code.claude.com/docs/en/cli-reference) | 12.09.2026 | да |
| `--permission-mode dontAsk` отклоняет tool calls без pre-approve — паттерн для locked-down CI | [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) | 12.09.2026 | да |
| Официальный GitHub Action: `anthropics/claude-code-action@v1` | [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) | 12.09.2026 | да |
| Quick setup: команда `/install-github-app` в Claude Code; требуется admin repo + `gh auth login` | [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) | 12.09.2026 | да |
| Interactive mode: без `prompt` в workflow — ждёт `@claude` в issue/PR comment | [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) | 12.09.2026 | да |
| Automation mode: с `prompt` — запуск по триггеру workflow без mention | [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) | 12.09.2026 | да |
| Секреты: `ANTHROPIC_API_KEY` (API) или `CLAUDE_CODE_OAUTH_TOKEN` (OAuth через `claude setup-token`, Pro/Max/Team/Enterprise) | [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) | 12.09.2026 | да |
| Перед запуском Action: write access triggering user + reject bot actors (кроме `allowed_bots`) | [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) | 12.09.2026 | да |
| Минимальные permissions job: `contents: write`, `pull-requests: write`, `issues: write`, `id-token: write` | [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) | 12.09.2026 | да |
| Cost control: `--max-turns` в `claude_args`, workflow timeout, concurrency limits | [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) | 12.09.2026 | да |
| GitLab CI/CD интеграция — **beta** (поддержка GitLab) | [code.claude.com/docs/en/gitlab-ci-cd](https://code.claude.com/docs/en/gitlab-ci-cd) | 12.09.2026 | да |
| GitLab quick start: image `node:24-alpine3.21`, install `curl -fsSL https://claude.ai/install.sh \| bash`, PATH `$HOME/.local/bin` | [code.claude.com/docs/en/gitlab-ci-cd](https://code.claude.com/docs/en/gitlab-ci-cd) | 12.09.2026 | да |
| GitLab job example: `claude -p ... --permission-mode acceptEdits --allowedTools "Bash Read Edit Write mcp__gitlab"` | [code.claude.com/docs/en/gitlab-ci-cd](https://code.claude.com/docs/en/gitlab-ci-cd) | 12.09.2026 | да |
| GitLab: masked variable `ANTHROPIC_API_KEY`; для MR — `CI_JOB_TOKEN` или PAT `GITLAB_ACCESS_TOKEN` | [code.claude.com/docs/en/gitlab-ci-cd](https://code.claude.com/docs/en/gitlab-ci-cd) | 12.09.2026 | да |
| Enterprise providers: Bedrock (GitLab→AWS OIDC), Vertex (WIF), без long-lived keys в repo | [code.claude.com/docs/en/gitlab-ci-cd](https://code.claude.com/docs/en/gitlab-ci-cd) | 12.09.2026 | да |
| `CLAUDE.md` в корне repo — persistent policy для interactive и headless runs | [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) | 12.09.2026 | да |

**Не использовать без первичника:** конкретные $/review из SFEIR FAQ; «@beta retired» — сверять с актуальной docs при publish.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** читатель **выбирает** путь (GitHub App/Action vs bare `claude -p`), **настраивает** секреты и минимальный workflow, **ограничивает** tools/turns/budget, **прогоняет** тестовый job и получает чеклист перед продакшеном.

**Отличие от конкурентов:**
- Официальные docs разнесены по GitHub / GitLab / headless — статья собирает decision tree на русском.
- Англ. longread'ы не дают B2B-языка «что делать / не делать» для команды без deep Anthropic-экспертизы.
- Связка с экосистемой блога: MCP (B03), оркестрация агентов n8n (B05).

**Tone:** инструкция для техлида/DevOps; термины headless, OIDC, MCP — сразу с пояснением; без «новости Anthropic».

**H2-каркас (из карточки + research):**
1. Headless vs GitHub App: когда `claude -p`, когда `claude-code-action`
2. Секреты и auth: API key vs OAuth vs OIDC/WIF
3. GitHub Actions: quick `/install-github-app` + automation workflow
4. GitLab CI: minimal job + triggers
5. Безопасность: `--bare`, `--allowedTools`, `--permission-mode`, `--max-turns`, timeout
6. Отладка + чеклист перед prod + FAQ

**Internal links (из карточки):**
- `/podklyuchenie-mcp-cursor/` — MCP в dev-среде vs CI
- `/avtomatizaciya-n8n-ai-agents/` — оркестрация агентов рядом с CI

---

## 5. Decision matrix (черновик для writer)

| Критерий | `claude -p` в job | `anthropics/claude-code-action` |
|----------|-------------------|----------------------------------|
| Setup | install script / npm + env secret | `/install-github-app` или manual App + workflow |
| Триггер | любой shell step (GitHub, GitLab, Jenkins) | GitHub events + `@claude` или `prompt` |
| Контекст GitHub | вручную checkout + gh CLI/MCP | встроено (comments, PR, commits) |
| Воспроизводимость | `--bare` + явные flags | `claude_args` passthrough |
| Лучше когда | generic CI, custom JSON pipeline | PR/issue automation на GitHub |

---

## 6. FAQ-кандидаты (из faq_hints + research)

1. **Как запустить Claude Code в GitHub Actions?** — `/install-github-app` или manual: App + `ANTHROPIC_API_KEY` + `anthropics/claude-code-action@v1`.
2. **Что такое headless режим?** — `claude -p "prompt"`; один прогон agent loop, exit code для CI.
3. **Чем `--bare` отличается от обычного `-p`?** — не грузит hooks/plugins/MCP/CLAUDE.md; нужен `ANTHROPIC_API_KEY`.
4. **Безопасно ли Claude Code в CI/CD?** — да при least-privilege tools, `dontAsk`, caps turns/budget, без `pull_request_target` + untrusted diff.
5. **OAuth или API key в CI?** — API key/OIDC для org; OAuth token привязан к одному subscription.
6. **GitLab поддерживается?** — да, beta job в `.gitlab-ci.yml` + masked variables.
7. **Как контролировать стоимость?** — `--max-turns`, `--max-budget-usd`, job timeout, `--output-format json` + `total_cost_usd`.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение headless Claude Code 40–60 слов | Lead | «Headless Claude Code — …» |
| Decision table headless vs Action | H2-1 | Таблица + «выбирай если» |
| Workflow YAML (минимальный GH + GL) | H2-3, H2-4 | Code blocks + комментарии |
| Security checklist 10+ пунктов | H2-5 | Чеклист |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** claude code ci cd, claude code github actions, claude code headless, настройка claude code, claude -p --bare.

---

## 8. Риски для writer

- Не выдумывать Wordstat-цифры — MCP недоступен.
- GitLab integration — явно beta.
- Не обещать bypass security checks Action (write access, bot filter).
- Объём: 8 500–9 500 знаков (quality-blog).
- Min 5 нумерованных шагов + чеклист 10+ пунктов (utility gate статьи).
- Без эмодзи; utility-only — каждый H2 = подзадача + рекомендация.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель выберет схему интеграции (GitHub Action или headless `claude -p`), добавит секреты, соберёт рабочий workflow для GitHub Actions и/или GitLab CI с `--bare`/`--allowedTools`/`--max-turns`, прогонит тестовый job и пройдёт чеклист безопасности перед продакшеном.

**action_outline (для writer):**

1. **Выбрать путь:** GitHub-only automation → `claude-code-action`; multi-CI или кастомный JSON → `claude -p` + `--bare`.
2. **Создать credential:** `ANTHROPIC_API_KEY` в Secrets (GitHub) или masked variable (GitLab); для org — рассмотреть OIDC/WIF вместо long-lived key.
3. **GitHub quick path:** локально `claude` → `/install-github-app` → merge workflow PR → тест `@claude` или automation `prompt`.
4. **Headless job (любой CI):** install via `https://claude.ai/install.sh`, export PATH, `claude --bare -p "..." --allowedTools "Read" --permission-mode dontAsk --output-format json`.
5. **Добавить `CLAUDE.md`:** стандарты review/implement для стабильного поведения в CI.
6. **GitLab (beta):** скопировать minimal job из docs, `rules` под MR/web trigger, `--allowedTools "Bash Read Edit Write mcp__gitlab"`.
7. **Hardening:** `--max-turns`, `--max-budget-usd`, job `timeout`, concurrency; не использовать `pull_request_target` с agent на untrusted PR.
8. **Проверить run:** exit code, JSON `total_cost_usd`, логи permission denied → сузить `--allowedTools`.
9. **Чеклист prod:** secrets masked, bot loop prevention, human MR review, rollback plan.

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ недоступен (fallback LSI) |
| Таблица фактов с URL | ✅ (22 факта) |
| utility_verdict + action_outline | ✅ |
| Decision matrix + FAQ | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.
