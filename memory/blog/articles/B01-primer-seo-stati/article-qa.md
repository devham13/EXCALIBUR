# QA: B01 primer-seo-stati

date: 2026-10-13
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ-структура, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, workflow 7 шагов, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 78.4 |
| Fact safety | 15 | 13 | fact-check PASS; 6 чисел не в fact-bank (ориентиры/даты — допустимо) |
| Contract HTML | 10 | 7 | linter PASS, объём ~9005 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (рекомендация контракта) |

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
| O04 | ✓ | ol (7 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster, mayai/kv-ai — с ссылками |
| R03 | ✓ | Нет неподтверждённых %; оговорки по Wordstat без API |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA kv-ai ×2, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно |
| Ept02 | ✓ | Все 6 ссылок HTTP 200 (link-verify) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | pass | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- internal: `/blog/geo-optimizaciya-sajta-2026/` — OK
- external: wordstat, webmaster, kv-ai (×2), mayai.ru — OK
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5
- Flesch RU: 78.4 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (9 extracted, 3 verified in fact-bank, 6 unverified — ориентиры, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS (numbered_list_items 7, h2_sections 7, faq_h3 8, tables 1)
- see `utility-gate-report.json`

## Fix cycle (GEO QA)

- cycle 1: H2 «Настройте мета, FAQ и schema» → «Настройте мета-теги и schema» (html-linter duplicate FAQ heading)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту writer/cover

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
