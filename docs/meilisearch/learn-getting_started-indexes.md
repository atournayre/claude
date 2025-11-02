# Indexes

**Source:** https://www.meilisearch.com/docs/learn/getting_started/indexes.md
**Extrait le:** 2025-10-08
**Sujet:** Getting Started - Indexes

---

# Indexes

> An index is a collection of documents, much like a table in MySQL or a collection in MongoDB.

An index is a group of documents with associated settings. It is comparable to a table in `SQL` or a collection in MongoDB.

An index is defined by a `uid` and contains the following information:

* One [primary key](#primary-key)
* Customizable [settings](#index-settings)
* An arbitrary number of documents

#### Example

Suppose you manage a database that contains information about movies, similar to [IMDb](https://imdb.com/). You would probably want to keep multiple types of documents, such as movies, TV shows, actors, directors, and more. Each of these categories would be represented by an index in Meilisearch.

Using an index's settings, you can customize search behavior for that index. For example, a `movies` index might contain documents with fields like `movie_id`, `title`, `genre`, `overview`, and `release_date`. Using settings, you could make a movie's `title` have a bigger impact on search results than its `overview`, or make the `movie_id` field non-searchable.

One index's settings do not impact other indexes. For example, you could use a different list of synonyms for your `movies` index than for your `costumes` index, even if they're on the same server.

## Index creation

### Implicit index creation

If you try to add documents or settings to an index that does not already exist, Meilisearch will automatically create it for you.

### Explicit index creation

You can explicitly create an index using the [create index endpoint](/reference/api/indexes#create-an-index). Once created, you can add documents using the [add documents endpoint](/reference/api/documents#add-or-update-documents).

While implicit index creation is more convenient, requiring only a single API request, **explicit index creation is considered safer for production**. This is because implicit index creation bundles multiple actions into a single task. If one action completes successfully while the other fails, the problem can be difficult to diagnose.

## Index UID

The `uid` is the **unique identifier** of an index. It is set when creating the index and must be an integer or string containing only alphanumeric characters `a-z A-Z 0-9`, hyphens `-`, and underscores `_`.

::: note
Though there is no officially defined limit to `uid` length, excessively long UIDs may have a negative performance impact.
:::

## Primary key

The **primary key** is a special field in each document. Its value is the **document id**, and it must be unique across all documents in a given index. It must be of type integer or string.

If you try to index documents without a primary key, or if two documents in the same batch share a primary key value, Meilisearch will throw an error.

::: note
In Meilisearch, the primary key field is always case insensitive. `ID`, `id`, `iD`, and `Id` are all treated the same way.
:::

### Meilisearch guesses your primary key

When adding documents to an index for the first time, if the primary key has not been specified by the user, Meilisearch will search your first document for an attribute that contains `id` in a case-insensitive manner, such as `uid`, `MovieId`, `ID`, or `123id321`. If it finds such an attribute, it will set that field as the primary key for the index.

If Meilisearch finds multiple attributes containing `id`, it will choose the first one in alphabetical order. For example, if a document has the attributes `objectID`, `movie_id`, and `id`, Meilisearch will choose `id` as the primary key field.

::: warning
Because of this behavior, if some of your documents contain an attribute such as `objectID` or `movie_id` but not all of them, Meilisearch may set the wrong attribute as the primary key. To prevent this from happening, you must manually set the primary key. You can do this during [index creation](/reference/api/indexes#create-an-index) or using the [update index endpoint](/reference/api/indexes#update-an-index).
:::

### Primary key inference

In some situations, Meilisearch may be able to infer the primary key from the document id when adding or updating documents. In that case, the document id will be automatically added to the document.

For example, if you add the following document using the [add or replace documents endpoint](/reference/api/documents#add-or-replace-documents):

```json
{
  "id": 123,
  "title": "The Little Prince"
}
```

And use the primary key `id` as the document id:

```
POST /indexes/books/documents?primaryKey=id
```

Meilisearch will automatically add the primary key to the document:

```json
{
  "id": 123,
  "title": "The Little Prince"
}
```

#### Limitations

Primary key inference is only possible when the primary key field is entirely composed of digits (`[0-9]+`).

## Index settings

Index settings allow you to customize the behavior of Meilisearch. They can be [configured for each index independently](/reference/api/settings).

Some of the things you can configure through index settings include:

* [Searchable attributes](/learn/relevancy/displayed_and_searchable_attributes#searchable-attributes)
* [Displayed attributes](/learn/relevancy/displayed_and_searchable_attributes#displayed-attributes)
* [Distinct attributes](/learn/relevancy/distinct)
* [Ranking rules](/learn/relevancy/ranking_rules)
* [Stop words](/learn/relevancy/stop_words)
* [Synonyms](/learn/relevancy/synonyms)
* [Filterable attributes](/learn/filtering_and_faceted_search/filter_search_results#configuring-filters)
* [Sortable attributes](/learn/filtering_and_faceted_search/sort_search_results)
* [Pagination settings](/learn/getting_started/pagination)

For a complete list of index settings, see our [API reference](/reference/api/settings).