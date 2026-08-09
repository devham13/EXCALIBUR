# QA: B01 primer-seo-stati

date: 2026-08-09
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ-структура, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 6 шагов, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 75.7 |
| Fact safety | 15 | 13 | fact-check PASS; 4 числа не в fact-bank (ориентиры объёма — допустимо) |
| Contract HTML | 10 | 7 | linter PASS, объём 9332 ✓, CTA 2× ✓; −3 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (6 шагов), ul (чеклист 18), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster, llms.txt — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; выдуманная статистика запрещена в чеклисте |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 (делайте/не делайте) |
| E03 | ✓ | CTA kv-ai.ru ×2, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно (Fact Check Box) |
| Ept02 | ✓ | Все 4 ссылки HTTP 200 |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING (0 cliches) | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility-gate | PASS | utility-gate-report.json |

## Link verify

- total: 4, failed: 0
- OK: wordstat.yandex.ru, webmaster.yandex.ru, internal /, kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (таблица/чеклист/TL;DR — допустимо для WARNING)
- Flesch RU: 75.7 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 2 verified in fact-bank, 4 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS
- warn: «в этой статье вы узнаете» — в чеклисте как антипример, не вода в тексте
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (GEO QA): переименован H2 «Настройте FAQ и schema для блога» → «Настройте schema и разметку для блога» (duplicate FAQ linter fail)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
