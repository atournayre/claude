# Tenant token payload reference

**Source:** https://www.meilisearch.com/docs/learn/security/tenant_token_reference.md
**Extrait le:** 2025-10-08
**Sujet:** Security - Tenant Token Reference

---

# Tenant token payload reference

> Meilisearch's tenant tokens are JSON web tokens (JWTs). Their payload is made of three elements: search rules, an API key UID, and an optional expiration date.

Meilisearch's tenant tokens are JSON web tokens (JWTs). Their payload is made of three elements: [search rules](#search-rules), an [API key UID](#api-key-uid), and an optional [expiration date](#expiry-date).

## Example payload

```json
{
  "exp": 1646756934,
  "apiKeyUid": "at5cd97d-5a4b-4226-a868-2d0eb6d197ab",
  "searchRules": {
    "INDEX_NAME": {
      "filter": "attribute = value"
    }
  }
}
```

## Search rules

The search rules object are a set of instructions defining search parameters Meilisearch will enforced in every query made with a specific tenant token.

### Search rules object

`searchRules` must be a JSON object. Each key must correspond to one or more indexes:

```json
{
  "searchRules": {
    "*": {},
    "INDEX_*": {},
    "INDEX_NAME_A": {}
  }
}
```

Each search rule object may contain a single `filter` key. This `filter`'s value must be a [filter expression](/learn/filtering_and_sorting/filter_expression_reference):

```json
{
  "*": {
    "filter": "attribute_A = value_X AND attribute_B = value_Y"
  }
}
```

Meilisearch applies the filter to all searches made with that tenant token. A token only has access to the indexes present in the `searchRules` object.

A token may contain rules for any number of indexes. **Specific rulesets take precedence and overwrite `*` rules.**

<Warning>
  Because tenant tokens are generated in your application, Meilisearch cannot check if search rule filters are valid. Invalid search rules return throw errors when searching.

  Consult the search API reference for [more information on Meilisearch filter syntax](/reference/api/search.md#filter).
</Warning>

## API key UID

The `apiKeyUid` field must contain the UID of a valid API key. You can find a key's UID by [fetching a single key](/reference/api/keys.md#get-one-key) or [listing all keys](/reference/api/keys.md#get-all-keys).

Meilisearch will use this API key to determine the tenant token's permissions. **The API key UID should belong to a search key**, otherwise a tenant token will have access to non-search routes.

## Expiry date

Tenant token payloads may include an expiration date with the `exp` field. `exp` must contain a UTC numeric timestamp in seconds indicating the date the token expires.

Meilisearch rejects expired tokens and returns an error.

```json
{
  "exp": 1641835850
}
```
