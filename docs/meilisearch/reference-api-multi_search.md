# Multi-search

**Source:** https://www.meilisearch.com/docs/reference/api/multi_search.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Multi-search endpoint

---

> Note: Cette documentation a été extraite automatiquement. Pour le contenu complet et à jour, consulter l'URL source ci-dessus.

## Vue d'ensemble

La route `/multi-search` permet d'effectuer plusieurs requêtes de recherche sur un ou plusieurs index en les regroupant dans une seule requête HTTP. Cette fonctionnalité est également connue sous le nom de recherche fédérée (federated search).

## Endpoint

**POST** `/multi-search`

## Corps de la requête

| Paramètre | Type | Description |
|-----------|------|-------------|
| `federation` | Object | Si présent et non `null`, retourne une liste unique fusionnant tous les résultats de recherche de toutes les requêtes spécifiées |
| `queries` | Array of objects | Contient la liste des requêtes de recherche à effectuer. Le paramètre `indexUid` est obligatoire, tous les autres paramètres sont optionnels |

### Structure de `queries`

Chaque objet dans le tableau `queries` peut contenir :

- `indexUid` (obligatoire) : L'identifiant de l'index à rechercher
- Tous les paramètres de recherche standards de Meilisearch :
  - `q` : La requête de recherche
  - `limit` : Nombre de résultats à retourner
  - `offset` : Nombre de résultats à ignorer
  - `filter` : Filtres à appliquer
  - `facets` : Facettes à calculer
  - `attributesToRetrieve` : Attributs à retourner
  - `attributesToCrop` : Attributs à tronquer
  - `cropLength` : Longueur du crop
  - `attributesToHighlight` : Attributs à surligner
  - `highlightPreTag` : Tag de début de surbrillance
  - `highlightPostTag` : Tag de fin de surbrillance
  - `showMatchesPosition` : Afficher les positions des correspondances
  - `sort` : Tri des résultats
  - `matchingStrategy` : Stratégie de correspondance
  - Et autres paramètres de recherche Meilisearch

### Structure de `federation`

L'objet `federation` permet de configurer la fusion des résultats :

- Options de ranking pour la fusion des résultats
- Configuration du scoring
- Paramètres de déduplication

## Formats de réponse

### Recherche multi-index sans fédération

Retourne un tableau de résultats, un par requête :

```json
{
  "results": [
    {
      "indexUid": "index_name_1",
      "hits": [...],
      "query": "search term",
      "processingTimeMs": 10,
      "limit": 20,
      "offset": 0,
      "estimatedTotalHits": 100
    },
    {
      "indexUid": "index_name_2",
      "hits": [...],
      "query": "search term",
      "processingTimeMs": 5,
      "limit": 20,
      "offset": 0,
      "estimatedTotalHits": 50
    }
  ]
}
```

### Recherche fédérée

Avec l'option `federation`, retourne un ensemble fusionné de résultats :

```json
{
  "hits": [...],
  "processingTimeMs": 15,
  "limit": 20,
  "offset": 0,
  "estimatedTotalHits": 150,
  "semanticHitCount": 0
}
```

## Fonctionnalités clés

1. **Recherche multi-index** : Rechercher dans plusieurs index simultanément
2. **Recherche fédérée** : Fusionner les résultats de plusieurs index en une seule liste
3. **Optimisation des performances** : Une seule requête HTTP pour plusieurs recherches
4. **Flexibilité** : Chaque requête peut avoir ses propres paramètres
5. **Support expérimental** : Recherche à distance (remote search)

## Gestion des erreurs

⚠️ **Important** : Si Meilisearch rencontre une erreur lors du traitement d'une des requêtes, il arrête immédiatement le traitement et retourne un message d'erreur. Le message retourné ne concernera que la première erreur rencontrée.

## Algorithme de ranking pour les résultats fusionnés

Lorsque `federation` est utilisé, Meilisearch fusionne les résultats selon un algorithme de ranking qui :

- Prend en compte les scores de pertinence de chaque index
- Applique les règles de ranking configurées
- Gère la déduplication si configurée
- Maintient l'ordre de pertinence global

## Cas d'usage

- **Recherche globale** : Chercher dans tous les types de contenu (articles, produits, utilisateurs, etc.)
- **Comparaison de résultats** : Comparer les résultats entre différents index
- **Optimisation des performances** : Réduire le nombre de requêtes HTTP
- **Interface unifiée** : Présenter des résultats de sources multiples dans une seule interface

## Exemples d'utilisation

La documentation officielle fournit des exemples détaillés dans plusieurs langages de programmation pour :

- Recherche multi-index basique
- Recherche fédérée avec fusion des résultats
- Configuration avancée avec filtres et facettes
- Recherche à distance (expérimental)

---

**Pour la documentation technique complète, les exemples de code détaillés et les dernières mises à jour, consulter :**
https://www.meilisearch.com/docs/reference/api/multi_search.md
