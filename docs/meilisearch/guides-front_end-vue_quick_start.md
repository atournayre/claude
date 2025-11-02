# Vue3 quick start

**Source:** https://www.meilisearch.com/docs/guides/front_end/vue_quick_start.md
**Extrait le:** 2025-10-08
**Sujet:** Vue.js Integration Guide

---

# Vue3 quick start

> Integrate a search-as-you-type experience into your Vue app.

## 1. Create a Vue application

Run the `npm create` tool to install base dependencies and create your app folder structure.

```bash
npm create vue@latest my-app
```

## 2. Install the library of search components

Navigate to your Vue app and install `vue-instantsearch`, `@meilisearch/instant-meilisearch`, and `instantsearch.css`.

```bash
npm install vue-instantsearch @meilisearch/instant-meilisearch instantsearch.css
```

* [Vue InstantSearch](https://github.com/algolia/instantsearch/): front-end tools to customize your search environment
* [instant-meilisearch](https://github.com/meilisearch/meilisearch-js-plugins/tree/main/packages/instant-meilisearch): Meilisearch client to connect with Vue InstantSearch
* [instantsearch.css](https://github.com/algolia/instantsearch/tree/master/packages/instantsearch.css) (optional): CSS library to add basic styles to the search components

## 3. Add InstantSearch

Include InstantSearch into `main.js` to include the Vue InstantSearch library.

```js
import { createApp } from 'vue';
import App from './App.vue';
import InstantSearch from 'vue-instantsearch/vue3/es';

const app = createApp(App);
app.use(InstantSearch);
app.mount('#app');
```

## 4. Initialize the search client

Add the code below to the `App.vue` file.

```js
<template>
  <ais-instant-search :search-client="searchClient" index-name="steam-videogames">
  </ais-instant-search>
</template>

<script>
import { instantMeiliSearch } from "@meilisearch/instant-meilisearch";

export default {
  data() {
    return {
      searchClient: instantMeiliSearch(
        'https://ms-adf78ae33284-106.lon.meilisearch.io',
        'a63da4928426f12639e19d62886f621130f3fa9ff3c7534c5d179f0f51c4f303'
      ).searchClient,
    };
  },
};
</script>
```

The above code creates a MeiliSearch client using `instant-meilisearch` and passes it to the `<ais-instant-search>` wrapper component. All the Vue InstantSearch components must be included within `<ais-instant-search>` in order to be able to make search queries.

## 5. Create a search bar

Add a search box so users can query the Meilisearch index.

```js
<template>
  <ais-instant-search :search-client="searchClient" index-name="steam-videogames">
    <ais-search-box placeholder="Search here…" class="searchbox" />
  </ais-instant-search>
</template>
```

## 6. Display search results

Use the `<ais-hits>` component to display the search results.

```js
<template>
  <ais-instant-search :search-client="searchClient" index-name="steam-videogames">
    <ais-search-box placeholder="Search here…" class="searchbox" />
    <ais-hits>
      <template v-slot:item="{ item }">
        <h2>{{ item.name }}</h2>
      </template>
    </ais-hits>
  </ais-instant-search>
</template>
```

## 7. Add styling

Import the default CSS stylesheet from the `instantsearch.css` library inside your `<script>` block.

```js
<script>
import { instantMeiliSearch } from "@meilisearch/instant-meilisearch";
import 'instantsearch.css/themes/satellite-min.css';

export default {
  data() {
    return {
      searchClient: instantMeiliSearch(
        'https://ms-adf78ae33284-106.lon.meilisearch.io',
        'a63da4928426f12639e19d62886f621130f3fa9ff3c7534c5d179f0f51c4f303'
      ).searchClient,
    };
  },
};
</script>
```

## Final result

Here is the complete `App.vue` with all the integrated search components.

```js
<template>
  <ais-instant-search :search-client="searchClient" index-name="steam-videogames">
    <ais-search-box placeholder="Search here…" class="searchbox" />
    <ais-hits>
      <template v-slot:item="{ item }">
        <h2>{{ item.name }}</h2>
      </template>
    </ais-hits>
  </ais-instant-search>
</template>

<script>
import { instantMeiliSearch } from "@meilisearch/instant-meilisearch";
import 'instantsearch.css/themes/satellite-min.css';

export default {
  data() {
    return {
      searchClient: instantMeiliSearch(
        'https://ms-adf78ae33284-106.lon.meilisearch.io',
        'a63da4928426f12639e19d62886f621130f3fa9ff3c7534c5d179f0f51c4f303'
      ).searchClient,
    };
  },
};
</script>
```

The above code creates a simple page with a search bar and search results.

![A simple web page with a search bar reading "games about dinosaurs". Below it, a list of search results, including the games Turok, Dino D-Day, and Nanosaur 2](https://raw.githubusercontent.com/meilisearch/meilisearch/main/assets/front-end-demo.gif)

**Your search preview is now up and running!** 🚀

If you have any problems or questions about Meilisearch or this quick start, come say hi in [our discussion forum](https://github.com/orgs/meilisearch/discussions).
