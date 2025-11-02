# Filtering and sorting by date

**Source:** https://www.meilisearch.com/docs/learn/filtering_and_sorting/working_with_dates.md
**Extrait le:** 2025-10-08
**Sujet:** Learn - Filtering and Sorting - Working with Dates

---

# Filtering and sorting by date

> Learn how to index documents with chronological data, and how to sort and filter search results based on time.

In this guide, you will learn about Meilisearch's approach to date and time values, how to prepare your dataset for indexing, and how to chronologically sort and filter search results.

## Preparing your documents

To filter and sort search results chronologically, your documents must have at least one field containing a [UNIX timestamp](https://kb.narrative.io/what-is-unix-time). You may also use a string with a date in a format that can be sorted lexicographically, such as `"2025-01-13"`.

As an example, consider a database of video games. In this dataset, the release year is formatted as a timestamp:

```json
[
  {
    "id": 0,
    "title": "Return of the Obra Dinn",
    "genre": "adventure",
    "release_timestamp": 1538949600
  },
  {
    "id": 1,
    "title": "The Excavation of Hob's Barrow",
    "genre": "adventure",
    "release_timestamp": 1664316000
  },
  {
    "id": 2,
    "title": "Bayonetta 2",
    "genre": "action",
    "release_timestamp": 1411164000
  }
]
```

## Configuring filterable and sortable attributes

After adding documents to Meilisearch, you must explicitly allow filtering and sorting for the fields containing date information.

Use the `filterableAttributes` index setting to configure fields you can use when filtering results:

```sh
curl \
  -X PUT 'http://localhost:7700/indexes/games/settings/filterable-attributes' \
  -H 'Content-Type: application/json' \
  --data-binary '[
    "release_timestamp"
  ]'
```

Use the `sortableAttributes` index setting to configure fields you can use to sort results:

```sh
curl \
  -X PUT 'http://localhost:7700/indexes/games/settings/sortable-attributes' \
  -H 'Content-Type: application/json' \
  --data-binary '[
    "release_timestamp"
  ]'
```

## Filtering results based on date

Use the `filter` search parameter with [comparison operators](/reference/api/search#comparison-operators) to filter results based on their timestamps:

```sh
curl \
  -X POST 'http://localhost:7700/indexes/games/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "",
    "filter": "release_timestamp > 1577836800"
  }'
```

In this example, Meilisearch will only return games released after the first of January of 2020.

You may also use the comparison operators with string values as long as they can be sorted lexicographically. For example, `"release_date > \"2020-01-01\""` will return the same results as the query above.

## Sorting search results by date

Use the `sort` search parameter to sort results in ascending or descending date order:

```sh
curl \
  -X POST 'http://localhost:7700/indexes/games/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "",
    "sort": ["release_timestamp:desc"]
  }'
```

When you sort results with `sort`, Meilisearch effectively deactivates its built-in ranking rules. This can lead to unexpected results when performing queries with non-empty search terms. You can partially mitigate this by using the `showRankingScore` and `rankingScoreThreshold` parameters. Consult the [API reference](/reference/api/search#ranking-score) for more information.

## Filtering and sorting with timestamps in milliseconds

UNIX timestamps are whole numbers representing the seconds elapsed since 1 January 1970. For increased precision, many systems use millisecond timestamps: whole numbers representing the milliseconds elapsed since 1 January 1970.

Meilisearch stores numeric values as a signed 32-bit integer. This means it can store values between -2³¹ and 2³¹-1. Since `2³¹-1` evaluates to `2147483647`, Meilisearch is not able to store timestamps bigger than 2147483647.

A few example dates that would overflow a 32-bit timestamp:

| Date | Timestamp (seconds) | Timestamp (milliseconds) |
| ---- | ------------------- | ------------------------ |
| 19 January 2038, 3:14:07 AM | 2147483647 | 2147483647000 |
| 1 January 2020 | 1577836800 | 1577836800000 |
| 9 September 2001 | 1000000000 | 1000000000000 |

Millisecond timestamps after 9 September 2001 will overflow the limits of 32-bit integers.

If your dataset contains millisecond timestamps, store them as string values and format them to support lexicographic sorting:

```json
[
  {
    "id": 0,
    "title": "Return of the Obra Dinn",
    "genre": "adventure",
    "release_timestamp": "1538949600000"
  }
]
```

When filtering or sorting by date, quote your string values so Meilisearch does not treat them as integers:

```sh
curl \
  -X POST 'http://localhost:7700/indexes/games/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "",
    "filter": "release_timestamp > \"1577836800000\""
  }'
```

## Conclusion

You should now be able to:

- Prepare your dataset with UNIX timestamps
- Configure `filterableAttributes` and `sortableAttributes`
- Filter search results with comparison operators and the `filter` parameter
- Sort search results chronologically with the `sort` parameter
- Work with timestamps in both seconds and milliseconds
