# Semantic Search with Hugging Face Inference Endpoints

**Source:** https://www.meilisearch.com/docs/guides/embedders/huggingface.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Embedders - HuggingFace Integration

---

# Semantic Search with Hugging Face Inference Endpoints

> This guide will walk you through the process of setting up Meilisearch with Hugging Face Inference Endpoints.

## Introduction

This guide will walk you through the process of setting up a Meilisearch REST embedder with [Hugging Face Inference Endpoints](https://ui.endpoints.huggingface.co/) to enable semantic search capabilities.

<Note>
  You can use Hugging Face and Meilisearch in two ways: running the model locally by setting the embedder source to `huggingface`, or remotely in Hugging Face's servers by setting the embeder source to `rest`.
</Note>

## Requirements

To follow this guide, you'll need:

* A [Meilisearch Cloud](https://www.meilisearch.com/cloud) project running version >=1.13
* A [Hugging Face account](https://huggingface.co/) with a deployed inference endpoint
* The endpoint URL and API key of the deployed model on your Hugging Face account

## Configure the embedder

Set up an embedder using the update settings endpoint:

```json
{
  "hf-inference": {
    "source": "rest",
    "url": "ENDPOINT_URL",
    "apiKey": "API_KEY",
    "dimensions": 384,
    "documentTemplate": "CUSTOM_LIQUID_TEMPLATE",
    "request": {
      "inputs": ["{{text}}", "{{..}}"],
      "model": "baai/bge-small-en-v1.5"
    },
    "response": ["{{embedding}}", "{{..}}"]
  }
}
```

In this configuration:

* `source`: declares Meilisearch should connect to this embedder via its REST API
* `url`: replace `ENDPOINT_URL` with the address of your Hugging Face model endpoint
* `apiKey`: replace `API_KEY` with your Hugging Face API key
* `dimensions`: specifies the dimensions of the embeddings, which are 384 for `baai/bge-small-en-v1.5`
* `documentTemplate`: an optional field to customize the document template
