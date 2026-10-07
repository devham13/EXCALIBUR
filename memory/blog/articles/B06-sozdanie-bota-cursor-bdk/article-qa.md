# QA: B06 sozdanie-bota-cursor-bdk

date: 2026-10-07
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2×7, primary «cursor bdk», FAQ 7, якоря id на H2 |
| GEO / citability | 25 | 24 | TL;DR, таблица BDK/Automations/Grok, FAQ 7, 5+5 шагов, workflow blockquote |
| CORE-EEAT lite | 15 | 14 | 19/20; −1 за absolute mayai.ru вместо relative (QA fix link-verify) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0 |
| Fact safety | 15 | 14 | fact-check PASS; Wordstat не выдумывали (research MCP unavailable) |
| Contract HTML | 10 | 7 | linter PASS, объём ~9377 ✓, CTA Make ×1 ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/meta закрывают «cursor bdk» / bot development kit |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: команда с Git, нужен production-агент |
| C04 | ✓ | MCP, API, Tool — «на пальцах» |
| O01 | ✓ | H2 по каркасу B06 (7 секций + FAQ) |
| O02 | ✓ | compare → init → configure → evals → deploy → fix → next |
| O03 | ✓ | FAQ 7, queries из research |
| O04 | ✓ | ol (5+5), ul checklist 11, table |
| R01 | ✓ | TL;DR + workflow + Fact Check blockquote |
| R02 | ✓ | Node 22.13+, README/skills — в research-notes + blockquote |
| R03 | ✓ | Нет выдуманных Wordstat; pricing Teams не выдуман |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол «Ковчег»: RU how-to BDK vs Telegram SERP |
| E02 | ✓ | «Делайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA Make ×1, author kv-ai ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон research/brief |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Bun, secrets, pending deploy, eval credentials |
| Ept02 | ✗ | Internal B03 — absolute URL (relative + PUBLIC_SITE_URL давал 404 в QA) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| excalibur_blog_fact_checker.py | PASS | fact-check-report.json |
| excalibur_blog_link_verify.py | PASS | link-verify.json |
| excalibur_blog_html_linter.py | PASS | html-linter-report.json |
| excalibur_blog_slop_detector.py | PASS | slop-detector-report.json |
| excalibur_blog_cannibalization_guard.py | PASS | cannibalization-report.json |
| excalibur_blog_utility_gate.py | PASS | utility-gate-report.json |

## Link verify

- total: 4, failed: 0
- OK: mayai.ru/podklyuchenie-mcp-cursor/ (×3), cursor.com/docs/cloud-agent/automations, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- fix applied (cycle 1): relative `/podklyuchenie-mcp-cursor/` → `https://mayai.ru/podklyuchenie-mcp-cursor/` (PUBLIC_SITE_URL в Cloud не отдаёт slug блога)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/checklist — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (1 extracted, 1 verified)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` → `<blockquote>` (html-linter); internal MCP links → absolute mayai.ru (link-verify)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- при желании вернуть relative `/podklyuchenie-mcp-cursor/` после выравнивания PUBLIC_SITE_URL с prod

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
