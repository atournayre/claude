# Migrating from Algolia to Meilisearch

**Source:** https://www.meilisearch.com/docs/learn/update_and_migration/algolia_migration.md
**Extrait le:** 2025-10-08
**Sujet:** Migration - Migrating from Algolia to Meilisearch

---

# Migrating from Algolia to Meilisearch

> This guide will take you step-by-step through the creation of a Node.js script to upload data indexed by Algolia to Meilisearch.

## Requirements

- Node.js 14 or higher
- An API key for your [Algolia account](https://www.algolia.com/users/sign_in)
- A running Meilisearch project ([cloud](https://www.meilisearch.com/pricing) or [self-hosted](/learn/cookbooks/docker#setup))

## Create a Node.js project

Create and navigate to a new Node.js directory:

```sh
mkdir algolia-meilisearch
cd algolia-meilisearch
```

Then, initialize a new npm project:

```sh
npm init
```

This guide uses two libraries:

- [algoliasearch](https://www.npmjs.com/package/algoliasearch): the official Algolia library
- [meilisearch](https://www.npmjs.com/package/meilisearch): the official Meilisearch library

Install them as project dependencies:

```sh
npm install algoliasearch meilisearch
```

## Get data from Algolia

### Initialize the Algolia client

First, import `algoliasearch` and initialize the client with your application ID and API key:

```js
const algoliasearch = require('algoliasearch')
const algoliaClient = algoliasearch('YourApplicationID', 'YourAPIKey')
```

### Retrieve an index

Use the Algolia client to retrieve the index you want to migrate. This example retrieves an index called `movies`:

```js
const algoliaIndex = algoliaClient.initIndex('movies')
```

### Fetch all documents

Use `browseObjects()` to fetch all documents in the `movies` index. This method sends batched queries to your index and aggregates the results. Batching queries improves the speed and reliability of large data transfers. The code below also handles potential errors:

```js
const algoliaHits = []

try {
  await algoliaIndex.browseObjects({
    query: '',
    batch: (batch) => {
      algoliaHits.push(...batch)
    }
  })
} catch (error) {
  console.log(error)
}
```

Algolia stores document identifiers in the `objectID` attribute. Rename `objectID` to `id`, since this is [Meilisearch's default primary key](/learn/core_concepts/primary_key):

```js
const algoliaDocuments = algoliaHits.map((hit) => {
  return {
    id: hit.objectID,
    ...hit
  }
})
```

## Import data to Meilisearch

### Initialize the Meilisearch client

Import `meilisearch` and create a new instance of the `MeiliSearch` object. `host` is the URL of your Meilisearch instance, and `apiKey` is your [Meilisearch master key](/learn/security/master_api_keys):

```js
const { MeiliSearch } = require('meilisearch')
const meiliClient = new MeiliSearch({
  host: 'http://127.0.0.1:7700',
  apiKey: 'aSampleMasterKey',
})
```

If you are running a local instance of Meilisearch with the [`--no-env` command-line option](/learn/configuration/instance_options#disable-security), you may omit `apiKey`.

### Add documents to Meilisearch

Use `addDocuments()` to add your documents to your Meilisearch instance:

```js
await meiliClient.index('movies').addDocuments(algoliaDocuments)
```

## Full script

```js
const algoliasearch = require('algoliasearch')
const { MeiliSearch } = require('meilisearch')

const algoliaClient = algoliasearch('YourApplicationID', 'YourAPIKey')
const algoliaIndex = algoliaClient.initIndex('movies')

const meiliClient = new MeiliSearch({
  host: 'http://127.0.0.1:7700',
  apiKey: 'aSampleMasterKey',
})

const algoliaHits = []

;(async () => {
  try {
    await algoliaIndex.browseObjects({
      query: '',
      batch: (batch) => {
        algoliaHits.push(...batch)
      }
    })
  } catch (error) {
    console.log(error)
  }

  const algoliaDocuments = algoliaHits.map((hit) => {
    return {
      id: hit.objectID,
      ...hit
    }
  })

  await meiliClient.index('movies').addDocuments(algoliaDocuments)
})()
```

## Conclusion

This guide walked you through migrating your data from Algolia to Meilisearch using a simple Node.js script. Meilisearch also has [SDKs for other languages](/learn/what_is_meilisearch/sdks), like PHP, Python, Go, and Rust.
