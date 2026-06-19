# QA: B01 primer-seo-stati

date: 2026-06-19 (GEO QA cycle 1)
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 6 шагов, атомарные H2, TL;DR |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 79.5 |
| Fact safety | 15 | 13 | fact-check PASS; 6 чисел не в fact-bank (ориентиры объёма — допустимо) |
| Contract HTML | 10 | 7 | linter PASS, объём ~8510 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (cover на шаге ④a) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Maya AI |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (6 шагов), ul (чеклист 15 п.), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Direct — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; «+140%» только как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA Make ×1, internal `/` ×3 — без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно (нет топ-1, объём по SERP) |
| Ept02 | ✓ | Internal `/` + mayai.ru/geo-… (200), link-verify pass |

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
- OK: `/`, mayai.ru/geo-optimizaciya-sajta-2026/, wordstat.yandex.ru, webmaster.yandex.ru, direct.yandex.ru, kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо)
- Flesch RU: 79.5 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (10 extracted, 4 verified in fact-bank, 6 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate (article)

- verdict: PASS
- warn: «в этой статье вы узнаете» — в контексте «не делайте» (не blocker)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (GEO QA): `/geo-optimizaciya-sajta-2026/` → `https://mayai.ru/geo-optimizaciya-sajta-2026/` (404 на PUBLIC_SITE_URL); H2 «Настройте FAQ и schema…» → «Настройте schema…» (duplicate FAQ linter)
- cycle 2: повтор QA — **PASS**

## Optional (не blocker)

- `<img>` с alt — на шаге cover (④a)
- blockquote «верифицированы по Вордстат» — editorial claim; Wordstat MCP недоступен в research (см. handoff)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
