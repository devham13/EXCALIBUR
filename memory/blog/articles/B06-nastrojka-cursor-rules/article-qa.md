# QA: B06 nastrojka-cursor-rules

date: 2026-06-20
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «cursor rules», FAQ 7, без in-body TOC — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица 4 режимов, FAQ 7, 9 шагов + чек-лист 12 пунктов |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за 401 repos (UC Irvine) не в fact-bank |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, editorial «Делайте/Не делайте» |
| Fact safety | 15 | 13 | fact-check PASS; 3/4 чисел в fact-bank, 401 — из Habr/SimpleOne research |
| Contract HTML | 10 | 7 | linter PASS после fix; объём 8542 ✓, CTA ≤3 ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «cursor rules» / «настройка cursor rules» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: разработчики и автоматизаторы, настраивающие Agent в Cursor |
| C04 | ✓ | .mdc, frontmatter, globs, alwaysApply — «на пальцах» |
| O01 | ✓ | H2 совпадают с action_outline research (7 секций + FAQ) |
| O02 | ✓ | Outline: legacy → mkdir → пошагово → режимы → MCP workflow → migration → next steps |
| O03 | ✓ | FAQ 7 пар, queries из research (mdc, globs, alwaysApply, Cmd+K) |
| O04 | ✓ | ol (9 шагов + 4 next steps), ul (12 checklist), 1 table |
| R01 | ✓ | TL;DR + workflow blockquote + «Материал проверен» blockquote |
| R02 | ✓ | 401 repos / 28,7% dup (Habr), 4 режима Cursor docs — с research-notes |
| R03 | ✓ | Статистика UC Irvine с источником; нет неподтверждённых цен |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: Rules+MCP workflow, миграция .cursorrules, troubleshooting silent failure |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, author blockquote ×1, internal B03 ×2 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: rules — подсказки, не 100% соблюдение; Tab/Inline Edit не используют rules |
| Ept02 | ✗ | Internal links на mayai.ru (B03 published); relative `/podklyuchenie-mcp-cursor/` давал 404 на PUBLIC_SITE_URL worker |

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

- total: 3, failed: 0
- OK: mayai.ru/podklyuchenie-mcp-cursor/ (×2), kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- fix applied (cycle 1):
  - `/podklyuchenie-mcp-cursor/` → `https://mayai.ru/podklyuchenie-mcp-cursor/` (404 на PUBLIC_SITE_URL worker; B03 published на mayai.ru)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблица/blockquote/чек-лист — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (4 extracted, 3 verified in fact-bank, 1 unverified — 401 repos UC Irvine из research/Habr, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` → `<blockquote>` (html-linter); relative internal links → absolute mayai.ru (link-verify)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести «401 repos / 28,7% duplicates» в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
