# Primary key

**Source:** https://www.meilisearch.com/docs/learn/getting_started/primary_key.md
**Extrait le:** 2025-10-08
**Sujet:** Getting Started - Primary Key
**Note:** Contenu extrait depuis le repository GitHub officiel (fichier MDX source)

---

## Primary field

An [index](/learn/getting_started/indexes) in Meilisearch is a collection of [documents](/learn/getting_started/documents). Documents are composed of fields, each field containing an attribute and a value.

The primary field is a special field that must be present in all documents. Its attribute is the **primary key** and its value is the **document id**. It uniquely identifies each document in an index, ensuring that **it is impossible to have two exactly identical documents** present in the same index.

### Example

Suppose we have an index of books. Each document contains a number of fields with data on the book's `author`, `title`, and `price`. More importantly, each document contains a **primary field** consisting of the index's **primary key** `id` and a **unique id**.

```json
[
  {
    "id": 1,
    "title": "Diary of a Wimpy Kid: Rodrick Rules",
    "author": "Jeff Kinney",
    "genres": ["comedy","humor"],
    "price": 5.00
  },
  {
    "id": 2,
    "title": "Black Leopard, Red Wolf",
    "author": "Marlon James",
    "genres": ["fantasy","drama"],
    "price": 5.00
  }
]
```

Aside from the primary key, **documents in the same index are not required to share attributes**. A book in this dataset could be missing the `title` or `genre` attribute and still be successfully indexed by Meilisearch, provided it has the `id` attribute.

## Primary key

The primary key is the attribute of the primary field.

Every index has a primary key, an attribute that must be shared across all documents in that index. If you attempt to add documents to an index and even a single one is missing the primary key, **none of the documents will be stored.**

### Document ID requirements

The document ID must be of type integer or string. If it is a string, it can only contain alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (_).

### Setting the primary key

You can set the primary key:

1. **Explicitly during index creation**
2. **When adding documents to an empty index** - Meilisearch will automatically infer the primary key
3. **Automatically by Meilisearch** - looking for attributes ending with "id" (case-insensitive)

### Key constraints

- An index can have **only one primary key**
- The primary key **cannot be changed** while documents are present in the index
- To change the primary key, you must delete all documents first

### Common errors

#### `index_primary_key_multiple_candidates_found`
Multiple attributes ending with "id" were detected. You must explicitly specify which one to use as the primary key.

#### `index_primary_key_no_candidate_found`
No attribute ending with "id" was found in the documents. You must explicitly set the primary key.

#### `invalid_document_id`
The document ID format is incorrect. It must be an integer or a string containing only alphanumeric characters, hyphens, and underscores.

#### `missing_document_id`
One or more documents are missing the required primary key attribute.

---

**Résumé des points clés:**

- La clé primaire est un champ spécial obligatoire dans tous les documents
- Elle identifie de manière unique chaque document dans un index
- Peut être définie explicitement ou automatiquement déduite par Meilisearch
- Les ID de documents doivent être des entiers ou des chaînes alphanumériques (avec - et _ autorisés)
- Un index ne peut avoir qu'une seule clé primaire
- La clé primaire ne peut pas être modifiée tant que des documents sont présents
