#!/bin/bash

set -e

HOOKS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GIT_HOOKS_DIR="$HOOKS_DIR/../.git/hooks"

echo "🔗 Installation des git hooks..."

# Copier post-merge
if [ -f "$HOOKS_DIR/post-merge" ]; then
    cp "$HOOKS_DIR/post-merge" "$GIT_HOOKS_DIR/post-merge"
    chmod +x "$GIT_HOOKS_DIR/post-merge"
    echo "✅ post-merge installé"
fi

echo "✨ Git hooks installés avec succès"
