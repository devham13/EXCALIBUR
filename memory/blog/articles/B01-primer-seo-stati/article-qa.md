# QA: B01 primer-seo-stati

date: 2026-10-13 (GEO QA после перезаписи Writer)
score_total: 93/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренняя ссылка `/` — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, workflow, 8 шагов ol, FAQ — OK |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 75.4 |
| Fact safety | 15 | 13 | fact-check PASS; 5 чисел/годов не в fact-bank (ориентиры объёма, KDD 2024 — допустимо) |
| Contract HTML | 10 | 6 | linter PASS после fix H2; объём 9346 ✓; −4 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье вы узнаете» в лиде |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline, 8 шагов |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (8 шагов), ul (чеклист 13), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Вордстат, Вебмастер, Яндекс B2B — с URL |
| R03 | ✓ | Нет неподтверждённых %; GEO-bench как именованный источник |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA Make + hub `/`, без перебора |
| Exp01 | ✓ | Режим B, author_id artur-horoshev |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения объёма названы честно |
| Ept02 | ✓ | Все ссылки HTTP 200 (mayai.ru, kv-ai.ru, Яндекс) |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, b2b.yandex.ru (SEO-гайд), kv-ai.ru/obuchenie-po-make, mayai.ru/ (relative `/`)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 75.4 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 2 verified in fact-bank, 5 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS
- warning: water phrase «в этой статье вы узнаете» — только в антипримере в ol (не blocker)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (GEO QA): H2 «Настройте FAQ, schema…» → «Настройте schema…» (html-linter duplicate FAQ headings)
- cycle 2: повтор скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- при желании — второй CTA services по контракту Writer (сейчас Make + hub)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
