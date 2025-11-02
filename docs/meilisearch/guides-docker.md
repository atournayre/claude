# Using Meilisearch with Docker

**Source:** https://www.meilisearch.com/docs/guides/docker.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Docker Integration

---

# Using Meilisearch with Docker

> Learn how to use Docker to download and run Meilisearch, configure its behavior, and manage your Meilisearch data.

In this guide you will learn how to use Docker to download and run Meilisearch, configure its behavior, and manage your Meilisearch data.

Docker is a tool that bundles applications into containers. Docker containers ensure your application runs the same way in different environments. When using Docker for development, we recommend following [the official instructions to install Docker Desktop](https://docs.docker.com/get-docker/).

## Download Meilisearch with Docker

Docker containers are distributed in images. To use Meilisearch, use the `docker pull` command to download a Meilisearch image:

```sh
docker pull getmeili/meilisearch:v1.16
```

Meilisearch deploys a new Docker image with every release of the engine. Each image is tagged with the corresponding Meilisearch version, indicated in the above example by the text following the `:` symbol. You can see [the full list of available Meilisearch Docker images](https://hub.docker.com/r/getmeili/meilisearch/tags#!) on Docker Hub.

<Warning>
  The `latest` tag will always download the most recent Meilisearch release. Meilisearch advises against using it, as it might result in different machines running different images if significant time passes between setting up each one of them.
</Warning>

## Run Meilisearch with Docker

After completing the previous step, use `docker run` to launch the Meilisearch image:

```sh
docker run -it --rm \
  -p 7700:7700 \
  -v $(pwd)/meili_data:/meili_data \
  getmeili/meilisearch:v1.16
```

### Configure Meilisearch

Meilisearch accepts a number of instance options during launch. You can configure these in two ways: environment variables and CLI arguments. Note that some options are only available as CLI arguments—[consult our configuration reference for more details](/learn/self_hosted/configure_meilisearch_at_launch).

#### Using environment variables

Use the `-e` flag with `docker run` to pass environment variables to your Meilisearch instance:

```sh
docker run -it --rm \
  -p 7700:7700 \
  -e MEILI_MASTER_KEY='aSampleMasterKey' \
  -v $(pwd)/meili_data:/meili_data \
  getmeili/meilisearch:v1.16
```

The above code sample sets the master key to `aSampleMasterKey`.

#### Using CLI arguments

You can also use CLI arguments by appending them to the end of the `docker run` command:

```sh
docker run -it --rm \
  -p 7700:7700 \
  -v $(pwd)/meili_data:/meili_data \
  getmeili/meilisearch:v1.16 \
  meilisearch --master-key="aSampleMasterKey"
```

Like the previous example, this sets the master key to `aSampleMasterKey`.

<Danger>
  Meilisearch is open and does not require authentication by default. Make sure to set a master key when launching your instance in production environments. [Read more about security in Meilisearch](/learn/security/basic_security).
</Danger>

## Manage Meilisearch data with Docker

By default, the Docker image stores database files in the `/meili_data` directory. To make this data persistent across Docker restarts and updates, mount a volume using the `-v` flag:

```sh
docker run -it --rm \
  -p 7700:7700 \
  -v $(pwd)/meili_data:/meili_data \
  getmeili/meilisearch:v1.16
```

When you run the above command, Docker creates a directory called `meili_data` in your current working directory. Docker then maps this directory to the container's internal `/meili_data` directory. Any changes to files in `/meili_data` will be reflected in `$(pwd)/meili_data` and vice-versa.

If you do not mount a volume with the `-v` flag, all data will be lost when you remove the container.

## Updating Meilisearch with Docker

Use `docker pull` to download a new Meilisearch Docker image. Remember to use a specific version tag instead of `latest`:

```sh
docker pull getmeili/meilisearch:v1.16
```

After downloading a newer image, use `docker run` to create a new container based on that image. Make sure to mount a volume pointing to the directory with your Meilisearch data:

```sh
docker run -it --rm \
  -p 7700:7700 \
  -v $(pwd)/meili_data:/meili_data \
  getmeili/meilisearch:v1.16
```

<Warning>
  Updating Meilisearch might require you to [migrate your database dumps](/learn/update_and_migration/updating). Always back up your database before updating Meilisearch.
</Warning>

## Troubleshooting

### Port already in use

If you get an error message similar to the following:

```
docker: Error response from daemon: driver failed programming external connectivity on endpoint meilisearch:
Bind for 0.0.0.0:7700 failed: port is already allocated.
```

This means port `7700` is already in use on your machine. You can fix this by using a different port:

```sh
docker run -it --rm \
  -p 7701:7700 \
  -v $(pwd)/meili_data:/meili_data \
  getmeili/meilisearch:v1.16
```

The above command maps the container's internal port `7700` to your machine's port `7701`.

### Permission issues

If you encounter permission issues when trying to use Docker volumes, you might need to specify the user ID:

```sh
docker run -it --rm \
  -p 7700:7700 \
  -v $(pwd)/meili_data:/meili_data \
  --user $(id -u):$(id -g) \
  getmeili/meilisearch:v1.16
```

This ensures the container runs with your user's permissions.
