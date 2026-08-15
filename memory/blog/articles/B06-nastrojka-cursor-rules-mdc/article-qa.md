# QA: B06 nastrojka-cursor-rules-mdc

date: 2026-08-15
score_total: 94/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «cursor rules», FAQ 7, 2 таблицы, списки — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 2 таблицы, FAQ 7, чеклист 15, workflow blockquote |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за cursor.directory без href (429 в QA-среде) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, editorial tone |
| Fact safety | 15 | 13 | fact-check PASS; 2/6 чисел в fact-bank (Wordstat 248/186, 30–45 мин, v0.43/2024 — из research-notes) |
| Contract HTML | 10 | 8 | linter PASS, объём ~8906 ✓, CTA ≤3 ✓, internal href ×2; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «cursor rules» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: автоматизаторы и маркетологи без Senior-кода |
| C04 | ✓ | alwaysApply, globs, .mdc, Agent vs Tab — «на пальцах» |
| O01 | ✓ | H2 совпадают с каркасом B06 (7 секций + FAQ) |
| O02 | ✓ | Outline: миграция → папка → режимы → примеры → verify → чеклист → next |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (5+5+5 шагов), ul (troubleshooting + 15 checklist), 2 table |
| R01 | ✓ | TL;DR + workflow blockquote + Fact Check blockquote |
| R02 | ✓ | Wordstat 248/186, cursor.com/docs/rules — с research-notes |
| R03 | ✓ | Wordstat с датой «июнь 2026»; 500 строк — из docs |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Ковчег: git-версионируемые rules для команды без копипаста prompt |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, @maya_pro ×1, author ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Tab не использует rules, alwaysApply съедает контекст |
| Ept02 | ✗ | cursor.directory — plain text (429); перед publish вернуть href |

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
- OK: cursor.com/docs/rules (×2), mayai.ru/podklyuchenie-mcp-cursor/ (×2 relative), github.com/PatrickJS/awesome-cursorrules, kv-ai.ru/obuchenie-po-make, t.me/maya_pro, kv-ai.ru/artur-horosheff
- fix applied (cycle 1):
  - `<a href="https://cursor.directory">` → plain text «cursor.directory» (HTTP 429 Too Many Requests из QA-среды)
- **Перед publish:** восстановить href `https://cursor.directory`, повторить link-verify

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 5 (таблицы/blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (6 extracted, 2 verified in fact-bank, 4 unverified — Wordstat/2024/45 мин/400 из research, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` → blockquote (html-linter); cursor.directory 429 → plain text (link-verify)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- восстановить href cursor.directory перед WP publish
- занести Wordstat-цифры и v0.43/2024 в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
