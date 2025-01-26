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
go get ./...
```

Run application

```bash
go run .
```

Test that everything works:

```bash
curl http://localhost:8000/currency/
```

## Acknowledgements

[RESTful API with Gin](https://go.dev/doc/tutorial/web-service-gin)

CoinMarketCap [docs](https://coinmarketcap.com/api/documentation/v1/)
