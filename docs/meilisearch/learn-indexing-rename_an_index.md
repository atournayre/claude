# Rename an index

**Source:** https://www.meilisearch.com/docs/learn/indexing/rename_an_index.md
**Extrait le:** 2025-10-08
**Sujet:** Indexing - Renaming indexes

---

# Rename an index

> Use the PATCH endpoint of the /indexes route to rename an index

This guide shows you how to change the name of an index.

## Requirements

* A Meilisearch project with at least one index
* A command-line terminal

## Choose the target index and its new name

Decide which index you want to rename and keep note of its `uid`. This guide changes the name of an index called  `INDEX_A`.

Also choose the new name you wish to assign the index. This guide uses `INDEX_B` for the new name of the index.

## Query the `/indexes/{index_uid}` route

Send a `PATCH` request targeting the index you want to rename:

<CodeGroup>
  ```bash cURL
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/INDEX_A' \
    -H 'Content-Type: application/json' \
    --data-binary '{ "uid": "INDEX_B" }'
  ```

  ```rust Rust
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/INDEX_A' \
    -H 'Content-Type: application/json' \
    --data-binary '{ "uid": "INDEX_B" }'
  ```
</CodeGroup>

Replace `INDEX_A` with the current name of your index, and `INDEX_B` with its new name.
