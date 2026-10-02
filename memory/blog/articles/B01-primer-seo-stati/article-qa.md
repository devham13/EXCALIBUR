# QA: B01 primer-seo-stati

date: 2026-10-02
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, workflow, 9 шагов, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 14 | 0 AI-slop hits; Flesch RU 82.3; slop WARNING — 6 длинных предложений (таблица/чеклист) |
| Fact safety | 15 | 13 | fact-check PASS; 3 числа вне fact-bank (ориентиры объёма — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, объём 8734 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

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
| O04 | ✓ | ol (9 шагов), ul (чеклист 15), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Яндекс Direct, Wordstat — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых % |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×2, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения (Вордстат MCP) названы честно |
| Ept02 | ✓ | Internal: главная + mayai.ru/geo-optimizaciya-sajta-2026 |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING (0 cliches) | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility-gate | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- fix applied (GEO QA): `/blog/geo-optimizaciya-sajta-2026/` → absolute `https://mayai.ru/geo-optimizaciya-sajta-2026/`; H2 «Настройте FAQ…» → «Настройте разметку schema…» (duplicate FAQ linter)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (таблица/чеклист — допустимо)
- Flesch RU: 82.3 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 2 verified in fact-bank, 3 unverified — ориентиры объёма, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, blog-dir scan)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS (article gate PASS, water_hits: 0 после fix формулировки в шаге 4)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (GEO QA): linter duplicate FAQ + link 404 + water phrase в шаге 4 — правки в `article.html`
- cycle 2: все скрипты PASS/WARNING (slop) — **PASS**

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | author_id: artur-horoshev
