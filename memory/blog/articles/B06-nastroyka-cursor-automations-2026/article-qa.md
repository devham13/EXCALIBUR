# QA: B06 nastroyka-cursor-automations-2026

date: 2026-08-28
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query cursor automations, FAQ 7, без TOC в теле |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 3 таблицы, 7 FAQ, ol 4+6+5 шагов |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за editorial «30–45 минут» без fact-bank |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, режим B first-person |
| Fact safety | 15 | 13 | fact-check PASS; 1/2 unverified (45 мин — editorial estimate) |
| Contract HTML | 10 | 8 | linter PASS, объём 9303 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «cursor automations» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: маркетологи и автоматизаторы без dev-бэкграунда |
| C04 | ✓ | Trigger, repo scope, MCP — «на пальцах» |
| O01 | ✓ | H2 совпадают с research action_outline (8 секций) |
| O02 | ✓ | Outline: Agents vs Automations → setup → create → triggers → /goal → troubleshooting |
| O03 | ✓ | FAQ 7 пар, реальные queries |
| O04 | ✓ | ol (4+6+5), ul checklist 11 п., 3 таблицы |
| R01 | ✓ | TL;DR + blockquote workflow + cron block, standalone блоки |
| R02 | ✓ | Факты 19.08.2026, UTC cron, secrets — из research-notes + официальная docs |
| R03 | ✓ | Нет выдуманных Wordstat-объёмов; billing с оговоркой API pricing |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: RU how-to Agents+Automations+troubleshooting UTC/secrets |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×2, author ×1 — ≤3 оффера |
| Exp01 | ✓ | Режим B, editorial без fake case |
| Exp02 | ✓ | Тон brief, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: billing, UTC, Slack private, 403 secrets |
| Ept02 | ✗ | Internal links только B03 MCP (2×); карточка темы допускает 2–3 — на минимуме |

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

- total: 5, failed: 0
- OK: /podklyuchenie-mcp-cursor/ (×2), cursor.com/docs/cloud-agent/setup, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff, cursor.com/help/ai-features/automations
- fix applied (cycle 1):
  - `https://cursor.com/dashboard/cloud-agents` → docs link + plain text URL (403 из QA-среды)
  - `https://cursor.com/automations/new` → plain text cursor.com/automations/new (403)
- **Перед publish:** опционально восстановить href на dashboard/automations/new и повторить link-verify

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблицы/чеклист — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (2 extracted, 1 verified in fact-bank, 1 unverified — «45 минут» editorial)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- topic B06: PASS (how_to, mode B)
- article: PASS (15 numbered steps, 8 H2, 7 FAQ, 3 tables)
- see `utility-gate-report.json`

## Fix cycle

- cycle 1: GEO QA — заменены `<code>`/`<pre>` на `<b>`/`<blockquote>` (html-linter); auth-only cursor.com URLs → docs/plain text (link-verify PASS)

## Optional (не blocker)

- добавить `<img>` с alt по контракту (cover-агент)
- восстановить href dashboard/automations/new перед WP publish
- занести «45 минут» в fact-bank или смягчить формулировку

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
