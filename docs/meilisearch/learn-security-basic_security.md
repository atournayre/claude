# Securing your project

**Source:** https://www.meilisearch.com/docs/learn/security/basic_security.md
**Extrait le:** 2025-10-08
**Sujet:** Security - Basic security implementation

---

# Securing your project

> This tutorial will show you how to secure your Meilisearch project.

This tutorial will show you how to secure your Meilisearch project. You will see how to manage your master key and how to safely send requests to the Meilisearch API using an API key.

## Creating the master key

The master key is the first and most important step to secure your Meilisearch project.

### Creating the master key in Meilisearch Cloud

Meilisearch Cloud automatically generates a master key for each project. This means Meilisearch Cloud projects are secure by default.

You can view your master key by visiting your project settings, then clicking "API Keys" on the sidebar:

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/pdzkg8J6JAejKYyu/assets/images/security/01-master-api-keys.png?fit=max&auto=format&n=pdzkg8J6JAejKYyu&q=85&s=40a99ee767aded0f531c51662260f709" alt="An interface element named 'API keys' showing obscured security keys including: 'Master key', 'Default Search API Key', and 'Default Admin API Key'" data-og-width="1356" width="1356" data-og-height="694" height="694" data-path="assets/images/security/01-master-api-keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/meilisearch-6b28dec2/pdzkg8J6JAejKYyu/assets/images/security/01-master-api-keys.png?w=280&fit=max&auto=format&n=pdzkg8J6JAejKYyu&q=85&s=11613845b13d8e618b04ed52c82a8d83 280w, https://mintcdn.com/meilisearch-6b28dec2/pdzkg8J6JAejKYyu/assets/images/security/01-master-api-keys.png?w=560
