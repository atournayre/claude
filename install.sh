#!/bin/bash

set -e

CLAUDE_DIR="$HOME/.claude"
BACKUP_DIR="$HOME/.claude.backup.$(date +%s)"
REPO_URL="git@github.com:atournayre/claude.git"

echo "🔍 Vérification de l'installation..."

# Sauvegarder si le répertoire existe
if [ -d "$CLAUDE_DIR" ]; then
    echo "📦 Sauvegarde du contenu existant dans $BACKUP_DIR..."
    cp -r "$CLAUDE_DIR" "$BACKUP_DIR"
    rm -rf "$CLAUDE_DIR"
fi

# Cloner le repo
echo "📥 Clonage du repository..."
git clone "$REPO_URL" "$CLAUDE_DIR"

# Restaurer le contenu sauvegardé
if [ -d "$BACKUP_DIR" ]; then
    echo "♻️  Restauration du contenu personnel..."

    # Restaurer commands, hooks, plugins
    [ -d "$BACKUP_DIR/commands" ] && cp -r "$BACKUP_DIR/commands" "$CLAUDE_DIR/"
    [ -d "$BACKUP_DIR/hooks" ] && cp -r "$BACKUP_DIR/hooks" "$CLAUDE_DIR/"
    [ -d "$BACKUP_DIR/plugins" ] && cp -r "$BACKUP_DIR/plugins" "$CLAUDE_DIR/"

    # Sauvegarder settings.json existant
    if [ -f "$BACKUP_DIR/settings.json" ]; then
        echo "⚠️  settings.json existant sauvegardé dans $CLAUDE_DIR/settings.json.backup"
        cp "$BACKUP_DIR/settings.json" "$CLAUDE_DIR/settings.json.backup"
    fi

    echo "✅ Backup conservé dans $BACKUP_DIR"
fi

# Installer les marketplaces
echo "📦 Installation des marketplaces..."
claude plugin marketplace add atournayre/claude-marketplace
claude plugin marketplace add anthropics/claude-code

echo ""
echo "✨ Installation terminée!"
echo ""
echo "📝 Prochaines étapes:"
echo "   1. Vérifiez settings.json et fusionnez settings.json.backup si nécessaire"
echo "   2. Activez les plugins souhaités dans settings.json"
echo ""
