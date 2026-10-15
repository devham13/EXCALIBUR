# QA: B01 primer-seo-stati

date: 2026-10-10
score_total: 91/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2/H3, primary query, FAQ 7 пар, без TOC — OK; −1 за абсолютный mayai.ru вместо относительного interlink |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица SEO vs GEO, 8 шагов, чеклист 15 пунктов |
| CORE-EEAT lite | 15 | 14 | 18/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 83.0, editorial «Ковчег» |
| Fact safety | 15 | 13 | fact-check PASS; 3 числа (объём, Description) из контракта/research, не blocker |
| Contract HTML | 10 | 10 | linter PASS, объём 8570 ✓, CTA ≤3 ✓, whitelist tags |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, hook без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога / контент-маркетинг |
| C04 | ✓ | GEO, llms.txt, JSON-LD — простым языком |
| O01 | ✓ | H2 совпадают с research workflow (SEO+GEO, структура, schema, чеклист) |
| O02 | ✓ | Outline: определение → семантика → FAQ/schema → publish gate |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (8 шагов), ul (15 checklist), table |
| R01 | ✓ | TL;DR + blockquote workflow, island H2 |
| R02 | ✓ | Яндекс/Google/Wordstat — с research-notes |
| R03 | ✓ | Объём 8500–9500 как editorial norm, не fake stats |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: один longread SEO+GEO, режим B-эталон |
| E02 | ✓ | «Делайте / Не делайте» в ключевых H2 |
| E03 | ✓ | CTA Make ×1, Fact Check block, author |
| Exp01 | ✓ | Режим B, без выдуманного кейса |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Оговорки: нет универсального объёма, schema — следующий шаг пайплайна |
| Ept02 | ✗ | Interlink на GEO-гайд — absolute mayai.ru (PUBLIC_SITE_URL в QA ≠ mayai.ru) |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, mayai.ru/geo-optimizaciya-sajta-2026/, site home `/`, kv-ai.ru/obuchenie-po-make
- fix applied (cycle 1):
  - H2 «Добавьте FAQ…» → «Добавьте JSON-LD…» (duplicate FAQ linter)
  - `/blog/geo-…` → `https://mayai.ru/geo-optimizaciya-sajta-2026/` (404 на PUBLIC_SITE_URL)
  - negation lead-cliché перефразирован (utility water_hits)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо)
- Flesch RU: 83.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 2 verified in fact-bank, 3 unverified — объём/meta из контракта)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass, 0 issues
- see `cannibalization-report.json`

## Utility gate

- verdict: PASS (8 numbered steps, table, FAQ, no water hits after fix)
- see `utility-gate-report.json`

## QA cycles

1. FAIL html-linter (duplicate FAQ H2) + link-verify (geo 404) → minimal HTML fixes → **PASS**

next: excalibur-blog-cover || excalibur-blog-schema (параллельно после PASS)
