# QA: B01 primer-seo-stati

date: 2026-08-09
score_total: 96/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ-структура, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 9 шагов, 7 FAQ, answer capsules после H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | slop PASS; Flesch RU 74.4 |
| Fact safety | 15 | 13 | fact-check PASS; 5 чисел не в fact-bank (ориентиры объёма/lead — допустимо) |
| Contract HTML | 10 | 9 | linter PASS, CTA ≤3 ✓; −1 нет `<img>` с alt (рекомендация контракта) |

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
| O04 | ✓ | ol (9 шагов), ul (чеклист 17), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Вордстат, Webmaster, Google SC — упомянуты с контекстом |
| R03 | ✓ | Нет неподтверждённых %; «+140%» только как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA курс Make + internal / — без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | slop PASS (1 anti-example cliche) |
| Ept01 | ✓ | Ограничения названы честно |
| Ept02 | ✓ | CTA kv-ai.ru + internal / — HTTP 200 |

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

- total: 2, failed: 0
- OK: kv-ai.ru/obuchenie-po-make, internal /
- see `link-verify.json`

## AI-slop scan

- cliches: 1 (anti-example «в этой статье мы рассмотрим»)
- over-long sentences (>25 words): 4 (таблица/чеклист — допустимо)
- Flesch RU: 74.4 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 2 verified in fact-bank, 5 unverified — ориентиры объёма/lead)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS (9 numbered steps, 6 H2, 7 FAQ, 1 table, 20 action markers)
- see `utility-gate-report.json`

## Fix cycle (GEO QA)

- cycle 1: переименован H2 «Настройте FAQ…» → «Настройте блок вопросов…» (duplicate FAQ lint)
- cycle 1: удалены `<pre><code>` — заменены на `<p>` (whitelist lint)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- char_count body: 9887 (чуть выше writer target 8500–9500; utility gate PASS)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | author_id: artur-horoshev
