# Errors

**Source:** https://www.meilisearch.com/docs/reference/errors/overview.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Error Handling

---

# Errors

> Consult this page for an overview of how Meilisearch reports and formats error objects.

Meilisearch uses the following standard HTTP codes for a successful or failed API request:

| Status code | Description                                                                               |
| :---------- | :---------------------------------------------------------------------------------------- |
| 200         | ✅ **Ok** Everything worked as expected.                                                   |
| 201         | ✅ **Created** The resource has been created (synchronous)                                 |
| 202         | ✅  **Accepted** The task has been added to the queue (asynchronous)                       |
| 204         | ✅ **No Content** The resource has been deleted or no content has been returned            |
| 205         | ✅ **Reset Content** All the resources have been deleted                                   |
| 400         | ❌ **Bad Request** The request was unacceptable, often due to missing a required parameter |
| 401         | ❌ **Unauthorized** No valid API key provided                                              |
| 403         | ❌ **Forbidden** The API key doesn't have the permissions to perform the request           |
| 404         | ❌ **Not Found** The requested resource doesn't exist                                      |

## Errors

All detailed task responses contain an [`error`](/reference/api/tasks#error) field. When a task fails, it is always accompanied by a JSON-formatted error response. Meilisearch errors can be of one of the following types:

| Type                  | Description                                                                                                                                                                                     |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`invalid_request`** | This is due to an error in the user input. It is accompanied by the HTTP code `4xx`                                                                                                             |
| **`internal`**        | This is due to machine or configuration constraints. It is accompanied by the HTTP code `5xx`                                                                                                   |
| **`auth`**            | This type of error is related to authentication and authorization. It is accompanied by the HTTP code `4xx`                                                                                     |
