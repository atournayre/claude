# Migrating to Meilisearch Cloud

**Source:** https://www.meilisearch.com/docs/learn/update_and_migration/migrating_cloud.md
**Extrait le:** 2025-10-08
**Sujet:** Update and Migration - Migrating to Cloud

---

# Migrating to Meilisearch Cloud — Meilisearch Documentation

> Meilisearch Cloud is the recommended way of using Meilisearch. This guide walks you through migrating Meilisearch from a self-hosted installation to Meilisearch Cloud.

Meilisearch Cloud is the recommended way of using Meilisearch. This guide walks you through migrating Meilisearch from a self-hosted installation to Meilisearch Cloud.

## Requirements

To follow this guide you need:

* A running Meilisearch instance
* A command-line terminal
* A Meilisearch Cloud account

## Export a dump from your self-hosted installation

To migrate Meilisearch, you must first [export a dump](/learn/data_backup/dumps). A dump is a compressed file containing all your indexes, documents, and settings.

To export a dump, make sure your self-hosted Meilisearch instance is running. Then, open your terminal and run the following command, replacing `MEILISEARCH_URL` with your instance's address:

```sh
curl -X POST 'MEILISEARCH_URL:7700/dumps'
```

Meilisearch will return a summarized task object and begin creating the dump. [Use the returned object's `taskUid` to monitor its progress.](/learn/async/asynchronous_operations)

Once the task has been completed, you can find the dump in your project's dump directory. By default, this is `/dumps`.

<Note>
  Instance configuration options and experimental features that can only be activated at launch are not included in dumps.

  Once you have successfully migrated your data to Meilisearch Cloud, use the project overview interface to reactivate available options. Not all instance options are supported in the Cloud.
</Note>

## Create a Meilisearch Cloud project and import dump

Navigate to Meilisearch Cloud in your browser and log in. If you don't have a Meilisearch Cloud account yet, [create one for free](https://cloud.meilisearch.com/register?utm_campaign=oss\&utm_source=docs\&utm_medium=migration-guide).

You can only import dumps into new Meilisearch Cloud projects. Once you have created a project, you can import your dump during the project creation process or from the project overview page.
