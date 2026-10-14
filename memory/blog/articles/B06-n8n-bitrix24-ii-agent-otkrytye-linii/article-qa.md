# QA: B06 n8n-bitrix24-ii-agent-otkrytye-linii

date: 2026-10-14
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2×7 + FAQ, primary query, якоря id, без TOC в теле |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица CoPilot vs n8n, 6 FAQ, 9+4+12 шагов |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 96.6, editorial «Делайте/Не делайте» |
| Fact safety | 15 | 13 | fact-check PASS; 3/4 числа вне fact-bank (#3094, 172 800, 503 — из research/apidocs) |
| Contract HTML | 10 | 7 | linter PASS, объём 9438 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (cover после QA) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «n8n битрикс24 ии агент» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: админы CRM / автоматизаторы без DevOps |
| C04 | ✓ | Webhook, REST, ONIMBOTV2*, LINES — «на пальцах» |
| O01 | ✓ | H2 = 9 шагов research + prod + next |
| O02 | ✓ | Outline: выбор стека → Bitrix → n8n → CRM → HITL → приёмка |
| O03 | ✓ | FAQ 6 пар, queries из research |
| O04 | ✓ | ol (9+4), ul (12 checklist), table |
| R01 | ✓ | TL;DR + blockquote цепочка MVP, standalone блоки |
| R02 | ✓ | 2 rps, ONIMBOTV2*, imopenlines.* — apidocs + research-notes |
| R03 | ✓ | Нет выдуманных Wordstat; расчёт 172 800 с явной формулой |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: MVP OL за вечер, не CRM-webhook-only |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, t.me ×1, author ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон research/brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Лимиты 2 rps, QUERY_LIMIT_EXCEEDED, scopes |
| Ept02 | ✓ | Internal href ×2 (B02, B03 на mayai.ru) |

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

- **site-base:** `https://mayai.ru` (опубликованные B02/B03; `PUBLIC_SITE_URL` в QA-среде отдаёт 404 на те же пути)
- total: 10, failed: 0
- OK: apidocs.bitrix24.ru (×4), helpdesk, n8n.io, mayai.ru/avtomatizaciya-n8n-ai-agents/, mayai.ru/podklyuchenie-mcp-cursor/, kv-ai.ru (×2), t.me/maya_pro
- fix applied: **нет** (relative internal links резолвятся на mayai.ru)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (lead/таблица/чеклист — допустимо)
- Flesch RU: 96.6 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (4 extracted, 1 verified in fact-bank, 3 unverified — не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass, 0 issues (6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate (article)

- overall: PASS (19 numbered items, 7 H2, 6 FAQ, 1 table, 3 blockquotes)
- see `utility-gate-report.json`

## Blockers

- none

## Следующий шаг

④ cover || schema (параллельно после PASS)
