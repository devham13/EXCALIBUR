# QA: B06 n8n-multi-agent-orkestraciya-2026

date: 2026-06-22
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «n8n агенты», FAQ 7 пар, 2 таблицы, ol/ul — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, workflow blockquote, FAQ 7, 8 шагов + чеклист 16 |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за 1 internal link (карточка B06 — только B02) |
| Human voice | 15 | 15 | 0 AI-slop hits, технический тон, Flesch RU 100 (короткие предложения в FAQ/lists) |
| Fact safety | 15 | 13 | fact-check PASS; 2/5 чисел в fact-bank; Wordstat 699/720 — из B02/research-notes |
| Contract HTML | 10 | 9 | linter PASS после fix `<pre><code>` → blockquote; объём 8721 ✓; CTA ≤3 ✓; −1 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «n8n агенты» / multi-agent orchestration |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: уже собрали single agent (B02), нужен multi-agent prod |
| C04 | ✓ | orchestrator, RAG, MCP, human-in-the-loop, session ID — объяснены |
| O01 | ✓ | H2 совпадают с action_outline research (6 секций + FAQ + next steps) |
| O02 | ✓ | Outline: prerequisite → паттерн → сборка → memory → prod → чеклист |
| O03 | ✓ | FAQ 7 пар, queries из faq_hints + research |
| O04 | ✓ | ol (8 шагов + 16 чеклист + 5 next), ul ×2, 2 table |
| R01 | ✓ | TL;DR + blockquote workflow + FAQ standalone blocks |
| R02 | ✓ | +90,2% Anthropic/n8n.io, Wordstat 699/720, 20 € pricing — research-notes |
| R03 | ✓ | Цены n8n с источником n8n.io/pricing; % с контекстом |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: orchestrator + prod checklist, anti-pattern «один agent достаточно» |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA Make ×1, author blockquote ×1, Maya AI ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: 2,5% задач без HITL, ~40% pilot cancel, ~15x tokens |
| Ept02 | ✗ | 1 internal link `/avtomatizaciya-n8n-ai-agents/` (карточка B06 — 1 шт.; общий порог 2–3 не достигнут) |

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

- total: 3, failed: 0
- site-base: `https://mayai.ru`
- OK: /avtomatizaciya-n8n-ai-agents/, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (таблицы/blockquote/чеклист — допустимо)
- Flesch RU: 100.0 (Very Easy — короткие FAQ/списки доминируют в метрике)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 2 verified in fact-bank, 3 unverified — Wordstat 699/720 из B02, 12345 — пример JSON)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

1. **html-linter FAIL:** forbidden `<pre><code>` (line 79) → заменено на `<blockquote>` с inline JSON (минимальная правка `article.html`). Перезапуск QA — PASS.

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести Wordstat 699/720 в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
