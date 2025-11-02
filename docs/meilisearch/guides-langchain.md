# Implementing semantic search with LangChain

**Source:** https://www.meilisearch.com/docs/guides/langchain.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - LangChain Integration

---

# Implementing semantic search with LangChain

> This guide shows you how to implement semantic search using LangChain and similarity search.

In this guide, you'll use OpenAI's text embeddings to measure the similarity between document properties. Then, you'll use the LangChain framework to seamlessly integrate Meilisearch and create an application with semantic search.

## Requirements

This guide assumes a basic understanding of Python and LangChain. Beginners to LangChain will still find the tutorial accessible.

* Python (LangChain requires >= 3.8.1 and \< 4.0) and the pip CLI
* A [Meilisearch >= 1.6 project](/learn/getting_started/cloud_quick_start)
* An [OpenAI API key](https://platform.openai.com/account/api-keys)

## Creating the application

Create a folder for your application with an empty `setup.py` file.

Before writing any code, install the necessary dependencies:

```bash
pip install langchain openai meilisearch python-dotenv
```

First create a .env to store our credentials:

```
# .env

MEILI_HTTP_ADDR="your Meilisearch host"
MEILI_API_KEY="your Meilisearch API key"
OPENAI_API_KEY="your OpenAI API key"
```

Now that you have your environment variables available, create a `setup.py` file with some boilerplate code:

```python
# setup.py

import os
from dotenv import load_dotenv # remove if not using dotenv
from langchain.vectorstores import Meilisearch
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import JSONLoader

load_dotenv() # remove if not using dotenv

# exit if missing env vars
if "MEILI_HTTP_ADDR" not in os.environ:
    raise Exception("Missing MEILI_HTTP_ADDR env var")
if "MEILI_API_KEY" not in os.environ:
    raise Exception("Missing MEILI_API_KEY env var")
if "OPENAI_API_KEY" not in os.environ:
    raise Exception("Missing OPENAI_API_KEY env var")
```

## Loading documents

For this tutorial, you'll need some documents. We recommend [this movies dataset](https://www.meilisearch.com/movies.json).

Download the file and place it in your project's root directory.

Use the following code to load the dataset and convert it into a list of LangChain documents:

```python
# setup.py

# ...

embeddings = OpenAIEmbeddings()

def metadata_func(record: dict, metadata: dict) -> dict:
    metadata["title"] = record.get("title")
    metadata["overview"] = record.get("overview")
    metadata["release_date"] = record.get("release_date")
    metadata["genres"] = record.get("genres")
    return metadata

loader = JSONLoader(
    file_path='./movies.json',
    jq_schema='.',
    content_key='overview',
    is_content_key_jq_parsable=True,
    metadata_func=metadata_func,
    text_content=False
)

documents = loader.load()
```

The `metadata_func` receives each document from the dataset and returns only the fields you need.

Since you'll use the `overview` field for semantic search, pass it as the `content_key` parameter. The `overview` field will be converted to an embedding vector and added to documents as the `_vectors` property.

## Adding documents to the database

Before adding documents to Meilisearch, configure `embeddings` as your embedder:

```python
# setup.py

# ...

vectorstore = Meilisearch(
    embedding=embeddings,
    embedders={
        "default": {
            "source": "userProvided",
            "dimensions": 1536,
        }
    },
    search_parameters={
        "hybrid": {
            "embedder": "default",
            "semanticRatio": 1.0,
        }
    }
)
```

`embedders` is a dictionary defining one or more embedders for your Meilisearch instance. Since you're using OpenAI embeddings with 1536 dimensions, set `dimensions` to `1536`.

In `search_parameters`, set `semanticRatio` to `1.0` to perform a purely semantic search. Setting it to `0.0` would perform a purely keyword-based search, and values between `0.0` and `1.0` would perform hybrid search with varying emphasis on semantic vs. keyword matching.

Finally, add the documents to Meilisearch:

```python
# setup.py

# ...

vectorstore.add_documents(documents)
```

Run `python setup.py` to add the documents to your database. This may take a few minutes.

## Searching

Once the documents are added, you can perform semantic searches.

Create a new file called `search.py`:

```python
# search.py

import os
from dotenv import load_dotenv
from langchain.vectorstores import Meilisearch
from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv()

if "MEILI_HTTP_ADDR" not in os.environ:
    raise Exception("Missing MEILI_HTTP_ADDR env var")
if "MEILI_API_KEY" not in os.environ:
    raise Exception("Missing MEILI_API_KEY env var")
if "OPENAI_API_KEY" not in os.environ:
    raise Exception("Missing OPENAI_API_KEY env var")

embeddings = OpenAIEmbeddings()

vectorstore = Meilisearch(
    embedding=embeddings,
)

query = "superhero movie"
docs = vectorstore.similarity_search(query)

print(docs[0].page_content)
```

Run `python search.py` to perform a similarity search. The application will return documents similar to your query.

## Conclusion

You've successfully implemented semantic search using LangChain and Meilisearch. You can now extend this application by:

* Adjusting the `semanticRatio` to experiment with hybrid search
* Adding more fields to your metadata for richer search results
* Implementing filters to narrow down results
* Using different embedding models

For more information, consult the [Meilisearch documentation](/learn/getting_started/quick_start) and [LangChain documentation](https://python.langchain.com/docs/get_started/introduction).
