# QA: B01 primer-seo-stati

date: 2026-08-15
score_total: 96/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ-структура, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 9 шагов, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 81.1 |
| Fact safety | 15 | 13 | fact-check PASS; 5 чисел не в fact-bank (ориентиры объёма — допустимо) |
| Contract HTML | 10 | 9 | linter PASS, объём 8612 ✓, CTA ≤3 ✓; −1 нет `<img>` с alt (рекомендация) |

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
| O04 | ✓ | ol (9 шагов), table, чеклист 18 пунктов |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Яндекс Direct, LikaCloud — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; «+140%» только как антипример в research |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (режим B) |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA Make.com ×2, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно (нет универсального объёма) |
| Ept02 | ✓ | Internal link `/` → mayai.ru (HTTP 200) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate | PASS | utility-gate-report.json |

## Link verify

- total: 7, failed: 0
- OK: wordstat.yandex.ru, direct.yandex.ru (×2), likacloud.com, mayai.ru/, webmaster yandex, kv-ai.ru (×2)
- fix applied: seospravka.ru (connection reset) → direct.yandex.ru meta recommendations

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 1 (таблица SEO vs GEO — допустимо)
- Flesch RU: 81.1 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 2 verified in fact-bank, 5 unverified — ориентиры объёма/lead)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- verdict: PASS
- metrics: 27 numbered steps, 6 H2, 7 FAQ h3, 1 table, 36 action markers, 0 water hits
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (geo-qa): H2 «Оформите мета, FAQ…» → «Оформите мета-теги…» (duplicate FAQ linter); убраны water-фразы из антипримеров; seospravka.ru → Яндекс Direct
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту (cover после publish)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
