# Using task webhooks

**Source:** https://www.meilisearch.com/docs/learn/async/task_webhook.md
**Extrait le:** 2025-10-08
**Sujet:** Async Operations - Task Webhooks

---

> Learn how to use webhooks to react to changes in your Meilisearch database.

This guide teaches you how to configure a single webhook via instance options to notify a URL when Meilisearch completes a [task](/learn/async/asynchronous_operations).

<Tip>
  If you are using Meilisearch Cloud or need to configure multiple webhooks, use the [`/webhooks` API route](/reference/api/webhooks) instead.
</Tip>

## Requirements

* a command-line console
* a self-hosted Meilisearch instance
* a server configured to receive `POST` requests with an ndjson payload

## Configure the webhook URL

Restart your Meilisearch instance and provide the webhook URL to `--task-webhook-URL`:

```sh
meilisearch --task-webhook-url http://localhost:8000
```

You may also define the webhook URL with environment variables or in the configuration file with `MEILI_TASK_WEBHOOK_URL`.

## Optional: configure an authorization header

Depending on your setup, you may need to provide an authorization header. Provide it to `task-webhook-authorization-header`:

```sh
meilisearch --task-webhook-url http://localhost:8000 --task-webhook-authorization-header Bearer aSampleMasterKey
```

## Test the webhook

A common asynchronous operation is adding or updating documents to an index. The following example adds a test document to our `books` index:

```sh
curl \
  -X POST 'MEILISEARCH_URL/indexes/books/documents' \
  -H 'Content-Type: application/json' \
  --data-binary '[
    {
      "id": 1,
      "title": "Nuestra parte de noche",
      "author": "Mariana Enríquez"
    }
  ]'
```

When Meilisearch finishes indexing this document, it will send a `POST` request the URL you configured with `--task-webhook-url`. The request body will be one or more task objects in [ndjson](https://github.com/ndjson/ndjson-spec) format
