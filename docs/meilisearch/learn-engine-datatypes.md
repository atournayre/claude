# Data types

**Source:** https://www.meilisearch.com/docs/learn/engine/datatypes.md
**Extrait le:** 2025-10-08
**Sujet:** Engine - Data Types

---

# Data types

> Learn about how Meilisearch handles different data types: strings, numerical values, booleans, arrays, and objects.

This article explains how Meilisearch handles the different types of data in your dataset.

**The behavior described here concerns only Meilisearch's internal processes** and can be helpful in understanding how the tokenizer works. Document fields remain unchanged for most practical purposes not related to Meilisearch's inner workings.

## String

String is the primary type for indexing data in Meilisearch. It enables to create the content in which to search. Strings are processed as detailed below.

String tokenization is the process of **splitting a string into a list of individual terms that are called tokens.**

A string is passed to a tokenizer and is then broken into separate string tokens. A token is a **word**.

### Tokenization

Tokenization relies on two main processes to identifying words and separating them into tokens: separators and dictionaries.

#### Separators

Separators are characters that indicate where one word ends and another word begins. In languages using the Latin alphabet, for example, words are usually delimited by white space. In Japanese, word boundaries are more commonly indicated in other ways, such as appending particles like `に` and `で` to the end of a word.

There are two kinds of separators in Meilisearch: soft and hard. Hard separators signal a significant context switch such as a new sentence or paragraph. Soft separators only delimit one word from another but do not imply a major change of subject.

The list below presents some of the most common separators in languages using the Latin alphabet:

* **Soft spaces** (distance: 1): whitespaces, quotes, `'-' | '_' | '\'' | ':' | '/' | '\\' | '@' | '"' | '+' | '~' | '=' | '^' | '*' | '#'`
* **Hard spaces** (distance: 8): `'.' | ';' | ',' | '!' | '?' | '(' | ')' | '[' | ']' | '{' | '}'| '|'`

For more separators, including those used in other writing systems like Cyrillic and Thai, [consult this exhaustive list](https://github.com/meilisearch/charabia/tree/main/charabia/src/separators).

**Distance** is a value used for proximity ranking. Hard separators have a distance of 8, as opposed to soft separators' distance of 1.

##### Example

If your search query is `hello world`, Meilisearch will take this into account when calculating each result's relevancy scores: it will assume that terms separated by hard separators are less likely to be meaningfully related than terms separated only by soft separators.

Let's say you have one document with `hello` and `world` separated by a soft separator and another with the same terms separated by a hard separator. The first one will be considered more relevant.

```json
[
  {
    "id": 1,
    "text": "hello world" // Returned first
  },
  {
    "id": 2,
    "text": "hello. world" // Returned second
  }
]
```

#### Dictionary

When looking for separators, Meilisearch also checks whether characters or sequences of characters match terms in one of its included dictionaries. This is especially useful for handling Chinese characters, which require different word-splitting techniques.

Currently, Meilisearch supports dictionaries for Chinese (Simplified and Traditional, via the [jieba project](https://github.com/messense/jieba-rs)) and Japanese (via the [lindera project](https://github.com/lindera-morphology/lindera)).

##### Example

```json
{
  "id": 1,
  "text": "罗密欧与朱丽叶是伟大的戏剧"
}
```

The document's `text` field is detected as Simplified Chinese. Meilisearch then uses [jieba](https://github.com/messense/jieba-rs)'s dictionary to separate individual tokens:

```
罗密欧 | 与 | 朱丽叶 | 是 | 伟大 | 的 | 戏剧
```

### Phrase search

By default, Meilisearch treats multiple search terms as a single search. When searching for `"the great gatsby"`, Meilisearch returns all results containing all three terms.

If you enclose search terms in double quotes, Meilisearch only returns results where the queried words appear in the same order with no other words in between. When searching for `"\"the great gatsby\""`, results must contain the words `the`, `great`, and `gatsby` sequentially and with no separating terms.

For more information, consult the [phrase search reference](/reference/api/search#phrase-search).

## Numeric

A numeric type (`integer`, `float`) is converted to a human-readable decimal number string representation.

For example, if a field has a numeric value, for example: `"count": 32`, it will be converted into: `"count": "32"`.

You can also pass numerical values as strings. `"count": "32"` is valid and will be processed as a number.

[You can use numeric fields for filtering data.](/learn/filtering_and_sorting/filter_search_results)

## Boolean

A Boolean value (`true` / `false`) is converted to a lowercase human-readable text representation.

```json
{
  "id": 1,
  "isActive": true
}
```

The value `true` of the field `isActive` will be processed as the string `"true"`. This means you can search for documents containing `true` and Meilisearch will return `"id": 1`.

[You can use boolean fields for filtering data.](/learn/filtering_and_sorting/filter_search_results)

## Array

An array is a **recursive data-type**, meaning that arrays of strings follow string rules and arrays of numbers follow numeric rules. Also, note that **Meilisearch does not support nested arrays**.

```json
{
  "id": 1,
  "labels": ["2022", "horror", "bestseller"],
  "description": "After a deadly virus strikes, one man must save the human race from zombies."
}
```

If you search for `horror 2022`, the document above would be a valid result and the search terms would be considered separate.

However, if you search for `"horror 2022"` (enclosed in double quotes), Meilisearch will perform a phrase search. In this case, the document would not be returned, since `horror` and `2022` are separate values in an array.

## Object

A JSON object is a **recursive data-type**. When the engine encounters objects during indexing, their keys are flattened, creating a nested structure.

```json
{
  "id": 1,
  "person": {
    "name": "Jimmy",
    "age": "25"
  }
}
```

The `person` field's object will be flattened and processed as: `"person.name": "Jimmy"` and `"person.age": "25"`.

You can query nested fields by using dot notation: `person.name:Jimmy`. You may also [configure nested fields as `searchableAttributes`](/learn/relevancy/displayed_searchable_attributes#searchable-fields) and [`filterableAttributes`](/learn/filtering_and_sorting/filter_search_results#configuring-filters).

## `null`

A `null` value is represented by the absence of a value.

For example, a document containing an attribute with a `null` value:

```json
{
  "id": 0,
  "color": null
}
```

will be processed as if the attribute did not exist at all:

```json
{
  "id": 0
}
```

Both `"color": null` and `"color": [null]` will be handled the same way.

## Summary

To summarize, the following table shows how each type is processed:

| Type                           | Representation                    | Example                   |
|--------------------------------|-----------------------------------|---------------------------|
| String                         | String                            | `"hello world"`           |
| Integer                        | Number as string                  | `"1254"`                  |
| Float                          | Number as string                  | `"1.254"`                 |
| Boolean                        | Boolean as lowercase string       | `"true"`                  |
| Array of strings               | Array of strings                  | `["Horror", "Comedy"]`    |
| Array of numbers               | Array of numbers as strings       | `["1", "2"]`              |
| Object                         | Flattened object, dot-separated   | `"person.name": "Jimmy"`  |
| Array of objects               | Array of flattened objects        | `"person.name": ["Jimmy", "Kimmy"]` |
| `null`                         | Absence of value                  | (field is not indexed)    |
