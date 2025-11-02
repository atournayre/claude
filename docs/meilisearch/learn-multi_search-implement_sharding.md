# Implement sharding with remote federated search

**Source:** https://www.meilisearch.com/docs/learn/multi_search/implement_sharding.md
**Extrait le:** 2025-10-08
**Sujet:** Multi-search - Sharding implementation

---

> This guide walks you through implementing a sharding strategy by activating the `/network` route, configuring the network object, and performing remote federated searches.

export const NoticeTag = ({label}) => <span className="noticeTag noticeTag--{ label }">
    {label}
  </span>;

Sharding is the process of splitting an index containing many documents into multiple smaller indexes, often called shards. This horizontal scaling technique is useful when handling large databases. In Meilisearch, the best way to implement a sharding strategy is to use remote federated search.

This guide walks you through activating the `/network` route, configuring the network object, and performing remote federated searches.

<NoticeTag label="Enterprise Edition" />

Sharding is an Enterprise Edition feature. You are free to use it for evaluation purposes. Please [reach out to us](mailto:sales@meilisearch.com) before using it in production.

<Tip>
  ## Configuring multiple instances

  To minimize issues and limit unexpected behavior, instance, network, and index configuration should be identical for all shards. This guide describes the individual steps you must take on a single instance and assumes you will replicate them across all instances.
</Tip>

## Prerequisites

* Multiple Meilisearch projects (instances) running Meilisearch >=v1.19

## Activate the `/network` endpoint

### Meilisearch Cloud

If you are using Meilisearch Cloud, contact support to enable this feature in your projects.

### Self-hosting

Use the `/experimental-features` route to enable `network`:

```sh
curl \
  -X PATCH 'MEILISEARCH_URL/experimental-features/' \
  -H 'Content-Type: application/json'  \
  --data-binary '{
    "network": true
  }'
```

Meilisearch should respond immediately, confirming the route is now accessible. Repeat this process for all instances.

## Configuring the network object

Next, you must configure the network object. It consists of the following fields:

* `remotes`: defines a list with the required information to access each remote instance
* `self`: specifies which instance is the current one
