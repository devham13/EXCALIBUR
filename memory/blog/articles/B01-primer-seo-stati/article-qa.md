# QA: B01 primer-seo-stati

date: 2026-10-04 (GEO QA прогон EXCALIBUR_RUN_DATE)
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 8 шагов, FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 72.5 |
| Fact safety | 15 | 12 | fact-check PASS; 5 чисел не в fact-bank (коридор объёма, чанки — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, объём 8843 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, AEO объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline (8 шагов + чек-лист + FAQ) |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (8 шагов), ul (чек-лист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Яндекс Direct, kv-ai — с URL |
| R03 | ✓ | Нет выдуманных % Wordstat; GEO-bench — как ориентир эксперимента |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика «Делайте / Не делайте» в H2 |
| E03 | ✓ | CTA внешний (Make) — один, без перебора |
| Exp01 | ✓ | Режим B, экспертный блок с author_id artur-horoshev |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения Wordstat/MCP названы честно |
| Ept02 | ✓ | Все 4 ссылки HTTP 200 (link-verify) |

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
- OK: wordstat.yandex.ru, direct.yandex.ru (SEO-текст), `/` (internal), kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/workflow — допустимо для PASS slop-detector)
- Flesch RU: 72.5 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 1 verified in fact-bank, 5 unverified — ориентиры объёма/чанков, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS (8 numbered steps, 8 H2, 7 FAQ H3, 1 table, 3 blockquotes, 21 action markers)
- see `utility-gate-report.json`

## Fix cycle

- cycle 0: правки article.html не потребовались — все скрипты PASS с первого прогона

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту writer/cover
- при желании усилить fact-bank для коридора 8 500–9 500 знаков

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: optional (8 шагов в ol) | author_id: artur-horoshev
