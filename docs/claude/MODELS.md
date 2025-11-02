# Modèles Claude pour les Slash Commands

## Vue d'Ensemble

Chaque slash command dans ce projet est configurée pour utiliser le modèle Claude le plus approprié basé sur la complexité de la tâche. Ce document explique les modèles disponibles, les critères de sélection et liste toutes les commandes par modèle.

## Modèles Disponibles

### Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)

**Caractéristiques :**
- Modèle rapide et économique
- Excellent pour les tâches simples et répétitives
- Temps de réponse minimal
- Coût optimisé
- Dernière génération de la famille Haiku

**Cas d'usage idéaux :**
- Commandes de navigation et d'information simple
- Opérations Git basiques (statut, listing)
- Affichage d'aide et de statut
- Commandes avec peu ou pas de logique complexe
- Tâches fréquemment exécutées

### Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)

**Caractéristiques :**
- Modèle le plus récent de la gamme Sonnet
- Modèle par défaut, équilibre optimal
- Très bon rapport performance/coût
- Capable de gérer la majorité des tâches
- Excellent pour le code et l'analyse technique

**Cas d'usage idéaux :**
- Analyse de code et refactoring
- Génération de code avec patterns standards
- Opérations Git complexes (commits, PR, conflits)
- Documentation technique
- Résolution de bugs standards
- Intégrations et workflows

### Claude Opus 4.1 (`claude-opus-4-1-20250805`)

**Caractéristiques :**
- Modèle le plus puissant et capable de la gamme Opus
- Raisonnement approfondi et analytique
- Excellent pour les problèmes complexes
- Meilleur pour les décisions architecturales

**Cas d'usage idéaux :**
- Analyse approfondie et raisonnement complexe
- Architecture Decision Records (ADR)
- Résolution d'erreurs complexes (PHPStan niveau 9)
- Analyse d'impact de changements majeurs
- Génération de commandes ou d'agents
- Tâches nécessitant une compréhension profonde du contexte

## Critères de Sélection

### Complexité de la Tâche
- **Simple** → Haiku : Opérations directes, pas de logique conditionnelle
- **Moyenne** → Sonnet : Analyse, génération de code, workflows standards
- **Complexe** → Opus : Problèmes nécessitant raisonnement multi-étapes

### Fréquence d'Usage
- **Très fréquent** → Haiku : Optimiser les coûts pour usage répété
- **Fréquent** → Sonnet : Balance entre performance et coût
- **Occasionnel** → Opus : Qualité maximale quand nécessaire

### Impact et Criticité
- **Faible impact** → Haiku : Erreurs acceptables, tâches non critiques
- **Impact moyen** → Sonnet : Qualité importante mais pas critique
- **Impact élevé** → Opus : Décisions architecturales, analyses critiques

## Liste des Commandes par Modèle

### Commandes Haiku (6 total)

| Commande | Description | Raison |
|----------|-------------|---------|
| `/analytics-stop` | Arrêter le serveur analytics | Simple commande d'arrêt de processus |
| `/sessions:help` | Afficher l'aide sessions | Affichage statique d'informations |
| `/sessions:list` | Lister les sessions | Lecture et affichage simple |
| `/sessions:current` | Statut session actuelle | Lecture de fichier et affichage |
| `/git:status` | Statut Git du dépôt | Commandes git basiques |
| `/cc:challenge` | Évaluer ma dernière réponse | Évaluation structurée simple |

### Commandes Sonnet (24 total)

#### Workflow et Build
| Commande | Description |
|----------|-------------|
| `/code` | Construire selon un plan |
| `/prepare` | Créer un plan rapide |
| `/analytics` | Lancer analytics dashboard |

#### Sessions
| Commande | Description |
|----------|-------------|
| `/sessions:start` | Démarrer une session |
| `/sessions:update` | Mettre à jour session |
| `/sessions:end` | Terminer session avec rapport |

#### Git Operations
| Commande | Description |
|----------|-------------|
| `/git:commit` | Commits conventionnels |
| `/git:branch` | Créer des branches |
| `/git:pr` | Créer Pull Requests |
| `/git:conflit` | Résoudre conflits |

#### GitHub & Issues
| Commande | Description |
|----------|-------------|
| `/github:fix` | Corriger une issue GitHub |

#### Documentation
| Commande | Description |
|----------|-------------|
| `/doc:rtfm` | Lire documentation |
| `/doc:update` | Mettre à jour documentation |
| `/load:doc:symfony` | Charger docs Symfony |
| `/load:doc:api-platform` | Charger docs API Platform |
| `/load:doc:claude` | Charger docs Claude |
| `/load:doc:atournayre-framework` | Charger docs framework |
| `/load:doc:meilisearch` | Charger docs Meilisearch |

#### Contexte et Debug
| Commande | Description |
|----------|-------------|
| `/context:default` | Charger contexte par défaut |
| `/context:elegant_object` | Règles Elegant Objects |
| `/debug:stack-trace` | Analyser stack traces |
| `/debug:error-fix` | Corriger erreurs |

#### Utilitaires
| Commande | Description |
|----------|-------------|
| `/question` | Répondre aux questions |
| `/cc:make:command` | Générer nouvelles commandes |

### Commandes Opus (6 total)

| Commande | Description | Raison |
|----------|-------------|---------|
| `/think:harder` | Analyse intensive | Raisonnement approfondi requis |
| `/think:ultra` | Analyse ultra-complexe | Problèmes les plus complexes |
| `/doc:adr` | Générer ADR | Décisions architecturales critiques |
| `/qa:phpstan` | Résoudre erreurs PHPStan | PHPStan niveau 9, typage strict |
| `/analyse:impact` | Analyser impact PR | Analyse technique et métier |
| `/all_tools` | Accès tous outils | Flexibilité maximale pour tâches variées |

## Bonnes Pratiques

### Pour les Utilisateurs
- **Haiku** : Utiliser pour les commandes rapides et fréquentes
- **Sonnet** : Utiliser par défaut pour les tâches de développement
- **Opus** : Réserver pour les décisions importantes et analyses complexes

### Pour les Développeurs de Commandes
1. **Commencer par Haiku** si la tâche est simple et bien définie
2. **Utiliser Sonnet par défaut** pour les nouvelles commandes
3. **Passer à Opus** uniquement si :
   - La tâche nécessite un raisonnement multi-étapes complexe
   - Les décisions ont un impact architectural important
   - La qualité est absolument critique

### Éviter
- ❌ Utiliser Opus pour des tâches que Sonnet peut gérer
- ❌ Utiliser Haiku pour des tâches nécessitant de l'analyse
- ❌ Changer de modèle sans raison valable

## Maintenance et Évolution

### Ajouter une Nouvelle Commande
1. Évaluer la complexité de la tâche
2. Choisir le modèle selon les critères ci-dessus
3. Ajouter le champ `model` dans le frontmatter avec la version spécifique :
   - Haiku : `model: claude-haiku-4-5-20251001`
   - Sonnet : `model: claude-sonnet-4-5-20250929`
   - Opus : `model: claude-opus-4-1-20250805`
4. Mettre à jour ce document

### Changer le Modèle d'une Commande
1. Identifier pourquoi le modèle actuel n'est pas optimal
2. Tester avec le nouveau modèle
3. Documenter la raison du changement
4. Mettre à jour ce document

### Script de Validation
```bash
# Vérifier que toutes les commandes ont un modèle
for file in commands/**/*.md; do
  if ! grep -q "^model:" "$file"; then
    echo "❌ Missing model in: $file"
  fi
done
```

## Statistiques

- **Total commandes** : 36
- **Haiku** : 6 (17%) - Tâches simples et fréquentes
- **Sonnet** : 24 (67%) - Tâches moyennes, modèle par défaut
- **Opus** : 6 (16%) - Tâches complexes et critiques

Cette répartition optimise le rapport qualité/coût tout en garantissant la performance sur les tâches critiques.

## Références

- [Documentation Claude Models](https://docs.anthropic.com/en/docs/models-overview)
- [Plan d'implémentation](specs/add-model-to-slash-commands.md)
- [CLAUDE.md](../CLAUDE.md) - Configuration projet