# Bind search analytics events to a user

**Source:** https://www.meilisearch.com/docs/learn/analytics/bind_events_user.md
**Extrait le:** 2025-10-08
**Sujet:** Analytics - Binding Events to Users

---

# Bind search analytics events to a user

> This guide shows you how to manually differentiate users across search analytics using the X-MS-USER-ID HTTP header.

By default, Meilisearch uses IP addresses to identify users and calculate the total user metrics. This guide shows you how to use the `X-MS-USER-ID` HTTP header to manually link analytics events to specific users.

This is useful if you're searching from your back end, as all searches would otherwise appear to come from your server's IP address, making it difficult to accurately track the number of individual users.

## Requirements

* A Meilisearch Cloud project with analytics and monitoring enabled
* A working pipeline for submitting analytics events

## Add `X-MS-USER-ID` to your search query

Include the `X-MS-USER-ID` header in your search requests:

<CodeGroup>
  ```bash cURL
  curl \
    -X POST 'MEILISEARCH_URL/indexes/INDEX_NAME/search' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer DEFAULT_SEARCH_API_KEY' \
    -H 'X-MS-USER-ID: MEILISEARCH_USER_ID' \
    --data-binary '{}'
  ```
</CodeGroup>

Replace `MEILISEARCH_USER_ID` with any value that uniquely identifies that user. This may be an authenticated user's ID when running searches from your own back end, or a hash of the user's IP address.

## Add `X-MS-USER-ID` to the analytics event

Next, submit your analytics event to the analytics endpoint. Send the same header and value in your API call:

<CodeGroup>
  ```bash cURL
  curl \
    -X POST 'https://edge.meilisearch.com/events' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer DEFAULT_SEARCH_API_KEY' \
    -H 'X-MS-USER-ID: MEILISEARCH_USER_ID' \
    --data-binary '{
      "eventType": "click",
      "eventName": "Search Result Clicked",
      "indexUid": "INDEX_NAME",
      "objectID": "DOCUMENT_ID",
      "position": 1,
      "queryID": "QUERY_ID"
    }'
  ```
</CodeGroup>

Replace `MEILISEARCH_USER_ID` with the same value you used in your search query.

## Conclusion

You have successfully bound analytics events to specific users. Meilisearch will now use the `X-MS-USER-ID` value to identify individual users instead of relying solely on IP addresses.
