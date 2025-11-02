# Improve relevancy when working with large documents

**Source:** https://www.meilisearch.com/docs/guides/improve_relevancy_large_documents.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Amélioration de la pertinence pour les documents volumineux

---

# Improve relevancy when working with large documents

> Use JavaScript with Node.js to split a single large document and configure Meilisearch with a distinct attribute to prevent duplicated results.

Meilisearch is optimized for handling paragraph-sized chunks of text. Datasets with many documents containing large amounts of text may lead to reduced search result relevancy.

In this guide, you will see how to use JavaScript with Node.js to split a single large document and configure Meilisearch with a distinct attribute to prevent duplicated results.

## Requirements

* A running Meilisearch project
* A command-line console
* Node.js v18

## Dataset

<a id="downloadstories" href="/assets/datasets/stories.json" download="stories.json">`stories.json`</a> contains two documents, each storing the full text of a short story in its `text` field:

```json
[
  {
    "id": 0,
    "title": "A Haunted House",
    "author": "Virginia Woolf",
    "text": "Whatever hour you woke there was a door shutting. From room to room they went, hand in hand, lifting here, opening there, making sure—a ghostly couple.\n\n \"Here we left it,\" she said. And he added, \"Oh, but here too!\" \"It's upstairs,\" she murmured. \"And in the garden,\" he whispered. \"Quietly,\" they said, \"or we shall wake them.\"\n\nBut it wasn't that you woke us. Oh, no. \"They're looking for it; they're drawing the curtain,\" one might say, and so read on a page or two. \"Now they've found it,\" one would be certain, stopping the pencil on the margin. And then, tired of reading, one might rise and see for oneself, the house all empty, the doors standing open, only the wood pigeons bubbling with content and the hum of the threshing machine sounding from the farm. \"What did I come in here for? What did I want to find?\" My hands were empty. \"Perhaps it's upstairs then?\" The apples were in the loft. And so down again, the garden still
