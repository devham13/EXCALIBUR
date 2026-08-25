# QA: B01 primer-seo-stati

date: 2026-08-25
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | TL;DR answer-first, таблица SEO vs GEO, 9 шагов ol, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 80.8 |
| Fact safety | 15 | 13 | fact-check PASS; 4/6 чисел не в fact-bank (ориентиры объёма/мета — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, объём 9309 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Maya AI |
| C04 | ✓ | SEO, GEO, llms.txt, LSI объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research action_outline (9 шагов) |
| O02 | ✓ | Outline: SEO+GEO → семантика → outline → черновик → schema → чек-лист → FAQ |
| O03 | ✓ | FAQ 7 пар, queries из research/Wordstat |
| O04 | ✓ | ol (9 шагов), ul (чек-лист), table SEO vs GEO |
| R01 | ✓ | TL;DR + workflow blockquote + Fact Check blockquote |
| R02 | ✓ | Wordstat, Webmaster — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; антипример «раздувание до 15 000» |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (эталон B01) |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, internal links ×2 |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Wordstat показы уточнять; объём по SERP |
| Ept02 | ✓ | Internal links: `/`, `/geo-optimizaciya-sajta-2026/` — HTTP 200 |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, `/geo-optimizaciya-sajta-2026/`, `/`, kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо)
- Flesch RU: 80.8 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 2 verified in fact-bank, 4 unverified — ориентиры объёма/мета, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 13`, `h2_sections: 7`, `faq_h3: 8`, `tables: 1`)
- topic: PASS (preflight utility gate B01)

## Fix cycle

- cycle 1: GEO QA — переименован H2 «Подключите FAQ и schema…» → «Подключите schema и разметку…» (html-linter: duplicate FAQ sections)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
