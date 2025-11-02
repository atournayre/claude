# Dumps API

**Source:** https://www.meilisearch.com/docs/reference/api/dump.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Dumps

---

# Dumps

> The /dumps route allows the creation of database dumps. Use dumps to migrate Meilisearch to a new version.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/dumps` route allows the creation of database dumps. Dumps are `.dump` files that can be used to restore Meilisearch data or migrate between different versions.

<Warning>
  Meilisearch Cloud does not support the `/dumps` route.
</Warning>

[Learn more about dumps](/learn/data_backup/dumps).

## Create a dump

<RouteHighlighter method="POST" path="/dumps" />

Triggers a dump creation task. Once the process is complete, a dump is created in the [dump directory](/learn/self_hosted/configure_meilisearch_at_launch#dump-directory). If the dump directory does not exist yet, it will be created.

Dump tasks take priority over all other tasks in the queue. This means that a newly created dump task will be processed as soon as the current task is finished.

[Learn more about asynchronous operations](/learn/async/asynchronous_operations).

### Example

<CodeGroup>
  ```bash cURL
  curl \
    -X POST 'MEILISEARCH_URL/dumps'
  ```

  ```javascript JS
  client.createDump()
  ```

  ```python Python
  client.create_dump()
  ```

  ```php PHP
  $client->createDump();
  ```

  ```java Java
  client.createDump();
  ```

  ```ruby Ruby
  client.create_dump
  ```

  ```go Go
  resp, err := client.CreateDump()
  ```

  ```csharp C#
  await client.CreateDumpAsync();
  ```

  ```rust Rust
  client
    .create_dump()
    .await
    .
