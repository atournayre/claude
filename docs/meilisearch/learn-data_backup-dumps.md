# Exporting and importing dumps

**Source:** https://www.meilisearch.com/docs/learn/data_backup/dumps.md
**Extrait le:** 2025-10-08
**Sujet:** Data Backup - Dumps

---

# Exporting and importing dumps

> Dumps are data backups containing all data related to a Meilisearch instance. They are often useful when migrating to a new Meilisearch release.

A [dump](/learn/data_backup/snapshots_vs_dumps#dumps) is a compressed file containing an export of your Meilisearch instance. Use dumps to migrate to new Meilisearch versions. This tutorial shows you how to create and import dumps.

Creating a dump is also referred to as exporting it. Launching Meilisearch with a dump is referred to as importing it.

## Creating a dump

### Creating a dump in Meilisearch Cloud

**You cannot manually export dumps in Meilisearch Cloud**. To [migrate your project to the most recent Meilisearch release](/learn/update_and_migration/updating), use the Cloud interface:

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-dumps/01-export-dump.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=a7bf333c25efde3ce77440665a198ebe" alt="The General settings interface displaying various data fields relating to a Meilisearch Cloud project. One of them reads 'Meilisearch version'. Its value is 'v1.6.2'. Next to the value is a button 'Update to v1.7.0'" data-og-width="1304" width="1304" data-og-height="467" height="467" data-path="assets/images/cloud-dumps/01-export-dump.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-dumps/01-export-dump.png?w=280&fit=max&auto=format&n=kYJO98Uevt3SrL
