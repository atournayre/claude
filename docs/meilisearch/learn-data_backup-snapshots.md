# Exporting and using Snapshots

**Source:** https://www.meilisearch.com/docs/learn/data_backup/snapshots.md
**Extrait le:** 2025-10-08
**Sujet:** Data Backup - Snapshots

---

# Exporting and using Snapshots

> Snapshots are exact copies of Meilisearch databases. They are often useful for periodical backups.

A [snapshot](/learn/data_backup/snapshots_vs_dumps#snapshots) is an exact copy of the Meilisearch database. Snapshots are useful as quick backups, but cannot be used to migrate to a new Meilisearch release.

This tutorial shows you how to schedule snapshot creation to ensure you always have a recent backup of your instance ready to use. You will also see how to start Meilisearch from this snapshot.

<Warning>
  Meilisearch Cloud does not support snapshots.
</Warning>

## Scheduling periodic snapshots

It is good practice to create regular backups of your Meilisearch data. This ensures that you can recover from critical failures quickly in case your Meilisearch instance becomes compromised.

Use the [`--schedule-snapshot` configuration option](/learn/self_hosted/configure_meilisearch_at_launch#schedule-snapshot-creation) to create snapshots at regular time intervals:

```bash
meilisearch --schedule-snapshot
```

The first snapshot is created on launch. You will find it in the [snapshot directory](/learn/self_hosted/configure_meilisearch_at_launch#snapshot-destination), `/snapshots`. Meilisearch will then create a new snapshot every 24 hours until you terminate your instance.

Meilisearch **automatically overwrites** old snapshots during snapshot creation. Only the most recent snapshot will be present in the folder at any given time.

In cases where your database is updated several times a day, it might be better to modify the interval between each new snapshot:

```bash
meilisearch --schedule-snapshot=3600
```

This instructs Meilisearch to create a new snapshot once every hour.

<Tip>
  If you need to generate a single snapshot without relaunching your instance, use [the `/snapshots` route](/reference/api/snapshots).
</Tip>

## Starting from a snapshot

To import snapshot data into your instance, launch Meilisearch using `--import-snapshot`:

```bash
meilisearch --import-snapshot mySnapshot
```

This command imports data from `mySnapshot` into your Meilisearch instance.
