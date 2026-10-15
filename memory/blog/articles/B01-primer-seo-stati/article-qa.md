# QA: B01 primer-seo-stati

date: 2026-10-15
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, чек-лист — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица SEO/GEO, workflow, 7 FAQ |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за 1 live internal + B04 plain text |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 76.3 |
| Fact safety | 15 | 13 | fact-check PASS; 2/8 в fact-bank; остальное — ориентиры объёма |
| Contract HTML | 10 | 8 | linter PASS, объём ~9386 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt |

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
| O04 | ✓ | ol (6 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых % |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA Make ×1, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно |
| Ept02 | ✗ | 1 internal (`/` 200); B04 — plain text (404 draft) |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, `/` (главная), kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- fix applied (cycle 1): `/geo-optimizaciya-sajta-2026/` → plain text «B04, href после публикации» (HTTP 404)
- **После publish B04:** восстановить href на geo longread, повторить link-verify

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист — допустимо)
- Flesch RU: 76.3 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 2 verified in fact-bank, 6 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS (water_hits: 0 после fix H2)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (GEO QA): link B04 404 → plain text; H2 «…FAQ и schema…» → «Schema и сниппеты под AI-поиск» (duplicate FAQ linter)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- после публикации B04 — вернуть internal href на geo-статью

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
