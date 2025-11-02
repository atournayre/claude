# Getting started with conversational search

**Source:** https://www.meilisearch.com/docs/learn/chat/getting_started_with_chat.md
**Extrait le:** 2025-10-08
**Sujet:** Chat - Getting Started with Conversational Search

---

# Getting started with conversational search

> Learn how to implement AI-powered conversational search in your application

This guide walks you through implementing Meilisearch's chat completions feature to create conversational search experiences in your application.

## Prerequisites

Before starting, ensure you have:

* A [secure](/learn/security/basic_security) Meilisearch >= v1.15.1 project
* An API key from an LLM provider
* At least one index with searchable content

## Enable the chat completions feature

First, enable the chat completions experimental feature:

```bash
curl \
  -X PATCH 'http://localhost:7700/experimental-features/' \
  -H 'Authorization: Bearer MEILISEARCH_KEY' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "chatCompletions": true
  }'
```

## Find your chat API key

When Meilisearch runs with a master key on an instance created after v1.15.1, it automatically generates a "Default Chat API Key" with `chatCompletions` and `search` permissions on all indexes. Check if you have the key using:

```bash
curl http://localhost:7700/keys \
  -H "Authorization: Bearer MEILISEARCH_KEY"
```

Look for the key with the description "Default Chat API Key" Use this key when querying the `/chats` endpoint.

### Troubleshooting: Missing default chat API key

If your instance does not have a Default Chat API Key, create one manually:

```bash
curl \
  -X POST 'http://localhost:7700/keys' \
  -H 'Authorization: Bearer MEILISEARCH_KEY' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "name": "Chat API Key",
    "description": "API key for chat completions",
    "actions": ["search", "chatCompletions"],
    "indexes": ["*"],
    "expiresAt": null
  }'
```

## Configure your indexes for chat

Each index that you want to be searchable through chat needs specific configuration:

```bash
curl \
  -X PATCH 'http://localhost:7700/indexes/INDEX_NAME/settings' \
  -H 'Authorization: Bearer MEILISEARCH_KEY' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "chat": {
      "enabled": true,
      "llmProvider": {
        "provider": "openai",
        "model": "gpt-4o-mini"
      },
      "maxResponseLength": 2000,
      "prompt": {
        "systemPrompt": "You are a helpful assistant.",
        "messageTemplate": "Answer the user's question based on the following context:\n\n{{#each context}}\n{{this}}\n{{/each}}\n\nQuestion: {{query}}\n\nAnswer:"
      }
    }
  }'
```

Configure chat settings for each index:

* `enabled`: Enable chat for this index
* `llmProvider`: Configure your LLM (OpenAI, Anthropic, etc.)
* `maxResponseLength`: Maximum response length in characters
* `prompt`: Customize system and message templates

## Set up your LLM API key

Configure your LLM provider's API key using environment variables. For example, with OpenAI:

```bash
export MEILI_OPENAI_API_KEY=your-openai-api-key
```

Restart Meilisearch for the changes to take effect.

### Supported LLM providers

Meilisearch supports multiple LLM providers:

* OpenAI (`openai`)
* Anthropic (`anthropic`)
* Mistral AI (`mistral`)
* Custom endpoints (`custom`)

## Make your first chat request

Now you can start making chat requests:

```bash
curl \
  -X POST 'http://localhost:7700/chats' \
  -H 'Authorization: Bearer CHAT_API_KEY' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "index": "movies",
    "query": "What are some good sci-fi movies?",
    "stream": false
  }'
```

Response:

```json
{
  "answer": "Based on the available movies, here are some excellent sci-fi options:\n\n1. Blade Runner 2049 - A visually stunning sequel exploring themes of consciousness and humanity\n2. The Matrix - A groundbreaking film about reality and technology\n3. Interstellar - An epic space exploration movie dealing with time and relativity\n\nAll of these offer unique perspectives on science fiction themes.",
  "sources": [
    {
      "id": "123",
      "title": "Blade Runner 2049",
      "overview": "Officer K uncovers a secret..."
    }
  ]
}
```

## Enable streaming responses

For a better user experience, enable streaming to get responses as they're generated:

```javascript
const response = await fetch('http://localhost:7700/chats', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer CHAT_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    index: 'movies',
    query: 'What are some good sci-fi movies?',
    stream: true
  })
});

const reader = response.body.getReader();
const decoder = new TextDecoder();

while (true) {
  const { done, value } = await reader.read();
  if (done) break;

  const chunk = decoder.decode(value);
  const lines = chunk.split('\n');

  for (const line of lines) {
    if (line.startsWith('data: ')) {
      const data = JSON.parse(line.slice(6));
      process(data); // Handle each chunk
    }
  }
}
```

## Next steps

You've now set up basic conversational search. To enhance your implementation:

* [Customize chat prompts](/learn/chat/customizing_chat_prompts) for your use case
* [Implement conversation history](/learn/chat/conversation_history) for multi-turn chats
* [Optimize search relevance](/learn/relevancy/relevancy) for better context retrieval
* [Monitor chat usage](/learn/monitoring/monitoring_meilisearch) and performance

## Learn more

* [Chat API reference](/reference/api/chat)
* [Chat settings reference](/reference/api/settings#chat)
* [Security best practices](/learn/security/basic_security)
