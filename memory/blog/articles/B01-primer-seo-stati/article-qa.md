# QA: B01 primer-seo-stati

date: 2026-08-13
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренняя ссылка `/` — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, ol 6 шагов, FAQ 7, island H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 76.3 |
| Fact safety | 15 | 13 | fact-check PASS; 4 числа не в fact-bank (ориентиры объёма/мета — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, объём 9699 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (schema блок переименован без «FAQ» в H2) |
| O02 | ✓ | Логичный outline: SEO+GEO → структура → schema → чек-лист → next → FAQ |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (6 шагов), ul (чеклист 14), table, blockquote ×3 |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов (TL;DR, таблица, Fact Check) |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Direct — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; объёмы — как ориентиры |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (режим B) |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make.com ×2 (kv-ai.ru), без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно (Wordstat, llms.txt) |
| Ept02 | ✓ | CTA `kv-ai.ru/obuchenie-po-make` ×2 — HTTP 200 |

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
- OK: direct.yandex.ru, wordstat.yandex.ru, webmaster.yandex.ru, kv-ai.ru/obuchenie-po-make (×2), mayai.ru/ (relative `/`)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо)
- Flesch RU: 76.3 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 2 verified in fact-bank, 4 unverified — ориентиры объёма/lead/мета)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS
- warn: «в этой статье вы узнаете» — только в anti-pattern («без …»), не в prose
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (GEO QA): H2 «Добавьте FAQ и schema…» → «Добавьте schema и разметку…» (html-linter duplicate FAQ rule)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover после publish)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
