# Tasks

**Source:** https://www.meilisearch.com/docs/reference/api/tasks.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Tasks

---

# Tasks

> The /tasks route allows you to manage and monitor Meilisearch's asynchronous operations.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/tasks` route gives information about the progress of [asynchronous operations](/learn/async/asynchronous_operations).

## Get all tasks

<RouteHighlighter method="GET" path="/tasks"/>

List all tasks globally, regardless of index. Task objects are contained in the `results` array.

The `tasks` route also offers extensive filtering and paginating capabilities through [query parameters](#query-parameters).

### Query parameters

| Query parameter | Description                                                                                    | Default value                 |
| --------------- | ---------------------------------------------------------------------------------------------- | ----------------------------- |
| **`limit`**     | Number of tasks to return                                                                      | `20`                          |
| **`from`**      | UID of the first task returned                                                                 | `0` (the earliest task)       |
| **`uids`**      | Filter tasks by their `uid`. Separate multiple task UIDs with a comma (`,`)                    | All tasks                     |
| **`statuses`**  | Filter tasks by their status. Separate multiple task statuses with a comma (`,`)               | All statuses                  |
| **`types`**     | Filter tasks by their type. Separate multiple task types with a comma (`,`)                    | All types                     |
| **`indexUids`** | Filter tasks by their index name. Separate multiple index names with a comma (`,`)             | All indexes                   |
| **`canceledBy`**| Filter tasks by the `uid` of the task that canceled them. Separate multiple task UIDs with a comma (`,`) | All tasks |
| **`beforeEnqueuedAt`** | Filter tasks by enqueued date. Tasks enqueued before the given date will be returned | All tasks |
| **`afterEnqueuedAt`** | Filter tasks by enqueued date. Tasks enqueued after the given date will be returned | All tasks |
| **`beforeStartedAt`** | Filter tasks by start date. Tasks started before the given date will be returned | All tasks |
| **`afterStartedAt`** | Filter tasks by start date. Tasks started after the given date will be returned | All tasks |
| **`beforeFinishedAt`** | Filter tasks by finished date. Tasks finished before the given date will be returned | All tasks |
| **`afterFinishedAt`** | Filter tasks by finished date. Tasks finished after the given date will be returned | All tasks |

[Learn more about filtering and paginating tasks](/learn/async/filtering_tasks).

#### Date filters

All date filters accept dates in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format:

```
2022-06-10T15:17:07Z
2022-06-10T15:17:07.123Z
2022-06-10T15:17:07+02:00
2022-06-10T15:17:07.123+02:00
```

<Capsule intent="note">
Date filters use strict inequalities (e.g., `<`, `>`). This means `afterStartedAt` and `beforeStartedAt` do not include tasks started at the exact specified date.
</Capsule>

#### Paginating tasks

`limit` and `from` support paginating through task objects.

Tasks are sorted by creation date and always return the most recent tasks. For example, if you send three tasks in this order: `A`, then `B`, then `C`, the result will contain tasks `C`, `B`, and `A`, in that order.

**`limit`**: Sets the number of task objects to be returned. If no value is specified, `limit` is set to `20`. `limit` will be capped to a max of `100` (default: `20`).

**`from`**: Sets the starting point for search, and returns tasks with `uid`s lower than the given value. For example, `from=100` will return the most recent tasks created with `uid`s lower than `100`. If no value is specified, `from` is set to `0` (the earliest task).

### Response

| Name          | Type    | Description                                                              |
| ------------- | ------- | ------------------------------------------------------------------------ |
| **`results`** | Array   | An array of [task objects](/reference/api/tasks#task-object)            |
| **`total`**   | Integer | Total number of tasks matching the query                                 |
| **`limit`**   | Integer | Number of tasks returned                                                 |
| **`from`**    | Integer | UID of the first task returned                                           |
| **`next`**    | Integer | Value to use in the `from` query parameter to get the next set of results. If `null`, you have reached the end of the result set |

#### `200 Ok` - All task objects

```json
{
  "results": [
    {
      "uid": 1,
      "indexUid": "movies",
      "status": "succeeded",
      "type": "indexCreation",
      "canceledBy": null,
      "details": {
        "primaryKey": "id"
      },
      "error": null,
      "duration": "PT0.028500S",
      "enqueuedAt": "2021-08-12T10:00:00.000000Z",
      "startedAt": "2021-08-12T10:00:01.000000Z",
      "finishedAt": "2021-08-12T10:00:02.000000Z"
    },
    {
      "uid": 0,
      "indexUid": "movies",
      "status": "succeeded",
      "type": "documentAdditionOrUpdate",
      "canceledBy": null,
      "details": {
        "receivedDocuments": 100,
        "indexedDocuments": 100
      },
      "error": null,
      "duration": "PT0.030000S",
      "enqueuedAt": "2021-08-11T09:25:53.000000Z",
      "startedAt": "2021-08-11T10:03:00.000000Z",
      "finishedAt": "2021-08-11T10:03:00.788440Z"
    }
  ],
  "total": 2,
  "limit": 20,
  "from": 1,
  "next": null
}
```

## Get one task

<RouteHighlighter method="GET" path="/tasks/{task_uid}"/>

Get a single task by its `uid`.

### Path parameters

| Name           | Type    | Description                                             |
| -------------- | ------- | ------------------------------------------------------- |
| **`task_uid`** | Integer | [`uid`](/reference/api/tasks#task-object) of the task. **Required.** |

### Response

Returns a single [task object](/reference/api/tasks#task-object) in JSON format.

#### `200 Ok` - Task object

```json
{
  "uid": 1,
  "indexUid": "movies",
  "status": "succeeded",
  "type": "settingsUpdate",
  "canceledBy": null,
  "details": {
    "rankingRules": [
      "typo",
      "ranking:desc",
      "words",
      "proximity",
      "attribute",
      "exactness"
    ]
  },
  "error": null,
  "duration": "PT1.320718S",
  "enqueuedAt": "2021-08-10T14:29:17.000000Z",
  "startedAt": "2021-08-10T14:29:18.000000Z",
  "finishedAt": "2021-08-10T14:29:19.788440Z"
}
```

#### `404 Not Found` - Task not found

The requested task does not exist.

```json
{
  "message": "Task `1` not found.",
  "code": "task_not_found",
  "type": "invalid_request",
  "link": "https://docs.meilisearch.com/errors#task-not-found"
}
```

## Cancel tasks

<RouteHighlighter method="POST" path="/tasks/cancel"/>

Cancel any number of enqueued or processing tasks based on their `uid`, `status`, `type`, or `indexUid`.

Task cancellation is an atomic transaction: **either all tasks are successfully canceled or none are**.

To cancel tasks, use [query parameters](#query-parameters-1). Canceling tasks is always an [asynchronous operation](/learn/async/asynchronous_operations).

<Capsule intent="warning">
If a task is already being processed when the cancel request is received, Meilisearch will attempt to stop it. The task will then be marked as `canceled`, but depending on how far it had progressed, its changes may still be applied.
</Capsule>

### Query parameters

| Query parameter | Description                                                                                    | Default value                 |
| --------------- | ---------------------------------------------------------------------------------------------- | ----------------------------- |
| **`uids`**      | Cancel tasks by their `uid`. Separate multiple task UIDs with a comma (`,`)                    | All tasks                     |
| **`statuses`**  | Cancel tasks by their status. Separate multiple task statuses with a comma (`,`)               | All statuses                  |
| **`types`**     | Cancel tasks by their type. Separate multiple task types with a comma (`,`)                    | All types                     |
| **`indexUids`** | Cancel tasks by their index name. Separate multiple index names with a comma (`,`)             | All indexes                   |
| **`beforeEnqueuedAt`** | Cancel tasks enqueued before the given date                                       | All tasks |
| **`afterEnqueuedAt`** | Cancel tasks enqueued after the given date                                         | All tasks |
| **`beforeStartedAt`** | Cancel tasks started before the given date                                          | All tasks |
| **`afterStartedAt`** | Cancel tasks started after the given date                                           | All tasks |

<Capsule intent="danger">
If you do not use any query parameters, Meilisearch will cancel all tasks no matter their status or type.
</Capsule>

### Response

Canceling tasks returns a summarized [task object](/reference/api/tasks#summarized-task-objects) with `taskCancelation` type. You can use this `uid` to [track the status of your request](/learn/async/asynchronous_operations#task-status).

#### `200 Ok` - Cancelation request received

```json
{
  "taskUid": 3,
  "indexUid": null,
  "status": "enqueued",
  "type": "taskCancelation",
  "enqueuedAt": "2021-08-12T10:00:00.000000Z"
}
```

## Delete tasks

<RouteHighlighter method="DELETE" path="/tasks"/>

Delete a finished (`succeeded`, `failed`, or `canceled`) task based on `uid`, `status`, `type`, or `indexUid`.

Task deletion is an atomic transaction: **either all tasks are successfully deleted or none are**.

To delete a task, use [query parameters](#query-parameters-2). Deleting tasks is always an [asynchronous operation](/learn/async/asynchronous_operations).

<Capsule intent="warning">
You can only delete finished tasks. Deleting an `enqueued` or `processing` task will result in an [`invalid_task_uids`](/reference/errors/error_codes#invalid-task-uids) error.
</Capsule>

### Query parameters

| Query parameter | Description                                                                                    | Default value                 |
| --------------- | ---------------------------------------------------------------------------------------------- | ----------------------------- |
| **`uids`**      | Delete tasks by their `uid`. Separate multiple task UIDs with a comma (`,`)                    | All tasks                     |
| **`statuses`**  | Delete tasks by their status. Separate multiple task statuses with a comma (`,`)               | All statuses                  |
| **`types`**     | Delete tasks by their type. Separate multiple task types with a comma (`,`)                    | All types                     |
| **`indexUids`** | Delete tasks by their index name. Separate multiple index names with a comma (`,`)             | All indexes                   |
| **`canceledBy`**| Delete tasks by the `uid` of the task that canceled them. Separate multiple task UIDs with a comma (`,`) | All tasks |
| **`beforeEnqueuedAt`** | Delete tasks enqueued before the given date                                       | All tasks |
| **`afterEnqueuedAt`** | Delete tasks enqueued after the given date                                         | All tasks |
| **`beforeStartedAt`** | Delete tasks started before the given date                                          | All tasks |
| **`afterStartedAt`** | Delete tasks started after the given date                                           | All tasks |
| **`beforeFinishedAt`** | Delete tasks finished before the given date                                        | All tasks |
| **`afterFinishedAt`** | Delete tasks finished after the given date                                          | All tasks |

<Capsule intent="danger">
If you do not use any query parameters, Meilisearch will delete all tasks no matter their status or type.
</Capsule>

### Response

Deleting tasks returns a summarized [task object](/reference/api/tasks#summarized-task-objects) with `taskDeletion` type. You can use this `uid` to [track the status of your request](/learn/async/asynchronous_operations#task-status).

#### `200 Ok` - Deletion request received

```json
{
  "taskUid": 3,
  "indexUid": null,
  "status": "enqueued",
  "type": "taskDeletion",
  "enqueuedAt": "2021-08-12T10:00:00.000000Z"
}
```

## Task object

A task object has the following fields:

| Field              | Type    | Description                                                                                                                     |
| ------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **`uid`**          | Integer | Unique sequential identifier                                                                                                    |
| **`indexUid`**     | String  | Unique index identifier. This is `null` for tasks that do not operate on an index, such as `taskDeletion` and `dumpCreation`  |
| **`status`**       | String  | Status of the task. Possible values are `enqueued`, `processing`, `succeeded`, `failed`, and `canceled`                        |
| **`type`**         | String  | Type of operation performed by the task. [Possible values](/learn/async/asynchronous_operations#task-types) vary with Meilisearch version |
| **`canceledBy`**   | Integer | UID of the task that canceled this task. This is `null` if the task was not canceled                                          |
| **`details`**      | Object  | Detailed information on the task payload. This object's contents depend on the task's `type`                                   |
| **`error`**        | Object  | If the task has the `failed` status, this object contains information about the error. Otherwise, set to `null`                |
| **`duration`**     | String  | Total elapsed time the task spent in the `processing` state, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format |
| **`enqueuedAt`**   | String  | Date and time when the task was first enqueued, in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format                    |
| **`startedAt`**    | String  | Date and time when the task began processing, in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format                      |
| **`finishedAt`**   | String  | Date and time when the task finished processing, in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format                   |

Depending on the task's status, some fields may be set to `null`.

### Summarized task objects

Some operations, such as [document addition](/reference/api/documents#add-or-replace-documents) and [settings updates](/reference/api/settings), return a summarized version of a task object containing only the following fields: `taskUid`, `indexUid`, `status`, `type`, and `enqueuedAt`.

Use the value of the `taskUid` field to get the full task object with the [get task endpoint](/reference/api/tasks#get-one-task).

## Common errors

### Task not found

If a task does not exist (e.g., it was deleted), the API returns a `task_not_found` error:

```json
{
  "message": "Task `1` not found.",
  "code": "task_not_found",
  "type": "invalid_request",
  "link": "https://docs.meilisearch.com/errors#task-not-found"
}
```

### Invalid task uids

If you attempt to cancel or delete a task with a status of `enqueued` or `processing`, the API returns an `invalid_task_uids` error:

```json
{
  "message": "Task `0` is not finished and cannot be deleted. Only succeeded, failed, or canceled tasks can be deleted.",
  "code": "invalid_task_uids",
  "type": "invalid_request",
  "link": "https://docs.meilisearch.com/errors#invalid-task-uids"
}
```