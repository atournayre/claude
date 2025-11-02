# Semantic Search with Cloudflare Worker AI Embeddings

**Source:** https://www.meilisearch.com/docs/guides/embedders/cloudflare.md
**Extrait le:** 2025-10-08
**Sujet:** Embedders Guide - Cloudflare Worker AI Integration

---

> This guide will walk you through the process of setting up Meilisearch with Cloudflare Worker AI embeddings to enable semantic search capabilities.

## Introduction

This guide will walk you through the process of setting up Meilisearch with Cloudflare Worker AI embeddings to enable semantic search capabilities. By leveraging Meilisearch's AI features and Cloudflare Worker AI's embedding API, you can enhance your search experience and retrieve more relevant results.

## Requirements

To follow this guide, you'll need:

* A [Meilisearch Cloud](https://www.meilisearch.com/cloud) project running version >=1.13
* A Cloudflare account with access to Worker AI and an API key. You can sign up for a Cloudflare account at [Cloudflare](https://www.cloudflare.com/)
* Your Cloudflare account ID

## Setting up Meilisearch

To set up an embedder in Meilisearch, you need to configure it to your settings. You can refer to the [Meilisearch documentation](/reference/api/settings) for more details on updating the embedder settings.

Cloudflare Worker AI offers the following embedding models:

* `baai/bge-base-en-v1.5`: 768 dimensions
* `baai/bge-large-en-v1.5`: 1024 dimensions
* `baai/bge-small-en-v1.5`: 384 dimensions

Here's an example of embedder settings for Cloudflare Worker AI:

```json
{
  "cloudflare": {
    "source": "rest",
    "apiKey": "<API Key>",
    "dimensions": 384,
    "documentTemplate": "<Custom template (Optional, but recommended)>",
    "url": "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai/run/@cf/<Model>",
    "request": {
      "text": ["{{text}}", "{{..}}"]
    },
    "response": {
      "result": {
        "data": ["{{embedding}}"]
      }
    }
  }
}
```
