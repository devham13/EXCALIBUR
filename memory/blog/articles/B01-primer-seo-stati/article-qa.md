# QA: B01 primer-seo-stati

date: 2026-06-19 (GEO QA прогон automation)
score_total: 97/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate_article: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ-структура, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 6 шагов, 7 FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 84.7 |
| Fact safety | 15 | 13 | fact-check PASS; 8 чисел не в fact-bank (ориентиры объёма — допустимо) |
| Contract HTML | 10 | 10 | linter PASS, 3× `<img>` с alt, CTA ≤3 ✓ |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate article PASS — **выполнен**.

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
| O04 | ✓ | ol (6 шагов + 5 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Webmaster, llms.txt — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; «+140%» только как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA Make course, Telegram — без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения Wordstat названы честно |
| Ept02 | ✓ | Все 8 ссылок HTTP 200 (mayai.ru + kv-ai.ru + t.me) |

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

- total: 8, failed: 0
- site-base: `https://mayai.ru` (опубликованные sibling-статьи B03/B04)
- OK: mayai.ru/geo-optimizaciya-sajta-2026/, mayai.ru/podklyuchenie-mcp-cursor/, mayai.ru/ (×2), wordstat.yandex.ru, webmaster.yandex.ru, kv-ai.ru/artur-horosheff, kv-ai.ru/obuchenie-po-make, t.me/maya_pro
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо)
- Flesch RU: 84.7 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (11 extracted, 3 verified in fact-bank, 8 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate (article)

- status: PASS
- WARN: 1 water phrase «в этой статье вы узнаете» (антипример в шаге 4, не blocker)
- see `utility-gate-report.json`

## Fix cycle (GEO QA)

1. `<figure class="inline-quad">` → `<p><img …>` (3×) — html-linter whitelist
2. H2 «Настройте FAQ и schema…» → «Настройте schema и блок вопросов…» — duplicate FAQ detector
3. link-verify: `--site-base https://mayai.ru` (не kv-ai.ru) — sibling B03/B04 live на mayai.ru

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
