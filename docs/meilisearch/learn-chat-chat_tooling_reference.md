# Chat tooling reference

**Source:** https://www.meilisearch.com/docs/learn/chat/chat_tooling_reference.md
**Extrait le:** 2025-10-08
**Sujet:** Chat / AI Tooling - Chat tooling reference for conversational search

---

# Chat tooling reference

> An exhaustive reference of special chat tools supported by Meilisearch

When creating your conversational search agent, you may be able to extend the model's capabilities with a number of tools. This page lists Meilisearch-specific tools that may improve user experience.

<Note>
  This is an exhaustive feature. Use the Meilisearch Cloud UI or the experimental features endpoint to activate it:

  ```sh
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "chatCompletions": true
    }'
  ```
</Note>

## Meilisearch chat tools

For the best user experience, configure all following tools.

1. **Handle progress updates** by displaying search status to users during streaming
2. **Append conversation messages** as requested to maintain context for future requests
3. **Display source documents** to users for transparency and verification
4. **Use `call_id`** to associate progress updates with their corresponding source results

<Note>
  These special tools are handled internally by Meilisearch and are not forwarded to the LLM provider. They serve as a communication mechanism between Meilisearch and your application to provide enhanced user experience features.
</Note>

### `_meiliSearchProgress`

This tool reports real-time progress of internal search operations. When declared, Meilisearch will call this function whenever search operations are performed in the background.

**Purpose**: Provides transparency about search operations and reduces perceived latency by showing users what's happening behind the scenes.

**Arguments**:

* `call_id`: Unique identifier to track the search operation
* `function_name`: Name of the internal function being executed (e.g., "\_meiliSearchInIndex")
* `function_parameters`: JSON-encoded string containing search parameters like `q` (query) and `index_uid`

**Example Response**:

```json
{
  "function": {
    "name": "_meiliSearchProgress",
    "arguments": "{\"call_id\":\"89939d1f-6857-477c-8ae2-838c7a504"
  }
}
```
