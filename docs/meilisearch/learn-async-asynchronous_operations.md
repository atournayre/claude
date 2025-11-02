# Tasks and asynchronous operations

**Source:** https://www.meilisearch.com/docs/learn/async/asynchronous_operations.md
**Extrait le:** 2025-10-08
**Sujet:** Learn - Async Operations

---

> Meilisearch uses a task queue to handle asynchronous operations. This in-depth guide explains tasks, their uses, and how to manage them using Meilisearch's API.

Many operations in Meilisearch are processed **asynchronously**. These API requests are not handled immediately—instead, Meilisearch places them in a queue and processes them in the order they were received.

## Which operations are asynchronous?

Every operation that might take a long time to be processed is handled asynchronously. Processing operations asynchronously allows Meilisearch to handle resource-intensive tasks without impacting search performance.

Currently, these are Meilisearch's asynchronous operations:

* Creating an index
* Updating an index
* Swapping indexes
* Deleting an index
* Updating index settings
* Adding documents to an index
* Updating documents in an index
* Deleting documents from an index
* Canceling a task
* Deleting a task
* Creating a dump
* Creating snapshots

## Understanding tasks

When an API request triggers an asynchronous process, Meilisearch creates a task and places it in a [task queue](#task-queue).

### Task objects

Tasks are objects containing information that allow you to track their progress and troubleshoot problems when things go wrong.

A [task object](/reference/api/tasks#task-object) includes data not present in the original request, such as when the request was enqueued, the type of request, and an error code when the task fails:

```json
{
    "uid": 1,
    "indexUid": "movies",
    "status": "enqueued",
    "type": "documentAdditionOrUpdate",
    "canceledBy": null,
    "details": {
        "receivedDocuments": 67493,
        "indexedDocuments": null
    },
    "error": null,
    "duration": null,
    "enqueuedAt": "2021-08-10T14:29:17.000000Z",
    "startedAt": null,
    "finishedAt": null
}
```

For a comprehensive description of each task object field, consult the [task API reference](/reference/api/tasks).
