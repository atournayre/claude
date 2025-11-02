# React quick start

**Source:** https://www.meilisearch.com/docs/guides/front_end/react_quick_start.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - React Integration

---

# React quick start

> Integrate a search-as-you-type experience into your React app.

Integrate a search-as-you-type experience into your React app.

## 1. Create a React application

Create your React application using a [Vite](https://vitejs.dev/) template:

```bash
npm create vite@latest my-app -- --template react
```

## 2. Install the library of search components

Navigate to your React app and install `react-instantsearch`, `@meilisearch/instant-meilisearch`, and `instantsearch.css`.

```bash
npm install react-instantsearch @meilisearch/instant-meilisearch instantsearch.css
```

* [React InstantSearch](https://github.com/algolia/instantsearch/): front-end tools to customize your search environment
* [instant-meilisearch](https://github.com/meilisearch/meilisearch-js-plugins/tree/main/packages/instant-meilisearch): Meilisearch client to connect with React InstantSearch
* [instantsearch.css](https://github.com/algolia/instantsearch/tree/master/packages/instantsearch.css) (optional): CSS library to add basic styles to the search components

## 3. Initialize the search client

Use the following URL and API key to connect to a Meilisearch instance containing data from Steam video games.

```jsx
import React from 'react';
import { instantMeiliSearch } from '@meilisearch/instant-meilisearch';

const { searchClient } = instantMeiliSearch(
  'https://ms-adf78ae33284-106.lon.meilisearch.io',
  'a63da4928426f12639e19d62886f621130f3fa9ff3c7534c5d179f0f51c4f303'
);
```

## 4. Add the InstantSearch provider

`<InstantSearch>` is the root provider component for the InstantSearch library. It takes two props: the `searchClient` and the [index name](/learn/getting_started/indexes#index-uid).
