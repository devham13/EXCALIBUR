# QA: B06 claude-code-n8n-mcp-nastrojka-2026

date: 2026-06-22
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «claude code n8n», FAQ 7, 11 секций — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 2 таблицы сравнения, FAQ 7, 4×ol + чеклист 12, workflow blockquote |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 14 | 0 AI-slop hits, Flesch RU 100.0; −1 slop WARNING (10 длинных предложений в таблицах/blockquote) |
| Fact safety | 15 | 13 | fact-check PASS; 3/12 чисел в fact-bank (GitHub stats, Wordstat, 5 800 ₽ — из research-notes) |
| Contract HTML | 10 | 8 | linter PASS, объём ~9400 ✓, CTA Make ×1 ✓, internal href ×3; −2 нет `<img>` с alt, код в blockquote (whitelist) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «claude code n8n» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: разработчики/автоматизаторы с Claude Code CLI |
| C04 | ✓ | MCP, n8n-mcp, API key, stdio — «на пальцах» в TL;DR и §1 |
| O01 | ✓ | H2 совпадают с research-каркасом (11 секций + FAQ) |
| O02 | ✓ | Outline: prerequisites → compare MCP → install → verify → CLAUDE.md → workflow → test → fix |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (5+5+5 шагов), ul (6+12 checklist), 2 table |
| R01 | ✓ | TL;DR + workflow-схема + Fact Check blockquote |
| R02 | ✓ | GitHub 1845/2352, Wordstat 37115/74/630 — с research-notes |
| R03 | ✓ | Цены с контекстом курса; n8n Cloud tier — с оговоркой free tier |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: RU how-to Claude Code CLI + n8n-mcp vs Instance MCP |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, author ×1, internal B02/B03 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: JSON parsing, 401, human-in-the-loop, MCP output tokens |
| Ept02 | ✓ | Internal links ×3: /podklyuchenie-mcp-cursor/, /avtomatizaciya-n8n-ai-agents/ |

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
- OK: /podklyuchenie-mcp-cursor/, /avtomatizaciya-n8n-ai-agents/ (×2), github.com/czlonkowski/n8n-mcp, blog.n8n.io/n8n-mcp-server/, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 10 (таблицы/blockquote/чеклист — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (12 extracted, 3 verified in fact-bank, 9 unverified — GitHub stats/Wordstat/тарифы из research, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` → `<blockquote>` (html-linter FAIL → PASS; whitelist контракт)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести GitHub stats n8n-mcp и Wordstat-цифры в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
