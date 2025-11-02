# Configuring index settings with the Meilisearch API

**Source:** https://www.meilisearch.com/docs/learn/configuration/configuring_index_settings_api.md
**Extrait le:** 2025-10-08
**Sujet:** Configuration - Index Settings API

---

# Configuring index settings with the Meilisearch API

> This tutorial shows how to check and change an index setting using the Meilisearch API.

This tutorial shows how to check and change an index setting using one of the setting subroutes of the Meilisearch API.

If you are Meilisearch Cloud user, you may also [configure index settings using the Meilisearch Cloud interface](/learn/configuration/configuring_index_settings).

## Requirements

* a new [Meilisearch Cloud](https://cloud.meilisearch.com/projects/) project or a self-hosted Meilisearch instance with at least one index
* a command-line terminal with `curl` installed

## Getting the value of a single index setting

Start by checking the value of the searchable attributes index setting.

Use the `GET` endpoint of the `/settings/searchable-attributes` subroute, replacing `INDEX_NAME` with your index:

<CodeGroup>
  ```bash cURL
  curl \
    -X GET 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/searchable-attributes'
  ```

  ```rust Rust
  let searchable_attributes: Vec<String> = index
    .get_searchable_attributes()
    .await
    .unwrap();
  ```
</CodeGroup>

Depending on your setup, you might also need to replace `localhost:7700` with the appropriate address and port.

You should receive a response immediately:

```json
[
  "*"
]
```

If this is a new index, you should see the default value, \["\*"]. This indicates Meilisearch looks through all document attributes when searching.

## Updating an index setting

All documents include a primary key attribute. In most cases, this attribute does not contain any relevant data, so you can improve your application search experience by explicitly removing it from your searchable attributes list.

Use the `PUT` endpoint of the `/settings/searchable-attributes` subroute, replacing `INDEX_NAME` with your index and the sample attributes `"title"` and `"overview"` with attributes present in your dataset:

<CodeGroup>
  ```bash cURL
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/searchable-attributes' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      "title",
      "overview"
    ]'
  ```

  ```rust Rust
  index
    .set_searchable_attributes(&["title", "overview"])
    .await
    .unwrap();
  ```
</CodeGroup>

You should receive a response similar to this:

```json
{
  "taskUid": 1,
  "indexUid": "INDEX_NAME",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2022-04-14T20:56:44.991039Z"
}
```

This response indicates Meilisearch has accepted your request and enqueued a task to update the setting. Use the `taskUid` to track the task status.

## Checking task status

Use the `GET` endpoint of the `/tasks` route with the `taskUid` from the previous response:

<CodeGroup>
  ```bash cURL
  curl \
    -X GET 'MEILISEARCH_URL/tasks/1'
  ```

  ```rust Rust
  let task = client
    .get_task(1)
    .await
    .unwrap();
  ```
</CodeGroup>

You should receive a response similar to this:

```json
{
  "uid": 1,
  "indexUid": "INDEX_NAME",
  "status": "succeeded",
  "type": "settingsUpdate",
  "canceledBy": null,
  "details": {
    "searchableAttributes": [
      "title",
      "overview"
    ]
  },
  "error": null,
  "duration": "PT0.012345S",
  "enqueuedAt": "2022-04-14T20:56:44.991039Z",
  "startedAt": "2022-04-14T20:56:44.995062Z",
  "finishedAt": "2022-04-14T20:56:45.003407Z"
}
```

Once the task `status` is `succeeded`, Meilisearch has successfully updated your index settings.

## Verifying the update

Use the `GET` endpoint of the `/settings/searchable-attributes` subroute again:

<CodeGroup>
  ```bash cURL
  curl \
    -X GET 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/searchable-attributes'
  ```

  ```rust Rust
  let searchable_attributes: Vec<String> = index
    .get_searchable_attributes()
    .await
    .unwrap();
  ```
</CodeGroup>

You should see the updated value:

```json
[
  "title",
  "overview"
]
```

## Conclusion

You have successfully:

* Retrieved the value of an index setting
* Updated an index setting
* Tracked the update task status
* Verified the setting change

You can use this same workflow to configure any of the [index settings](/reference/api/settings) available in Meilisearch.

## Next steps

* Learn more about [index settings](/learn/configuration/settings)
* Explore the [settings API reference](/reference/api/settings)
* Discover other [configuration options](/learn/configuration/instance_options)
