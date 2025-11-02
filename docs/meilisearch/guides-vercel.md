# Integrate Meilisearch Cloud with Vercel

**Source:** https://www.meilisearch.com/docs/guides/vercel.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Vercel Integration

---

# Integrate Meilisearch Cloud with Vercel

> Link Meilisearch Cloud to a Vercel Project.

In this guide you will learn how to link a [Meilisearch Cloud](https://www.meilisearch.com/cloud?utm_campaign=oss\&utm_source=docs\&utm_medium=vercel-integration) instance to your Vercel project.

## Introducing our tools

### What is Vercel?

[Vercel](https://vercel.com/) is a cloud platform for building and deploying web applications. It works out of the box with most popular web development tools.

### What is Meilisearch Cloud?

[Meilisearch Cloud](https://www.meilisearch.com/cloud?utm_campaign=oss\&utm_source=docs\&utm_medium=vercel-integration) offers a managed search service that is scalable, reliable, and designed to meet the needs of all companies.

## Integrate Meilisearch into your Vercel project

### Create and deploy a Vercel project

From your Vercel dashboard, create a new project. You can create a project from a template, or import a Git repository.

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/vercel/01.create-new-project-on-vercel-dashboard.png?fit=max&auto=format&n=JZ1wsU7CEWrp9Xec&q=85&s=6e15dd4e0c4e249c51b51fec3055c98c" alt="Create a new project on Vercel dashboard" data-og-width="3170" width="3170" data-og-height="2192" height="2192" data-path="assets/images/vercel/01.create-new-project-on-vercel-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/vercel/01.create-new-project-on-vercel-dashboard.png?fit=max&auto=format&n=JZ1wsU7CEWrp9Xec&q=85&s=6e15dd4e0c4e249c51b51fec3055c98c 3170w" sizes="100vw">
</Frame>

After configuring your project settings, deploy it by clicking the "Deploy" button.

### Create a Meilisearch Cloud project

From the [Meilisearch Cloud dashboard](https://cloud.meilisearch.com/projects), create a new project by clicking on "+ New project".

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/vercel/02.create-project-meilisearch-cloud.png?fit=max&auto=format&n=JZ1wsU7CEWrp9Xec&q=85&s=b30f7e8e8e0b8e0b7e0b8e0b7e0b8e0b" alt="Create a Meilisearch Cloud project" data-og-width="3170" width="3170" data-og-height="2192" height="2192" data-path="assets/images/vercel/02.create-project-meilisearch-cloud.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/vercel/02.create-project-meilisearch-cloud.png?fit=max&auto=format&n=JZ1wsU7CEWrp9Xec&q=85&s=b30f7e8e8e0b8e0b7e0b8e0b7e0b8e0b 3170w" sizes="100vw">
</Frame>

Select a region, a plan and give your project a name. Then click on "Create".

### Connect Meilisearch Cloud to your Vercel project

Navigate to the "Integrations" tab in your Meilisearch Cloud project and click the "Install" button under "Vercel".

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/vercel/03.install-vercel-integration.png?fit=max&auto=format&n=JZ1wsU7CEWrp9Xec&q=85&s=a30f7e8e8e0b8e0b7e0b8e0b7e0b8e0b" alt="Install Vercel integration" data-og-width="3170" width="3170" data-og-height="2192" height="2192" data-path="assets/images/vercel/03.install-vercel-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/vercel/03.install-vercel-integration.png?fit=max&auto=format&n=JZ1wsU7CEWrp9Xec&q=85&s=a30f7e8e8e0b8e0b7e0b8e0b7e0b8e0b 3170w" sizes="100vw">
</Frame>

You will be redirected to the Vercel integration page. Select your Vercel account and click "Add Integration".

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/vercel/04.add-integration.png?fit=max&auto=format&n=JZ1wsU7CEWrp9Xec&q=85&s=930f7e8e8e0b8e0b7e0b8e0b7e0b8e0b" alt="Add Vercel integration" data-og-width="3170" width="3170" data-og-height="2192" height="2192" data-path="assets/images/vercel/04.add-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/vercel/04.add-integration.png?fit=max&auto=format&n=JZ1wsU7CEWrp9Xec&q=85&s=930f7e8e8e0b8e0b7e0b8e0b7e0b8e0b 3170w" sizes="100vw">
</Frame>

Choose the Vercel project you want to connect to your Meilisearch Cloud project and click "Continue".

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/vercel/05.select-vercel-project.png?fit=max&auto=format&n=JZ1wsU7CEWrp9Xec&q=85&s=830f7e8e8e0b8e0b7e0b8e0b7e0b8e0b" alt="Select Vercel project" data-og-width="3170" width="3170" data-og-height="2192" height="2192" data-path="assets/images/vercel/05.select-vercel-project.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/vercel/05.select-vercel-project.png?fit=max&auto=format&n=JZ1wsU7CEWrp9Xec&q=85&s=830f7e8e8e0b8e0b7e0b8e0b7e0b8e0b 3170w" sizes="100vw">
</Frame>

The integration will create environment variables for your Vercel project. Review them and click "Add Integration".

<Frame>
  <img src="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/vercel/06.review-environment-variables.png?fit=max&auto=format&n=JZ1wsU7CEWrp9Xec&q=85&s=730f7e8e8e0b8e0b7e0b8e0b7e0b8e0b" alt="Review environment variables" data-og-width="3170" width="3170" data-og-height="2192" height="2192" data-path="assets/images/vercel/06.review-environment-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/meilisearch-6b28dec2/JZ1wsU7CEWrp9Xec/assets/images/vercel/06.review-environment-variables.png?fit=max&auto=format&n=JZ1wsU7CEWrp9Xec&q=85&s=730f7e8e8e0b8e0b7e0b8e0b7e0b8e0b 3170w" sizes="100vw">
</Frame>

The following environment variables will be added to your Vercel project:

- `MEILISEARCH_HOST`: The URL of your Meilisearch Cloud instance
- `MEILISEARCH_ADMIN_API_KEY`: The admin API key for your Meilisearch Cloud instance
- `MEILISEARCH_SEARCH_API_KEY`: The search API key for your Meilisearch Cloud instance

You can now use these environment variables in your Vercel project to connect to your Meilisearch Cloud instance.

## Conclusion

You have successfully integrated Meilisearch Cloud with your Vercel project. You can now use Meilisearch to add search to your Vercel application.

For more information on how to use Meilisearch, check out our [documentation](https://www.meilisearch.com/docs).
