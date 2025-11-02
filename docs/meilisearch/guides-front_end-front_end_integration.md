# Front-end integration

**Source:** https://www.meilisearch.com/docs/guides/front_end/front_end_integration.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Front-end Integration

---

# Front-end integration

> Create a simple front-end interface to search through your dataset after following Meilisearch's quick start.

In the [quick start tutorial](/learn/self_hosted/getting_started_with_self_hosted_meilisearch), you learned how to launch Meilisearch and make a search request. This article will teach you how to create a simple front-end interface to search through your dataset.

Using [`instant-meilisearch`](https://github.com/meilisearch/instant-meilisearch) is the easiest way to build a front-end interface for search. `instant-meilisearch` is a plugin that establishes communication between a Meilisearch instance and [InstantSearch](https://github.com/algolia/instantsearch.js). InstantSearch, an open-source project developed by Algolia, renders all the components needed to start searching.

1. Create an empty file and name it `index.html`
2. Open it in a text editor like Notepad, Sublime Text, or Visual Studio Code
3. Copy-paste one the code sample below
4. Open `index.html` in your browser by double-clicking it in your folder

```js
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@meilisearch/instant-meilisearch/templates/basic_search.css" />
  </head>
  <body>
    <div class="wrapper">
      <div id="searchbox" focus></div>
      <div id="hits"></div>
    </div>
  </body>
  <script src="https://cdn.jsdelivr.net/npm/@meilisearch/instant-meilisearch/dist/instant-meilisearch.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4"></script>
  <script>
    const search = instantsearch({
      indexName: "movies",
      searchClient: instantMeiliSearch(
        "http://localhost:7700"
      ).searchClient
    });

    search.addWidgets([
      instantsearch.widgets.searchBox({
        container: "#searchbox"
      }),
      instantsearch.widgets.configure({ hitsPerPage: 8 }),
      instantsearch.widgets.hits({
        container: "#hits",
        templates: {
          item: `
            <div>
              <div class="hit-name">
                  {{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}
              </div>
            </div>
          `
        }
      })
    ]);

    search.start();
  </script>
</html>
```
