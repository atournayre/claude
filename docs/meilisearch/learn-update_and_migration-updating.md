# Update to the latest Meilisearch version

**Source:** https://www.meilisearch.com/docs/learn/update_and_migration/updating.md
**Extrait le:** 2025-10-08
**Sujet:** Update and Migration - Updating Meilisearch

---

# Update to the latest Meilisearch version

> Learn how to migrate to the latest Meilisearch release.

export const NoticeTag = ({label}) => <span className="noticeTag noticeTag--{ label }">
    {label}
  </span>;

Currently, Meilisearch databases are only compatible with the version of Meilisearch used to create them. The following guide will walk you through using a [dump](/learn/data_backup/dumps) to migrate an existing database from an older version of Meilisearch to the most recent one.

If you're updating your Meilisearch instance on cloud platforms like DigitalOcean or AWS, ensure that you can connect to your cloud instance via SSH. Depending on the user you are connecting with (root, admin, etc.), you may need to prefix some commands with `sudo`.

If migrating to the latest version of Meilisearch will cause you to skip multiple versions, this may require changes to your codebase. [Refer to our version-specific update warnings for more details](#version-specific-warnings).

<Tip>
  If you are running Meilisearch as a `systemctl` service using v0.22 or above, try our [migration script](https://github.com/meilisearch/meilisearch-migration).
</Tip>

## Update Meilisearch with a dump

### 1. Verify the current Meilisearch version

First, verify the version of the Meilisearch instance you are currently using. You can check this with the [get version endpoint](/reference/api/version#get-version):

```bash
curl http://localhost:7700/version
```

You should get a response like this:

```json
{
  "commitSha":"b46889b5f0f2f8b91438a08a358ba8f05fc09fc1",
  "commitDate":"2019-11-15T09:51:54.278977+00:00",
  "pkgVersion":"0.1.1"
}
```

### 2. Create a dump

<Tip>
If you are using a version of Meilisearch **below v0.15**, you must first upgrade to v0.21 by following the same process described below.
</Tip>

<Warning>
Creating a dump might take some time to complete depending on the size of your dataset.
</Warning>

<Tabs.Container labels={["Local", "Cloud"]}>
  <Tabs.Content label="Local">

Use the [create a dump endpoint](/reference/api/dump#create-a-dump):

```bash
curl \
  -X POST 'http://localhost:7700/dumps'
```

The above code triggers a dump creation process. Creating a dump can take some time to complete.

Once the dump creation process is complete, the dump file is generated in the dump directory.

By default, this folder is `/dumps` at the root of your Meilisearch directory.

The generated dump file has the following format: `YYYYMMDD-hhmmss.dump`.

  </Tabs.Content>
  <Tabs.Content label="Cloud">

**Important**: For Meilisearch Cloud users, contact [our support team](mailto:cloud@meilisearch.com) and we will take care of the migration for you.

  </Tabs.Content>
</Tabs.Container>

### 3. Download the latest Meilisearch version

<Warning>
Before migrating your dump, make sure you have properly backed up your old database.
</Warning>

After [downloading and launching](/learn/getting_started/installation) the latest version of Meilisearch, first verify that the upload was successful:

```bash
curl http://localhost:7700/version
```

You should receive a response similar to this:

```json
{
  "commitSha":"b46889b5f0f2f8b91438a08a358ba8f05fc09fc1",
  "commitDate":"2019-11-15T09:51:54.278977+00:00",
  "pkgVersion":"0.30.0"
}
```

### 4. Import the dump

To import the dump into the new Meilisearch version, use the [`--import-dump` command-line option](/learn/configuration/instance_options#import-dump):

<Tabs.Container labels={["macOS / Linux", "Windows"]}>
  <Tabs.Content label="macOS / Linux">

```bash
./meilisearch --import-dump /dumps/your_dump_file.dump
```

  </Tabs.Content>
  <Tabs.Content label="Windows">

```bash
meilisearch.exe --import-dump /dumps/your_dump_file.dump
```

  </Tabs.Content>
</Tabs.Container>

Once the import process is complete, your existing data has been migrated into the latest version of Meilisearch.

<Warning>
Do not use the Meilisearch instance while the dump importing is in progress. If you use the instance during this process, you will receive `no-space-left-on-device` errors.
</Warning>

<Capsule intent="tip" title="Want to automate the migration process?">
  You can also choose to automate this process. In order to do this, configure the new installation to [import a dump at launch](/learn/configuration/instance_options#import-dump) and [ignore a missing dump file](/learn/configuration/instance_options#ignore-missing-dump) if it doesn't exist in the specified folder.
</Capsule>

## Version-specific warnings

Depending on which versions of Meilisearch you are migrating between, you may need to alter your application code or dumps might not be compatible.

### Coming from v0.29 or below

#### Soft-deleted documents

If you are running v0.30, [soft-deleted documents](/learn/documents/delete_documents#about-document-deletion) are now permanently deleted when a dump is imported.

### Coming from v0.27 or below

#### Changes to the `attributes` prefix in the `filter` search parameter

If you are using the `_geoRadius` built-in filter rule, you must update it to `_geoRadius()` for versions v0.28.0 and above.

#### Changes to the `filter` search parameter

If you were using ` ` (whitespace) to separate OR operations, you must replace it with a comma (`,`) for versions v0.28.0 and above.

For example, replace `"thriller horror romance"` with `"thriller, horror, romance"`.

### Coming from v0.24 or below

#### Changes to `sortableAttributes`

The `attributesForFaceting` index setting is replaced by `filterableAttributes` for all Meilisearch versions above v0.25.0. If you were using `attributesForFaceting` to make facets searchable and not for filtering, you should use the `sortableAttributes` setting instead.

### Coming from v0.21 or below

#### Changes to ranking rules and `frenchStopWords`

If you're currently using a version of Meilisearch below v0.21, the dump taken with these versions cannot be imported in a higher version.

In order to migrate, you must first upgrade your Meilisearch instance to v0.21 using the same process, then do another migration to v0.30.

### Coming from v0.20 or below

#### Changes to language support

If you're currently using a version of Meilisearch below v0.20, note that the default language for Meilisearch was French. Since v0.20, English is the new default language.

Depending on your database content, the search results might be slightly different after migration.

#### Changes to the `/indexes` API endpoint

The create index endpoint no longer requires `uid` in the request body.

```bash
curl \
  -X POST 'http://localhost:7700/indexes' \
  --data '{ "uid": "movies" }'
```

Instead, you should now include the `uid` in the endpoint:

```bash
curl \
  -X POST 'http://localhost:7700/indexes/movies'
```

### Coming from v0.15 or below

If you are currently using Meilisearch v0.15 or below, this version is not compatible with the latest version of Meilisearch.

The dumps from these versions are also not compatible, which means that dumps from v0.15 cannot be imported into latest version.

#### Solution

If you are using a version below or equal to v0.15, you must update your Meilisearch instance to v0.21 first by following this guide. Then, go through the process once more to update from v0.21 to latest version.
