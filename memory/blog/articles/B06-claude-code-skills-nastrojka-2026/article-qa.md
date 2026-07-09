# QA: B06 claude-code-skills-nastrojka-2026

date: 2026-07-09
score_total: 95/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «claude code skills», FAQ 7 пар, 2 таблицы, ol 7 шагов — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, decision tree + 2 таблицы, FAQ 7, blockquote-примеры SKILL.md |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за 4 unverified числа в fact-bank (официальная документация) |
| Human voice | 15 | 15 | 0 AI-slop hits, технический how-to тон, Flesch RU 100 (простые предложения) |
| Fact safety | 15 | 13 | fact-check PASS; 3/7 чисел в fact-bank, 4 из docs Claude Code (1536, 1024, 500, 200) |
| Contract HTML | 10 | 9 | linter PASS после fix pre/code→blockquote; объём 8816 ✓, CTA ≤3 ✓; −1 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «claude code skills» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: разработчики и автоматизаторы Claude Code |
| C04 | ✓ | SKILL.md, frontmatter, auto-invocation, MCP — «на пальцах» |
| O01 | ✓ | H2 совпадают с action_outline research (7 секций + FAQ) |
| O02 | ✓ | Outline: decision tree → scope → anatomy → 7 шагов → production → чеклист → next steps |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (7 шагов + 5 next steps), ul (2 списка), 2 table |
| R01 | ✓ | TL;DR + Fact Check blockquote + чеклист 12 пунктов |
| R02 | ✓ | Лимиты 1536/500/1024, пути ~/.claude/skills/ — из research-notes и docs |
| R03 | ✓ | Дата «июль 2026» в Fact Check; версии Claude Code v2.1.199+ |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Ковчег: how-to SKILL.md с нуля vs listicle «top skills» |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA Make ×1, internal links ×3, author blockquote ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: 500 строк, disable-model-invocation, restart для нового каталога |
| Ept02 | ✗ | −1: 4 числа (1536, 1024, 45 мин, 200 words) не в fact-bank — не blocker, источник docs |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | WARNING | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |
| utility gate (topic B06) | PASS | utility-gate-topic.json |

## Link verify

- total: 7, failed: 0
- OK: /nastroyka-claude-code-mcp/, /claude-code-hooks-nastrojka-2026/, /subagenty-claude-code/, code.claude.com/docs/ru/skills, github.com/anthropics/skills, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 7 (таблицы/blockquote/списки — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (7 extracted, 3 verified in fact-bank, 4 unverified — лимиты из официальной документации Claude Code, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (`excalibur_blog_utility_gate.py --topic-id B06`)

## Fix cycle

- **Цикл 1:** html-linter FAIL — `<pre><code>` запрещены контрактом; заменены на `<blockquote>` с `<br>`. Перезапуск всех скриптов → PASS.

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести лимиты 1536/1024/500 в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
