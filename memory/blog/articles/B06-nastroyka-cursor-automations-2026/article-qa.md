# QA: B06 nastroyka-cursor-automations-2026

date: 2026-10-15
score_total: 92/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
verdict: PASS

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2×7, FAQ 7 пар, ol/ul, 2 таблицы; primary query в H1/title |
| GEO / citability | 25 | 23 | Lead answer-first, TL;DR, таблицы триггеров, FAQ citability-first |
| CORE-EEAT lite | 15 | 13 | 18/20; −2 за environment.json через docs Cursor вместо internal slug (статья ещё не на mayai.ru) |
| Human voice | 15 | 15 | 0 AI-slop hits, режим B, Flesch RU 100 (короткие предложения) |
| Fact safety | 15 | 13 | fact-check PASS; 45 мин / 200 строк — editorial пороги, не blocker |
| Contract HTML | 10 | 9 | linter PASS после замены `<pre><code>` на blockquote (whitelist); CTA ≤3; −1 нет `<img>` |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, utility gate pass — **выполнен**.

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | H1/Title — «cursor automations настройка» |
| C02 | ✓ | Lead — direct answer без «в этой статье» |
| C03 | ✓ | Аудитория: автоматизаторы Cloud Agents / Make-мышление |
| C04 | ✓ | Cloud Agent, webhook, Run as, CRON_TZ — по месту |
| O01 | ✓ | H2 совпадают с action_outline research |
| O02 | ✓ | Automations vs agent → billing → cron → webhook → GitHub → checklist → next |
| O03 | ✓ | FAQ 7 пар из faq_hints |
| O04 | ✓ | ol (5), ul (чеклист 13), 2 table |
| R01 | ✓ | TL;DR + табличные блоки + FAQ standalone |
| R02 | ✓ | GA 5 марта 2026, Save-first webhook — research-notes + docs |
| R03 | ✓ | $2 headroom с пометкой forum; pricing — ссылка на docs |
| R04 | ✓ | FAQ: ответ в первом предложении |
| E01 | ✓ | Угол: первая automation 30–45 мин, forum cron workarounds |
| E02 | ✓ | «Делайте / Не делайте» в секциях |
| E03 | ✓ | Make ×1, Telegram ×1, author blockquote |
| Exp01 | ✓ | Режим B, без fake case |
| Exp02 | ✓ | Тон research/brief |
| Exp03 | ✓ | 0 slop hits |
| Ept01 | ✓ | Fork PR, billing cap, stale cron — ограничения названы |
| Ept02 | ✗ | `/cursor-environment-json-cloud-agents/` заменён на cursor.com/docs/cloud-agent/setup (slug не опубликован) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |

## Fix cycle (GEO QA)

- Заменён `<pre><code>` curl на `<blockquote>` (html-linter whitelist).
- Internal MCP → `https://mayai.ru/podklyuchenie-mcp-cursor/`; environment → docs setup (link-verify 8/8 OK).

## Optional (не blocker)

- Добавить `<img>` с alt по контракту cover/publish.
- После публикации гайда environment.json — вернуть internal slug из карточки B06.

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (7) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: artur-horoshev)
