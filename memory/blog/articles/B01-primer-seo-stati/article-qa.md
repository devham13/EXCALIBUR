# QA: B01 primer-seo-stati

date: 2026-10-13
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: PASS
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query, FAQ 7×, внутренние ссылки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, таблица SEO vs GEO, ol 6 шагов, атомарные H2 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 71.5 |
| Fact safety | 15 | 13 | fact-check PASS; 5/7 чисел вне fact-bank (ориентиры/бенч — допустимо) |
| Contract HTML | 10 | 7 | linter PASS после fix H2; объём 9683 ✓; CTA 1× Make ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate PASS — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают primary query |
| C02 | ✓ | Lead — direct answer |
| C03 | ✓ | Аудитория: авторы блога, редакция |
| C04 | ✓ | SEO, GEO, llms.txt объяснены |
| O01 | ✓ | H2 совпадают с research-каркасом |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 пар |
| O04 | ✓ | ol, ul, table |
| R01 | ✓ | Standalone блоки под H2 |
| R02 | ✓ | Внешние ссылки на источники (Яндекс B2B, anyseo) |
| R03 | ✓ | Нет неподтверждённых % в lead |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол SEO+GEO workflow |
| E02 | ✓ | Практика в каждой H2 |
| E03 | ✓ | CTA Make ×1 |
| Exp01 | ✓ | Режим B |
| Exp02 | ✓ | Тон brief |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения честно |
| Ept02 | ✓ | mayai.ru/, kv-ai.ru — HTTP 200 |

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

- total: 4, failed: 0
- OK: mayai.ru/, b2b.yandex.ru, anyseo.io, kv-ai.ru/obuchenie-po-make
- see `link-verify.json`

## Fix cycle (GEO QA)

- cycle 1 (2026-10-13): duplicate FAQ H2 — переименован `Добавьте FAQ…` → `Подготовьте пары вопрос-ответ для schema-разметки` (минимальный fix в article.html)

## Optional (не blocker)

- добавить 1+ `<img>` с alt по контракту
- utility gate WARN: фраза «в этой статье вы узнаете» только в антипримере (шаг 5) — не правим

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | author_id: artur-horoshev
