# QA: B06 avtomatizaciya-obrabotki-dokumentov-ii

date: 2026-06-21
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, anchor id на H2 — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица n8n vs Make, 8 шагов + чеклист 13, JSON-schema blockquote |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 94.2, «Делайте / Не делайте» в каждой H2 |
| Fact safety | 15 | 13 | fact-check PASS; 3/5 чисел в fact-bank, 599 (Wordstat) и #2764 — из research-notes |
| Contract HTML | 10 | 8 | linter PASS, объём 8941 ✓, CTA ≤3 ✓, internal href ×1; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «автоматизация обработки документов» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: бухгалтерия/ops без штата разработчиков |
| C04 | ✓ | IDP, webhook, API, HITL — «на пальцах» |
| O01 | ✓ | H2 совпадают с research-каркасом (7 секций + FAQ) |
| O02 | ✓ | Outline: карта → стек → 8 шагов → schema → validation → чеклист → next steps |
| O03 | ✓ | FAQ 7 пар, queries из research (OCR vs LLM, HITL, n8n vs Make, ИНН, 152-ФЗ, KPI) |
| O04 | ✓ | ol (8+5 шагов), ul (13 checklist), table |
| R01 | ✓ | TL;DR + blockquote-схемы workflow, standalone FAQ |
| R02 | ✓ | Wordstat 599, VibeLab OCR 94–97%, 2,5% автономии — с research-notes |
| R03 | ✓ | Цифры с оговорками и датой «июнь 2026»; KPI ≥90% как критерий пилота |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: DIY scan→CRM на одном типе документа, не ЭДО-TOP-N |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, Telegram ×1, author ×2 (blockquote + next steps) |
| Exp01 | ✓ | Режим B, editorial без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: HITL, 152-ФЗ, hallucinations, confidence threshold |
| Ept02 | ✓ | Internal link `/avtomatizaciya-n8n-ai-agents/` — 200 на mayai.ru |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (topic) | PASS | utility-gate-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 4, failed: 0
- OK: mayai.ru/avtomatizaciya-n8n-ai-agents/ (internal), kv-ai.ru/obuchenie-po-make, t.me/maya_pro, kv-ai.ru/artur-horosheff

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/чеклист/blockquote — допустимо)
- Flesch RU: 94.2 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 3 verified in fact-bank, 2 unverified — Wordstat 599, n8n template #2764 из research)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- topic: PASS (`excalibur_blog_utility_gate.py --topic-id B06`)
- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- metrics: 7 H2, 7 FAQ h3, 1 table, 13 numbered list items, 21 action markers

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` JSON-schema → `<blockquote>` с `<br>` (html-linter whitelist)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести Wordstat-599 и n8n template #2764 в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
