# QA: B06 nastrojka-cursor-subagents-2026

date: 2026-06-22
score_total: 97/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «cursor subagents», FAQ 7 пар, списки, 2 таблицы — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, comparison table subagents vs Background vs MCP, FAQ 7, чеклист 12 |
| CORE-EEAT lite | 15 | 15 | 20/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop hits, технический how-to тон, Flesch RU 100 (короткие предложения) |
| Fact safety | 15 | 14 | fact-check PASS; 1/2 unverified — «20–30 минут» из action_outline, не blocker |
| Contract HTML | 10 | 9 | linter PASS после fix `<pre>/<code>` → blockquote; CTA ≤3 ✓, internal ×2; −1 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/meta/lead закрывают «cursor subagents» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: разработчики и автоматизаторы, первая ИИ-команда в Cursor |
| C04 | ✓ | Subagents, YAML frontmatter, Task tool — объяснены при первом появлении |
| O01 | ✓ | 10 H2 совпадают с action_outline research (compare → FAQ) |
| O02 | ✓ | Outline: встроенные → структура → create → invoke → orchestration → comparison → troubleshooting → checklist |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (7+5 шагов), ul (12 пунктов), 2 table |
| R01 | ✓ | TL;DR + verdict blockquote + FAQ standalone answers |
| R02 | ✓ | Cursor 2.4, 5× tokens, frontmatter — с docs/changelog URLs в research-notes |
| R03 | ✓ | Wordstat цифры не включены (MCP unavailable); disclaimer в Fact Check |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: reviewer + test-runner за 20–30 мин, decision tree vs MCP/Background |
| E02 | ✓ | «Делайте/Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA Make ×1, author blockquote ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: 5× tokens, merge conflicts, nested limits |
| Ept02 | ✓ | Internal links B03 MCP + B02 n8n — link-verify 200 |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS (after fix) | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Link verify

- total: 5, failed: 0
- OK: /podklyuchenie-mcp-cursor/, cursor.com/docs/subagents, /avtomatizaciya-n8n-ai-agents/, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (таблицы/blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (2 extracted, 1 verified in fact-bank, 1 unverified — «30 минут» из outline)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- **Цикл 1 (GEO QA):** html-linter FAIL — forbidden `<pre>/<code>` в примерах code-reviewer/test-runner. Минимальный fix: заменены на `<blockquote>` с `<br>` (контракт B03). Повторный linter PASS.

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести «20–30 минут» в fact-bank как editorial estimate

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
