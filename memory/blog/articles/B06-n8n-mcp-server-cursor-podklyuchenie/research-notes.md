# Research notes — B06 «Как подключить n8n к Cursor через MCP: Server Trigger и instance-level MCP»

**topic_id:** B06  
**slug:** n8n-mcp-server-cursor-podklyuchenie  
**article_mode:** B (how-to)  
**research_date:** 2026-10-10  
**disclaimer:** Все даты, версии и статистика проверены на 10.10.2026 (2026 год).

---

## 1. SERP-обзор (WebSearch; research-serp.json — все 7 запросов failed SSL timeout)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | Официальная docs EN | Канон instance-level: enable, OAuth/API key, expose workflows, troubleshooting | Английский; два режима (instance vs Trigger) разнесены по разным страницам | Сухой перевод без выбора «что вам в Cursor» |
| 2 | [docs.n8n.io/connect/.../mcp-client-examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples) | Официальная docs EN | Готовый JSON для Cursor (`streamable-http`), one-click, Claude supergateway pattern | Нет сценария «один tool = один бизнес-процесс» | Копировать только JSON без контекста test/production |
| 3 | [docs.n8n.io/.../mcptrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/) | Официальная docs EN | MCP Server Trigger: URL, auth, queue mode, nginx, mcp-remote для Claude | Не про Cursor напрямую (remote HTTP) | Путать URL workflow-trigger с `/mcp-server/http` |
| 4 | [serhiilabs.dev/.../building-an-mcp-server-for-n8n](https://serhiilabs.dev/n8n-automation/building-an-mcp-server-for-n8n/) | RU/EN блог 2026 | Сравнение официального MCP vs community `n8n-mcp`, лимит tools в Cursor, WEBHOOK_SECURITY_MODE | Community-цифры по лимиту tools | Выдавать «~40 tools» за официальный SLA Cursor |
| 5 | [perlod.com/tutorials/n8n-mcp-server-trigger-setup](https://perlod.com/tutorials/n8n-mcp-server-trigger-setup/) | EN tutorial | Пошагово Call n8n Workflow Tool, Execute Workflow Trigger, publish sub-workflow | Только Trigger-path; мало Cursor | Структура 1:1 |
| 6 | [github.com/czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp/blob/main/docs/CURSOR_SETUP.md) | Community MCP (stdio) | Документация n8n через npx, N8N_API_KEY | **Не** официальный instance MCP; другой продукт | Путать `n8n-mcp` (stdio docs) с `/mcp-server/http` |
| 7 | [mayai.ru/n8n-gayd-biznes-ai-agenty-mcp](https://mayai.ru/n8n-gayd-biznes-ai-agenty-mcp/) | RU гайд (свой сайт) | Бизнес-угол, версия ≥2.18.4, связка Cursor | Обзорный; меньше Trigger vs instance | Каннибализация: B06 = узкий how-to connect |
| 8 | [mayai.ru/podklyuchenie-mcp-cursor](https://mayai.ru/podklyuchenie-mcp-cursor/) | RU how-to (B03) | Общий MCP в Cursor | Нет n8n endpoint | Дублировать B03; только internal link |

**Паттерн SERP:** доминирует **официальная документация n8n** (Connect + Trigger). Русскоязычный intent «подключить n8n к cursor mcp» закрыт фрагментами на mayai.ru и EN-туториалами по Trigger. **Пробел:** один русский how-to, который **сразу помогает выбрать** instance-level (управление/запуск workflow из IDE) vs MCP Server Trigger (кастомный набор tools для одного сценария) и доводит до зелёного статуса в Cursor.

**Intent:** how_to — пользователь хочет **подключить Cursor к n8n** (OAuth или Bearer), увидеть tools и **осознанно выбрать** режим; вторично — опубликовать workflow с Trigger и отдать production URL в remote-конфиг (если не хватает instance-level).

**Связь с внутренними статьями:** [B03 podklyuchenie-mcp-cursor](/podklyuchenie-mcp-cursor/) — базовый MCP в Cursor; [B02 avtomatizaciya-n8n-ai-agents](/avtomatizaciya-n8n-ai-agents/) — агенты в n8n. B06 = мост «IDE ↔ ваш n8n».

---

## 2. Яндекс Wordstat

⚠️ **WORDSTAT UNAVAILABLE:** namespace `user-mcp-kv` / инструмент `wordstat_get_top_requests` **отсутствует** в Cloud run 2026-10-10. Точные показы/мес **не получены**; цифры спроса не выдумывать.

**Экспертная семантика (без объёмов):** ядро — `n8n mcp server`, `n8n mcp cursor`, `mcp server trigger n8n`, `подключить n8n cursor mcp`; LSI — `instance-level MCP`, `/mcp-server/http`, `streamable-http`, `Available in MCP`, `Call n8n Workflow Tool`, `Bearer`, `OAuth`, `production URL`, `mcp-remote`, `supergateway`.

**SEO-стратегия writer:** primary «n8n mcp server» + «n8n mcp cursor» в title/lead; secondary «mcp server trigger n8n» в H2 про Trigger; русский long-tail «подключить n8n к cursor mcp» в FAQ.

---

## 3. Таблица фактов (только с URL; fact-bank.md про n8n MCP пуст)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Instance-level MCP: один коннект на инстанс, централизованная auth, выбор workflow для доступа | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| MCP Server Trigger: tools **только из одного workflow**; кастомное поведение MCP-сервера | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| Server URL instance-level заканчивается на **`/mcp-server/http`** | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| Enable: **Settings → Instance-level MCP → Enable MCP access** (owner/admin) | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| UI «Connection details / Connect a client / Allowed callback URLs» — с **n8n 2.33.0** | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| Auth клиентов: **OAuth (recommended)** или **API key** (Bearer token) | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| API key: токен показывается **один раз** при генерации; после ухода с вкладки — redacted | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| Workflow в MCP: toggle **Available in MCP** (меню workflow / Settings) или список Workflows enabled | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| `search_workflows` — превью всех доступных пользователю workflow; execute/modify только при явном enable | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| Создание/редактирование workflow через MCP — с **n8n 2.13.0** | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| `execute_workflow` по умолчанию **production** (published version); есть режим `manual` для черновика | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| Cursor manual config: `"type": "streamable-http"`, `"url": "https://<domain>/mcp-server/http"` | [docs.n8n.io/.../mcp-client-examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples) | 10.10.2026 | да |
| Cursor: **One-click setup** из Connect a client → Your client → Cursor | [docs.n8n.io/.../mcp-client-examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples) | 10.10.2026 | да |
| Self-hosted/local: в примерах допускается **`http://`** (например localhost:5678) вместо https | [docs.n8n.io/.../mcp-client-examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples) | 10.10.2026 | да |
| MCP Server Trigger: транспорты **SSE** и **streamable HTTP**; **stdio не поддерживается** | [docs.n8n.io/.../mcptrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/) | 10.10.2026 | да |
| Trigger: **Test URL** (Listen for Test Event / Execute) vs **Production URL** (после Publish) | [docs.n8n.io/.../mcptrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/) | 10.10.2026 | да |
| Trigger auth: **None / Bearer / Header** | [docs.n8n.io/.../mcptrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/) | 10.10.2026 | да |
| Workflow как tool: нода **Custom n8n Workflow Tool** (в UI также **Call n8n Workflow Tool**) к коннектору Tools | [docs.n8n.io/.../mcptrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/) | 10.10.2026 | да |
| Queue mode + несколько webhook replicas: маршрутизировать **`/mcp*`** на **одну** dedicated replica | [docs.n8n.io/.../mcptrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/) | 10.10.2026 | да |
| Claude Desktop к Trigger URL: **`mcp-remote`** + Bearer в env (обход отсутствия stdio) | [docs.n8n.io/.../mcptrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/) | 10.10.2026 | да |
| Полное отключение MCP на self-host: **`N8N_DISABLED_MODULES=mcp`** | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| За reverse proxy: allowlist заголовков **`MCP-Protocol-Version`**, **`Mcp-Method`**, **`Mcp-Name`** (CORS с **2.36.0**) | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| Project/folder bulk MCP enable — с **n8n 2.24.0** | [docs.n8n.io/connect/connect-to-n8n-mcp-server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) | 10.10.2026 | да |
| Cursor: глобальный `~/.cursor/mcp.json`, проектный `.cursor/mcp.json`; настройка через Customize / docs MCP | [cursor.com/docs/mcp](https://cursor.com/docs/mcp) | 10.10.2026 | да |
| Cursor forum: предупреждение про **~40 enabled tools**; в обсуждениях 2025–2026 упоминают порог **80** как soft limit на новых билдах | [forum.cursor.com/t/mcp-40-tools-way-to-less/79686](https://forum.cursor.com/t/mcp-40-tools-way-to-less/79686) | 10.10.2026 | да (community, не SLA) |
| mayai.ru: instance-level MCP для Cursor/Claude — рекомендуемый минимум **n8n ≥ 2.18.4** | [mayai.ru/n8n-gayd-biznes-ai-agenty-mcp](https://mayai.ru/n8n-gayd-biznes-ai-agenty-mcp/) | 10.10.2026 | да (с оговоркой «проверить версию на дату») |
| fact-bank: self-hosted n8n снижает накладные на медиа vs SaaS; маржа контент-производства до **35%** (контекст «зачем self-host + MCP») | [mayai.ru/n8n-ili-make-com...](https://mayai.ru/n8n-ili-make-com-chto-vybrat-dlya-kontent-zavoda-i-frilansa-v-2026-godu/) | 2026-06-11 | да (фон, не ядро статьи) |

**Не путать в тексте:**
- **Official** `https://<domain>/mcp-server/http` (instance-level) vs **уникальный path** MCP Server Trigger на webhook-домене.
- **`n8n-mcp`** (community npm, stdio, документация нод) vs **встроенный** MCP n8n.

---

## 4. Выбор режима (decision table для writer)

| Критерий | Instance-level MCP | MCP Server Trigger |
|----------|-------------------|-------------------|
| Цель в Cursor | Искать/запускать/собирать workflow в инстансе | Вызвать **фиксированный** набор tools (1–N нод) |
| URL | `/mcp-server/http` | Test/Production URL **из ноды Trigger** |
| Конфиг Cursor | OAuth one-click или `streamable-http` | Remote HTTP (+ Bearer); для stdio-only клиентов — proxy |
| Expose workflow | **Available in MCP** per workflow | Publish workflow + tool-ноды |
| Типичный B2B-кейс | «Собери в n8n воронку лидов из промпта» | «Дай Cursor один tool: создать лид в CRM» |

---

## 5. Черновики конфигов (для writer; плейсхолдеры не секреты)

**Instance-level + OAuth (предпочтительно):** n8n UI → Connect a client → Cursor → One-click → approve redirect.

**Instance-level + API key (фрагмент для `.cursor/mcp.json`):**

```json
{
  "mcpServers": {
    "n8n": {
      "type": "streamable-http",
      "url": "https://<your-n8n-domain>/mcp-server/http",
      "headers": {
        "Authorization": "Bearer <YOUR_N8N_MCP_TOKEN>"
      }
    }
  }
}
```

Источник формата Bearer для HTTP MCP: примеры Claude Code в [mcp-client-examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples); для Cursor в той же странице — блок без headers (OAuth), headers добавлять при API key.

**MCP Server Trigger в Cursor:** отдельная запись `mcpServers` с **production URL** из панели ноды + `headers` при Bearer auth; **не** подставлять `/mcp-server/http`.

---

## 6. FAQ-кандидаты (из карточки + docs)

1. **Чем MCP Server Trigger отличается от instance-level MCP?** — один workflow/tools vs весь инстанс + центральный `/mcp-server/http`.  
2. **Какой URL давать Cursor: test или production?** — для Cursor в проде: **production** URL Trigger; instance-level всегда `/mcp-server/http`.  
3. **Можно ли self-hosted n8n?** — да, если домен доступен Cursor (HTTPS или local http по docs); проверить proxy headers.  
4. **Почему 401?** — неверный/просроченный Bearer, MCP disabled, или auth на Trigger не совпадает с headers.  
5. **Почему пустой список tools?** — workflow не **Available in MCP** / не publish Trigger / в Cursor отключены tools / лимит enabled tools.  
6. **Claude Desktop vs Cursor?** — Claude часто через `supergateway`/`mcp-remote`; Cursor — native `streamable-http` или one-click.  
7. **Нужен ли community пакет `n8n-mcp`?** — нет для официального сценария; опционально для doc-only stdio.

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение двух режимов n8n MCP | Lead | 50–70 слов |
| Decision table | H2-1 | Таблица instance vs Trigger |
| Workflow A: instance-level | H2-3 | Нумерованные шаги enable → expose → Cursor |
| Workflow B: Trigger + Call Workflow Tool | H2-2 | Схема trigger → tool → sub-workflow |
| Пример mcp.json | H2-4 | JSON + пояснение полей |
| Troubleshooting | H2-6 | 401, proxy, queue mode, tools limit |
| FAQ | Конец | Ответы-действия |
| Internal links | В тексте | B03, B02 |

**Целевые формулировки:** «n8n mcp server», «n8n mcp cursor», «mcp server trigger n8n», «подключить n8n к cursor mcp».

---

## 8. Риски для writer

- Не выдумывать версии n8n/Cursor — опираться на 2.33.0 / 2.13.0 / 2.36.0 из docs и «проверьте на дату статьи».  
- Не подменять how-to обзором «что такое MCP».  
- Min **5** нумерованных шагов + чеклист **10+** (utility gate статьи).  
- Без эмодзи; дефис вместо длинного тире; прямые кавычки (site-brief).  
- CTA ≤ 3; не печатать реальные токены/API keys.  
- Объём по quality-blog; не копировать PerLod 1:1.

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель выберет instance-level MCP или MCP Server Trigger под задачу, включит доступ в n8n, подключит Cursor через one-click OAuth или `.cursor/mcp.json` (`streamable-http` + при необходимости Bearer), отметит нужные workflow как Available in MCP или опубликует Trigger-workflow с production URL, проверит tools в Cursor и устранит типичные ошибки (401, proxy, пустой список tools, лимит enabled tools).

**action_outline (для writer):**

1. **Сверить версию n8n** (рекомендация ≥2.18.4 для MCP; UI Connect a client — 2.33.0+) и доступность инстанса из сети, где работает Cursor.  
2. **Выбрать режим:** instance-level (управление/запуск workflow из IDE) **или** MCP Server Trigger (узкий набор tools) — таблица раздела 4.  
3. **Instance-level:** Settings → Instance-level MCP → **Enable MCP access** (admin); Connect a client → Cursor → **One-click** **или** скопировать Server URL + API key/OAuth.  
4. **Expose workflow:** для каждого сценария — **Available in MCP** / Workflows enabled; добавить **description** для поиска агентом.  
5. **Cursor:** `.cursor/mcp.json` или `~/.cursor/mcp.json` с `"type": "streamable-http"` и URL `https://<domain>/mcp-server/http`; при API key — `Authorization: Bearer`; перезапуск Cursor / проверка Customize.  
6. **Trigger-path (если выбран):** новый workflow → **MCP Server Trigger** → tool-ноды (в т.ч. **Call n8n Workflow Tool** с sub-workflow на **Execute Workflow Trigger**) → **Publish** → в Cursor добавить **production URL** (+ Bearer при auth).  
7. **Проверка:** в Agent запрос, который вызывает `search_workflows` / конкретный exposed workflow или tool Trigger; смотреть Executions в n8n.  
8. **Ограничить шум tools:** в Cursor отключить лишние MCP tools (community signal ~40 warning); не включать community `n8n-mcp` одновременно без нужды.  
9. **Troubleshooting:** 401 (token/MCP off), insufficient permissions (MCP disabled), пустые tools (expose/publish), reverse proxy (заголовки MCP 2.36+), queue mode (`/mcp*` на одну replica).

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS (preflight) |
| SERP ≥ 3 конкурента | ✅ (8; WebSearch) |
| Wordstat MCP | ⚠️ недоступен |
| Таблица фактов с URL | ✅ (24 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + internal B03/B02.
