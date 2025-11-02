# Semantic Search with OpenAI Embeddings

**Source:** https://www.meilisearch.com/docs/guides/embedders/openai.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Embedders OpenAI

---

# Semantic Search with OpenAI Embeddings

> This guide will walk you through the process of setting up Meilisearch with OpenAI embeddings to enable semantic search capabilities.

## Introduction

This guide will walk you through the process of setting up Meilisearch with OpenAI embeddings to enable semantic search capabilities. By leveraging Meilisearch's AI features and OpenAI's embedding API, you can enhance your search experience and retrieve more relevant results.

## Requirements

To follow this guide, you'll need:

* A [Meilisearch Cloud](https://www.meilisearch.com/cloud) project running version >=1.13
* An OpenAI account with an API key for embedding generation. You can sign up for an OpenAI account at [OpenAI](https://openai.com/).
* No backend required.

## Setting up Meilisearch

To set up an embedder in Meilisearch, you need to configure it to your settings. You can refer to the [Meilisearch documentation](/reference/api/settings) for more details on updating the embedder settings.

OpenAI offers three main embedding models:

* `text-embedding-3-large`: 3,072 dimensions
* `text-embedding-3-small`: 1,536 dimensions
* `text-embedding-ada-002`: 1,536 dimensions

Here's an example of embedder settings for OpenAI:

```json
{
  "openai": {
    "source": "openAi",
    "apiKey": "<OpenAI API Key>",
    "dimensions": 1536,
    "documentTemplate": "<Custom template (Optional, but recommended)>",
    "model": "text-embedding-3-small"
  }
}
```

In this configuration:

* `source`: Specifies the source of the embedder, which is set to "openAi" for using OpenAI's API.
* `apiKey`: Replace `<OpenAI API Key>` with your actual OpenAI API key.
* `dimensions`: Specifies the dimensions of the embeddings. Set to 1536 for `text-embedding-3-small` and `text-embedding-ada-002`, or 3072 for `text-embedding-3-large`.
* `documentTemplate`: (Optional) A custom template for generating embeddings from your documents.
* `model`: Specifies the OpenAI embedding model to use.
