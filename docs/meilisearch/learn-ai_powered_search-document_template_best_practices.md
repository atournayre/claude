# Document template best practices

**Source:** https://www.meilisearch.com/docs/learn/ai_powered_search/document_template_best_practices.md
**Extrait le:** 2025-10-08
**Sujet:** AI-Powered Search - Document Template Best Practices

---

# Document template best practices

> This guide shows you what to do and what to avoid when writing a `documentTemplate`.

When using AI-powered search, Meilisearch generates prompts by filling in your embedder's `documentTemplate` with each document's data. The better your prompt is, the more relevant your search results.

This guide shows you what to do and what to avoid when writing a `documentTemplate`.

## Sample document

Take a look at this document from a database of movies:

```json
{
  "id": 2,
  "title": "Ariel",
  "overview": "Taisto Kasurinen is a Finnish coal miner whose father has just committed suicide and who is framed for a crime he did not commit. In jail, he starts to dream about leaving the country and starting a new life. He escapes from prison but things don't go as planned...",
  "genres": [
    "Drama",
    "Crime",
    "Comedy"
  ],
  "poster": "https://image.tmdb.org/t/p/w500/ojDg0PGvs6R9xYFodRct2kdI6wC.jpg",
  "release_date": 593395200
}
```

## Do not use the default `documentTemplate`

Use a custom `documentTemplate` value in your embedder configuration.

The default `documentTemplate` includes all searchable fields with non-`null` values. In most cases, this adds noise and more information than the embedder needs to provide relevant search results.

## Only include highly relevant information

Take a look at your document and identify the most relevant fields. A good `documentTemplate` for the sample document could be:

```
"A movie called {{doc.title}} about {{doc.overview}}"
```

In the sample document, `poster` and `id` contain data that has little semantic importance and can be safely excluded. The data in `genres` and `release_date` is very useful for filters, but say little about this specific film.

This leaves two relevant fields: `title` and `overview`.

## Keep prompts short

For the best results, keep prompts somewhere between 15 and 45 words:

```
"A movie called {{doc.title}}"
```

This is a short, concise prompt that focuses on the most important information about a movie.