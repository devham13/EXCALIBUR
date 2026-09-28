# QA: B01 primer-seo-stati

date: 2026-09-12 (GEO QA после writer refresh)
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ-структура, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 6 шагов, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 84.5 |
| Fact safety | 15 | 13 | fact-check PASS; 3 числа объёма не в fact-bank (ориентиры — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, объём ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация контракта) |

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
| O04 | ✓ | ol (9 шагов), ul (чеклист 18), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Princeton, Seer Interactive — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; корреляция Seer с первоисточником |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×1, без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения названы честно |
| Ept02 | ✓ | Internal links 3: /, mayai.ru/geo, mayai.ru/mcp |

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

- total: 9, failed: 0
- OK: wordstat.yandex.ru, arxiv.org, seerinteractive.com, mayai.ru/geo-optimizaciya-sajta-2026/, mayai.ru/podklyuchenie-mcp-cursor/, kv-ai.ru (×2), direct.yandex.ru, site root /
- fix applied (cycle 1): getllmspy.com (SSL fail) → seerinteractive.com; /blog/* → absolute mayai.ru URLs
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо для PASS slop-detector)
- Flesch RU: 84.5 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 2 verified in fact-bank, 3 unverified — ориентиры объёма, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- verdict: PASS
- water_hits: 0 (после fix «в этой статье вы узнаете»)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (GEO QA): H2 «Добавьте FAQ…» → «Подготовьте видимый блок вопросов…» (duplicate FAQ linter); getllmspy → Seer Interactive; internal links mayai.ru absolute; water phrase rephrase
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
