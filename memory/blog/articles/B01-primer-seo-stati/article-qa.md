# QA: B01 primer-seo-stati

date: 2026-07-11
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренняя ссылка `/` — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 5 шагов ol, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 73 |
| Fact safety | 15 | 12 | fact-check PASS; 7 чисел не в fact-bank (ориентиры объёма/мета — допустимо); 44,2% из research-notes |
| Contract HTML | 10 | 8 | linter PASS, объём 9256 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Maya AI |
| C04 | ✓ | SEO, GEO, RAG объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (workflow 9 шагов) |
| O02 | ✓ | Логичный outline how-to |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (5 шагов), ul (чеклист 18), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Direct — с внешними ссылками |
| R03 | ✓ | 44,2% — в research-notes с URL text.ru; нет выдуманных % |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика «Делайте/Не делайте» в каждой H2 |
| E03 | ✓ | CTA ×2 (курс Make, профиль автора), без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения Wordstat/MCP названы честно |
| Ept02 | ✓ | Internal link `/` из карточки темы B01 — HTTP 200 |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, internal `/`, direct.yandex.ru, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 73.0 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 1 verified in fact-bank, 7 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- verdict: PASS (5 numbered steps, 7 FAQ, 1 table, 35 action markers)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1: GEO QA переименовал H2 «Оформите мета, FAQ и schema…» → «Оформите мета и schema…» (html-linter duplicate FAQ)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- после publish B01 — перелинковка с B04

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
