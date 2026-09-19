# QA: B06 claude-code-hooks-nastrojka-2026

date: 2026-07-08
score_total: 92/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2×7, primary query «claude code hooks» в lead, FAQ 7, якоря id на H2 — OK |
| GEO / citability | 25 | 24 | TL;DR, workflow blockquote, 3 таблицы, FAQ 7, ol 7+3 шагов, ul 12 checklist |
| CORE-EEAT lite | 15 | 14 | 18/20 (см. ниже); −1 timeout 600 сек не в fact-bank (есть в research-notes) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, editorial «Делайте/Не делайте» |
| Fact safety | 15 | 14 | fact-check PASS; 1/3 чисел (600 сек) unverified — из official docs research, не blocker |
| Contract HTML | 10 | 9 | linter PASS после fix `<pre><code>`→blockquote; CTA Make ×2; −1 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/meta закрывают «claude code hooks» |
| C02 | ✓ | Lead — direct answer (20–40 мин, три hook, /hooks) |
| C03 | ✓ | Аудитория: разработчики/техлиды автоматизации |
| C04 | ✓ | Hooks, Pre/PostToolUse, MCP — «на пальцах» в §1 |
| O01 | ✓ | H2 совпадают с каркасом B06 (7 секций + FAQ) |
| O02 | ✓ | Outline: compare → scope → walkthrough → guards → optional → checklist → next |
| O03 | ✓ | FAQ 7 пар, queries из research §6 |
| O04 | ✓ | ol (7+3 шагов), ul (12 checklist), 3 table |
| R01 | ✓ | TL;DR + workflow + E-E-A-T blockquote + FAQ standalone |
| R02 | ✓ | 30 events, exit 2, /hooks — с code.claude.com/docs + дата 08.07.2026 |
| R03 | ✓ | Без выдуманного Wordstat; «20–40 мин» — экспертная оценка из research |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Ковчег: production pack hooks, exit 1 vs 2, CI -p |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×2, author ×1 — ≤ лимита conversion-map |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: exit 1 non-blocking, PermissionRequest в -p, allowManagedHooksOnly |
| Ept02 | ✓ | Internal link /podklyuchenie-mcp-cursor/ ×3 (B03) |

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
- OK: mayai.ru/podklyuchenie-mcp-cursor/ (×3 relative), code.claude.com/docs/en/hooks-guide, code.claude.com/docs/en/hooks, kv-ai.ru/obuchenie-po-make (×2), kv-ai.ru/artur-horosheff

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблицы/checklist — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (3 extracted, 2 verified in fact-bank, 1 unverified — timeout 600 сек из research-notes/docs, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (research phase, utility-gate-topic.json)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` ×3 → `<blockquote>` с `<br>` (html-linter FAIL → PASS)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести timeout defaults (600/30/60 сек) в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
