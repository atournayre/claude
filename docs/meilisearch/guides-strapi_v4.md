# Strapi v4 guide

**Source:** https://www.meilisearch.com/docs/guides/strapi_v4.md
**Extrait le:** 2025-10-08
**Sujet:** Integration Guide - Strapi v4

---

# Strapi v4 guide

> Learn how to use Meilisearch with Strapi v4.

This tutorial will show you how to integrate Meilisearch with [Strapi](https://strapi.io/) to create a search-based web app. First, you will use Strapi's quick start guide to create a restaurant collection, and then search this collection with Meilisearch.

## Prerequisites

* [Node.js](https://nodejs.org/): active LTS or maintenance LTS versions, currently Node.js >=18.0.0 \<=20.x.x
* npm >=6.0.0 (installed with Node.js)
* A running instance of Meilisearch (v >= 1.x). If you need help with this part, you can consult the [Installation section](/learn/self_hosted/install_meilisearch_locally).

## Create a back end using Strapi

### Set up the project

Create a directory called `my-app` where you will add the back and front-end parts of the application. Generate a back-end API using Strapi inside `my-app`:

```bash
npx create-strapi-app@latest back --quickstart
```

[The rest of the markdown content remains exactly the same as in the original document]
