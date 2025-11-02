# Known limitations

**Source:** https://www.meilisearch.com/docs/learn/resources/known_limitations.md
**Extrait le:** 2025-10-08
**Sujet:** Resources - Known Limitations

---

# Known limitations

> Meilisearch has a number of known limitations. These are hard limits you cannot change and should take into account when designing your application.

Meilisearch has a number of known limitations. Some of these limitations are the result of intentional design trade-offs, while others can be attributed to [LMDB](/learn/engine/storage), the key-value store that Meilisearch uses under the hood.

This article covers hard limits that cannot be altered. Meilisearch also has some default limits that *can* be changed, such as a [default payload limit of 100MB](/learn/self_hosted/configure_meilisearch_at_launch#payload-limit-size) and a [default search limit of 20 hits](/reference/api/search#limit).

## Maximum Meilisearch Cloud upload size

**Limitation:** The maximum file upload size when using the Meilisearch Cloud interface is 20mb.

**Explanation:** Handling large files may result in degraded user experience and performance issues. To add datasets larger than 20mb to a Meilisearch Cloud project, use the [add documents endpoint](/reference/api/documents#add-or-replace-documents) or [`meilisearch-importer`](https://github.com/meilisearch/meilisearch-importer).

## Maximum number of query words

**Limitation:** The maximum number of terms taken into account for each [search query](/reference/api/search#query-q) is 10. If a search query includes more than 10 words, all words after the 10th will be ignored.

**Explanation:** Queries with many search terms can lead to long response times. This goes against our goal of providing a fast search-as-you-type experience.

## Maximum number of words per attribute

**Limitation:** Meilisearch can index a maximum of 65535 positions per attribute. Any words exceeding the 65535 position limit will be silently ignored.

**Explanation:** This limit is enforced for relevancy reasons. The more words there are in a given attribute, the less relevant the search queries will be.

### Example

Suppose you have three similar queries: `Hello World`, `Hello, World`, and `Hello - World`.
