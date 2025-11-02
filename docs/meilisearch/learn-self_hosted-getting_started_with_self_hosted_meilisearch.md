# Getting started with self-hosted Meilisearch

**Source:** https://www.meilisearch.com/docs/learn/self_hosted/getting_started_with_self_hosted_meilisearch.md
**Extrait le:** 2025-10-08
**Sujet:** Getting Started - Self-Hosted Installation

---

# Getting started with self-hosted Meilisearch

> Learn how to install Meilisearch, index a dataset, and perform your first search.

This quick start walks you through installing Meilisearch, adding documents, and performing your first search.

To follow this tutorial you need:

* A [command line terminal](https://www.learnenough.com/command-line-tutorial#sec-running_a_terminal)
* [cURL](https://curl.se)

<Tip>
  Using Meilisearch Cloud? Check out the dedicated guide, [Getting started with Meilisearch Cloud](/learn/getting_started/cloud_quick_start).
</Tip>

## Setup and installation

First, you need to download and install Meilisearch. This command installs the latest Meilisearch version in your local machine:

```bash
# Install Meilisearch
curl -L https://install.meilisearch.com | sh
```

<InfoBox>
Meilisearch runs in development mode by default without any security. To run Meilisearch in production mode, you must pass a master key using the `--master-key` command-line option:

```bash
./meilisearch --master-key="aSampleMasterKey"
```

For more information, see our [configuration reference](/learn/configuration/instance_options) and [security guide](/learn/security/basic_security).
</InfoBox>

Now launch Meilisearch:

```bash
./meilisearch
```

Meilisearch indicates it is listening for new commands on port 7700:

```bash
888b     888          d8b 888 d8b
8888b   d888          Y8P 888 Y8P
88888b.d88888              888
888Y88888P888  .d88b.  888 888 888 .d8888b   .d88b.   8888b.  888d888 .d8888b 88888b.
888 Y888P 888 d8P  Y8b 888 888 888 88K      d8P  Y8b     "88b 888P"  d88P"    888 "88b
888  Y8P  888 88888888 888 888 888 "Y8888b. 88888888 .d888888 888    888      888  888
888   "   888 Y8b.     888 888 888      X88 Y8b.     888  888 888    Y88b.    888  888
888       888  "Y8888  888 888 888  88888P'  "Y8888  "Y888888 888     "Y8888P 888  888

Database path:       "./data.ms"
Server listening on: "http://127.0.0.1:7700"
```

That's it! You now have Meilisearch running on your local machine.

## Add documents

Documents are the objects Meilisearch processes and returns when you perform a search. When you add documents, Meilisearch stores them in datasets called indexes.

Use cURL to add documents from the command line. `movies.json` is a publicly accessible file containing movie documents:

```bash
curl \
  -X POST 'http://127.0.0.1:7700/indexes/movies/documents' \
  -H 'Content-Type: application/json' \
  --data-binary @movies.json
```

<InfoBox>
Meilisearch returns a summarized version of the task object:

```json
{
  "taskUid": 0,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "documentAdditionOrUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use the `taskUid` to track the status of your request.
</InfoBox>

## Search

Now that you have added documents, you can start searching. Use cURL to search for movies about dogs:

```bash
curl \
  'http://127.0.0.1:7700/indexes/movies/search' \
  -d 'q=dog'
```

Meilisearch returns:

```json
{
  "hits": [
    {
      "id": "263421",
      "title": "A Dog's Will",
      "poster": "https://image.tmdb.org/t/p/w1280/kHu7vABv5KCE0X9YikFbfJMj3va.jpg",
      "overview": "The lively João Grilo and the sly Chicó are poor guys living in the hinterland who cheat a bunch of people in a small Northeast Brazil town. But when they die, they have to be judged by Christ, the Devil and the Virgin Mary, before they are admitted to paradise.",
      "release_date": 957657600
    },
    {
      "id": "960898",
      "title": "Togo",
      "poster": "https://image.tmdb.org/t/p/w1280/921q4n8wvWiFk3doCyYdDRxZjO1.jpg",
      "overview": "The untold true story set in the winter of 1925 that takes you across the treacherous terrain of the Alaskan tundra for an exhilarating and uplifting adventure that will test the strength, courage and determination of one man, Leonhard Seppala, and his lead sled dog, Togo.",
      "release_date": 1576195200
    },
    …
  ],
  "query": "dog",
  "processingTimeMs": 1,
  "limit": 20,
  "offset": 0,
  "estimatedTotalHits": 12
}
```

Congratulations! You have just performed your first Meilisearch search query. 🎉

## What's next?

* Learn how to [configure Meilisearch for production](/learn/cookbooks/running_production)
* Explore [different deployment options](/learn/cookbooks/deployment)
* Use one of Meilisearch's [SDKs and integration tools](/learn/what_is_meilisearch/sdks)
* Take a look at [Meilisearch's API reference](/reference/api/overview)
