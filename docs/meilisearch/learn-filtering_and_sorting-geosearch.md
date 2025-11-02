# Geosearch

**Source:** https://www.meilisearch.com/docs/learn/filtering_and_sorting/geosearch.md
**Extrait le:** 2025-10-08
**Sujet:** Filtering and Sorting - Geosearch

---

# Geosearch

> Filter and sort search results based on their geographic location.

Meilisearch allows you to filter and sort results based on their geographic location. This can be useful when you only want results within a specific area or when sorting results based on their distance from a specific location.

<Warning>
  Due to Meilisearch allowing malformed `_geo` fields in the following versions (v0.27, v0.28 and v0.29), please ensure the `_geo` field follows the correct format.
</Warning>

## Preparing documents for location-based search

To perform location-based searches, your documents must include a `_geo` field containing a valid GeoJSON object. You can add `_geo` data to documents at any time, but it must be present in a document before that document can be returned as part of a location-based search.

### Valid `_geo` objects

The `_geo` field must contain an object with two keys:

- `lat`: latitude coordinate, must be a floating point number
- `lng`: longitude coordinate, must be a floating point number

```json
{
  "id": 1,
  "name": "Nàpiz' Milano",
  "address": "Viale Vittorio Veneto, 30, 20124, Milan, Italy",
  "_geo": {
    "lat": 45.4777599,
    "lng": 9.1967508
  }
}
```

<Note>
  `_geo` coordinates are always in the order `lat`, `lng`.
</Note>

### Invalid `_geo` objects

Meilisearch will not accept documents with malformed `_geo` data. The following will all cause errors:

```json
// latitude or longitude is missing
{
  "id": 1,
  "name": "Nàpiz' Milano",
  "_geo": {
    "lat": 45.4777599
  }
}
```

```json
// latitude or longitude is not a number
{
  "id": 1,
  "name": "Nàpiz' Milano",
  "_geo": {
    "lat": "45.4777599",
    "lng": 9.1967508
  }
}
```

```json
// _geo is not an object
{
  "id": 1,
  "name": "Nàpiz' Milano",
  "_geo": [45.4777599, 9.1967508]
}
```

## Filtering results with `_geoRadius`

You can use `_geoRadius` to filter results based on their distance from a specific location. `_geoRadius` establishes a circular area around a central point and only returns results located within that area.

`_geoRadius` requires three parameters:

- **latitude**: latitude of the center point, must be a floating point number
- **longitude**: longitude of the center point, must be a floating point number
- **distance**: maximum distance from the center point, can be in meters (`m`), kilometers (`km`), or miles (`mi`)

### Usage

Use `_geoRadius` in a filter expression:

<CodeSamples id="geosearch_guide_filter_usage_1" />

```bash
curl \
  -X POST 'http://localhost:7700/indexes/restaurants/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "filter": "_geoRadius(45.472735, 9.184019, 2000)"
  }'
```

The above query returns all restaurants located within 2000 meters of the specified geographic coordinates.

You can use `_geoRadius` with other filters:

<CodeSamples id="geosearch_guide_filter_usage_2" />

```bash
curl \
  -X POST 'http://localhost:7700/indexes/restaurants/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "filter": "type = pizza AND _geoRadius(45.472735, 9.184019, 2 km)"
  }'
```

The above query returns pizza restaurants within 2 kilometers of the specified point.

## Sorting results with `_geoPoint`

Use `_geoPoint` to sort results based on their distance from a geographic location. `_geoPoint` requires two parameters:

- **latitude**: latitude of the reference point, must be a floating point number
- **longitude**: longitude of the reference point, must be a floating point number

### Usage

Use `_geoPoint` in the `sort` search parameter:

<CodeSamples id="geosearch_guide_sort_usage_1" />

```bash
curl \
  -X POST 'http://localhost:7700/indexes/restaurants/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "sort": ["_geoPoint(45.472735, 9.184019):asc"]
  }'
```

The above query returns results sorted by their distance from the specified geographic coordinates, from nearest to farthest.

You can combine `_geoPoint` with other sorting rules:

<CodeSamples id="geosearch_guide_sort_usage_2" />

```bash
curl \
  -X POST 'http://localhost:7700/indexes/restaurants/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "filter": "type = pizza",
    "sort": [
      "_geoPoint(45.472735, 9.184019):asc",
      "rating:desc"
    ]
  }'
```

The above query returns pizza restaurants sorted by distance, with those at the same distance sorted by rating.

### `_geoDistance` in search results

When using `_geoPoint` to sort results, Meilisearch includes a `_geoDistance` field in each search result. This field contains the distance in meters between the document and the reference point specified in `_geoPoint`.

```json
{
  "hits": [
    {
      "id": 1,
      "name": "Nàpiz' Milano",
      "address": "Viale Vittorio Veneto, 30, 20124, Milan, Italy",
      "_geo": {
        "lat": 45.4777599,
        "lng": 9.1967508
      },
      "_geoDistance": 1532
    }
  ]
}
```

## Configuring geosearch

By default, Meilisearch indexes the `_geo` field as a sortable attribute. This allows you to use `_geoPoint` without additional configuration.

If you have disabled `_geo` as a sortable attribute, you must re-enable it to use `_geoPoint`:

<CodeSamples id="geosearch_guide_settings_1" />

```bash
curl \
  -X PATCH 'http://localhost:7700/indexes/restaurants/settings' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "sortableAttributes": ["_geo"]
  }'
```

You do not need to configure anything to use `_geoRadius` filters.

## Conclusion

Meilisearch's geosearch features allow you to create location-aware search experiences. Use `_geoRadius` to find results within a specific area and `_geoPoint` to sort results by distance from a location.
