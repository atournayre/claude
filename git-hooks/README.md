# Git Hooks

Ce dossier contient les git hooks pour automatiser les tâches après mise à jour du projet.

## Hooks disponibles

### post-merge

Exécuté automatiquement après `git pull` ou `git merge`.

Actions :
- Détecte changements dans `settings.json` et avertit
- Met à jour automatiquement les marketplaces si fichiers plugins modifiés
- Notifie si `install.sh` a changé

## Installation

Les hooks sont installés automatiquement par `install.sh`.

Installation manuelle :
```bash
bash hooks/install-hooks.sh
```

## Test

Simuler post-merge :
```bash
.git/hooks/post-merge
```
