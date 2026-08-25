# QA: B06 cursor-subscriptions-nastrojka-2026

date: 2026-08-25
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | 7 H2, FAQ 7, primary «cursor subscriptions» + disambiguation от тарифа Pro |
| GEO / citability | 25 | 24 | TL;DR, таблица Subscriptions vs Automations, workflow blockquote, 18 numbered steps |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за 2 internal href на один slug B03 (карточка допускает 2–3) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0 |
| Fact safety | 15 | 13 | fact-check PASS; 3/4 числа не в fact-bank (30–45 мин, 180 дней — из research-notes/docs) |
| Contract HTML | 10 | 7 | linter PASS, объём 9375 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/H1 закрывают «cursor subscriptions» с уточнением «фича cloud agents» |
| C02 | ✓ | Lead — direct answer (PR+Slack сценарий), без «в этой статье» |
| C03 | ✓ | Аудитория: команда с GitHub+Slack, cloud agents на paid плане |
| C04 | ✓ | Subscriptions vs Pro, Automations, spend limit — при первом появлении |
| O01 | ✓ | H2 совпадают с каркасом B06 (7 секций + FAQ) |
| O02 | ✓ | Outline: compare → dashboard → PR → Slack → /goal → security → next |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (5+5+3+5), ul (12 checklist), 1 table |
| R01 | ✓ | TL;DR + workflow blockquote + Fact Check blockquote |
| R02 | ✓ | 180 days, autofix limits — cursor.com/docs/cloud-agent/capabilities |
| R03 | ✓ | Нет неподтверждённых цен/процентов |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | RU how-to gap: Subscriptions ≠ тариф Pro; единый PR+Slack workflow |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, @maya_pro ×1, author ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон research/brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Teams autofix, GitHub Actions only, 180 days, local Agent |
| Ept02 | ✗ | 2× href на `/podklyuchenie-mcp-cursor/` (достаточно по карточке, но один target) |

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

- total: 10, failed: 0
- OK: cursor.com/changelog, docs/cloud-agent/*, docs/integrations/github, mayai.ru/podklyuchenie-mcp-cursor/, kv-ai.ru, t.me/maya_pro
- fix applied (cycle 1):
  - `cursor.com/automations`, `cursor.com/dashboard/*` (HTTP 403 из QA-среды) → docs URLs (`/docs/cloud-agent/automations`, `/docs/integrations/github`, `/docs/cloud-agent`, `/docs/cloud-agent/setup`)
- **Перед publish:** при необходимости вернуть прямые dashboard href для UX; повторить link-verify

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (4 extracted, 1 verified in fact-bank, 3 unverified — 30–45 мин и 180 дней из research-notes/docs, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — dashboard/automations URLs 403 → официальные docs URLs (link-verify pass)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- перед WP publish — опционально восстановить прямые dashboard href
- занести 180 days и setup timing в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
