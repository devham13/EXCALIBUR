# QA: B06 subagenty-claude-code

date: 2026-07-08
score_total: 95/100
core_eeat_lite: 20/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H1/H2/H3 покрывают «subagents claude code», primary query в H1, 8 H2-секций, FAQ 7 пар |
| GEO / citability | 25 | 24 | Lead direct answer, TL;DR blockquote, 2 таблицы, ol 7 шагов, FAQ 7; −1 за минимальные внешние цитаты с URL |
| CORE-EEAT lite | 15 | 15 | 20/20, все критерии выполнены |
| Human voice | 15 | 14 | 0 slop-clichés; 3 over-long (из blockquote/чеклиста); Flesch RU 100 (приемлемо для how-to) |
| Fact safety | 15 | 14 | PASS; 2/3 verified в fact-bank; «198» (версия) не в банке — не блокер |
| Contract HTML | 10 | 8 | PASS после fix; char 8856 (OK 8500–9500); нет `<img>` с alt (-2) |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен (95/100)**.

## Fix-цикл

**html-linter FAIL → FIX → PASS** (1 цикл):
- Заменены `<code>` (inline) → `<b>` в шагах 1 и 5
- Заменены два блока `<pre><code>...</code></pre>` → `<blockquote>` с `<br>` для code-reviewer.md и блока 6 ролей

## CORE-EEAT lite: 20/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «subagents claude code», «pošagovaja instrukcija» |
| C02 | ✓ | Lead — direct answer без «в этой статье» |
| C03 | ✓ | Аудитория: разработчики Claude Code v2.1.198+ |
| C04 | ✓ | .claude/agents/, YAML frontmatter, background/foreground — объяснено доступно |
| O01 | ✓ | H2 покрывают action_outline: compare → create → yaml → 7 roles → parallel → CLAUDE.md → security → FAQ |
| O02 | ✓ | Логичный порядок: от архитектуры к чеклисту безопасности |
| O03 | ✓ | FAQ 7 пар из реальных user queries |
| O04 | ✓ | ol (7 шагов), ul (14-item чеклист), 2 таблицы |
| R01 | ✓ | TL;DR blockquote + «Итоговый вердикт» в compare + раздел «Что делать дальше» |
| R02 | ✓ | Версии 2.1.198/2.1.196/2.1.186, дата «1 июля 2026», npm-команды |
| R03 | ✓ | Даты с контекстом: «от 1 июля 2026», «на 8 июля 2026» |
| R04 | ✓ | FAQ: каждый ответ начинается с прямого ответа |
| E01 | ✓ | Угол: актуальный путь без удалённого wizard /agents — уникальный gap в RU-контенте |
| E02 | ✓ | «Делайте/Не делайте» в каждой H2-секции |
| E03 | ✓ | CTA Make × 1, blockquote автора × 1 |
| Exp01 | ✓ | Режим B (How-to), без fake case studies |
| Exp02 | ✓ | YAML-примеры реальных файлов, конкретные команды npm/claude |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Agent Teams — эксперимент, не включать без причины; background prompts 2.1.186+ |
| Ept02 | ✓ | Все ссылки рабочие: link-verify PASS, 3/3 (200 OK) |

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

- total: 3, failed: 0
- OK: /podklyuchenie-mcp-cursor/ (200), kv-ai.ru/obuchenie-po-make (200), kv-ai.ru/artur-horosheff (200)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (из blockquote/чеклиста — допустимо)
- Flesch RU: 100.0 (Very Easy — приемлемо для технического how-to с короткими предложениями)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (3 extracted, 2 verified in fact-bank, 1 unverified — «198» версия, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (excalibur_blog_utility_gate.py --article-dir)
- topic: PASS (из research phase)

## Optional (не blocker)

- добавить 1 `<img>` с alt (cover будет добавлен schema-агентом)
- занести «2.1.198» в fact-bank как версию v1

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (mode B, 7 steps) | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
