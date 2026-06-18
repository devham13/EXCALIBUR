# QA: B01 primer-seo-stati

date: 2026-06-18
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внешние ссылки Вордстат/Webmaster — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица SEO vs GEO, 8 шагов ol, 7 FAQ, island test |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 85.7 |
| Fact safety | 15 | 13 | fact-check PASS; 4/5 чисел не в fact-bank (ориентиры объёма, Princeton 2024 — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, объём 8594 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Maya AI |
| C04 | ✓ | SEO, GEO, llms.txt, JSON-LD объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Outline: SEO+GEO → структура/8 шагов → schema → чеклист → next → FAQ |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (8 шагов), ul (чеклист 14), table, blockquote |
| R01 | ✓ | TL;DR + схема workflow + Fact Check blockquote |
| R02 | ✓ | Wordstat, Webmaster, Text.ru, Princeton GEO-bench — с контекстом |
| R03 | ✓ | Нет выдуманных %; «+140%» только как антипример в чеклисте |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo страницы |
| E02 | ✓ | «Делайте / Не делайте» в ключевых H2 |
| E03 | ✓ | CTA Make ×2, author ×1 — в лимите ≤3 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Wordstat MCP недоступен, llms.txt optional |
| Ept02 | ✓ | Все 5 ссылок HTTP 200 (kv-ai.ru, wordstat, webmaster) |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, kv-ai.ru/obuchenie-po-make, kv-ai.ru/, kv-ai.ru/artur-horosheff
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/чеклист/blockquote — допустимо)
- Flesch RU: 85.7 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 1 verified in fact-bank, 4 unverified — ориентиры объёма/чанков, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 6`, `h2_sections: 5`, `faq_h3: 10`, `tables: 1`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: H2 «Добавьте FAQ и schema для блога» → «Добавьте JSON-LD разметку для блога» (html-linter: duplicate FAQ heading)
- cycle 2: не потребовался — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести Princeton GEO-bench и ориентиры объёма в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
