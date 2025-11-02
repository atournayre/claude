# Search result pagination

**Source:** https://www.meilisearch.com/docs/guides/front_end/pagination.md
**Extrait le:** 2025-10-08
**Sujet:** Guide - Pagination des résultats de recherche

---

> Follow this guide to learn more about the two pagination types available Meilisearch.

In a perfect world, users would not need to look beyond the first search result to find what they were looking for. In practice, however, it is usually necessary to create some kind of pagination interface to browse through long lists of results.

In this guide, we discuss two different approaches to pagination supported by Meilisearch: one using `offset` and `limit`, and another using `hitsPerPage` and `page`.

## Choosing the right pagination UI

There are many UI patterns that help your users navigate through search results. One common and efficient solution in Meilisearch is using `offset` and `limit` to create interfaces centered around ["Previous" and "Next" buttons](#previous-and-next-buttons).

Other solutions, such as [creating a page selector](/guides/front_end/pagination#numbered-page-selectors) allowing users to jump to any search results page, make use of `hitsPerPage` and `page` to obtain the exhaustive total number of matched documents. These tend to be less efficient and may result in decreased performance.

Whatever UI pattern you choose, there is a limited maximum number of search results Meilisearch will return for any given query. You can use [the `maxTotalHits` index setting](/reference/api/settings#pagination) to configure this, but be aware that higher limits will negatively impact search performance.

<Danger>
  Setting `maxTotalHits` to a value higher than the default will negatively impact search performance. Setting `maxTotalHits` to values over `20000` may result in queries taking seconds to complete.
</Danger>

## "Previous" and "Next" buttons

Using "Previous" and "Next" buttons for pagination means that users can easily navigate through results, but don't have the ability to jump to an arbitrary results page. This is Meilisearch's recommended solution when creating paginated interfaces.

Though this approach offers less precision than a full-blown page selector, it does not require knowing the exact number of search results. Since calculating the exhaustive number of documents matching a query is a resource-intensive process, interfaces like this might offer better performance.

### Implementation

To implement this interface in a website or application, we make our queries using `offset` and `limit` parameters.
