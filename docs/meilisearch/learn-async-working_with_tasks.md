# Working with tasks

**Source:** https://www.meilisearch.com/docs/learn/async/working_with_tasks.md
**Extrait le:** 2025-10-08
**Sujet:** Learn - Async Operations - Working with Tasks

---

# Working with tasks

> In this tutorial, you'll use the Meilisearch API to add documents to an index, and then monitor its status.

[Many Meilisearch operations are processed asynchronously](/learn/async/asynchronous_operations) in a task. Asynchronous tasks allow you to make resource-intensive changes to your Meilisearch project without any downtime for users.

In this tutorial, you'll use the Meilisearch API to add documents to an index, and then monitor its status.

## Requirements

* a running Meilisearch project
* a command-line console

## Adding a task to the task queue

Operations that require indexing, such as adding and updating documents or changing an index's settings, will always generate a task.

Start by creating an index, then add a large number of documents to this index:

<CodeGroup>
  ```bash cURL
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/documents'\
    -H 'Content-Type: application/json' \
    --data-binary @movies.json
  ```

  ```javascript JS
  const movies = require('./movies.json')
  client.index('movies').addDocuments(movies).then((res) => console.log(res))
  ```

  ```python Python
  import json

  json_file = open('movies.json', encoding='utf-8')
  movies = json.load(json_file)
  client.index('movies').add_documents(movies)
  ```

  ```php PHP
  $moviesJson = file_get_contents('movies.json');
  $movies = json_decode($moviesJson);

  $client->index('movies')->addDocuments($movies);
  ```

  ```java Java
  import com.meilisearch.sdk;
  import org.json.JSONArray;
  import java.nio.file.Files;
  import java.nio.file.Path;

  Path fileName = Path.of("movies.json");
  String moviesJson = Files.readString(fileName);
  Client client = new Client(new Config("http://localhost:7700", "masterKey"));

  client.index("movies").addDocuments(moviesJson);
  ```
</CodeGroup>

---

**Note:** Le contenu a été partiellement récupéré. Le WebFetch a retourné un contenu tronqué. Pour obtenir la documentation complète, il faudrait soit utiliser un outil différent, soit accéder directement au repository GitHub de Meilisearch.
