# Conversational search

**Source:** https://www.meilisearch.com/docs/learn/chat/conversational_search.md
**Extrait le:** 2025-10-08
**Sujet:** Chat & Conversational Search

---

# Conversational search

> Learn how to implement AI-powered conversational search using Meilisearch's chat feature

Meilisearch's chat completions feature enables AI-powered conversational search, allowing users to ask questions in natural language and receive direct answers based on your indexed content. This feature transforms the traditional search experience into an interactive dialogue.

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

## What is conversational search?

Conversational search interfaces allow users to:

* Ask questions in natural language instead of using keywords
* Receive direct answers rather than just document links
* Maintain context across multiple questions
* Get responses grounded in your actual content

This approach bridges the gap between traditional search and modern AI experiences, making information more accessible and intuitive to find.

## How chat completions differs from traditional search

### Traditional search workflow

1. User enters keywords
2. Meilisearch returns matching documents
3. User reviews results to find answers

### Conversational search workflow

1. User asks a question in natural language
2. Meilisearch retrieves relevant documents
3. AI generates a direct answer based on those documents
4. User can ask follow-up questions

## When to use chat completions vs traditional search

### Use conversational search when:

* Users need direct answers to specific questions
* Content is informational (documentation, knowledge bases, FAQs)
* Users benefit from follow-up questions
* Natural language interaction improves user experience

### Use traditional search when:

* Users need to browse multiple options
* Results require comparison (e-commerce products, listings)
* Exact matching is critical
* Response time is paramount

## Use chat completions to implement RAG pipelines

The chat completions feature implements a complete Retrieval Augmented Generation (RAG) pipeline in a single API endpoint. Meilisearch's chat completions consolidates RAG creation into one streamlined process:
