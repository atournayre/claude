# Image search with multimodal embeddings

**Source:** https://www.meilisearch.com/docs/learn/ai_powered_search/image_search_with_multimodal_embeddings.md
**Extrait le:** 2025-10-08
**Sujet:** AI-Powered Search - Multimodal Image Search

---

# Image search with multimodal embeddings

> This article shows you the main steps for performing multimodal text-to-image searches

This guide shows the main steps to search through a database of images using Meilisearch's experimental multimodal embeddings.

## Requirements

* A database of images
* A Meilisearch project
* Access to a multimodal embedding provider (for example, [VoyageAI multimodal embeddings](https://docs.voyageai.com/reference/multimodal-embeddings-api))

## Enable multimodal embeddings

First, enable the `multimodal` experimental feature:

```sh
curl \
  -X PATCH 'MEILISEARCH_URL/experimental-features/' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "multimodal": true
  }'
```

You may also enable multimodal in your Meilisearch Cloud project's general settings, under "Experimental features".

## Configure a multimodal embedder

Much like other embedders, multimodal embedders must set their `source` to `rest` and explicitly declare their `url`. Depending on your chosen provider, you may also have to specify `apiKey`.

All multimodal embedders must contain an `indexingFragments` field and a `searchFragments` field. Fragments are sets of embeddings built out of specific parts of document data.

Fragments must follow the structure defined by the REST API of your chosen provider.

### `indexingFragments`

Use `indexingFragments` to tell Meilisearch how to send document data to the provider's API when generating document embeddings.

For example, when using VoyageAI's multimodal model, an indexing fragment might look like this:

```json
"indexingFragments": {
  "TEXTUAL_FRAGMENT_NAME": {
    "value": {
      "content": [
        {
          "type": "text",
          "text": "A document named {{doc.title}} described as {{doc.description}}"
        }
      ]
    }
  },
  "IMAGE_FRAGMENT_NAME": {
    "value": {
      "content": [
        {
          "type": "image_url",
          "image_url": "{{doc.image_url}}"
        }
      ]
    }
  }
}
```

### `searchFragments`

Use `searchFragments` to tell Meilisearch how to send search queries to the provider's API when generating query embeddings.

For example, when using VoyageAI's multimodal model, a search fragment might look like this:

```json
"searchFragments": {
  "TEXTUAL_FRAGMENT_NAME": {
    "value": {
      "content": [
        {
          "type": "text",
          "text": "{{doc.search_query}}"
        }
      ]
    }
  }
}
```

### Complete multimodal embedder configuration

The following example shows a complete multimodal embedder configuration using VoyageAI:

```json
{
  "multimodal_embedder": {
    "source": "rest",
    "url": "https://api.voyageai.com/v1/multimodalembeddings",
    "apiKey": "YOUR_VOYAGE_AI_API_KEY",
    "request": "{{text}}",
    "response": "{{embedding}}",
    "indexingFragments": {
      "text": {
        "value": {
          "content": [
            {
              "type": "text",
              "text": "A document named {{doc.title}} described as {{doc.description}}"
            }
          ]
        }
      },
      "image": {
        "value": {
          "content": [
            {
              "type": "image_url",
              "image_url": "{{doc.image_url}}"
            }
          ]
        }
      }
    },
    "searchFragments": {
      "text": {
        "value": {
          "content": [
            {
              "type": "text",
              "text": "{{doc.search_query}}"
            }
          ]
        }
      }
    }
  }
}
```

## Index your images

After configuring your multimodal embedder, add your image data to Meilisearch. Make sure your documents include the fields referenced in your embedder configuration:

```json
[
  {
    "id": 1,
    "title": "Mountain Landscape",
    "description": "Beautiful mountain vista at sunset",
    "image_url": "https://example.com/images/mountain.jpg"
  },
  {
    "id": 2,
    "title": "Ocean Beach",
    "description": "Tropical beach with clear blue water",
    "image_url": "https://example.com/images/beach.jpg"
  }
]
```

## Perform multimodal searches

Once your documents are indexed and embeddings are generated, you can perform text-to-image searches:

```sh
curl \
  -X POST 'MEILISEARCH_URL/indexes/images/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "sunset mountains",
    "hybrid": {
      "embedder": "multimodal_embedder",
      "semanticRatio": 1.0
    }
  }'
```

This search will find images that semantically match your text query, even if the exact words don't appear in the image metadata.
