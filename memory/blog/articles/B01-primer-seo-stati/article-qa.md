# QA: B01 primer-seo-stati

date: 2026-06-19
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внутренние ссылки на / (×2) — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 8 шагов, 7 FAQ, атомарные H2, blockquote workflow |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 77.5 |
| Fact safety | 15 | 13 | fact-check PASS; 5 чисел не в fact-bank (ориентиры объёма/мета — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, объём 9424 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer (боль + workflow), без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (SEO+GEO, longread, FAQ/schema, чеклист) |
| O02 | ✓ | Логичный outline + «Что дальше» |
| O03 | ✓ | FAQ 7 пар, реальные queries из карточки темы |
| O04 | ✓ | ol (8 шагов), ul (чеклист 15), table SEO vs GEO |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов (FAQ, H2-чанки) |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Директ — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; ориентиры объёма без выдуманной статистики |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo на B01 |
| E02 | ✓ | «Делайте/Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×3 (курс ×2, профиль ×1), без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы (нет универсального объёма, GEO ≠ замена SEO) |
| Ept02 | ✓ | Internal links 2× на / из карточки темы — HTTP 200 |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- OK: wordstat.yandex.ru, webmaster.yandex.ru, / (×2), direct.yandex.ru (SEO-текст), kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 77.5 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 3 verified in fact-bank, 5 unverified — ориентиры объёма/lead/мета, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS
- metrics: 8 numbered steps, 5 H2, 7 FAQ H3, 1 table, 3 blockquotes, 33 action markers, 0 water hits
- see `utility-gate-report.json`

## Fix cycle

- cycle 0: writer PASS → GEO QA cycle 1 — PASS без правок article.html

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover/inline на этапе cover)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
