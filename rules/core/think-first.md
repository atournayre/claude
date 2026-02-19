---
description: REFLECHIR avant d'ecrire du code pour les taches non-triviales
---

# Think First

## Regle

Pour toute tache non-triviale : **reflechir, reflechir encore, reflechir une derniere fois, puis ecrire.**

## Taches Non-Triviales

Une tache est non-triviale si elle implique au moins un de ces criteres :
- 3+ fichiers a modifier
- Decision architecturale ou nouveau pattern
- Bug dont la cause racine n'est pas evidente
- Impact potentiel sur d'autres composants

## Les 3 Questions Obligatoires

Avant d'ecrire la moindre ligne de code, repondre explicitement :

1. **Qu'est-ce qui est demande exactement ?** (perimetre precis, pas d'interpretation)
2. **Quelles sont les implications et effets de bord ?** (qu'est-ce qui pourrait casser ?)
3. **Quelle est la solution la plus simple ?** (pas la plus elegante, la plus simple)

## Regle d'Arret

Si je ne peux pas repondre clairement aux 3 questions → **STOP**, demander clarification.

## Interdit

- Commencer a coder sans avoir repondu aux 3 questions
- Supposer ce qui est demande
- Ignorer les effets de bord potentiels
- Choisir une solution complexe avant d'avoir explore la simple
