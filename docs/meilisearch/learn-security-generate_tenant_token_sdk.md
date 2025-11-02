# Multitenancy and tenant tokens

**Source:** https://www.meilisearch.com/docs/learn/security/generate_tenant_token_sdk.md
**Extrait le:** 2025-10-08
**Sujet:** Security - Generating Tenant Tokens with SDK

---

# Multitenancy and tenant tokens

> This guide shows you the main steps when creating tenant tokens using Meilisearch's official SDKs.

There are two steps to use tenant tokens with an official SDK: generating the tenant token, and making a search request using that token.

## Requirements

* a working Meilisearch project
* an application supporting authenticated users
* one of Meilisearch's official SDKs installed

## Generate a tenant token with an official SDK

First, import the SDK. Then create a set of [search rules](/learn/security/tenant_token_reference#search-rules):

```json
{
  "patient_medical_records": {
    "filter": "user_id = 1"
  }
}
```

Search rules must be an object where each key corresponds to an index in your instance. You may configure any number of filters for each index.

Next, find your default search API key. Query the [get an API key endpoint](/reference/api/keys#get-one-key) and inspect the `uid`  field to obtain your API key's UID:

```sh
curl \
  -X GET 'MEILISEARCH_URL/keys/API_KEY' \
  -H 'Authorization: Bearer MASTER_KEY'
```

For maximum security, you should also define an expiry date for tenant tokens.

Finally, send this data to your chosen SDK's tenant token generator:

<CodeGroup>
  ```javascript JS
  import { generateTenantToken } from 'meilisearch/token'

  const searchRules = {
    patient_medical_records: {
      filter: 'user_id = 1'
    }
  }
  const apiKey = 'B5KdX2MY2jV6EXfUs6scSfmC...'
  const apiKeyUid = '85c3c2f9-bdd6-41f1-abd8-11fcf80e0f76'
  const expiresAt = new Date('2025-12-20') // optional

  const token = await generateTenantToken({ apiKey, apiKeyUid, searchRules, expiresAt })
  ```
