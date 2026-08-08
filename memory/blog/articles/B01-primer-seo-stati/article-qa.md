# QA: B01 primer-seo-stati

date: 2026-08-08
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | TL;DR, таблица SEO vs GEO, 8 шагов ol, 7 FAQ, атомарные H2, island test |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 81.6 |
| Fact safety | 15 | 13 | fact-check PASS; 4/9 чисел в fact-bank; ориентиры объёма/lead — допустимо |
| Contract HTML | 10 | 8 | linter PASS, объём 8541 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Ковчега |
| C04 | ✓ | SEO, GEO, llms.txt, passages — объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (SEO+GEO workflow) |
| O02 | ✓ | Логичный outline: объединение → структура → schema → чеклист → FAQ |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (8 шагов), ul (чеклист 12 пунктов), table |
| R01 | ✓ | ≥3 standalone блоков (TL;DR, таблица, Fact Check Box) |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Direct, Google — с внешними ссылками |
| R03 | ✓ | Нет выдуманных %; ориентиры объёма без fake stats |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO longread, self-demo эталона |
| E02 | ✓ | Практика в каждой H2 (Делайте/Не делайте) |
| E03 | ✓ | CTA kv-ai.ru ×2, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно (нет универсальной нормы объёма) |
| Ept02 | ✓ | Все 7 ссылок HTTP 200 |

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
- OK: `/` (internal), wordstat.yandex.ru, webmaster.yandex.ru, kv-ai.ru/artur-horosheff, kv-ai.ru/obuchenie-po-make, direct.yandex.ru (SEO-текст), developers.google.com (helpful content)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/blockquote/чеклист — допустимо)
- Flesch RU: 81.6 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (9 extracted, 4 verified in fact-bank, 5 unverified — ориентиры объёма/lead/duration, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 1 article in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- WARN: water phrase «в этой статье вы узнаете» — в антипримере шага 4, не blocker
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (GEO QA): html-linter FAIL — duplicate FAQ H2 («Настройте FAQ…» + «Частые вопросы»). Fix: переименован H2 → «Настройте schema и блок вопросов для блога». Повтор — PASS.

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
