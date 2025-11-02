# Running Meilisearch in production

**Source:** https://www.meilisearch.com/docs/guides/running_production.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Running Meilisearch in Production

---

# Running Meilisearch in production

> Deploy Meilisearch in a Digital Ocean droplet. Covers installation,  server configuration, and securing your instance.

This tutorial will guide you through setting up a production-ready Meilisearch instance. These instructions use a DigitalOcean droplet running Debian, but should be compatible with any hosting service running a Linux distro.

<Note>
  [Meilisearch Cloud](https://www.meilisearch.com/cloud?utm_campaign=oss\&utm_source=docs\&utm_medium=running-production-oss) is the recommended way to run Meilisearch in production environments.
</Note>

## Requirements

* A DigitalOcean droplet running Debian 12
* An SSH key pair to connect to that machine

<Tip>
  DigitalOcean has extensive documentation on [how to use SSH to connect to a droplet](https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/).
</Tip>

## Step 1: Install Meilisearch

Log into your server via SSH, update the list of available packages, and install `curl`:

```sh
apt update
apt install curl -y
```

Using the latest version of a package is good security practice, especially in production environments.

Next, use `curl` to download and run the Meilisearch command-line installer:

```sh
# Install Meilisearch latest version from the script
curl -L https://install.meilisearch.com | sh
```

The Meilisearch installer is a set of scripts that ensure you will get the correct binary for your system.

Next, you need to make the binary accessible from anywhere in your system. Move the binary file into `/usr/local/bin`:

```sh
mv ./meilisearch /usr/local/bin/
```

Meilisearch is now installed in your system, but it is not publicly accessible.

## Step 2: Create system user

Running applications as root exposes you to unnecessary security risks. To prevent that, create a dedicated user for Meilisearch:

```sh
useradd -d /var/lib/meilisearch -b /bin/false -m -r meilisearch
```

This command creates a new user called `meilisearch` with `/var/lib/meilisearch` as its home directory. Since this user will run the Meilisearch binary, it is good security practice to set this account's default shell to `/bin/false`. This way the `meilisearch` user cannot be used to log into the system.

## Step 3: Create Meilisearch configuration file

By default, Meilisearch starts a server listening on port `7700` without a master key. For security reasons, you must set a master key and configure environment settings using command-line options or environment variables.

An alternative to command-line options or environment variables is to create a configuration file. This will make it easier to customize your setup as needed.

Create the configuration file `/etc/meilisearch.toml`:

```sh
nano /etc/meilisearch.toml
```

Paste in the following configuration:

```toml
# This file shows all the default values. You can remove any of the lines
# below to apply the defaults specified here.

# Designates the location where database files will be created and retrieved.
db_path = "/var/lib/meilisearch/data"

# Configures the instance's environment. Value must be either `production` or `development`.
env = "production"

# The address on which the HTTP server will listen.
http_addr = "127.0.0.1:7700"

# Sets the instance's master key, automatically protecting all routes except GET /health.
# CHANGE THIS TO A RANDOM VALUE
master_key = "YOUR_MASTER_KEY_VALUE"

# Deactivates analytics.
# Analytics help us improve Meilisearch by collecting anonymous data about your usage.
no_analytics = false
```

<Warning>
  Choose a strong alphanumeric master key and replace `YOUR_MASTER_KEY_VALUE` with it.
</Warning>

For a complete list of configuration options, check the [configuration reference](/reference/api/configuration).

Save and close the file.

Next, change the ownership of the configuration file so only the root user has write access to it:

```sh
chown root:meilisearch /etc/meilisearch.toml
chmod 640 /etc/meilisearch.toml
```

Change ownership of the database directory:

```sh
chown -R meilisearch:meilisearch /var/lib/meilisearch
```

## Step 4: Running Meilisearch as a service

Create a systemd unit file to manage the Meilisearch service. This will allow your instance to start automatically on reboot, log any errors, and otherwise behave like a well-integrated system service.

Create the file `/etc/systemd/system/meilisearch.service`:

```sh
nano /etc/systemd/system/meilisearch.service
```

Paste in the following configuration:

```
[Unit]
Description=Meilisearch
After=network.target

[Service]
Type=simple
User=meilisearch
Group=meilisearch
ExecStart=/usr/local/bin/meilisearch --config-file-path /etc/meilisearch.toml
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Save and close the file.

Activate and start the service:

```sh
systemctl enable meilisearch
systemctl start meilisearch
```

Verify Meilisearch started successfully:

```sh
systemctl status meilisearch
```

You should see output similar to:

```
● meilisearch.service - Meilisearch
     Loaded: loaded (/etc/systemd/system/meilisearch.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2023-01-17 14:33:57 UTC; 4s ago
   Main PID: 13371 (meilisearch)
      Tasks: 15 (limit: 1114)
     Memory: 27.1M
        CPU: 410ms
     CGroup: /system.slice/meilisearch.service
             └─13371 /usr/local/bin/meilisearch --config-file-path /etc/meilisearch.toml
```

You can view Meilisearch logs using journalctl:

```sh
journalctl -u meilisearch -f
```

This will show you real-time Meilisearch logs.

## Step 5: Configure reverse proxy

Meilisearch is configured to listen on `127.0.0.1:7700`. To make Meilisearch publicly accessible, configure a reverse proxy with nginx.

Install nginx:

```sh
apt install nginx -y
```

Create an nginx configuration file:

```sh
nano /etc/nginx/sites-enabled/meilisearch
```

Add the following configuration, replacing `meilisearch.example.com` with your domain name:

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name meilisearch.example.com;
    location / {
        proxy_pass  http://127.0.0.1:7700;
    }
}
```

Remove the default enabled site to prevent any conflicts:

```sh
rm /etc/nginx/sites-enabled/default
```

Test the nginx configuration:

```sh
nginx -t
```

You should see:

```
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Restart nginx:

```sh
systemctl restart nginx
```

Your Meilisearch instance is now publicly accessible through your domain name.

## Step 6: Configure HTTPS with Let's Encrypt

Let's Encrypt is a certificate authority that provides free TLS/SSL certificates. These certificates allow web browsers to verify and establish secure connections to your server.

Install certbot:

```sh
apt install certbot python3-certbot-nginx -y
```

Run certbot:

```sh
certbot --nginx
```

Follow the prompts to configure HTTPS for your domain. When successful, certbot will update your nginx configuration to use HTTPS.

Test your configuration by accessing your domain at `https://meilisearch.example.com`.

## Conclusion

You now have a production-ready Meilisearch instance running on a DigitalOcean droplet secured with HTTPS.

To ensure you maintain a secure installation:

- Keep Meilisearch updated to the [latest version](https://github.com/meilisearch/meilisearch/releases)
- Keep your operating system and installed packages up to date
- Regularly review your firewall rules and nginx configuration
- Back up your database files stored in `/var/lib/meilisearch/data`

For more information on securing and optimizing Meilisearch, check:

- [Configuration reference](/reference/api/configuration)
- [Security best practices](/learn/security/basic_security)
- [Performance optimization](/learn/advanced/indexing_best_practices)
