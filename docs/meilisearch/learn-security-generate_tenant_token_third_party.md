# Generate tenant tokens without a Meilisearch SDK

**Source:** https://www.meilisearch.com/docs/learn/security/generate_tenant_token_third_party.md
**Extrait le:** 2025-10-08
**Sujet:** Security - Generating Tenant Tokens with Third-Party Libraries

---

> This guide shows you the main steps when creating tenant tokens without using Meilisearch's official SDKs.

This guide shows you the main steps when creating tenant tokens using [`node-jsonwebtoken`](https://www.npmjs.com/package/jsonwebtoken), a third-party library.

## Requirements

* a working Meilisearch project
* a JavaScript application supporting authenticated users
* `jsonwebtoken` v9.0

## Generate a tenant token with `jsonwebtoken`

### Build the tenant token payload

First, create a set of search rules:

```json
{
  "INDEX_NAME": {
    "filter": "ATTRIBUTE = VALUE"
  }
}
```

Next, find your default search API key. Query the [get an API key endpoint](/reference/api/keys#get-one-key) and inspect the `uid`  field to obtain your API key's UID:

```sh
curl \
  -X GET 'MEILISEARCH_URL/keys/API_KEY' \
  -H 'Authorization: Bearer MASTER_KEY'
```

For maximum security, you should also set an expiry date for your tenant tokens. The following example configures the token to expire 20 minutes after its creation:

```js
parseInt(Date.now() / 1000) + 20 * 60
```

### Create tenant token

First, include `jsonwebtoken` in your application. Next, assemble the token payload and pass it to `jsonwebtoken`'s `sign` method:

```js
const jwt = require('jsonwebtoken');

const apiKey = 'API_KEY';
const apiKeyUid = 'API_KEY_UID';
const currentUserID = 'USER_ID';
const expiryDate = parseInt(Date.now() / 1000) + 20 * 60; // 20 minutes

const tokenPayload = {
  searchRules: {
    'INDEX_NAME': {
      'filter': `user_id = ${currentUserID}`
     }
  },
  apiKeyUid: apiKeyUid,
  exp: expiryDate
};

const token = jwt.sign(tokenPayload, apiKey, { algorithm: 'HS256' });
```
