# Plan : Slash Command /dev:log [FICHIER]

## Objectif
Créer une commande qui ajoute des fonctionnalités de logging à un fichier PHP en utilisant `LoggableInterface` d'Atournayre.

## Fichier à créer
`dev/commands/log.md`

## Structure de la commande

### Front Matter
```yaml
---
description: Ajoute des fonctionnalités de log au fichier en cours
argument-hint: [FICHIER]
allowed-tools: Read, Edit, Grep, Glob
---
```

### Workflow
1. **Lire le fichier** cible passé en argument
2. **Analyser** les classes et propriétés du fichier
3. **Vérifier** si `LoggableInterface` est déjà implémentée
4. **Chercher** les dépendances (objets utilisés) qui implémentent `LoggableInterface`
5. **Ajouter** :
   - Import `use Atournayre\Contracts\Log\LoggableInterface;`
   - `implements LoggableInterface` sur la classe
   - Méthode `toLog(): array` avec les propriétés pertinentes
6. **Pour les objets imbriqués** : appeler `->toLog()` si ils implémentent `LoggableInterface`

### Règles métier
- Propriétés à logger : `id`, identifiants métier, états clés
- Exclure : mots de passe, tokens, données sensibles
- Collections : `count` + `items` mappés sur `toLog()`
- Objets imbriqués : vérifier `LoggableInterface` avant d'appeler `toLog()`

## Template toLog()

```php
/**
 * @return array<string, mixed>
 */
public function toLog(): array
{
    return [
        'id' => $this->id,
        // Propriétés clés
        // Objets: 'relation' => $this->relation->toLog(),
    ];
}
```

### PHPStan Compliance
- Toujours ajouter `@return array<string, mixed>` sur `toLog()`
- Pour les collections avec items : `@return array{count: int, items: array<int, array<string, mixed>>}`

## Fichiers impactés
- Création : `dev/commands/log.md`
