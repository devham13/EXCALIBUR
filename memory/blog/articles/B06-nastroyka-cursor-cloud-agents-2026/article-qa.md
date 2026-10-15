# QA: B06 nastroyka-cursor-cloud-agents-2026

date: 2026-09-13
score_total: 91/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2/H3, primary query «настройка cursor cloud agents», FAQ 7, без in-body TOC |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, 3 таблицы, FAQ 7, 15+ шагов, workflow blockquote |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за rules → cursor.com/docs вместо internal slug (404) |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 100.0, editorial tone |
| Fact safety | 15 | 13 | fact-check PASS; 2/3 чисел в fact-bank (port 3000 — пример из schema, не blocker) |
| Contract HTML | 10 | 8 | linter PASS, объём 9223 ✓, CTA ≤3 ✓; −2 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «настройка cursor cloud agents» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: разработчики и автоматизаторы на Cursor |
| C04 | ✓ | VM, Build, tmux, idempotent install — «на пальцах» |
| O01 | ✓ | H2 совпадают с каркасом B06 (9 секций + FAQ) |
| O02 | ✓ | Outline: compare → GitHub → setup/Build → env.json → secrets → run → fix → checklist |
| O03 | ✓ | FAQ 7 пар, queries из research |
| O04 | ✓ | ol (5+5+4 шагов), ul (12 checklist), 3 table |
| R01 | ✓ | TL;DR + workflow + Fact Check blockquote |
| R02 | ✓ | Builds Aug 2026, schema 10 полей, start:true forum — из research-notes |
| R03 | ✓ | Дата проверки «13.09.2026» в Fact Check |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол Ковчег: русский first-run how-to с Builds + environment.json |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, @maya_pro ×1, author ×1 |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: Hobby не подходит, secrets не в JSON, snapshot trap |
| Ept02 | ✗ | `/nastroyka-cursor-rules-mdc/` → 404; заменено на cursor.com/docs/context/rules |

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

- total: 8, failed: 0
- OK: cursor.com/docs/cloud-agent/setup, cursor.com/docs/cloud-agent, cursor.com/docs/context/rules, mayai.ru/podklyuchenie-mcp-cursor/, environment.schema.json, kv-ai.ru/obuchenie-po-make, t.me/maya_pro, kv-ai.ru/artur-horosheff
- fix applied (cycle 1):
  - `cursor.com/dashboard/cloud-agents` → `cursor.com/docs/cloud-agent/setup` (403 из QA-среды)
  - `cursor.com/agents` → `cursor.com/docs/cloud-agent` (403)
  - `/podklyuchenie-mcp-cursor/` → `https://mayai.ru/podklyuchenie-mcp-cursor/` (site-base 404)
  - `/nastroyka-cursor-rules-mdc/` → `cursor.com/docs/context/rules` (slug не опубликован, 404)
- **Перед publish:** при появлении internal slug rules — вернуть `/nastroyka-cursor-rules-mdc/`; dashboard/agents href можно восстановить после link-verify на prod

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (таблицы/blockquote — допустимо)
- Flesch RU: 100.0 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (3 extracted, 2 verified in fact-bank, 1 unverified — port 3000 пример, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`excalibur_blog_utility_gate.py --article-dir`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycle

- cycle 1: GEO QA — `<pre><code>` → blockquote (html-linter); 4 broken/403 links → docs + mayai.ru absolute URLs (link-verify)

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- восстановить internal rules slug после публикации темы
- занести port 3000 example в fact-bank

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
