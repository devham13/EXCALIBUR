# QA: B01 primer-seo-stati

date: 2026-07-07
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7, чеклист 15 п. — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 8 шагов, 7 FAQ, island H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | slop PASS (1 anti-пример в контексте «не делайте»), Flesch RU 78.1 |
| Fact safety | 15 | 13 | fact-check PASS; 2/7 чисел в fact-bank (ориентиры объёма — допустимо) |
| Contract HTML | 10 | 7 | linter PASS, объём ~8960 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция, контент-маркетинг |
| C04 | ✓ | SEO, GEO, llms.txt, island test — при первом появлении |
| O01 | ✓ | H2 покрывают research-каркас (SEO+GEO, семантика, структура, E-E-A-T, мета/schema, чеклист, FAQ) |
| O02 | ✓ | Логичный outline how_to |
| O03 | ✓ | FAQ 7 пар, queries из faq_hints |
| O04 | ✓ | ol (5+3 шагов), ul (чеклист 15), table |
| R01 | ✓ | TL;DR + таблица SEO/GEO + workflow blockquote + Fact Check |
| R02 | ✓ | Wordstat, Webmaster, гайд Яндекс Директ — с URL |
| R03 | ✓ | Нет неподтверждённых %; переспам — как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow + self-demo longread |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru ×2 (author + Make), без перебора |
| Exp01 | ✓ | Режим B, без fake «я сделал» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 1 slop hit — цитата-антипример (≤1) |
| Ept01 | ✓ | Ограничения: llms.txt опционален, Wordstat вручную |
| Ept02 | ✓ | internal `/` из карточки B01 (1 ссылка по теме) |

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
- OK: wordstat.yandex.ru, webmaster.yandex.ru, direct.yandex.ru (×2), kv-ai.ru/artur-horosheff, kv-ai.ru/obuchenie-po-make, internal `/`
- see `link-verify.json`

## AI-slop scan

- cliches: 1 (антипример «в этой статье мы рассмотрим» в рекомендации «не делайте»)
- over-long sentences (>25 words): 3 (таблица/чеклист — допустимо)
- Flesch RU: 78.1 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 2 verified in fact-bank, 5 unverified — ориентиры объёма/lead, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 8`, `h2_sections: 6`, `faq_h3: 7`, `tables: 1`)
- topic: PASS (research phase, utility_verdict PASS)

## Fix cycle

- cycle 1: GEO QA — H2 «Настройте мета, FAQ и schema» → «Настройте мета-теги и schema» (html-linter duplicate FAQ sections)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- после публикации B02–B05 — добавить 1–2 inbound internal links из indexer

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
