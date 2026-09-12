# QA: B06 claude-code-routines-nastrojka-2026

date: 2026-08-16
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «claude code routines», FAQ 7 пар, 2 ol-блока (5+10), 2 таблицы — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, workflow blockquote, curl-пример, FAQ 7, 9 H2-секций |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, технический how-to тон |
| Fact safety | 15 | 13 | fact-check PASS; 2/6 чисел в fact-bank, остальные — API/docs (2023-06-01, 65536, HTTP 200) |
| Contract HTML | 10 | 7 | linter PASS, объём ~9k ✓, CTA ≤3 ✓, internal href ×2 (200); −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «claude code routines» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: разработчики/автоматизаторы, нужен cloud run без ноутбука |
| C04 | ✓ | Routine, hooks, /loop, API trigger — объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с action_outline research (9 секций + FAQ) |
| O02 | ✓ | Outline: сравнение → подготовка → создание → триггеры → чек-лист → 5 рутин → next steps |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (5 + 10 шагов), 2 table, blockquote workflow |
| R01 | ✓ | TL;DR + workflow blockquote + «Делайте/Не делайте» в каждой H2 |
| R02 | ✓ | Лимиты Pro 5/Max 15/Team 25, cron ≥1h, beta-header — из research-notes + docs |
| R03 | ✓ | Нет неподтверждённых процентов/цен |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: 30–45 мин, три триггера, production-чек-лист, 5 готовых рутин |
| E02 | ✓ | «Делайте/Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA Make ×2 (conversion-map) |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Research preview, cap, 429, auto-merge риски названы |
| Ept02 | ✓ | Internal links `/ustanovka-claude-code/`, `/claude-code-hooks-nastrojka-2026/` — 200 |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| utility gate (topic + article) | PASS | utility-gate-report.json |
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |

## Link verify

- total: 6, failed: 0
- OK: /ustanovka-claude-code/, /claude-code-hooks-nastrojka-2026/, github.com/apps/claude, code.claude.com/docs/en/routines, kv-ai.ru/obuchenie-po-make

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблицы/curl blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy — короткие предложения в how-to)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 2 verified in fact-bank, 4 unverified — API version/date/limit из официальной docs, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- topic B06: PASS (how_to, mode B)
- article: PASS (20 numbered items, 9 h2, 7 FAQ, 2 tables, 18 action markers)
- see `utility-gate-report.json`

## Fix cycle (1)

1. **html-linter FAIL:** заменены `<code>` и `<pre><code>` на `<b>` и `<blockquote>` с `<br>` (whitelist linter).
2. **link-verify FAIL:** href `https://claude.ai/code/routines` → `https://code.claude.com/docs/en/routines` (403 bot-block на claude.ai); anchor text сохранён.
3. Повторный прогон всех скриптов — **PASS**.

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести API-метрики (65536, anthropic-version) в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
