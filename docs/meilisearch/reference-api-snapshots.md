# Snapshots

**Source:** https://www.meilisearch.com/docs/reference/api/snapshots.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Snapshots

---

# Snapshots

> The /snapshots route creates database snapshots. Use snapshots to backup your Meilisearch data.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/snapshot` route allows you to create database snapshots. Snapshots are `.snapshot` files that can be used to make quick backups of Meilisearch data.

[Learn more about snapshots.](/learn/data_backup/snapshots)

<Warning>
  Meilisearch Cloud does not support the `/snapshots` route.
</Warning>

## Create a snapshot

<RouteHighlighter method="POST" path="/snapshots" />

Triggers a snapshot creation task. Once the process is complete, Meilisearch creates a snapshot in the [snapshot directory](/learn/self_hosted/configure_meilisearch_at_launch#snapshot-destination). If the snapshot directory does not exist yet, it will be created.

Snapshot tasks take priority over other tasks in the queue.

[Learn more about asynchronous operations](/learn/async/asynchronous_operations).

### Example

<CodeGroup>
  ```bash cURL
  curl \
    -X POST 'MEILISEARCH_URL/snapshots'
  ```

  ```javascript JS
  client.createSnapshot()
  ```

  ```python Python
  client.create_snapshot()
  ```

  ```php PHP
  $client->createSnapshot();
  ```

  ```java Java
  client.createSnapshot();
  ```

  ```ruby Ruby
  client.create_snapshot
  ```

  ```go Go
  client.CreateSnapshot()
  ```

  ```csharp C#
  await client.CreateSnapshotAsync();
  ```

  ```rust Rust
  client
    .create_snapshot()
    .await
    .unwrap();
  ```

  ```swift Swift
  let task = try await client.createSnapshot()
  ```
</CodeGroup>

### Response

```json
{
  "taskUid": 1,
  "indexUid": null,
  "status": "enqueued",
  "type": "snapshotCreation",
  "enqueuedAt": "2021-08-12T10:00:00.000000Z"
}
```
