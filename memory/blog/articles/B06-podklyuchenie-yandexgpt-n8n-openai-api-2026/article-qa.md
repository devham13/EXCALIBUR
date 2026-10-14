# QA: B06 podklyuchenie-yandexgpt-n8n-openai-api-2026

date: 2026-10-14
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, якоря id — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 3 таблицы, FAQ 7, 3× ol + чеклист 12 |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 нет `<img>` с alt (cover после QA) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, editorial first-person |
| Fact safety | 15 | 13 | fact-check PASS; 2/6 в fact-bank; HTTP-коды 401/403/404 — контекст troubleshooting |
| Contract HTML | 10 | 6 | linter PASS, объём ~8182 ✓, CTA ≤3 ✓; −4 нет inline `<img>` |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «подключить yandexgpt к n8n» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: автоматизаторы без DevOps, РФ |
| C04 | ✓ | IAM, SA, Base URL, scope — «на пальцах» |
| O01 | ✓ | H2 совпадают с research-каркасом (6 секций + FAQ) |
| O02 | ✓ | Outline: checklist → credential → agent → business → compare → fix |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (6+6+5), checklist 12, 3 table |
| R01 | ✓ | TL;DR + workflow blockquote, standalone блоки |
| R02 | ✓ | Base URL, scopes, роли — с research-notes |
| R03 | ✓ | Wordstat не использовались (MCP недоступен на research) |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: OpenAI credential + AI Agent MVP 2026 |
| E02 | ✓ | «Делайте / Не делайте» в секциях |
| E03 | ✓ | CTA Make ×1, internal B02/B03 ×3 |
| Exp01 | ✓ | Режим B how-to, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: billing, ПДн, красный Test credential |
| Ept02 | ✗ | Нет `<img>` с alt до cover-агента |

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

- total: 3, failed: 0
- OK: mayai.ru/avtomatizaciya-n8n-ai-agents/ (×2 relative), mayai.ru/podklyuchenie-mcp-cursor/, kv-ai.ru/obuchenie-po-make
- **Примечание:** `--site-base https://mayai.ru` (опубликованные B02/B03); env `PUBLIC_SITE_URL` в QA-run давал 404 на те же slug

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблицы/blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 2 verified in fact-bank, 4 unverified — HTTP status codes в таблице ошибок, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` → `<blockquote>` (html-linter FAIL → PASS)

## Optional (не blocker)

- cover-агент: inline images + featured
- при publish сверить link-verify с актуальным `PUBLIC_SITE_URL`

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
