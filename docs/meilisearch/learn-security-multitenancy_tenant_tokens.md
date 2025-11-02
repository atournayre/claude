# Multitenancy and tenant tokens

**Source:** https://www.meilisearch.com/docs/learn/security/multitenancy_tenant_tokens.md
**Extrait le:** 2025-10-08
**Sujet:** Security - Multi-tenant Architecture

---

# Multitenancy and tenant tokens

> In this article you'll read what multitenancy is and how tenant tokens help managing complex applications and sensitive data.

In this article you'll read what multitenancy is and how tenant tokens help managing complex applications and sensitive data.

## What is multitenancy?

In software development, multitenancy means that multiple users or tenants share the same computing resources with different levels of access to system-wide data. Proper multitenancy is crucial in cloud computing services such as [DigitalOcean's Droplets](https://www.digitalocean.com/products/droplets) and [Amazon's AWS](https://aws.amazon.com/).

If your Meilisearch application stores sensitive data belonging to multiple users in the same index, you are managing a multi-tenant index. In this context, it is very important to make sure users can only search through their own documents. This can be accomplished with **tenant tokens**.

## What is a tenant token?

Tenant tokens are small packages of encrypted data presenting proof a user can access a certain index. They contain not only security credentials, but also instructions on which documents within that index the user is allowed to see. **Tenant tokens only give access to the search endpoints.** They are meant to be short-lived, so Meilisearch does not store nor keep track of generated tokens.

## What is the difference between tenant tokens and API keys?

API keys give general access to specific actions in an index. An API key with search permissions for a given index can access all information in that index.

Tenant tokens add another layer of control over API keys. They can restrict which information a specific user has access to in an index. If you store private data from multiple customers in a single index, tenant tokens allow you to prevent one user from accessing another's data.

## How to integrate tenant tokens with an application?

Tenant tokens do not require any specific Meilisearch configuration. You can use them exactly the same way as you would use any API key with search permissions.

You must generate tokens in your application. The quickest method to generate tenant tokens is [using an official SDK](/learn/security/generate_tenant_token_sdk). It is also possible to [generate a token with a third-party library](/learn/security/generate_tenant_token_third_party).

## Sample
