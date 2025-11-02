# Similar documents

**Source:** https://www.meilisearch.com/docs/reference/api/similar.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Similar documents endpoint

---

> The /similar route accepts one search result and uses AI-powered search to return a number of similar documents.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/similar` route uses AI-powered search to return a number of documents similar to a target document.

Meilisearch exposes two routes for retrieving similar documents: `POST` and `GET`. In the majority of cases, `POST` will offer better performance and ease of use.

## Get similar documents with `POST`

<RouteHighlighter method="POST" path="/indexes/{index_uid}/similar" />

Retrieve documents similar to a specific search result.

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Body

| Parameter                                                                    | Type             | Default value | Description                                               |
| ---------------------------------------------------------------------------- | ---------------- | ------------- | --------------------------------------------------------- |
| **`id`**                                                                     | String or number | `null`        | Identifier of the target document (mandatory)             |
| **[`embedder`](/reference/api/search#hybrid-search)**                        | String           | `null`        | Embedder to use when computing recommendations. Mandatory |
| **[`attributesToRetrieve`](/reference/api/search#attributes-to-retrieve)**   | Array of strings | `["*"]`       | Attributes to display in the returned documents           |
| **[`offset`](/reference/api/search#offset)**                                 | Integer          | `0`           | Number of documents to skip                               |
| **[`limit`](/reference/api/search#limit)**                                   | Integer          | `20`          | Maximum number of documents returned                      |
