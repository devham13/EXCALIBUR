# QA: B01 primer-seo-stati

date: 2026-10-02
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2/H3, primary query, FAQ 7 пар, один блок «Частые вопросы» — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 9 шагов, TL;DR blockquote |
| CORE-EEAT lite | 15 | 14 | 19/20 (Ept02: одна внутренняя ссылка `/`, рекомендация 2–3) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 76.7 |
| Fact safety | 15 | 14 | fact-check PASS; 3 числа вне fact-bank (коридор объёма, антипример 3000) |
| Contract HTML | 10 | 7 | linter PASS после fix H2; ~9017 знаков ✓; −2 нет `<img>` с alt; −1 одна internal |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, schema объяснены при первом появлении |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol (9 шагов), ul (чеклист), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Яндекс Direct, SERP — с внешними ссылками |
| R03 | ✓ | Нет неподтверждённых %; «3000» как антипример |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA kv-ai.ru уместны |
| Exp01 | ✓ | Режим B |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения (Вордstat, robots) названы |
| Ept02 | ✗ | 1 relative internal (`/`), цель 2–3 по карточке темы |

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

- total: 4, failed: 0
- external: direct.yandex.ru (×2), kv-ai.ru (×2)
- internal relative: `/` (HTTP 200)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4
- Flesch RU: 76.7 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 3 verified, 3 unverified — ориентиры объёма, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS (numbered_list_items 9, faq_h3 7, action_markers 29)
- see `utility-gate-report.json`

## Fix cycle (GEO QA)

- cycle 1: переименован H2 «Добавьте FAQ и schema…» → «Добавьте schema и видимый блок…» (html-linter duplicate FAQ headings)
- повтор прогона скриптов — PASS

## Optional (не blocker)

- добавить 1–2 internal links и `<img>` с alt по контракту
- обновить `char_count` в meta после финальной правки writer/indexer

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | author_id: artur-horoshev
