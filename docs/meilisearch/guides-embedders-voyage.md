# Semantic Search with Voyage AI Embeddings

**Source:** https://www.meilisearch.com/docs/guides/embedders/voyage.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Embedders - Voyage AI Integration

---

> This guide will walk you through the process of setting up Meilisearch with Voyage AI embeddings to enable semantic search capabilities.

## Introduction

This guide will walk you through the process of setting up Meilisearch with Voyage AI embeddings to enable semantic search capabilities. By leveraging Meilisearch's AI features and Voyage AI's embedding API, you can enhance your search experience and retrieve more relevant results.

## Requirements

To follow this guide, you'll need:

* A [Meilisearch Cloud](https://www.meilisearch.com/cloud) project running version >=1.13
* A Voyage AI account with an API key for embedding generation. You can sign up for a Voyage AI account at [Voyage AI](https://www.voyageai.com/).
* No backend required.

## Setting up Meilisearch

To set up an embedder in Meilisearch, you need to configure it to your settings. You can refer to the [Meilisearch documentation](/reference/api/settings) for more details on updating the embedder settings.

Voyage AI offers the following embedding models:

* `voyage-large-2-instruct`: 1024 dimensions
* `voyage-multilingual-2`: 1024 dimensions
* `voyage-large-2`: 1536 dimensions
* `voyage-2`: 1024 dimensions

Here's an example of embedder settings for Voyage AI:

```json
{
  "voyage": {
    "source": "rest",
    "apiKey": "<Voyage AI API Key>",
    "dimensions": 1024,
    "documentTemplate": "<Custom template (Optional, but recommended)>",
    "url": "https://api.voyageai.com/v1/embeddings",
    "request": {
      "model": "voyage-2",
      "input": ["{{text}}", "{{..}}"]
    },
    "response": {
      "data": [
        {
          "embedding": "{{embedding}}"
        },
        "{{..}}"
      ]
    }
  }
}
```

In this configuration:

* `source`: Specifies the embedder source, which is "rest" for Voyage AI.
* `apiKey`: Your Voyage AI API key for authentication.
* `dimensions`: The number of dimensions in the embedding vector (1024 for voyage-2).
* `documentTemplate`: A custom template for formatting documents before embedding (optional but recommended).
* `url`: The Voyage AI API endpoint for embeddings.
* `request`: The request body format expected by Voyage AI.
* `response`: The response format from Voyage AI.
