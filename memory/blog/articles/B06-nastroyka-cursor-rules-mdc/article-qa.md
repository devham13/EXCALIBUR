# QA: B06 nastroyka-cursor-rules-mdc

date: 2026-09-10
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «cursor rules», FAQ 7, 8 секций — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 2 таблицы режимов, FAQ 7, 7+5 шагов, workflow blockquote |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, editorial second-person |
| Fact safety | 15 | 13 | fact-check PASS; 3/7 чисел в fact-bank (248, 5 мин, 40 747 — из research-notes) |
| Contract HTML | 10 | 7 | linter PASS после fix; объём 9460 ✓; CTA ≤3 ✓; internal href ×3; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «cursor rules» |
| C02 | ✓ | Lead — direct answer (Agent переписывает без rules), без «в этой статье» |
| C03 | ✓ | Аудитория: разработчики и автоматизаторы в Cursor Agent mode |
| C04 | ✓ | Agent mode, Tab, frontmatter, globs — «на пальцах» |
| O01 | ✓ | H2 совпадают с каркасом B06 (8 секций + FAQ) |
| O02 | ✓ | Outline: зачем → create → modes → modular → migration → fix → checklist → next |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (7+5 шагов), ul (3 чеклиста), 2 table |
| R01 | ✓ | TL;DR + workflow blockquote + Fact Check blockquote + примеры .mdc |
| R02 | ✓ | Wordstat 248/186, cursor.com/docs/rules, awesome-cursorrules stars — из research-notes |
| R03 | ✓ | Цифры с датой «июнь 2026» / «10.09.2026»; нет голых процентов |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: Agent mode + модульные .mdc + migration 5 min + link B03 MCP |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, author ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Tab/Cmd+K не читают rules, перегруз alwaysApply, silent YAML |
| Ept02 | ✓ | Internal link /podklyuchenie-mcp-cursor/ ×3 — link-verify 200 |

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

- total: 5, failed: 0
- OK: /podklyuchenie-mcp-cursor/ (×3 relative → 200), github.com/PatrickJS/awesome-cursorrules, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff, cursor.com/docs/rules

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблицы/blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 3 verified in fact-bank, 4 unverified — Wordstat/GitHub stars/5 min из research, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` → `<blockquote>` (2 примера .mdc; html-linter whitelist)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести Wordstat-248 и GitHub stars в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
