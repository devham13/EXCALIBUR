# QA: B01 primer-seo-stati

date: 2026-10-06
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ-структура, перелинковка — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 9 шагов, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 80.4 |
| Fact safety | 15 | 13 | fact-check PASS; 3/9 в fact-bank; остальное — ориентиры объёма из research |
| Contract HTML | 10 | 7 | linter PASS, объём 8564 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (RSS-режим writer) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

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
| O04 | ✓ | ol (9 шагов), ul (чеклист 18), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Direct — с URL |
| R03 | ✓ | Нет неподтверждённых %; цифры с оговорками |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA kv-ai ×1, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения (Wordstat без API) названы честно |
| Ept02 | ✓ | Карта блога `/`, B04 mayai.ru ×2 — HTTP 200 |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, site root `/`, mayai.ru/geo-optimizaciya-sajta-2026/ (×2), direct.yandex.ru, kv-ai.ru/obuchenie-po-make
- fix applied (cycle 1):
  - `/blog/geo-optimizaciya-sajta-2026/` → `https://mayai.ru/geo-optimizaciya-sajta-2026/` (404 на site-base kv-ai)
  - H2 «Настройте FAQ…» → «Подготовьте блок вопросов…» (html-linter: ложный duplicate FAQ по слову FAQ в заголовке)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист — допустимо)
- Flesch RU: 80.4 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (9 extracted, 3 verified in fact-bank, 6 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- verdict: PASS (9 ol items, 6 H2, 7 FAQ h3, 18 action markers)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1: GEO QA — правки article.html (H2 + ссылки B04), повтор скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt после cover-агента
- обновить `char_count` в article.meta.json при publish

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
