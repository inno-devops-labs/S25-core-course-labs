# Lab 1: Web Application Development

## Bonus Task: Additional Web Application

### Language and Framework Choice

I chose **Go** and the **Echo framework** for this project because:

#### Go

- Native HTTP/JSON handling in standard library
- Static typing for reliability
- Fast compilation and execution

#### Echo

- Minimalist design for fast API development
- Built-in middleware (logging, error recovery)
- Simple route handlers with built-in functions for building JSON responses

### Best Practices Applied

- Structured project using Go's recommended layout (`/cmd`, `/internal`)
- Formatted code with `gofmt`/`goimports` (Go's official tools)
- Added graceful shutdown for production readiness
- Clean error handling with HTTP status codes
- Added `.gitignore` for build artifacts/dependencies
- Added `Makefile` with commands to run, test and build the application
- Added `.env` file with HTTP server config
- Used `Binance API` for real-time crypto prices

These best practices helped me follow coding standards and ensure code quality.

### Testing

To test web application I made several `GET http://localhost:8080/price` requests via web browser.
Requests return realtime data about BTC/USDT and ETH/USDT pairs on Binance exchange.
