# Health

**Source:** https://www.meilisearch.com/docs/reference/api/health.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Health endpoint

---

> The /health route allows you to verify the status and availability of a Meilisearch instance.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/health` route allows you to verify the status and availability of a Meilisearch instance.

## Get health

<RouteHighlighter method="GET" path="/health" />

Get health of Meilisearch server.

### Example

<CodeGroup>
  ```bash cURL
  curl \
    -X GET 'MEILISEARCH_URL/health'
  ```

  ```javascript JS
  client.health()
  ```

  ```python Python
  client.health()
  ```

  ```php PHP
  $client->health();
  ```

  ```java Java
  client.health();
  ```

  ```ruby Ruby
  client.health
  ```

  ```go Go
  client.Health()
  ```

  ```csharp C#
  await client.HealthAsync();
  ```

  ```rust Rust
  // health() return an Err() if the server is not healthy, so this example would panic due to the unwrap
  client
    .health()
    .await
    .unwrap();
  ```

  ```swift Swift
  client.health { (result) in
      switch result {
      case .success:
          print("Healthy!")
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart
  await client.health();
  ```
</CodeGroup>

#### Response: `200 OK`

```json
{ "status": "available" }
```
