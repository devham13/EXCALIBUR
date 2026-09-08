# QA: B01 primer-seo-stati

date: 2026-09-08
score_total: 97/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, ol 9 шагов, FAQ 7, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 77.6 |
| Fact safety | 15 | 13 | fact-check PASS; 3/6 чисел в fact-bank (ориентиры объёма/160 — допустимо) |
| Contract HTML | 10 | 10 | html-linter PASS; объём 9368 ✓, CTA ≤3 ✓, TOC нет ✓, один FAQ-H2 ✓ |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass, все скрипты PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Excalibur |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline workflow |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (9 шагов), ul (чеклист 13), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых % и выдуманной статистики |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика «Делайте / Не делайте» в H2 |
| E03 | ✓ | CTA Make + профиль автора — 2 упоминания |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения в Fact Check Box (Wordstat на дату публикации) |
| Ept02 | ✓ | Internal links ×2: `/`, `/blog/geo-optimizaciya-sajta-2026/` — HTTP 200 |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility-gate | PASS | utility-gate-report.json |

## Fix cycle

- cycle 1: **FIX_REQUIRED** — writer переименовал H2 «Добавьте FAQ…» → «Добавьте schema и GEO-упаковку»
- cycle 2: **PASS** — html-linter PASS, все скрипты PASS

## Link verify

- total: 6, failed: 0
- OK: wordstat.yandex.ru, webmaster.yandex.ru, `/`, `/blog/geo-optimizaciya-sajta-2026/`, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо)
- Flesch RU: 77.6 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: PASS (6 extracted, 3 verified in fact-bank, 3 unverified — ориентиры объёма/160, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: PASS (0 issues)
- see `cannibalization-report.json`

## Utility gate

- verdict: PASS (9 numbered steps, 7 H2, 8 FAQ h3, 1 table)
- see `utility-gate-report.json`

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover-агент)

## Schema ready (handoff для schema-агента после PASS)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
