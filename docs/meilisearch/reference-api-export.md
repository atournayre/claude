# Export

**Source:** https://www.meilisearch.com/docs/reference/api/export.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Export

---

# Export

> Migrate between instances with the `/export` route

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

Use the `/export` route to transfer data from your origin instance to a remote target instance. This is particularly useful when migrating from your local development environment to a Meilisearch Cloud instance.

## Migrate database between instances

<RouteHighlighter method="POST" path="/export" />

Migrate data from the origin instance to a target instance.

Migration is an additive operation. If the exported indexes already exist in the target instance, Meilisearch keeps the existing documents intact and adds the new data to the index. If the same document is present in both the target and origin, Meilisearch replaces the target documents with the new data.

### Body

| Name                 | Type   | Default value | Description                                                                                               |
| -------------------- | ------ | ------------- | --------------------------------------------------------------------------------------------------------- |
| **`url`** \*         | String | `null`        | The target instance's URL address. Required                                                               |
| **`apiKey`** \*      | String | `null`        | An API key with full admin access to the target instance                                                  |
| **`payloadSize`** \* | String | "50 MiB"      | A string specifying the payload size in a human-readable format                                           |
| **`indexes`** \*     | Object | `null`        | A set of patterns matching the indexes you want to export. Defaults to all indexes in the origin instance |

#### `url`

A string pointing to a remote Meilisearch instance, including its port if necessary.

This field is required.

#### `apiKey`

A security key with `index.create`, `settings.update`, and `documents.add` permissions to a secured Meilisearch instance.

#### `payloadSize`

The maximum size
