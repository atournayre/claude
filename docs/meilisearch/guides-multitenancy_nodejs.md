# Node.js multitenancy guide

**Source:** https://www.meilisearch.com/docs/guides/multitenancy_nodejs.md
**Extrait le:** 2025-10-08
**Sujet:** Guide - Multitenancy avec Node.js

---

> Learn how to implement secure, multitenant search in your Node.js applications.

This guide will walk you through implementing search in a multitenant Node.js application handling sensitive medical data.

## What is multitenancy?

In Meilisearch, you might have one index containing data belonging to many distinct tenants. In such cases, your tenants must only be able to search through their own documents. You can implement this using [tenant tokens](/learn/security/multitenancy_tenant_tokens).

## Requirements

* [Node.js](https://nodejs.org/en) and a package manager like `npm`, `yarn`, or `pnpm`
* [Meilisearch JavaScript SDK](/learn/resources/sdks)
* A Meilisearch server running — see our [quick start](/learn/getting_started/cloud_quick_start)
* A search API key — available in your Meilisearch dashboard
* A search API key UID — retrieve it using the [keys endpoints](/reference/api/keys)

<Tip>
  Prefer self-hosting? Read our [installation guide](/learn/self_hosted/install_meilisearch_locally).
</Tip>

## Data models

This guide uses a simple data model to represent medical appointments. The documents in the Meilisearch index will look like this:

```json
[
  {
    "id": 1,
    "patient": "John",
    "details": "I think I caught a cold. Can you help me?",
    "status": "pending"
  },
  {
    "id": 2,
    "patient": "Zia",
    "details": "I'm suffering from fever. I need an appointment ASAP.",
    "status": "pending"
  },
  {
    "id": 3,
    "patient": "Kevin",
    "details": "Some confidential information Kevin has shared.",
    "status": "confirmed"
  }
]
```

For the purpose of this guide, we assume documents are stored in an `appointments` index.

## Creating a tenant token

The first step is generating a tenant token that will allow a given patient to search only for their appointments.
