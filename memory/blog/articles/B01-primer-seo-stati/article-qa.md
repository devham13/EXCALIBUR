# QA: B01 primer-seo-stati

date: 2026-10-15
score_total: 93/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ×7, внутренние/внешние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, ol×6, FAQ, island test |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 80.9 |
| Fact safety | 15 | 12 | fact-check PASS; 3 числа вне fact-bank (объём/Description — ориентиры) |
| Contract HTML | 10 | 7 | linter PASS, char_count 8535 ✓; −3 нет `<img>` с alt (рекомендация контракта) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, JSON-LD, llms.txt объяснены |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (6), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Яндекс Директ, Google SC — с ссылками |
| R03 | ✓ | Нет выдуманных %; даты с оговорками |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA Make ×1, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения (Вордstat) названы |
| Ept02 | ✓ | Все 6 ссылок HTTP 200 |

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

- total: 6, failed: 0
- OK: wordstat.yandex.ru, example.com/, direct.yandex.ru, developers.google.com, mayai.ru/geo-optimizaciya-sajta-2026/, kv-ai.ru/obuchenie-po-make
- fix (GEO QA): `/blog/geo-optimizaciya-sajta-2026/` → `https://mayai.ru/geo-optimizaciya-sajta-2026/`
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/чеклист — допустимо)
- Flesch RU: 80.9 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 3 verified, 3 unverified — ориентиры объёма/мета)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, blog-dir scan)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS (article metrics: ol×6, h2×5, faq_h3×7+1 body, table×1)
- see `utility-gate-report.json`

## Fix cycle (GEO QA)

1. link-verify fail: phantom internal `/blog/geo-…` на example.com → абсолютный URL mayai.ru (200)
2. html-linter fail: два H2 с «FAQ» → переименован H2 «Добавьте schema JSON-LD и видимый блок вопросов»
3. повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- при publish перепроверить link-verify с `--site-base` из `PUBLIC_SITE_URL`

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | author_id: artur-horoshev
