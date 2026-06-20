# Excalibur BLOG — Cloud Automation Setup

Настройка запуска в **Cursor Cloud Agents / Automations** по образцу [kovcheg-office-cloud](https://github.com/Horosheff/kovcheg-office-cloud).

## Что запускаем

Пайплайн одной статьи:

```text
today → [Scout?] → research_start → research → writer → geo-qa → cover||schema → indexer → publish
```

## Структура репозитория (как у Kovcheg Cloud)

```text
<PROJECT_ROOT>/
  AGENTS.md                          ← инструкции Cloud Agent
  CLOUD-AUTOMATION.md                ← этот файл
  .env.example
  .cursor/
    agents/                          ← Task types для Cloud
    skills/
    rules/
    excalibur-blog-handoff.md        ← runtime, не в git
    excalibur-blog-fragments/        ← cover + schema parallel
  agents/                            ← исходники плагина
  skills/
  shared/
  scripts/
  memory/
  .cursor-plugin/plugin.json
```

## Cursor docs

- [Cloud Agents setup](https://cursor.com/docs/cloud-agent/setup.md)
- [Secrets / env vars](https://cursor.com/docs/cloud-agent/setup.md#environment-variables-and-secrets)
- [Automations](https://cursor.com/docs/cloud-agent/automations.md)
- [Self-hosted pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md)
- [MCP in Cloud](https://cursor.com/docs/cloud-agent/capabilities.md#mcp-tools)

## Self-hosted worker

Нужен, если в облаке Cursor нет:

- MCP KV (`gpt-image-2` для обложек);
- FTP к WordPress;
- стабильного web search для research.

```powershell
cd "<PROJECT_ROOT>"
$env:CURSOR_API_KEY="YOUR_KEY"
$env:EXCALIBUR_PROJECT_ROOT="<PROJECT_ROOT>"
agent worker start --pool --pool-name excalibur-blog --idle-release-timeout 600
```

## Secrets / env vars

Из `.env.example` + Cloud Dashboard:

| Variable | Зачем |
|----------|--------|
| `EXCALIBUR_PUBLIC_SITE_URL` | Production WP URL — link verify, publish, post-publish check (project-scoped) |
| `FTP_*` | `excalibur_blog_wp_publish.py` |
| `EXCALIBUR_BLOG_ALLOW_PUBLISH` | `yes` только когда готовы публиковать |
| `EXCALIBUR_TOPIC_ID` | опционально фиксировать тему (иначе today.py предложит P0) |
| `EXCALIBUR_PROJECT_ROOT` | корень репо на worker |

Не коммитить: `memory/site.env.local`, реальные ключи MCP.

## Automation schedule

Cursor Automation → Schedule, пример:

```text
0 10,15,20 * * *
```

- Repository: ваш fork `excalibur-blog` / EXCALIBUR
- Worker pool: `excalibur-blog`
- Branch: `main`

## Automation prompt (шаблон)

**Канонический промпт (Scout + полный pipeline + publish):**  
→ **`shared/excalibur-blog-automation-prompt.md`** — копируй блок PROMPT в Cursor Automation.

Краткая версия:

```text
Работай автономно. Не спрашивай подтверждения на deploy, SSH, SFTP, QA, исправления и publish.

Ты — Директор Excalibur BLOG. Прочитай AGENTS.md, shared/excalibur-blog-automation-prompt.md, shared/production-site.md.

1. today.py → если нет свободной P0 → Task(excalibur-blog-scout) → today.py снова
2. utility gate + research_start
3. Task: research → writer → geo-qa
4. ПАРАЛЛЕЛЬНО Task: cover + schema (после QA PASS)
5. Task: indexer → publish (default yes)
6. Live check $EXCALIBUR_PUBLIC_SITE_URL/{slug}/ → commit/PR

Fallback: generalPurpose per role (AGENTS.md). Финал: PIPELINE DONE + live_url.
```

## После каждого прогона

Проверь изменения:

- `shared/published-articles.md` (если publish)
- `memory/blog/excalibur-blog-run-log.md`
- артефакты в `memory/blog/articles/<topic_id>-<slug>/`

Если Automation через PR — merge PR, чтобы следующий run видел ledger.

## Локальная разработка плагина

Правки agents/skills делай в `agents/` и `skills/`, затем **синхронизируй в `.cursor/`**:

```powershell
Copy-Item agents\* .cursor\agents\ -Force
Copy-Item skills\* .cursor\skills\ -Recurse -Force
Copy-Item rules\* .cursor\rules\ -Force
```

Или добавь script `scripts/sync_cursor_cloud.ps1` при необходимости.
