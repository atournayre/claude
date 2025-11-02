# Filter expression reference

**Source:** https://www.meilisearch.com/docs/learn/filtering_and_sorting/filter_expression_reference.md
**Extrait le:** 2025-10-08
**Sujet:** Learn - Filtering and Sorting - Filter Expression Reference

---

> The `filter` search parameter expects a filter expression. Filter expressions are made of attributes, values, and several operators.

export const NoticeTag = ({label}) => <span className="noticeTag noticeTag--{ label }">
    {label}
  </span>;

The `filter` search parameter expects a filter expression. Filter expressions are made of attributes, values, and several operators.

`filter` expects a **filter expression** containing one or more **conditions**. A filter expression can be written as a string, array, or mix of both.

## Data types

Filters accept numeric and string values. Empty fields or fields containing an empty array will be ignored.

Filters do not work with [`NaN`](https://en.wikipedia.org/wiki/NaN) and infinite values such as `inf` and `-inf` as they are [not supported by JSON](https://en.wikipedia.org/wiki/JSON#Data_types). It is possible to filter infinite and `NaN` values if you parse them as strings, except when handling [`_geo` fields](/learn/filtering_and_sorting/geosearch#preparing-documents-for-location-based-search).

<Warning>
  For best results, enforce homogeneous typing across fields, especially when dealing with large numbers. Meilisearch does not enforce a specific schema when indexing data, but the filtering engine may coerce the type of `value`. This can lead to undefined behavior, such as when big floating-point numbers are coerced into integers.
</Warning>

## Conditions

Conditions are a filter's basic building blocks. They are written in the `attribute OPERATOR value` format, where:

* `attribute` is the attribute of the field you want to filter on
* `OPERATOR` can be `=`, `!=`, `>`, `>=`, `<`, `<=`, `TO`, `EXISTS`, `IN`, `NOT`, `AND`, or `OR`
* `value` is the value the `OPERATOR` should look for in the `attribute`

### Examples

A basic condition requesting movies whose `genres` attribute is equal to `horror`:

```
genres = horror
```

String values containing whitespace must be enclosed in single or double quotes:

```
director = 'Jordan Peele'
```