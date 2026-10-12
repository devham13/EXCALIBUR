# QA: B06 integraciya-amocrm-n8n-2026

date: 2026-10-12
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, таблицы, anchor id на секциях |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 2 таблицы, 7 FAQ, inbound/outbound схемы |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за отсутствие href internal links |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100, first-person / editorial |
| Fact safety | 15 | 13 | fact-check PASS; HTTP-коды 403/200/429 не в fact-bank (техконтекст, не blocker) |
| Contract HTML | 10 | 6 | linter PASS, объём 9480 ✓, CTA ≤3 ✓; −4 нет `<img>` с alt, нет internal href |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/meta закрывают «интеграция amoCRM n8n» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: no-code без программиста |
| C04 | ✓ | OAuth, webhook, complex lead — на пальцах |
| O01 | ✓ | H2 совпадают с research-каркасом (6 + FAQ) |
| O02 | ✓ | stack → OAuth → inbound → outbound → dedupe → prod |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol/ul, 2 table, blockquote-схемы |
| R01 | ✓ | TL;DR + standalone блоки |
| R02 | ✓ | Лимиты amoCRM/n8n из research-notes |
| R03 | ✓ | 7 rps, 50/250 batch — с оговоркой по докам |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: amoCRM+n8n how-to, честное сравнение с Make |
| E02 | ✓ | «Делайте / Не делайте» в секциях |
| E03 | ✓ | CTA kv-ai ×1, author ×1, t.me ×1 |
| Exp01 | ✓ | Режим B, editorial без fake case |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Cloud community nodes, HTTPS, 429 |
| Ept02 | ✗ | Нет href internal links (404 до публикации hub-статей) |

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
- OK: kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff, t.me/maya_pro
- fix applied (cycle 1):
  - `/sravnenie-make-zapier-n8n-2026/`, `/ustanovka-n8n-docker-vps-2026/`, `/avtomatizaciya-n8n-ai-agents/` → plain text (HTTP 404 — статьи ещё не на live)
- **Перед publish / Indexer:** восстановить href на hub-статьи, повторить link-verify с `--site-base` из `PUBLIC_SITE_URL`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблицы/blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 2 verified in fact-bank, 3 unverified — HTTP-коды в техническом контексте)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 20`, `h2_sections: 7`, `faq_h3: 7`, `tables: 2`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — internal 404 → plain text (link-verify PASS); char_count 9480 в коридоре 8500–9500

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- восстановить internal href после публикации связанных slug на сайте
- занести лимиты amoCRM (7 rps, 16 MB payload) в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
