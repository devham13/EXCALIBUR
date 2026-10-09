# QA: B01 primer-seo-stati

date: 2026-10-09
score_total: 93/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 8 шагов, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 82.8 |
| Fact safety | 15 | 12 | fact-check PASS; 6 чисел не в fact-bank (ориентиры объёма — допустимо) |
| Contract HTML | 10 | 7 | linter PASS, объём ~8513 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (рекомендация контракта) |

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
| R02 | ✓ | Вордстат, Яндекс Direct — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; ориентиры объёма без выдуманных частот |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, режим B |
| E02 | ✓ | Практика «делайте / не делайте» в секциях |
| E03 | ✓ | CTA умеренно (Make, профиль автора) |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения (объём, Wordstat MCP) названы честно |
| Ept02 | ✓ | Внутренние: главная + mayai.ru/geo-…; внешние первоисточники |

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

- total: 6, failed: 0
- OK: wordstat.yandex.ru, direct.yandex.ru (×2 в тексте), mayai.ru/geo-optimizaciya-sajta-2026/, kv-ai.ru (×2), internal `/` (site-base)
- fix applied (GEO QA): `/geo-optimizaciya-sajta-2026/` → `https://mayai.ru/geo-optimizaciya-sajta-2026/` (404 на PUBLIC_SITE_BASE для относительного пути)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4
- Flesch RU: 82.8 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 2 verified in fact-bank, 6 unverified — ориентиры объёма/lead)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Fix cycle (GEO QA)

- cycle 1: H2 «…FAQ и schema…» → «…вопросы-ответы и schema…» (html-linter duplicate FAQ heading)
- cycle 1: internal geo slug → absolute mayai.ru URL (link-verify)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover после QA)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | author_id: artur-horoshev
