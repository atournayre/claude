---
description: Principes Elegant Objects (Yegor Bugayenko) pour projets PHP
---

# Elegant Objects

## Regle

Avant d'implementer : **"Yegor approuverait-il ?"**

Si la solution semble hacky ou procedurale → chercher l'approche EO correcte.

## Principes Cles

- **Pas de getters/setters** — exposer le comportement, pas les donnees
- **Objets immutables** — pas de mutation d'etat interne
- **Pas de classes statiques ni de methodes statiques** (sauf constructeurs nommes)
- **Constructeurs legers** — pas de logique dans le constructeur
- **Interfaces** pour chaque concept metier significatif
- **Exceptions metier** plutot que codes d'erreur ou null
- **Pas de null** — utiliser NullObject pattern ou exceptions

## Constructeurs Nommes

```php
// Bien
final class Email
{
    private function __construct(private string $value) {}

    public static function of(string $value): self
    {
        return new self($value);
    }
}

// Interdit
$email = new Email($value); // constructeur public avec logique
```

## Exception a la Regle

Ne pas appliquer EO pour :
- Fixes triviaux (typo, config, renommage)
- Code legacy qu'on ne refactorise pas dans cette tache
- Scripts utilitaires one-shot
