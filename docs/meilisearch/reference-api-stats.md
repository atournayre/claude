# Stats

**Source:** https://www.meilisearch.com/docs/reference/api/stats.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Stats

---

# Stats

> The /stats route you gives extended information and metrics about indexes and the Meilisearch database.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/stats` route gives extended information and metrics about indexes and the Meilisearch database.

## Stats object

```json
{
  "databaseSize": 447819776,
  "usedDatabaseSize": 196608,
  "lastUpdate": "2019-11-15T11:15:22.092896Z",
  "indexes": {
    "movies": {
      "numberOfDocuments": 19654,
      "numberOfEmbeddedDocuments": 1,
      "numberOfEmbeddings": 1,
      "rawDocumentDbSize": 5320,
      "avgDocumentSize": 92,
      "isIndexing": false,
      "fieldDistribution": {
        "poster": 19654,
        "overview": 19654,
        "title": 19654,
        "id": 19654,
        "release_date": 19654
      }
    },
    "books": {
      "numberOfDocuments": 5,
      "numberOfEmbeddedDocuments": 5,
      "numberOfEmbeddings": 10,
      "rawDocumentDbSize": 8780,
      "avgDocumentSize": 422,
      "isIndexing": false,
      "fieldDistribution": {
        "id": 5,
        "title": 5,
        "author": 5,
        "price": 5,
        "genres": 5
      }
    }
  }
}
```

| Name                            | Type    | Description                                                                                                  |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------ |
| `databaseSize`                  | Integer | Total size of the database in bytes                                                                          |
| `usedDatabaseSize`              | Integer | Size of the database actually used by data in bytes (excluding free pages)                                   |
| `lastUpdate`                    | String  | Timestamp of the last database update in RFC 3339 format                                                     |
| `indexes`                       | Object  | Object containing all indexes and their respective stats                                                     |
| `indexes.{indexName}`           | Object  | Stats for a specific index identified by `{indexName}`                                                       |
| `numberOfDocuments`             | Integer | Number of documents in the index                                                                             |
| `numberOfEmbeddedDocuments`     | Integer | Number of documents containing embeddings                                                                    |
| `numberOfEmbeddings`            | Integer | Total number of embeddings across all documents                                                              |
| `rawDocumentDbSize`             | Integer | Size of raw documents in bytes before compression                                                            |
| `avgDocumentSize`               | Integer | Average size of a document in bytes                                                                          |
| `isIndexing`                    | Boolean | `true` if indexing is in progress, `false` otherwise                                                         |
| `fieldDistribution`             | Object  | Number of documents containing each field                                                                    |

## Get stats of all indexes

<RouteHighlighter method="GET" path="/stats" />

Get stats of all indexes.

### Example

<CodeSamples id="stats_get_1" />

#### Response: `200 Ok`

```json
{
  "databaseSize": 447819776,
  "usedDatabaseSize": 196608,
  "lastUpdate": "2019-11-15T11:15:22.092896Z",
  "indexes": {
    "movies": {
      "numberOfDocuments": 19654,
      "numberOfEmbeddedDocuments": 1,
      "numberOfEmbeddings": 1,
      "rawDocumentDbSize": 5320,
      "avgDocumentSize": 92,
      "isIndexing": false,
      "fieldDistribution": {
        "poster": 19654,
        "overview": 19654,
        "title": 19654,
        "id": 19654,
        "release_date": 19654
      }
    },
    "books": {
      "numberOfDocuments": 5,
      "numberOfEmbeddedDocuments": 5,
      "numberOfEmbeddings": 10,
      "rawDocumentDbSize": 8780,
      "avgDocumentSize": 422,
      "isIndexing": false,
      "fieldDistribution": {
        "id": 5,
        "title": 5,
        "author": 5,
        "price": 5,
        "genres": 5
      }
    }
  }
}
```

## Get stats of an index

<RouteHighlighter method="GET" path="/indexes/{index_uid}/stats" />

Get stats of a specific index.

### Path parameters

| Name         | Type   | Description                                                      |
| ------------ | ------ | ---------------------------------------------------------------- |
| `index_uid`  | String | [`uid`](/learn/core_concepts/indexes#index-uid) of the requested index |

### Example

<CodeSamples id="get_index_stats_1" />

#### Response: `200 Ok`

```json
{
  "numberOfDocuments": 19654,
  "numberOfEmbeddedDocuments": 1,
  "numberOfEmbeddings": 1,
  "rawDocumentDbSize": 5320,
  "avgDocumentSize": 92,
  "isIndexing": false,
  "fieldDistribution": {
    "poster": 19654,
    "overview": 19654,
    "title": 19654,
    "id": 19654,
    "release_date": 19654
  }
}
```
