# Getting started with AI-powered search

**Source:** https://www.meilisearch.com/docs/learn/ai_powered_search/getting_started_with_ai_search.md
**Extrait le:** 2025-10-08
**Sujet:** AI-Powered Search - Getting Started Guide

---

> AI-powered search uses LLMs to retrieve search results. This tutorial shows you how to configure an OpenAI embedder and perform your first search.

[AI-powered search](https://meilisearch.com/solutions/vector-search), sometimes also called vector search or hybrid search, uses [large language models (LLMs)](https://en.wikipedia.org/wiki/Large_language_model) to retrieve search results based on the meaning and context of a query.

This tutorial will walk you through configuring AI-powered search in your Meilisearch project. You will see how to set up an embedder with OpenAI, generate document embeddings, and perform your first search.

## Requirements

* A running Meilisearch project
* An [OpenAI API key](https://platform.openai.com/api-keys)
* A command-line console

## Create a new index

First, create a new Meilisearch project. If this is your first time using Meilisearch, follow the [quick start](/learn/getting_started/cloud_quick_start) then come back to this tutorial.

Next, create a `kitchenware` index and add [this kitchenware products dataset](/assets/datasets/kitchenware.json) to it. It will take Meilisearch a few moments to process your request, but you can continue to the next step while your data is indexing.

## Generate embeddings with OpenAI

In this step, you will configure an OpenAI embedder. Meilisearch uses **embedders** to translate documents into **embeddings**, which are mathematical representations of a document's meaning and context.

Open a blank file in your text editor. You will only use this file to build your embedder one step at a time, so there's no need to save it if you plan to finish the tutorial in one sitting.

### Choose an embedder name

In your blank file, create your `embedder` object:

```json
{
  "products-openai": {}
}
```

`products-openai` is the name of your embedder for this tutorial. You can name embedders any way you want, but try to keep it simple, short, and easy to remember.

###
