# Configuration Claude Code

Configuration personnalisée pour [Claude Code](https://claude.com/claude-code) - assistant de développement IA.

## Structure

```
~/.claude/
├── CLAUDE.md              # Préférences utilisateur et instructions globales
├── settings.json          # Configuration Claude Code
├── commands/              # Slash commands personnalisées
│   ├── git/              # Commandes Git (commit, branch, PR, conflits, status)
│   ├── github/           # Intégration GitHub (fix issues)
│   ├── symfony/          # Commandes Symfony (make, documentation)
│   ├── docker/           # Gestion Docker
│   ├── debug/            # Debugging (stack-trace, error-fix)
│   ├── qa/               # Qualité (PHPStan)
│   ├── doc/              # Documentation (ADR, update, RTFM)
│   ├── analyse/          # Analyse d'impact PR
│   ├── api-platform/     # Documentation API Platform
│   ├── meilisearch/      # Documentation Meilisearch
│   ├── claude/           # Documentation Claude Code
│   ├── atournayre-framework/ # Documentation framework custom
│   ├── cc/               # Utilitaires Claude Code
│   ├── context/          # Chargement de contexte
│   ├── sessions/         # Gestion de sessions de développement
│   ├── think/            # Analyse approfondie
│   └── alias/            # Alias de commandes
├── hooks/                # Git hooks et événements
├── status-line/          # Script de status line personnalisée
└── mcp/                  # Serveurs MCP
```

## Commandes principales

### Git & GitHub
- `/git:commit` - Commits avec format conventional + emojis
- `/git:branch` - Création de branches structurées
- `/git:pr` - Pull Requests optimisées avec workflow
- `/git:conflit` - Résolution de conflits guidée
- `/git:status` - État du dépôt
- `/github:fix` - Corriger une issue GitHub

### Symfony & PHP
- `/symfony:make` - Utilise les makers Symfony ou `/prepare`
- `/symfony:doc:load` - Charger doc Symfony locale
- `/symfony:doc:question` - Interroger la doc Symfony
- `/qa:phpstan` - Résoudre erreurs PHPStan

### Documentation
- `/doc:adr` - Générer Architecture Decision Records
- `/doc:update` - Créer/mettre à jour la documentation
- `/doc:rtfm` - Lire documentation technique
- `/api-platform:doc:load|question` - Doc API Platform
- `/meilisearch:doc:load|question` - Doc Meilisearch
- `/claude:doc:load|question` - Doc Claude Code

### Développement
- `/docker` - Actions avec Docker
- `/debug:stack-trace` - Analyser une stack trace
- `/debug:error-fix` - Résoudre une erreur
- `/analyse:impact` - Analyser impact d'une PR
- `/code` - Coder selon un plan
- `/question` - Questions sur le projet sans coder

### Utilitaires
- `/sessions:start|end|current|list|update` - Gestion de sessions
- `/think:harder|ultra` - Analyse approfondie
- `/context:default|elegant_object` - Charger contexte
- `/cc:make:command` - Générer nouvelles slash commands
- `/cc:challenge` - Évaluer une réponse
- `/alias:add` - Créer alias de commande

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

```bash
git clone git@github.com:atournayre/claude.git ~/.claude
```

## Fichiers ignorés

Le `.gitignore` exclut:
- Credentials et clés
- Historique et sessions (volumineux)
- Logs et debug
- Cache et données temporaires
- Documentation externe (rechargeable)
- Projets locaux

## Licence

Configuration personnelle - À adapter selon vos besoins.
