# Configure Meilisearch at launch

**Source:** https://www.meilisearch.com/docs/learn/self_hosted/configure_meilisearch_at_launch.md
**Extrait le:** 2025-10-08
**Sujet:** Self-Hosted Configuration - Launch Options

---

# Configure Meilisearch at launch

> Configure Meilisearch at launch with command-line options, environment variables, or a configuration file.

export const NoticeTag = ({label}) => <span className="noticeTag noticeTag--{ label }">
    {label}
  </span>;

When self-hosting Meilisearch, you can configure your instance at launch with **command-line options**, **environment variables**, or a **configuration file**.

These startup options affect your entire Meilisearch instance, not just a single index. For settings that affect search within a single index, see [index settings](/reference/api/settings).

## Command-line options and flags

Pass **command-line options** and their respective values when launching a Meilisearch instance.

```bash
./meilisearch --db-path ./meilifiles --http-addr 'localhost:7700'
```

Some command-line options have both a long form and a short form, for example `--env` or `-e` for environment.

### Boolean command-line options

Pass **boolean** options as flags. If the flag is present, the option is set to `true`. If the flag is absent, the option is set to `false`.

```bash
# Enabling the option
./meilisearch --no-analytics

# Disabling the option
./meilisearch
```

## Environment variables

In a terminal, use the `export` command to set the environment variable:

```bash
export MEILI_DB_PATH=./meilifiles
export MEILI_HTTP_ADDR=localhost:7700
./meilisearch
```

If you're using a `.env` file:

```bash
MEILI_DB_PATH=./meilifiles
MEILI_HTTP_ADDR=localhost:7700
```

Then run:

```bash
./meilisearch
```

### Boolean environment variables

To enable a **boolean** environment variable, set it to `true`, `t`, `yes`, `y`, `1`, `on` or `enabled` (case-insensitive). Any other value will disable it.

```bash
# Enabling the option
export MEILI_NO_ANALYTICS=true

# Disabling the option
export MEILI_NO_ANALYTICS=false
```

## Configuration file

Use a configuration file to configure Meilisearch at launch. It must be in `.toml` format and passed using the `--config-file-path` command-line option.

```bash
./meilisearch --config-file-path ./config.toml
```

Configuration file example:

```toml
db_path = "./meilifiles"
http_addr = "localhost:7700"
```

### Boolean configuration file options

In a configuration file, **boolean** options are set using `true` or `false`.

```toml
# Enabling the option
no_analytics = true

# Disabling the option
no_analytics = false
```

## Option precedence

Options are applied in the following order of priority:

1. Command-line option
2. Environment variable
3. Configuration file
4. Default value

When an option is specified multiple times, the option with the highest priority takes effect.

For example, if `db_path` is specified both as a command-line option and an environment variable, Meilisearch will use the command-line option value.

## All instance options

The following options are available when configuring Meilisearch at launch. Every instance option has a default value that is used when the option is not specified at launch.

### General options

#### Config file path

**Command-line option**: `--config-file-path`
**Environment variable**: `MEILI_CONFIG_FILE_PATH`
**Default value**: none
**Expected value**: file path

Indicates the path of the configuration file to use. The file must be in `.toml` format.

```bash
./meilisearch --config-file-path ./config.toml
```

#### Database path

**Command-line option**: `--db-path`
**Environment variable**: `MEILI_DB_PATH`
**Configuration file variable**: `db_path`
**Default value**: `"data.ms/"`
**Expected value**: file path

Defines the location for the database files Meilisearch creates and uses. Meilisearch requires write access.

```bash
./meilisearch --db-path ./meilifiles
```

#### Environment

**Command-line option**: `--env`, `-e`
**Environment variable**: `MEILI_ENV`
**Configuration file variable**: `env`
**Default value**: `development`
**Expected value**: `production` or `development`

Sets the environment Meilisearch runs in.

In a **production** environment:
- The [web interface](/learn/getting_started/cloud_quick_start#search-preview) is disabled
- A [master key](/learn/security/basic_security#master-key) is required

```bash
./meilisearch --env production
```

#### HTTP address and port

**Command-line option**: `--http-addr`
**Environment variable**: `MEILI_HTTP_ADDR`
**Configuration file variable**: `http_addr`
**Default value**: `"localhost:7700"`
**Expected value**: HTTP address and port

Address and port Meilisearch uses. Meilisearch listens to this address.

```bash
./meilisearch --http-addr 'localhost:7700'
```

#### Master key

**Command-line option**: `--master-key`
**Environment variable**: `MEILI_MASTER_KEY`
**Configuration file variable**: `master_key`
**Default value**: none
**Expected value**: alphanumeric string (at least 16 bytes)

Sets the master key, automatically protecting all routes except [`GET /health`](/reference/api/health).

Master keys must be composed of:
- At least 16 bytes
- Valid UTF-8 characters
- Printable ASCII characters (0x20 to 0x7E), excluding control characters

```bash
./meilisearch --master-key "WORKINGmasterKEY123456789"
```

For more information about security and master keys, see the [security guide](/learn/security/basic_security).

#### Disable analytics

**Command-line option**: `--no-analytics`
**Environment variable**: `MEILI_NO_ANALYTICS`
**Configuration file variable**: `no_analytics`
**Default value**: `false`
**Expected value**: `true` or `false`

Deactivates Meilisearch's analytics. Analytics help us understand how you use Meilisearch. To learn more, see our [dedicated analytics page](/learn/analytics/send_data_to_meilisearch_cloud).

```bash
./meilisearch --no-analytics
```

### Advanced options

#### Disable auto-batching

**Command-line option**: `--experimental-enable-auto-batching`
**Environment variable**: `MEILI_EXPERIMENTAL_ENABLE_AUTO_BATCHING`
**Configuration file variable**: `experimental_enable_auto_batching`
**Default value**: `true`
**Expected value**: `true` or `false`

<NoticeTag label="Experimental" />

Activates or deactivates auto-batching. Auto-batching is activated by default. Use `false` to deactivate.

When activated, Meilisearch will attempt to join consecutive tasks together and process them at once. This can significantly improve performance in write-heavy workloads.

```bash
./meilisearch --experimental-enable-auto-batching=false
```

#### Experimental logs mode

**Command-line option**: `--experimental-logs-mode`
**Environment variable**: `MEILI_EXPERIMENTAL_LOGS_MODE`
**Configuration file variable**: `experimental_logs_mode`
**Default value**: none
**Expected value**: `human`, `json`, or `profile`

<NoticeTag label="Experimental" />

Defines the mode for Meilisearch logs.

**Available modes**:
- `human` (default): Human-readable, colorized logs
- `json`: JSON-formatted logs for structured logging and parsing
- `profile`: Detailed profiling logs for performance analysis

```bash
./meilisearch --experimental-logs-mode json
```

#### Experimental reduce indexing memory usage

**Command-line option**: `--experimental-reduce-indexing-memory-usage`
**Environment variable**: `MEILI_EXPERIMENTAL_REDUCE_INDEXING_MEMORY_USAGE`
**Configuration file variable**: `experimental_reduce_indexing_memory_usage`
**Default value**: `false`
**Expected value**: `true` or `false`

<NoticeTag label="Experimental" />

Activates or deactivates experimental memory usage reduction during indexing.

When activated, Meilisearch uses less memory during indexing, which can help on machines with limited RAM. However, this usually results in slower indexing.

```bash
./meilisearch --experimental-reduce-indexing-memory-usage
```

#### Log level

**Command-line option**: `--log-level`
**Environment variable**: `MEILI_LOG_LEVEL`
**Configuration file variable**: `log_level`
**Default value**: `'INFO'`
**Expected value**: `'OFF'`, `'ERROR'`, `'WARN'`, `'INFO'`, `'DEBUG'`, or `'TRACE'`

Defines how much detail Meilisearch should return in its logs.

Available log levels, from least to most verbose:
- `'OFF'`: No logs
- `'ERROR'`: Only errors
- `'WARN'`: Errors and warnings
- `'INFO'`: Errors, warnings, and basic information
- `'DEBUG'`: All of the above, plus debugging information
- `'TRACE'`: All of the above, plus very detailed tracing information

```bash
./meilisearch --log-level 'WARN'
```

#### Max indexing memory

**Command-line option**: `--max-indexing-memory`
**Environment variable**: `MEILI_MAX_INDEXING_MEMORY`
**Configuration file variable**: `max_indexing_memory`
**Default value**: 2/3 of available memory
**Expected value**: amount of RAM as an integer, followed by a unit (`KB`, `MB`, `GB`, `TB`, or `PB`)

Sets the maximum memory Meilisearch can use when indexing. By default, Meilisearch uses no more than 2/3 of available memory.

```bash
./meilisearch --max-indexing-memory '2GiB'
```

The value must be an integer followed by a unit:
- `KB`: kilobytes
- `MB`: megabytes
- `GB`: gigabytes
- `TB`: terabytes
- `PB`: petabytes

Additionally:
- Use binary units like `KiB`, `MiB`, `GiB`, `TiB`, or `PiB` for binary units (1024-based)
- Use decimal units like `KB`, `MB`, `GB`, `TB`, or `PB` for decimal units (1000-based)

Setting `max_indexing_memory` to a higher value can improve indexing speed, at the cost of increased memory usage. Setting it to a lower value can decrease RAM usage, but will negatively impact indexing performance.

#### Max indexing threads

**Command-line option**: `--max-indexing-threads`
**Environment variable**: `MEILI_MAX_INDEXING_THREADS`
**Configuration file variable**: `max_indexing_threads`
**Default value**: half of available threads
**Expected value**: positive integer

Sets the maximum number of threads Meilisearch can use for indexing. By default, Meilisearch uses half of available threads.

```bash
./meilisearch --max-indexing-threads 4
```

Setting `max_indexing_threads` to a higher value can improve indexing speed, at the cost of increased CPU usage. Setting it to a lower value can decrease CPU usage, but will negatively impact indexing performance.

If the value is higher than the available number of threads, Meilisearch will use all available threads.

#### Max task database size

**Command-line option**: `--max-task-db-size`
**Environment variable**: `MEILI_MAX_TASK_DB_SIZE`
**Configuration file variable**: `max_task_db_size`
**Default value**: `"100GiB"`
**Expected value**: amount of disk space as an integer, followed by a unit (`KB`, `MB`, `GB`, `TB`, or `PB`)

Sets the maximum size Meilisearch's task database can reach.

```bash
./meilisearch --max-task-db-size '1GiB'
```

The value must be an integer followed by a unit:
- `KB`: kilobytes
- `MB`: megabytes
- `GB`: gigabytes
- `TB`: terabytes
- `PB`: petabytes

Additionally:
- Use binary units like `KiB`, `MiB`, `GiB`, `TiB`, or `PiB` for binary units (1024-based)
- Use decimal units like `KB`, `MB`, `GB`, `TB`, or `PB` for decimal units (1000-based)

#### Payload limit size

**Command-line option**: `--http-payload-size-limit`
**Environment variable**: `MEILI_HTTP_PAYLOAD_SIZE_LIMIT`
**Configuration file variable**: `http_payload_size_limit`
**Default value**: `"100MB"`
**Expected value**: amount of data as an integer, followed by a unit (`KB`, `MB`, `GB`, or `TB`)

Sets the maximum size of accepted JSON payloads. Meilisearch will refuse requests larger than the specified limit.

```bash
./meilisearch --http-payload-size-limit '200MB'
```

The value must be an integer followed by a unit:
- `KB`: kilobytes
- `MB`: megabytes
- `GB`: gigabytes
- `TB`: terabytes

Additionally:
- Use binary units like `KiB`, `MiB`, `GiB`, or `TiB` for binary units (1024-based)
- Use decimal units like `KB`, `MB`, `GB`, or `TB` for decimal units (1000-based)

#### SSL options

##### SSL authentication path

**Command-line option**: `--ssl-auth-path`
**Environment variable**: `MEILI_SSL_AUTH_PATH`
**Configuration file variable**: `ssl_auth_path`
**Default value**: none
**Expected value**: file path

Enables client authentication, requiring clients to provide a valid client certificate when connecting.

This path must point to a valid PKCS12 archive (`.p12` or `.pfx`) or a PEM certificate chain (`.crt`, `.pem`).

```bash
./meilisearch --ssl-auth-path './path/to/client-cert.p12'
```

##### SSL certificate path

**Command-line option**: `--ssl-cert-path`
**Environment variable**: `MEILI_SSL_CERT_PATH`
**Configuration file variable**: `ssl_cert_path`
**Default value**: none
**Expected value**: file path

Sets the SSL certificate file. Meilisearch uses this certificate when clients connect.

This path must point to a valid PEM-formatted certificate (`.crt`, `.pem`). This can be a chain of certificates.

```bash
./meilisearch --ssl-cert-path './path/to/server-cert.pem'
```

##### SSL key path

**Command-line option**: `--ssl-key-path`
**Environment variable**: `MEILI_SSL_KEY_PATH`
**Configuration file variable**: `ssl_key_path`
**Default value**: none
**Expected value**: file path

Sets the SSL key file. Meilisearch uses this key when clients connect.

This path must point to a valid PEM-formatted private key (`.key`, `.pem`).

```bash
./meilisearch --ssl-key-path './path/to/server-key.pem'
```

##### SSL OCSP path

**Command-line option**: `--ssl-ocsp-path`
**Environment variable**: `MEILI_SSL_OCSP_PATH`
**Configuration file variable**: `ssl_ocsp_path`
**Default value**: none
**Expected value**: file path

Sets the SSL OCSP file. Used for OCSP stapling.

This path must point to a valid DER-encoded OCSP response.

```bash
./meilisearch --ssl-ocsp-path './path/to/ocsp-response.der'
```

##### SSL require auth

**Command-line option**: `--ssl-require-auth`
**Environment variable**: `MEILI_SSL_REQUIRE_AUTH`
**Configuration file variable**: `ssl_require_auth`
**Default value**: `false`
**Expected value**: `true` or `false`

Makes SSL client authentication mandatory. Clients must provide a valid certificate.

Only works if [`--ssl-auth-path`](#ssl-authentication-path) is also defined.

```bash
./meilisearch --ssl-require-auth --ssl-auth-path './path/to/client-cert.p12'
```

##### SSL resumption

**Command-line option**: `--ssl-resumption`
**Environment variable**: `MEILI_SSL_RESUMPTION`
**Configuration file variable**: `ssl_resumption`
**Default value**: `false`
**Expected value**: `true` or `false`

Activates SSL session resumption. This can improve performance when clients make multiple connections.

```bash
./meilisearch --ssl-resumption
```

##### SSL tickets

**Command-line option**: `--ssl-tickets`
**Environment variable**: `MEILI_SSL_TICKETS`
**Configuration file variable**: `ssl_tickets`
**Default value**: `false`
**Expected value**: `true` or `false`

Activates SSL tickets. This can improve performance when clients make multiple connections.

```bash
./meilisearch --ssl-tickets
```

#### Task webhook URL

**Command-line option**: `--task-webhook-url`
**Environment variable**: `MEILI_TASK_WEBHOOK_URL`
**Configuration file variable**: `task_webhook_url`
**Default value**: none
**Expected value**: URL

Sets a URL Meilisearch calls whenever a task finishes processing. The task data is sent in the request body.

```bash
./meilisearch --task-webhook-url 'https://example.com/webhook'
```

For more information, see [task webhooks](/learn/tasks/task_webhook).

#### Task webhook authorization header

**Command-line option**: `--task-webhook-authorization-header`
**Environment variable**: `MEILI_TASK_WEBHOOK_AUTHORIZATION_HEADER`
**Configuration file variable**: `task_webhook_authorization_header`
**Default value**: none
**Expected value**: string

Value Meilisearch includes in the `Authorization` header when calling the task webhook URL.

```bash
./meilisearch --task-webhook-authorization-header 'Bearer token123'
```

For more information, see [task webhooks](/learn/tasks/task_webhook).