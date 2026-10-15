# QA: B01 primer-seo-stati

date: 2026-08-16
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 6 пар, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 9 шагов, TL;DR, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | slop PASS (1 hit — антипример в тексте), Flesch RU 80.7 |
| Fact safety | 15 | 13 | fact-check PASS; 6/8 чисел не в fact-bank (ориентиры объёма — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, объём 8519 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Maya AI |
| C04 | ✓ | SEO, GEO, BLUF, LSI объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (9 шагов + FAQ) |
| O02 | ✓ | Логичный outline workflow → чеклист → FAQ |
| O03 | ✓ | FAQ 6 пар, queries из research |
| O04 | ✓ | ol (9 шагов), ul (чеклист 11), table |
| R01 | ✓ | ≥3 standalone блоков (TL;DR, таблица, Fact Check) |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Direct — с URL |
| R03 | ✓ | Нет неподтверждённых %; «+140%» только как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo B01 |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make.com ×1, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 1 slop hit — цитата запрета «в этой статье мы рассмотрим» |
| Ept01 | ✓ | Ограничения в Fact Check Box (Wordstat API) |
| Ept02 | ✓ | Internal links: /, /blog/geo-optimizaciya-sajta-2026/ — HTTP 200 |

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

- total: 6, failed: 0
- OK: wordstat.yandex.ru, webmaster.yandex.ru, mayai.ru/, mayai.ru/blog/geo-optimizaciya-sajta-2026/, direct.yandex.ru (SEO-текст), kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## AI-slop scan

- cliches: 1 (антипример «без "в этой статье мы рассмотрим"» — не blocker)
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо)
- Flesch RU: 80.7 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 2 verified in fact-bank, 6 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 6`, `h2_sections: 5`, `faq_h3: 6`, `tables: 1`, `action_markers: 20`)
- warning: water phrase «в этой статье вы узнаете» — ложное срабатывание на антипример в шаге 5
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — H2 «…атомарные H2 и FAQ» → «…атомарные H2 и чанки для AI» (html-linter duplicate FAQ)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
