# QA: B01 primer-seo-stati

date: 2026-10-09
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, перелинковка — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 7 шагов ol, чек-лист 18, FAQ 7 |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 B04 через absolute mayai.ru (404 на relative `/blog/…` в QA site-base) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 76.9 |
| Fact safety | 15 | 13 | fact-check PASS; 4/7 чисел вне fact-bank (ориентиры объёма, llms 2024 — из research) |
| Contract HTML | 10 | 8 | linter PASS, объём ~9711 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (7 шагов), ul (чек-лист 18), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Яндекс Direct, Wordstat, Webmaster — с href |
| R03 | ✓ | Нет неподтверждённых % |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA Make + главная, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно |
| Ept02 | ✗ | 2× `/` internal OK; B04 — absolute URL (relative `/blog/…` → 404 на PUBLIC_SITE_URL) |

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

- total: 6, failed: 0
- site-base: PUBLIC_SITE_URL
- fix cycle 1: H2 без «FAQ» в заголовке (duplicate FAQ linter); `/blog/geo-…` → `https://mayai.ru/geo-optimizaciya-sajta-2026/`
- see `link-verify.json`

## Utility gate

- overall: PASS
- warn: water phrase «в этой статье вы узнаете» — в anti-примере в body (не blocker)
- see `utility-gate-report.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист — допустимо)
- Flesch RU: 76.9 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 3 verified, 4 unverified — ориентиры, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Fix cycle

- cycle 1 (GEO QA): rename H2 «мета, FAQ и schema» → «мета, разметку и schema»; fix B04 href
- cycle 2: не потребовался

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- после publish B01 на mayai.ru — заменить B04 на relative `/geo-optimizaciya-sajta-2026/` и повторить link-verify

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
