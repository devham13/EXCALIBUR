# QA: B01 primer-seo-stati

date: 2026-08-26
score_total: 96/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ-структура, внутренняя ссылка `/` по карточке темы |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 6 шагов, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 81.9 |
| Fact safety | 15 | 13 | fact-check PASS; 3 числа не в fact-bank (ориентиры объёма/lead — допустимо) |
| Contract HTML | 10 | 9 | linter PASS, объём 8558 ✓, CTA ≤3 ✓; −1 нет `<img>` с alt (рекомендация) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (6 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых % и цен |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика «Делать/Не делать» в H2-секциях |
| E03 | ✓ | CTA kv-ai.ru ×2 + author — ≤3 |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения (переспам, GEO без SEO) названы |
| Ept02 | ✓ | internal_links `/` из карточки B01 — HTTP 200 |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, mayai.ru/, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/чеклист — допустимо)
- Flesch RU: 81.9 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 3 verified in fact-bank, 3 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues)
- see `cannibalization-report.json`

## Utility gate

- verdict: PASS (6 numbered steps, 7 FAQ, 1 table, 0 water hits)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1: H2 «Добавьте FAQ…» → «Подготовьте блок вопросов…» (html-linter duplicate FAQ); +1 предложение для char_count ≥8500
- cycle 2: повтор GEO QA — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (роль cover после QA PASS)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | Author: artur-horoshev (pending SameAs)
