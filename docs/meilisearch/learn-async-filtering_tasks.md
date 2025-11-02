# Filtering tasks

**Source:** https://www.meilisearch.com/docs/learn/async/filtering_tasks.md
**Extrait le:** 2025-10-08
**Sujet:** Async Operations - Task Filtering

---

# Filtering tasks

> This guide shows you how to use query parameters to filter tasks and obtain a more readable list of asynchronous operations.

Querying the [get tasks endpoint](/reference/api/tasks#get-tasks) returns all tasks that have not been deleted. This unfiltered list may be difficult to parse in large projects.

This guide shows you how to use query parameters to filter tasks and obtain a more readable list of asynchronous operations.

<Tip>
  Filtering batches with [the `/batches` route](/reference/api/batches) follows the same rules as filtering tasks. Keep in mind that many `/batches` parameters such as `uids` target the tasks included in batches, instead of the batches themselves.
</Tip>

## Requirements

* a command-line terminal
* a running Meilisearch project

## Filtering tasks with a single parameter

Use the get tasks endpoint to fetch all `canceled` tasks:

<CodeGroup>
  ```bash cURL
  curl \
    -X GET 'MEILISEARCH_URL/tasks?statuses=failed'
  ```

  ```javascript JS
  client.tasks.getTasks({ statuses: ['failed', 'canceled'] })
  ```

  ```python Python
  client.get_tasks({'statuses': ['failed', 'canceled']})
  ```

  ```php PHP
  $client->getTasks((new TasksQuery())->setStatuses(['failed', 'canceled']));
  ```

  ```java Java
  TasksQuery query = new TasksQuery().setStatuses(new String[] {"failed", "canceled"});
  client.getTasks(query);
  ```

  ```ruby Ruby
  client.get_tasks(statuses: ['failed', 'canceled'])
  ```

  ```go Go
  client.GetTasks(&meilisearch.TasksQuery{
    Statuses: []meilisearch.TaskStatus{
      meilisearch.TaskStatusFailed,
      meilisearch.TaskStatusCanceled,
    },
  })
  ```

  ```csharp C#
  await client.GetTasksAsync(new TasksQuery { Statuses = new List<TaskInfoStatus> { TaskInfoStatus.Failed, TaskInfoStatus.Canceled } });
  ```
</CodeGroup>

---

**Note:** Le contenu complet de cette page peut être plus long. Consulte la source originale si nécessaire.
