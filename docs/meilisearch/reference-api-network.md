# Network API Reference

**Source:** https://www.meilisearch.com/docs/reference/api/network.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Network

---

# Network

> Use the `/network` route to create a network of Meilisearch instances.

Use the `/network` route to create a network of Meilisearch instances. This is particularly useful when used together with federated search to implement horizontal database partition strategies such as sharding.

<Note>
  This is an experimental feature. Use the Meilisearch Cloud UI or the experimental features endpoint to activate it:

  ```sh
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "network": true
    }'
  ```
</Note>

<Warning>
  If an attribute is both:

  * not on the `displayedAttributes` list
  * present on the `sortableAttributes`

  It is possible its value becomes publicly accessible via the `/network` endpoint.

  Do not enable the `network` feature if you rely on the value of attributes not present in `displayedAttributes` to remain hidden at all times.
</Warning>

## The network object

```json
{
  "self": "ms-00",
  "sharding": false,
  "remotes": {
    "ms-00": {
      "url": "http://ms-1235.example.meilisearch.io",
      "searchApiKey": "Ecd1SDDi4pqdJD6qYLxD3y7VZAEb4d9j6LJgt4d6xas",
      "writeApiKey": "O2OaIHgwGuHNx9duH6kSe1YJ55Bh0dXvLhbr8FQVvr3vRVViBO"
    },
    "ms-01": {
      "url": "http://ms-4242.example.meilisearch.io",
      "searchApiKey": "hrVu-OMcjPGElK7692K7bwriBoGyHXTMvB5NmZkMKqQ",
      "writeApiKey": "AXmRMjdYT0tT_5pzQOhT0bWe7dLUdXvtl2bPBvx3XT0"
    }
  }
}
```

## Endpoints

- [Get network configuration](#get-network-configuration)
- [Update network configuration](#update-network-configuration)

## Get network configuration

<RouteHighlighter method="GET" path="/network"/>

Get the network configuration of a Meilisearch instance.

### Example

```sh
curl \
  -X GET 'http://localhost:7700/network' \
  -H 'Authorization: Bearer MASTER_KEY'
```

### Response

```json
{
  "self": "ms-00",
  "sharding": false,
  "remotes": {
    "ms-00": {
      "url": "http://ms-1235.example.meilisearch.io",
      "searchApiKey": "Ecd1SDDi4pqdJD6qYLxD3y7VZAEb4d9j6LJgt4d6xas",
      "writeApiKey": "O2OaIHgwGuHNx9duH6kSe1YJ55Bh0dXvLhbr8FQVvr3vRVViBO"
    },
    "ms-01": {
      "url": "http://ms-4242.example.meilisearch.io",
      "searchApiKey": "hrVu-OMcjPGElK7692K7bwriBoGyHXTMvB5NmZkMKqQ",
      "writeApiKey": "AXmRMjdYT0tT_5pzQOhT0bWe7dLUdXvtl2bPBvx3XT0"
    }
  }
}
```

## Update network configuration

<RouteHighlighter method="PATCH" path="/network"/>

Update the network configuration of a Meilisearch instance.

### Body

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `self` | String | `null` | A string identifying the current instance. Must be unique within the network |
| `sharding` | Boolean | `false` | Whether this instance is part of a sharded network |
| `remotes` | Object | `{}` | An object mapping remote instance identifiers to their configuration |

Each entry in `remotes` must contain:

| Field | Type | Description |
|-------|------|-------------|
| `url` | String | The URL of the remote Meilisearch instance |
| `searchApiKey` | String | API key with search permissions for the remote instance |
| `writeApiKey` | String | API key with write permissions for the remote instance |

### Example

```sh
curl \
  -X PATCH 'http://localhost:7700/network' \
  -H 'Authorization: Bearer MASTER_KEY' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "self": "ms-00",
    "sharding": true,
    "remotes": {
      "ms-01": {
        "url": "http://ms-4242.example.meilisearch.io",
        "searchApiKey": "hrVu-OMcjPGElK7692K7bwriBoGyHXTMvB5NmZkMKqQ",
        "writeApiKey": "AXmRMjdYT0tT_5pzQOhT0bWe7dLUdXvtl2bPBvx3XT0"
      }
    }
  }'
```

### Response

```json
{
  "self": "ms-00",
  "sharding": true,
  "remotes": {
    "ms-01": {
      "url": "http://ms-4242.example.meilisearch.io",
      "searchApiKey": "hrVu-OMcjPGElK7692K7bwriBoGyHXTMvB5NmZkMKqQ",
      "writeApiKey": "AXmRMjdYT0tT_5pzQOhT0bWe7dLUdXvtl2bPBvx3XT0"
    }
  }
}
```
