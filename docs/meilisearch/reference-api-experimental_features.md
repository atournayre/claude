# Experimental Features API

**Source:** https://www.meilisearch.com/docs/reference/api/experimental_features.md
**Extrait le:** 2025-10-08
**Sujet:** API Reference - Experimental Features

---

# Experimental

> The /experimental-features route allows you to manage some of Meilisearch's experimental features.

export const RouteHighlighter = ({method, path}) => <div className={`routeHighlighter routeHighlighter--${method}`}>
    <div className="routeHighlighter__method">
      {method}
    </div>
    <div className="routeHighlighter__path">
      {path}
    </div>
  </div>;

The `/experimental-features` route allows you to activate or deactivate some of Meilisearch's [experimental features](/learn/resources/experimental_features_overview).

This route is **synchronous**. This means that no task object will be returned, and any activated or deactivated features will be made available or unavailable immediately.

<Warning>
  The experimental API route is not compatible with all experimental features. Consult the [experimental feature overview](/learn/resources/experimental_features_overview) for a compatibility list.
</Warning>

## Experimental features object

```json
{
  "metrics": false,
  "logsRoute": true,
  "containsFilter": false,
  "editDocumentsByFunction": false,
  "network": false,
  "chatCompletions": false,
  "multimodal": false,
  "vectorStoreSetting": false
}
```

| Name                          | Type    | Description                                    |
| :---------------------------- | :------ | :--------------------------------------------- |
| **`metrics`**                 | Boolean | `true` if feature is active, `false` otherwise |
| **`logsRoute`**               | Boolean | `true` if feature is active, `false` otherwise |
| **`containsFilter`**          | Boolean | `true` if feature is active, `false` otherwise |
| **`editDocumentsByFunction`** | Boolean | `true` if feature is active, `false` otherwise |
| **`network`**                 | Boolean | `true` if feature is active, `false` otherwise |
| **`chatCompletions`**         | Boolean | `true` if feature is active, `false` otherwise |
| **`multimodal`**              | Boolean | `true` if feature is active, `false` otherwise |
| **`vectorStoreSetting`**      | Boolean | `true` if feature is active, `false` otherwise |
