# Integrate a relevant search bar to your documentation

**Source:** https://www.meilisearch.com/docs/guides/front_end/search_bar_for_docs.md
**Extrait le:** 2025-10-08
**Sujet:** Front-end Integration - Search bar for documentation

---

# Integrate a relevant search bar to your documentation

> Use Meilisearch to index content in a text-heavy website. Covers installing Meilisearch, configuring a text scraper, and creating a simple front end.

This tutorial will guide you through the steps of building a relevant and powerful search bar for your documentation 🚀

* [Run a Meilisearch instance](#run-a-meilisearch-instance)
* [Scrape your content](#scrape-your-content)
  * [Configuration file](#configuration-file)
  * [Run the scraper](#run-the-scraper)
* [Integrate the search bar](#integrate-the-search-bar)
  * [For VuePress documentation sites](#for-vuepress-documentation-sites)
  * [For all kinds of documentation](#for-all-kinds-of-documentation)
* [What's next?](#whats-next)

## Run a Meilisearch instance

First, create a new Meilisearch project on Meilisearch Cloud. You can also [install and run Meilisearch locally or in another cloud service](/learn/self_hosted/getting_started_with_self_hosted_meilisearch#setup-and-installation).

<Note>
  The host URL and the API key you will provide in the next steps correspond to the credentials of this Meilisearch instance.
</Note>

## Scrape your content

The Meilisearch team provides and maintains a [scraper tool](https://github.com/meilisearch/docs-scraper) to automatically read the content of your website and store it into an index in Meilisearch.

### Configuration file

The scraper tool needs a configuration file to know what content you want to scrape. This is done by providing selectors (for example, the `html` tag).

Here is an example of a basic configuration file:

```json
{
  "index_uid": "docs",
  "start_urls": [
    "https://www.example.com/doc/"
  ],
  "sitemap_urls": [
    "https://www.example.com/sitemap.xml"
  ],
  "stop_urls": [],
