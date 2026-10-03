# QA: B01 primer-seo-stati

date: 2026-10-03
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, перелинковка hub GEO — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 8 шагов, 7 FAQ, island test |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 14 | 0 AI-slop hits; slop-detector WARNING (8 длинных предложений — таблица/чеклист) |
| Fact safety | 15 | 13 | fact-check PASS; 3 числа не в fact-bank (8500–9500, 2024 llms — из research) |
| Contract HTML | 10 | 8 | linter PASS, объём ~9336 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research action_outline |
| O02 | ✓ | Логичный outline: SEO/GEO → семантика → структура → шаги → schema → чеклист |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (8 шагов), ul (17 checklist), table |
| R01 | ✓ | TL;DR + blockquote, standalone H2-чанки |
| R02 | ✓ | Яндекс Директ, ЭПОС, Wordstat — с URL |
| R03 | ✓ | Нет выдуманных %; объёмы с оговоркой |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, режим B self-demo |
| E02 | ✓ | «Делайте / Не делайте» в ключевых H2 |
| E03 | ✓ | CTA Make ×1, author kv-ai ×1 |
| Exp01 | ✓ | Режим B, editorial без fake case |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop cliché hits |
| Ept01 | ✓ | Wordstat MCP / показы — честная оговорка |
| Ept02 | ✓ | Все href HTTP 200 (hub GEO — absolute mayai.ru) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 7, failed: 0
- OK: wordstat, mayai.ru/geo-optimizaciya-sajta-2026/, direct.yandex, webmaster epos, site root, kv-ai Make, kv-ai author
- fix applied (cycle 1): `/geo-optimizaciya-sajta-2026/` → `https://mayai.ru/geo-optimizaciya-sajta-2026/` (404 на PUBLIC_SITE_URL)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 8 (таблица/чеклист/lead — допустимо, не blocker)
- Flesch RU: 74.1 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 2 verified in fact-bank, 3 unverified — коридор объёма, llms 2024)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- WARN: water detector сработал на фразе «в этой статье вы узнаете» в антипримере чеклиста (не blocker)

## Fix cycle

- cycle 1: GEO QA — absolute URL hub GEO; переименован H2 «Настройте FAQ…» → «Подготовьте schema handoff…» (html-linter duplicate FAQ)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- перед WP publish: при желании вернуть относительный `/geo-optimizaciya-sajta-2026/` если PUBLIC_SITE_URL = mayai.ru

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
