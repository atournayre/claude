# Semantic Search with Cohere Embeddings

**Source:** https://www.meilisearch.com/docs/guides/embedders/cohere.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Embedders - Cohere Integration

---

# Semantic Search with Cohere Embeddings

> This guide will walk you through the process of setting up Meilisearch with Cohere embeddings to enable semantic search capabilities.

## Introduction

This guide will walk you through the process of setting up Meilisearch with Cohere embeddings to enable semantic search capabilities. By leveraging Meilisearch's AI features and Cohere's embedding API, you can enhance your search experience and retrieve more relevant results.

## Requirements

To follow this guide, you'll need:

* A [Meilisearch Cloud](https://www.meilisearch.com/cloud) project running version >=1.13
* A Cohere account with an API key for embedding generation. You can sign up for a Cohere account at [Cohere](https://cohere.com/).
* No backend required.

## Setting up Meilisearch

To set up an embedder in Meilisearch, you need to configure it to your settings. You can refer to the [Meilisearch documentation](/reference/api/settings) for more details on updating the embedder settings.

Cohere offers multiple embedding models:

* `embed-english-v3.0` and `embed-multilingual-v3.0`: 1024 dimensions
* `embed-english-light-v3.0` and `embed-multilingual-light-v3.0`: 384 dimensions

Here's an example of embedder settings for Cohere:

```json
{
  "cohere": {
    "source": "rest",
    "apiKey": "<Cohere API Key>",
    "dimensions": 1024,
    "documentTemplate": "<Custom template (Optional, but recommended)>",
    "url": "https://api.cohere.com/v1/embed",
    "request": {
      "model": "embed-english-v3.0",
      "texts": [
        "{{text}}",
        "{{..}}"
      ],
      "input_type": "search_document"
    },
    "response": {
      "embeddings": [
        "{{embedding}}",
        "{{..}}"
      ]
    }
  }
}
```
