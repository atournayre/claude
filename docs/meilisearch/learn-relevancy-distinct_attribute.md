# Distinct attribute

**Source:** https://www.meilisearch.com/docs/learn/relevancy/distinct_attribute.md
**Extrait le:** 2025-10-08
**Sujet:** Relevancy - Distinct Attribute

---

# Distinct attribute

> Distinct attribute is a field that prevents Meilisearch from returning a set of several similar documents. Often used in ecommerce datasets where many documents are variations of the same item.

The distinct attribute is a special, user-designated field. It is most commonly used to prevent Meilisearch from returning a set of several similar documents, instead forcing it to return only one.

You may set a distinct attribute in two ways: using the `distinctAttribute` index setting during configuration, or the `distinct` search parameter at search time.

## Setting a distinct attribute during configuration

`distinctAttribute` is an index setting that configures a default distinct attribute Meilisearch applies to all searches and facet retrievals in that index.

<Warning>
  There can be only one `distinctAttribute` per index. Trying to set multiple fields as a `distinctAttribute` will return an error.
</Warning>

The value of a field configured as a distinct attribute will always be unique among returned documents. This means **there will never be more than one occurrence of the same value** in the distinct attribute field among the returned documents.

When multiple documents have the same value for the distinct attribute, Meilisearch returns only the highest-ranked result after applying [ranking rules](/learn/relevancy/ranking_rules). If two or more documents are equivalent in terms of ranking, Meilisearch returns the first result according to its `internal_id`.

## Example

Suppose you have an e-commerce dataset. For an index that contains information about jackets, you may have several identical items with minor variations such as color or size.

As shown below, this dataset contains three documents representing different versions of a Lee jeans leather jacket. One of the jackets is brown, one is black, and the last one is blue.

```json
[
  {
    "id": 1,
    "description": "Leather jacket",
    "brand": "Lee jeans",
    "color": "brown",
    "product_id": "123456"
  },
  {
    "id": 2,
    "description": "Leather jacket",
    "brand": "Lee jeans",
    "color": "black",
    "product_id": "123456"
  },
  {
    "id": 3,
    "description": "Leather jacket",
    "brand": "Lee jeans",
    "color": "blue",
    "product_id": "123456"
  }
]
```

If you search `Lee leather jacket` and don't use the distinct attribute, you will get all three documents.

If you set `product_id` as the distinct attribute, Meilisearch will only return the highest-ranked document among the three. This is because all three jackets share the same `product_id`.

### Setting the distinct attribute

Use the [update distinct attribute endpoint](/reference/api/settings#update-distinct-attribute):

<CodeSample
  id="distinct_attribute_guide_1"
  codeExample={distinctAttributeGuide1}
/>

You only have to configure `distinctAttribute` once. After setting it, **all search queries automatically use the distinct attribute**.

## Setting a distinct attribute at search time

`distinct` is a search parameter that accepts a string corresponding to a document field. It instructs Meilisearch to use that field as the distinct attribute only for that specific search.

When using the `distinct` search parameter, Meilisearch ignores the `distinctAttribute` index setting.

### Example

Using the previous e-commerce example, you can use the `distinct` search parameter to ensure Meilisearch only returns one jacket per brand:

<CodeSample
  id="distinct_search_parameter_1"
  codeExample={distinctSearchParameter1}
/>

This query should return only one Lee jeans jacket, even if there are multiple products from that brand in the index.

## Distinct attribute versus faceting

The distinct attribute and [faceting](/learn/filtering_and_sorting/facet_search) are both useful for grouping search results, but they work differently:

- **Distinct attribute**: Returns only one document per distinct value. You cannot control which document is returned beyond ranking rules.
- **Faceting**: Returns all documents grouped by facet values. You have full control over the results through filtering.

Use the distinct attribute when you want to remove duplicates from results. Use faceting when you want to organize results into categories while showing all matching documents.