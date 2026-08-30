# QA: B01 primer-seo-stati

date: 2026-08-30
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, чеклист 15 пунктов, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | TL;DR answer-first, таблица SEO vs GEO, workflow 9 шагов, FAQ 7, island test |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 83.4 |
| Fact safety | 15 | 13 | fact-check PASS; 4/5 чисел не в fact-bank (ориентиры объёма — допустимо) |
| Contract HTML | 10 | 7 | linter PASS, объём 8613 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, контент-редакция |
| C04 | ✓ | SEO, GEO, RAG, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (6 секций + FAQ) |
| O02 | ✓ | Outline: SEO+GEO → workflow → структура → schema → чеклист → next |
| O03 | ✓ | FAQ 7 пар, queries из research/SERP |
| O04 | ✓ | ol (9 шагов), ul (чеклист 15), 2 table, 3 blockquote |
| R01 | ✓ | TL;DR + схема workflow + Fact Check blockquote |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Direct, Google SEO guide — с URL |
| R03 | ✓ | Нет выдуманной статистики; объёмы — ориентиры с оговоркой |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (формат B) |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, internal links ×2 (geo-landing, главная) |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: llms.txt опционален, объём по SERP |
| Ept02 | ✓ | Все href HTTP 200 (mayai.ru, kv-ai.ru, wordstat, webmaster, yandex, google) |

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

- total: 7, failed: 0
- OK: wordstat.yandex.ru, webmaster.yandex.ru, mayai.ru/geo-optimizaciya-sajta-2026/, mayai.ru/, kv-ai.ru/obuchenie-po-make, direct.yandex.ru, developers.google.com
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблицы/blockquote — допустимо)
- Flesch RU: 83.4 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 1 verified in fact-bank, 4 unverified — ориентиры объёма, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 9`, `h2_sections: 6`, `faq_h3: 7`, `tables: 2`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — переименован H2 «Добавьте FAQ и schema…» → «Добавьте schema: BlogPosting и блок вопросов» (html-linter: duplicate FAQ heading)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести ориентиры объёма (8500–9500) в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
