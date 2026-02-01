# Configuration Claude Code

Configuration personnalisée pour [Claude Code](https://claude.com/claude-code) - assistant de développement IA.

## Structure

```
~/.claude/
├── CLAUDE.md                  # Préférences utilisateur et instructions globales
├── settings.json              # Configuration Claude Code
├── commands/                  # Slash commands personnalisées (non versionnées)
├── hooks/                     # Hooks personnalisés (non versionnés)
├── plugins/                   # Plugins installés (non versionnés)
├── git-hooks/                 # Git hooks pour automatisation
│   ├── post-merge             # Hook exécuté après git pull/merge
│   └── install-hooks.sh       # Script installation hooks
├── scripts/                   # Scripts utilitaires
│   ├── kyutai-tts-installer/  # Installer Kyutai TTS
│   ├── notification-kyutai.sh # Hook notifications vocales
│   └── ...
├── status-line/               # Script de status line personnalisée
├── docs/                      # Documentation (non versionnée)
└── mcp/                       # Serveurs MCP
    ├── sentry.json            # Monitoring Sentry
    ├── chrome-dev-tools.json  # Chrome DevTools
    └── context7.json          # Context7 (doc code)
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

## Prompts Système

Prompts additionnels stockés dans `prompts/append-system/`:

**Chrome** (`chrome.txt`):
Force l'utilisation de Chrome pour tester les fonctionnalités web.

Usage:
```bash
# Mode print
claude -p --append-system-prompt-file ~/.claude/prompts/append-system/chrome.txt "query"

# Mode interactif
claude --append-system-prompt "$(cat ~/.claude/prompts/append-system/chrome.txt)"
```

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

## Notifications Vocales

Notifications vocales avec **Kyutai TTS** pour les événements Claude Code (permissions, idle, auth success, etc.).

**Documentation complète**: [docs/kyutai-tts.md](docs/kyutai-tts.md)

**Installation rapide**:
```bash
cd ~/.claude/scripts/kyutai-tts-installer
./install.sh
```

Prérequis: Docker + GPU NVIDIA (8GB+ VRAM)

## Notifications Desktop

Notifications desktop visuelles pour les événements clés de Claude Code, avec emojis spécifiques par type et affichage du titre de session (si défini via `/rename`).

### Types de notifications

| Type | Emoji | Description |
|------|-------|-------------|
| `permission_prompt` | 🔐 | Demandes de permission |
| `idle_prompt` | ⏰ | Attente input utilisateur (60+ sec) |
| `auth_success` | ✅ | Authentification réussie |
| `elicitation_dialog` | ❓ | Input requis pour MCP |
| Tâche terminée | ✅ | Fin de session principale |
| Sous-agent terminé | 🤖 | Fin de sous-agent |

### Configuration

Les notifications desktop sont configurées dans `settings.json` :

```json
{
  "env": {
    "CLAUDE_DESKTOP_NOTIFY": "true",
    "CLAUDE_DESKTOP_NOTIFY_URGENCY": "normal",
    "CLAUDE_DESKTOP_NOTIFY_TIMEOUT": "5000"
  },
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/notification.py --desktop"
          }
        ]
      }
    ]
  }
}
```

### Titre de session personnalisé

Utilisez `/rename` pour définir un titre personnalisé qui s'affichera dans les notifications :

```bash
# Dans Claude Code
/rename "Amélioration notifications desktop"
```

**Sans titre** :
- Notification : "✅ Claude Code - Tâche terminée"
- Corps : "Session: abc123\nDurée: 45.2s"

**Avec titre** :
- Notification : "✅ Amélioration notifications desktop"
- Corps : "Durée: 45.2s"

### Dépendances

**Linux** (Ubuntu/Debian) :
```bash
sudo apt install libnotify-bin
```

Vérification :
```bash
which notify-send
```

### Désactivation

Pour désactiver les notifications desktop :

```json
{
  "env": {
    "CLAUDE_DESKTOP_NOTIFY": "false"
  }
}
```

## Serveurs MCP

**Documentation complète**: [docs/mcp-servers.md](docs/mcp-servers.md)

Serveurs installés:
- **Sentry**: Monitoring erreurs et performance
- **Chrome DevTools**: Debug navigateur en temps réel
- **Context7**: Documentation code pour LLMs (repos GitHub/GitLab)
- **n8n**: Workflows d'automatisation et intégrations

## Installation

### Installation automatique (recommandé)

```bash
curl -sSL https://raw.githubusercontent.com/atournayre/claude/main/install.sh | bash
```

Le script d'installation :
- Sauvegarde automatiquement votre configuration existante
- Clone le repository
- Restaure vos fichiers personnels (`commands/`, `hooks/`, `plugins/`)
- Préserve votre `settings.json` dans `settings.json.backup`

### Installation manuelle

```bash
# 1. Télécharger et exécuter le script
wget https://raw.githubusercontent.com/atournayre/claude/main/install.sh
chmod +x install.sh
./install.sh
```

### Après installation

1. Vérifiez et fusionnez manuellement vos paramètres personnels depuis `settings.json.backup` si nécessaire

2. Les marketplaces sont installés automatiquement par le script

3. Les git hooks sont installés automatiquement - ils détectent et gèrent :
   - Changements dans `settings.json` → avertissement
   - Modifications plugins → mise à jour marketplaces
   - Changements `install.sh` → notification

## Git Hooks

Hooks automatiques pour maintenir votre configuration à jour après `git pull`.

**Hook post-merge** détecte automatiquement :
- `settings.json` modifié → avertit de vérifier/fusionner
- Fichiers plugins modifiés → met à jour les marketplaces
- `install.sh` modifié → suggère de relancer

**Installation manuelle** (déjà fait par `install.sh`) :
```bash
bash ~/.claude/git-hooks/install-hooks.sh
```

**Test** :
```bash
git pull  # Hook s'exécute automatiquement
# ou test direct :
~/.git/hooks/post-merge
```

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
