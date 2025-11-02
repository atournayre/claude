# Facet search

**Source:** https://www.meilisearch.com/docs/reference/api/facet_search.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Facet Search

---

# Facet search

> The /facet-search route allows you to search for facet values.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/facet-search` route allows you to search for facet values. Facet search supports [prefix search](/learn/engine/prefix) and [typo tolerance](/learn/relevancy/typo_tolerance_settings). The returned hits are sorted lexicographically in ascending order.

<Note>
  Meilisearch does not support facet search on numbers. Convert numeric facets to strings to make them searchable.

  Internally, Meilisearch represents numbers as [`float64`](https://en.wikipedia.org/wiki/Double-precision_floating-point_format). This means they lack precision and can be represented in different ways, making it difficult to search facet values effectively.
</Note>

## Perform a facet search

Search for a facet value within a given facet.

<RouteHighlighter method="POST" path="/indexes/{index_uid}/facet-search" />

<Warning>
  This endpoint will not work without first explicitly adding attributes to the [`filterableAttributes`](/reference/api/settings#update-filterable-attributes) list. [Learn more about facets in our dedicated guide.](/learn/filtering_and_sorting/search_with_facet_filters)
</Warning>

<Warning>
  Meilisearch's facet search does not support multi-word facets and only considers the first term in the`facetQuery`.

  For example, searching for `Jane` will return `Jane Austen`, but searching for `Austen` will not return `Jane Austen`.
</Warning>

### Body

| Name                                                                                                  | Type                                                                 | Default value | Description                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ----------
