# Using multi-search to perform a federated search

**Source:** https://www.meilisearch.com/docs/learn/multi_search/performing_federated_search.md
**Extrait le:** 2025-10-08
**Sujet:** Multi-Search - Federated Search Tutorial

---

> In this tutorial you will see how to perform a query searching multiple indexes at the same time to obtain a single list of results.

Meilisearch allows you to make multiple search requests at the same time with the `/multi-search` endpoint. A federated search is a multi-search that returns results from multiple queries in a single list.

In this tutorial you will see how to create separate indexes containing different types of data from a CRM application. You will then perform a query searching all these indexes at the same time to obtain a single list of results.

## Requirements

* A running Meilisearch project
* A command-line console

## Create three indexes

Download the following datasets: <a href="/assets/datasets/crm-chats.json">`crm-chats.json`</a>, <a href="/assets/datasets/crm-profiles.json">`crm-profiles.json`</a>, and <a href="/assets/datasets/crm-tickets.json">`crm-tickets.json`</a> containing data from a fictional CRM application.

Add the datasets to Meilisearch and create three separate indexes, `profiles`, `chats`, and `tickets`:

```sh
curl  -X POST 'MEILISEARCH_URL/indexes/profiles'  -H 'Content-Type: application/json'  --data-binary @crm-profiles.json &&
curl  -X POST 'MEILISEARCH_URL/indexes/chats'  -H 'Content-Type: application/json'  --data-binary @crm-chats.json &&
curl  -X POST 'MEILISEARCH_URL/indexes/tickets'  -H 'Content-Type: application/json'  --data-binary @crm-tickets.json
```

[Use the tasks endpoint](/learn/async/working_with_tasks) to check the indexing status. Once Meilisearch successfully indexed all three datasets, you are ready to perform a federated search.

## Perform a federated search

When you are looking for Natasha Nguyen's email address in your CRM application, you may not know whether you will find it in a chat log, among user profiles, or in a support ticket.

---

**Note:** Le contenu complet de cette page n'a pu être entièrement récupéré via WebFetch. Pour la version complète, consulter directement l'URL source ci-dessus.
