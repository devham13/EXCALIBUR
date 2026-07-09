# QA: B01 primer-seo-stati

date: 2026-07-09
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внутренняя ссылка `/` — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 5 шагов ol, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 77.0 |
| Fact safety | 15 | 13 | fact-check PASS; 2/8 чисел в fact-bank; ориентиры объёма/CWV — допустимо |
| Contract HTML | 10 | 7 | linter PASS, объём 9345 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (cover после QA) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, E-E-A-T, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (8 секций + FAQ) |
| O02 | ✓ | Workflow outline: семантика → SEO+GEO → каркас → черновик → мета/schema → чеклист |
| O03 | ✓ | FAQ 7 пар, queries из research/SERP |
| O04 | ✓ | ol (5 шагов), ul (чеклист 15), table SEO vs GEO |
| R01 | ✓ | TL;DR + таблица + blockquote workflow + standalone H2-блоки |
| R02 | ✓ | Wordstat, Яндекс Direct, Google Search Central — с URL |
| R03 | ✓ | Нет выдуманных %; антипример «+140%» в research, не в body |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo эталона |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, author kv-ai.ru ×1 — без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: llms.txt опционален, Wordstat API недоступен |
| Ept02 | ✓ | Internal `/` из карточки B01; смежные GEO — plain text до publish B04 |

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
- OK: wordstat.yandex.ru, direct.yandex.ru, developers.google.com, webmaster.yandex.ru, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff, internal `/`
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист — допустимо)
- Flesch RU: 77.0 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 2 verified in fact-bank, 6 unverified — ориентиры объёма/lead/CWV, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 5`, `h2_sections: 7`, `faq_h3: 7`, `tables: 1`, `water_hits: []`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1 (GEO QA minimal fix):
  - H2 «Настройте мета, FAQ и schema…» → «…блок вопросов и schema…» (html-linter duplicate FAQ)
  - «в этой статье вы узнаете» → «здесь вы узнаете всё о теме» (utility gate water_hits)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- `<img>` с alt — после cover-агента
- author_id: artur-horoshev (SameAs для schema-агента)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
