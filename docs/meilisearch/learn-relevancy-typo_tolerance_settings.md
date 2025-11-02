# Typo tolerance settings

**Source:** https://www.meilisearch.com/docs/learn/relevancy/typo_tolerance_settings.md
**Extrait le:** 2025-10-08
**Sujet:** Relevancy - Typo Tolerance Settings

---

# Typo tolerance settings

> This article describes each of the typo tolerance settings.

Typo tolerance helps users find relevant results even when their search queries contain spelling mistakes or typos, for example, typing `phnoe` instead of `phone`. You can [configure the typo tolerance feature for each index](/reference/api/settings#update-typo-tolerance-settings).

## `enabled`

Typo tolerance is enabled by default, but you can disable it if needed:

<CodeGroup>
  ```bash cURL
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/movies/settings/typo-tolerance' \
    -H 'Content-Type: application/json' \
    --data-binary '{ "enabled": false }'
  ```

  ```javascript JS
  client.index('movies').updateTypoTolerance({
    enabled: false
  })
  ```

  ```python Python
  client.index('movies').update_typo_tolerance({
    'enabled': False
  })
  ```

  ```php PHP
  $client->index('movies')->updateTypoTolerance([
    'enabled' => false
  ]);
  ```

  ```java Java
  TypoTolerance typoTolerance = new TypoTolerance();
  typoTolerance.setEnabled(false);
  client.index("movies").updateTypoToleranceSettings(typoTolerance);
  ```

  ```ruby Ruby
  index('books').update_typo_tolerance({ enabled: false })
  ```

  ```go Go
  client.Index("movies").UpdateTypoTolerance(&meilisearch.TypoTolerance{
    Enabled: false,
  })
  ```

  ```csharp C#
  var typoTolerance = new TypoTolerance {
    Enabled = false
  };
  await client.Index("movies").UpdateTypoToleranceAsync(typoTolerance);
  ```

  ```rust Rust
  let typo_tolerance = TypoToleranceSettings {
    enabled: Some(false),
    ..Default::default()
  };
  client.index("movies").set_typo_tolerance(&typo_tolerance).await.unwrap();
  ```

  ```swift Swift
  try await client.index("movies").updateTypoTolerance([
    "enabled": false
  ])
  ```
</CodeGroup>

## `minWordSizeForTypos`

Sets the minimum word size for typos. Words shorter than the given minimum size will not be considered for typos.

There are two settings in `minWordSizeForTypos`:

- `oneTypo`: The minimum word size for accepting 1 typo; must be between `0` and `twoTypos`
- `twoTypos`: The minimum word size for accepting 2 typos; must be between `oneTypo` and `255`

The default value for `oneTypo` is `5`, and for `twoTypos` is `9`.

<CodeGroup>
  ```bash cURL
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/movies/settings/typo-tolerance' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "minWordSizeForTypos": {
        "oneTypo": 4,
        "twoTypos": 8
      }
    }'
  ```

  ```javascript JS
  client.index('movies').updateTypoTolerance({
    minWordSizeForTypos: {
      oneTypo: 4,
      twoTypos: 8
    }
  })
  ```

  ```python Python
  client.index('movies').update_typo_tolerance({
    'minWordSizeForTypos': {
      'oneTypo': 4,
      'twoTypos': 8
    }
  })
  ```

  ```php PHP
  $client->index('movies')->updateTypoTolerance([
    'minWordSizeForTypos' => [
      'oneTypo' => 4,
      'twoTypos' => 8
    ]
  ]);
  ```

  ```java Java
  MinWordSizeForTypos minWordSizeForTypos = new MinWordSizeForTypos();
  minWordSizeForTypos.setOneTypo(4);
  minWordSizeForTypos.setTwoTypos(8);

  TypoTolerance typoTolerance = new TypoTolerance();
  typoTolerance.setMinWordSizeForTypos(minWordSizeForTypos);

  client.index("movies").updateTypoToleranceSettings(typoTolerance);
  ```

  ```ruby Ruby
  index('books').update_typo_tolerance({
    minWordSizeForTypos: {
      oneTypo: 4,
      twoTypos: 8
    }
  })
  ```

  ```go Go
  client.Index("movies").UpdateTypoTolerance(&meilisearch.TypoTolerance{
    MinWordSizeForTypos: meilisearch.MinWordSizeForTypos{
      OneTypo: 4,
      TwoTypos: 8,
    },
  })
  ```

  ```csharp C#
  var typoTolerance = new TypoTolerance {
    MinWordSizeForTypos = new MinWordSizeForTypos {
      OneTypo = 4,
      TwoTypos = 8
    }
  };
  await client.Index("movies").UpdateTypoToleranceAsync(typoTolerance);
  ```

  ```rust Rust
  let typo_tolerance = TypoToleranceSettings {
    min_word_size_for_typos: Some(MinWordSizeForTypos {
      one_typo: Some(4),
      two_typos: Some(8),
    }),
    ..Default::default()
  };
  client.index("movies").set_typo_tolerance(&typo_tolerance).await.unwrap();
  ```

  ```swift Swift
  try await client.index("movies").updateTypoTolerance([
    "minWordSizeForTypos": [
      "oneTypo": 4,
      "twoTypos": 8
    ]
  ])
  ```
</CodeGroup>

## `disableOnWords`

You can disable typo tolerance on certain words. This can be useful for proper nouns or technical terms that shouldn't be subject to typos.

By default, this setting is an empty array: `[]`.

<CodeGroup>
  ```bash cURL
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/movies/settings/typo-tolerance' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "disableOnWords": ["shrek", "hallelujah"]
    }'
  ```

  ```javascript JS
  client.index('movies').updateTypoTolerance({
    disableOnWords: ['shrek', 'hallelujah']
  })
  ```

  ```python Python
  client.index('movies').update_typo_tolerance({
    'disableOnWords': ['shrek', 'hallelujah']
  })
  ```

  ```php PHP
  $client->index('movies')->updateTypoTolerance([
    'disableOnWords' => ['shrek', 'hallelujah']
  ]);
  ```

  ```java Java
  TypoTolerance typoTolerance = new TypoTolerance();
  typoTolerance.setDisableOnWords(new String[]{"shrek", "hallelujah"});
  client.index("movies").updateTypoToleranceSettings(typoTolerance);
  ```

  ```ruby Ruby
  index('books').update_typo_tolerance({
    disableOnWords: ['shrek', 'hallelujah']
  })
  ```

  ```go Go
  client.Index("movies").UpdateTypoTolerance(&meilisearch.TypoTolerance{
    DisableOnWords: []string{"shrek", "hallelujah"},
  })
  ```

  ```csharp C#
  var typoTolerance = new TypoTolerance {
    DisableOnWords = new string[] { "shrek", "hallelujah" }
  };
  await client.Index("movies").UpdateTypoToleranceAsync(typoTolerance);
  ```

  ```rust Rust
  let typo_tolerance = TypoToleranceSettings {
    disable_on_words: Some(vec!["shrek".to_string(), "hallelujah".to_string()]),
    ..Default::default()
  };
  client.index("movies").set_typo_tolerance(&typo_tolerance).await.unwrap();
  ```

  ```swift Swift
  try await client.index("movies").updateTypoTolerance([
    "disableOnWords": ["shrek", "hallelujah"]
  ])
  ```
</CodeGroup>

## `disableOnAttributes`

You can disable typo tolerance on specific attributes. This is helpful when you want some attributes to require exact matches.

By default, this setting is an empty array: `[]`.

<CodeGroup>
  ```bash cURL
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/movies/settings/typo-tolerance' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "disableOnAttributes": ["title"]
    }'
  ```

  ```javascript JS
  client.index('movies').updateTypoTolerance({
    disableOnAttributes: ['title']
  })
  ```

  ```python Python
  client.index('movies').update_typo_tolerance({
    'disableOnAttributes': ['title']
  })
  ```

  ```php PHP
  $client->index('movies')->updateTypoTolerance([
    'disableOnAttributes' => ['title']
  ]);
  ```

  ```java Java
  TypoTolerance typoTolerance = new TypoTolerance();
  typoTolerance.setDisableOnAttributes(new String[]{"title"});
  client.index("movies").updateTypoToleranceSettings(typoTolerance);
  ```

  ```ruby Ruby
  index('books').update_typo_tolerance({
    disableOnAttributes: ['title']
  })
  ```

  ```go Go
  client.Index("movies").UpdateTypoTolerance(&meilisearch.TypoTolerance{
    DisableOnAttributes: []string{"title"},
  })
  ```

  ```csharp C#
  var typoTolerance = new TypoTolerance {
    DisableOnAttributes = new string[] { "title" }
  };
  await client.Index("movies").UpdateTypoToleranceAsync(typoTolerance);
  ```

  ```rust Rust
  let typo_tolerance = TypoToleranceSettings {
    disable_on_attributes: Some(vec!["title".to_string()]),
    ..Default::default()
  };
  client.index("movies").set_typo_tolerance(&typo_tolerance).await.unwrap();
  ```

  ```swift Swift
  try await client.index("movies").updateTypoTolerance([
    "disableOnAttributes": ["title"]
  ])
  ```
</CodeGroup>

## Learn more

- [Typo tolerance guide](/learn/relevancy/typo_tolerance)
- [Typo tolerance API reference](/reference/api/settings#typo-tolerance)
