# QA: B06 nastrojka-make-ai-agents

date: 2026-09-12
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «make ai agents настройка», FAQ 7, anchor id — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица agent vs scenario, FAQ 7, 5+4 шага, workflow blockquote |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 нет `<img>` с alt |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, editorial first-person |
| Fact safety | 15 | 13 | fact-check PASS; 2/7 чисел в fact-bank (3000+, credits, 5 800 ₽ — из research/help.make.com) |
| Contract HTML | 10 | 8 | linter PASS, объём 9407 ✓, CTA ≤3 ✓, internal href ×2 (mayai.ru); −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «make ai agents настройка» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: triage заявок, Make-пользователи без кода |
| C04 | ✓ | MCP, RAG, webhook, Run an agent — «на пальцах» |
| O01 | ✓ | H2 совпадают с research-каркасом B06 (6 секций + FAQ) |
| O02 | ✓ | Outline: agent vs scenario → create → instructions → tools → knowledge/test → prod |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (5+4 шага), ul (12 checklist + tools), 1 table |
| R01 | ✓ | TL;DR + workflow blockquote + Fact Check blockquote |
| R02 | ✓ | Релиз 02.02.2026, credits, 3000+ apps — с research-notes / help.make.com |
| R03 | ✓ | Цены/credits с оговоркой open beta и датой сверки 12.09.2026 |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Ковчег: triage MVP, guardrails, credits checklist |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×2, author ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: nesting 1 level, HITL, credits, Free limits |
| Ept02 | ✗ | Internal links — absolute mayai.ru (PUBLIC_SITE_URL ≠ mayai.ru); перед publish можно вернуть relative `/avtomatizaciya-n8n-ai-agents/` |

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
- OK: mayai.ru/avtomatizaciya-n8n-ai-agents/ (×2), kv-ai.ru/obuchenie-po-make (×2 в HTML), kv-ai.ru/artur-horosheff
- fix applied (cycle 1):
  - `/avtomatizaciya-n8n-ai-agents/` → `https://mayai.ru/avtomatizaciya-n8n-ai-agents/` (404 на PUBLIC_SITE_URL при relative)
- **Перед publish:** при необходимости вернуть relative href для mayai.ru и повторить link-verify с `--site-base https://mayai.ru`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/blockquote/чеклист — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 2 verified in fact-bank, 5 unverified — credits/3000+/5 800 ₽ из research, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — relative internal links → absolute mayai.ru (link-verify 404 на PUBLIC_SITE_URL)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести credits/3000+/5 800 ₽ в fact-bank
- восстановить relative internal href после publish на mayai.ru

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
