# Language

**Source:** https://www.meilisearch.com/docs/learn/resources/language.md
**Extrait le:** 2025-10-08
**Sujet:** Learn - Resources - Language Support

---

# Language

> Meilisearch is compatible with datasets in any language. Additionally, it features optimized support for languages using whitespace to separate words, Chinese, Hebrew, Japanese,  Korean, and Thai.

Meilisearch is multilingual, featuring optimized support for:

* Any language that uses whitespace to separate words
* Chinese
* Hebrew
* Japanese
* Khmer
* Korean
* Swedish
* Thai

We aim to provide global language support, and your feedback helps us move closer to that goal. If you notice inconsistencies in your search results or the way your documents are processed, please [open an issue in the Meilisearch repository](https://github.com/meilisearch/meilisearch/issues/new/choose).

[Read more about our tokenizer](/learn/indexing/tokenization)

## Improving our language support

While we have employees from all over the world at Meilisearch, we don't speak every language. We rely almost entirely on feedback from external contributors to understand how our engine is performing across different languages.

If you'd like to request optimized support for a language, please upvote the related [discussion in our product repository](https://github.com/meilisearch/product/discussions?discussions_q=label%3Ascope%3Atokenizer+) or [open a new one](https://github.com/meilisearch/product/discussions/new?category=feedback-feature-proposal) if it doesn't exist.

If you'd like to help by developing a tokenizer pipeline yourself: first of all, thank you! We recommend that you take a look at the [tokenizer contribution guide](https://github.com/meilisearch/charabia/blob/main/CONTRIBUTING.md) before making a PR.

## FAQ

### What do you mean when you say Meilisearch offers *optimized* support for a language?

Optimized support for a language means Meilisearch has implemented internal processes specifically tailored to parsing that language, leading to more relevant results.

### My language does not use whitespace to separate words. Can I still use Meilisearch?

Yes, but search results might be less relevant than in one of the fully optimized languages.

### My language does not use the Roman alphabet. Can I still use Meilisearch?

Yes! Meilisearch supports all alphabets and character sets.
