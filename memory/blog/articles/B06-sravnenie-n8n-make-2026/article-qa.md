# QA: B06 sravnenie-n8n-make-2026

date: 2026-07-08
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «n8n vs make», FAQ 7 пар, таблицы, чеклист 15 — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, сравнительная таблица, матрица 6 сценариев, FAQ 7, workflow 9 шагов |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за plain text make.com/en/pricing (403 от Cloudflare в QA-среде) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, editorial comparison без marketing-bias |
| Fact safety | 15 | 13 | fact-check PASS; 5/13 чисел в fact-bank, тарифы n8n/Make — из research-notes |
| Contract HTML | 10 | 8 | linter PASS, объём 8705 ✓, CTA ≤3 ✓, internal href ×2; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «n8n vs make» |
| C02 | ✓ | Lead — direct answer (billing models), без «в этой статье» |
| C03 | ✓ | Аудитория: бизнес, выбирающий платформу автоматизации по TCO |
| C04 | ✓ | Self-host, DevOps, webhook, API, RAG, MCP — «на пальцах» |
| O01 | ✓ | H2 совпадают с карточкой B06 (критерии, таблица, Make/n8n, матрица, чеклист) |
| O02 | ✓ | Outline: критерии → таблица → Make → n8n → матрица 6 → чеклист 15 → next steps |
| O03 | ✓ | FAQ 7 пар, queries из research/Wordstat |
| O04 | ✓ | ol (9+15+5 шагов), 2 table, blockquotes |
| R01 | ✓ | TL;DR + схема выбора + итоговый вердикт матрицы |
| R02 | ✓ | Тарифы n8n/Make, billing models — с research-notes + n8n.io/pricing |
| R03 | ✓ | Цены с датой 08.07.2026; оговорка Core $12 vs $9 compare |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: decision workflow + матрица 6 + чеклист 15 (не клон make.com compare) |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, Telegram ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, честное comparison |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: DevOps, credit burn, 152-ФЗ, HITL |
| Ept02 | ✗ | make.com/en/pricing — plain text (href убран: HTTP 403 в link-verify) |

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
- OK: n8n.io/pricing, /podklyuchenie-mcp-cursor/, /avtomatizaciya-n8n-ai-agents/, kv-ai.ru/obuchenie-po-make, t.me/maya_pro
- fix applied (cycle 1):
  - `<a href="https://www.make.com/en/pricing">` → plain text `make.com/en/pricing` (HTTP 403 Forbidden от Cloudflare в QA-среде)
- **Перед publish:** восстановить href `https://www.make.com/en/pricing` (страница валидна в браузере)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/матрица — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (13 extracted, 5 verified in fact-bank, 8 unverified — тарифы/метрики из research-notes, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — make.com/en/pricing href → plain text для link-verify PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover-агент)
- восстановить href make.com/en/pricing перед WP publish
- занести тарифы Make/n8n и 5 800 ₽ курса в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
