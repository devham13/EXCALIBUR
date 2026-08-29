# QA: B06 human-in-the-loop-ai-agents-n8n

date: 2026-08-29
score_total: 92/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query в lead, FAQ 7, без TOC в теле |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, risk-map + n8n vs Make, 7 FAQ, 49 numbered steps |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, editorial first-person |
| Fact safety | 15 | 13 | fact-check PASS; 3 числа не в fact-bank (EU deadline 2027, SLA 30 мин, kill switch 5 мин — из research-notes) |
| Contract HTML | 10 | 5 | linter PASS, объём 9364 ✓, CTA ×1 ✓, internal href ×2 ✓; −5 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Lead/H2 закрывают «human in the loop n8n» + RU «контроль ии агентов» |
| C02 | ✓ | Lead — direct answer (HITL = пауза перед опасным action), без «в этой статье» |
| C03 | ✓ | Аудитория: no-code-практики с AI-агентами на n8n/Make/Cursor |
| C04 | ✓ | Tool, API, HITL, human-on-the-loop — объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research action_outline (7 секций + FAQ) |
| O02 | ✓ | Outline: why → risk-map → n8n → Make → Cursor → checklist → next |
| O03 | ✓ | FAQ 7 пар, реальные queries из research |
| O04 | ✓ | ol (7+5+5+27+5), 2 table, blockquote-схемы |
| R01 | ✓ | TL;DR + blockquote-схемы + standalone FAQ blocks |
| R02 | ✓ | n8n 2.6.0, 9 каналов, Make Enterprise, EU AI Act Art.14 — research-notes |
| R03 | ✓ | Проценты/даты с оговорками («открытые обзоры 2026», Wordstat B02) |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: risk-map + чек-лист 27 пунктов на 3 платформах (пробел SERP) |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×1, author blockquote ×1 |
| Exp01 | ✓ | Режим B, editorial без fake case study |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Enterprise Make, Cloud Agents без per-action approve, EU legal disclaimer |
| Ept02 | ✓ | Internal links: /avtomatizaciya-n8n-ai-agents/, /nastroyka-cursor-automations-2026/ |

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
- OK: /avtomatizaciya-n8n-ai-agents/ (200), /nastroyka-cursor-automations-2026/ (200), kv-ai.ru/obuchenie-po-make (200)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (таблицы risk-map / n8n vs Make — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (4 extracted, 1 verified in fact-bank, 3 unverified — EU deadline 2027, SLA 30 мин, kill switch 5 мин из research-notes, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json из preflight)

## Fix cycle

- cycle 0: все скрипты PASS без правок article.html

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover-агент после QA)
- занести EU AI Act deadline 2027 и SLA-метрики в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
