# QA: B01 primer-seo-stati

date: 2026-08-07
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица SEO vs GEO, 8 шагов, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 75.9 |
| Fact safety | 15 | 13 | fact-check PASS; 5 чисел не в fact-bank (ориентиры объёма/мета — из research) |
| Contract HTML | 10 | 7 | linter PASS, объём 9251 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Maya AI |
| C04 | ✓ | SEO, GEO, llms.txt, passages объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (SEO+GEO, структура, schema, чеклист) |
| O02 | ✓ | Логичный outline: workflow → структура → schema → чеклист → FAQ |
| O03 | ✓ | FAQ 7 пар, реальные queries из faq_hints |
| O04 | ✓ | ol (8 шагов), ul (13 checklist), table SEO vs GEO |
| R01 | ✓ | TL;DR + blockquote-схемы + FAQ standalone |
| R02 | ✓ | Wordstat, Webmaster, llms.txt — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых % и цен |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (эталон формата) |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, mayai internal ×3 — в лимите |
| Exp01 | ✓ | Режим B, editorial без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Wordstat MCP недоступен — честная оговорка |
| Ept02 | ✓ | Internal links: `/`, `/blog/geo-optimizaciya-sajta-2026/`, `/` (×2 в чеклисте) |

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
- OK: mayai.ru/ (×1), wordstat.yandex.ru, webmaster.yandex.ru, mayai.ru/blog/geo-optimizaciya-sajta-2026/, kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо)
- Flesch RU: 75.9 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 3 verified in fact-bank, 5 unverified — ориентиры объёма/мета из research, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json)
- warn: «в этой статье вы узнаете» — в контексте антипримера (шаг 4), не blocker

## Fix cycle

- cycle 1: GEO QA — H2 «Оформите FAQ и schema…» → «Оформите schema и разметку…» (duplicate FAQ linter)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- перефразировать шаг 4 без фразы «в этой статье вы узнаете» (utility gate warn)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
