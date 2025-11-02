# Search with facets

**Source:** https://www.meilisearch.com/docs/learn/filtering_and_sorting/search_with_facet_filters.md
**Extrait le:** 2025-10-08
**Sujet:** Filtering and Sorting - Faceted Search

---

# Search with facets

> Faceted search interfaces provide users with a quick way to narrow down search results by selecting categories relevant to their query.

In Meilisearch, facets are a specialized type of filter. This guide shows you how to configure facets and use them when searching a database of books. It also gives you instruction on how to get

## Requirements

* a Meilisearch project
* a command-line terminal

## Configure facet index settings

First, create a new index using this <a id="downloadBooks" href="/assets/datasets/books.json" download="books.json">books dataset</a>. Documents in this dataset have the following fields:

```json
{
  "id": 5,
  "title": "Hard Times",
  "genres": ["Classics","Fiction", "Victorian", "Literature"],
  "publisher": "Penguin Classics",
  "language": "English",
  "author": "Charles Dickens",
  "description": "Hard Times is a novel of social […] ",
  "format": "Hardcover",
  "rating": 3
}
```

Next, add `genres`, `language`, and `rating` to the list of `filterableAttributes`:

<CodeGroup>
  ```bash cURL
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/books/settings/filterable-attributes' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      "genres", "rating", "language"
    ]'
  ```

  ```javascript JS
  client.index('movie_ratings').updateFilterableAttributes(['genres', 'rating', 'language'])
  ```

  ```python Python
  client.index('movie_ratings').update_filterable_attributes([
    'genres',
    'director',
    'language'
  ])
  ```

  ```php PHP
  $client->index('movie_ratings')->updateFilterableAttributes(['genres', 'rating', 'language']);
  ```

  ```java Java
  client.index("movie_ratings").updateFilterableAttributesSettings(new String[] { "genres", "director", "language" });
  ```
