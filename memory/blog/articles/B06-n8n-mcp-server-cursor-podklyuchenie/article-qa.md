# QA: B06 n8n-mcp-server-cursor-podklyuchenie

date: 2026-10-10
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, без anchor-TOC |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица режимов, 7 FAQ, пошаговые ol |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0 |
| Fact safety | 15 | 13 | fact-check PASS; 5678/401 — HTTP/порт, не blocker |
| Contract HTML | 10 | 7 | linter PASS после fix; объём 9318 ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/H1 закрывают «n8n mcp server» |
| C02 | ✓ | Lead — direct answer |
| C03 | ✓ | Аудитория: Cursor + self-hosted/cloud n8n |
| C04 | ✓ | MCP и n8n — в intro |
| O01 | ✓ | H2 совпадают с research action_outline |
| O02 | ✓ | Режим → Trigger → instance → config → verify → troubleshooting |
| O03 | ✓ | FAQ 7 пар, queries из карточки |
| O04 | ✓ | ol (6+5+2), ul checklist, table |
| R01 | ✓ | TL;DR + blockquote-схемы |
| R02 | ✓ | Версии n8n, URL — research-notes / docs |
| R03 | ✓ | Нет неподтверждённых цен/процентов |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: Trigger vs instance + community n8n-mcp vs official |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai ×1, author ×1, mayai internal ×2 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Практический тон, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | 401, proxy, queue mode, лимит tools |
| Ept02 | ✗ | Нет relative internal href (only absolute mayai.ru — OK для publish) |

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
- OK: mayai.ru/podklyuchenie-mcp-cursor/, mayai.ru/avtomatizaciya-n8n-ai-agents/, cursor.com/docs/mcp, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- `--site-base`: EXCALIBUR_PUBLIC_SITE_URL

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (3 extracted, 1 verified in fact-bank, 2 unverified — порт 5678, HTTP 401)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS
- topic: PASS (utility-gate-topic.json, preflight)

## Fix cycle

- cycle 1: GEO QA — заменены запрещённые `<code>`/`<pre>` на `<b>` и blockquote (whitelist linter); перезапуск всех скриптов → PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
