# Filter search results

**Source:** https://www.meilisearch.com/docs/learn/filtering_and_sorting/filter_search_results.md
**Extrait le:** 2025-10-08
**Sujet:** Learn - Filtering and Sorting

---

> In this guide you will see how to configure and use Meilisearch filters in a hypothetical movie database.

In this guide you will see how to configure and use Meilisearch filters in a hypothetical movie database.

## Configure index settings

Suppose you have a collection of movies called `movie_ratings` containing the following fields:

```json
[
  {
    "id": 458723,
    "title": "Us",
    "director": "Jordan Peele",
    "release_date": 1552521600,
    "genres": [
      "Thriller",
      "Horror",
      "Mystery"
    ],
    "rating": {
      "critics": 86,
      "users": 73
    },
  },
  …
]
```

Before using filters, you must add all attributes you want to use for filtering to the `filterableAttributes` index setting. `filterableAttributes` defaults to an empty array (`[]`), meaning none of a document's attributes are filterable.

Use the update filterable attributes endpoint to mark attributes as filterable:

```bash
curl \
  -X PUT 'http://localhost:7700/indexes/movie_ratings/settings/filterable-attributes' \
  -H 'Content-Type: application/json' \
  --data-binary '[
    "director",
    "genres",
    "release_date",
    "rating.critics",
    "rating.users"
  ]'
```

<Note>`id` is the primary key of this index and is thus filterable by default. There is no need to add it to `filterableAttributes`.</Note>

Filterable attributes do not need to be part of the displayed attributes or searchable attributes lists.

Once you have configured `filterableAttributes`, you can use that attribute's values to filter search results.

## Filter results at search time

You can use filters to narrow down search results. This is helpful when querying data that contains a lot of information. For example, getting only movies released after 2020 or directed by Jordan Peele.

Use the `filter` search parameter to filter results based on specific attributes.

### Filter expressions

Filter expressions use the following syntax:

```
field OPERATOR value
```

#### Supported fields

Use dot notation to reference nested fields:

```
rating.critics > 80
```

Fields in arrays and nested object arrays:

```
genres = "Horror"
genres = "Horror" AND genres = "Mystery"
```

#### Supported operators

Meilisearch supports the following filter operators:

- `=`: equal to
- `!=`: not equal to
- `>`: greater than
- `>=`: greater than or equal to
- `<`: less than
- `<=`: less than or equal to
- `TO`: between two values (numeric and alphanumeric)
- `EXISTS` and `NOT EXISTS`: check if a field exists or doesn't exist
- `IS NULL` and `IS NOT NULL`: check if a field contains `null` or non-null
- `IS EMPTY` and `IS NOT EMPTY`: check if array or object is empty or not empty

#### Comparison operators

Use comparison operators to compare a field's value to a specific value:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "thriller",
    "filter": "release_date > 1577836800"
  }'
```

The above query returns only thrillers released after January 1, 2020 (Unix timestamp: `1577836800`).

You can also use a numeric or alphanumeric range with `TO`:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "thriller",
    "filter": "release_date 1577836800 TO 1609459200"
  }'
```

The above query returns only thrillers released between January 1, 2020 (`1577836800`) and December 31, 2020 (`1609459200`).

<Note>When using `TO`, the range is inclusive: `1 TO 10` includes `1` and `10`.</Note>

#### Equality operators

Use equality operators to filter based on exact matches:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "us",
    "filter": "director = \"Jordan Peele\""
  }'
```

The above query returns only movies directed by Jordan Peele.

<Note>When filtering string values, wrap your strings in double quotes (`"`) and escape them with a backslash (`\`) as shown above.</Note>

You can also filter on `_geo` data:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_theaters/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "",
    "filter": "_geoRadius(45.472735, 9.184019, 2000)"
  }'
```

The above query returns documents with a `_geo` field containing coordinates within 2km of the Duomo di Milano. `_geoRadius` takes three parameters: latitude, longitude, and distance in meters.

<Note>`_geo` filtering requires a `_geo` field containing an object with `lat` and `lng` keys with numeric values.</Note>

#### Existence operators

Use `EXISTS` to filter based on whether a field exists:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "thriller",
    "filter": "release_date EXISTS"
  }'
```

Use `NOT EXISTS` to filter documents missing a specific field:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "thriller",
    "filter": "release_date NOT EXISTS"
  }'
```

#### Null operators

Use `IS NULL` to filter documents where a field's value is `null`:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "thriller",
    "filter": "release_date IS NULL"
  }'
```

Use `IS NOT NULL` to filter documents where a field has any non-null value:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "thriller",
    "filter": "release_date IS NOT NULL"
  }'
```

#### Empty operators

Use `IS EMPTY` to filter documents where an array or object is empty:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "thriller",
    "filter": "genres IS EMPTY"
  }'
```

Use `IS NOT EMPTY` to filter documents where an array or object is not empty:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "thriller",
    "filter": "genres IS NOT EMPTY"
  }'
```

### Combining filter expressions

You can build complex filters by combining expressions with `AND` and `OR` operators.

#### AND

Use `AND` to require all conditions be true:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "us",
    "filter": "director = \"Jordan Peele\" AND rating.critics > 85"
  }'
```

The above query returns only Jordan Peele movies with a critics rating above 85.

#### OR

Use `OR` to match any condition:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "thriller",
    "filter": "director = \"Jordan Peele\" OR director = \"Ari Aster\""
  }'
```

The above query returns only thrillers by Jordan Peele or Ari Aster.

#### NOT

Use `NOT` to negate a filter expression:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "thriller",
    "filter": "NOT director = \"Jordan Peele\""
  }'
```

The above query returns only thrillers not directed by Jordan Peele.

<Note>`NOT` has the highest precedence. Use parentheses to control the order of operations.</Note>

#### Grouping with parentheses

Use parentheses to group expressions and control operator precedence:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movie_ratings/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "",
    "filter": "(director = \"Tim Burton\" OR director = \"Christopher Nolan\") AND genres = \"Sci-Fi\""
  }'
```

The above query returns only sci-fi movies by Tim Burton or Christopher Nolan.

### Array filters

Use array notation to build complex filters with multiple expressions:

```json
{
  "filter": [
    "genres = Horror",
    [
      "director = \"Jordan Peele\"",
      "director = \"Ari Aster\""
    ]
  ]
}
```

This is equivalent to:

```
genres = Horror AND (director = "Jordan Peele" OR director = "Ari Aster")
```

Array filter rules:

- Individual array items are joined with `AND`
- Nested arrays are joined with `OR`
- String filters can use `AND`, `OR`, and `NOT`
- You can nest arrays as deeply as needed

For example:

```json
{
  "filter": [
    [
      "genres = Horror",
      "genres = Thriller"
    ],
    "director = \"Jordan Peele\"",
    [
      "rating.critics > 80",
      "rating.users > 80"
    ]
  ]
}
```

This is equivalent to:

```
(genres = Horror OR genres = Thriller) AND director = "Jordan Peele" AND (rating.critics > 80 OR rating.users > 80)
```

## Filtering performance

### `filterableAttributes` and index size

Adding attributes to `filterableAttributes` increases index size. Only add attributes you plan to filter on.

### Filtering on nested fields

Filtering nested fields is less efficient than filtering top-level fields. If you frequently filter on nested fields, consider denormalizing your data structure.

### Filter query cost

Different filter operators have different performance costs:

- **Cheapest**: `=`, `!=`, `EXISTS`, `NOT EXISTS`, `IS NULL`, `IS NOT NULL`, `IS EMPTY`, `IS NOT EMPTY`
- **Moderate**: `>`, `<`, `>=`, `<=`, `TO`
- **Most expensive**: `_geoRadius`

Complex queries with many `OR` and `NOT` operators are more expensive than simple `AND` queries.

## Related resources

- [filterableAttributes API reference](/reference/api/settings#filterable-attributes)
- [filter search parameter](/reference/api/search#filter)
- [Sort search results guide](/learn/filtering_and_sorting/sort_search_results)
- [Geosearch guide](/learn/filtering_and_sorting/geosearch)
