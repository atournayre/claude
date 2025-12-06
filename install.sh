#!/bin/bash

set -e

CLAUDE_DIR="$HOME/.claude"
BACKUP_DIR="$HOME/.claude.backup.$(date +%s)"
TEMP_CLONE_DIR="$HOME/.claude.temp.$$"
REPO_URL="git@github.com:atournayre/claude.git"

# Fichiers/dossiers gérés par le repo (à ne pas restaurer depuis le backup)
REPO_MANAGED="\.git|install\.sh|README\.md|\.gitignore|git-hooks"

echo "🔍 Vérification de l'installation..."

# Cloner d'abord dans un répertoire temporaire (fail-safe)
echo "📥 Clonage du repository..."
if ! git clone "$REPO_URL" "$TEMP_CLONE_DIR"; then
    echo "❌ Échec du clonage. Aucune modification effectuée."
    rm -rf "$TEMP_CLONE_DIR"
    exit 1
fi

# Sauvegarder si le répertoire existe
if [ -d "$CLAUDE_DIR" ]; then
    echo "📦 Sauvegarde du contenu existant dans $BACKUP_DIR..."
    mv "$CLAUDE_DIR" "$BACKUP_DIR"
fi

# Déplacer le clone vers sa destination finale
mv "$TEMP_CLONE_DIR" "$CLAUDE_DIR"

# Restaurer TOUT le contenu sauvegardé (sauf fichiers du repo)
if [ -d "$BACKUP_DIR" ]; then
    echo "♻️  Restauration du contenu personnel..."

    # Restaurer tous les fichiers/dossiers non gérés par le repo
    for item in "$BACKUP_DIR"/*; do
        [ -e "$item" ] || continue
        basename=$(basename "$item")
        if [[ ! "$basename" =~ ^($REPO_MANAGED)$ ]]; then
            cp -r "$item" "$CLAUDE_DIR/"
        fi
    done

    # Restaurer les fichiers cachés aussi
    for item in "$BACKUP_DIR"/.*; do
        [ -e "$item" ] || continue
        basename=$(basename "$item")
        [[ "$basename" =~ ^\.{1,2}$ ]] && continue
        [[ "$basename" == ".git" ]] && continue
        cp -r "$item" "$CLAUDE_DIR/"
    done

    echo "✅ Contenu restauré. Backup conservé dans $BACKUP_DIR"
fi

# Installer les marketplaces (si claude CLI disponible)
if command -v claude &> /dev/null; then
    echo "📦 Installation des marketplaces..."
    claude plugin marketplace add atournayre/claude-marketplace
    claude plugin marketplace add anthropics/claude-code
else
    echo "⚠️  Claude CLI non trouvé. Marketplaces à installer manuellement:"
    echo "   claude plugin marketplace add atournayre/claude-marketplace"
    echo "   claude plugin marketplace add anthropics/claude-code"
fi

# Installer les git hooks
if [ -f "$CLAUDE_DIR/git-hooks/install-hooks.sh" ]; then
    echo "🔗 Installation des git hooks..."
    bash "$CLAUDE_DIR/git-hooks/install-hooks.sh"
fi

echo ""
echo "✨ Installation terminée!"
echo ""
echo "📝 Prochaines étapes:"
echo "   1. Vérifiez settings.json et fusionnez settings.json.backup si nécessaire"
echo "   2. Activez les plugins souhaités dans settings.json"
echo ""
