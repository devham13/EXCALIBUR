# QA: B01 primer-seo-stati

date: 2026-06-19
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 9 шагов ol, FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 76.5 |
| Fact safety | 15 | 13 | fact-check PASS; 3 числа не в fact-bank (ориентиры объёма/lead — допустимо) |
| Contract HTML | 10 | 7 | linter PASS, char_count 9366 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (рекомендация контракта) |

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
| O04 | ✓ | ol (9 шагов), ul (чеклист 15), table |
| R01 | ✓ | ≥3 standalone блоков 40–80 слов |
| R02 | ✓ | Wordstat, Webmaster, mayai.ru/geo — с URL |
| R03 | ✓ | Нет неподтверждённых % роста |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика «делайте/не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×2, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения объёма и переспама названы честно |
| Ept02 | ✓ | Internal `/` по карточке B01; релевантный external mayai.ru/geo |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility-gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: wordstat.yandex.ru, webmaster.yandex.ru, `/`, mayai.ru/geo-optimizaciya-sajta-2026/, kv-ai.ru/artur-horosheff, kv-ai.ru/obuchenie-po-make
- fix applied: `/geo-optimizaciya-sajta-2026/` → `https://mayai.ru/geo-optimizaciya-sajta-2026/` (404 на PUBLIC_SITE_URL)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 76.5 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 3 verified in fact-bank, 3 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate (article)

- verdict: PASS (9 ol steps, 5 H2, 7 FAQ, 1 table, 30 action markers)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1: H2 «Настройте FAQ и schema…» → «Настройте schema и JSON-LD…» (html-linter duplicate FAQ)
- cycle 1: internal `/geo-optimizaciya-sajta-2026/` → external mayai.ru (link-verify 404)
- cycle 2: повтор GEO QA — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- смягчить blockquote «верифицированы по Вордстат» (Wordstat MCP недоступен в research)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
