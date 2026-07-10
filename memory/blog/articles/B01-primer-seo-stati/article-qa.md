# QA: B01 primer-seo-stati

date: 2026-07-10
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внутренняя ссылка `/` — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица SEO vs GEO, 7 FAQ, атомарные H2, blockquote workflow |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 84.4 |
| Fact safety | 15 | 13 | fact-check PASS; 1/7 в fact-bank; 6 unverified — ориентиры объёма/lead из research, не blocker |
| Contract HTML | 10 | 8 | linter PASS, объём 8770 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция B2B |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (7 секций + FAQ + next) |
| O02 | ✓ | Логичный outline: SEO+GEO → семантика → черновик → мета → перелинковка → schema → чеклист |
| O03 | ✓ | FAQ 7 пар, queries из research/Wordstat |
| O04 | ✓ | ol (3+16+3 шага), table, 3 blockquote |
| R01 | ✓ | TL;DR + таблица SEO/GEO + Fact Check blockquote |
| R02 | ✓ | Wordstat, Webmaster, Princeton GEO-bench, Ahrefs — с внешними ссылками |
| R03 | ✓ | Цифры с источниками (Princeton, Ahrefs, Яндекс Директ) |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo режима B |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru/obuchenie ×1, author blockquote ×1 — в лимите |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: llms.txt опционален, Wordstat без MCP-цифр |
| Ept02 | ✓ | Все 6 ссылок HTTP 200 (link-verify) |

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
- OK: `/` (internal), wordstat.yandex.ru, webmaster.yandex.ru, search.google.com/test/rich-results, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (lead + таблица — допустимо для PASS slop-detector)
- Flesch RU: 84.4 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 1 verified in fact-bank, 6 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 22`, `h2_sections: 8`, `faq_h3: 7`, `tables: 1`)
- topic: PASS (preflight, research phase)

## Fix cycle

- cycle 1: GEO QA — H2 «Добавьте FAQ, перелинковку…» → «Добавьте перелинковку и GEO-чанки» (html-linter duplicate FAQ)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести ориентиры 60–90 мин, 8 500–9 500 знаков в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
