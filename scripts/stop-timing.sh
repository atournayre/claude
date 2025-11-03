#!/bin/bash
# Stop timing helper - calculate and display duration

TIMING_FILE="$CLAUDE_PROJECT_DIR/.claude/tmp/.claude_timing"

if [[ ! -f "$TIMING_FILE" ]]; then
    cat <<EOF
{
  "systemMessage": "⏱️ Timing data not found",
  "suppressOutput": true
}
EOF
    exit 0
fi

# Load start data
source "$TIMING_FILE"

# Capture end
END_TIMESTAMP=$(date +%s)
END_DATE=$(date '+%Y-%m-%d %H:%M:%S %Z')

# Calculate duration
DURATION=$((END_TIMESTAMP - START_TIMESTAMP))

# Format duration
if [[ $DURATION -lt 60 ]]; then
    DURATION_FORMATTED="${DURATION}s"
elif [[ $DURATION -lt 3600 ]]; then
    MINUTES=$((DURATION / 60))
    SECONDS=$((DURATION % 60))
    DURATION_FORMATTED="${MINUTES}m ${SECONDS}s"
else
    HOURS=$((DURATION / 3600))
    MINUTES=$(((DURATION % 3600) / 60))
    SECONDS=$((DURATION % 60))
    DURATION_FORMATTED="${HOURS}h ${MINUTES}m ${SECONDS}s"
fi

# JSON output with systemMessage for Stop hook
cat <<EOF
{
  "systemMessage": "✅ Terminé: $END_DATE\n⏱️ Durée: $DURATION_FORMATTED",
  "suppressOutput": true
}
EOF
