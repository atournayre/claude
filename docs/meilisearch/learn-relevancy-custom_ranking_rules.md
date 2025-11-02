# Custom ranking rules

**Source:** https://www.meilisearch.com/docs/learn/relevancy/custom_ranking_rules.md
**Extrait le:** 2025-10-08
**Sujet:** Relevancy - Custom Ranking Rules

---

# Custom ranking rules

> Custom ranking rules promote certain documents over other search results that are otherwise equally relevant.

There are two types of ranking rules in Meilisearch: [built-in ranking rules](/learn/relevancy/ranking_rules) and custom ranking rules. This article describes the main aspects of using and configuring custom ranking rules.

Custom ranking rules promote certain documents over other search results that are otherwise equally relevant.

## Ascending and descending sorting rules

Meilisearch supports two types of custom rules: one for ascending sort and one for descending sort.

To add a custom ranking rule, you have to communicate the attribute name followed by a colon (`:`) and either `asc` for ascending order or `desc` for descending order.

* To apply an **ascending sort** (results sorted by increasing value of the attribute): `attribute_name:asc`

* To apply a **descending sort** (results sorted by decreasing value of the attribute): `attribute_name:desc`

**The attribute must have either a numeric or a string value** in all of the documents contained in that index.

You can add this rule to the existing list of ranking rules using the [update settings endpoint](/reference/api/settings#update-settings) or [update ranking rules endpoint](/reference/api/settings#update-ranking-rules).

## Example

Suppose you have a movie dataset. The documents contain the fields `release_date` with a timestamp as value, and `movie_ranking`, an integer that represents its ranking.

The following example creates a rule that makes older movies more relevant than recent ones. A movie released in 1999 will appear before a movie released in 2020.

```
release_date:asc
```

The following example will create a rule that makes movies with a good rank more relevant than movies with a lower rank. Movies with a higher ranking will appear first.

```
movie_ranking:desc
```

The following array includes all built-in ranking rules and places the custom rules at the bottom of the processing order:

```json
[
  "words",
  "typo",
  "proximity",
  "attribute",
  "sort",
  "exactness",
  "release_date:asc",
  "movie_ranking:desc"
]
```

## Sorting at search time

Custom ranking rules are not the only way to sort results in Meilisearch. You can also use the `sort` search parameter to order results at query time.

When using `sort`, Meilisearch follows the sorting order you specify in your query, without taking into account built-in ranking rules such as `typo` and `words`.

Custom ranking rules, instead, only apply to results that are otherwise equally relevant.

[Read more about sorting results](/learn/filtering_and_sorting/sort_search_results).
