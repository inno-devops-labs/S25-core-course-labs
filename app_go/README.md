# TRUMP coin retriever

## Overview

Simple web application which shows TRUMP coin price in USD. As for future development, it can be enhanced by adding user input field and choose currency to display.

## Local installation

Create `.env`:

```bash
cp example.env .env
```

To get the API key, sign up to [CoinMarketCap](https://pro.coinmarketcap.com/signup). From [account](https://pro.coinmarketcap.com/account) paste obtained key into `.env`

Download dependencies

```bash
go mod download
```

Run application

```bash
go run .
```

Test that everything works:

```bash
curl http://localhost:8000/currency/
```

## Docker

Dockerized golang application. After build exec to container and run `curl http://127.0.0.1:8000/currency` to retrieve currency.

### How to build

```bash
docker build --no-cache -t <your_path_your_tag> .
```

[Tagging reference](https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/#tagging-images). For push to DockerHub:

```bash
docker push <your_path_your_tag>
```

### How to pull

Use path and tag which you used on build, if you want to retrieve your image, otherwise, here is from my account:

```bash
docker pull muhammaduss/app-go:latest
```

### How to run

Command with my image, if you want, use instead last argument - your pulled or built image

```bash
docker run -e API_KEY='<coinmarketcap_api_key>' -p 8080:8080 muhammaduss/app-go
```

## Acknowledgements

[RESTful API with Gin](https://go.dev/doc/tutorial/web-service-gin)

CoinMarketCap [docs](https://coinmarketcap.com/api/documentation/v1/)
