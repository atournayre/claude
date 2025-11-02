# Metrics

**Source:** https://www.meilisearch.com/docs/reference/api/metrics.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Metrics (Experimental)

---

# Metrics

> The /metrics endpoint is an experimental feature. It exposes data compatible with Prometheus and offers insight into Meilisearch's behavior and performance.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/metrics` route exposes data compatible with [Prometheus](https://prometheus.io/). You will also need to have Grafana installed in your system to make use of this feature.

<Note>
  This is an experimental feature. Use the experimental features endpoint to activate it:

  ```sh
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "metrics": true
    }'
  ```

  This feature is not available for Meilisearch Cloud users.
</Note>

## Exposed information

`/metrics` exposes the following information:

| Name                                     | Description                                                                                                                                                                                                                                                                                                                                                                             | Type      |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `meilisearch_http_requests_total`        | Returns the number of times an API resource is accessed.                                                                                                                                                                                                                                                                                                                                | counter   |
| `meilisearch_http_response_time_seconds` | Returns a time histogram showing the number of times an API resource call goes into a time bucket (expressed in second).                                                                                                                                                                                                                                                                | histogram |
| `meilisearch_db_size_bytes`              | Returns the "real" size of the database on disk in bytes. It includes all the lmdb memory mapped files plus all the files contained in the `data.ms` directory (mainly the updates files that were not