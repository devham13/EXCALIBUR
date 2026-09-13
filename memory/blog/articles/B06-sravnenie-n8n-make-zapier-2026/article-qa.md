# QA: B06 sravnenie-n8n-make-zapier-2026

date: 2026-09-13
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2×8, primary query, FAQ 7, anchor ids — OK |
| GEO / citability | 25 | 24 | TL;DR, таблица 15 параметров, матрица 6 сценариев, эталонный workflow |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за 10 unverified stats в fact-bank |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0 |
| Fact safety | 15 | 13 | fact-check PASS; тарифы из research-notes, не blocker |
| Contract HTML | 10 | 8 | linter PASS, объём 9450 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «сравнение n8n make zapier» |
| C02 | ✓ | Lead — direct answer с пересчётом tasks/credits/executions |
| C03 | ✓ | Аудитория: выбор платформы для ИИ-автоматизации |
| C04 | ✓ | no-code, API, RAG, MCP — «на пальцах» в абзаце 2 |
| O01 | ✓ | H2 совпадают с research-каркасом (8 секций) |
| O02 | ✓ | Outline: пересчёт → n8n → Make → Zapier → таблица → матрица → чеклист |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (6 шагов), ul (12 checklist), 3 таблицы |
| R01 | ✓ | TL;DR + blockquote workflow, standalone блоки |
| R02 | ✓ | Тарифы n8n/Make/Zapier — с research-notes и Fact Check Box |
| R03 | ✓ | Цены с датой сверки 13.09.2026; LLM API с диапазоном |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: 15 параметров + 6 сценариев + единый TCO-калькулятор |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, internal n8n ×2 |
| Exp01 | ✓ | Режим B (comparison), editorial без fake case |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: task wall, dynamic AI credits, DevOps |
| Ept02 | ✓ | Internal links B02 (×2) — https://mayai.ru/avtomatizaciya-n8n-ai-agents/ |

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

- total: 2, failed: 0
- OK: mayai.ru/avtomatizaciya-n8n-ai-agents/ (×2), kv-ai.ru/obuchenie-po-make
- fix applied (cycle 1):
  - `/avtomatizaciya-n8n-ai-agents/` → `https://mayai.ru/avtomatizaciya-n8n-ai-agents/` (relative 404 на PUBLIC_SITE_URL; mayai.ru 200)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблицы/матрицы — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (15 extracted, 5 verified in fact-bank, 10 unverified — тарифы из research-notes, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json)

## Fix cycle

- cycle 1: GEO QA — relative internal links → absolute mayai.ru для link-verify PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести тарифы n8n/Make/Zapier в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
