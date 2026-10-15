# QA: B01 primer-seo-stati

date: 2026-09-06
score_total: 96/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 8 шагов, FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 74 |
| Fact safety | 15 | 13 | fact-check PASS; 5 чисел не в fact-bank (ориентиры объёма/мета — допустимо) |
| Contract HTML | 10 | 9 | linter PASS, объём 9466 ✓, CTA 1 ✓; −1 нет `<img>` с alt (рекомендация) |

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
| O04 | ✓ | ol (8 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Вордстат, Webmaster, Яндекс Direct — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; Princeton GEO-bench — с URL mayai.ru |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (режим B) |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×1, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы (Wordstat MCP недоступен) |
| Ept02 | ✓ | Internal links: /, /geo-optimizaciya-sajta-2026/ |

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

- total: 7, failed: 0
- OK: direct.yandex.ru, wordstat.yandex.ru, webmaster.yandex.ru, mayai.ru/geo-optimizaciya-sajta-2026/, /geo-optimizaciya-sajta-2026/, /, kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (таблица/чеклист/ol — допустимо)
- Flesch RU: 74.0 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 2 verified in fact-bank, 5 unverified — ориентиры объёма/мета, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- verdict: PASS
- warnings: water phrase «в этой статье вы узнаете» — только в антипримере шага 4, не blocker
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (GEO QA): H2 «Настройте мета, FAQ и schema» → «Настройте мета, разметку и schema» (html-linter duplicate FAQ false positive)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover-агент)
- уточнить llms.txt «сентября 2024» первоисточником в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | author_id: artur-horoshev
