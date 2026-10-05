# QA: B01 primer-seo-stati

date: 2026-10-05
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, ol 8 шагов, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица SEO vs GEO, FAQ 7, island test в чек-листе |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 77.3 |
| Fact safety | 15 | 13 | fact-check PASS; 2/4 числа в fact-bank (ориентиры 8500–9500 — из контракта) |
| Contract HTML | 10 | 7 | linter PASS, объём 9469 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без вводных штампов |
| C03 | ✓ | Аудитория: авторы блога, редакция Maya AI |
| C04 | ✓ | SEO, GEO, JSON-LD, llms.txt — при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом writer |
| O02 | ✓ | Логичный outline: сравнение → запрос → текст → Q&A/schema → чек-лист |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (8 шагов), ul (11 пунктов), table, blockquote |
| R01 | ✓ | TL;DR, workflow blockquote, Fact Check blockquote |
| R02 | ✓ | Яндекс Direct, Wordstat, Google helpful content — с URL |
| R03 | ✓ | Нет выдуманных %; переспам только как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo пайплайна |
| E02 | ✓ | «Делайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA Make ×1, author profile ×1 |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Вордstat не в тексте, llms.txt опционален |
| Ept02 | ✓ | mayai.ru B04 + kv-ai.ru CTA/author — HTTP 200 |

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

- total: 8, failed: 0
- fix: `/geo-optimizaciya-sajta-2026/` (404 на site-base) → `https://mayai.ru/geo-optimizaciya-sajta-2026/` (200)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4
- Flesch RU: 77.3 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (4 extracted, 2 verified, 2 unverified — ориентиры объёма)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues across blog-dir)
- see `cannibalization-report.json`

## Fix cycle

- cycle 1 (GEO QA): absolute URL на B04; переименован H2 (убран «FAQ» из заголовка — duplicate FAQ linter); anti-water в шаге 4; лёгкий trim объёма
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- обновить `char_count` в `article.meta.json` после правок (9469 plain)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | author_id: artur-horoshev
