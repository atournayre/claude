# Ruby on Rails quick start

**Source:** https://www.meilisearch.com/docs/guides/ruby_on_rails_quick_start.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Integration Ruby on Rails

---

# Ruby on Rails quick start

> Integrate Meilisearch into your Ruby on Rails app.

Integrate Meilisearch into your Ruby on Rails app.

## 1. Create a Meilisearch project

[Create a project](https://cloud.meilisearch.com) in the Meilisearch Cloud dashboard. Check out our [getting started guide](/learn/getting_started/cloud_quick_start) for step-by-step instructions.

If you prefer to use the self-hosted version of Meilisearch, you can follow the [quick start](https://www.meilisearch.com/docs/learn/self_hosted/getting_started_with_self_hosted_meilisearch) tutorial.

## 2. Create a Rails app

Ensure your environment uses at least Ruby 2.7.0 and Rails 6.1.

```bash
rails new blog
```

## 3. Install the meilisearch-rails gem

Navigate to your Rails app and install the `meilisearch-rails` gem.

```bash
bundle add meilisearch-rails
```

## 4. Add your Meilisearch credentials

Run the following command to create a `config/initializers/meilisearch.rb` file.

```bash
bin/rails meilisearch:install
```

Then add your Meilisearch URL and [Default Admin API Key](/learn/security/basic_security#obtaining-api-keys). On Meilisearch Cloud, you can find your credentials in your project settings.

```Ruby
MeiliSearch::Rails.configuration = {
  meilisearch_url: '<your Meilisearch URL>',
  meilisearch_api_key: '<your Meilisearch API key>'
}
```

## 5. Generate the model and run the database migration

Create an example `Article` model and generate the migration files.

```bash
bin/rails generate model Article title:string body:text

bin/rails db:migrate
```

## 6. Index your model into Meilisearch

Include the `MeiliSearch::Rails` module and the `meilisearch` block.

```Ruby
class Article < ApplicationRecord
  include MeiliSearch::Rails

  meilisearch do
    attribute :title, :body
  end
end
```

**Note:** Le contenu complet de cette page semble avoir été tronqué lors de l'extraction. Consulter la source originale pour la documentation complète.
