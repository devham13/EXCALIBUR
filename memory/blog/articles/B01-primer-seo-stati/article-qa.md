# QA: B01 primer-seo-stati

date: 2026-10-02 (GEO QA после fix H2 duplicate FAQ)
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, внутренняя ссылка — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, ol 7 шагов, FAQ, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 14 | 0 AI-slop hits; slop script WARNING только по длинным предложениям в таблице/чеклисте |
| Fact safety | 15 | 13 | fact-check PASS; 2 числа объёма не в fact-bank (редакционный ориентир — допустимо) |
| Contract HTML | 10 | 8 | linter PASS, char_count 9335 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt (рекомендация) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция Maya AI |
| C04 | ✓ | SEO, GEO, llms.txt объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом (FAQ-секция переименована для linter) |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (7 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Wordstat, Яндекс Direct — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых % трафика |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | Практика «Делайте / Не делайте» в секциях |
| E03 | ✓ | CTA Make 1×, internal / |
| Exp01 | ✓ | Режим B, блок эксперта без fake кейсов |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения объёма названы честно |
| Ept02 | ✓ | Все 4 ссылки HTTP 200 (link-verify pass) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING (0 cliches) | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility-gate | PASS | utility-gate-report.json |

## Link verify

- total: 4, failed: 0
- OK: wordstat.yandex.ru, direct.yandex.ru (SEO-текст), internal /, kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## Fix cycle

- cycle 1 (GEO QA): H2 «Добавьте FAQ и schema» → «Подключите schema после текста» (duplicate FAQ h2 rule)
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- синхронизировать author_id в schema-handoff (meta: artur-horoshev)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | Author: artur-horoshev (из article.meta.json)
