# Plan: Refonte plugin dev avec workflow unifié

## Objectif

Créer un workflow de développement structuré avec :
- Commandes numérotées (verbes)
- Commande orchestratrice `/dev:feature`
- Commande status `/dev:status` pour voir les étapes
- Réutilisation des agents `feature-dev` (pas de duplication)
- Conservation de `/dev:debug`

---

## Nouvelle structure de commandes

### Commandes du workflow principal

| Commande | Phase | Description |
|----------|-------|-------------|
| `/dev:feature [desc]` | - | Orchestrateur (enchaîne toutes les phases) |
| `/dev:status` | - | Affiche le plan et l'étape courante |
| `/dev:discover [desc]` | 0 | Comprendre le besoin |
| `/dev:explore` | 1 | Explorer codebase (agents parallèles) |
| `/dev:clarify` | 2 | Questions de clarification |
| `/dev:design` | 3 | Proposer 2-3 architectures |
| `/dev:plan` | 4 | Générer le plan dans docs/specs/ |
| `/dev:code [plan]` | 5 | Implémenter |
| `/dev:review` | 6 | QA (PHPStan + Elegant Objects + review) |
| `/dev:summary` | 7 | Résumé final |

### Commandes utilitaires (conservées)

| Commande | Description |
|----------|-------------|
| `/dev:debug [error]` | Analyse et résolution d'erreurs |
| `/dev:log [fichier]` | Ajout LoggableInterface |
| `/dev:docker` | Mode Docker |
| `/dev:question` | Questions sans code |

### Commandes supprimées

| Commande | Raison |
|----------|--------|
| `/dev:prepare` | Remplacé par `/dev:plan` |
| `/dev:context:load` | Peu utilisé, complexité inutile |

---

## Dépendance au plugin feature-dev

### Agents réutilisés (de feature-dev@claude-code-plugins)

- `code-explorer` - Exploration codebase (Phase 1)
- `code-architect` - Design architecture (Phase 3)
- `code-reviewer` - Review qualité (Phase 6)

### Message d'incitation à l'installation

Si le plugin `feature-dev` n'est pas installé, afficher :

```
⚠️ Plugin feature-dev requis pour les agents spécialisés.
Installation : /plugin install feature-dev@claude-code-plugins
```

### Agents conservés (dans dev)

- `phpstan-error-resolver` - Spécifique PHP/PHPStan
- `elegant-objects-reviewer` - Spécifique Elegant Objects

---

## Fichiers à créer/modifier

### Fichiers à créer

```
commands/
├── feature.md          # Orchestrateur /dev:feature
├── status.md           # /dev:status (affiche plan)
├── discover.md         # Phase 0: Comprendre
├── explore.md          # Phase 1: Explorer
├── clarify.md          # Phase 2: Questions
├── design.md           # Phase 3: Architecture
├── plan.md             # Phase 4: Générer plan (remplace prepare.md)
├── review.md           # Phase 6: QA
└── summary.md          # Phase 7: Résumé
```

### Fichiers à modifier

```
commands/
├── code.md             # Adapter pour nouveau workflow
├── debug/error.md      # Renommer en debug.md (simplification)
└── log.md              # Conserver tel quel
```

### Fichiers à supprimer

```
commands/
├── prepare.md          # Remplacé par plan.md
├── question.md         # Peu utilisé
├── docker.md           # Peu utilisé
└── context/load.md     # Peu utilisé
```

### Agents à supprimer (duplication)

```
agents/
├── meta-agent.md                       # Rarement utilisé
├── symfony-docs-scraper.md             # Dans plugin symfony
├── claude-docs-scraper.md              # Dans plugin claude
├── api-platform-docs-scraper.md        # Dans plugin doc
├── meilisearch-docs-scraper.md         # Dans plugin doc
└── atournayre-framework-docs-scraper.md # Dans plugin doc
```

---

## Détail des commandes

### `/dev:feature [description]`

**Orchestrateur principal** - Enchaîne automatiquement les 8 phases.

```yaml
---
description: Workflow complet de développement de feature
argument-hint: <description-feature>
model: sonnet
allowed-tools: Read, Write, Edit, Grep, Glob, Task, TodoWrite, AskUserQuestion
---
```

**Workflow :**
1. Crée todo list avec 8 phases
2. Exécute chaque phase séquentiellement
3. Attend approbation user aux checkpoints (phases 2, 3, 5)
4. Met à jour `/dev:status` à chaque phase

### `/dev:status`

**Affiche le plan et l'état actuel**

```yaml
---
description: Affiche le workflow et l'étape courante
model: haiku
allowed-tools: Read, Glob
---
```

**Output :**
```
🔄 Workflow de développement

  ✅ 0. Discover   - Comprendre le besoin
  ✅ 1. Explore    - Explorer codebase
  🔵 2. Clarify    - Questions clarification  ← En cours
  ⬜ 3. Design     - Proposer architectures
  ⬜ 4. Plan       - Générer specs
  ⬜ 5. Code       - Implémenter
  ⬜ 6. Review     - QA complète
  ⬜ 7. Summary    - Résumé final

📋 Feature: "Ajouter authentification OAuth"
📁 Plan: docs/specs/feature-oauth.md
```

### `/dev:discover [description]`

**Phase 0 : Comprendre le besoin**

```yaml
---
description: Comprendre le besoin avant développement
argument-hint: <description-feature>
model: sonnet
allowed-tools: Read, AskUserQuestion
---
```

**Actions :**
- Clarifier la demande si ambiguë
- Identifier problème résolu
- Lister contraintes
- Résumer et confirmer compréhension

### `/dev:explore`

**Phase 1 : Explorer le codebase**

```yaml
---
description: Explorer le codebase avec agents parallèles
model: sonnet
allowed-tools: Task, Read, Glob, Grep
---
```

**Actions :**
- Lancer 2-3 agents `code-explorer` en parallèle
- Focus différents : features similaires, architecture, patterns
- Consolider findings
- Identifier 5-10 fichiers clés

**Dépendance :** `feature-dev@claude-code-plugins` (agent `code-explorer`)

### `/dev:clarify`

**Phase 2 : Questions de clarification**

```yaml
---
description: Poser questions pour lever ambiguités
model: sonnet
allowed-tools: AskUserQuestion, Read
---
```

**Questions types :**
- Edge cases
- Gestion erreurs
- Points d'intégration
- Rétrocompatibilité
- Performance

**Checkpoint :** Attend réponses avant phase suivante.

### `/dev:design`

**Phase 3 : Proposer architectures**

```yaml
---
description: Designer 2-3 approches architecturales
model: sonnet
allowed-tools: Task, Read, Glob, Grep, AskUserQuestion
---
```

**Actions :**
- Lancer 2-3 agents `code-architect` avec focus :
  - Minimal changes
  - Clean architecture
  - Pragmatic balance
- Présenter comparaison + trade-offs
- Recommander une approche
- Demander choix user

**Dépendance :** `feature-dev@claude-code-plugins` (agent `code-architect`)

**Checkpoint :** Attend choix avant phase suivante.

### `/dev:plan [approach]`

**Phase 4 : Générer le plan**

```yaml
---
description: Générer plan d'implémentation dans docs/specs/
argument-hint: [approche-choisie]
model: sonnet
allowed-tools: Write, Read, Glob
---
```

**Actions :**
- Rédiger plan détaillé basé sur architecture choisie
- Sauvegarder dans `docs/specs/feature-{nom}.md`
- Format : objectif, fichiers, étapes, tests

### `/dev:code [plan]`

**Phase 5 : Implémenter**

```yaml
---
description: Implémenter selon le plan
argument-hint: [path-to-plan]
model: sonnet
allowed-tools: Read, Write, Edit, Bash, Grep, Glob, TodoWrite
---
```

**Actions :**
- Lire le plan depuis `docs/specs/`
- Implémenter chaque étape
- Respecter conventions codebase
- Créer tests unitaires
- Mettre à jour todos

**Checkpoint :** Attend approbation explicite avant de commencer.

### `/dev:review`

**Phase 6 : Quality Review**

```yaml
---
description: Review qualité complète (PHPStan + EO + review)
model: sonnet
allowed-tools: Task, Bash, Read, Grep, Glob
---
```

**Actions :**
1. Lancer agent `code-reviewer` (feature-dev)
2. Lancer `phpstan-error-resolver` (dev)
3. Lancer `elegant-objects-reviewer` (dev)
4. Consolider findings
5. Proposer : fix now / fix later / proceed

**Dépendances :**
- `feature-dev@claude-code-plugins` (agent `code-reviewer`)
- Agents locaux `phpstan-error-resolver`, `elegant-objects-reviewer`

### `/dev:summary`

**Phase 7 : Résumé final**

```yaml
---
description: Résumé de ce qui a été construit
model: haiku
allowed-tools: Read, Glob
---
```

**Output :**
- Ce qui a été construit
- Décisions clés
- Fichiers modifiés
- Prochaines étapes suggérées

### `/dev:debug [error]`

**Utilitaire : Debug erreurs** (conservé, renommé)

```yaml
---
description: Analyser et résoudre une erreur
argument-hint: <message-erreur-ou-fichier-log>
model: sonnet
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, TodoWrite, Task
---
```

Contenu identique à l'actuel `/dev:debug:error`.

---

## Structure finale du plugin

```
dev/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── feature.md      # Orchestrateur
│   ├── status.md       # Affiche plan
│   ├── discover.md     # Phase 0
│   ├── explore.md      # Phase 1
│   ├── clarify.md      # Phase 2
│   ├── design.md       # Phase 3
│   ├── plan.md         # Phase 4
│   ├── code.md         # Phase 5
│   ├── review.md       # Phase 6
│   ├── summary.md      # Phase 7
│   ├── debug.md        # Utilitaire (ex debug/error.md)
│   └── log.md          # Utilitaire (conservé)
├── agents/
│   ├── phpstan-error-resolver.md      # Conservé
│   └── elegant-objects-reviewer.md    # Conservé
├── README.md
└── CHANGELOG.md
```

---

## Ordre d'implémentation

1. **Créer `/dev:status`** - Base du système de tracking
2. **Créer `/dev:discover`** - Phase 0
3. **Créer `/dev:explore`** - Phase 1 (avec dépendance feature-dev)
4. **Créer `/dev:clarify`** - Phase 2
5. **Créer `/dev:design`** - Phase 3 (avec dépendance feature-dev)
6. **Modifier `/dev:plan`** - Phase 4 (ex prepare.md)
7. **Adapter `/dev:code`** - Phase 5
8. **Créer `/dev:review`** - Phase 6 (avec dépendance feature-dev)
9. **Créer `/dev:summary`** - Phase 7
10. **Créer `/dev:feature`** - Orchestrateur
11. **Renommer `/dev:debug:error`** → `/dev:debug`
12. **Supprimer commandes obsolètes**
13. **Supprimer agents dupliqués**
14. **Mettre à jour README.md**
15. **Mettre à jour CHANGELOG.md**
16. **Bump version** → 2.0.0

---

## Questions résolues

- ✅ Nommage : verbes (`discover`, `explore`, etc.)
- ✅ Orchestrateur : `/dev:feature`
- ✅ Status : `/dev:status`
- ✅ Debug conservé : `/dev:debug`
- ✅ Agents : réutilisation feature-dev + incitation installation
