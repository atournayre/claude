# Keys

**Source:** https://www.meilisearch.com/docs/reference/api/keys.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Keys Management

---

# Keys

> The /keys route allows you to create, manage, and delete API keys.

The `/keys` route allows you to create, manage, and delete API keys. To use these endpoints, you must first [set the master key](/learn/security/basic_security). Once a master key is set, you can access these endpoints by supplying it in the header of the request, or using API keys that have access to the `keys.get`, `keys.create`, `keys.update`, or `keys.delete` actions.

<Warning>
  Accessing the `/keys` route without setting a master key will throw a [`missing_master_key`](/reference/errors/error_codes#missing_master_key) error.
</Warning>

## Get all keys

<RouteHighlighter method="GET" path="/keys" />

Get a list of all keys.

### Query parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `offset` | Integer | False | Number of keys to skip. Defaults to `0` |
| `limit` | Integer | False | Number of keys to return. Defaults to `20` |

### Response

| Field | Type | Description |
|-------|------|-------------|
| `results` | Array | Array of [key objects](#key-object) |
| `offset` | Integer | Number of keys skipped |
| `limit` | Integer | Number of keys returned |
| `total` | Integer | Total number of keys |

#### Key object

| Field | Type | Description |
|-------|------|-------------|
| `key` | String | The key itself. Only returned when creating a key |
| `description` | String | Key description |
| `name` | String | Key name. `null` if not specified |
| `uid` | String | Unique identifier for this key |
| `actions` | Array of strings | List of actions permitted for this key. Use `["*"]` to allow all actions |
| `indexes` | Array of strings | List of indexes this key is permitted to act on. Use `["*"]` to allow all indexes |
| `expiresAt` | String | Date and time when the key expires, in ISO-8601 format. `null` if the key has no expiration date |
| `createdAt` | String | Date and time when the key was created, in ISO-8601 format |
| `updatedAt` | String | Date and time when the key was last updated, in ISO-8601 format |

### Example

```bash
curl \
  -X GET 'http://localhost:7700/keys' \
  -H 'Authorization: Bearer MASTER_KEY'
```

#### Response: `200 Ok`

```json
{
  "results": [
    {
      "description": "Use it for anything that is not a search operation. Caution! Do not expose it on a public frontend",
      "name": "Default Admin API Key",
      "uid": "74c9c733-3368-4738-bbe5-1d18a5fecb37",
      "actions": ["*"],
      "indexes": ["*"],
      "expiresAt": null,
      "createdAt": "2021-08-11T10:00:00Z",
      "updatedAt": "2021-08-11T10:00:00Z"
    },
    {
      "description": "Use it to search from the frontend",
      "name": "Default Search API Key",
      "uid": "0a6e572e-918b-4a17-855e-1e42c8c6faa4",
      "actions": ["search"],
      "indexes": ["*"],
      "expiresAt": null,
      "createdAt": "2021-08-11T10:00:00Z",
      "updatedAt": "2021-08-11T10:00:00Z"
    }
  ],
  "offset": 0,
  "limit": 20,
  "total": 2
}
```

## Get one key

<RouteHighlighter method="GET" path="/keys/:uid_or_key" />

Get information about a specific key based on its `uid` or its `key` value.

### Path parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `uid_or_key` | String | True | `uid` or `key` value of the requested key |

### Response

Returns a [key object](#key-object).

### Example

```bash
curl \
  -X GET 'http://localhost:7700/keys/74c9c733-3368-4738-bbe5-1d18a5fecb37' \
  -H 'Authorization: Bearer MASTER_KEY'
```

#### Response: `200 Ok`

```json
{
  "description": "Use it for anything that is not a search operation. Caution! Do not expose it on a public frontend",
  "name": "Default Admin API Key",
  "uid": "74c9c733-3368-4738-bbe5-1d18a5fecb37",
  "actions": ["*"],
  "indexes": ["*"],
  "expiresAt": null,
  "createdAt": "2021-08-11T10:00:00Z",
  "updatedAt": "2021-08-11T10:00:00Z"
}
```

## Create a key

<RouteHighlighter method="POST" path="/keys" />

Create a new API key with specific permissions.

### Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | String | False | Key description |
| `name` | String | False | Key name |
| `uid` | String | False | Unique identifier for this key. Meilisearch generates this automatically if not specified |
| `actions` | Array of strings | True | Actions permitted for this key. Use `["*"]` to allow all actions. [See actions list](#actions) |
| `indexes` | Array of strings | True | Indexes this key is permitted to act on. Use `["*"]` to allow all indexes |
| `expiresAt` | String | False | Date and time when the key expires, in ISO-8601 format. `null` if the key has no expiration date |

#### Actions

Available actions for API keys:

- `*`: Allow all actions
- `search`: Allow search queries
- `documents.add`: Allow adding documents
- `documents.get`: Allow retrieving documents
- `documents.delete`: Allow deleting documents
- `indexes.create`: Allow creating indexes
- `indexes.get`: Allow retrieving index information
- `indexes.update`: Allow updating index settings
- `indexes.delete`: Allow deleting indexes
- `indexes.swap`: Allow swapping indexes
- `tasks.get`: Allow retrieving tasks
- `tasks.cancel`: Allow canceling tasks
- `tasks.delete`: Allow deleting tasks
- `settings.get`: Allow retrieving settings
- `settings.update`: Allow updating settings
- `stats.get`: Allow retrieving stats
- `metrics.get`: Allow retrieving metrics
- `dumps.create`: Allow creating dumps
- `snapshots.create`: Allow creating snapshots
- `version`: Allow retrieving version information
- `keys.get`: Allow retrieving API keys
- `keys.create`: Allow creating API keys
- `keys.update`: Allow updating API keys
- `keys.delete`: Allow deleting API keys

### Response

Returns a [key object](#key-object) with the `key` field included.

### Example

```bash
curl \
  -X POST 'http://localhost:7700/keys' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer MASTER_KEY' \
  --data-binary '{
    "description": "Search API key for website frontend",
    "name": "Frontend search key",
    "actions": ["search"],
    "indexes": ["products"],
    "expiresAt": "2025-01-01T00:00:00Z"
  }'
```

#### Response: `201 Created`

```json
{
  "key": "d0552b41536279a0ad88bd595327b96f01176a60c2243e906c52ac02375f9bc4",
  "description": "Search API key for website frontend",
  "name": "Frontend search key",
  "uid": "298b0945-8b23-4e45-aa87-3cc3b8f0dc4e",
  "actions": ["search"],
  "indexes": ["products"],
  "expiresAt": "2025-01-01T00:00:00Z",
  "createdAt": "2021-08-11T10:00:00Z",
  "updatedAt": "2021-08-11T10:00:00Z"
}
```

## Update a key

<RouteHighlighter method="PATCH" path="/keys/:uid_or_key" />

Update an existing API key. Only `name` and `description` can be updated. To update other fields, delete and recreate the key.

### Path parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `uid_or_key` | String | True | `uid` or `key` value of the key to update |

### Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | String | False | New key description |
| `name` | String | False | New key name |

### Response

Returns the updated [key object](#key-object).

### Example

```bash
curl \
  -X PATCH 'http://localhost:7700/keys/298b0945-8b23-4e45-aa87-3cc3b8f0dc4e' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer MASTER_KEY' \
  --data-binary '{
    "description": "Updated description",
    "name": "Updated name"
  }'
```

#### Response: `200 Ok`

```json
{
  "description": "Updated description",
  "name": "Updated name",
  "uid": "298b0945-8b23-4e45-aa87-3cc3b8f0dc4e",
  "actions": ["search"],
  "indexes": ["products"],
  "expiresAt": "2025-01-01T00:00:00Z",
  "createdAt": "2021-08-11T10:00:00Z",
  "updatedAt": "2021-08-12T14:30:00Z"
}
```

## Delete a key

<RouteHighlighter method="DELETE" path="/keys/:uid_or_key" />

Delete an API key.

### Path parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `uid_or_key` | String | True | `uid` or `key` value of the key to delete |

### Response

Returns `204 No Content` on success.

### Example

```bash
curl \
  -X DELETE 'http://localhost:7700/keys/298b0945-8b23-4e45-aa87-3cc3b8f0dc4e' \
  -H 'Authorization: Bearer MASTER_KEY'
```

#### Response: `204 No Content`
