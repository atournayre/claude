# Configure a REST embedder

**Source:** https://www.meilisearch.com/docs/learn/ai_powered_search/configure_rest_embedder.md
**Extrait le:** 2025-10-08
**Sujet:** AI-Powered Search - Configuration REST Embedder

---

# Configure a REST embedder

> Create Meilisearch embedders using any provider with a REST API

You can integrate any text embedding generator with Meilisearch if your chosen provider offers a public REST API.

The process of integrating a REST embedder with Meilisearch varies depending on the provider and the way it structures its data. This guide shows you where to find the information you need, then walks you through configuring your Meilisearch embedder based on the information you found.

## Find your embedder provider's documentation

Each provider requires queries to follow a specific structure.

Before beginning to create your embedder, locate your provider's documentation for embedding creation. This should contain the information you need regarding API requests, request headers, and responses.

For example, [Mistral's embeddings documentation](https://docs.mistral.ai/api/#tag/embeddings) is part of their API reference. In the case of [Cloudflare's Workers AI](https://developers.cloudflare.com/workers-ai/models/bge-base-en-v1.5/#Parameters), expected input and response are tied to your chosen model.

## Set up the REST source and URL

Open your text editor and create an embedder object. Give it a name and set its source to `"rest"`:

```json
{
  "EMBEDDER_NAME": {
    "source": "rest"
  }
}
```

Next, configure the URL Meilisearch should use to contact the embedding provider:

```json
{
  "EMBEDDER_NAME": {
    "source": "rest",
    "url": "PROVIDER_URL"
  }
}
```

Setting an embedder name, a `source`, and a `url` is mandatory for all REST embedders.

## Configure the data Meilisearch sends to the provider

Meilisearch's `request` field defines the structure of the input it will send to the provider. The way you must fill this field changes for each provider.

For example, Mistral expects two mandatory parameters: `model` and `input`. It also accepts one optional parameter: `encoding_format`. Cloudflare instead only expects a single field, `text`.

### Choose a model

In many cases, your provider requires you