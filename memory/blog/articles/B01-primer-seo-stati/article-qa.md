# QA: B01 primer-seo-stati

date: 2026-08-08 (GEO QA rerun после fix H2)
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, ol 8 шагов, island test, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 81.5 |
| Fact safety | 15 | 13 | fact-check PASS; 4 числа не в fact-bank (ориентиры объёма/meta — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, объём ~9438 ✓, CTA 1 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt, island test объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (8 шагов workflow) |
| O02 | ✓ | Логичный outline: SEO+GEO → семантика → SERP → блоки → мета → чеклист → FAQ |
| O03 | ✓ | FAQ 7 пар, реальные queries из research |
| O04 | ✓ | ol (8 шагов), ul (чеклист 16 пунктов), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Direct, GEO-bench — с внешними ссылками |
| R03 | ✓ | Princeton GEO-bench с контекстом; нет выдуманных ROI |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (режим B) |
| E02 | ✓ | Практика «делать/не делать» в каждой H2 |
| E03 | ✓ | CTA Make.com ×1, без перебора |
| Exp01 | ✓ | Режим B, Fact Check Box с автором |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения Wordstat MCP offline названы честно |
| Ept02 | ✓ | Все 5 ссылок HTTP 200 (mayai.ru/, kv-ai.ru, wordstat, webmaster, direct.yandex) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility-gate | PASS | utility-gate-report.json |

## Link verify

- total: 5, failed: 0
- OK: wordstat.yandex.ru, webmaster.yandex.ru, direct.yandex.ru (SEO-текст), mayai.ru/ (relative `/`), kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист/workflow — допустимо для PASS slop-detector)
- Flesch RU: 81.5 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 1 verified in fact-bank, 4 unverified — ориентиры объёма/meta/GEO-bench, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- verdict: PASS
- warn: water phrase «в этой статье вы узнаете» — в контексте «Без фразы…» (антипример), не blocker
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (GEO QA): H2 «Оформите FAQ, мета и schema» → «Оформите мета и schema» (duplicate FAQ linter fail)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover-агент)
- schema Person автора — зона schema-агента

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
