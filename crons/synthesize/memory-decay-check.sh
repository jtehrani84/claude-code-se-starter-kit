#!/bin/bash
# Memory Decay Checker
# Runs weekly (Sunday 6 AM). Identifies memory files that may be stale.
# Appends recommendations to wiki/inbox.md for review during /curate.
#
# No LLM call — pure date math + grep.

set -euo pipefail

# Auto-detect project memory directory
MEMORY_DIR=$(find "$HOME/.claude/projects" -maxdepth 2 -name "memory" -type d 2>/dev/null | head -1)
# Wiki inbox — adjust path to your project
INBOX="$HOME/wiki/inbox.md"
[ -f "$INBOX" ] || INBOX=$(find "$HOME" -maxdepth 3 -path "*/wiki/inbox.md" -type f 2>/dev/null | head -1)
TODAY=$(date +%Y-%m-%d)
LOG_DIR="$HOME/.claude/crons/logs"
THRESHOLD_DAYS=45

mkdir -p "$LOG_DIR"

echo "$(date): Running memory decay check (threshold: ${THRESHOLD_DAYS} days)" >> "$LOG_DIR/decay.log"

STALE_COUNT=0
STALE_FILES=""

# Check each memory file for date references
for f in "$MEMORY_DIR"/*.md; do
    [ -f "$f" ] || continue
    basename_f=$(basename "$f")

    # Skip MEMORY.md index
    [ "$basename_f" = "MEMORY.md" ] && continue

    # Check git last-modified date
    LAST_MODIFIED=$(git -C "$MEMORY_DIR" log -1 --format="%ai" -- "$basename_f" 2>/dev/null | cut -d' ' -f1)

    if [ -n "$LAST_MODIFIED" ]; then
        # Calculate days since last modification
        LAST_MOD_EPOCH=$(date -j -f "%Y-%m-%d" "$LAST_MODIFIED" +%s 2>/dev/null || echo "0")
        TODAY_EPOCH=$(date +%s)
        DAYS_AGO=$(( (TODAY_EPOCH - LAST_MOD_EPOCH) / 86400 ))

        if [ "$DAYS_AGO" -gt "$THRESHOLD_DAYS" ]; then
            STALE_COUNT=$((STALE_COUNT + 1))
            STALE_FILES="$STALE_FILES\n- $basename_f (${DAYS_AGO}d ago)"
        fi
    fi
done

# Append to inbox if stale files found
if [ "$STALE_COUNT" -gt 0 ]; then
    echo "" >> "$INBOX"
    echo "## ${TODAY} — Memory Decay Check" >> "$INBOX"
    echo "${STALE_COUNT} memory files unchanged for >${THRESHOLD_DAYS} days:" >> "$INBOX"
    echo -e "$STALE_FILES" >> "$INBOX"
    echo "Review during next /curate session." >> "$INBOX"
    echo "$(date): Found $STALE_COUNT stale memories, appended to inbox" >> "$LOG_DIR/decay.log"
else
    echo "$(date): All memories fresh (< ${THRESHOLD_DAYS} days)" >> "$LOG_DIR/decay.log"
fi
