# Version API Endpoint

**Source:** https://www.meilisearch.com/docs/reference/api/version.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Version endpoint

---

# Version

> The /version route allows you to check the version of a running Meilisearch instance.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/version` route allows you to check the version of a running Meilisearch instance.

## Version object

| Name             | Description                                            |
| :--------------- | :----------------------------------------------------- |
| **`commitSha`**  | Commit identifier that tagged the `pkgVersion` release |
| **`commitDate`** | Date when the `commitSha` was created                  |
| **`pkgVersion`** | Meilisearch version                                    |

## Get version of Meilisearch

<RouteHighlighter method="GET" path="/version" />

Get version of Meilisearch.

### Example

<CodeGroup>
  ```bash cURL
  curl \
    -X GET 'MEILISEARCH_URL/version'
  ```

  ```javascript JS
  client.getVersion()
  ```

  ```python Python
  client.get_version()
  ```

  ```php PHP
  $client->version();
  ```

  ```java Java
  client.getVersion();
  ```

  ```ruby Ruby
  client.version
  ```

  ```go Go
  client.GetVersion()
  ```

  ```csharp C#
  await client.GetVersionAsync();
  ```

  ```rust Rust
  let version: Version = client
    .get_version()
    .await
    .unwrap();
  ```

  ```swift Swift
  client.version { (result) in
      switch result {
      case .success(let version):
          print(version)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart
  await client.getVersion();
  ```
</CodeGroup>

### Response

```json
{
  "commitSha": "b46889b5f0f2f8b91438a08a358ba8f05fc09fc1",
  "commitDate": "2019-11-15T09:51:54.278247+00:00",
  "pkgVersion": "0.1.1"
}
```
