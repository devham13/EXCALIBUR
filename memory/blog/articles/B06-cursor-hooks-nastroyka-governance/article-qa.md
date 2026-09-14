# QA: B06 cursor-hooks-nastroyka-governance

date: 2026-08-26
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «как настроить cursor hooks», FAQ 7, 9 секций с id — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 2 таблицы, FAQ 7, 7+12 шагов, 5 code blockquote |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за author blockquote без href на профиль |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, editorial how-to |
| Fact safety | 14 | 13 | fact-check PASS; 1/2 чисел в fact-bank (30–45 мин — editorial estimate) |
| Contract HTML | 10 | 7 | linter PASS после fix; объём ~8513 ✓, CTA Make ×2 ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «как настроить cursor hooks» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: DevOps, тимлиды, автоматизаторы с Cloud Agents |
| C04 | ✓ | failClosed, deny, matcher, subagentStart — с контекстом |
| O01 | ✓ | H2 совпадают с каркасом B06 (9 секций + FAQ) |
| O02 | ✓ | Outline: compare → location → setup → block → audit → MCP matrix → cloud → checklist → next |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (7+12 шагов), 2 table, 8 blockquote |
| R01 | ✓ | TL;DR + workflow + Fact Check blockquote |
| R02 | ✓ | Cloud matrix, paths hooks.json — с research-notes / official docs |
| R03 | ✓ | Wordstat unavailable — честно указано в blockquote |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: repo-first governance для Cloud Agents, deny-only policy |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×2, internal B03 ×3 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: beforeMCPExecution не в cloud, allow/ask ненадёжны |
| Ept02 | ✗ | Author blockquote — plain text без href на kv-ai.ru/artur-horosheff |

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

- total: 2 unique URLs, failed: 0
- OK: /podklyuchenie-mcp-cursor/ (×3 relative), kv-ai.ru/obuchenie-po-make (×2)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (таблицы/blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (2 extracted, 1 verified in fact-bank, 1 unverified — «30–45 минут» editorial estimate)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` → `<blockquote>` (5 блоков кода, html-linter FAIL → PASS)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- href на профиль автора в blockquote «Материал проверен»
- занести «30–45 минут» в fact-bank при стандартизации editorial estimates

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
