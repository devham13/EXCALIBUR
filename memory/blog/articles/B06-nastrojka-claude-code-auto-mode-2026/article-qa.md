# QA: B06 nastrojka-claude-code-auto-mode-2026

date: 2026-07-10
score_total: 95/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «claude code auto mode», FAQ 7 пар, списки, таблица режимов — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 1 таблица сравнения режимов, FAQ 7, чеклист 15 пунктов, 2 JSON blockquote |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 Wordstat offline (честно в Fact Check box) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, технический how-to тон |
| Fact safety | 15 | 14 | fact-check PASS; 2/2 extracted verified; метрики 93%/FPR/FNR — с inline cite Anthropic docs |
| Contract HTML | 10 | 8 | linter PASS, объём 11412 ✓, CTA ≤3 ✓, internal href ×3; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «claude code auto mode» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: разработчики и DevOps на Claude Code, unattended на shared infra |
| C04 | ✓ | classifier, autoMode, hard_deny, Shift+Tab — «на пальцах» |
| O01 | ✓ | H2 совпадают с research action_outline (7 секций + FAQ) |
| O02 | ✓ | Outline: сравнение режимов → eligibility → enable → autoMode → layers → checklist → next |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (5+3 шагов), ul (15 checklist + 4 layers), 1 table |
| R01 | ✓ | TL;DR + итоговый вердикт + «Делайте/Не делайте» в H2 |
| R02 | ✓ | 93% approve, v2.1.83+, FPR 8.5%, FNR 17% — с research-notes / Anthropic docs |
| R03 | ✓ | Wordstat offline указан честно; docs сверены 10.07.2026 |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Ковчег: RU how-to autoMode.environment + CLI verify без bypass на prod |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA Make ×1, author blockquote ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: classifier FNR ~17%, latency/tokens, project settings ignore autoMode |
| Ept02 | ✗ | Wordstat MCP offline — точные показы не в тексте (не blocker, зафиксировано) |

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
- OK: /dinamicheskie-workflow-claude-code/, /claude-code-hooks-nastrojka-2026/, /nastroyka-claude-code-mcp/, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff, code.claude.com/docs/en/auto-mode-config

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 2 (таблица/чеклист — допустимо)
- Flesch RU: 100.0 (Very Easy — короткие предложения в списках)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (2 extracted, 2 verified in fact-bank, 0 unverified)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- **Cycle 1 (GEO QA minimal fix):** html-linter FAIL — `<pre><code>` запрещены whitelist; заменены на `<blockquote>` для двух JSON-примеров settings.json. Повторный прогон всех скриптов — PASS.

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- при доступном user-mcp-kv — дополнить Wordstat показы в Fact Check box

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
