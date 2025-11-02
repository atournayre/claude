# Contributing to our documentation

**Source:** https://www.meilisearch.com/docs/learn/resources/contributing_docs.md
**Extrait le:** 2025-10-08
**Sujet:** Resources - Contributing to Documentation

---

# Contributing to our documentation

> The Meilisearch documentation is open-source. Learn how to help make it even better.

This documentation website is hosted in a [public GitHub repository](https://github.com/meilisearch/documentation). It is built with [Next.js](https://nextjs.org), written in [MDX](https://mdxjs.com), and deployed on [Vercel](https://www.vercel.com).

## Our documentation philosophy

Our documentation aims to be:

* **Efficient**: we don't want to waste anyone's time
* **Accessible**: reading the texts here shouldn't require native English or a computer science degree
* **Thorough**: the documentation website should contain all information anyone needs to use Meilisearch
* **Open source**: this is a resource by Meilisearch users, for Meilisearch users

## Documentation repository and local development

The Meilisearch documentation repository only stores the content of the docs website. Because the code that makes up the website lives in another repository, **it is not possible to run a local copy of the documentation**.

### Handling images and other static assets

When contributing content to the Meilisearch docs, store screenshots, images, GIFs, and videos in the relevant directory under `/assets`.

The build process does not currently support static assets with relative paths. When adding them to a document, make sure the asset URL points to the raw GitHub file address:

```markdown
\!\[Image description\]\(https://raw.githubusercontent.com/meilisearch/documentation/[branch_name]/assets/images/[guide_name]/diagram.png\)
```

## How to contribute?

### Issues

The maintainers of Meilisearch's documentation use [GitHub Issues](https://github.com/meilisearch/documentation/issues/new) to track tasks. Helpful issues include:

* Notify the docs team about content that is inaccurate, outdated, or confusing
* Requests for new features such as versioning or an embedded console
* Requests for new content such as new guides and tutorials

Before opening an issue or PR, please look through our [open issues](https://github.com/meilisearch/documentation/issues) to see if one already exists for
