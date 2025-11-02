# Experimental features overview

**Source:** https://www.meilisearch.com/docs/learn/resources/experimental_features_overview.md
**Extrait le:** 2025-10-08
**Sujet:** Resources - Experimental Features

---

> This article covers how to activate activate and configure Meilisearch experimental features.

Meilisearch periodically introduces new experimental features. Experimental features are not always ready for production, but offer functionality that might benefit some users.

An experimental feature's API can change significantly and become incompatible between releases. Keep this in mind when using experimental features in a production environment.

Meilisearch makes experimental features available expecting they will become stable in a future release, but this is not guaranteed.

## Activating experimental features

Experimental features fall into two groups based on how they are activated or deactivated:

1. Those that are activated at launch with a command-line flag or environment variable
2. Those that are activated with the [`/experimental-features` API route](/reference/api/experimental_features).

## Activating experimental features at launch

Some experimental features can be [activated at launch](/learn/self_hosted/configure_meilisearch_at_launch), for example with a command-line flag:

```sh
./meilisearch --experimental-enable-metrics
```

Flags and environment variables for experimental features are not included in the [regular configuration options list](/learn/self_hosted/configure_meilisearch_at_launch#all-instance-options). Instead, consult the specific documentation page for the feature you are interested in, which can be found in the experimental section.

Command-line flags for experimental features are always prefixed with `--experimental`. Environment variables for experimental features are always prefixed with `MEILI_EXPERIMENTAL`.

Activating or deactivating experimental features this way requires you to relaunch Meilisearch.

### Activating experimental features during runtime

Some experimental features can be activated via an HTTP call using the [`/experimental-features` API route](/reference/api/experimental_features):

<CodeGroup>
  ```bash cURL
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json'  \
    --data-binary '{
      "metrics": true
    }'
  ```

  ```ruby Ruby
  client.update_experimental_features(metrics: true)
  ```

  ```go Go
  ```
