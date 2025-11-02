# Settings API Reference

**Source:** https://www.meilisearch.com/docs/reference/api/settings.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Settings configuration

---

# Settings

> The /settings route allows you to customize search settings for the given index.

export const NoticeTag = ({label}) => <span className="noticeTag noticeTag--{ label }">
    {label}
  </span>;

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

Use the `/settings` route to customize search settings for a given index. You can either modify all index settings at once using the [update settings endpoint](#update-settings), or use a child route to configure a single setting.

For a conceptual overview of index settings, refer to the [indexes explanation](/learn/getting_started/indexes#index-settings). To learn more about the basics of index configuration, refer to the [index configuration tutorial](/learn/configuration/configuring_index_settings_api).

## Settings interface

[Meilisearch Cloud](https://meilisearch.com/cloud) offers a [user-friendly graphical interface for managing index settings](/learn/configuration/configuring_index_settings) in addition to the `/settings` route. The Cloud interface offers more immediate and visible feedback, and is helpful for tweaking relevancy when used in conjunction with the [search preview](/learn/getting_started/search_preview).

## Settings object

By default, the settings object looks like this. All fields are modifiable.

```json
{
  "displayedAttributes": [
    "*"
  ],
  "searchableAttributes": [
    "*"
  ],
  "filterableAttributes": [],
  "sortableAttributes": [],
  "rankingRules":
  [
    "words",
    "typo",
    "proximity",
    "attribute",
    "sort",
    "exactness"
  ],
  "stopWords": [],
  "nonSeparatorTokens": [],
  "separatorTokens": [],
  "dictionary": [],
  "synonyms": {},
  "distinctAttribute": null,
  "proximityPrecision": "byWord",
  "typoTolerance": {
    "enabled": true,
    "minWordSizeForTypos": {
      "oneTypo": 5,
      "twoTypos": 9
    },
    "disableOnWords": [],
    "disableOnAttributes": []
  },
  "faceting": {
    "maxValuesPerFacet": 100,
    "sortFacetValuesBy": {
      "*": "alpha"
    }
  },
  "pagination": {
    "maxTotalHits": 1000
  },
  "embedders": null,
  "searchCutoffMs": null,
  "localizedAttributes": null
}
```

## Get settings

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings"/>

Get the settings of an index.

[Learn more about index settings.](/learn/getting_started/indexes#index-settings)

### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Example

<CodeSamples id="get_settings_1" />

#### Response: `200 Ok`

```json
{
  "displayedAttributes": [
    "*"
  ],
  "searchableAttributes": [
    "*"
  ],
  "filterableAttributes": [],
  "sortableAttributes": [],
  "rankingRules": [
    "words",
    "typo",
    "proximity",
    "attribute",
    "sort",
    "exactness"
  ],
  "stopWords": [],
  "nonSeparatorTokens": [],
  "separatorTokens": [],
  "dictionary": [],
  "synonyms": {},
  "distinctAttribute": null,
  "proximityPrecision": "byWord",
  "typoTolerance": {
    "enabled": true,
    "minWordSizeForTypos": {
      "oneTypo": 5,
      "twoTypos": 9
    },
    "disableOnWords": [],
    "disableOnAttributes": []
  },
  "faceting": {
    "maxValuesPerFacet": 100,
    "sortFacetValuesBy": {
      "*": "alpha"
    }
  },
  "pagination": {
    "maxTotalHits": 1000
  },
  "embedders": null,
  "searchCutoffMs": null,
  "localizedAttributes": null
}
```

## Update settings

<RouteHighlighter method="PATCH" path="/indexes/{index_uid}/settings"/>

Update the settings of an index. Passing `null` to an index setting will reset it to its default value.

Updates in the settings route are **partial**. This means that any parameters not provided in the body will be left unchanged.

If the provided index does not exist, it will be created.

[Learn more about index settings.](/learn/getting_started/indexes#index-settings)

### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Body

| Variable                                                                                                   | Type             | Description                                                                                                                                                           | Default value                                                 |
| :--------------------------------------------------------------------------------------------------------- | :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------ |
| **[`displayedAttributes`](/reference/api/settings#displayed-attributes)**             | Array of strings | Fields displayed in the returned documents                                                                                                                            | `["*"]` (all attributes)                                      |
| **[`searchableAttributes`](/reference/api/settings#searchable-attributes)**           | Array of strings | Fields in which to search for matching query words sorted by order of importance                                                                                      | `["*"]` (all attributes)                                      |
| **[`filterableAttributes`](/reference/api/settings#filterable-attributes)**           | Array of strings | Fields used for [filtering](/learn/filtering_and_sorting/filter_search_results) and faceted search                                                      | `[]`                                                          |
| **[`sortableAttributes`](/reference/api/settings#sortable-attributes)**               | Array of strings | Fields used for [sorting](/learn/filtering_and_sorting/sort_search_results)                                                                             | `[]`                                                          |
| **[`rankingRules`](/reference/api/settings#ranking-rules)**                           | Array of strings | Ranking rules in order of importance                                                                                                                                  | [A list of ordered built-in ranking rules](/learn/relevancy/relevancy#ranking-rules) |
| **[`stopWords`](/reference/api/settings#stop-words)**                                 | Array of strings | Words ignored by Meilisearch when present in search queries                                                                                                           | `[]`                                                          |
| **[`nonSeparatorTokens`](/reference/api/settings#non-separator-tokens)**              | Array of strings | List of characters Meilisearch should not treat as word separators                                                                                                    | `[]`                                                          |
| **[`separatorTokens`](/reference/api/settings#separator-tokens)**                     | Array of strings | List of characters Meilisearch should treat as word separators, even when the language default considers them part of a word                                          | `[]`                                                          |
| **[`dictionary`](/reference/api/settings#dictionary)**                                | Array of strings | List of words Meilisearch should not split. Each string must contain a single word. Words are not case sensitive                                                     | `[]`                                                          |
| **[`synonyms`](/reference/api/settings#synonyms)**                                    | Object           | List of associated words treated similarly                                                                                                                            | `{}`                                                          |
| **[`distinctAttribute`](/reference/api/settings#distinct-attribute)**                 | String           | Search returns documents with distinct (different) values of the given field                                                                                          | `null`                                                        |
| **[`proximityPrecision`](/reference/api/settings#proximity-precision)**               | String           | Determines how Meilisearch calculates proximity between query terms. Either `byWord` or `byAttribute`                                                                 | `byWord`                                                      |
| **[`typoTolerance`](/reference/api/settings#typo-tolerance)**                         | Object           | Typo tolerance settings                                                                                                                                               | [Typo tolerance object](/reference/api/settings#typo-tolerance-object)         |
| **[`faceting`](/reference/api/settings#faceting)**                                    | Object           | Faceting settings                                                                                                                                                     | [Faceting object](/reference/api/settings#faceting-object)                     |
| **[`pagination`](/reference/api/settings#pagination)**                                | Object           | Pagination settings                                                                                                                                                   | [Pagination object](/reference/api/settings#pagination-object)                 |
| **[`embedders`](/reference/api/settings#embedders)**                                  | Object / `null`  | Configure vector search                                                                                                                                               | `null`                                                        |
| **[`searchCutoffMs`](/reference/api/settings#search-cutoff-ms)**                      | Integer / `null` | Configure a runtime in milliseconds beyond which Meilisearch interrupts the search and delivers results based on the data it scanned before the interruption          | `null`                                                        |
| **[`localizedAttributes`](/reference/api/settings#localized-attributes)** <NoticeTag label="experimental" /> | Array of objects / `null` | Configure language-specific settings for attributes                                                                                                                   | `null`                                                        |

### Example

<CodeSamples id="update_settings_1" />

#### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Reset settings

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings"/>

Reset all the settings of an index to their [default value](#settings-object).

### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Example

<CodeSamples id="reset_settings_1" />

#### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Displayed attributes

The fields whose attributes are added to the displayed-attributes list are **displayed in each matching document**.

Documents returned upon search contain only displayed fields.

[Learn more about displayed attributes.](/learn/fine_tuning_results/displayed_searchable_attributes#displayed-fields)

### Get displayed attributes

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/displayed-attributes"/>

Get the displayed attributes of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_displayed_attributes_1" />

##### Response: `200 Ok`

```json
[
  "*"
]
```

### Update displayed attributes

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/displayed-attributes"/>

Update the displayed attributes of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

An array of strings that contains attributes of an index to display.

If you specify `null` or a field that does not exist, the engine will return an error, even when using array notation (`["*"]`).

| Variable               | Type             | Description                            | Default value            |
| :--------------------- | :--------------- | :------------------------------------- | :----------------------- |
| **displayedAttributes** | Array of strings | Fields displayed in returned documents | `["*"]` (all attributes) |

#### Example

<CodeSamples id="update_displayed_attributes_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset displayed attributes

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/displayed-attributes"/>

Reset the displayed attributes of the index to the default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_displayed_attributes_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Distinct attribute

The **value of a field** whose attribute is set as a distinct attribute will always be **unique** in the returned documents.

[Learn more about the distinct attribute.](/learn/configuration/distinct)

### Get distinct attribute

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/distinct-attribute"/>

Get the distinct attribute field of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_distinct_attribute_1" />

##### Response: `200 Ok`

```json
null
```

### Update distinct attribute

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/distinct-attribute"/>

Update the distinct attribute field of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

| Variable               | Type   | Description                             | Default value |
| :--------------------- | :----- | :-------------------------------------- | :------------ |
| **distinctAttribute** | String | Field to apply the distinct attribute | `null`        |

#### Example

<CodeSamples id="update_distinct_attribute_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset distinct attribute

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/distinct-attribute"/>

Reset the distinct attribute field of an index to its default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_distinct_attribute_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Faceting

Configure facet behavior and options.

[Learn more about faceting.](/learn/filtering_and_sorting/faceted_search)

### Faceting object

| Name                                      | Type    | Default value         | Description                                                                                                           |
| :---------------------------------------- | :------ | :-------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| **[`maxValuesPerFacet`](#max-values-per-facet)** | Integer | `100`                 | Maximum number of facet values returned for each facet                                                                |
| **[`sortFacetValuesBy`](#sort-facet-values-by)** | Object  | `{ "*": "alpha" }` | Customize facet order. By default, facet values are sorted alphanumerically in ascending order across all facets |

### Get faceting settings

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/faceting"/>

Get the faceting settings of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_faceting_1" />

##### Response: `200 Ok`

```json
{
  "maxValuesPerFacet": 100,
  "sortFacetValuesBy": {
    "*": "alpha"
  }
}
```

### Update faceting settings

<RouteHighlighter method="PATCH" path="/indexes/{index_uid}/settings/faceting"/>

Partially update the faceting settings for an index. Any parameters not provided in the body will be left unchanged.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

| Variable                                      | Type    | Description                                                                                                                               | Default value         |
| :-------------------------------------------- | :------ | :---------------------------------------------------------------------------------------------------------------------------------------- | :-------------------- |
| **[`maxValuesPerFacet`](#max-values-per-facet)** | Integer | Maximum number of facet values returned for each facet                                                                                    | `100`                 |
| **[`sortFacetValuesBy`](#sort-facet-values-by)** | Object  | Customize facet value order. By default, all facets are sorted alphanumerically in ascending order with the `"*": "alpha"` key-value pair | `{ "*": "alpha" }` |

#### Example

<CodeSamples id="update_faceting_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset faceting settings

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/faceting"/>

Reset an index's faceting settings to their default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_faceting_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Max values per facet

Configure the maximum number of values returned by the [facet search parameters](/reference/api/search#facets).

`maxValuesPerFacet` takes an integer with a maximum value of `1000`.

### Sort facet values by

Control the sort order of facet values. If multiple sorting rules are provided, the first rule has the highest precedence.

`sortFacetValuesBy` is an object whose keys are the names of facets and whose values are the sort order. The facet name must be present in [`filterableAttributes`](/reference/api/settings#filterable-attributes).

The sort order can be either `alpha` (alphanumeric, ascending) or `count` (by number of matching results, descending).

Use the `*` character as a wildcard key to configure the default sort order for all facets. If you set a custom rule for a facet as well as a wildcard rule, the custom rule overrides the wildcard.

[Learn more about `sortFacetValuesBy`.](/learn/filtering_and_sorting/faceted_search#the-sortfacetvaluesby-setting)

---

## Filterable attributes

Attributes used as criteria for filtering and faceted search.

[Learn more about filterable attributes.](/learn/filtering_and_sorting/filter_search_results#configuring-filters)

### Get filterable attributes

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/filterable-attributes"/>

Get the filterable attributes of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_filterable_attributes_1" />

##### Response: `200 Ok`

```json
[]
```

### Update filterable attributes

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/filterable-attributes"/>

Update the filterable attributes of an index.

Adding a field to the `filterableAttributes` list triggers Meilisearch to create the corresponding inverted index, if it doesn't already exist.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

An array of strings containing the attributes that can be used as filters at query time.

| Variable                  | Type             | Description                                                | Default value |
| :------------------------ | :--------------- | :--------------------------------------------------------- | :------------ |
| **filterableAttributes** | Array of strings | Attributes to use as filters and facets for a search query | `[]`          |

#### Example

<CodeSamples id="update_filterable_attributes_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset filterable attributes

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/filterable-attributes"/>

Reset the filterable attributes of the index to the default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_filterable_attributes_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Localized attributes <NoticeTag label="experimental" />

Configures language-specific settings for certain index attributes.

[Learn more about the localized attributes setting.](/learn/relevancy/language_support#localized-attributes)

### Get localized attributes

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/localized-attributes"/>

Get the localized attributes of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_localized_attributes_1" />

##### Response: `200 Ok`

```json
null
```

### Update localized attributes

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/localized-attributes"/>

Update the localized attributes of an index. This will completely overwrite the old list of localized attributes with the new one.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

An array of objects. Each object maps an attribute to a locale.

| Variable                  | Type                      | Description                                                         | Default value |
| :------------------------ | :------------------------ | :------------------------------------------------------------------ | :------------ |
| **localizedAttributes** | Array of objects / `null` | Applies language-specific rules to one or more index attributes | `null`        |

Each object in the `localizedAttributes` array must follow this structure:

| Variable       | Type                      | Description                                                                                                                                                                    |
| :------------- | :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **locales**    | Array of strings          | Array of supported locales in [ISO 639-3](https://iso639-3.sil.org/) format. Meilisearch will apply language-specific rules for these locales to `attributePatterns`     |
| **attributePatterns** | Array of strings | Array of attribute patterns. Meilisearch will apply language-specific rules to attributes matching any of these patterns. Patterns may use [wildcards](#attribute-wildcards) |

Use `null` to reset `localizedAttributes` to its default value.

##### Attribute wildcards

Attribute patterns may include the wildcard character `*`, which matches any number of characters in attribute names:

- `*`: matches all attributes
- `title_*`: matches `title_en`, `title_fr`, `title_de`, etc.
- `*_ja`: matches `title_ja`, `description_ja`, `author_ja`, etc.
- `t*_*n`: matches `title_en`, `title_cn`, `translation_en`, `t_in`, etc.

When setting `localizedAttributes`, duplicate an attribute or an attribute pattern in multiple locale groups. If you do this, the last locale group in the array will have precedence.

#### Example

<CodeSamples id="update_localized_attributes_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset localized attributes

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/localized-attributes"/>

Reset the localized attributes of the index to the default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_localized_attributes_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Pagination

Configure pagination behavior for searches performed on this index.

[Learn more about result pagination.](/learn/filtering_and_sorting/pagination)

### Pagination object

| Name                                                        | Type    | Default value | Description                                               |
| :---------------------------------------------------------- | :------ | :------------ | :-------------------------------------------------------- |
| **[`maxTotalHits`](#maximum-number-of-results-per-search)** | Integer | `1000`        | Maximum number of search results Meilisearch can return |

### Get pagination settings

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/pagination"/>

Get the pagination settings of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_pagination_1" />

##### Response: `200 Ok`

```json
{
  "maxTotalHits": 1000
}
```

### Update pagination settings

<RouteHighlighter method="PATCH" path="/indexes/{index_uid}/settings/pagination"/>

Update the pagination settings of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

| Variable                                                | Type    | Description                                               | Default value |
| :------------------------------------------------------ | :------ | :-------------------------------------------------------- | :------------ |
| **[`maxTotalHits`](#maximum-number-of-results-per-search)** | Integer | Maximum number of search results Meilisearch can return | `1000`        |

#### Example

<CodeSamples id="update_pagination_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset pagination settings

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/pagination"/>

Reset an index's pagination settings to their default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_pagination_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Maximum number of results per search

Configure the maximum number of search results Meilisearch can return. By default, Meilisearch returns up to 1000 search results.

`maxTotalHits` takes an integer with a maximum value of `20000`.

---

## Proximity precision

`proximityPrecision` allows you to determine how Meilisearch calculates proximity between multiple query terms.

When `proximityPrecision` is set to `byWord`, Meilisearch favors document fields containing query terms that are close to each other. When it is set to `byAttribute`, Meilisearch will favor documents containing query terms in the same attribute, but ignores word distance.

[Learn more about proximity precision.](/learn/relevancy/proximity#precision-level)

### Get proximity precision

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/proximity-precision"/>

Get the proximity precision setting of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_proximity_precision_setting_1" />

##### Response: `200 Ok`

```json
"byWord"
```

### Update proximity precision

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/proximity-precision"/>

Update the proximity precision setting for an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

| Variable                | Type   | Description                                                    | Default value |
| :---------------------- | :----- | :------------------------------------------------------------- | :------------ |
| **proximityPrecision** | String | One of `byWord` or `byAttribute` | `byWord`      |

#### Example

<CodeSamples id="update_proximity_precision_setting_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset proximity precision

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/proximity-precision"/>

Reset an index's proximity precision setting to the default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_proximity_precision_setting_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Ranking rules

Ranking rules determine the order in which Meilisearch returns results. Ranking rules are applied in a default order which can be changed in the settings. You can add or remove rules and change their order of importance.

[Learn more about ranking rules.](/learn/relevancy/relevancy#ranking-rules)

### Get ranking rules

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/ranking-rules"/>

Get the ranking rules of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_ranking_rules_1" />

##### Response: `200 Ok`

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

### Update ranking rules

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/ranking-rules"/>

Update the ranking rules of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

An array that contains ranking rules in order of importance.

To add your own ranking rule, you have to communicate either `asc` for ascending order or `desc` for descending order followed by the field name in brackets.

- To apply an **ascending sorting** (results sorted by increasing value): `asc(attribute_name)`

- To apply a **descending sorting** (results sorted by decreasing value): `desc(attribute_name)`

[Learn more about ranking rules.](/learn/relevancy/relevancy#ranking-rules)

| Variable         | Type             | Description                                          | Default value                                                                   |
| :--------------- | :--------------- | :--------------------------------------------------- | :------------------------------------------------------------------------------ |
| **rankingRules** | Array of strings | An array of ranking rules in order of importance | [Default order](/learn/relevancy/relevancy#order-of-the-rules) |

#### Example

<CodeSamples id="update_ranking_rules_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset ranking rules

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/ranking-rules"/>

Reset the ranking rules of an index to their default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_ranking_rules_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Search cutoff

Interrupts the search when it takes longer than the provided cutoff value in milliseconds. Meilisearch then returns all documents evaluated so far.

If a search request is interrupted, it does not result in an error. Instead, Meilisearch includes an `estimatedTotalHits` field in the search results.

### Get search cutoff

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/search-cutoff-ms"/>

Get the search cutoff setting of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_search_cutoff_ms_1" />

##### Response: `200 Ok`

```json
null
```

### Update search cutoff

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/search-cutoff-ms"/>

Update the search cutoff setting for an index. Expects an integer or `null`.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

An integer value indicating the cutoff time in milliseconds, or `null`.

| Variable            | Type             | Description                       | Default value |
| :------------------ | :--------------- | :-------------------------------- | :------------ |
| **searchCutoffMs** | Integer / `null` | Search cutoff time in milliseconds | `null`        |

#### Example

<CodeSamples id="update_search_cutoff_ms_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset search cutoff

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/search-cutoff-ms"/>

Reset the search cutoff setting to its default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_search_cutoff_ms_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Searchable attributes

Fields in which Meilisearch searches for matching query words sorted by order of importance.

Adding a field to the `searchableAttributes` list triggers Meilisearch to create the corresponding inverted index, if it doesn't already exist.

[Learn more about searchable attributes.](/learn/fine_tuning_results/displayed_searchable_attributes#searchable-fields)

### Get searchable attributes

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/searchable-attributes"/>

Get the searchable attributes of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_searchable_attributes_1" />

##### Response: `200 Ok`

```json
[
  "*"
]
```

### Update searchable attributes

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/searchable-attributes"/>

Update the searchable attributes of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

An array of strings that contains searchable attributes sorted by order of importance (arranged from the most important attribute to the least important attribute).

| Variable                  | Type             | Description                                                                                       | Default value            |
| :------------------------ | :--------------- | :------------------------------------------------------------------------------------------------ | :----------------------- |
| **searchableAttributes** | Array of strings | Fields in which to search for matching query words (ordered by importance) | `["*"]` (all attributes) |

#### Example

<CodeSamples id="update_searchable_attributes_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset searchable attributes

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/searchable-attributes"/>

Reset the searchable attributes of the index to the default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_searchable_attributes_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Separator tokens

A list of characters and character sequences Meilisearch should treat as word separators. Configuring separator tokens requires setting `separatorTokens` to an array of strings, with each string representing a single separator token.

If multiple separator tokens partially or fully overlap, Meilisearch gives precedence to the longest match. For example, if you set both `:` and `:)` as separator tokens and your dataset contains `:)`, Meilisearch will only split on `:)`.

Separator tokens must be between one and 10 bytes long.

If a character is not included in the `separatorTokens` nor in the `nonSeparatorTokens` list, Meilisearch checks its Unicode category and uses the default behavior.

[Learn more about separator tokens.](/learn/relevancy/language_support#separator-tokens)

### Get separator tokens

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/separator-tokens"/>

Get the separator tokens of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_separator_tokens_1" />

##### Response: `200 Ok`

```json
[]
```

### Update separator tokens

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/separator-tokens"/>

Update the separator tokens of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

An array of strings, with each string indicating a character or sequence of characters to use as word separators.

| Variable             | Type             | Description                                                                           | Default value |
| :------------------- | :--------------- | :------------------------------------------------------------------------------------ | :------------ |
| **separatorTokens** | Array of strings | An array of strings with each string representing a separator | `[]`          |

#### Example

<CodeSamples id="update_separator_tokens_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset separator tokens

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/separator-tokens"/>

Reset the separator tokens of the index to the default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_separator_tokens_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Non-separator tokens

List of characters and character sequences Meilisearch should not treat as word separators. Configuring non-separator tokens requires setting `nonSeparatorTokens` to an array of strings, with each string representing a single non-separator token.

If multiple non-separator tokens partially or fully overlap, Meilisearch gives precedence to the longest match. For example, if you set both `@` and `@+` as non-separator tokens and your dataset contains `@+`, Meilisearch will only match on `@+`.

Non-separator tokens must be between one and 10 bytes long.

If a character is not included in the `nonSeparatorTokens` nor in the `separatorTokens` list, Meilisearch checks its Unicode category and uses the default behavior.

[Learn more about non-separator tokens.](/learn/relevancy/language_support#non-separator-tokens)

### Get non-separator tokens

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/non-separator-tokens"/>

Get the non-separator tokens of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_non_separator_tokens_1" />

##### Response: `200 Ok`

```json
[]
```

### Update non-separator tokens

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/non-separator-tokens"/>

Update the non-separator tokens of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

An array of strings, with each string indicating a character or sequence of characters not to use as word separators.

| Variable                | Type             | Description                                                                     | Default value |
| :---------------------- | :--------------- | :------------------------------------------------------------------------------ | :------------ |
| **nonSeparatorTokens** | Array of strings | An array of strings with each string representing a non-separator | `[]`          |

#### Example

<CodeSamples id="update_non_separator_tokens_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset non-separator tokens

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/non-separator-tokens"/>

Reset the non-separator tokens of the index to the default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_non_separator_tokens_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Dictionary

List of words for which Meilisearch should not perform word segmentation. Configuring `dictionary` requires setting it to an array of strings, with each string representing a single word. Words are not case sensitive.

Use the dictionary to instruct Meilisearch not to split your data's compound words. Some languages, such as German, Swedish, and Dutch, often join smaller words together to create new terms. Since Meilisearch splits words by default, it also segments compound words, which might lead to unexpected or irrelevant search results.

[Learn more about the dictionary setting.](/learn/relevancy/language_support#dictionary)

### Get dictionary

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/dictionary"/>

Get the dictionary setting of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_dictionary_1" />

##### Response: `200 Ok`

```json
[]
```

### Update dictionary

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/dictionary"/>

Update the dictionary setting for an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

An array of strings, each representing a single word Meilisearch should not split. Words are not case sensitive.

| Variable       | Type             | Description                             | Default value |
| :------------- | :--------------- | :-------------------------------------- | :------------ |
| **dictionary** | Array of strings | An array of strings | `[]`          |

#### Example

<CodeSamples id="update_dictionary_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset dictionary

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/dictionary"/>

Reset the dictionary setting to its default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_dictionary_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Sortable attributes

Attributes that can be used when sorting search results with the [`sort` search parameter](/reference/api/search#sort).

[Learn more about sortable attributes.](/learn/filtering_and_sorting/sort_search_results)

### Get sortable attributes

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/sortable-attributes"/>

Get the sortable attributes of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_sortable_attributes_1" />

##### Response: `200 Ok`

```json
[]
```

### Update sortable attributes

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/sortable-attributes"/>

Update the sortable attributes of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

An array of strings containing the attributes that can be used when sorting search results using the [`sort` search parameter](/reference/api/search#sort).

| Variable                | Type             | Description                                                    | Default value |
| :---------------------- | :--------------- | :------------------------------------------------------------- | :------------ |
| **sortableAttributes** | Array of strings | Attributes to use as search parameters when sorting results | `[]`          |

#### Example

<CodeSamples id="update_sortable_attributes_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset sortable attributes

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/sortable-attributes"/>

Reset the sortable attributes of the index to the default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_sortable_attributes_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Stop words

A list of words for which Meilisearch should not return documents matching these terms. Stop words are strongly related to the language used in your dataset. For example, most datasets containing English documents will have countless occurrences of `the` and `of`. Italian datasets, instead, will benefit from ignoring words such as `a` and `che`.

[Learn more about stop words.](/learn/relevancy/stop_words)

### Get stop words

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/stop-words"/>

Get the stop words list of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_stop_words_1" />

##### Response: `200 Ok`

```json
[]
```

### Update stop words

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/stop-words"/>

Update the stop words list of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

An array of strings that contains the stop words.

| Variable      | Type             | Description                                                           | Default value |
| :------------ | :--------------- | :-------------------------------------------------------------------- | :------------ |
| **stopWords** | Array of strings | An array of strings that contains words ignored in search queries | `[]`          |

#### Example

<CodeSamples id="update_stop_words_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset stop words

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/stop-words"/>

Reset the stop words list of an index to its default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_stop_words_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Synonyms

A list of associated words treated similarly by the search engine.

[Learn more about synonyms.](/learn/relevancy/synonyms)

### Get synonyms

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/synonyms"/>

Get the list of synonyms of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_synonyms_1" />

##### Response: `200 Ok`

```json
{}
```

### Update synonyms

<RouteHighlighter method="PUT" path="/indexes/{index_uid}/settings/synonyms"/>

Update the list of synonyms of an index. Synonyms are [normalized](/learn/relevancy/synonyms#normalization).

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

An object that contains all synonyms and their associated words.

| Variable     | Type   | Description                                         | Default value |
| :----------- | :----- | :-------------------------------------------------- | :------------ |
| **synonyms** | Object | An object containing words and their associated synonyms | `{}`          |

#### Example

<CodeSamples id="update_synonyms_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset synonyms

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/synonyms"/>

Reset the list of synonyms of an index to its default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_synonyms_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

---

## Typo tolerance

Typo tolerance helps users find relevant results even when their search queries contain spelling mistakes or typos. This setting allows you to configure the minimum word size for typos and disable typo tolerance for specific words or attributes.

[Learn more about typo tolerance.](/learn/relevancy/typo_tolerance)

### Typo tolerance object

| Variable                                                                        | Type             | Default Value                                    | Description                                                                                  |
| :------------------------------------------------------------------------------ | :--------------- | :----------------------------------------------- | :------------------------------------------------------------------------------------------- |
| **[`enabled`](#typo-tolerance-enabled)**                                        | Boolean          | `true`                                           | Whether typo tolerance is enabled or not                                                     |
| **[`minWordSizeForTypos`](#minimum-word-size-for-typos)**                      | Object           | `{ "oneTypo": 5, "twoTypos": 9 }`                | The minimum word size for accepting typos                                                    |
| **[`minWordSizeForTypos.oneTypo`](#minimum-word-size-for-typos)**              | Integer          | `5`                                              | The minimum word size for accepting 1 typo; must be between `0` and `twoTypos`              |
| **[`minWordSizeForTypos.twoTypos`](#minimum-word-size-for-typos)**             | Integer          | `9`                                              | The minimum word size for accepting 2 typos; must be between `oneTypo` and `255`            |
| **[`disableOnWords`](#disable-typo-tolerance-on-words)**                       | Array of strings | `[]`                                             | An array of words for which typo tolerance is disabled                                       |
| **[`disableOnAttributes`](#disable-typo-tolerance-on-attributes)**             | Array of strings | `[]`                                             | An array of attributes for which typo tolerance is disabled                                  |

### Get typo tolerance settings

<RouteHighlighter method="GET" path="/indexes/{index_uid}/settings/typo-tolerance"/>

Get the typo tolerance settings of an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="get_typo_tolerance_1" />

##### Response: `200 Ok`

```json
{
  "enabled": true,
  "minWordSizeForTypos": {
    "oneTypo": 5,
    "twoTypos": 9
  },
  "disableOnWords": [],
  "disableOnAttributes": []
}
```

### Update typo tolerance settings

<RouteHighlighter method="PATCH" path="/indexes/{index_uid}/settings/typo-tolerance"/>

Partially update the typo tolerance settings for an index.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

| Variable                                                                | Type             | Default Value                         | Description                                                                       |
| :---------------------------------------------------------------------- | :--------------- | :------------------------------------ | :-------------------------------------------------------------------------------- |
| **[`enabled`](#typo-tolerance-enabled)**                                | Boolean          | `true`                                | Whether typo tolerance is enabled or not                                          |
| **[`minWordSizeForTypos`](#minimum-word-size-for-typos)**              | Object           | `{ "oneTypo": 5, "twoTypos": 9 }`     | The minimum word size for accepting typos                                         |
| **[`minWordSizeForTypos.oneTypo`](#minimum-word-size-for-typos)**      | Integer          | `5`                                   | The minimum word size for accepting 1 typo; must be between `0` and `twoTypos`   |
| **[`minWordSizeForTypos.twoTypos`](#minimum-word-size-for-typos)**     | Integer          | `9`                                   | The minimum word size for accepting 2 typos; must be between `oneTypo` and `255` |
| **[`disableOnWords`](#disable-typo-tolerance-on-words)**               | Array of strings | `[]`                                  | An array of words for which typo tolerance is disabled                            |
| **[`disableOnAttributes`](#disable-typo-tolerance-on-attributes)**     | Array of strings | `[]`                                  | An array of attributes for which typo tolerance is disabled                       |

#### Example

<CodeSamples id="update_typo_tolerance_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset typo tolerance settings

<RouteHighlighter method="DELETE" path="/indexes/{index_uid}/settings/typo-tolerance"/>

Reset an index's typo tolerance settings to their default value.

#### Path parameters

| Name              | Type   | Description                                                                                   |
| :---------------- | :----- | :-------------------------------------------------------------------------------------------- |
| **`index_uid`** * | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamples id="reset_typo_tolerance_1" />

##### Response: `202 Accepted`

```json
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Typo tolerance `enabled`

Whether typo tolerance is enabled or not. Setting `enabled` to `false` disables typo tolerance entirely on the specified index. The other typo tolerance settings remain stored and will apply again once typo tolerance is re-enabled.

### Minimum word size for typos

The minimum word size for accepting typos. `minWordSizeForTypos` is an object with two fields:

- `oneTypo`: The minimum size for a word to tolerate one typo; must be between `0` and `twoTypos`
- `twoTypos`: The minimum size for a word to tolerate two typos; must be between `oneTypo` and `255`

### Disable typo tolerance on words

An array of query words for which typo tolerance is disabled. Each string represents a query word: if a search query includes that exact word, Meilisearch will disable typo tolerance for that query word in that specific search.

### Disable typo tolerance on attributes

An array of attributes on which typo tolerance is disabled. If an attribute in this list contains a value matching a query word, Meilisearch will consider the query word as matching even if there are typos.

---

## Embedders

Configure embedders for vector search. Read the [dedicated embedders API reference](/reference/api/embedders) for details on how to use this setting.
