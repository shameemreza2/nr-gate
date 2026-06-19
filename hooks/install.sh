#!/usr/bin/env bash
# Install the gate hook for this repo.
# Run once per clone:  bash hooks/install.sh
set -e
git config core.hooksPath hooks
chmod +x hooks/commit-msg 2>/dev/null || true
echo "Gate hook installed: core.hooksPath=hooks"
echo "From now on, a day-card PASS commit is blocked unless tracker.md proves the gate."
echo "(Bypass with 'git commit --no-verify' = breaking your own gate. Don't.)"
