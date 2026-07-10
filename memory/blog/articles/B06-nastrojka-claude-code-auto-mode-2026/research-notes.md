# Research notes — B06 «Как настроить Auto Mode в Claude Code: пошаговая инструкция для безопасной автоматизации в 2026 году»

**topic_id:** B06  
**slug:** nastrojka-claude-code-auto-mode-2026  
**article_mode:** B (how-to)  
**research_date:** 2026-07-10  
**disclaimer:** Все даты, версии и статистика проверены на 10.07.2026.

---

## 1. SERP-обзор (WebSearch, 8 конкурентов)

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [code.claude.com/docs/en/auto-mode-config](https://code.claude.com/docs/en/auto-mode-config) | Официальная docs (EN) | Канон: `autoMode.environment`, `allow` / `soft_deny` / `hard_deny`, `$defaults`, CLI `claude auto-mode *`, Bedrock/Vertex env | Английский; нет русского чеклиста для команды | Сухой перевод без сценария «безопасный unattended» |
| 2 | [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) | Официальная docs (EN) | Требования плана/модели, `Shift+Tab`, `defaultMode`, что блокирует классификатор, v2.1.142 project ignore | Мало примеров `settings.json` целиком | Копировать устаревший rollout «только Team» без сверки с актуальной docs |
| 3 | [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) | Engineering blog (25.03.2026) | 93% approve rate, двухстадийный классификатор, метрики FPR/FNR, threat model, deny-and-continue | Не how-to по настройке | Пересказ архитектуры вместо шагов включения |
| 4 | [claude.com/blog/auto-mode](https://claude.com/blog/auto-mode) | Product announcement (24.03.2026) | Зачем auto vs `--dangerously-skip-permissions`, research preview, admin disable | Устаревший scope «Team today»; нет `autoMode` JSON | News-формат без чеклиста |
| 5 | [developersdigest.tech/blog/claude-code-auto-mode-explained](https://www.developersdigest.tech/blog/claude-code-auto-mode-explained) | Практический EN-гайд | `Shift+Tab`, `defaultMode` только user-level, precedence hard/soft/allow | EN; смешивает managed vs user без таблицы scope | Структуру 1:1 |
| 6 | [datacamp.com/tutorial/claude-code-auto-mode-and-channels](https://www.datacamp.com/tutorial/claude-code-auto-mode-and-channels) | Tutorial EN | `claude auto-mode defaults/config`, что broad allow rules сбрасываются при входе в auto | Уклон в Channels; поверхностная безопасность | Коммерческий tutorial-tone |
| 7 | [smyslokod.ru/guides/11-sovetov-claude-code](https://smyslokod.ru/guides/11-sovetov-claude-code) | RU гайд 2026 | `Shift+Tab`, предупреждение про `--dangerously-skip-permissions` | Auto mode = «если включён», без настройки `autoMode` | Путать auto mode с acceptEdits или /goal |
| 8 | [vc.ru/ai/2892898-nastroiki-claude-code](https://vc.ru/ai/2892898-nastroiki-claude-code-kotorye-izmenyat-vashu-razrabotku) | RU permissions | Хороший `permissions.allow/deny`, hooks, sandbox | Нет блока auto mode / classifier config | Копировать deny-листы без связи с auto mode |

**Паттерн SERP:** топ — официальная документация Anthropic (auto-mode-config + permission-modes) и engineering post; EN-туториалы (DataCamp, Developers Digest, Medium) дают пошаговый JSON; русскоязычный SERP закрывает общие permissions и `/goal`, но **почти нет** отдельного RU how-to «настроить auto mode + `autoMode.environment` + проверка `claude auto-mode config`».

**Intent:** how_to — читатель хочет **включить** auto mode, **настроить** доверенную инфраструктуру и **безопасно** запустить длинную unattended-сессию без `--dangerously-skip-permissions`.

**Пробел для «Ковчег»:** пошаговый русский гайд «включение → `~/.claude/settings.json` → `autoMode.environment` → verify CLI → hooks/sandbox → чеклист команды 10+» с явным сравнением режимов и troubleshooting «auto недоступен / блокирует push / false positive».

---

## 2. Яндекс Wordstat (MCP user-mcp-kv, 10.07.2026)

⚠️ **WORDSTAT MCP WARNING:** MCP-сервер `user-mcp-kv` **не подключён** в текущем Cloud Agent run (доступны только `Cursor Automation Tools`, `cursor-cloud`). Вызов `wordstat_get_top_requests` выполнить невозможно. **Точные показы в месяц не получены** — цифры ниже не приводятся, чтобы не выдумывать спрос.

**Экспертная семантика (без объёмов, для writer):**

| Кластер | Пример фраз | Роль в статье |
|---------|-------------|---------------|
| Primary EN | claude code auto mode | H1, lead, slug |
| RU how-to | настройка auto mode claude code, claude code режим разрешений | H2/H3, FAQ |
| Config | claude auto-mode config, claude code permissions settings | Блок `settings.json` + CLI |
| Infra | autoMode environment, CLAUDE_CODE_ENABLE_AUTO_MODE | Bedrock/Vertex/Foundry |
| Safety | dangerously skip permissions, claude code sandbox hooks | Сравнение режимов, чеклист |
| Adjacent (не путать) | claude code plan mode, claude code /goal | 1 абзац «auto ≠ /goal» |

**LSI для writer (из SERP + secondary_queries):**

- permission mode, Shift+Tab, defaultMode auto, `--permission-mode auto`
- classifier, soft_deny, hard_deny, allow, `$defaults`
- `claude auto-mode defaults`, `claude auto-mode config`, `claude auto-mode critique`
- managed settings, disableAutoMode, Owner enablement Team/Enterprise
- hooks PermissionDenied, sandbox, classifyAllShell
- Pro / Team / Max / API, Sonnet 4.6+, Opus 4.6+

**SEO-стратегия:** primary «claude code auto mode» — в title/lead; RU secondary «настройка auto mode claude code», «claude code режим разрешений» — в H2; long-tail «CLAUDE_CODE_ENABLE_AUTO_MODE», «claude auto-mode config» — в troubleshooting и FAQ.

**Действие для пайплайна:** при следующем прогоне с подключённым `user-mcp-kv` повторить `wordstat_get_top_requests` для `claude code auto mode`, `настройка claude code`, `claude code настройка`, `claude code permissions`.

---

## 3. Таблица фактов (цифры только с URL)

| Факт | Источник | Дата | Можно в текст |
|------|----------|------|---------------|
| Auto mode анонсирован 24 марта 2026 как research preview permission mode | [claude.com/blog/auto-mode](https://claude.com/blog/auto-mode) | 24.03.2026 | да |
| Engineering post опубликован 25 марта 2026 | [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) | 25.03.2026 | да |
| Пользователи Claude Code одобряют **93%** permission prompts | [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) | 25.03.2026 | да |
| Auto mode требует Claude Code **v2.1.83 или новее** | [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) | 10.07.2026 | да |
| Auto mode доступен на **всех планах**; на Team/Enterprise Owner должен включить в admin settings | [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) | 10.07.2026 | да |
| На Anthropic API: модели **Opus 4.6+** или **Sonnet 4.6+**; на Bedrock/Vertex/Foundry: Sonnet 5, Opus 4.7, Opus 4.8 | [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) | 10.07.2026 | да |
| На Bedrock/Agent Platform/Foundry auto mode выключен, пока не задан `CLAUDE_CODE_ENABLE_AUTO_MODE=1` (v2.1.158+) | [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) | 10.07.2026 | да |
| Переключение режимов в CLI: **Shift+Tab** (default → acceptEdits → plan → auto при eligibility) | [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) | 10.07.2026 | да |
| Сессия в auto: `claude --permission-mode auto`; первый раз — opt-in при цикле Shift+Tab | [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) | 10.07.2026 | да |
| `defaultMode: "auto"` **игнорируется** в `.claude/settings.json` и `.claude/settings.local.json` с v2.1.142+; только `~/.claude/settings.json` или managed | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 10.07.2026 | да |
| `autoMode` **не читается** из shared `.claude/settings.json` — репозиторий не может inject allow rules | [code.claude.com/docs/en/auto-mode-config](https://code.claude.com/docs/en/auto-mode-config) | 10.07.2026 | да |
| Поля `autoMode`: `environment`, `allow`, `soft_deny`, `hard_deny` — prose rules; включать `"$defaults"` чтобы не заменить baseline | [code.claude.com/docs/en/auto-mode-config](https://code.claude.com/docs/en/auto-mode-config) | 10.07.2026 | да |
| Precedence: hard_deny → soft_deny → allow → explicit user intent (для soft) | [code.claude.com/docs/en/auto-mode-config](https://code.claude.com/docs/en/auto-mode-config) | 10.07.2026 | да |
| CLI: `claude auto-mode defaults`, `claude auto-mode config`, `claude auto-mode critique` | [code.claude.com/docs/en/auto-mode-config](https://code.claude.com/docs/en/auto-mode-config) | 10.07.2026 | да |
| `autoMode.classifyAllShell: true` — все shell-команды через классификатор (v2.1.193+) | [code.claude.com/docs/en/auto-mode-config](https://code.claude.com/docs/en/auto-mode-config) | 10.07.2026 | да |
| Админ может отключить: `permissions.disableAutoMode: "disable"` в managed settings | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 10.07.2026 | да |
| При входе в auto mode сбрасываются broad allow rules: `Bash(*)`, wildcard interpreters, blanket Agent allows | [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) | 25.03.2026 | да |
| In-project file writes/edits — **без** вызова классификатора (Tier 2) | [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) | 25.03.2026 | да |
| Stage 1 FPR **8.5%** на real traffic (n=10,000); pipeline Stage1→2 FPR **0.4%** | [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) | 25.03.2026 | да |
| FNR на real overeager actions **17%** (n=52) — «honest number» | [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) | 25.03.2026 | да |
| Классификатор reasoning-blind: видит user messages + tool calls, не assistant reasoning | [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) | 25.03.2026 | да |
| Deny-and-continue: **3** consecutive denials или **20** total → escalation к человеку | [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) | 25.03.2026 | да |
| Auto mode может увеличить token/cost/latency на tool calls | [claude.com/blog/auto-mode](https://claude.com/blog/auto-mode) | 24.03.2026 | да |
| Блокировки по умолчанию включают: `curl \| bash`, force push, prod deploys, mass cloud delete, IAM grants | [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) | 10.07.2026 | да |
| `permissions.deny` в managed settings — до классификатора, не override | [code.claude.com/docs/en/auto-mode-config](https://code.claude.com/docs/en/auto-mode-config) | 10.07.2026 | да |
| Denials смотреть в `/permissions` → Recently denied; v2.1.193+ — reason рядом с блокировкой | [code.claude.com/docs/en/auto-mode-config](https://code.claude.com/docs/en/auto-mode-config) | 10.07.2026 | да |
| Hook `PermissionDenied` — programmatic reaction на deny | [code.claude.com/docs/en/auto-mode-config](https://code.claude.com/docs/en/auto-mode-config) | 10.07.2026 | да |
| v2.1.200: alias `manual` для режима `default` в UI | [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) | 10.07.2026 | да |
| Auto mode ≠ `/goal`: auto убирает per-tool prompts в turn; `/goal` добавляет evaluator между turns | [smyslokod.ru/guides/goal-i-agent-view-v-claude-code](https://smyslokod.ru/guides/goal-i-agent-view-v-claude-code) | 2026 | да (community, сверять с docs) |

**Не использовать без оговорки:** blog post от 24.03 «Team only today» как актуальный scope — в docs на 07.2026 указаны все планы + API; в статье писать по permission-modes docs с датой проверки.

**fact-bank.md:** записей про Claude Code auto mode нет — все цифры только из таблицы выше.

---

## 4. Угол статьи (utility-only, режим B)

**Главный угол:** за **20–40 минут** включить auto mode легальным способом, прописать минимальный безопасный `autoMode.environment` для своей инфраструктуры, проверить effective config через CLI и пройти **чеклист команды** перед unattended-задачами — **без** `--dangerously-skip-permissions`.

**Почему отличается от конкурентов:**
- Официальная docs — канон, но размазана по permission-modes + auto-mode-config + settings.
- EN-туториалы не закрывают русский intent «настройка auto mode».
- RU-материалы путают auto mode с acceptEdits, plan или `/goal`.
- «Ковчег»: практик автоматизации, фокус на **безопасный workflow** (auto + hooks + sandbox + managed deny), не news про релиз марта.

**Tone:** auto mode = «автопилот с вторым пилотом-классификатором»; `$defaults` = «не выкидывай штатные правила Anthropic»; `hard_deny` = «красная линия без override».

**H2-каркас (из карточки + research):**
1. Auto Mode vs Manual vs `--dangerously-skip-permissions`: матрица выбора
2. Требования: план, модель, Owner на Team/Enterprise, env на Bedrock/Vertex
3. Включение: Shift+Tab, `--permission-mode auto`, `defaultMode` в `~/.claude/settings.json`
4. `autoMode.environment` + allow/soft_deny/hard_deny + `$defaults` + verify CLI
5. Hooks + sandbox + managed deny: четыре слоя перед unattended
6. Чеклист безопасного запуска (10+ пунктов) + FAQ troubleshooting

**Conversion (conversion-map.md):**
- CTA Make/kv-ai — max 2×, если уместно «Claude Code + Make-воронки»
- Internal: `/claude-code-hooks-nastrojka-2026/`, `/dinamicheskie-workflow-claude-code/`, `/nastroyka-claude-code-mcp/`

---

## 5. FAQ-кандидаты (5–7)

1. **Чем auto mode отличается от `--dangerously-skip-permissions`?** — Классификатор блокирует опасные tool calls; bypass отключает почти все проверки.
2. **Можно ли включить auto mode в `.claude/settings.json` проекта?** — Нет для `defaultMode: "auto"` (v2.1.142+) и `autoMode` в shared project settings.
3. **Почему auto mode не появляется в Shift+Tab?** — Проверить план/модель/Owner enablement/`CLAUDE_CODE_ENABLE_AUTO_MODE`/disableAutoMode.
4. **Как администратор Team отключает auto mode?** — `permissions.disableAutoMode: "disable"` в managed settings.
5. **Сколько стоит auto mode по токенам?** — Доп. latency/cost на classifier calls; точный % — не фиксировать без billing docs.
6. **Что делать при false positive (блокирует push в свой org)?** — Добавить org в `autoMode.environment`, `claude auto-mode config`, retry с explicit intent.
7. **Auto mode или /goal?** — Auto = per-tool; /goal = per-turn evaluator; complementary.

---

## 6. GEO hooks

| Hook | Где | Формат |
|------|-----|--------|
| Определение auto mode 40–60 слов | Lead | «Auto Mode в Claude Code — …» |
| Таблица режимов (manual / acceptEdits / plan / auto / bypass) | H2-1 | Когда какой + рекомендация |
| Пример `~/.claude/settings.json` | H2-3–4 | JSON: env + permissions.defaultMode + autoMode |
| Workflow | H2-3–5 | Eligibility → enable → environment → verify → test task → checklist |
| FAQ 5–7 | Конец | Ответы-действия |
| Schema | handoff schema | BlogPosting + FAQPage |

**Целевые формулировки:** «claude code auto mode», «настройка auto mode claude code», «claude code режим разрешений», «claude auto-mode config».

---

## 7. Риски для writer

- Не выдумывать показы Wordstat — MCP недоступен в этом run.
- Не писать «auto mode бесплатен/включён у всех Pro» без проверки admin settings на Team.
- Объём: 8 500–9 500 знаков (quality-blog).
- Min **5** нумерованных шагов + чеклист **10+** пунктов.
- Не подменять how-to пересказом engineering blog (93%, 17% FNR — 1–2 абзаца максимум).
- Упомянуть research preview + isolated environments — без fear-mongering.
- Без эмодзи; дефис вместо длинного тире.

---

## 8. Utility gate (research)

**utility_verdict:** PASS

**reader_outcome:** Читатель проверит eligibility auto mode, включит его через Shift+Tab или `--permission-mode auto`, настроит `autoMode.environment` и при необходимости `hard_deny` в `~/.claude/settings.json`, проверит effective rules через `claude auto-mode config`, дополнит защиту hooks/sandbox/managed deny и пройдёт чеклист перед unattended-сессией без `--dangerously-skip-permissions`.

**action_outline (для writer):**

1. **Обновить Claude Code** до v2.1.83+ (`claude --version`); на Bedrock/Vertex/Foundry добавить `CLAUDE_CODE_ENABLE_AUTO_MODE=1` в `env` user или managed settings.
2. **Проверить eligibility:** план, модель Sonnet 4.6+/Opus 4.6+ (или Sonnet 5/Opus 4.7+ на cloud providers); на Team/Enterprise — Owner включил auto mode; убедиться, что нет `disableAutoMode: "disable"`.
3. **Включить auto mode:** в сессии Shift+Tab до статуса `auto` (принять one-time opt-in) **или** `claude --permission-mode auto` для одной сессии.
4. **Задать default (опционально):** в `~/.claude/settings.json` добавить `"permissions": {"defaultMode": "auto"}` — **не** в project `.claude/settings.json`.
5. **Настроить classifier:** в том же user settings блок `autoMode.environment` с `"$defaults"` + trusted GitHub org, buckets, internal domains; при необходимости `hard_deny` для org-specific red lines.
6. **Verify:** выполнить `claude auto-mode defaults`, затем `claude auto-mode config`; при custom rules — `claude auto-mode critique`.
7. **Усилить защиту:** добавить managed/user `permissions.deny` для критичных паттернов; hooks на `PermissionDenied`; sandbox для экспериментов; опционально `classifyAllShell: true` если narrow allow rules слишком permissive.
8. **Тестовая unattended-задача** на безопасном репо (refactor + tests), мониторить `/permissions` → Recently denied; при повторных deny — расширить `environment` или explicit intent.
9. **Пройти чеклист команды** (10+ пунктов из карточки B06) перед prod/shared infra.

---

## 9. Готовность к writer

| Критерий | Статус |
|----------|--------|
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (8) |
| Wordstat MCP | ⚠️ сервер недоступен; LSI экспертно |
| Таблица фactов с URL | ✅ (26 фактов) |
| utility_verdict + action_outline | ✅ |
| FAQ 5–7 | ✅ |
| GEO hooks | ✅ |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B06 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B06
article_dir: memory/blog/articles/B06-nastrojka-claude-code-auto-mode-2026
status: ✅ PASS
utility_verdict: PASS
wordstat: ⚠️ MCP user-mcp-kv недоступен — показы не получены
summary: RU how-to auto mode + autoMode config + security checklist. 26 фактов, 9 action steps, 7 FAQ. Writer ready.
===
