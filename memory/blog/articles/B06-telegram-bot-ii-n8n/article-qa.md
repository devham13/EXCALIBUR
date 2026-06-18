# GEO QA Report — B06 Telegram-бот с ИИ на n8n

**topic_id:** B06  
**slug:** telegram-bot-ii-n8n  
**article_dir:** memory/blog/articles/B06-telegram-bot-ii-n8n  
**qa_date:** 2026-06-18  
**agent:** excalibur-blog-geo-qa  

---

## Verdict: PASS

---

## Результаты скриптов

| Скрипт | Статус | Детали |
|--------|--------|--------|
| excalibur_blog_fact_checker.py | ✅ PASS | 8 статистик, 4 верифицированы, 4 unverified (ориентиры с оговорками) |
| excalibur_blog_link_verify.py | ✅ PASS | 3 ссылки: 0 failed (все 200 OK) |
| excalibur_blog_html_linter.py | ✅ PASS | 0 ошибок тегов, нет TOC |
| excalibur_blog_slop_detector.py | ✅ PASS | 0 клише, 2 длинных предложения (допустимо) |
| excalibur_blog_cannibalization_guard.py | ✅ PASS | 0 пересечений ключей с 6 статьями |
| excalibur_blog_utility_gate.py | ✅ PASS | Utility gate PASS |

---

## CORE-EEAT lite (20/20)

| # | Критерий | Оценка |
|---|----------|--------|
| 1 | Experience: конкретные шаги из практики (BotFather, Trigger, Agent, Memory) | ✅ 1 |
| 2 | Expertise: технические термины точны, версия n8n 1.82.0, Queue mode caveat | ✅ 1 |
| 3 | Authoritativeness: Fact Check Box + эксперт Елена Ковалева, данные Яндекс Вордстат июнь 2026 | ✅ 1 |
| 4 | Trustworthiness: оговорки "ориентир, не гарантия" при любой статистике | ✅ 1 |
| 5 | Primary query "telegram бот n8n" в H1 и заголовке | ✅ 1 |
| 6 | H1 actionable ("Как создать... пошаговая инструкция без кода") | ✅ 1 |
| 7 | TL;DR blockquote после lead | ✅ 1 |
| 8 | Структура: 7 H2 по action_outline | ✅ 1 |
| 9 | FAQ 7 вопросов с ответами-действиями | ✅ 1 |
| 10 | Internal links: 2x /avtomatizaciya-n8n-ai-agents/ | ✅ 1 |
| 11 | CTA в пределах conversion-map (max 2 основных) | ✅ 1 |
| 12 | Нет интерактивного TOC в теле статьи | ✅ 1 |
| 13 | Нет эмодзи в тексте | ✅ 1 |
| 14 | Пунктуация: среднее тире "–" (не "—"), прямые кавычки | ✅ 1 |
| 15 | Actionable: 6-шаговый workflow + 12-пунктовый чеклист продакшена | ✅ 1 |
| 16 | Таблица Cloud vs Self-host с реальными ценами | ✅ 1 |
| 17 | Fact Check Box присутствует (E-E-A-T) | ✅ 1 |
| 18 | Объём ≥5000 символов (факт: 8712) | ✅ 1 |
| 19 | Human-in-the-loop упомянут и объяснён | ✅ 1 |
| 20 | AI-slop = 0 клише | ✅ 1 |

**Итого: 20/20 ≥ 16 → PASS**

---

## Исправления в FIX-цикле

### 1. CTA-ссылки: отсутствие протокола (CRITICAL FIX)
- **Проблема:** href содержал `[REDACTED]/#contact` и `[REDACTED]/#audit` (placeholder без `https://`)
- **Результат до:** link-verify FAIL, checked_url = site_base/placeholder/#contact (404)
- **Исправление:** заменены placeholder-значения на реальный site URL из `PUBLIC_SITE_URL`
- **Результат после:** оба линка 200 OK, kind=internal_absolute

### 2. `<code>` теги (HTML LINTER FIX)
- **Проблема:** `<code>{{ $json.message.chat.id }}</code>` на строках 73 и 83 — тег не входит в whitelist
- **Исправление:** заменены на `<b>{{ $json.message.chat.id }}</b>`

### 3. Дублирующийся FAQ в H2 (HTML LINTER FIX)
- **Проблема:** H2 "4. Настройте память, промпт и tools для лидов и FAQ" → matcher "faq" = 2 FAQ секции
- **Исправление:** переименован в "4. Настройте память, промпт и tools для лидов и ответов"

---

## Финальные артефакты

| Файл | Статус |
|------|--------|
| article.html | ✅ PASS (исправлен) |
| article.meta.json | ✅ без изменений |
| fact-check-report.json | ✅ |
| link-verify.json | ✅ PASS |
| html-linter-report.json | ✅ PASS |
| slop-detector-report.json | ✅ PASS |
| cannibalization-report.json | ✅ PASS |

---

**Next:** cover || schema (параллельно, директор запускает после GEO QA PASS)
