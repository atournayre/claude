# Built-in ranking rules

**Source:** https://www.meilisearch.com/docs/learn/relevancy/ranking_rules.md
**Extrait le:** 2025-10-08
**Sujet:** Relevancy - Ranking Rules

---

# Built-in ranking rules

> Built-in ranking rules are the core of Meilisearch's relevancy calculations.

There are two types of ranking rules in Meilisearch: built-in ranking rules and [custom ranking rules](/learn/relevancy/custom_ranking_rules). This article describes the main aspects of using and configuring built-in ranking rules.

Built-in ranking rules are the core of Meilisearch's relevancy calculations.

## List of built-in ranking rules

Meilisearch contains six built-in ranking rules in the following order:

```json
[
  "words",
  "typo",
  "proximity",
  "attribute",
  "sort",
  "exactness"
]
```

Depending on your needs, you might want to change this order. To do so, use the [update settings endpoint](/reference/api/settings#update-settings) or [update ranking rules endpoint](/reference/api/settings#update-ranking-rules).

## 1. Words

Results are sorted by **decreasing number of matched query terms**. Returns documents that contain all query terms first.

To ensure optimal relevancy, **Meilisearch always sort results as if the `words` ranking rule were present** with a higher priority than the attributes, exactness, typo and proximity ranking rules. This happens even if `words` has been removed or set with a lower priority.

<Note>
  The `words` rule works from right to left. Therefore, the order of the query string impacts the order of results.

  For example, if someone were to search `batman dark knight`, the `words` rule would rank documents containing all three terms first, documents containing only `batman` and `dark` second, and documents containing only `batman` third.
</Note>

## 2. Typo

Results are sorted by **increasing number of typos**. Returns documents that match query terms with fewer typos first.

## 3. Proximity

Results are sorted by **increasing distance between matched query terms**. Returns documents where query terms occur close together and in the same order as the query string first.

[It is possible to lower the precision of this ranking rule.](/reference/api/settings#proximity-precision) This may significantly improve indexing performance. In a minority of use cases, it might also negatively impact search results relevancy.

## 4. Attribute

Results are sorted according to the **[attribute ranking order](/learn/relevancy/displayed_searchable_attributes#searchable-fields)**. Returns documents that contain query terms in more important attributes first.

The attribute ranking order is determined by the order in which attributes appear in the [searchableAttributes list](/learn/configuration/configuring_index_settings#searchable-fields). When a document field is not in the `searchableAttributes` list, the attribute rule gives it a default ranking.

<Note>
  The `attribute` ranking rule always applies, even if it was removed or if it was placed after custom ranking rules. However, setting its position will change how it interacts with [custom ranking rules](/learn/relevancy/custom_ranking_rules).
</Note>

## 5. Sort

Results are sorted according to parameters decided at query time. When the [`sort` search parameter](/reference/api/search#sort) is not used, this rule has no impact on search results.

[Read more about sorting and geosearch.](/learn/filtering_and_sorting/sort_search_results)

## 6. Exactness

Results are sorted by **the similarity of the matched words with the query words**. Returns documents that contain exactly the same terms as the ones in the query string first.

[Exactness is calculated differently depending on the type of search.](/learn/relevancy/exactness)

## Ranking rules and search intent

Meilisearch's search intent detection adds a layer of subtlety to ranking rules.

When Meilisearch detects a search query is looking for exact matches, it will consider the query to be `keyword` search.  In these cases, Meilisearch will partially skip the `typo` ranking rule in order to better satisfy user intent.

[Read more about search intent detection.](/learn/relevancy/search_intent)

## Deleting a ranking rule

To remove a ranking rule, set the `rankingRules` array to the list of rules you want to keep. The removed ranking rules will no longer apply.

For example, if you want to remove the `typo` ranking rule, you would send the following request:

```json
[
  "words",
  "proximity",
  "attribute",
  "sort",
  "exactness"
]
```

Note that removing the `attribute` rule will not remove its effect on the ranking. The `attribute` ranking rule always applies, even if it was removed or if it was placed after custom ranking rules.

## Changing ranking rule order

You might also want to change the order of the ranking rules. In some cases, the order of ranking rules can have a significant impact on your search results.

To change the order of the rules, use the [update ranking rules endpoint](/reference/api/settings#update-ranking-rules) and send them in the desired order:

```json
[
  "words",
  "typo",
  "attribute",
  "proximity",
  "sort",
  "exactness"
]
```

In the above example, the `attribute` rule has been placed before `proximity`.

## Resetting ranking rules

To restore default ranking rules, send an empty array to the [update ranking rules endpoint](/reference/api/settings#update-ranking-rules).
