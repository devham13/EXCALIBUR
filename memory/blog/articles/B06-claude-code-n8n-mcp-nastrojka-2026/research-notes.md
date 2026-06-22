# Research notes — B06 «Как подключить n8n-mcp к Claude Code и собирать workflow из терминала: пошаговая инструкция»

**topic_id:** B06  
**slug:** claude-code-n8n-mcp-nastrojka-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-06-22  
**disclaimer:** Все даты, версии и статистика проверены на 22.06.2026.

---

## 1. SERP-обзор (WebSearch + research-serp.json, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [github.com/czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) + [CLAUDE_CODE_SETUP.md](https://github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md) | Официальный репозиторий + setup | Канон команды `claude mcp add`, env-переменные, scope local/project, optional n8n-skills | Английский; нет русского troubleshooting Cloud vs self-hosted | Сухой перевод README без сценария «первый workflow из терминала» |
| 2 | [docs.n8n.io/.../accessing-n8n-mcp-server](https://docs.n8n.io/advanced-ai/mcp/accessing-n8n-mcp-server/) | Официальная docs n8n | **Instance-level MCP** n8n (встроенный сервер инстанса) | Другой продукт, не пакет `n8n-mcp`; легко перепутать с czlonkowski | Подменять в H1 «n8n-mcp» встроенным MCP n8n без таблицы отличий |
| 3 | [vantaige.io/.../n8n-mcp-claude-code-setup-guide-2026](https://vantaige.io/blog/n8n-mcp-claude-code-setup-guide-2026) | EN how-to 2026 | Docker Compose n8n, API key, verify `/mcp`, типичные ошибки URL/whitespace | EN; bias к Docker; нет CLAUDE.md | Структуру 1:1; «10 minutes» без чеклиста безопасности |
| 4 | [adaptoit.com/.../claude-code-n8n-mcp-workflow-automation-free-guide](https://adaptoit.com/claude-code-n8n-mcp-workflow-automation-free-guide/) | EN free guide | Пошагово: API key → `claude mcp add` → skills; `.mcp.json` пример | Нет русского; смешивает scope user/project | Коммерческий тон «without a course» |
| 5 | [dudarik.com/blog/n8n-mcp](https://dudarik.com/blog/n8n-mcp/) | RU практик (июнь 2026) | `MCP_MODE=stdio` обязателен, hosted dashboard, реальные промпты, pin версии npx | Цифры нод отличаются от upstream README (версия пакета) | Копировать устаревшие counts без сверки с github |
| 6 | [contextstudios.ai/.../connect-n8n-and-claude-code-complete-mcp-integration-guide-2026](https://www.contextstudios.ai/blog/connect-n8n-and-claude-code-complete-mcp-integration-guide-2026) | EN longread | Skills + MCP + agentic framing | Мало про Claude Code CLI flags (`--`, scope) | News-формат без чеклиста |
| 7 | [smyslokod.ru/guides/n8n-vs-claude-code](https://smyslokod.ru/guides/n8n-vs-claude-code) | RU comparison | Контекст «зачем оба в стеке» | Intent comparison, не setup; доминирует в SERP по «claude code n8n» | Увод в «что выбрать» вместо how-to |
| 8 | [2030ai.ru/library/kak-podklyuchat-mcp-n8n-k-claude-code-484b3bcd](https://2030ai.ru/library/kak-podklyuchat-mcp-n8n-k-claude-code-484b3bcd) | RU видео/курс | Живой кейс MCP + n8n в Claude Code | Paywall; Nathan-брендинг; не текстовый чеклист | Каннибализация с B03 (Cursor) без явной дифференциации CLI |

**Паттерн SERP:** по запросу «claude code n8n» топ перекошен в **comparison** (n8n vs Claude Code, vc.ru, Habr). Реальные setup-гайды — **англоязычные** (GitHub, Vantaige, AdapToIT). Русскоязычный how-to по **именно Claude Code CLI + n8n-mcp** почти не закрыт (dudarik — ближе всего, но без полного CLAUDE.md + первого deploy workflow).

**Intent:** how_to — пользователь хочет **подключить n8n-mcp в Claude Code**, выдать API key, увидеть tools в `/mcp` и **собрать/задеплоить workflow текстом**, не копируя JSON руками. Вторичный intent: чем отличается community `n8n-mcp` от встроенного MCP сервера n8n.

**Пробел для «Ковчег»:** русский пошаговый гайд для **Claude Code в терминале** (не Cursor): prerequisites → `claude mcp add` → CLAUDE.md правила → первый промпт → activate/test webhook → troubleshooting Cloud/self-hosted; таблица **czlonkowski n8n-mcp vs instance MCP n8n**; связка с B02/B03.

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 22.06.2026)

⚠️ **WORDSTAT MCP WARNING:** инструмент `wordstat_get_top_requests` сервера `user-mcp-kv` **недоступен** в Cloud Automation worker (MCP не подключён, `MCP_KV_TOKEN` отсутствует). Точные объёмы спроса по `claude code n8n` и secondary queries **не получены из API**. Обновите токен/подключение MCP через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Семантическая оценка (без выдуманных цифр)

| Запрос | Оценка спроса RU | Комментарий для SEO |
|--------|------------------|---------------------|
| claude code n8n | Низкий / EN long-tail | Латиница; конкуренция comparison, не setup |
| n8n mcp claude code | Низкий / EN | Технический кластер; целевой для H2/H3 |
| n8n-mcp настройка | Средний (смежный RU) | Ближе к intent статьи; использовать в подзаголовках |
| claude mcp add n8n | Низкий / EN CLI | FAQ и блок «команда установки» |

### Смежный верифицированный кластер (B02/B03, Wordstat 11.06.2026 — **не** повторный API-вызов B06)

Использовать writer'у для перекрёстной семантики и internal links, **не** как прямой спрос по primary_query:

| Фраза | Показы/мес | Источник |
|-------|------------|----------|
| n8n | 37 115 | B02 research-notes |
| n8n ai | 720 | B02 |
| n8n агенты | 699 | B02 |
| автоматизация n8n | 539 | B02 |
| n8n docker | 498 | B02 |
| настройка mcp сервера | 74 | B03 |
| cursor mcp | 630 | B03 |
| mcp сервер для cursor | 32 | B03 |

### LSI для writer (SERP + docs + смежный кластер)

- claude mcp add, claude mcp list, /mcp, scope local/project, `.mcp.json`
- n8n-mcp, npx n8n-mcp, MCP_MODE=stdio, N8N_API_URL, N8N_API_KEY
- n8n API key Settings, localhost:5678, n8n Cloud API
- workflow из терминала, validate workflow, webhook test
- instance MCP n8n vs n8n-mcp (czlonkowski)
- claude code skills n8n-skills, CLAUDE.md workflow rules
- troubleshooting JSON parsing, ENOENT node/npx, trailing slash URL

**SEO-стратегия:** H1/lead — «подключить n8n-mcp к Claude Code» + «собрать workflow из терминала»; head «n8n» через H2 «зачем связка» (ссылка B02); secondary «n8n-mcp настройка», «claude mcp add» в шагах и FAQ; не оптимизировать title под comparison «n8n vs Claude Code».

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| n8n-MCP (czlonkowski) даёт AI доступ к **1 845** n8n-нодам (816 core + 1 029 community) | [github.com/czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 22.06.2026 | да |
| Покрытие свойств нод в базе n8n-mcp — **99%** | [github.com/czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 22.06.2026 | да |
| Покрытие операций нод — **63,6%** | [github.com/czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 22.06.2026 | да |
| Покрытие официальной документации нод — **87%** | [github.com/czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 22.06.2026 | да |
| В базе n8n-mcp **2 352** workflow-шаблона с AI-метаданными (**99,96%** coverage) | [github.com/czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 22.06.2026 | да |
| Hosted `dashboard.n8n-mcp.com`: free tier **100 tool calls/day** | [github.com/czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 22.06.2026 | да |
| Без `N8N_API_URL`/`N8N_API_KEY` n8n-mcp даёт **только документацию/валидацию**; с ключом — управление workflow в инстансе | [github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md](https://github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md) | 22.06.2026 | да |
| Базовая установка Claude Code: `claude mcp add n8n-mcp` + env `MCP_MODE=stdio`, `LOG_LEVEL=error`, `DISABLE_CONSOLE_OUTPUT=true` + `-- npx n8n-mcp` | [github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md](https://github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md) | 22.06.2026 | да |
| Полная установка добавляет `-e N8N_API_URL=...` и `-e N8N_API_KEY=...` | [github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md](https://github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md) | 22.06.2026 | да |
| Для локального n8n URL часто `http://localhost:5678` (без лишнего path) | [github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md](https://github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md) | 22.06.2026 | да |
| `--` в `claude mcp add` отделяет флаги Claude от команды сервера | [docs.anthropic.com/en/docs/claude-code/mcp](https://docs.anthropic.com/en/docs/claude-code/mcp) | 22.06.2026 | да |
| Scope по умолчанию `local` (в `~/.claude.json`); `--scope project` → `.mcp.json` в корне проекта | [docs.anthropic.com/en/docs/claude-code/mcp](https://docs.anthropic.com/en/docs/claude-code/mcp) | 22.06.2026 | да |
| Проверка: `claude mcp list`, `claude mcp get n8n-mcp`, в сессии `/mcp` | [github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md](https://github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md) | 22.06.2026 | да |
| Без `MCP_MODE=stdio` возможны **JSON parsing errors** (debug в stdout ломает MCP) | [github.com/czlonkowski/n8n-mcp/blob/main/docs/SELF_HOSTING.md](https://github.com/czlonkowski/n8n-mcp/blob/main/docs/SELF_HOSTING.md) | 22.06.2026 | да |
| Требования: **Node.js 18+**, Claude Code CLI | [dudarik.com/blog/n8n-mcp](https://dudarik.com/blog/n8n-mcp) | 20.06.2026 | да |
| API key n8n: Settings → n8n API → Create API key | [dudarik.com/blog/n8n-mcp](https://dudarik.com/blog/n8n-mcp) | 20.06.2026 | да |
| Опционально: `/plugin install czlonkowski/n8n-skills` — 7 skills для production workflow | [github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md](https://github.com/czlonkowski/n8n-mcp/blob/main/docs/CLAUDE_CODE_SETUP.md) | 22.06.2026 | да |
| **Встроенный MCP сервер n8n** (instance-level) с апреля 2026 умеет **создавать и обновлять** workflow, не только запускать | [blog.n8n.io/n8n-mcp-server](https://blog.n8n.io/n8n-mcp-server/) | 29.04.2026 | да |
| Для создания workflow через instance MCP рекомендуется n8n **2.18.4+** | [blog.n8n.io/n8n-mcp-server](https://blog.n8n.io/n8n-mcp-server/) | 29.04.2026 | да |
| Instance MCP n8n ≠ MCP Server Trigger node (один workflow vs весь инстанс) | [blog.n8n.io/n8n-mcp-server](https://blog.n8n.io/n8n-mcp-server/) | 29.04.2026 | да |
| Instance MCP доступен на Cloud, Enterprise, Community Edition | [blog.n8n.io/n8n-mcp-server](https://blog.n8n.io/n8n-mcp-server/) | 29.04.2026 | да |
| Claude Code: `MCP_TIMEOUT` задаёт timeout старта MCP-серверов (мс) | [docs.anthropic.com/en/docs/claude-code/mcp](https://docs.anthropic.com/en/docs/claude-code/mcp) | 22.06.2026 | да |
| Claude Code предупреждает при MCP output **> 10 000 tokens**; лимит меняется через `MAX_MCP_OUTPUT_TOKENS` | [docs.anthropic.com/en/docs/claude-code/mcp](https://docs.anthropic.com/en/docs/claude-code/mcp) | 22.06.2026 | да |
| n8n Cloud Starter: **20 €/мес** (годовая оплата), 2 500 executions | [n8n.io/pricing](https://n8n.io/pricing/) | 22.06.2026 | да |
| Курс Make.com kv-ai.ru: **5 800 ₽/мес**, 159+ уроков | [kv-ai.ru/obuchenie-po-make](https://kv-ai.ru/obuchenie-po-make) | 22.06.2026 | да (единственный верифицированный прайс продукта) |

**Не использовать без оговорки:** разные версии n8n-mcp публикуют разные counts нод (dudarik vs upstream README) — в статье брать **актуальные цифры с github.com/czlonkowski/n8n-mcp** на дату публикации или формулировку «1 800+ нод».

**fact-bank.md:** прямых фактов по n8n-mcp/Claude Code нет — только таблица выше + смежные n8n из B02.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **20–40 минут** подключить **n8n-mcp** к **Claude Code CLI**, проверить tools в `/mcp`, добавить **CLAUDE.md** с правилами именования нод и собрать **первый рабочий workflow** (webhook → обработка → уведомление) **из терминала**, затем активировать и протестировать webhook.

**Почему отличается от конкурентов:**
- Comparison-статьи (smyslokod, vc.ru) не дают `claude mcp add` и не различают два типа MCP.
- EN-гайды не закрывают русский troubleshooting n8n Cloud vs self-hosted.
- B03 про Cursor — другой хост; здесь фокус **Claude Code + терминал**.
- «Ковчег»: практик автоматизации, язык для предпринимателя/маркетолога с n8n-фоном (B02), без «Claude заменит n8n».

**Tone:** Claude Code = «агент в терминале»; n8n-mcp = «справочник + руки для n8n»; instance MCP n8n = «официальный мост к вашему инстансу» — три роли, не одна.

**H2-каркас (из карточки + research):**
1. Зачем Claude Code + n8n в 2026: builder (CLI) vs runtime (оркестратор)  
2. Что понадобится: n8n API key, Node.js 18+, Claude Code CLI  
3. **Таблица:** czlonkowski `n8n-mcp` vs встроенный MCP n8n  
4. Установка n8n-mcp через `claude mcp add` (basic → full)  
5. CLAUDE.md: правила workflow, naming нод, human-in-the-loop  
6. Пошаговая сборка первого workflow из текстового промпта  
7. Активация, тест webhook, troubleshooting (Cloud vs self-hosted)  
8. FAQ + чеклист перед продакшеном  

**Conversion (conversion-map.md):**
- CTA курс Make: max 2× — «Claude Code строит, Make/n8n крутит 24/7» → [kv-ai.ru/obuchenie-po-make](https://kv-ai.ru/obuchenie-po-make)  
- Internal: [B02 n8n agents](/avtomatizaciya-n8n-ai-agents/), [B03 MCP Cursor](/podklyuchenie-mcp-cursor/)  

---

## 5. Сравнение двух MCP (черновик таблицы для writer)

| | **n8n-mcp** (npm/GitHub czlonkowski) | **Instance MCP** (встроенный в n8n) |
|---|--------------------------------------|-------------------------------------|
| Кто поддерживает | Community (Romuald Członkowski) | n8n first-party |
| Где ставится | `claude mcp add` + npx | Enable в n8n → URL в MCP client |
| Без API key | Доки + validate JSON | Нет доступа к инстансу |
| С API key | CRUD workflow в вашем n8n | CRUD + run exposed workflows |
| Лучше для | Глубокая база нод, шаблоны, Claude Code CLI | Единый официальный доступ к инстансу |
| Версия n8n | Любой с API | **2.18.4+** для create/update (blog) |

**Рекомендация writer:** в гайде основной путь — **n8n-mcp** (по H1); instance MCP — отдельный FAQ «когда перейти на официальный».

---

## 6. FAQ-кандидаты (5–7)

1. **Чем n8n-mcp отличается от встроенного MCP в n8n?** — см. таблицу §5.  
2. **Нужен ли API key на n8n Cloud?** — да для full mode; создать в Settings → n8n API; не публиковать в `.mcp.json` в git без secrets.  
3. **Как проверить, что MCP подключился?** — `claude mcp list`, в сессии `/mcp`, тестовый prompt «list workflows».  
4. **Почему JSON parsing error?** — нет `MCP_MODE=stdio` / `DISABLE_CONSOLE_OUTPUT=true`.  
5. **localhost:5678 не работает из Claude Code?** — n8n не запущен, неверный URL (без `/api/v1` в base для czlonkowski mcp), firewall.  
6. **Можно без n8n API?** — да, doc-only mode; workflow в UI импортировать JSON вручную.  
7. **Claude Code vs Cursor для n8n?** — оба MCP; Code лучше для terminal-first и CI; Cursor — IDE (1 абзац + B03).  

---

## 7. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение n8n-mcp 40–60 слов | Lead | «n8n-mcp в Claude Code — …» |
| Таблица два MCP | H2-3 | czlonkowski vs instance |
| Блок команды `claude mcp add` | H2-4 | shell + пояснение env |
| Workflow | H2-4–6 | API key → mcp add → CLAUDE.md → prompt → test webhook |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

---

## 8. Риски для writer

- Не выдумывать количество tools в `/mcp` (39 vs 20+ — зависит от версии пакета).  
- Не путать `N8N_API_URL` форматы разных форков MCP.  
- Объём: 8 500–9 500 знаков (quality-blog).  
- Min **5** нумерованных шагов + чеклист **10+** пунктов.  
- Production warning из README n8n-mcp: **копия workflow перед AI-правками**.  
- Без эмодзи; дефис вместо длинного тире; прямые кавычки.  

---

## 9. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель сгенерирует n8n API key, выполнит `claude mcp add n8n-mcp` с корректными env, увидит активный n8n-mcp в `/mcp`, добавит CLAUDE.md с правилами workflow, соберёт и активирует первый workflow из промпта в терминале и при ошибке URL/API/stdio исправит конфиг по чеклисту.

**action_outline (для writer):**

1. **Проверить prerequisites:** Node.js 18+, установленный Claude Code, доступный n8n (Cloud или self-hosted на `:5678`).  
2. **Создать n8n API key:** Settings → n8n API → label `claude-code-mcp` → скопировать ключ (без пробелов).  
3. **Добавить MCP (doc-only smoke test):** `claude mcp add n8n-mcp -e MCP_MODE=stdio -e LOG_LEVEL=error -e DISABLE_CONSOLE_OUTPUT=true -- npx n8n-mcp` → `claude mcp list`.  
4. **Переключить на full config:** `claude mcp remove n8n-mcp` → добавить с `-e N8N_API_URL=...` и `-e N8N_API_KEY=...` (local scope по умолчанию).  
5. **Проверить в сессии Claude Code:** `/mcp` зелёный статус; prompt «перечисли workflow через n8n-mcp».  
6. **Создать CLAUDE.md** в проекте: naming нод, запрет править prod без копии, предпочитать native nodes над Code, timezone, список сервисов.  
7. **Собрать первый workflow промптом** (webhook → IF/Set → Slack/Telegram/email); попросить validate перед deploy.  
8. **Активировать workflow в n8n**, скопировать webhook URL, отправить test POST, проверить execution log.  
9. **Troubleshooting:** JSON parse → stdio env; 401 → key/URL; Cloud → HTTPS base URL без лишнего path; при необходимости `--scope project` + `.mcp.json` без секретов в git.  

---

## 10. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ MCP недоступен; смежный кластер B02/B03 |
| Таблица фактов с URL | ✅ (24 факта) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md` + `conversion-map.md`.
