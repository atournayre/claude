# API Reference - Overview

**Source:** https://www.meilisearch.com/docs/reference/api/overview.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Overview

---

# Overview

> Consult this page for an overview of how to query Meilisearch's API, which types of parameters it supports, and how it structures its responses.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

This reference describes the general behavior of Meilisearch's RESTful API.

If you are new to Meilisearch, check out the [getting started](/learn/self_hosted/getting_started_with_self_hosted_meilisearch).

## OpenAPI

Meilisearch OpenAPI specifications (`meilisearch-openapi.json`) are attached to the [latest release of Meilisearch](https://github.com/meilisearch/meilisearch/releases/tag/latest)

## Document conventions

This API documentation uses the following conventions:

* Curly braces (`{}`) in API routes represent path parameters, for example, GET `/indexes/{index_uid}`
* Required fields are marked by an asterisk (`*`)
* Placeholder text is in uppercase characters with underscore delimiters, for example, `MASTER_KEY`

## Authorization

By [providing Meilisearch with a master key at launch](/learn/security/basic_security), you protect your instance from unauthorized requests. The provided master key must be at least 16 bytes. From then on, you must include the `Authorization` header along with a valid API key to access protected routes (all routes except [`/health`](/reference/api/health).

<CodeGroup>
  ```bash cURL
  # replace the MASTER_KEY placeholder with your master key
  curl \
    -X GET 'MEILISEARCH_URL/keys' \
    -H 'Authorization: Bearer MASTER_KEY'
  ```

  ```javascript JS
  const client = new MeiliSearch({ host: 'http://localhost:7700', apiKey: 'masterKey' })
  client
  ```
</CodeGroup>
