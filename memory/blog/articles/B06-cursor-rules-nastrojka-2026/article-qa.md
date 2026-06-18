# QA: B06 cursor-rules-nastrojka-2026

date: 2026-06-18
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2×7, primary query «cursor rules», FAQ×7, якоря id на H2 — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 2 таблицы, workflow blockquote, ol×3 (5+5+5), ul×1 (15 пунктов) |
| CORE-EEAT lite | 15 | 15 | 19/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, режим B без fake case |
| Fact safety | 15 | 13 | fact-check PASS; 2/6 чисел в fact-bank (2026, 500 строк); 4 из research-notes/контекста |
| Contract HTML | 10 | 7 | linter PASS, объём 9100 ✓, CTA ≤3 ✓, internal B03 ×3; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «cursor rules» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: автоматизаторы и контент-команда |
| C04 | ✓ | cursor rules, frontmatter, alwaysApply, globs — объяснены |
| O01 | ✓ | H2 совпадают с action_outline research (7 секций + FAQ) |
| O02 | ✓ | Outline: legacy → first rule → modes → stack → checklist → fix → next |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (5+5+5), ul (15 checklist), 2 table |
| R01 | ✓ | TL;DR + workflow + Fact Check blockquote |
| R02 | ✓ | 4 типа rules, 500 строк, minimatch — с research-notes / docs |
| R03 | ✓ | Нет неподтверждённых процентов/цен; Wordstat без цифр |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: стек general/n8n/content-seo, не «топ-100 rules» |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, author ×1, Maya AI ×1 |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Tab/Inline Edit, deprecated .cursorrules, Wordstat MCP |
| Ept02 | ✓ | Internal B03 ×3 по карточке темы |

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

- total: 4 unique URLs, failed: 0
- OK: cursor.com/docs/context/rules, mayai.ru/podklyuchenie-mcp-cursor/ (×3 relative), kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- site-base: https://mayai.ru

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (таблицы/blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 2 verified in fact-bank, 4 unverified — 30–45 мин, 150–200 слов, 2000 строк, «топ-100» из research/контекста, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` → blockquote «Пример 00-general.mdc» (html-linter FAIL → PASS)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести 30–45 мин и 150–200 слов в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
