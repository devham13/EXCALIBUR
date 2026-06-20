# QA: B06 make-ai-agents-nastrojka-2026

date: 2026-06-20
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «make ai agents», FAQ 7 пар, 2 таблицы, 9 шагов + чек-лист 12 п. — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, workflow blockquote, 2 таблицы, FAQ 7; −1 Wordstat MCP недоступен (отмечено в Fact Check box) |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за 4/7 чисел вне fact-bank (официальные make.com, не blocker) |
| Human voice | 15 | 15 | 0 AI-slop hits, технический no-code тон, Flesch RU 99.6 |
| Fact safety | 15 | 13 | fact-check PASS; 3/7 чисел в fact-bank; 3000+, credits, 240 символов — из help/pricing make.com |
| Contract HTML | 10 | 7 | linter PASS, объём 8997 ✓, CTA ≤3 ✓, internal href ×3; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «make ai agents» + RU «настройка» |
| C02 | ✓ | Lead — direct answer про диспетчер на канвасе, без «в этой статье» |
| C03 | ✓ | Аудитория: no-code, поддержка/лиды/отчёты, B2B без программирования |
| C04 | ✓ | LLM, tool, MCP, Return output — «на пальцах» |
| O01 | ✓ | H2 совпадают с action_outline research (7 секций + FAQ) |
| O02 | ✓ | Outline: агент vs сценарий → подготовка → 9 шагов → tools → prod → n8n → next steps |
| O03 | ✓ | FAQ 7 пар, queries из SERP/research (credits, CRM, n8n, tool-calls) |
| O04 | ✓ | ol (9 шагов + 12 чек-лист + 5 next steps), 2 table, blockquotes |
| R01 | ✓ | TL;DR + workflow blockquote + итоговый вердикт n8n + FAQ |
| R02 | ✓ | Тарифы Core/Pro, 3000+ apps, февраль 2026 UI — с research-notes |
| R03 | ✓ | Цены с датой «июнь 2026»; credits без выдуманных фикс-цифр |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: next-gen canvas 2026, Reasoning Panel, Return output, 12-p guardrails |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA kv-ai.ru ×2, @maya_pro ×1 |
| Exp01 | ✓ | Режим B, без fake «я внедрил» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Credits variable, human approval, Free 15 мин интервал |
| Ept02 | ✗ | Internal link только B02 (×3 один URL) — по карточке достаточно, но нет второго inbound из плана |

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

- total: 3 (unique), failed: 0
- OK: /avtomatizaciya-n8n-ai-agents/ (×3 в тексте), kv-ai.ru/obuchenie-po-make (×2), t.me/maya_pro

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблицы/blockquote — допустимо)
- Flesch RU: 99.6 (Very Easy — короткие предложения, how-to стиль)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 3 verified in fact-bank, 4 unverified — 3000+, 1 000 credits, 240 символов, 100 прогонов из официальных/help источников)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- Нет критических замечаний. Writer-цикл не требуется.

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести тарифы Make/credits в fact-bank
- после восстановления MCP Wordstat — обновить research-notes и Fact Check box

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
