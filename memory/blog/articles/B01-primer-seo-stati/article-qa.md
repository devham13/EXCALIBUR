# QA: B01 primer-seo-stati

date: 2026-10-04 (GEO QA после writer refresh)
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 7 шагов ol, FAQ, island H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 83.7 |
| Fact safety | 15 | 13 | fact-check PASS; 4 числа-ориентира объёма вне fact-bank — допустимо |
| Contract HTML | 10 | 7 | linter PASS, объём 8794 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без intro-клише |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (7 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Direct — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; ориентиры объёма без fake stats |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA Make ×2, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно |
| Ept02 | ✓ | Internal `/`, `/#services` — HTTP 200 на example.com |

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
- OK: direct.yandex.ru, wordstat, webmaster, example.com/, example.com/#services, kv-ai.ru
- fix applied (geo-qa cycle 1): `/geo-optimizaciya-sajta-2026/` → `/#services`; H2 переименован (duplicate FAQ linter)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист — допустимо)
- Flesch RU: 83.7 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 3 verified in fact-bank, 4 unverified — коридоры объёма/lead)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, blog-dir scan)
- see `cannibalization-report.json`

## Fix cycle

- cycle 1 (geo-qa): rename H2 «мета, FAQ…» → «мета, снипpet и GEO-упаковку»; internal link 404 → `/#services`; убрана water-фраза в ol
- cycle 2: повтор скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту writer/cover

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
