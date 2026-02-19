---
description: Definition of Done pour projets PHP avec Makefile
---

# Definition of Done

## Regle

Une tache n'est **jamais** declaree terminee sans preuve concrete.

## Conditions (projets PHP avec Makefile)

- `make run-all-tests-php` passe sans erreur
- Aucun test en echec, aucun warning non resolu

## Workflow Bug Fix

1. Ecrire un test qui reproduit le bug → doit etre **rouge**
2. Corriger le bug
3. Le test passe → **vert**
4. `make run-all-tests-php` passe en entier

## Regle d'Arret

- Apres 2 tentatives echouees sur la meme approche → **STOP**
- Changer d'approche ou demander clarification
- Ne jamais continuer a forcer la meme solution qui echoue

## Interdit

- Dire "c'est fait" sans avoir execute les tests
- Skipper les tests "parce que ca semble logique"
- Ignorer un test en echec non lie a la tache
- Marquer done si `make run-all-tests-php` n'existe pas dans le projet
