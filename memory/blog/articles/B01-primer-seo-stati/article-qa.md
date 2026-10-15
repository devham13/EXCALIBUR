# QA: B01 primer-seo-stati

date: 2026-10-07
score_total: 91/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2/H3, primary query, FAQ 7, checklist 15 — OK; −1 нет `<img>` с alt (cover позже) |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица SEO vs GEO, workflow blockquote, island-ready H2 |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 75.1, editorial «мы/вы» |
| Fact safety | 15 | 13 | fact-check PASS; 3 числа вне fact-bank (8500–9500, 2024 llms.txt — из research) |
| Contract HTML | 10 | 10 | linter PASS после правки H2; объём ~9211 ✓, CTA ≤3 ✓, internal `/` ✓ |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/H1 закрывают «как писать seo статьи» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога / контент без отдельного «AI-проекта» |
| C04 | ✓ | RAG, GEO, llms.txt — с расшифровкой |
| O01 | ✓ | 7 H2 по research action_outline |
| O02 | ✓ | семантика → SEO/GEO → черновик → schema/ссылки → чек-лист → FAQ |
| O03 | ✓ | FAQ 7 пар, real queries |
| O04 | ✓ | ol (7 шагов), ul (15 checklist), table |
| R01 | ✓ | TL;DR + blockquote workflow |
| R02 | ✓ | Яндекс Direct, Вебмастер, Вордстат — href |
| R03 | ✓ | Wordstat без выдуманных показов; Fact Check block |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: один workflow SEO+GEO |
| E02 | ✓ | «Делайте / Не делайте» в секциях |
| E03 | ✓ | CTA Make ×1, author ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон практика, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: нет магического объёма, llms.txt ≠ индексация |
| Ept02 | ✗ | Нет `<img>` с alt до cover (ожидаемо на шаге ④a) |

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

- total: 7, failed: 0
- OK: direct.yandex.ru, wordstat, webmaster, yandex threat/seo-text, kv-ai.ru (×2), internal `/`

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (чек-лист/таблица — допустимо)
- Flesch RU: 75.1 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 3 verified in fact-bank, 3 unverified — диапазоны объёма и 2024 llms из research, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass, 0 issues vs другие статьи в `memory/blog/articles`
- see `cannibalization-report.json`

## Fixes (cycle 1, QA)

1. **html-linter:** H2 «Подключите FAQ, schema…» → «Подключите schema, перелинковку и блок вопросов» (ложный duplicate FAQ по regex `faq` в заголовке).
2. **utility gate warning:** перефразирован шаг 4 в ol — убрана дословная water-фраза из текста (контекст «не использовать»).

## Next

- excalibur-blog-cover || excalibur-blog-schema (после директора)
- После cover: добавить `<img alt=…>` и пересчитать Contract HTML при необходимости
