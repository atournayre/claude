# Indexes

**Source:** https://www.meilisearch.com/docs/reference/api/indexes.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Indexes

---

# Indexes

> The /indexes route allows you to create, manage, and delete your indexes.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/indexes` route allows you to create, manage, and delete your indexes.

[Learn more about indexes](/learn/getting_started/indexes).

## Index object

```json
{
  "uid": "movies",
  "createdAt": "2022-02-10T07:45:15.628261Z",
  "updatedAt": "2022-02-21T15:28:43.496574Z",
  "primaryKey": "id"
}
```

| Name             | Type            | Default value | Description                                                                                                                                                                                                                                                  |
| :--------------- | :-------------- | :------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`uid`**        | String          | N/A           | [Unique identifier](/learn/getting_started/indexes#index-uid) of the index. Once created, it cannot be changed                                                                                                                                               |
| **`createdAt`**  | String          | N/A           | Creation date of the index, represented in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. Auto-generated on index creation                                                                                                                         |
| **`updatedAt`**  | String          | N/A           | Latest date of index update, represented in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. Auto-generated on index creation or update                                                                                                              |
| **`primaryKey`** | String / `null` | `null`        | [Primary key](/learn/getting_started/primary_key#primary-field) of the index. If not specified, Meilisearch will [infer the primary key](/learn/getting_started/primary_key#meilisearch-guesses-your-primary-key) from the first document you add to the index |
