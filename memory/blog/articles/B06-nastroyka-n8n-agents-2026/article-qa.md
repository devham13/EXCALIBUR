# QA: B06 nastroyka-n8n-agents-2026

date: 2026-10-03
score_total: 94/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary «n8n агенты», FAQ 6 пар, id-якоря, disambiguation vs B02 |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 2 таблицы, blockquote-схема, 13 numbered steps |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 14 | 0 AI-slop hits; slop-detector WARNING — 6 длинных фраз (таблицы/blockquote), допустимо |
| Fact safety | 15 | 14 | fact-check PASS; 1 600 credits/mo не в fact-bank — из n8n pricing + research |
| Contract HTML | 10 | 7 | linter PASS, объём 9339 ✓, CTA ≤3 ✓, internal href ×1; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/meta закрывают «n8n агенты» / standalone Agents |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: настраивающие Agents, не путающие с AI Agent node |
| C04 | ✓ | MCP, turn=execution, draft/published — при первом появлении |
| O01 | ✓ | H2 совпадают с research action_outline (7 секций + FAQ) |
| O02 | ✓ | Outline: compare → create → publish → channels → tools → security → next |
| O03 | ✓ | FAQ 6 пар, product queries (Slack, cron, pricing, self-host) |
| O04 | ✓ | ol (13 шагов), ul (6 checklist), 2 table |
| R01 | ✓ | TL;DR, итоговый вердикт, blockquote-схема Publish |
| R02 | ✓ | Launch 25.09.2026, pricing Starter, Preview status — с research-notes + официальные URL |
| R03 | ✓ | Цены/квоты с ссылкой на pricing; Wordstat не в тексте |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: Agents tab vs node + Message an Agent (пробел SERP) |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, author blockquote ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон how-to от практика, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Preview, queue mode, approvals, Enterprise rollout |
| Ept02 | ✓ | Internal link B02 (disambiguation) — карточка темы |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 6, failed: 0
- fix applied (cycle 1): `/avtomatizaciya-n8n-ai-agents/` → `https://mayai.ru/avtomatizaciya-n8n-ai-agents/` (PUBLIC_SITE_URL в QA давал 404 на relative path; live B02 — 200)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (конкатенация текста таблиц/blockquote — не blocker)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (2 extracted, 1 verified in fact-bank, 1 unverified — 1 600 Assistant credits из pricing, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (13 numbered items, 7 H2, 6 FAQ, 2 tables)
- see `utility-gate-report.json`
