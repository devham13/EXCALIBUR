# QA: B06 cursor-environment-json-cloud-agents

date: 2026-10-07
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2×8, FAQ 7, primary query «настройка cursor cloud agent», якоря id |
| GEO / citability | 25 | 23 | TL;DR, 2 таблицы, workflow blockquote, FAQ answer-first; −2 без inline `<img>` |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже) |
| Human voice | 15 | 15 | 0 AI-slop clichés, Flesch RU 100 |
| Fact safety | 15 | 13 | fact-check PASS; 3000/5432 — примеры портов, не blocker |
| Contract HTML | 10 | 7 | linter PASS, char_count 8994 ✓; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «настройка cursor cloud agent» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: команды с hosted Cloud Agents / Automations |
| C04 | ✓ | install/start, snapshot, Build — в контексте |
| O01 | ✓ | H2 совпадают с каркасом B06 (8 секций + FAQ) |
| O02 | ✓ | Outline: compare → structure → install → run → builds → secrets → checklist |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (7+5 шагов), ul checklist, 2 table |
| R01 | ✓ | TL;DR + workflow + expert blockquote |
| R02 | ✓ | install/start, приоритет config — research-notes + cursor docs |
| R03 | ✓ | Нет неподтверждённых процентов/цен |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: config-as-code, install vs start, failed Build fallback |
| E02 | ✓ | «Делайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA Make ×1, author ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Self-Hosted, secrets, failed Build — ограничения названы |
| Ept02 | ✗ | −1: internal links на mayai.ru (не relative `/slug/`) — fix для link-verify |

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
- OK: cursor.com/schemas/environment.schema.json, mayai.ru/podklyuchenie-mcp-cursor/, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- fix applied (cycle 1): `/podklyuchenie-mcp-cursor/` → `https://mayai.ru/podklyuchenie-mcp-cursor/` (404 на PUBLIC_SITE_URL root)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 6 (таблицы/checklist — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (4 extracted, 2 verified, 2 unverified — порты 3000/5432 как пример конфига)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` → blockquote (html-linter); internal MCP links → mayai.ru absolute (link-verify)

## Optional (не blocker)

- добавить 1–3 `<img>` с alt по контракту (cover/indexer зона)

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
