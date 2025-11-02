# Storage

**Source:** https://www.meilisearch.com/docs/learn/engine/storage.md
**Extrait le:** 2025-10-08
**Sujet:** Engine - Storage

---

# Storage

> Learn about how Meilisearch stores and handles data in its LMDB storage engine.

Meilisearch is in many ways a database: it stores indexed documents along with the data needed to return relevant search results.

## Database location

Meilisearch creates the database the moment you first launch an instance. By default, you can find it inside a `data.ms` folder located in the same directory as the `meilisearch` binary.

The database location can change depending on a number of factors, such as whether you have configured a different database path with the [`--db-path` instance option](/learn/self_hosted/configure_meilisearch_at_launch#database-path), or if you're using an OS virtualization tool like [Docker](https://docker.com).

## LMDB

Creating a database from scratch and managing it is hard work. It would make no sense to try and reinvent the wheel, so Meilisearch uses a storage engine under the hood. This allows the Meilisearch team to focus on improving search relevancy and search performance while abstracting away the complicated task of creating, reading, and updating documents on disk and in memory.

Our storage engine is called [Lightning Memory-Mapped Database](http://www.lmdb.tech/doc/) (LMDB for short). LMDB is a transactional key-value store written in C that was developed for OpenLDAP and has ACID properties. Though we considered other options, such as [Sled](https://github.com/spacejam/sled) and [RocksDB](https://rocksdb.org/), we chose LMDB because it provided us with the best combination of performance, stability, and features.

### Memory mapping

LMDB stores its data in a [memory-mapped file](https://en.wikipedia.org/wiki/Memory-mapped_file). All data fetched from LMDB is returned straight from the memory map, which means there is no memory allocation or memory copy during data fetches.

All documents stored on disk are automatically loaded in memory when Meilisearch asks for them. This ensures LMDB will always make the best use of the RAM available to retrieve the documents.

For the best performance, it is recommended to have enough RAM to hold the entire database in memory.