# Managing the task database

**Source:** https://www.meilisearch.com/docs/learn/async/paginating_tasks.md
**Extrait le:** 2025-10-08
**Sujet:** Async Operations - Paginating Tasks

---

# Managing the task database

> Meilisearch uses a task queue to handle asynchronous operations. This document describes how to navigate long task queues with filters and pagination.

By default, Meilisearch returns a list of 20 tasks for each request when you query the [get tasks endpoint](/reference/api/tasks#get-tasks). This guide shows you how to navigate the task list using query parameters.

<Tip>
  Paginating batches with [the `/batches` route](/reference/api/batches) follows the same rules as paginating tasks.
</Tip>

## Configuring the number of returned tasks

Use the `limit` parameter to change the number of returned tasks:

<CodeGroup>
  ```bash cURL
  curl \
    -X GET 'MEILISEARCH_URL/tasks?limit=2&from=10
  ```

  ```javascript JS
  client.tasks.getTasks({ limit: 2, from: 10 })
  ```

  ```python Python
  client.get_tasks({
    'limit': 2,
    'from': 10
  })
  ```

  ```php PHP
  $taskQuery = (new TasksQuery())->setLimit(2)->setFrom(10));
  $client->getTasks($taskQuery);
  ```

  ```java Java
  TasksQuery query = new TasksQuery()
        .setLimit(2)
        .setFrom(10);

  client.index("movies").getTasks(query);
  ```

  ```ruby Ruby
  client.tasks(limit: 2, from: 10)
  ```

  ```go Go
  client.GetTasks(&meilisearch.TasksQuery{
    Limit: 2,
    From: 10,
  });
  ```

  ```csharp C#
  ResourceResults<TaskInfo> taskResult = await client.GetTasksAsync(new TasksQuery { Limit = 2, From = 10 });
  ```

  ```rust Rust
  let mut query = TasksSearchQuery::new(&client)
      .with_limit(2)
      .with_from(10)
      .execute()
  ```
</CodeGroup>
