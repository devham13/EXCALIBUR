# QA: B01 primer-seo-stati

date: 2026-08-11
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ-структура, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 8 шагов, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 87.1 |
| Fact safety | 15 | 13 | fact-check PASS; 3 числа не в fact-bank (ориентиры объёма/CWV — допустимо) |
| Contract HTML | 10 | 7 | linter PASS после fix H2; объём 8643 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (рекомендация) |

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
| R02 | ✓ | Wordstat, Webmaster, web.dev — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; CWV по web.dev |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×1, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения Wordstat MCP названы честно |
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

- total: 7, failed: 0
- OK: search.google.com, wordstat.yandex.ru, webmaster.yandex.ru, web.dev, /geo-optimizaciya-sajta-2026/, /, kv-ai.ru
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 87.1 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (4 extracted, 1 verified in fact-bank, 3 unverified — ориентиры объёма/CWV, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS
- metrics: 8 numbered steps, 5 H2, 7 FAQ h3, 2 tables, 3 blockquotes
- see `utility-gate-report.json`

## Fix cycle

- cycle 1: html-linter FAIL — duplicate FAQ H2 («Добавьте FAQ и schema…» + «Частые вопросы»). Минимальный fix: переименован H2 → «Добавьте schema и блок вопросов для выдачи и AI».
- cycle 2: повтор GEO QA — все скрипты PASS.

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover-агент)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
