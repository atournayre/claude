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

## Serveurs MCP

**Documentation complète**: [docs/mcp-servers.md](docs/mcp-servers.md)

Serveurs installés:
- **Sentry**: Monitoring erreurs et performance
- **Chrome DevTools**: Debug navigateur en temps réel
- **Context7**: Documentation code pour LLMs (repos GitHub/GitLab)

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

2. Installez les marketplaces :
   ```bash
   /plugin marketplace add atournayre/claude-marketplace
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
