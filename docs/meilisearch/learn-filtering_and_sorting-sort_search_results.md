# Sort search results

**Source:** https://www.meilisearch.com/docs/learn/filtering_and_sorting/sort_search_results.md
**Extrait le:** 2025-10-08
**Sujet:** Filtering and Sorting - Sort search results

---

# Sort search results

> By default, Meilisearch sorts results according to their relevancy. You can alter this behavior so users can decide at search time results they want to see first.

By default, Meilisearch focuses on ordering results according to their relevancy. You can alter this sorting behavior so users can decide at search time what type of results they want to see first.

This can be useful in many situations, such as when a user wants to see the cheapest products available in a webshop.

<Tip>
  Sorting at search time can be particularly effective when combined with [placeholder searches](/reference/api/search#placeholder-search).
</Tip>

## Configure Meilisearch for sorting at search time

To allow your users to sort results at search time you must:

1. Decide which attributes you want to use for sorting
2. Add those attributes to the `sortableAttributes` index setting
3. Update Meilisearch's [ranking rules](/learn/relevancy/relevancy) (optional)

<Note>
  Meilisearch sorts strings in lexicographic order based on their byte values. For example, `á`, which has a value of 225, will be sorted after `z`, which has a value of 122.

  Uppercase letters are sorted as if they were lowercase. They will still appear uppercase in search results.
</Note>

### Add attributes to `sortableAttributes`

Meilisearch allows you to sort results based on document fields. Only fields containing numbers, strings, arrays of numeric values, and arrays of string values can be used for sorting.

After you have decided which fields you will allow your users to sort on, you must add their attributes to the [`sortableAttributes` index setting](/reference/api/settings#sortable-attributes).

<Warning>
  If a field has values of different types across documents, Meilisearch will give precedence to numbers over strings. This means documents with numeric field values will be ranked higher than those with string values.

  This can lead to unexpected behavior when sorting. For optimal user experience, only sort based on fields containing the same type of value.
</Warning>

#### Example

Suppose you have collection of books containing the following fields:
