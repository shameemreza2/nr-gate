#!/usr/bin/env bash
# hooks/gate-ci.sh — server-side mirror of hooks/commit-msg for GitHub Actions.
# Reads from the committed tree (no staging area) rather than git show :file.
# Usage: hooks/gate-ci.sh <before-sha> <after-sha>
# ---------------------------------------------------------------------------
set -uo pipefail

BEFORE="${1:-}"
AFTER="${2:-$(git rev-parse HEAD)}"

# Global: written inside check_commit, consumed by row_for.
SECT=""

row_for() {
  local d="$1"
  printf '%s\n' "$SECT" | awk -F'|' -v d="$d" '
    { k=$2; gsub(/^[ \t]+|[ \t]+$/,"",k) }
    k ~ /^[0-9]+$/ && (k+0)==(d+0) { print; exit }'
}

passed() {
  local r="$1"
  printf '%s' "$r" | grep -q '✅' || return 1
  local h
  h="$(printf '%s' "$r" | awk -F'|' '{gsub(/^[ \t]+|[ \t]+$/,"",$4); print $4}')"
  [ -n "$h" ] || return 1
  return 0
}

check_commit() {
  local sha="$1"
  local MSG
  MSG="$(git log -1 --format='%s' "$sha")"

  # Only police day-card commits
  if ! printf '%s' "$MSG" | grep -Eq '^(p2-)?day[0-9]+'; then
    return 0
  fi

  local token is_p2 day is_slip phase_name
  token="$(printf '%s' "$MSG" | grep -Eo '^(p2-)?day[0-9]+(-r[0-9]+)?')"
  is_p2=0; case "$token" in p2-*) is_p2=1 ;; esac
  day="$(printf '%s' "$token" | grep -Eo 'day[0-9]+' | grep -Eo '[0-9]+')"
  day=$((10#$day))
  is_slip=0; case "$token" in *-r[0-9]*) is_slip=1 ;; esac
  phase_name="Phase1"; [ "$is_p2" -eq 1 ] && phase_name="Phase2"

  # Slips are honest record-keeping — always pass
  [ "$is_slip" -eq 1 ] && return 0

  local TRACK
  TRACK="$(git show "${sha}:tracker.md" 2>/dev/null || true)"
  if [ -z "$TRACK" ]; then
    echo "GATE BLOCK [$sha]: tracker.md not found in commit tree." >&2
    return 1
  fi

  local marker
  marker='# Phase 2 Tracker'
  if [ "$is_p2" -eq 1 ]; then
    SECT="$(printf '%s\n' "$TRACK" | awk -v m="$marker" 'f{print} index($0,m){f=1}')"
  else
    SECT="$(printf '%s\n' "$TRACK" | awk -v m="$marker" 'index($0,m){exit} {print}')"
  fi

  local row
  row="$(row_for "$day")"
  if [ -z "$row" ]; then
    echo "GATE BLOCK [$sha]: no $phase_name tracker row for day $day." >&2
    return 1
  fi
  if ! passed "$row"; then
    echo "GATE BLOCK [$sha]: day $day not PASS in $phase_name tracker (needs hours + ✅)." >&2
    printf '  row: %s\n' "$row" >&2
    return 1
  fi

  if [ "$day" -gt 0 ]; then
    local prev prow
    prev=$((day - 1))
    prow="$(row_for "$prev")"
    if [ -n "$prow" ] && ! passed "$prow"; then
      echo "GATE BLOCK [$sha]: day $day blocked — day $prev is not ✅ yet (no skipping)." >&2
      return 1
    fi
  fi

  echo "GATE OK: $phase_name day $day ✅  ($sha)"
  return 0
}

# Determine commit range.
# BEFORE = all zeros on a brand-new branch: only check HEAD to avoid
# failing on pre-hook historical commits.
if [ -z "$BEFORE" ] || [ "$BEFORE" = "0000000000000000000000000000000000000000" ]; then
  COMMITS="$AFTER"
else
  COMMITS="$(git log --format='%H' "${BEFORE}..${AFTER}" 2>/dev/null || true)"
  [ -z "$COMMITS" ] && COMMITS="$AFTER"
fi

fail=0
for sha in $COMMITS; do
  check_commit "$sha" || fail=1
done

if [ "$fail" -eq 0 ]; then
  echo "All gate checks passed."
else
  echo "" >&2
  echo "Gate discipline violated — push rejected." >&2
  echo "Fill tracker.md (hours + ✅), commit normally (no --no-verify), and re-push." >&2
fi

exit "$fail"
