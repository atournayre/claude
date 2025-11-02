# Accessing previous docs versions

**Source:** https://www.meilisearch.com/docs/learn/update_and_migration/previous_docs_version.md
**Extrait le:** 2025-10-08
**Sujet:** Update and Migration - Accessing Previous Documentation Versions

---

# Accessing previous docs versions

> Meilisearch documentation only covers the engine's latest stable release. Learn how to access the docs for previous Meilisearch versions.

This documentation website only covers the latest stable release of Meilisearch. However, it is possible to view the documentation of previous Meilisearch versions stored in [our GitHub repository](https://github.com/meilisearch/documentation).

This guide shows you how to clone Meilisearch's documentation repository, fetch the content for a specific version, and read it on your local machine.

<Warning>
  While this guide's goal is to help users of old versions accomplish their bare minimum needs, it is not intended as a long-term solution or to encourage users to continue using outdated versions of Meilisearch. In almost every case, **it is better to upgrade to the latest Meilisearch version**.

  Depending on the version in question, the process of accessing old documentation may be difficult or error-prone. You have been warned!
</Warning>

## Prerequisites

To follow this guide, you should have some familiarity with the command line. Before beginning, make sure the following tools are installed on your machine:

* [Git](https://git-scm.com/)
* [Node v14](https://nodejs.org/en/)
* [Yarn](https://classic.yarnpkg.com/en/)
* [Python 3](https://www.python.org)

## Clone the repository

To access previous versions of the Meilisearch documentation, the first step is downloading the documentation repository into your local machine. In Git, this is referred to as cloning.

Open your console and run the following command. It will create a `documentation` directory in your current location containing the Meilisearch documentation site project files:

```sh
git clone https://github.com/meilisearch/documentation.git
```

Alternatively, you may [clone the repository using an SSH URL](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-ssh-urls).

## Select a Meilisearch version

The documentation repository contains tags for versions from `v0.8` up to the latest release. Use these
