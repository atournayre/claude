# Getting started with Meilisearch Cloud

**Source:** https://www.meilisearch.com/docs/learn/getting_started/cloud_quick_start.md
**Extrait le:** 2025-10-08
**Sujet:** Getting Started - Meilisearch Cloud Quick Start

---

# Getting started with Meilisearch Cloud

> Learn how to create your first Meilisearch Cloud project.

This tutorial walks you through setting up [Meilisearch Cloud](https://meilisearch.com/cloud), creating a project and an index, adding documents to it, and performing your first search with the default web interface.

You need a Meilisearch Cloud account to follow along. If you don't have one, register for a 14-day free trial account at [https://cloud.meilisearch.com/register](https://cloud.meilisearch.com/register?utm_campaign=oss\&utm_source=docs\&utm_medium=cloud-quick-start).

<iframe width="560" height="315" src="https://www.youtube.com/embed/KK2rV7i4IdI?si=F2DuOvzr7Du2jorz" title="Getting started with Meilisearch Cloud" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

## Creating a project

To use Meilisearch Cloud, you must first create a project. Projects act as containers for indexes, tasks, billing, and other information related to Meilisearch Cloud.

Click the "New project" button on the top menu. If you have a free trial account and this is your first project, the button will read "Start free trial" instead:

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-getting-started/1-new-project.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=dca6d7e62d243815bf4f803d790e1958" alt="The Meilisearch Cloud menu, featuring the 'New Project' button" data-og-width="2666" data-og-height="154" />
</Frame>

Meilisearch will prompt you to configure your project:

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-getting-started/2-configure-project.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=54dbbd07ada3a82de1ed27edc3e4de9a" alt="The project configuration screen" data-og-width="2666" data-og-height="1872" />
</Frame>

Enter a name for your project, then select the plan that best suits your needs. The next steps depend on your plan:

- Free trial and Hobby plans are immediately available. After naming your project and selecting either plan, click "Create" to create it
- With the Scale plan, you can configure CPU, RAM, and storage
- With the Enterprise plan, Meilisearch offers priority support, isolated infrastructure, and uptime guarantees

<Note>

This quick start guide was written for a free trial project. If you select a different plan, consult the [Meilisearch Cloud documentation](https://www.meilisearch.com/docs/cloud) for additional guidance.

</Note>

After your project is ready, the Meilisearch Cloud console displays a screen with your API keys and API endpoint. This screen looks like this:

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-getting-started/3-api-keys.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=b5a8fe58e39ca7b45bb3e7e2e1b5a0a7" alt="Project overview screen showing API keys" data-og-width="2666" data-og-height="1586" />
</Frame>

You need both your API endpoint and your default admin API key to interact with your Meilisearch project through the REST API or official SDKs. Keep this screen open or make a note of these values, as you will need them for the next steps.

## Using the web interface

Meilisearch Cloud offers a web interface for quick interaction with your project. This section shows how to add documents to an index and perform a simple search query.

### Adding documents

Navigate to the index list by clicking on "Indexes" in the project menu:

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-getting-started/4-indexes-menu.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=19c2e6e6b51c26cf964f9b0e9e5b89c5" alt="The Meilisearch Cloud menu, highlighting the 'Indexes' option" data-og-width="2666" data-og-height="562" />
</Frame>

Since this is a new project, your index list is empty. Create a new index by clicking on "Add an index":

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-getting-started/5-add-index.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=86f0d8f0b0c8a8d7e1b2a3f4c5d6e7f8" alt="The index list screen with the 'Add an index' button" data-og-width="2666" data-og-height="1382" />
</Frame>

Choose a name for your index and an optional primary key, then click "Create":

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-getting-started/6-create-index-modal.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=4d3c2b1a0e9f8d7c6b5a4d3c2b1a0e9f" alt="Modal window for creating a new index" data-og-width="2666" data-og-height="1382" />
</Frame>

The web interface redirects you to your index page. Click on "Add documents" to upload data to Meilisearch:

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-getting-started/7-add-documents.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=5e4d3c2b1a0e9f8d7c6b5a4d3c2b1a0e" alt="Empty index page with 'Add documents' button" data-og-width="2666" data-og-height="1382" />
</Frame>

A modal window opens with a text field. Paste the following document list or use your own:

```json
[
  {
    "id": 1,
    "title": "Carol",
    "genres": ["Romance", "Drama"]
  },
  {
    "id": 2,
    "title": "Wonder Woman",
    "genres": ["Action", "Adventure"]
  },
  {
    "id": 3,
    "title": "Life of Pi",
    "genres": ["Adventure", "Drama"]
  },
  {
    "id": 4,
    "title": "Mad Max: Fury Road",
    "genres": ["Adventure", "Science Fiction"]
  },
  {
    "id": 5,
    "title": "Moana",
    "genres": ["Fantasy", "Action"]
  },
  {
    "id": 6,
    "title": "Philadelphia",
    "genres": ["Drama"]
  }
]
```

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-getting-started/8-paste-documents.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=6d5c4b3a2f1e0d9c8b7a6d5c4b3a2f1e" alt="Modal window for adding documents with JSON data" data-og-width="2666" data-og-height="1382" />
</Frame>

After pasting your documents, click "Add" to add them to your index. Meilisearch will process your request and display the documents in the index page:

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-getting-started/9-documents-added.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=7e6d5c4b3a2f1e0d9c8b7a6d5c4b3a2f" alt="Index page showing the added documents" data-og-width="2666" data-og-height="1382" />
</Frame>

### Searching

Click on the "Search" tab at the top of the index page to access Meilisearch's search interface:

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-getting-started/10-search-tab.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=8f7e6d5c4b3a2f1e0d9c8b7a6d5c4b3a" alt="Index page highlighting the 'Search' tab" data-og-width="2666" data-og-height="1382" />
</Frame>

Type "wonder" in the search bar and press Enter:

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-getting-started/11-search-wonder.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=9g8f7e6d5c4b3a2f1e0d9c8b7a6d5c4b" alt="Search interface showing results for 'wonder'" data-og-width="2666" data-og-height="1382" />
</Frame>

Meilisearch returns one result, the movie "Wonder Woman". Notice that even though you searched for "wonder", Meilisearch still returned "Wonder Woman". By default, Meilisearch is [typo-tolerant](https://www.meilisearch.com/docs/learn/relevancy/typo_tolerance) and [returns results quickly](https://www.meilisearch.com/docs/learn/what_is_meilisearch/overview#search-as-you-type).

Now try searching for "phil". Meilisearch returns "Philadelphia":

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/kYJO98Uevt3SrL1y/assets/images/cloud-getting-started/12-search-phil.png?fit=max&auto=format&n=kYJO98Uevt3SrL1y&q=85&s=ah9g8f7e6d5c4b3a2f1e0d9c8b7a6d5c" alt="Search interface showing results for 'phil'" data-og-width="2666" data-og-height="1382" />
</Frame>

Once again, even though the search query is incomplete, Meilisearch returns relevant results. This is because Meilisearch uses [prefix search](https://www.meilisearch.com/docs/learn/relevancy/prefix_search) by default.

## Searching with code

This section demonstrates how to use a Meilisearch SDK to search your index from a Python script.

First, install the [Python SDK](https://github.com/meilisearch/meilisearch-python):

```bash
pip3 install meilisearch
```

Then create a file called `quick_start.py` and paste the following code:

```python
import meilisearch

# Replace with your Meilisearch Cloud API endpoint
api_url = "https://ms-xxxxx-xxxx.meilisearch.io"
# Replace with your Meilisearch Cloud admin API key
api_key = "YOUR_ADMIN_API_KEY"

client = meilisearch.Client(api_url, api_key)

# Replace 'movies' with your index name
index = client.index("movies")

# Perform a search query
results = index.search("wonder")

# Display the results
print(results)
```

Replace the placeholders with your API endpoint, API key, and index name. Then run the script:

```bash
python3 quick_start.py
```

You should see output similar to this:

```python
{
  "hits": [
    {
      "id": 2,
      "title": "Wonder Woman",
      "genres": ["Action", "Adventure"]
    }
  ],
  "query": "wonder",
  "processingTimeMs": 1,
  "limit": 20,
  "offset": 0,
  "estimatedTotalHits": 1
}
```

## Conclusion

You have successfully created a Meilisearch Cloud project, added documents to an index, and performed searches using both the web interface and a Python script.

To learn more about Meilisearch, consult the [official documentation](https://www.meilisearch.com/docs). You can also explore [search preview](https://www.meilisearch.com/docs/cloud/projects/search_preview), a tool allowing you to share your Meilisearch instance with non-technical users.
