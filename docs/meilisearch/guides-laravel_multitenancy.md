# Laravel multitenancy guide

**Source:** https://www.meilisearch.com/docs/guides/laravel_multitenancy.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Laravel Multitenancy

---

# Laravel multitenancy guide

> Learn how to implement secure, multitenant search in your Laravel applications.

This guide will walk you through implementing search in a multitenant Laravel application. We'll use the example of a customer relationship manager (CRM) application that allows users to store contacts.

## Requirements

This guide requires:

* A Laravel 10 application with [Laravel Scout](https://laravel.com/docs/10.x/scout) configured to use the `meilisearch` driver
* A Meilisearch server running — see our [quick start](/learn/getting_started/cloud_quick_start)
* A search API key — available in your Meilisearch dashboard
* A search API key UID — retrieve it using the [keys endpoints](/reference/api/keys)

<Tip>
  Prefer self-hosting? Read our [installation guide](/learn/self_hosted/install_meilisearch_locally).
</Tip>

## Models & relationships

Our example CRM is a multitenant application, where each user can only access data belonging to their organization.

On a technical level, this means:

* A `User` model that belongs to an `Organization`
* A `Contact` model that belongs to an `Organization` (can only be accessed by users from the same organization)
* An `Organization` model that has many `User`s and many `Contact`s

With that in mind, the first step is to define such these models and their relationship:

In `app/Models/Contact.php`:

```php
<?php

namespace App\Models;

use Laravel\Scout\Searchable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Contact extends Model
{
    use Searchable;

    public function organization(): BelongsTo
    {
        return $this->belongsTo(Organization::class, 'organization_id');
    }
}
```

In `app/Models/User.php`:

```php
<?php

namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Sanctum\HasApiTokens;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class User extends Authenticatable
{
    use HasApiTokens, Notifiable;

    public function organization(): BelongsTo
    {
        return $this->belongsTo(Organization::class, 'organization_id');
    }
}
```

In `app/Models/Organization.php`:

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Organization extends Model
{
    public function users(): HasMany
    {
        return $this->hasMany(User::class, 'organization_id');
    }

    public function contacts(): HasMany
    {
        return $this->hasMany(Contact::class, 'organization_id');
    }
}
```

## Generating tenant tokens

[Tenant tokens](/learn/security/tenant_tokens) are JWTs containing security rules. These allow you to enforce per-user access control at search time.

Since we want to ensure users can only search contacts from their own organization, we'll create an `organization_id` filter. When Meilisearch receives this token, it will automatically apply the filter to all search queries.

Create a new controller in `app/Http/Controllers/TenantTokenController.php`:

```php
<?php

namespace App\Http\Controllers;

use Meilisearch\Meilisearch;
use Illuminate\Http\Request;

class TenantTokenController extends Controller
{
    public function generate(Request $request)
    {
        $user = $request->user();
        $client = new Meilisearch(
            config('scout.meilisearch.host'),
            config('scout.meilisearch.key')
        );

        // Create search rules for this user's organization
        $searchRules = [
            'contacts' => [
                'filter' => 'organization_id = ' . $user->organization_id
            ]
        ];

        // Generate a tenant token that expires in 1 hour
        $tenantToken = $client->generateTenantToken(
            config('scout.meilisearch.key_uid'), // Your search API key UID
            $searchRules,
            [
                'expiresAt' => now()->addHour()
            ]
        );

        return response()->json([
            'token' => $tenantToken
        ]);
    }
}
```

Register this controller in your `routes/web.php`:

```php
use App\Http\Controllers\TenantTokenController;

Route::middleware('auth')->group(function () {
    Route::get('/tenant-token', [TenantTokenController::class, 'generate']);
});
```

## Using tenant tokens with Laravel Blade

Now that we can generate tenant tokens, we need to pass them to our search UI. The easiest way is through a Blade component.

Create a new Blade component in `resources/views/components/search.blade.php`:

```blade
<div x-data="searchComponent()" x-init="init()">
    <input
        type="search"
        x-model="query"
        @input.debounce.300ms="search()"
        placeholder="Search contacts..."
        class="form-control"
    />

    <div x-show="results.length > 0" class="search-results">
        <template x-for="result in results" :key="result.id">
            <div class="search-result">
                <h4 x-text="result.name"></h4>
                <p x-text="result.email"></p>
            </div>
        </template>
    </div>
</div>

<script>
function searchComponent() {
    return {
        query: '',
        results: [],
        tenantToken: null,
        client: null,

        async init() {
            // Fetch the tenant token
            const response = await fetch('/tenant-token');
            const data = await response.json();
            this.tenantToken = data.token;

            // Initialize Meilisearch client with tenant token
            this.client = new MeiliSearch({
                host: '{{ config('scout.meilisearch.host') }}',
                apiKey: this.tenantToken
            });
        },

        async search() {
            if (!this.query) {
                this.results = [];
                return;
            }

            const index = this.client.index('contacts');
            const searchResults = await index.search(this.query);
            this.results = searchResults.hits;
        }
    }
}
</script>
```

Don't forget to include the Meilisearch JavaScript SDK and Alpine.js in your layout:

```blade
<!-- In your layout file -->
<script src="https://cdn.jsdelivr.net/npm/meilisearch@latest/dist/bundles/meilisearch.umd.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
```

## Building the search UI

Finally, use the search component in your views:

```blade
@extends('layouts.app')

@section('content')
    <div class="container">
        <h1>Contacts</h1>

        <x-search />

        <!-- Your other content -->
    </div>
@endsection
```

## Configuring the Contact model for search

Make sure your `Contact` model's `toSearchableArray()` method includes the `organization_id`:

```php
public function toSearchableArray()
{
    return [
        'id' => $this->id,
        'name' => $this->name,
        'email' => $this->email,
        'organization_id' => $this->organization_id,
    ];
}
```

Also ensure the `organization_id` is configured as a filterable attribute in Meilisearch. You can do this via the dashboard or programmatically:

```php
use Meilisearch\Client;

$client = new Client(config('scout.meilisearch.host'), config('scout.meilisearch.key'));
$client->index('contacts')->updateFilterableAttributes(['organization_id']);
```

## Conclusion

You now have a secure multitenant search implementation in your Laravel application. Each user can only search contacts from their own organization, enforced at the search engine level using tenant tokens.

Key takeaways:

* Tenant tokens provide secure, per-user access control
* Filters are automatically applied at search time
* No backend queries needed for authorization
* Tokens can expire for added security

For more information, check out our [tenant tokens documentation](/learn/security/tenant_tokens).
