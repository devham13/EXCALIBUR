# QA: B01 primer-seo-stati

date: 2026-10-16
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ-структура, внешние/смежные ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, workflow, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 74.3 |
| Fact safety | 15 | 13 | fact-check PASS; 2 числа (диапазон объёма) не в fact-bank — допустимо |
| Contract HTML | 10 | 7 | linter PASS, объём 9090 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, schema объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol×2, ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Яндекс Direct, mayai.ru — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых % |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, режим B |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA kv-ai ×1, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно |
| Ept02 | ✓ | Все 4 URL HTTP 200 (link-verify) |

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

- total: 4, failed: 0
- OK: mayai.ru/geo-optimizaciya-sajta-2026/, direct.yandex.ru, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4
- Flesch RU: 74.3 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 3 verified, 2 unverified — ориентиры объёма, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS (7 FAQ h3, 9 H2, action_markers 19)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (GEO QA): H2 «…FAQ и schema» → «…вопросы на странице и schema» (html-linter duplicate FAQ); `/geo-…` → `https://mayai.ru/geo-optimizaciya-sajta-2026/` (link-verify 404)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
