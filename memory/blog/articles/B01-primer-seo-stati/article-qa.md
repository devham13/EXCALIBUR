# QA: B01 primer-seo-stati

date: 2026-09-11
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 8 шагов, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 77.5 |
| Fact safety | 15 | 13 | fact-check PASS; 5/6 чисел не в fact-bank (ориентиры объёма/lead — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, объём 9224 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer; «в этой статье» только как антипример |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, JSON-LD объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline: SEO+GEO → семантика → каркас → текст → мета → чеклист |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (8 шагов), ul (чеклист 18), table |
| R01 | ✓ | TL;DR + workflow blockquote + citation-ready H2 |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Директ — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; «+140%» только как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru/obuchenie-po-make ×2, artur-horosheff ×1 |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения Wordstat и объёма названы честно |
| Ept02 | ✓ | Internal link `/` (главная блога) + внешние первоисточники |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, `/` (internal), kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff, direct.yandex.ru (SEO-текст)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист/blockquote — допустимо)
- Flesch RU: 77.5 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 1 verified in fact-bank, 5 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- WARN: «в этой статье вы узнаете» — в тексте как антипример, не blocker

## Fix cycle

- cycle 1: GEO QA — H2 «Настройте FAQ, Title…» → «Настройте Title, Description и schema» (html-linter duplicate FAQ rule)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover-агент)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
