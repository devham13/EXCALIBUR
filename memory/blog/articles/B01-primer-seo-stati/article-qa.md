# QA: B01 primer-seo-stati

date: 2026-10-06
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7 пар, без TOC в body |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, 9+5 шагов, TL;DR |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 78.7 |
| Fact safety | 15 | 13 | fact-check PASS; 6 чисел не в fact-bank (ориентиры объёма/SERP — из research) |
| Contract HTML | 10 | 7 | linter PASS, объём ~9205 ✓, 3× `<img>` alt ✓; −3 одна internal href (`/#services`), смежный гайд — plain text до live slug |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, RAG, llms.txt объяснены |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (4+5 шагов), ul (15 checklist), table |
| R01 | ✓ | ≥3 standalone блоков 40–60 слов |
| R02 | ✓ | Яндекс Директ, Wordstat, Webmaster — с href |
| R03 | ✓ | Нет неподтверждённых %; GEO-bench с оговоркой |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: единый SEO+GEO workflow, self-demo |
| E02 | ✓ | «Делайте / Не делайте» в H2 |
| E03 | ✓ | CTA Make ×2, Telegram ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения и риски названы |
| Ept02 | ✓ | Internal `/#services` HTTP 200 |

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
- OK: wordstat, webmaster, direct.yandex SEO guide, `/#services`, kv-ai.ru/obuchenie-po-make, t.me/maya_pro
- fix applied (cycle 1, 2026-10-06):
  - `/geo-optimizaciya-sajta-2026/` → plain text + `/#services` (404 на live mayai.ru)
- **Перед publish:** при появлении slug `geo-optimizaciya-sajta-2026` на сайте — вернуть href на смежный гайд и повторить link-verify

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/чеклист — допустимо)
- Flesch RU: 78.7 (Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (8 extracted, 2 verified in fact-bank, 6 unverified — ориентиры, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 5 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- overall: PASS (9 numbered steps, 8 H2, 7 FAQ, 1 table, 24 action markers)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1 (2026-10-06): `<figure>` → `<p><img>`, H2 §6 без слова «FAQ» (duplicate FAQ linter), битая internal ссылка → `/#services`
- cycle 2: повтор всех скриптов — PASS

## Optional (не blocker)

- второй internal href на опубликованный смежный материал после live
- синхронизировать `article.meta.json` char_count с фактическим (~9205)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: elena-kovaleva)
