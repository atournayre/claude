#!/bin/bash
# Start timing helper - capture start time and display

START_DATE=$(date '+%Y-%m-%d %H:%M:%S %Z')

# JSON output with additionalContext for SessionStart/UserPromptSubmit
cat <<EOF
{
  "additionalContext": "🕐 Démarrage: $START_DATE",
  "suppressOutput": true
}
EOF
