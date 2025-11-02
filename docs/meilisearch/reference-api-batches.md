# Batches

**Source:** https://www.meilisearch.com/docs/reference/api/batches.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Batches

---

# Batches

> The /batches route allows you to monitor how Meilisearch is grouping and processing asynchronous operations.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <parameter name="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/batches` route gives information about the progress of batches of [asynchronous operations](/learn/async/asynchronous_operations).

## Batch object

```json
{
  "uid": 0,
  "progress": {
    "steps": [
      {
        "currentStep": "extracting words",
        "finished": 2,
        "total": 9,
      },
      {
        "currentStep": "document",
        "finished": 30546,
        "total": 31944,
      }
    ],
    "percentage": 32.8471
  },
  "details": {
    "receivedDocuments": 6,
    "indexedDocuments": 6
  },
  "stats": {
    "totalNbTasks": 1,
    "status": {
      "succeeded": 1
    },
    "types": {
      "documentAdditionOrUpdate": 1
    },
    "indexUids": {
      "INDEX_NAME": 1
    },
    "progressTrace": { … },
    "writeChannelCongestion": { … },
    "internalDatabaseSizes": { … },
    "embedderRequests": {
      "total": 12,
      "failed": 5,
      "lastError": "runtime error: received internal error HTTP 500 from embedding server\n  - server replied with `{\"error\":\"Service Unavailable\"}`"
    }
  },
  "duration": "PT0.250518S",
  "startedAt": "2024-01-01T09:39:00.000000Z",
  "finishedAt": "2024-01-01T09:39:00.250518Z"
}
```

| Field                                                   | Type    | Description                                                                                     |
|---------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------|
| **`uid`**                                               | Integer | Unique sequential identifier of the batch                                                       |
| **`progress`**                                          | Object  | Information about batch progress, only present for batches with `processing` status             |
| **`progress.steps`**                                    | Array   | Steps of the batch; one entry per task type present in the batch                               |
| **`progress.steps[].currentStep`**                      | String  | Current processing step for this task type                                                      |
| **`progress.steps[].finished`**                         | Integer | Number of finished steps                                                                        |
| **`progress.steps[].total`**                            | Integer | Total number of steps for this task type                                                        |
| **`progress.percentage`**                               | Float   | Estimated percentage of completion (0-100)                                                      |
| **`details`**                                           | Object  | Details of the batch according to each task type                                                |
| **`stats`**                                             | Object  | Detailed statistics about this batch                                                            |
| **`stats.totalNbTasks`**                                | Integer | Total number of tasks in this batch                                                             |
| **`stats.status`**                                      | Object  | Number of tasks per status (`enqueued`, `processing`, `succeeded`, `failed`, `canceled`)        |
| **`stats.types`**                                       | Object  | Number of tasks per type                                                                        |
| **`stats.indexUids`**                                   | Object  | Number of tasks per index                                                                       |
| **`stats.progressTrace`**                               | Object  | Only present when batch is `processing`. Traces progress statistics for each step               |
| **`stats.writeChannelCongestion`**                      | Object  | Only present when batch is `processing`. Information about write channel congestion             |
| **`stats.internalDatabaseSizes`**                       | Object  | Only present when batch is `processing`. Information about internal database sizes              |
| **`stats.embedderRequests`**                            | Object  | Only present when batch uses embedders. Information about embedder requests                     |
| **`stats.embedderRequests.total`**                      | Integer | Total number of embedder requests                                                               |
| **`stats.embedderRequests.failed`**                     | Integer | Number of failed embedder requests                                                              |
| **`stats.embedderRequests.lastError`**                  | String  | Last error message from embedder, if any                                                        |
| **`duration`**                                          | String  | Total elapsed time, in ISO 8601 format                                                          |
| **`startedAt`**                                         | String  | When batch processing started (RFC 3339 format)                                                 |
| **`finishedAt`**                                        | String  | When batch processing finished (RFC 3339 format)                                                |

## Get one batch

<RouteHighlighter method="GET" path="/batches/:batch_uid" />

Get a single batch.

### Path parameters

| Name              | Type    | Description                           |
|-------------------|---------|---------------------------------------|
| **`batch_uid`** * | Integer | [`uid`](/reference/api/batches#uid) of the requested batch |

### Example

<CodeSamples id="get_one_batch_1" />

#### Response: `200 Ok`

```json
{
  "uid": 0,
  "progress": null,
  "details": {
    "receivedDocuments": 6,
    "indexedDocuments": 6
  },
  "stats": {
    "totalNbTasks": 1,
    "status": {
      "succeeded": 1
    },
    "types": {
      "documentAdditionOrUpdate": 1
    },
    "indexUids": {
      "INDEX_NAME": 1
    }
  },
  "duration": "PT0.250518S",
  "startedAt": "2024-01-01T09:39:00.000000Z",
  "finishedAt": "2024-01-01T09:39:00.250518Z"
}
```

## Get batches

<RouteHighlighter method="GET" path="/batches" />

List all batches. Results are paginated and displayed in reverse chronological order.

By default, Meilisearch displays the first 20 results.

### Query parameters

| Query Parameter                      | Default Value | Description                                                                                                         |
|--------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------|
| **`limit`**                          | `20`          | Number of batches to return                                                                                         |
| **`from`**                           | `null`        | Fetch batches after this [`uid`](/reference/api/batches#uid)                                                        |
| **`uids`**                           | `*` (all)     | Filter batches by their [`uid`](/reference/api/batches#uid). Separate multiple values with a comma (`,`)           |
| **`statuses`**                       | `*` (all)     | Filter batches by their [`status`](/reference/api/batches#status). Separate multiple values with a comma (`,`)     |
| **`types`**                          | `*` (all)     | Filter batches by their task [`type`](/reference/api/tasks#type). Separate multiple values with a comma (`,`)      |
| **`indexUids`**                      | `*` (all)     | Filter batches by their [`indexUid`](/reference/api/tasks#indexuid). Separate multiple values with a comma (`,`)   |
| **`afterEnqueuedAt`**                | `null`        | Filter batches after this `enqueuedAt` date. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format              |
| **`beforeEnqueuedAt`**               | `null`        | Filter batches before this `enqueuedAt` date. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format             |
| **`afterStartedAt`**                 | `null`        | Filter batches after this `startedAt` date. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format               |
| **`beforeStartedAt`**                | `null`        | Filter batches before this `startedAt` date. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format              |
| **`afterFinishedAt`**                | `null`        | Filter batches after this `finishedAt` date. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format              |
| **`beforeFinishedAt`**               | `null`        | Filter batches before this `finishedAt` date. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format             |

### Example

<CodeSamples id="get_all_batches_1" />

#### Response: `200 Ok`

```json
{
  "results": [
    {
      "uid": 0,
      "progress": null,
      "details": {
        "receivedDocuments": 6,
        "indexedDocuments": 6
      },
      "stats": {
        "totalNbTasks": 1,
        "status": {
          "succeeded": 1
        },
        "types": {
          "documentAdditionOrUpdate": 1
        },
        "indexUids": {
          "INDEX_NAME": 1
        }
      },
      "duration": "PT0.250518S",
      "startedAt": "2024-01-01T09:39:00.000000Z",
      "finishedAt": "2024-01-01T09:39:00.250518Z"
    }
  ],
  "total": 1,
  "limit": 20,
  "from": 0,
  "next": null
}
```

## Cancel batches

<RouteHighlighter method="POST" path="/batches/cancel" />

Cancel any number of enqueued or processing batches based on their `uid`, `status`, `type`, or `indexUid`. Batch cancellation is an atomic transaction: **either all batches are successfully canceled or none are**.

Tasks in canceled batches are marked as `canceled` and Meilisearch does not process them.

### Query parameters

Same as [`GET /batches` query parameters](/reference/api/batches#query-parameters).

**`uids`, `statuses`, `types`, or `indexUids` is required**. You must use at least one of these filters.

### Example

<CodeSamples id="cancel_batches_1" />

#### Response: `200 Ok`

```json
{
  "taskUid": 3,
  "indexUid": null,
  "status": "enqueued",
  "type": "batchCancelation",
  "enqueuedAt": "2024-01-01T09:39:00.000000Z"
}
```

You can use the returned `taskUid` to track the cancelation progress using the [`/tasks/:task_uid` endpoint](/reference/api/tasks#get-one-task).

## Delete batches

<RouteHighlighter method="DELETE" path="/batches" />

Delete a finished (`succeeded`, `failed`, or `canceled`) batch based on `uid`, `status`, `type`, or `indexUid`. Batch deletion is an atomic transaction: **either all batches are successfully deleted or none are**.

### Query parameters

Same as [`GET /batches` query parameters](/reference/api/batches#query-parameters).

**`uids`, `statuses`, `types`, or `indexUids` is required**. You must use at least one of these filters.

### Example

<CodeSamples id="delete_batches_1" />

#### Response: `200 Ok`

```json
{
  "taskUid": 3,
  "indexUid": null,
  "status": "enqueued",
  "type": "batchDeletion",
  "enqueuedAt": "2024-01-01T09:39:00.000000Z"
}
```

You can use the returned `taskUid` to track the deletion progress using the [`/tasks/:task_uid` endpoint](/reference/api/tasks#get-one-task).
