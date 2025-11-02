# Install Meilisearch locally

**Source:** https://www.meilisearch.com/docs/learn/self_hosted/install_meilisearch_locally.md
**Extrait le:** 2025-10-08
**Sujet:** Self-Hosted - Installation locale

---

# Install Meilisearch locally

> Use Meilisearch with either Meilisearch Cloud, another cloud service, or install it locally.

You can install Meilisearch locally or deploy it over a cloud service.

## Meilisearch Cloud

[Meilisearch Cloud](https://www.meilisearch.com/cloud?utm_campaign=oss&utm_source=docs&utm_medium=installation-guide) greatly simplifies installing, maintaining, and updating Meilisearch. [Get started with a 14-day free trial](https://cloud.meilisearch.com/register?utm_campaign=oss&utm_source=docs&utm_medium=installation-guide).

Take a look at our [Meilisearch Cloud tutorial](/learn/getting_started/cloud_quick_start) for more information on setting up and using Meilisearch's cloud service.

## Local installation

### cURL

Download the **latest stable release** of Meilisearch with **cURL**.

Launch Meilisearch to start the server.

```bash
# Install Meilisearch
curl -L https://install.meilisearch.com | sh

# Launch Meilisearch
./meilisearch
```

### Homebrew

Download the **latest stable release** of Meilisearch with **[Homebrew](https://brew.sh/)**, a package manager for MacOS.

Launch Meilisearch to start the server.

```bash
# Update brew and install Meilisearch
brew update && brew install meilisearch

# Launch Meilisearch
meilisearch
```

### Docker

When using **Docker**, you can run [any tag available in our official Docker image](https://hub.docker.com/r/getmeili/meilisearch/tags).

These commands launch the **latest stable release** of Meilisearch.

```bash
# Fetch the latest version of Meilisearch image from DockerHub
docker pull getmeili/meilisearch:latest

# Launch Meilisearch in development mode with a master key
docker run -it --rm \
    -p 7700:7700 \
    -e MEILI_ENV='development' \
    -v $(pwd)/meili_data:/meili_data \
    getmeili/meilisearch:latest
```

### APT (Debian/Ubuntu)

Download the **latest stable release** of Meilisearch with **APT**.

```bash
# Add Meilisearch package
echo "deb [trusted=yes] https://apt.fury.io/meilisearch/ /" | sudo tee /etc/apt/sources.list.d/fury.list

# Update APT and install Meilisearch
sudo apt update && sudo apt install meilisearch
```

### Source

Meilisearch is written in `Rust`. To compile it, [install the Rust toolchain](https://www.rust-lang.org/tools/install).

If the Rust toolchain is already installed, clone the repository and compile Meilisearch.

```bash
git clone https://github.com/meilisearch/meilisearch
cd meilisearch
cargo build --release

# Execute the server binary
./target/release/meilisearch
```

### Windows

Download the **latest stable release** of Meilisearch for Windows.

```powershell
# Download Meilisearch
Invoke-WebRequest -Uri "https://github.com/meilisearch/meilisearch/releases/latest/download/meilisearch-windows-amd64.exe" -OutFile "meilisearch.exe"

# Launch Meilisearch
.\meilisearch.exe
```

### Direct download

Download the **latest stable release** from the [GitHub releases page](https://github.com/meilisearch/meilisearch/releases/latest).

After downloading, make the binary executable and launch Meilisearch.

```bash
# Give execute permission
chmod +x meilisearch

# Launch Meilisearch
./meilisearch
```

## Environment and configuration

Meilisearch supports a number of [configuration options](/reference/api/settings) you can set via the command line, environment variables, or a configuration file.

### Master key

In a production environment, a master key is mandatory. Without one, Meilisearch will refuse to start.

Set the master key using the `--master-key` option or the `MEILI_MASTER_KEY` environment variable:

```bash
./meilisearch --master-key="YOUR_MASTER_KEY"
```

### Database path

By default, Meilisearch stores its database in a folder called `data.ms` in the same directory as the Meilisearch binary.

Configure the database path with `--db-path` or `MEILI_DB_PATH`:

```bash
./meilisearch --db-path="./my_database"
```

### HTTP address and port

By default, Meilisearch listens on `127.0.0.1:7700`.

Configure the address and port with `--http-addr` or `MEILI_HTTP_ADDR`:

```bash
./meilisearch --http-addr="0.0.0.0:7700"
```

### Environment

Meilisearch can run in `development` or `production` mode:

- **Development mode**: Lighter on security, ideal for local testing
- **Production mode**: Enhanced security requirements, requires a master key

Set the environment with `--env` or `MEILI_ENV`:

```bash
./meilisearch --env="production" --master-key="YOUR_MASTER_KEY"
```

## Updating Meilisearch

To update Meilisearch, download the latest binary or Docker image and replace the old one. Your data will be preserved across updates.

For more information, consult the [updating Meilisearch documentation](/learn/self_hosted/updating).

## Cloud platforms

Meilisearch can also be deployed on various cloud platforms:

- [DigitalOcean](/learn/cookbooks/digitalocean_droplet)
- [AWS](/learn/cookbooks/aws)
- [GCP](/learn/cookbooks/gcp)
- [Azure](/learn/cookbooks/azure)
- [Qovery](/learn/cookbooks/qovery)
- [Koyeb](/learn/cookbooks/koyeb)

## Verifying the installation

After launching Meilisearch, you should see output similar to:

```
888b     d888          d8b 888 d8b                                            888
8888b   d8888          Y8P 888 Y8P                                            888
88888b.d88888              888                                                888
888Y88888P888  .d88b.  888 888 888 .d8888b   .d88b.   8888b.  888d888 .d8888b 88888b.
888 Y888P 888 d8P  Y8b 888 888 888 88K      d8P  Y8b     "88b 888P"  d88P"    888 "88b
888  Y8P  888 88888888 888 888 888 "Y8888b. 88888888 .d888888 888    888      888  888
888   "   888 Y8b.     888 888 888      X88 Y8b.     888  888 888    Y88b.    888  888
888       888  "Y8888  888 888 888  88888P'  "Y8888  "Y888888 888     "Y8888P 888  888

Database path:       "./data.ms"
Server listening on: "http://127.0.0.1:7700"
Environment:         "development"
```

Your Meilisearch instance is now running and ready to use.

## Next steps

- [Quick start guide](/learn/getting_started/quick_start)
- [Search preview tutorial](/learn/getting_started/search_preview)
- [API reference](/reference/api/overview)
