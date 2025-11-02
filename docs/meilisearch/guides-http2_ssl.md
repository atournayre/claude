# Using HTTP/2 and SSL with Meilisearch

**Source:** https://www.meilisearch.com/docs/guides/http2_ssl.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - Configuration HTTP/2 et SSL

---

> Learn how to configure a server to use Meilisearch with HTTP/2.

For those willing to use HTTP/2, please be aware that it is **only possible if your server is configured with SSL certificate**.

Therefore, you will see how to launch a Meilisearch server with SSL. This tutorial gives a short introduction to do it locally, but you can as well do the same thing on a remote server.

First of all, you need the binary of Meilisearch, or you can also use docker. In the latter case, it is necessary to pass the parameters using environment variables and the SSL certificates via a volume.

A tool to generate SSL certificates is also required. In this How To, you will use [mkcert](https://github.com/FiloSottile/mkcert). However, if on a remote server, you can also use certbot or certificates signed by a Certificate Authority.

Then, use `curl` to do requests. It is a simple way to specify that you want to send HTTP/2 requests by using the `--http2` option.

## Try to use HTTP/2 without SSL

Start by running the binary.

```bash
./meilisearch
```

And then, send a request.

```bash
curl -kvs --http2 --request GET 'http://localhost:7700/indexes'
```

You will get the following answer from the server:

```bash
*   Trying ::1...
* TCP_NODELAY set
* Connection failed
* connect to ::1 port 7700 failed: Connection refused
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 7700 (#0)
> GET /indexes HTTP/1.1
> Host: localhost:7700
> User-Agent: curl/7.64.1
> Accept: */*
> Connection: Upgrade, HTTP2-Settings
> Upgrade: h2c
> HTTP2-Settings: AAMAAABkAARAAAAAAAIAAAAA
>
< HTTP/1.1 200 OK
< content-length: 2
< content-type: application/json
< date: Tue, 05 Nov 2019 09:25:36 GMT
<
* Connection #0 to host localhost left intact
[]* Closing connection 0
```

As you can see in the answer, the protocol is HTTP/1.1. This is due to the fact that Meilisearch doesn't support HTTP/2 over clear text. Therefore, you need to configure SSL.

## Generate SSL certificate

Install mkcert if not done already.

```bash
brew install mkcert
brew install nss # if you use Firefox
```

Then, generate a certificate for localhost.

```bash
mkcert -install
mkcert localhost
```

You should now have two new files in the directory you ran the command from:
- `localhost.pem`
- `localhost-key.pem`

## Use SSL certificate with Meilisearch

Now, launch Meilisearch with the `--ssl-cert-path` and `--ssl-key-path` options.

```bash
./meilisearch --ssl-cert-path ./localhost.pem --ssl-key-path ./localhost-key.pem
```

And send a new request with HTTPS.

```bash
curl -kvs --http2 --request GET 'https://localhost:7700/indexes'
```

Here is the answer:

```bash
*   Trying ::1...
* TCP_NODELAY set
* Connection failed
* connect to ::1 port 7700 failed: Connection refused
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 7700 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/cert.pem
  CApath: none
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: O=mkcert development certificate; OU=username@hostname
*  start date: Jun  1 00:00:00 2019 GMT
*  expire date: Nov  5 10:50:57 2029 GMT
*  subjectAltName: host "localhost" matched cert's "localhost"
*  issuer: O=mkcert development CA; OU=username@hostname; CN=mkcert username@hostname
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7f8c7400a600)
> GET /indexes HTTP/2
> Host: localhost:7700
> User-Agent: curl/7.64.1
> Accept: */*
>
* Connection state changed (MAX_CONCURRENT_STREAMS == 4294967295)!
< HTTP/2 200
< content-length: 2
< content-type: application/json
< date: Tue, 05 Nov 2019 10:51:03 GMT
<
* Connection #0 to host localhost left intact
[]* Closing connection 0
```

Perfect! Look at the lines that contain `HTTP/2`. You can see that the server successfully negotiated an HTTP/2 connection with the client.

## Use SSL certificate with Docker

If you use Docker, you need to pass the certificate files via a volume and the options via environment variables.

```bash
docker run -it --rm \
  -p 7700:7700 \
  -v $(pwd)/localhost.pem:/localhost.pem \
  -v $(pwd)/localhost-key.pem:/localhost-key.pem \
  -e MEILI_SSL_CERT_PATH=/localhost.pem \
  -e MEILI_SSL_KEY_PATH=/localhost-key.pem \
  getmeili/meilisearch:latest
```

Then, you can send the same request as before.

```bash
curl -kvs --http2 --request GET 'https://localhost:7700/indexes'
```

And you should get the same answer.
