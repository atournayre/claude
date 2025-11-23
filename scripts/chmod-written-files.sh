#!/bin/bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path')
if [ -n "$file_path" ] && [ "$file_path" != "null" ]; then
    chmod 644 "$file_path"
    chmod 755 "$(dirname "$file_path")"
fi
