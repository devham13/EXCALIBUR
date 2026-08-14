# QA: B01 primer-seo-stati

date: 2026-08-14
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, чеклист 15 пунктов, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица SEO vs GEO, 9 шагов ol, FAQ 7, атомарные H2 |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за Princeton +30–40% без имени источника в body |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 79.6 |
| Fact safety | 15 | 13 | fact-check PASS; 2/7 чисел в fact-bank (ориентиры объёма/мета — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, объём 8559 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt, JSON-LD объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Outline: SEO+GEO → интент → структура → schema → чеклист → next |
| O03 | ✓ | FAQ 7 пар, queries из research/PAA |
| O04 | ✓ | ol (9 шагов), ul (чеклист 15), table, 3 blockquote |
| R01 | ✓ | TL;DR + схема workflow + Fact Check blockquote |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Direct — с внешними ссылками |
| R03 | ✗ | «+30–40% visibility» (Princeton GEO-bench) без имени источника в абзаце |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo эталон |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×1, без перебора |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Wordstat MCP, универсальной нормы объёма нет |
| Ept02 | ✓ | Все 6 ссылок HTTP 200 (link-verify) |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, direct.yandex.ru (×2), /blog/geo-optimizaciya-sajta-2026/, /, kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 79.6 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 2 verified in fact-bank, 5 unverified — ориентиры объёма/lead/мета, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 9`, `h2_sections: 6`, `faq_h3: 7`, `tables: 1`)
- topic: PASS (research phase, utility_gate_topic)

## Fix cycle

- cycle 1: GEO QA — H2 «Добавьте FAQ и schema для GEO» → «Добавьте schema и Q&A для GEO» (html-linter duplicate FAQ heading)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- уточнить «Princeton GEO-bench +30–40%» явной ссылкой на источник

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
