# QA: B01 primer-seo-stati

date: 2026-09-10
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ-структура, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 8 шагов, 6 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 79.3 |
| Fact safety | 15 | 13 | fact-check PASS; 5 чисел не в fact-bank (ориентиры объёма — допустимо); «44%» с оговоркой «по данным исследований» |
| Contract HTML | 10 | 7 | linter PASS после fix H2; объём ~9200 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Excalibur |
| C04 | ✓ | SEO, GEO, RAG объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 пар, реальные queries |
| O04 | ✓ | ol (8 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Директ — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых % без оговорки |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make.com ×1, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно (объём по SERP, Wordstat) |
| Ept02 | ✓ | Internal links: /, /geo-optimizaciya-sajta-2026/ |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, direct.yandex.ru, geo-optimizaciya-sajta-2026/, / (×2 dedupe), kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 79.3 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 3 verified in fact-bank, 5 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS
- warn: water phrase «в этой статье вы узнаете» — в антипримере («Без формулы…»), не blocker
- see `utility-gate-report.json`

## Fix cycle

- cycle 1: переименован H2 «5. Добавьте FAQ и подготовьте schema» → «5. Подготовьте schema и структурированные данные» (html-linter duplicate FAQ)
- cycle 2: повтор GEO QA — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover-агент)
- перефразировать антипример water phrase для чистого utility-gate warn

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
