# FAQ

**Source:** https://www.meilisearch.com/docs/learn/resources/faq.md
**Extrait le:** 2025-10-08
**Sujet:** Resources - FAQ (Frequently Asked Questions)

---

> Frequently asked questions

## I have never used a search engine before. Can I use Meilisearch anyway?

Of course! No knowledge of ElasticSearch or Solr is required to use Meilisearch.

Meilisearch is really **easy to use** and thus accessible to all kinds of developers.

[Take a quick tour](/learn/self_hosted/getting_started_with_self_hosted_meilisearch) to learn the basics of Meilisearch!

We also provide a lot of tools, including [SDKs](/learn/resources/sdks), to help you integrate easily Meilisearch in your project. We're adding new tools every day!

Plus, you can [contact us](https://discord.meilisearch.com) if you need any help.

## How to know if Meilisearch perfectly fits my use cases?

Since Meilisearch is an open-source and easy-to-use tool, you can give it a try using your data. Follow this [guide](/learn/self_hosted/getting_started_with_self_hosted_meilisearch) to get a quick start!

Besides, we published a [comparison between Meilisearch and other search engines](/learn/resources/comparison_to_alternatives) with the goal of providing an overview of Meilisearch alternatives.

## I am trying to add my documents but I keep receiving a `400 - Bad Request` response

The `400 - Bad request` response often means that your data is not in an expected format. You might have extraneous commas, mismatched brackets, missing quotes, etc. Meilisearch API accepts JSON, CSV, and NDJSON formats.

When [adding or replacing documents](/reference/api/documents#add-or-replace-documents), you must enclose them in an array even if there is only one new document.

## I have uploaded my documents, but I get no result when I search in my index

Your document upload probably failed. To understand why, please check the status of the document addition task using the returned [`taskUid`](/reference/api/tasks#get-one-task). If the task failed, the response should contain an `error` object.

Here is an example of a failed task
