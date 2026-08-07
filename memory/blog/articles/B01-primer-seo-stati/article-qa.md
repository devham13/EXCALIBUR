# QA: B01 primer-seo-stati

date: 2026-08-07
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внутренние ссылки mayai.ru — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, ol 9 шагов, FAQ 7, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 91.4 |
| Fact safety | 15 | 13 | fact-check PASS; 6/8 чисел — ориентиры объёма из research, не blocker |
| Contract HTML | 10 | 8 | linter PASS, объём 8527 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline: SEO+GEO → интент → семантика → текст → мета → чеклист → ритм |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (9 шагов), ul (чеклист 18), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Яндекс Direct, Google, arxiv — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; «+140%» только как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make.com ×1, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно (Wordstat MCP, универсальный объём) |
| Ept02 | ✓ | mayai.ru/ и geo-optimizaciya-sajta-2026/ — HTTP 200 |

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

- total: 8, failed: 0
- OK: wordstat.yandex.ru, direct.yandex.ru, developers.google.com, arxiv.org, mayai.ru/ (×2), mayai.ru/geo-optimizaciya-sajta-2026/, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 91.4 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 2 verified in fact-bank, 6 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 9`, `h2_sections: 7`, `faq_h3: 7`, `tables: 1`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — H2 «5. Настройте FAQ, мета и schema» → «5. Настройте мета и schema» (html-linter duplicate FAQ heading)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- обновить char_count в article.meta.json (8527 vs 8564)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
