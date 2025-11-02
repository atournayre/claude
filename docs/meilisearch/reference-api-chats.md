# Chats API Reference

**Source:** https://www.meilisearch.com/docs/reference/api/chats.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Chat Completions

---

# Chats

> Use the chat completion API to create conversational search experiences using LLM technology

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/chats` route enables AI-powered conversational search by integrating Large Language Models (LLMs) with your Meilisearch data.

<Note>
  This is an experimental feature. Use the Meilisearch Cloud UI or the experimental features endpoint to activate it:

  ```sh
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "chatCompletions": true
    }'
  ```
</Note>

## Authorization

When working with a secure Meilisearch instance, Use an API key with access to both the `search` and `chatCompletions` actions, such as the default chat API key.

Chat queries only search indexes its API key can access. The default chat API key has access to all indexes. To limit chat access to specific indexes, you must either create a new key, or [generate a tenant token](/learn/security/generate_tenant_token_sdk) from the default chat API key.

## Chat workspace object

```json
{
  "uid": "WORKSPACE_NAME"
}
```

| Name      | Type   | Description                                          |
| :-------- | :----- | :--------------------------------------------------- |
| **`uid`** | String | Unique identifier for the chat completions workspace |

## List chat workspaces

<RouteHighlighter method="GET" path="/chats" />

List all chat workspaces. Results can be paginated by using the `offset` and `limit` query parameters.

### Query parameters

| Query parameter | Description                    | Default value |
| :-------------- | :----------------------------- | :------------ |
| **`offset`**    | Number of results to skip      | `0`           |
| **`limit`**     | Maximum number of results      | `20`          |

### Response

| Name           | Type               | Description                                |
| :------------- | :----------------- | :----------------------------------------- |
| **`results`**  | Array of [objects] | List of returned chat workspaces           |
| **`offset`**   | Integer            | Number of results skipped                  |
| **`limit`**    | Integer            | Number of results returned                 |
| **`total`**    | Integer            | Total number of chat workspaces            |

### Example

```sh
curl \
  -X GET 'http://localhost:7700/chats'
```

```json
{
  "results": [
    {
      "uid": "workspace_1"
    },
    {
      "uid": "workspace_2"
    }
  ],
  "offset": 0,
  "limit": 20,
  "total": 2
}
```

## Get chat workspace

<RouteHighlighter method="GET" path="/chats/:workspace_uid" />

Get information about a specific chat workspace.

### Path parameters

| Name               | Type   | Description                                 |
| :----------------- | :----- | :------------------------------------------ |
| **`workspace_uid`** | String | Unique identifier of the chat workspace     |

### Response

Returns a [chat workspace object](#chat-workspace-object).

### Example

```sh
curl \
  -X GET 'http://localhost:7700/chats/workspace_1'
```

```json
{
  "uid": "workspace_1"
}
```

## Create chat workspace

<RouteHighlighter method="POST" path="/chats" />

Create a new chat workspace.

### Body

| Name      | Type   | Required | Description                                 |
| :-------- | :----- | :------- | :------------------------------------------ |
| **`uid`** | String | Required | Unique identifier for the chat workspace    |

### Response

Returns a [chat workspace object](#chat-workspace-object).

### Example

```sh
curl \
  -X POST 'http://localhost:7700/chats' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "uid": "my_workspace"
  }'
```

```json
{
  "uid": "my_workspace"
}
```

## Delete chat workspace

<RouteHighlighter method="DELETE" path="/chats/:workspace_uid" />

Delete a chat workspace.

### Path parameters

| Name               | Type   | Description                                 |
| :----------------- | :----- | :------------------------------------------ |
| **`workspace_uid`** | String | Unique identifier of the chat workspace     |

### Response

Returns HTTP 204 No Content on success.

### Example

```sh
curl \
  -X DELETE 'http://localhost:7700/chats/my_workspace'
```

## Chat completion

<RouteHighlighter method="POST" path="/chats/:workspace_uid/completions" />

Send a chat message and receive an AI-generated response based on your Meilisearch data.

### Path parameters

| Name               | Type   | Description                                 |
| :----------------- | :----- | :------------------------------------------ |
| **`workspace_uid`** | String | Unique identifier of the chat workspace     |

### Body

| Name                        | Type    | Required | Description                                                  |
| :-------------------------- | :------ | :------- | :----------------------------------------------------------- |
| **`messages`**              | Array   | Required | Array of message objects with `role` and `content`           |
| **`indexes`**               | Array   | Optional | Array of index UIDs to search. Searches all indexes if empty |
| **`model`**                 | String  | Optional | LLM model to use                                             |
| **`temperature`**           | Float   | Optional | Sampling temperature between 0 and 2                         |
| **`maxTokens`**             | Integer | Optional | Maximum number of tokens to generate                         |
| **`stream`**                | Boolean | Optional | Enable streaming responses                                   |

### Response

Returns a completion object with the AI-generated response.

### Example

```sh
curl \
  -X POST 'http://localhost:7700/chats/my_workspace/completions' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "messages": [
      {
        "role": "user",
        "content": "What movies are available?"
      }
    ],
    "indexes": ["movies"]
  }'
```

```json
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "Based on your data, you have several movies available including..."
    },
    "finishReason": "stop"
  }],
  "usage": {
    "promptTokens": 10,
    "completionTokens": 20,
    "totalTokens": 30
  }
}
```
