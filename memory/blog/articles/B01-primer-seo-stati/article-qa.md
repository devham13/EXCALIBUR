# QA: B01 primer-seo-stati

date: 2026-08-27
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 8 шагов, FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 76.7 |
| Fact safety | 15 | 13 | fact-check PASS; 3 числа не в fact-bank (ориентиры объёма/Description — допустимо) |
| Contract HTML | 10 | 7 | linter PASS после QA-fix H2; объём body 8 976 ✓, CTA 3 ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 покрывают research action-outline (8 шагов + FAQ) |
| O02 | ✓ | Логичный outline workflow |
| O03 | ✓ | FAQ 7 пар, вопросы из faq_hints + SERP |
| O04 | ✓ | ol (8 шагов), ul (чеклист 14), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster, Google SC, Яндекс Direct — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; «+140%» только как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (режим B) |
| E02 | ✓ | «Делайте / не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×3 — в пределах лимита |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Wordstat MCP недоступен — честно в Fact Check Box |
| Ept02 | ✓ | Internal `/` из карточки темы; внешние первоисточники |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, developers.google.com, direct.yandex.ru, `/` (internal), kv-ai.ru/artur-horosheff, kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 76.7 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (4 extracted, 1 verified in fact-bank, 3 unverified — ориентиры объёма/Description, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- verdict: PASS (8 numbered steps, 10 H2, 7 FAQ, 1 table, 33 action markers, water_hits: [])
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (QA): H2 «Упакуйте материал под GEO: FAQ и schema» → «…schema и атомарные блоки» (duplicate FAQ heading linter fail)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover-агент после PASS)
- обновить cover manifests: h2_anchor «FAQ и schema» → новый заголовок H2 (cover-агент)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
