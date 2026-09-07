# QA: B06 sravnenie-n8n-i-make-2026

date: 2026-09-07
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «n8n или make», FAQ 6, без TOC в теле — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица 6 критериев, TCO 6 шагов, чеклист 12, FAQ 6 |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за 1 internal link вместо 2–3 |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 96.8, практический тон без fake case |
| Fact safety | 15 | 13 | fact-check PASS; 6 чисел не в fact-bank (тарифы n8n/Make, Wordstat — из research-notes) |
| Contract HTML | 10 | 8 | linter PASS, объём 8605 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/H1 закрывают «n8n или make» |
| C02 | ✓ | Lead — direct answer (billing credits vs execution), без «в этой статье» |
| C03 | ✓ | Аудитория: SMB, выбирающий платформу автоматизации |
| C04 | ✓ | Execution, credits, self-hosted — «на пальцах» в первых абзацах |
| O01 | ✓ | H2 совпадают с research-каркасом (TCO → таблица → сценарии → гибрид → чеклист) |
| O02 | ✓ | Логичный outline: calc → compare → choose → hybrid → checklist → next |
| O03 | ✓ | FAQ 6 пар, реальные comparison-queries |
| O04 | ✓ | ol (6+12+4 шагов), ul (2), table |
| R01 | ✓ | TL;DR + blockquote-схемы, standalone FAQ-блоки |
| R02 | ✓ | Тарифы n8n/Make, credits transition — с research-notes и footer attribution |
| R03 | ✓ | Цены с датой 09.2026 и оговоркой «сверены 07.09.2026» |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: формула TCO runs×steps + чеклист 12 + гибрид 2026 |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×1, t.me ×1 — ≤3 |
| Exp01 | ✓ | Режим B (comparison), editorial без fake «я внедрил» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: 152-ФЗ с юристом, DevOps, API LLM отдельно, pilot |
| Ept02 | ✗ | 1 internal link (`/avtomatizaciya-n8n-ai-agents/`); карточка темы — 2–3 |

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
- OK: internal `/avtomatizaciya-n8n-ai-agents/` (200), kv-ai.ru/obuchenie-po-make (200), t.me/maya_pro (200)
- site-base: EXCALIBUR_PUBLIC_SITE_URL / site-brief

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (TL;DR/таблица — допустимо)
- Flesch RU: 96.8 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (10 extracted, 4 verified in fact-bank, 6 unverified — тарифы/Wordstat из research, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- metrics: 22 numbered items, 7 H2, 6 FAQ, 1 table, 16 action markers
- see `utility-gate-report.json`

## Fix cycle

- cycle 0: правки не потребовались — все скрипты PASS с первого прогона

## Optional (не blocker)

- добавить 1–2 internal links (B02/B03) для Ept02
- добавить 1 `<img>` с alt по контракту
- занести тарифы Make/n8n и Wordstat-цифры в fact-bank после восстановления API

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
