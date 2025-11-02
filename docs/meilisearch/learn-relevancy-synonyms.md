# Synonyms

**Source:** https://www.meilisearch.com/docs/learn/relevancy/synonyms.md
**Extrait le:** 2025-10-08
**Sujet:** Learn - Relevancy - Synonyms

---

# Synonyms

> Use Meilisearch synonyms to indicate sets of query terms which should be considered equivalent during search.

If multiple words have an equivalent meaning in your dataset, you can [create a list of synonyms](/reference/api/settings#update-synonyms). This will make your search results more relevant.

Words set as synonyms won't always return the same results. With the default settings, the `movies` dataset should return 547 results for `great` and 66 for `fantastic`. Let's set them as synonyms:

<CodeGroup>
  ```bash cURL
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/movies/settings/synonyms' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "great": ["fantastic"], "fantastic": ["great"]
    }'
  ```

  ```javascript JS
  client.index('movies').updateSynonyms({
    'great': ['fantastic'],
    'fantastic': ['great']
  })
  ```

  ```python Python
  client.index('movies').update_synonyms({
    'great': ['fantastic'],
    'fantastic': ['great']
  })
  ```

  ```php PHP
  $client->index('movies')->updateSynonyms([
    'great' => ['fantastic'],
    'fantastic' => ['great'],
  ]);
  ```

  ```java Java
  HashMap<String, String[]> synonyms = new HashMap<String, String[]>();
  synonyms.put("great", new String[] {"fantastic"});
  synonyms.put("fantastic", new String[] {"great"});

  client.index("movies").updateSynonymsSettings(synonyms);
  ```

  ```ruby Ruby
  client.index('movies').update_synonyms({
    great: ['fantastic'],
    fantastic: ['great']
  })
  ```

  ```go Go
  synonyms := map[string][]string{
    "great":      []string{"fantastic"},
    "fantastic":  []string{"great"},
  }
  client.Index("movies").UpdateSynonyms(&synonyms)
  ```

  ```csharp C#
  await client.Index("movies").UpdateSynonymsAsync(new Dictionary<string, IEnumerable<string>>
  {
    {"great", new string[] {"fantastic"}},
    {"fantastic", new string[] {"great"}}
  });
  ```

  ```swift Swift
  client.index("movies").updateSynonyms([
    "great": ["fantastic"],
    "fantastic": ["great"]
  ]) { result in
    switch result {
    case .success(let task):
      print(task)
    case .failure(let error):
      print(error)
    }
  }
  ```
</CodeGroup>

After the settings update, both queries will now return the same results (608 hits). You can also see that both terms are displayed in **bold** in the `formatted` field—meaning both are considered relevant to the query.

## Multi-word synonyms

A synonym can be made up of one or multiple words. You can specify them in the same way as single words, using commas and arrays to designate synonym groups.

<CodeGroup>
  ```bash cURL
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/movies/settings/synonyms' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "great": ["fantastic", "wonderful"],
      "fantastic": ["great", "wonderful"],
      "wonderful": ["great", "fantastic"],
      "SF": ["science fiction"],
      "science fiction": ["SF"]
    }'
  ```

  ```javascript JS
  client.index('movies').updateSynonyms({
    'great': ['fantastic', 'wonderful'],
    'fantastic': ['great', 'wonderful'],
    'wonderful': ['great', 'fantastic'],
    'SF': ['science fiction'],
    'science fiction': ['SF']
  })
  ```

  ```python Python
  client.index('movies').update_synonyms({
    'great': ['fantastic', 'wonderful'],
    'fantastic': ['great', 'wonderful'],
    'wonderful': ['great', 'fantastic'],
    'SF': ['science fiction'],
    'science fiction': ['SF']
  })
  ```

  ```php PHP
  $client->index('movies')->updateSynonyms([
    'great' => ['fantastic', 'wonderful'],
    'fantastic' => ['great', 'wonderful'],
    'wonderful' => ['great', 'fantastic'],
    'SF' => ['science fiction'],
    'science fiction' => ['SF'],
  ]);
  ```

  ```java Java
  HashMap<String, String[]> synonyms = new HashMap<String, String[]>();
  synonyms.put("great", new String[] {"fantastic", "wonderful"});
  synonyms.put("fantastic", new String[] {"great", "wonderful"});
  synonyms.put("wonderful", new String[] {"great", "fantastic"});
  synonyms.put("SF", new String[] {"science fiction"});
  synonyms.put("science fiction", new String[] {"SF"});

  client.index("movies").updateSynonymsSettings(synonyms);
  ```

  ```ruby Ruby
  client.index('movies').update_synonyms({
    great: ['fantastic', 'wonderful'],
    fantastic: ['great', 'wonderful'],
    wonderful: ['great', 'fantastic'],
    'SF': ['science fiction'],
    'science fiction': ['SF']
  })
  ```

  ```go Go
  synonyms := map[string][]string{
    "great":            []string{"fantastic", "wonderful"},
    "fantastic":        []string{"great", "wonderful"},
    "wonderful":        []string{"great", "fantastic"},
    "SF":               []string{"science fiction"},
    "science fiction":  []string{"SF"},
  }
  client.Index("movies").UpdateSynonyms(&synonyms)
  ```

  ```csharp C#
  await client.Index("movies").UpdateSynonymsAsync(new Dictionary<string, IEnumerable<string>>
  {
    {"great", new string[] {"fantastic", "wonderful"}},
    {"fantastic", new string[] {"great", "wonderful"}},
    {"wonderful", new string[] {"great", "fantastic"}},
    {"SF", new string[] {"science fiction"}},
    {"science fiction", new string[] {"SF"}}
  });
  ```

  ```swift Swift
  client.index("movies").updateSynonyms([
    "great": ["fantastic", "wonderful"],
    "fantastic": ["great", "wonderful"],
    "wonderful": ["great", "fantastic"],
    "SF": ["science fiction"],
    "science fiction": ["SF"]
  ]) { result in
    switch result {
    case .success(let task):
      print(task)
    case .failure(let error):
      print(error)
    }
  }
  ```
</CodeGroup>

Searching for `SF movie` will find all documents containing `science fiction movie` as well.

## Case sensitivity

**Synonyms are case-insensitive**. Whether the letters are uppercase or lowercase has no impact on the way Meilisearch handles synonyms.

If your synonym list contains:

```json
{
  "SF": ["science fiction"],
  "science fiction": ["SF"]
}
```

A search for either `SF` or `sf` will return documents containing both `SF` and `science fiction` in lowercase or uppercase.

## One-way associations

By default, synonyms work two-way. But if you want to match query terms with synonyms only when they're entered in a specific order, you should use [one-way associations](#one-way-associations).

Here is an example:

```json
{
  "dog": ["labrador", "rottweiler"],
  "labrador": [],
  "rottweiler": []
}
```

In this example, `labrador` and `rottweiler` will return documents containing both `labrador` AND `dog`, but `dog` will **only** return documents containing `dog`.

## Phrase search and synonyms

**Phrase searches** are queries wrapped in double quotes (`"`). They only return results containing the exact query phrase.

Synonyms aren't applied during [phrase search](/learn/search_parameters/phrase_search). If you want to get results for synonyms as well, you'll need to search for each synonym individually.

## Limitations

Meilisearch will not recognize synonyms for [prefix search](/learn/search_parameters/query#prefix-search).

For example, if you have added `SF` and `science fiction` as synonyms, the search `science fi` will not return documents containing `SF`.
