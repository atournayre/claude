# Error codes

**Source:** https://www.meilisearch.com/docs/reference/errors/error_codes.md
**Extrait le:** 2025-10-08
**Sujet:** Reference - Error codes

---

> Consult this page for an exhaustive list of errors you may encounter when using the Meilisearch API.

This page is an exhaustive list of Meilisearch API errors.

## `api_key_already_exists`

A key with this [`uid`](/reference/api/keys#uid) already exists.

## `api_key_not_found`

The requested API key could not be found.

## `bad_request`

The request is invalid, check the error message for more information.

## `database_size_limit_reached`

The database size limit has been reached. Consult the [database size limit documentation](/learn/advanced/database_size_limit) for more information.

## `document_fields_limit_reached`

Document fields limit reached. Maximum is 65535.

## `document_not_found`

The requested document could not be found.

## `dump_already_processing`

A dump is already being processed. Please wait until it finishes before creating a new one.

## `dump_not_found`

The requested dump could not be found.

## `duplicate_index_found`

Two indexes were found with the same uid.

## `immutable_api_key_actions`

The `actions` field of an API key cannot be modified.

## `immutable_api_key_created_at`

The `createdAt` field of an API key cannot be modified.

## `immutable_api_key_expires_at`

The `expiresAt` field of an API key cannot be modified.

## `immutable_api_key_indexes`

The `indexes` field of an API key cannot be modified.

## `immutable_api_key_key`

The `key` field of an API key cannot be modified.

## `immutable_api_key_uid`

The `uid` field of an API key cannot be modified.

## `immutable_api_key_updated_at`

The `updatedAt` field of an API key cannot be modified.

## `immutable_field`

The given field cannot be modified.

## `immutable_index_created_at`

The `createdAt` field of an index cannot be modified.

## `immutable_index_uid`

The `uid` field of an index cannot be modified.

## `immutable_index_updated_at`

The `updatedAt` field of an index cannot be modified.

## `index_already_exists`

An index with this [`uid`](/reference/api/indexes#uid) already exists.

## `index_creation_failed`

An internal error occurred while creating the index.

## `index_not_found`

The requested index could not be found.

## `index_primary_key_already_exists`

The primary key inference process already found a primary key for this index. If you want to change it, you must delete the index and recreate it.

## `index_primary_key_multiple_candidates_found`

The primary key inference process failed because the engine found multiple fields ending with `id` in their name. You must specify the primary key manually using the [`primaryKey` parameter](/reference/api/indexes#index-object).

## `index_primary_key_no_candidate_found`

The primary key inference process failed because the engine did not find any field ending with `id` in its name. You must specify the primary key manually using the [`primaryKey` parameter](/reference/api/indexes#index-object).

## `internal_error`

Meilisearch experienced an internal error. Check the error message for more information.

## `invalid_api_key`

The requested API key is invalid. Most likely, the key does not exist or does not have the proper permissions.

## `invalid_api_key_actions`

The `actions` field of an API key is invalid. It must be an array of strings.

## `invalid_api_key_description`

The `description` field of an API key is invalid. It must be a string or null.

## `invalid_api_key_expires_at`

The `expiresAt` field of an API key is invalid. It must be in the ISO 8601 format (e.g. `2021-12-31T23:59:59Z`) or null.

## `invalid_api_key_indexes`

The `indexes` field of an API key is invalid. It must be an array of strings representing index `uids`.

## `invalid_api_key_limit`

The `limit` query parameter is invalid. It must be an integer.

## `invalid_api_key_name`

The `name` field of an API key is invalid. It must be a string.

## `invalid_api_key_offset`

The `offset` query parameter is invalid. It must be an integer.

## `invalid_api_key_uid`

The `uid` field of an API key is invalid. It must be a valid v4 UUID string or null.

## `invalid_content_type`

The `Content-Type` header is invalid. Consult the [API reference](/reference/api/overview) for more information.

## `invalid_document_csv_delimiter`

The `csvDelimiter` query parameter is invalid. It must be a single ASCII character.

## `invalid_document_fields`

Some document fields are invalid. Check the error message for more information.

## `invalid_document_filter`

The document filter is invalid. Check the error message for more information.

## `invalid_document_geo_field`

The `_geo` field is invalid. It must be an object with `lat` and `lng` numeric properties.

## `invalid_document_id`

The document identifier is invalid. It must be an integer or a string.

## `invalid_document_limit`

The `limit` query parameter is invalid. It must be an integer.

## `invalid_document_offset`

The `offset` query parameter is invalid. It must be an integer.

## `invalid_facet_search_facet_name`

The `facetName` parameter is invalid. It must be a string.

## `invalid_facet_search_name`

The facet name in the facet search request is invalid. Check the error message for more information.

## `invalid_index_limit`

The `limit` query parameter is invalid. It must be an integer.

## `invalid_index_offset`

The `offset` query parameter is invalid. It must be an integer.

## `invalid_index_primary_key`

The primary key is invalid. It must be a string or null.

## `invalid_index_uid`

The index `uid` is invalid. It must be a string containing only alphanumeric characters, hyphens, and underscores. The `uid` must not be empty and must not exceed 512 bytes in length.

## `invalid_ranking_rules`

The `rankingRules` setting is invalid. It must be an array of strings representing valid ranking rules.

## `invalid_search_attributes_to_crop`

The `attributesToCrop` search parameter is invalid. It must be an array of strings or `["*"]`.

## `invalid_search_attributes_to_highlight`

The `attributesToHighlight` search parameter is invalid. It must be an array of strings or `["*"]`.

## `invalid_search_attributes_to_retrieve`

The `attributesToRetrieve` search parameter is invalid. It must be an array of strings or `["*"]`.

## `invalid_search_crop_length`

The `cropLength` search parameter is invalid. It must be an integer.

## `invalid_search_crop_marker`

The `cropMarker` search parameter is invalid. It must be a string.

## `invalid_search_facets`

The `facets` search parameter is invalid. It must be an array of strings.

## `invalid_search_filter`

The `filter` search parameter is invalid. Check the error message for more information.

## `invalid_search_highlight_post_tag`

The `highlightPostTag` search parameter is invalid. It must be a string.

## `invalid_search_highlight_pre_tag`

The `highlightPreTag` search parameter is invalid. It must be a string.

## `invalid_search_hits_per_page`

The `hitsPerPage` search parameter is invalid. It must be an integer between 1 and 1000.

## `invalid_search_limit`

The `limit` search parameter is invalid. It must be an integer between 0 and 1000.

## `invalid_search_matching_strategy`

The `matchingStrategy` search parameter is invalid. It must be either `all` or `last`.

## `invalid_search_offset`

The `offset` search parameter is invalid. It must be an integer between 0 and 1000.

## `invalid_search_page`

The `page` search parameter is invalid. It must be an integer greater than or equal to 1.

## `invalid_search_q`

The `q` search parameter is invalid. It must be a string.

## `invalid_search_show_matches_position`

The `showMatchesPosition` search parameter is invalid. It must be a boolean.

## `invalid_search_sort`

The `sort` search parameter is invalid. It must be an array of strings.

## `invalid_settings_displayed_attributes`

The `displayedAttributes` setting is invalid. It must be an array of strings or `["*"]`.

## `invalid_settings_distinct_attribute`

The `distinctAttribute` setting is invalid. It must be a string or null.

## `invalid_settings_faceting`

The `faceting` setting is invalid. Check the error message for more information.

## `invalid_settings_filterable_attributes`

The `filterableAttributes` setting is invalid. It must be an array of strings.

## `invalid_settings_pagination`

The `pagination` setting is invalid. Check the error message for more information.

## `invalid_settings_ranking_rules`

The `rankingRules` setting is invalid. It must be an array of strings representing valid ranking rules.

## `invalid_settings_searchable_attributes`

The `searchableAttributes` setting is invalid. It must be an array of strings or `["*"]`.

## `invalid_settings_sortable_attributes`

The `sortableAttributes` setting is invalid. It must be an array of strings.

## `invalid_settings_stop_words`

The `stopWords` setting is invalid. It must be an array of strings.

## `invalid_settings_synonyms`

The `synonyms` setting is invalid. It must be an object where keys and values are arrays of strings.

## `invalid_settings_typo_tolerance`

The `typoTolerance` setting is invalid. Check the error message for more information.

## `invalid_swap_duplicate_index_found`

Two indexes with the same `uid` were specified in the swap operation.

## `invalid_swap_indexes`

The swap indexes operation is invalid. It must be an array of objects with `indexes` array containing exactly two index `uids`.

## `invalid_task_after_enqueued_at`

The `afterEnqueuedAt` query parameter is invalid. It must be in the ISO 8601 format.

## `invalid_task_after_finished_at`

The `afterFinishedAt` query parameter is invalid. It must be in the ISO 8601 format.

## `invalid_task_after_started_at`

The `afterStartedAt` query parameter is invalid. It must be in the ISO 8601 format.

## `invalid_task_before_enqueued_at`

The `beforeEnqueuedAt` query parameter is invalid. It must be in the ISO 8601 format.

## `invalid_task_before_finished_at`

The `beforeFinishedAt` query parameter is invalid. It must be in the ISO 8601 format.

## `invalid_task_before_started_at`

The `beforeStartedAt` query parameter is invalid. It must be in the ISO 8601 format.

## `invalid_task_canceled_by`

The `canceledBy` query parameter is invalid. Check the error message for more information.

## `invalid_task_index_uids`

The `indexUids` query parameter is invalid. It must be an array of strings.

## `invalid_task_limit`

The `limit` query parameter is invalid. It must be an integer.

## `invalid_task_statuses`

The `statuses` query parameter is invalid. It must be an array of valid task statuses.

## `invalid_task_types`

The `types` query parameter is invalid. It must be an array of valid task types.

## `invalid_task_uids`

The `uids` query parameter is invalid. It must be an array of integers or a comma-separated list.

## `io_error`

Meilisearch experienced an I/O error. Check the error message for more information.

## `malformed_payload`

The request payload is malformed. Check the error message for more information.

## `missing_api_key_actions`

The `actions` field is required when creating an API key.

## `missing_api_key_expires_at`

The `expiresAt` field is required when creating an API key.

## `missing_api_key_indexes`

The `indexes` field is required when creating an API key.

## `missing_authorization_header`

The `Authorization` header is missing. Most likely, you forgot to add your API key to the request.

## `missing_content_type`

The `Content-Type` header is missing.

## `missing_document_id`

Document identifier is missing. Check the error message for more information.

## `missing_index_uid`

The index `uid` is missing.

## `missing_master_key`

The master key is missing. You must set the `MEILI_MASTER_KEY` environment variable. Consult the [security documentation](/learn/security/master_api_keys) for more information.

## `missing_payload`

The request payload is missing.

## `missing_swap_indexes`

The swap indexes operation requires an array of objects with `indexes` field.

## `missing_task_filters`

You must specify at least one filter to cancel or delete tasks. Consult the [task documentation](/reference/api/tasks) for more information.

## `no_space_left_on_device`

There is no more space left on the device. Consult the [database size limit documentation](/learn/advanced/database_size_limit) for more information.

## `not_found`

The requested resource could not be found.

## `payload_too_large`

The request payload is too large. The maximum payload size is 100MB.

## `task_not_found`

The requested task could not be found.

## `too_many_open_files`

There are too many open files. This usually occurs because the system has reached its limit of open file descriptors.

## `unretrievable_document`

The document could not be retrieved. Check the error message for more information.

## `unretrievable_error_code`

The error code could not be retrieved.

## `unsupported_media_type`

The media type specified in the `Content-Type` header is not supported. Consult the [API reference](/reference/api/overview) for more information.
