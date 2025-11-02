# Semantic Search with Mistral Embeddings

**Source:** https://www.meilisearch.com/docs/guides/embedders/mistral.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Embedders - Mistral Integration

---

> This guide will walk you through the process of setting up Meilisearch with Mistral embeddings to enable semantic search capabilities.

## Introduction

This guide will walk you through the process of setting up Meilisearch with Mistral embeddings to enable semantic search capabilities. By leveraging Meilisearch's AI features and Mistral's embedding API, you can enhance your search experience and retrieve more relevant results.

## Requirements

To follow this guide, you'll need:

* A [Meilisearch Cloud](https://www.meilisearch.com/cloud) project running version >=1.13
* A Mistral account with an API key for embedding generation. You can sign up for a Mistral account at [Mistral](https://mistral.ai/).
* No backend required.

## Setting up Meilisearch

To set up an embedder in Meilisearch, you need to configure it to your settings. You can refer to the [Meilisearch documentation](/reference/api/settings) for more details on updating the embedder settings.

While using Mistral to generate embeddings, you'll need to use the model `mistral-embed`. Unlike some other services, Mistral currently offers only one embedding model.

Here's an example of embedder settings for Mistral:

```json
{
  "mistral": {
    "source": "rest",
    "apiKey": "<Mistral API Key>",
    "dimensions": 1024,
    "documentTemplate": "<Custom template (Optional, but recommended)>",
    "url": "https://api.mistral.ai/v1/embeddings",
    "request": {
      "model": "mistral-embed",
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

* `source`: Specifies the source of the embedder, which is set to "rest" for using a REST API.
* `apiKey`: Replace `<Mistral API Key>` with your actual Mistral API key.
* `dimensions`: Sets the embedding dimensions to 1024, which is the standard for Mistral embeddings.
* `documentTemplate`: An optional field for customizing how documents are formatted before embedding. This is recommended to improve relevance.
* `url`: The endpoint for Mistral's embedding API.
* `request`: Defines the structure of the request sent to Mistral, including the model and input format.
* `response`: Specifies how to parse the embedding data from Mistral's response.

## Testing your setup

Once you've configured the embedder, you can test it by performing a semantic search query. Meilisearch will automatically use the configured embedder to generate embeddings for your search queries and documents.

Example search query:

```bash
curl -X POST 'http://localhost:7700/indexes/movies/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "space adventure",
    "hybrid": {
      "embedder": "mistral",
      "semanticRatio": 1.0
    }
  }'
```

This query will use the Mistral embedder to find semantically similar documents, even if they don't contain the exact keywords "space adventure".
