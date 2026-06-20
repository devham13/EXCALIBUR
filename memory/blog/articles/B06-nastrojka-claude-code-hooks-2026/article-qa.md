# QA: B06 nastrojka-claude-code-hooks-2026

date: 2026-06-20
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «claude code», FAQ 7, 8 секций + чек-лист 15 пунктов — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица scope settings, FAQ 7, 30 numbered steps, 6 blockquote |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за MCP href на mayai.ru (статья опубликована там, не на PUBLIC_SITE_URL) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, технический how-to без воды |
| Fact safety | 15 | 13 | fact-check PASS; 2/6 чисел в fact-bank (45–60 мин, 2026); v2.1.181, #18960, 600 с — из docs/issue |
| Contract HTML | 10 | 8 | linter PASS, объём ~8600 ✓, CTA ≤3 ✓, internal href ×5; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «claude code» / hooks / settings.json |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: техлиды и автоматизаторы, первый prod-сетап |
| C04 | ✓ | MCP, hooks, permissions, scope — «на пальцах» + метафора охранник/договор |
| O01 | ✓ | H2 совпадают с action_outline B06 (8 секций + FAQ) |
| O02 | ✓ | Outline: install → settings → CLAUDE.md → hooks → permissions → verify → checklist |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (5+6+15+4 шагов), 1 table, blockquote workflow |
| R01 | ✓ | TL;DR + workflow blockquote + Fact Check blockquote |
| R02 | ✓ | Иерархия scope, exit 2, --safe-mode — с research-notes / code.claude.com |
| R03 | ✓ | Цена Pro «от $17/мес» с оговоркой «на дату публикации»; Wordstat не утверждали |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Ковчег: settings + CLAUDE.md + hooks + permissions в одном workflow |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, internal B03/B02 ×5, author blockquote ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: регион, auto-mode, CLAUDE.md не enforcement |
| Ept02 | ✗ | MCP internal link — absolute mayai.ru (B03 live там); n8n — relative на PUBLIC_SITE_URL |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 9, failed: 0
- OK: claude.com/product/claude-code, mayai.ru/podklyuchenie-mcp-cursor/ (×3), avtomatizaciya-n8n-ai-agents/ (×2 relative), code.claude.com/docs (×3), github issue #18960, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- fix applied (cycle 1):
  - `<pre><code>` ×3 → `<blockquote>` (html-linter forbidden tags)
  - `/podklyuchenie-mcp-cursor/` → `https://mayai.ru/podklyuchenie-mcp-cursor/` (404 на PUBLIC_SITE_URL; B03 опубликован на mayai.ru)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (JSON blockquote + чек-лист — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 2 verified in fact-bank, 4 unverified — v2.1.181, #18960, 200 строк, 600 с из docs/issue, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` → blockquote (html-linter); MCP relative 404 → absolute mayai.ru (link-verify)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- после publish B06 на mayai.ru — унифицировать internal links (relative vs absolute)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
