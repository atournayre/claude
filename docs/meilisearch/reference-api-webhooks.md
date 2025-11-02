# Webhooks

**Source:** https://www.meilisearch.com/docs/reference/api/webhooks.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Webhooks

---

# Webhooks

> Use the /webhooks to trigger automatic workflows when Meilisearch finishes processing tasks.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

Use the `/webhooks` to trigger automatic workflows when Meilisearch finishes processing tasks.

## The webhook object

```json
{
  "uuid": "V4_UUID_GENERATED_BY_MEILISEARCH",
  "url": "WEBHOOK_NOTIFICATION_TARGET_URL",
  "headers": {
    "HEADER": "VALUE",
  },
  "isEditable": false
}
```

* `uuid`: a v4 uuid Meilisearch automatically generates when you create a new webhook
* `url`: a string indication the URL Meilisearch should notify whenever it completes a task, required
* `headers`: an object with HTTP headers and their values, optional, often used for authentication
* `isEditable`: read-only Boolean field indicating whether you can edit the webhook. Meilisearch automatically sets this to `true` for all webhooks created via the API and to `false` for reserved webhooks

## The webhook payload

When Meilisearch finishes processing a task, it sends the relevant [task object](/reference/api/tasks#task-object) to all configured webhooks.

## Get all webhooks

<RouteHighlighter method="GET" path="/webhooks" />

Get a list of all webhooks configured in the current Meilisearch instance.

### Example

<CodeGroup>
  ```bash cURL
  curl \
    -X GET 'MEILISEARCH_URL/webhooks'
  ```

  ```javascript JS
  client.getWebhooks()
  ```

  ```go Go
  client.ListWebhooks();
  ```
</CodeGroup>

#### Response: `200 OK`

```json
{
  "results":
```
