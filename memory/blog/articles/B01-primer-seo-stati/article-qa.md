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
| SEO structure | 20 | 20 | H2/H3, primary query «как писать seo статьи», FAQ 7, чек-лист 15 пунктов — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица SEO vs GEO, 7+5 шагов, 7 FAQ, island test в тексте |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 81.6, практичный тон |
| Fact safety | 15 | 13 | fact-check PASS; 4/8 чисел в fact-bank (ориентиры объёма/мета — из research-notes, не blocker) |
| Contract HTML | 10 | 7 | linter PASS, объём 8624 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (5 секций + FAQ) |
| O02 | ✓ | Outline: SEO+GEO → longread → schema → чеклист → next |
| O03 | ✓ | FAQ 7 пар, queries из research/карточки B01 |
| O04 | ✓ | ol (7+5 шагов), ul (чеклист 15), table, 3 blockquote |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов (H2, TL;DR, FAQ) |
| R02 | ✓ | Wordstat, Webmaster, kv-ai.ru — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; ориентиры объёма с оговоркой |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (эталон формата) |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, профиль Артура ×1, главная ×1 |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: llms.txt опционален, объём по SERP |
| Ept02 | ✓ | Все 6 ссылок HTTP 200 (internal + external) |

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

- total: 6, failed: 0
- OK: wordstat.yandex.ru, webmaster.yandex.ru, / (главная), /geo-optimizaciya-sajta-2026/, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 81.6 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 4 verified in fact-bank, 4 unverified — ориентиры объёма/мета из research, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 12`, `h2_sections: 5`, `faq_h3: 8`, `tables: 1`)
- topic: PASS (research phase, utility_verdict в research-notes.md)

## Fix cycle

- cycle 1: GEO QA — H2 «3. Настройте FAQ и schema для блога» → «3. Настройте schema и разметку для блога» (html-linter: duplicate FAQ sections)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover-агент)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
