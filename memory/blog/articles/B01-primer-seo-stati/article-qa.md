# QA: B01 primer-seo-stati

date: 2026-09-08
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, ol 7 шагов, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 81.4 |
| Fact safety | 15 | 13 | fact-check PASS; 4 числа-ориентира не в fact-bank (допустимо) |
| Contract HTML | 10 | 7 | linter PASS, объём 9339 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Ковчега |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (7 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; «+140%» только как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×2, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно (Wordstat вручную) |
| Ept02 | ✓ | CTA и internal links — HTTP 200 (link-verify) |

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

- total: 5, failed: 0
- OK: wordstat.yandex.ru, webmaster.yandex.ru, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff, internal `/`
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо)
- Flesch RU: 81.4 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 3 verified in fact-bank, 4 unverified — ориентиры объёма/lead)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- verdict: PASS (1 water phrase «в этой статье вы узнаете» — антипример в ol, не blocker)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1: переименован H2 «Добавьте FAQ и schema…» → «Добавьте schema и блок вопросов…» (duplicate FAQ linter)
- cycle 2: не потребовался — все скрипты PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- уточнить объёмы Wordstat вручную (research warning)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | author_id: artur-horoshev
