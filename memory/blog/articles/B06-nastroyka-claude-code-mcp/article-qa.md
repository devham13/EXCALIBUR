# QA: B06 nastroyka-claude-code-mcp

date: 2026-07-07
score_total: 92/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | 7 H2, primary «claude code», FAQ 7, LSI hooks/mcp/windows — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 2 таблицы, FAQ 7, workflow blockquote, ol×17 |
| CORE-EEAT lite | 15 | 14 | 18/20 (см. ниже); −1 за Wordstat без MCP в Cloud |
| Human voice | 15 | 14 | 0 AI-slop hits; slop WARNING: 6 длинных предложений (таблицы/ol) |
| Fact safety | 15 | 13 | fact-check PASS; 3/4 числа не в fact-bank (30–45 мин, Win 1809, MCP 2024 — из docs/research) |
| Contract HTML | 10 | 8 | linter PASS после fix, объём 8648 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «claude code» + MCP/hooks |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: автоматизаторы контента без dev-бэкграунда |
| C04 | ✓ | MCP, stdio, OAuth, hooks — «на пальцах» |
| O01 | ✓ | H2 = каркас research (7 секций + FAQ) |
| O02 | ✓ | Outline: choose → install → auth → CLAUDE.md → MCP → hooks → pipeline |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (5+12), 2 table, 3 blockquote (команды в blockquote) |
| R01 | ✓ | TL;DR + workflow + Fact Check blockquote |
| R02 | ✓ | Команды install/MCP/hooks — с code.claude.com/docs/ru |
| R03 | ✓ | Тарифы Pro/Max с контекстом; дата проверки 07.07.2026 |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Ковчег: CLI vs Cursor, Make/n8n webhook, без dev-сленга |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, author ×1 (Fact Check) |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: регион, free plan, секреты в .mcp.json |
| Ept02 | ✗ | Wordstat LSI не снят (MCP user-mcp-kv недоступен в Cloud) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: mayai.ru/podklyuchenie-mcp-cursor/, mayai.ru/avtomatizaciya-n8n-ai-agents/, code.claude.com/docs/ru/setup, code.claude.com/docs/ru/quickstart, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (таблицы/checklist — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (4 extracted, 1 verified in fact-bank, 3 unverified — duration/OS/MCP date из official docs, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` ×3 → `<blockquote>` (html-linter whitelist)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- повторить Wordstat через MCP при доступности user-mcp-kv
- занести тарифы Anthropic и длительность setup в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
