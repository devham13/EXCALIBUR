# QA: B01 primer-seo-stati

date: 2026-08-26
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «как писать seo статьи», FAQ 7, чек-лист 15 пунктов — OK |
| GEO / citability | 25 | 24 | TL;DR, таблица SEO vs GEO, workflow 8 шагов, FAQ 7, answer-first H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 79.1 |
| Fact safety | 15 | 13 | fact-check PASS; 2/5 чисел в fact-bank (2026, 350-500 lead); ориентиры объёма — допустимо |
| Contract HTML | 10 | 8 | linter PASS, объём 8562 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer; «в этой статье вы узнаете» только как антипример |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (переименован FAQ-H2 для linter) |
| O02 | ✓ | Outline: SEO+GEO → структура → schema/GEO → чеклист → next |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (8 шагов), ul (чеклист 15), table, 3 blockquote |
| R01 | ✓ | TL;DR + таблица SEO/GEO + workflow blockquote + Fact Check |
| R02 | ✓ | Wordstat, Webmaster, Яндекс Direct — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; «+140%» только как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo (режим B) |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai ×2 + author ×1 (≤3) |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Wordstat MCP недоступен — честно в Fact Check |
| Ept02 | ✓ | Все 6 ссылок HTTP 200 |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, /geo-optimizaciya-sajta-2026/, kv-ai.ru/obuchenie-po-make, / (×2), kv-ai.ru/artur-horosheff
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблица/чеклист — допустимо)
- Flesch RU: 79.1 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 2 verified in fact-bank, 3 unverified — ориентиры объёма/Description, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 6`, `h2_sections: 5`, `faq_h3: 7`, `tables: 1`)
- WARN: water phrase «в этой статье вы узнаете» — антипример в шаге 4, не blocker
- topic: PASS (research phase, utility-gate-topic.json)

## Fix cycle

- cycle 1: GEO QA — H2 «Настройте FAQ, schema и GEO-слой» → «Настройте schema и GEO-слой» (html-linter duplicate FAQ detection)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- подключить Wordstat MCP и дополнить показы в Fact Check

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
