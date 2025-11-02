# Typo tolerance calculations

**Source:** https://www.meilisearch.com/docs/learn/relevancy/typo_tolerance_calculations.md
**Extrait le:** 2025-10-08
**Sujet:** Relevancy - Typo Tolerance Calculations

---

# Typo tolerance calculations

> Typo tolerance helps users find relevant results even when their search queries contain spelling mistakes or typos.

Typo tolerance helps users find relevant results even when their search queries contain spelling mistakes or typos, for example, typing `phnoe` instead of `phone`. You can [configure the typo tolerance feature for each index](/reference/api/settings#update-typo-tolerance-settings).

Meilisearch uses a prefix [Levenshtein algorithm](https://en.wikipedia.org/wiki/Levenshtein_distance) to determine if a word in a document could be a possible match for a query term.

The [number of typos referenced above](/learn/relevancy/typo_tolerance_settings#minwordsizefortypos) is roughly equivalent to Levenshtein distance. The Levenshtein distance between two words *M* and *P* can be thought of as "the minimum cost of transforming *M* into *P*" by performing the following elementary operations on *M*:

* substitution of a character (for example, `kitten` → `sitten`)
* insertion of a character (for example, `siting` → `sitting`)
* deletion of a character (for example, `saturday` → `satuday`)

By default, Meilisearch uses the following rules for matching documents. Note that these rules are **by word** and not for the whole query string.

* If the query word is between `1` and `4` characters, **no typo** is allowed. Only documents that contain words that **start with** or are of the **same length** with this query word are considered valid
* If the query word is between `5` and `8` characters, **one typo** is allowed. Documents that contain words that match with **one typo** are retained for the next steps.
* If the query word contains more than `8` characters, we accept a maximum of **two typos**

This means that `saturday` which is `7` characters long, uses the second rule and matches every document containing **one typo**. For example:

* `saturday` is accepted because it is the same word
* `satuday` is accepted because it contains **one typo**
* `sutu` would be rejected because it requires more than one typo to match
