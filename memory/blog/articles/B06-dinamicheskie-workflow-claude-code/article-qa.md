# QA: B06 dinamicheskie-workflow-claude-code

date: 2026-07-07
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2×7, FAQ 7 пар, primary query «claude code workflow», таблица сравнения, чеклист 11 пунктов |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 1 таблица, FAQ 7, 3× ol (5+5+5 шагов), 6 blockquote |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за одну уникальную internal-цель (B03) при двух href |
| Human voice | 15 | 15 | 0 AI-slop hits, технический тон, Flesch RU 100.0 (короткие предложения + списки) |
| Fact safety | 15 | 13 | fact-check PASS; 2/5 чисел в fact-bank, 3 unverified (v2.1.154, 16/1000 — из docs, не blocker) |
| Contract HTML | 10 | 8 | linter PASS после fix; объём ✓, CTA ≤3 ✓; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «claude code workflow» + dynamic workflows |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: автоматизаторы, техлиды, разработчики в IDE |
| C04 | ✓ | ultracode, MCP, subagents, agent teams — «на пальцах» |
| O01 | ✓ | H2 совпадают с планом B06 (7 секций + FAQ) |
| O02 | ✓ | Outline: сравнение → config → первый run → /workflows → сценарии → безопасность → next steps |
| O03 | ✓ | FAQ 7 пар, queries из research/SERP |
| O04 | ✓ | ol (5+5+5), ul (сценарии + чеклист 11), 1 table |
| R01 | ✓ | TL;DR + итоговый вердикт + «Делайте/Не делайте» в H2 |
| R02 | ✓ | v2.1.154, 16/1000 agents, GA 28.05.2026 — из research-notes + docs |
| R03 | ✓ | Нет неподтверждённых процентов/цен; Bun case — illustrative |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: disambiguation dynamic vs CLAUDE.md/hooks + таблица примитивов |
| E02 | ✓ | «Делайте/Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA Make ×2, @maya_pro ×1, author blockquote ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Лимиты токенов, 16 concurrent, resume только в сессии |
| Ept02 | ✗ | Internal href ×2, но одна цель `/podklyuchenie-mcp-cursor/` (карточка B06 — только B03) |

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

- total: 4, failed: 0
- OK: /podklyuchenie-mcp-cursor/, kv-ai.ru/obuchenie-po-make, t.me/maya_pro, kv-ai.ru/artur-horosheff

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (таблица/blockquote/списки — допустимо)
- Flesch RU: 100.0 (Very Easy — короткие фразы и списки)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (5 extracted, 2 verified in fact-bank, 3 unverified — v2.1.154, 16/1000, 200 modules; из официальных docs, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

**Цикл 1:** html-linter FAIL — запрещённые `<pre><code>` (строки 84, 88). Заменены на `<blockquote>` с `<b>Пример …</b>` по контракту B03. Повторный прогон — PASS.

**Цикл 2:** не потребовался.

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести лимиты 16/1000 и v2.1.154 в fact-bank
- второй internal link из кластера (например B02 n8n) при расширении карточки темы

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
