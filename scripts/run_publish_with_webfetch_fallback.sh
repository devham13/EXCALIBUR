#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
ARTICLE_DIR="${1:?article dir}"
PUBLIC_BASE="${2:?public base}"
LOG="${3:-/tmp/excalibur-publish.log}"
FALLBACK_FILE="$ROOT/memory/webfetch-response.txt"
rm -f "$FALLBACK_FILE" "$LOG"

python3 scripts/excalibur_blog_wp_publish.py \
  --article-dir "$ARTICLE_DIR" \
  --public-base "$PUBLIC_BASE" >"$LOG" 2>&1 &
PID=$!

URL=""
for _ in $(seq 1 200); do
  if [[ -z "$URL" ]] && grep -q '=== FALLBACK_TRIGGER_URL ===' "$LOG" 2>/dev/null; then
    URL=$(awk '/=== FALLBACK_TRIGGER_URL ===/{getline; print; exit}' "$LOG")
    if [[ -n "$URL" && ! -f "$FALLBACK_FILE" ]]; then
      curl -fsSL --max-time 120 -A 'ExcaliburBlogPublish/1.0' "$URL" -o "$FALLBACK_FILE" || true
    fi
  fi
  if ! kill -0 "$PID" 2>/dev/null; then
    wait "$PID" || true
    cat "$LOG"
    exit "$(grep -q 'OK post=' "$LOG" && echo 0 || echo 1)"
  fi
  sleep 1
done

kill "$PID" 2>/dev/null || true
echo "Publish watcher timed out" >&2
cat "$LOG"
exit 1
