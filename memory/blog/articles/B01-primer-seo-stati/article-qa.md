# QA: B01 primer-seo-stati

date: 2026-06-18
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние ссылки mayai.ru ×2 — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица SEO vs GEO, 6 шагов, чеклист 15, island test |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 77.8 |
| Fact safety | 15 | 13 | fact-check PASS; 3/10 чисел в fact-bank; 7 unverified — ориентиры объёма/метрик, не blocker |
| Contract HTML | 10 | 8 | linter PASS, объём 9432 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Maya AI / «Ковчег» |
| C04 | ✓ | SEO, GEO, llms.txt, passages — объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (workflow, структура, schema, чеклист, FAQ) |
| O02 | ✓ | Логичный outline: SEO+GEO → семантика → schema → чеклист → next |
| O03 | ✓ | FAQ 7 пар, queries из meta/Wordstat |
| O04 | ✓ | ol (6 шагов), ul (чеклист 15), table SEO vs GEO |
| R01 | ✓ | TL;DR + workflow blockquote + Fact Check blockquote |
| R02 | ✓ | Яндекс Direct SEO-гайд, Wordstat, Webmaster — внешние ссылки |
| R03 | ✓ | Нет неподтверждённых %; цифры — ориентиры с оговорками |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo страницы |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, профиль автора ×2 — ≤3 |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Wordstat auth, llms.txt — ограничения названы |
| Ept02 | ✓ | Internal links 2× mayai.ru/ (HTTP 200) |

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
- OK: direct.yandex.ru, wordstat.yandex.ru, webmaster.yandex.ru, mayai.ru/ (×2), kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/чеклист/blockquote — допустимо)
- Flesch RU: 77.8 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (10 extracted, 3 verified in fact-bank, 7 unverified — ориентиры объёма/метрик, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate (article)

- verdict: PASS (6 numbered steps, 5 H2, 7 FAQ h3, 1 table, 3 blockquotes, 0 water hits)
- see `utility-gate-report.json`

## Fix cycles

- **cycle 1:** H2 «Настройте FAQ и передайте schema…» → «Настройте разметку schema перед публикацией» (html-linter: duplicate FAQ sections)
- **cycle 2:** шаг 4 lead — «без "в этой статье вы узнаете"» → «без шаблонного «здесь вы узнаете…»» (utility gate water warning)
- **cycle 3:** повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover-агент)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
