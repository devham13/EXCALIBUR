# QA: B01 primer-seo-stati

date: 2026-08-17
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 5 шагов ol, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 73.5 |
| Fact safety | 15 | 13 | fact-check PASS; 3/6 чисел не в fact-bank (ориентиры объёма — допустимо) |
| Contract HTML | 10 | 7 | linter PASS, объём 9280 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline: SEO+GEO → семантика → структура → schema → чеклист → FAQ |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (5 шагов), ul (чеклист 14 пунктов), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов (TL;DR, таблица, workflow blockquote) |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Директ — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; ориентиры объёма без fake stats |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make.com ×1, internal ×2 — без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно (нет универсального объёма, llms.txt ≠ индексация) |
| Ept02 | ✓ | Internal links 2: `/`, `/blog/geo-optimizaciya-sajta-2026/` — HTTP 200 |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, mayai.ru/blog/geo-optimizaciya-sajta-2026/, mayai.ru/, kv-ai.ru/obuchenie-po-make, direct.yandex.ru (SEO-текст)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 73.5 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 3 verified in fact-bank, 3 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)
- warning: false-positive water phrase «в этой статье вы узнаете» — в article.html отсутствует

## Fix cycle

- cycle 1: GEO QA — переименован H2 «Добавьте FAQ и schema…» → «Настройте schema и блок вопросов…» (html-linter duplicate FAQ false positive)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover-агент после PASS)
- занести ориентиры 8 500–9 500 в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
