# QA: B01 primer-seo-stati

date: 2026-07-11
score_total: 96/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 8 шагов, FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 81.9 |
| Fact safety | 15 | 13 | fact-check PASS; 7 чисел — ориентиры объёма (допустимо) |
| Contract HTML | 10 | 9 | linter PASS, объём 8581 ✓, CTA ≤3 ✓; −1 нет `<img>` с alt (рекомендация) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (schema-блок переименован без «FAQ» в заголовке) |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (8 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Директ — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых % |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (режим B) |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA Make ×1, профиль автора ×1 — без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения объёма названы честно |
| Ept02 | ✓ | Internal links `/` ×2 из карточки темы |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility-gate (topic B01 + article) | PASS | utility-gate-report.json |

## Link verify

- total: 6 unique URLs, failed: 0
- OK: wordstat.yandex.ru, webmaster.yandex.ru, direct.yandex.ru, kv-ai.ru (×2), internal `/`
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист/workflow — допустимо для PASS slop-detector)
- Flesch RU: 81.9 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (9 extracted, 2 verified in fact-bank, 7 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- topic B01: PASS
- article: PASS (8 numbered steps, 1 table, 3 blockquotes; WARN: water phrase «в этой статье вы узнаете» — антипример в шаге 4, не blocker)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1: GEO QA переименовал H2 «Настройте FAQ и schema» → «Настройте schema и блок вопросов» (html-linter duplicate FAQ FAIL → PASS)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover после schema-агента)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
