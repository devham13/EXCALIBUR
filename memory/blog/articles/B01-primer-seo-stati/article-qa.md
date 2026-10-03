# QA: B01 primer-seo-stati

date: 2026-10-03
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ-структура, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 6 шагов, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 76.9 |
| Fact safety | 15 | 13 | fact-check PASS; 3 числа не в fact-bank (ориентиры объёма — допустимо) |
| Contract HTML | 10 | 7 | linter PASS, объём 9053 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt (рекомендация контракта) |

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
| O04 | ✓ | ol (6 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Яндекс Direct, Webmaster, Вордстат — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; дата Google FAQ rich results — с контекстом |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo B01 |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×2 + внутренняя / — без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно |
| Ept02 | ✓ | Internal + external links по карточке темы |

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

- total: 8, failed: 0
- internal: `/` (site-base из PUBLIC_SITE_URL)
- external: direct.yandex.ru, wordstat, webmaster, yandex support (×2), kv-ai.ru (×2)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 76.9 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 3 verified in fact-bank, 3 unverified — ориентиры объёма/lead)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir scan)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS
- water_hits: [] (после правки шага 5 в ol)
- see `utility-gate-report.json`

## Fix cycle (GEO QA)

- cycle 1: H2 «Настройте FAQ…» → «Согласуйте HTML с JSON-LD для schema» (html-linter duplicate FAQ)
- cycle 1: убрана дословная water-фраза в ol (utility gate warning)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (роль cover после QA)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
