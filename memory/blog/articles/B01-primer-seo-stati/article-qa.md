# QA: B01 primer-seo-stati

date: 2026-08-29
score_total: 97/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, internal links — OK |
| GEO / citability | 25 | 24 | TL;DR, таблица SEO vs GEO, workflow blockquote, 7 FAQ, island test |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 80.1 |
| Fact safety | 15 | 13 | fact-check PASS; 4/7 чисел unverified (ориентиры объёма/мета — допустимо) |
| Contract HTML | 10 | 10 | char_count 8820 ✓, CTA ≤3 ✓, link-verify pass, html-linter PASS |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS, html-linter PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, AEO объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research action_outline (8 шагов) |
| O02 | ✓ | Логичный workflow outline |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (5 шагов), ul (чеклист 12), table, blockquotes |
| R01 | ✓ | TL;DR + workflow + Fact Check blockquote — standalone |
| R02 | ✓ | Wordstat, Webmaster — внешние ссылки |
| R03 | ✓ | Нет выдуманных %; «+140%» только как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (режим B) |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×1, internal / + /geo-optimizaciya-sajta-2026/ |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Wordstat MCP недоступен — честно в Fact Check |
| Ept02 | ✓ | Все 5 ссылок HTTP 200 |

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

- total: 5, failed: 0
- OK: wordstat.yandex.ru, webmaster.yandex.ru, /, /geo-optimizaciya-sajta-2026/, kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист/blockquote — допустимо)
- Flesch RU: 80.1 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 3 verified in fact-bank, 4 unverified — ориентиры объёма/lead/meta, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 5`, `h2_sections: 9`, `faq_h3: 7`, `tables: 1`)
- topic: PASS (research phase)

## Fix cycle

- cycle 1: writer fix H2 §6 (убрано «FAQ» из заголовка) → re-run GEO QA → **PASS**

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
