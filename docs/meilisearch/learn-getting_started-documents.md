# Documents

**Source:** https://www.meilisearch.com/docs/learn/getting_started/documents.md
**Extrait le:** 2025-10-08
**Sujet:** Getting Started - Documents

---

# Documents

> Documents are the individual items that make up a dataset. Each document is an object composed of one or more fields.

A document is an object composed of one or more fields. Each field consists of an **attribute** and its associated **value**. Documents function as containers for organizing data and are the basic building blocks of a Meilisearch database. To search for a document, you must first add it to an [index](/learn/getting_started/indexes).

Nothing will be shared between two indexes if they contain the exact same document. Instead, both documents will be treated as different documents. Depending on the [index's settings](/reference/api/settings), the documents might have different sizes.

## Structure

[Image of document structure diagram]

### Important terms

* **Document**: an object which contains data in the form of one or more fields
* **[Field](#fields)**: a set of two data items that are linked together: an attribute and a value
* **Attribute**: the first part of a field. Acts as a name or description for its associated value
* **Value**: the second part of a field, consisting of data of any valid JSON type
* **[Primary Field](#primary-field)**: a special field that is mandatory in all documents. It contains the primary key and document identifier

## Fields

A **field** is a set of two data items linked together: an attribute and a value. Documents are made up of fields.

An **attribute** is a case-sensitive string that functions as a field's name and allows you to store, access, and describe data.

That data is the field's **value**. Every field has a data type dictated by its value. Every value must be a valid [JSON data type](https://www.w3schools.com/js/js_json_datatypes.asp).

If the value is a string, it **[can contain at most 65535 positions](/learn/resources/known_limitations#maximum-number-of-words-per-attribute)**. Words exceeding the 65535 position limit will be ignored.

If a field contains an object, Meilisearch flattens it during indexing using dot notation and brings the object's keys and values to the root level of the document itself.
