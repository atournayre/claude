# Log customization

**Source:** https://www.meilisearch.com/docs/reference/api/logs.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Log customization

---

# Log customization

> Customize Meilisearch logs with two experimental features: --experimental-logs-mode and --experimental-enable-logs-route.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

<Note>
  This is an experimental feature. Use the experimental features endpoint to activate it:

  ```sh
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json'  \
    --data-binary '{
      "logsRoute": true
    }'
  ```

  This feature is not available for Meilisearch Cloud users.
</Note>

## Customize log levels

<RouteHighlighter method="POST" path="/logs/stderr" />

Customize logging levels for the default logging system.

### Body

| Name            | Type   | Default value | Description                                                |
| :-------------- | :----- | :------------ | :--------------------------------------------------------- |
| **`target`** \* | String | N/A           | A string specifying one or more log type and its log level |

### Example

<CodeGroup>
  ```bash cURL
  curl \
    -X POST MEILISEARCH_URL/logs/stderr \
    -H 'Content-Type: application/json' \
    --data-binary '{
        "target": "milli=trace,index_scheduler=info,actix_web=off"
    }'
  ```
</CodeGroup>

## Start log stream

<RouteHighlighter method="POST" path="/logs/stream" />

Opens a continuous stream of logs for focused debugging sessions. The stream will continue to run indefinitely until you [interrupt](#interrupt-log-stream) it.

### Body

| Name            | Type   | Default value | Description                                                |
| :-------------- | :----- |
