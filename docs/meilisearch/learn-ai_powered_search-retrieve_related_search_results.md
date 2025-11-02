# Retrieve related search results

**Source:** https://www.meilisearch.com/docs/learn/ai_powered_search/retrieve_related_search_results.md
**Extrait le:** 2025-10-08
**Sujet:** AI-Powered Search - Retrieve Related Search Results

---

# Retrieve related search results

> This guide shows you how to use the similar documents endpoint to create an AI-powered movie recommendation workflow.

# Retrieve related search results

This guide shows you how to use the [similar documents endpoint](/reference/api/similar) to create an AI-powered movie recommendation workflow.

First, you will create an embedder and add documents to your index. You will then perform a search, and use the top result's primary key to retrieve similar movies in your database.

## Prerequisites

* A running Meilisearch project
* A [tier >=2](https://platform.openai.com/docs/guides/rate-limits#usage-tiers) OpenAI API key

## Create a new index

Create an index called `movies` and add this <a href="/assets/datasets/movies.json" download="movies.json">`movies.json`</a> dataset to it. If necessary, consult the [getting started](/learn/getting_started/cloud_quick_start) for more instructions on index creation.

Each document in the dataset represents a single movie and has the following structure:

* `id`: a unique identifier for each document in the database
* `title`: the title of the movie
* `overview`: a brief summary of the movie's plot
* `genres`: an array of genres associated with the movie
* `poster`: a URL to the movie's poster image
* `release_date`: the release date of the movie, represented as a Unix timestamp

## Configure an embedder

Next, use the Cloud UI to configure an OpenAI embedder:

<img src="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/similar-guide/01-add-embedder-ui.gif?s=f51f0a2afd10d4614c8be26f34ddfa1e" alt="Animated image of the Meilisearch Cloud UI showing a user clicking on &#x22;add embedder&#x22;. This opens up a modal window, where the user fills in the name of the embedder, chooses OpenAI as its source. They then select a model, input their API key, and type out a document template." data-