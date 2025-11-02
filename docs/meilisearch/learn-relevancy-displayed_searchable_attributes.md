# Displayed and searchable attributes

**Source:** https://www.meilisearch.com/docs/learn/relevancy/displayed_searchable_attributes.md
**Extrait le:** 2025-10-08
**Sujet:** Relevancy - Displayed and Searchable Attributes

---

# Displayed and searchable attributes

> Displayed and searchable attributes define what data Meilisearch returns after a successful query and which fields Meilisearch takes in account when searching. Knowing how to configure them can help improve your application's performance.

By default, whenever a document is added to Meilisearch, all new attributes found in it are automatically added to two lists:

* [`displayedAttributes`](/learn/relevancy/displayed_searchable_attributes#displayed-fields): Attributes whose fields are displayed in documents
* [`searchableAttributes`](/learn/relevancy/displayed_searchable_attributes#the-searchableattributes-list): Attributes whose values are searched for matching query words

By default, every field in a document is **displayed** and **searchable**. These properties can be modified in the [settings](/reference/api/settings).

## Displayed fields

The fields whose attributes are added to the [`displayedAttributes` list](/reference/api/settings#displayed-attributes) are **displayed in each matching document**.

Documents returned upon search contain only displayed fields. If a field attribute is not in the displayed-attribute list, the field won't be added to the returned documents.

**By default, all field attributes are set as displayed**.

### Example

Suppose you manage a database that contains information about movies. By adding the following settings, documents returned upon search will contain the fields `title`, `overview`, `release_date` and `genres`.

<CodeGroup>
  ```bash cURL
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/movies/settings/displayed-attributes' \
    -H 'Content-Type: application/json' \
    --data-binary '[
        "title",
        "overview",
        "genres",
        "release_date"
      ]'
  ```

  ```javascript JS
  client.index('movies').updateDisplayedAttributes([
      'title',
      'overview',
      'genres',
      'release_date',
    ]
  )
  ```

  ```python Python
  client.index('movies').update_displayed_attributes([
      'title',
      'overview',
      'genres',
      'release_date'
    ])
  ```
</CodeGroup>
