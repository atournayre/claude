# Troubleshooting Guide - Claude Code

**Source:** https://docs.claude.com/en/docs/claude-code/troubleshooting.md
**Extrait le:** 2025-11-02
**Sujet:** Troubleshooting & Debugging

---

## Installation Problems

### Windows/WSL Issues

Le guide traite trois problèmes principaux dans les environnements WSL :

1. **Détection OS** : Exécuter `npm config set os linux` avant l'installation, ou utiliser `npm install -g @anthropic-ai/claude-code --force --no-os-check` sans sudo.

2. **Node Not Found** : Vérifier avec `which npm` et `which node`. Si les chemins commencent par `/mnt/c/`, vous utilisez Node Windows. Solution : installer via le gestionnaire de paquets de votre distribution Linux ou nvm.

3. **Conflits de versions nvm** : Quand nvm existe à la fois dans WSL et Windows, les versions Windows peuvent avoir la priorité. La solution principale implique de s'assurer que nvm se charge dans votre fichier de configuration shell :

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

Alternativement, préfixer les chemins Linux à votre variable PATH.

### Installation Linux/Mac

Pour les erreurs de permissions ou command-not-found, le document recommande un installateur natif (actuellement en beta) :

**Systèmes Unix :**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell :**
```powershell
irm https://claude.ai/install.ps1 | iex
```

Alternativement, migrer vers l'installation locale : `claude migrate-installer`

## Authentication & Permissions

- Les invites de permissions répétées peuvent être gérées via la commande `/permissions`
- Les problèmes d'authentification se résolvent en exécutant `/logout`, redémarrant, puis en utilisant `claude`
- Les problèmes persistants peuvent nécessiter la suppression de `~/.config/claude-code/auth.json`

## Performance Issues

- Utiliser `/compact` pour réduire la taille du contexte pour les grandes codebases
- Installer `ripgrep` système si Search et les mentions de fichiers ne fonctionnent pas
- Les pénalités de performance du système de fichiers WSL peuvent réduire les résultats de recherche ; déplacer les projets vers le système de fichiers Linux aide
- La détection IDE JetBrains sur WSL2 nécessite la configuration du pare-feu Windows ou le mode réseau en miroir

## Markdown Generation

L'outil produit parfois des blocs de code sans balises de langage. Solutions : demander à Claude d'ajouter les balises, implémenter des hooks de post-traitement, ou utiliser des formateurs markdown comme Prettier.

## Ressources Additionnelles

- `/bug` pour signaler des problèmes
- Consulter GitHub pour les problèmes connus
- Exécuter `/doctor` pour vérifier la santé de l'installation
- Demander directement à Claude sur ses capacités

---

## Notes d'extraction

- Cette documentation couvre les solutions aux problèmes courants d'installation, authentification, performance, intégration IDE et formatage markdown
- Pour WSL, privilégier `npm config set os linux` et les flags `--force --no-os-check`
- L'installateur natif via curl est recommandé pour Linux/Mac pour éviter les problèmes de permissions npm
- Commande `/permissions` pour gérer les autorisations d'outils
- Commande `/compact` pour optimiser les performances sur grandes codebases
- Installer `ripgrep` système pour améliorer la fonctionnalité de recherche
