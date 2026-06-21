# QA: B06 rag-baza-znanij-dlya-biznesa-2026

date: 2026-06-21
score_total: 93/100
core_eeat_lite: 19/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2/H3, primary query «rag база знаний», FAQ 7, чек-лист 13 пунктов — OK |
| GEO / citability | 25 | 24 | Lead answer-first, TL;DR, таблица Qdrant/pgvector, FAQ 7, 15 шагов ol, 6 blockquote |
| CORE-EEAT lite | 15 | 14 | 19/20 (см. ниже); −1 за 10/12 unverified metrics в fact-bank |
| Human voice | 15 | 15 | 0 AI-slop hits, Flesch RU 97.2, workflow-тон без generic AI |
| Fact safety | 15 | 13 | fact-check PASS; 2/12 чисел в fact-bank (Habr/Flowwow кейсы из research-notes) |
| Contract HTML | 10 | 7 | linter PASS, объём 8931 ✓, CTA ≤3 ✓, internal href ×2; −3 нет `<img>` с alt |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title закрывают «rag база знаний» |
| C02 | ✓ | Lead — direct answer, без «в этой статье» |
| C03 | ✓ | Аудитория: поддержка/онбординг без ML-команды |
| C04 | ✓ | RAG, hybrid, rerank, HITL, RRF — «на пальцах» |
| O01 | ✓ | H2 совпадают с research-каркасом (8 секций + FAQ) |
| O02 | ✓ | Outline: RAG vs FT → документы → стек → rerank → eval → бот → чек-лист → next |
| O03 | ✓ | FAQ 7 пар, queries из research/Wordstat |
| O04 | ✓ | ol (5+5+5 шагов), ul (13 чек-лист), 1 table, 6 blockquote |
| R01 | ✓ | TL;DR + схемы ingestion/бота + промпт + Fact Check blockquote |
| R02 | ✓ | Habr Wiki 3000→400, Flowwow 5,5×, hybrid precision 62→84% — с research-notes |
| R03 | ✓ | Цифры с оговорками («по отраслевым оценкам», «ориентир, не гарантия») |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: MVP n8n + Qdrant/pgvector + golden set + HITL, не enterprise «от 25 млн» |
| E02 | ✓ | «Делайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA Make ×1, author blockquote ×1 |
| Exp01 | ✓ | Режим B, кейсы Habr/Flowwow — third-party, не fake «я сделал» |
| Exp02 | ✓ | Тон brief/research, не generic AI |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Ограничения: 40% AI-проектов срываются, 6-8 недель MVP, Wordstat pending |
| Ept02 | ✗ | Internal links переведены на absolute mayai.ru (site-base env ≠ mayai.ru); href из карточки сохранены |

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

- total: 4, failed: 0
- OK: mayai.ru/avtomatizaciya-n8n-ai-agents/, mayai.ru/podklyuchenie-mcp-cursor/, kv-ai.ru/obuchenie-po-make, kv-ai.ru/artur-horosheff
- fix applied (cycle 1):
  - `/avtomatizaciya-n8n-ai-agents/`, `/podklyuchenie-mcp-cursor/` → absolute `https://mayai.ru/...` (404 на site-base env; mayai.ru — 200)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 4 (TL;DR, таблица, FAQ — допустимо)
- Flesch RU: 97.2 (Very Easy)
- see `slop-detector-report.json`

## Fact-check

- verdict: pass (12 extracted, 2 verified in fact-bank, 10 unverified — Habr/Flowwow/RAGAS из research, не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues, 6 articles in blog-dir)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 15`, `h2_sections: 8`, `faq_h3: 7`, `tables: 1`)
- topic: PASS (utility-gate-topic.json, research phase)

## Fix cycles

- cycle 0: initial run — html-linter FAIL (`<pre><code>`), link-verify FAIL (relative href 404 на site-base env)
- cycle 1: GEO QA — промпт → blockquote; internal href → absolute mayai.ru — **all PASS**

## Optional (не blocker)

- добавить 1 `<img>` с alt по контракту
- занести Habr/Flowwow метрики в fact-bank
- после publish на mayai.ru можно вернуть relative href для indexer

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
