# Handling multilingual datasets

**Source:** https://www.meilisearch.com/docs/learn/indexing/multilingual-datasets.md
**Extrait le:** 2025-10-08
**Sujet:** Learn - Indexing - Multilingual Datasets

---

> This guide covers indexing strategies, language-specific tokenizers, and best practices for aligning document and query tokenization.

When working with datasets that include content in multiple languages, it's important to ensure that both documents and queries are processed correctly. This guide explains how to index and search multilingual datasets in Meilisearch, highlighting best practices, useful features, and what to avoid.

## Recommended indexing strategy

### Create a separate index for each language (recommended)

If you have a multilingual dataset, the best practice is to create one index per language.

#### Benefits

* Provides natural sharding of your data by language, making it easier to maintain and scale.

* Lets you apply language-specific settings, such as [stop words](/reference/api/settings#stop-words), and [separators](/reference/api/settings#separator-tokens).

* Simplifies the handling of complex languages like Chinese or Japanese, which require specialized tokenizers.

#### Searching across languages

If you want to allow users to search in more than one language at once, you can:

* Run a [multi-search](/reference/api/multi_search), querying several indexes in parallel.

* Use [federated search](/reference/api/multi_search#federated-multi-search-requests), aggregating results from multiple language indexes into a single response.

### Create a single index for multiple languages

In some cases, you may prefer to keep multiple languages in a **single index**. This approach is generally acceptable for proof of concepts or datasets with fewer than \~1M documents.

#### When it works well

* Suitable for languages that use spaces to separate words and share similar tokenization behavior (e.g., English, French, Italian, Spanish, Portuguese).

* Useful when you want a simple setup without maintaining multiple indexes.

#### Limitations

* Languages with compound words (like German) or diacritics that change meaning (like Swedish), as well as non-space-separated writing systems (like Chinese, or Japanese), work better in their own index since they require specialized [tokenizers](/learn/indexing/tokenization).

* Chinese and Japanese documents should not be mixed in the same field, since distinguishing between them automatically is very difficult. Each of these languages works best in its own dedicated index. However, if fields are strictly separated by language (e.g., `title_en`, `title_ja`), a single index may still be acceptable.

## Language-specific tokenizers

Meilisearch provides tokenization support for a variety of languages. By default, Meilisearch tries to automatically detect the language and apply appropriate tokenization rules.

### Supported languages

* **Space-separated languages:** English, French, Spanish, Italian, Portuguese, German, Dutch, and many more.

* **Non-space-separated languages:** Chinese (Simplified and Traditional), Japanese, Korean (requires specialized tokenizers).

### Configure tokenization for specific languages

For languages like Chinese and Japanese, you can configure the tokenizer explicitly:

```json
{
  "localizedAttributes": {
    "attributePatterns": [
      {
        "pattern": "*_ja",
        "locales": ["jpn"]
      },
      {
        "pattern": "*_zh",
        "locales": ["cmn"]
      }
    ]
  }
}
```

## Best practices

### Align document and query tokenization

When indexing documents, ensure that the tokenization settings match how users will query the data. If documents are indexed with a specific language tokenizer, queries should use the same settings.

### Use language-specific stop words

For better search relevance, configure [stop words](/reference/api/settings#stop-words) for each language. Stop words are common words (like "the", "a", "is" in English) that can be ignored during indexing and search to improve performance and relevance.

### Test with real-world queries

Always test your multilingual setup with real-world queries to ensure that tokenization, ranking, and filtering work as expected across all languages in your dataset.

### Monitor performance

Large multilingual datasets can impact performance. Monitor your instance and consider:

* Splitting large indexes by language.

* Using [federated search](/reference/api/multi_search#federated-multi-search-requests) to query multiple language indexes efficiently.

## What to avoid

* **Mixing Chinese and Japanese in the same field:** These languages are difficult to distinguish automatically and should be kept in separate fields or indexes.

* **Using a single index for all languages with large datasets:** For datasets with more than \~1M documents, create separate indexes per language for better performance and maintainability.

* **Ignoring language-specific settings:** Always configure stop words, separators, and tokenizers for each language to ensure optimal search quality.

## Further reading

* [Tokenization overview](/learn/indexing/tokenization)
* [Localized attributes](/reference/api/settings#localized-attributes)
* [Multi-search](/reference/api/multi_search)
* [Federated search](/reference/api/multi_search#federated-multi-search-requests)
