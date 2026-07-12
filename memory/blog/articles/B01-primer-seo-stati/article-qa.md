# QA: B01 primer-seo-stati

date: 2026-07-12
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица SEO vs GEO, 6 шагов, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 85.8 |
| Fact safety | 15 | 13 | fact-check PASS; 8 чисел, 2 в fact-bank (ориентиры объёма — допустимо) |
| Contract HTML | 10 | 7 | linter PASS, объём 8549 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

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
| O04 | ✓ | ol (6 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Директ — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; Wordstat-цифры не выдуманы |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai ×1, @maya_pro ×1 |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно (Wordstat MCP, llms.txt опционален) |
| Ept02 | ✓ | Internal links: `/`, `/geo-optimizaciya-sajta-2026/` — HTTP 200 |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, direct.yandex.ru, kv-ai.ru/obuchenie-po-make, t.me/maya_pro, internal `/`, `/geo-optimizaciya-sajta-2026/`
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 85.8 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 2 verified in fact-bank, 6 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 6`, `h2_sections: 5`, `faq_h3: 8`, `tables: 1`)
- WARN: false-positive water phrase «в этой статье вы узнаете» (упомянута как антипример в шаге 4, не в тексте lead)
- topic: PASS (research phase, utility-gate-topic.json)

## Fix cycle

- cycle 1: GEO QA — переименован H2 «Настройте FAQ и schema вне body» → «Настройте schema и видимые ответы вне body» (html-linter: duplicate FAQ heading)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести ориентиры объёма (8 500–9 500) в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
