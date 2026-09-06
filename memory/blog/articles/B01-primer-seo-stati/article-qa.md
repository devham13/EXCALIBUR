# QA: B01 primer-seo-stati

date: 2026-09-06
score_total: 96/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внутренние / и B04 — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 7 шагов ol, workflow blockquote, FAQ 7 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 77 |
| Fact safety | 15 | 13 | fact-check PASS; 8/10 чисел — ориентиры объёма/lead, не blocker |
| Contract HTML | 10 | 9 | linter PASS, объём 9367 ✓, CTA ≤3 ✓; −1 нет `<img>` с alt (cover на 4a) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (7 шагов workflow) |
| O02 | ✓ | Логичный outline: семантика → текст → schema → чеклист → next steps |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (7 шагов), ul (чеклист 12), table SEO vs GEO |
| R01 | ✓ | TL;DR + workflow blockquote + Fact Check Box |
| R02 | ✓ | Wordstat, Яндекс Direct, arXiv:2311.09735 — с внешними ссылками |
| R03 | ✓ | «40% visibility» только с arXiv; «+140%» как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo longread |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×2, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения Wordstat API названы честно |
| Ept02 | ✓ | Все 5 ссылок HTTP 200 (link-verify pass) |

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

- total: 5, failed: 0
- OK: wordstat.yandex.ru, direct.yandex.ru, kv-ai.ru/obuchenie-po-make, internal /, internal /geo-optimizaciya-sajta-2026/
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо)
- Flesch RU: 77.0 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (10 extracted, 2 verified in fact-bank, 8 unverified — ориентиры объёма/lead)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS
- WARN: water phrase «в этой статье вы узнаете» — false positive (фраза в anti-example в шаге 5 ol)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1: html-linter FAIL — duplicate FAQ H2 («4. Настройте FAQ…» + «Частые вопросы»); переименован H2 → «4. Настройте schema и llms.txt»; повтор QA — PASS

## Optional (не blocker)

- `<img>` с alt — cover на шаге 4a
- utility gate water_hits — игнорировать (anti-example контекст)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
