#!/bin/bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path')
if [ -n "$file_path" ] && [ "$file_path" != "null" ]; then
    chown "$USER:$USER" "$file_path"
    chown "$USER:$USER" "$(dirname "$file_path")"
fi
