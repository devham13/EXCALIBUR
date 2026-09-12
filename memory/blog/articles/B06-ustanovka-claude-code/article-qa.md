# QA: B06 ustanovka-claude-code

date: 2026-08-13
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «claude code», FAQ 7, 7 H2-секций — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 2 таблицы, FAQ 7, ol 6+5 шагов, workflow + Fact Check blockquote |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, editorial tone |
| Fact safety | 15 | 13 | fact-check PASS; 3/5 чисел не в fact-bank (Windows 1809, v2.1.198, 403 — из docs/research) |
| Contract HTML | 10 | 7 | linter PASS, объём 8728 ✓, CTA ≤3 ✓, internal href ×1 (карточка B06); −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «claude code» |
| C02 | ✓ | Lead — direct answer (проблема → решение за 20–40 мин), без «в этой статье» |
| C03 | ✓ | Аудитория: разработчики и автоматизаторы, terminal/CI |
| C04 | ✓ | MCP, CLI, hooks, headless — «на пальцах» в lead и H2 |
| O01 | ✓ | H2 совпадают с research-каркасом B06 (7 секций + FAQ) |
| O02 | ✓ | Outline: choose → install → auth → MCP → hooks/headless → troubleshoot → next |
| O03 | ✓ | FAQ 7 пар, queries из research/faq_hints |
| O04 | ✓ | ol (6+5 шагов), ul (11 checklist), 2 table, 7 blockquote |
| R01 | ✓ | TL;DR + workflow + install/MCP/headless blockquotes + Fact Check |
| R02 | ✓ | Pro $20/Max, install.sh/ps1 — с research-notes и code.claude.com |
| R03 | ✓ | Цены с href claude.com/pricing; Wordstat не выдуман (MCP недоступен — честно в Fact Check) |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Ковчег: terminal/CI vs Cursor, Make/n8n связка, headless `-p` |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, internal MCP ×1, author Fact Check ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: подписка Pro+, sudo npm, лимиты 5h window, API key conflict |
| Ept02 | ✓ | Internal `/podklyuchenie-mcp-cursor/` ×2 (единственная ссылка из карточки B06) |

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
- site-base: from env (internal links checked as relative paths)
- OK: /podklyuchenie-mcp-cursor/, claude.com/pricing, code.claude.com/docs/ru/quickstart, code.claude.com/docs/ru/setup, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблицы/blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 2 verified in fact-bank, 3 unverified — Windows 1809, v2.1.198, 403 из official docs, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 11`, `h2_sections: 7`, `faq_h3: 7`, `tables: 2`, `blockquotes: 7`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` ×7 → `<blockquote>` с backticks (html-linter FAIL → PASS)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести версию пакета v2.1.198 и Windows build 1809 в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
