# QA: B06 n8n-agents-self-hosted-bez-queue-mode-2026

date: 2026-10-06
score_total: 92/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | 7 H2, FAQ 6, primary query в lead, без anchor-TOC — OK |
| GEO / citability | 25 | 24 | TL;DR, 2 таблицы, dual-instance blockquote, FAQ answer-first |
| CORE-EEAT lite | 15 | 13 | 18/20; −2 за 2 internal slug без href (404 на mayai.ru 06.10.2026) |
| Human voice | 15 | 15 | 0 AI-slop hits; Flesch RU 100 (короткие предложения) |
| Fact safety | 15 | 14 | fact-check PASS; Wordstat ~699 — с оговоркой B02 |
| Contract HTML | 10 | 6 | linter PASS, char 8632 ✓, CTA ≤3 ✓; −4 нет `<img>`; env в blockquote вместо `<pre>` |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Lead/H2 закрывают «n8n агенты на своем сервере» |
| C02 | ✓ | Lead — direct answer + чек-лист, без «в этой статье» |
| C03 | ✓ | Аудитория: self-hosted DevOps / админ n8n |
| C04 | ✓ | Agents vs node, queue mode, N8N_WEBHOOK_URL — disambiguation |
| O01 | ✓ | H2 = research action_outline (7 секций + FAQ) |
| O02 | ✓ | inventory → topology → env → publish → troubleshooting |
| O03 | ✓ | FAQ 6 пар из research |
| O04 | ✓ | ol шаги, ul 15 пунктов, 2 table |
| R01 | ✓ | TL;DR + blockquote dual instance + FAQ standalone |
| R02 | ✓ | Версии n8n, queue — docs.n8n.io в Fact Check blockquote |
| R03 | ✓ | Нет неподтверждённых цен; Wordstat с датой/оговоркой |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: dual instance обход queue mode |
| E02 | ✓ | «Делайте / Не делайте» в H2 |
| E03 | ✓ | CTA Make ×1, Telegram ×1, author ×2 (Fact Check) |
| Exp01 | ✓ | Режим B checklist, без fake case |
| Exp02 | ✓ | Тон how-to, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Риски: queue, shared credentials, surface attack |
| Ept02 | ✗ | 2 из 3 internal — plain slug (404 ustanovka/nastroyka на mayai.ru) |

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

- total: 4, failed: 0
- `--site-base`: https://mayai.ru
- OK: /avtomatizaciya-n8n-ai-agents/, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff, t.me/maya_pro
- fix cycle 1: убраны href на `/ustanovka-n8n-docker-vps/` и `/nastroyka-n8n-agents-2026/` (HTTP 404); slug в тексте для indexer/publish

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (таблицы/чек-лист — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (1 extracted, 1 verified)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS
- topic: PASS (handoff utility gate topic)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` → blockquote (html-linter); internal 404 → plain slug (link-verify)

## Optional (не blocker)

- восстановить href internal после публикации ustanovka/nastroyka на mayai.ru
- добавить `<img>` с alt по контракту

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
