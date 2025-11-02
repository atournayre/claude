# Configuration Claude Code

Configuration personnalisée pour [Claude Code](https://claude.com/claude-code) - assistant de développement IA.

## Structure

```
~/.claude/
├── CLAUDE.md              # Préférences utilisateur et instructions globales
├── settings.json          # Configuration Claude Code
├── commands/              # Slash commands personnalisées (non versionnées)
├── hooks/                # Hooks personnalisés (non versionnés)
├── plugins/              # Plugins installés (non versionnés)
├── status-line/          # Script de status line personnalisée
└── mcp/                  # Serveurs MCP
```

**Note**: Les dossiers `commands/`, `hooks/` et `plugins/` contiennent votre configuration personnelle et ne sont pas versionnés dans git.

## Commandes disponibles

Les slash commands sont stockées dans le dossier `commands/` (non versionné).

Pour voir la liste complète des commandes disponibles :
```bash
ls -R ~/.claude/commands/
```

Ou utilisez l'autocomplétion en tapant `/` dans Claude Code.

## Préférences

Défini dans `CLAUDE.md`:
- Ton casual, pas formel
- Réponses courtes et concises
- Listes plutôt que paragraphes
- Toujours écrire des tests
- Éviter phrases trop positives

## Permissions

Auto-approuvées (défini dans `settings.json`):
- Commandes Git (add, commit, push, branch, etc.)
- GitHub CLI (gh pr, gh issue, etc.)
- Composer, PHP, Symfony console
- Docker & Docker Compose
- PHPStan, PHPUnit
- WebFetch pour docs officielles

## Status Line

Status line personnalisée affichant:
- Modèle agent actuel
- Informations Git
- Durée de session
- Utilisation tokens
- Nom de session
- Coût journalier

## Installation

---

### ⚠️ AVERTISSEMENT IMPORTANT ⚠️

**L'installation va ÉCRASER votre `~/.claude/settings.json` existant !**

**SAUVEGARDEZ AVANT D'INSTALLER :**

```bash
# Sauvegarder votre configuration actuelle
cp ~/.claude/settings.json ~/.claude/settings.json.backup
```

---

### Procédure d'installation

```bash
git clone git@github.com:atournayre/claude.git ~/.claude
```

### Après installation

Vérifiez et fusionnez manuellement vos paramètres personnels depuis `settings.json.backup` si nécessaire.

## Fichiers ignorés

Le `.gitignore` exclut:
- **Configuration personnelle** : `commands/`, `hooks/`, `plugins/`
- **Credentials et clés** : `.credentials.json`, `*.key`, `*.pem`, `*.p12`
- **Historique et sessions** : `history.jsonl`, `file-history/`, `session-env/`, `shell-snapshots/`
- **Logs et debug** : `debug/`, `logs/`, `*.log`
- **Cache et données temporaires** : `todos/`, `statsig/`, `local/`, `task/`, `ide/`, `data/`
- **Rapports** : `reports/` (peuvent être regénérés)
- **Documentation externe** : `docs/` (peut être rechargée)
- **Projets locaux** : `projects/`

## Licence

Configuration personnelle - À adapter selon vos besoins.
