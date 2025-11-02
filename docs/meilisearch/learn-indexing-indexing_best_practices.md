# Indexing best practices

**Source:** https://www.meilisearch.com/docs/learn/indexing/indexing_best_practices.md
**Extrait le:** 2025-10-08
**Sujet:** Indexing - Best Practices

---

# Indexing best practices

> Tips to speed up your documents indexing process.

In this guide, you will find some of the best practices to index your data efficiently and speed up the indexing process.

## Define searchable attributes

Review your list of [searchable attributes](/learn/relevancy/displayed_searchable_attributes#searchable-fields) and ensure it includes only the fields you want to be checked for query word matches. This improves both relevancy and search speed by removing irrelevant data from your database. It will also keep your disk usage to the necessary minimum.

By default, all document fields are searchable. The fewer fields Meilisearch needs to index, the faster the indexing process.

### Review filterable and sortable attributes

Some document fields are necessary for [filtering](/learn/filtering_and_sorting/filter_search_results) and [sorting](/learn/filtering_and_sorting/sort_search_results) results, but they do not need to be *searchable*. Generally, **numeric and boolean fields** fall into this category. Make sure to review your list of searchable attributes and remove any fields that are only used for filtering or sorting.

## Configure your index before adding documents

When creating a new index, first [configure its settings](/reference/api/settings) and only then add your documents. Whenever you update settings such as [ranking rules](/learn/relevancy/relevancy), Meilisearch will trigger a reindexing of all your documents. This can be a time-consuming process, especially if you have a large dataset. For this reason, it is better to define ranking rules and other settings before indexing your data.

## Optimize document size

Smaller documents are processed faster, so make sure to trim down any unnecessary data from your documents. When a document field is missing from the list of [searchable](/reference/api/settings#searchable-attributes), [filterable](/reference/api/settings#filterable-attributes), [sortable](/reference/api/settings#sortable-attributes), or [displayed](/reference/api/settings#displayed-attributes) attributes, it might be best to remove it from the document. To go further, consider compressing your data using methods such as `br`, `deflate`, or `gzip`. Consult the [supported encoding formats reference](/reference/api/overview