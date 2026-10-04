# QA: B01 primer-seo-stati

date: 2026-10-04
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2/H3, primary query, FAQ 7 пар, перелинковка — OK; H2 schema переименован без «FAQ» в заголовке (linter) |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 8 шагов, workflow blockquote, атомарные H2 |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 70.3 |
| Fact safety | 15 | 13 | fact-check PASS; 5 чисел/лет вне fact-bank (ориентиры объёма, GEO-bench 2024 — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, объём ~9333 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция B2B |
| C04 | ✓ | SEO, GEO, schema, JSON-LD объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (4 блока + «Что дальше») |
| O02 | ✓ | Логичный outline how-to |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (8 шагов), ul (чеклист 17), 2× table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Яндекс Директ, Вордстат, GEO-bench — с URL |
| R03 | ✓ | Нет неподтверждённых % роста |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (режим B) |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA Make + профиль автора, ≤3 |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Wordstat MCP, ограничения объёма — честно |
| Ept02 | ✗ | 2× mayai.ru GEO (внешние 200), `/` — internal; нет 2–3 internal slug на site-base (example.com) |

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

- total: 7, failed: 0
- fix applied: `/blog/geo-optimizaciya-sajta-2026/` → `https://mayai.ru/geo-optimizaciya-sajta-2026/` (2×); H2 без дубля FAQ в заголовке
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4
- Flesch RU: 70.3 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 2 verified in fact-bank, 5 unverified — ориентиры, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS (8 numbered steps, 7 FAQ, 2 tables, workflow blockquote)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (GEO QA): переименован H2 «Настройте FAQ…» → «Настройте schema и JSON-LD…»; исправлены битые internal slug на абсолютный mayai.ru B04
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- после publish на mayai.ru — заменить перелинковку B04 на relative slug того же домена

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
