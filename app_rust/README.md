# Rust Sample Application

[![CI Status](https://github.com/Raleksan/S25-core-course-labs/actions/workflows/app_rust.yaml/badge.svg)](https://github.com/Raleksan/S25-core-course-labs/actions/workflows/app_rust.yaml?event=push)

## Overview

This is a simple Rust web application that shows current time in Moscow on the `/` page.
It also returns on endpoint `/visits` number of visits to main page, application metrics on `/metrics` endpoint,
and health status on `/health` endpoint.

## Copy sources

- Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/raleksan/S25-core-course-labs -b lab2
cd S25-core-course-labs/app_rust
```

## Installation

- _Optional:_ activate nix-shell environment for Nix-based systems

```bash
nix-shell -p cargo
```

- _Optional_: [install cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html)

- Run the application:

```bash
cargo run
```

- Application usage: open <http://127.0.0.1:8000> or

```bash
curl 127.0.0.1:8000
```

## Unit Tests

- To run the unit tests, use the following command:

```bash
cargo test
```

## Docker

- Build Docker container

```bash
docker build --tag raleksan/app_rust:v0.1 .
```

- Push image into Dockerhub

```bash
docker push raleksan/app_rust:v0.1
```

- Pull image from Dockerhub

```bash
docker pull raleksan/app_rust:v0.1
```

- Run image

```bash
docker run -p 8000:8000 raleksan/app_rust:v0.1
```

- Application usage: open <http://127.0.0.1:8000> or

```bash
curl 127.0.0.1:8000
```

## Distroless Image Version

- Build Docker container

```bash
docker build -f distroless.dockerfile --tag raleksan/app_rust_distroless:v0.1 .
```

- Push image into Dockerhub

```bash
docker push raleksan/app_rust_distroless:v0.1
```

- Pull image from Dockerhub

```bash
docker pull raleksan/app_rust_distroless:v0.1
```

- Run image

```bash
docker run -p 8000:8000 raleksan/app_rust_distroless:v0.1
```

- Application usage: open <http://127.0.0.1:8000> or

```bash
curl 127.0.0.1:8000
```

## GitHub Actions Workflow

The CI process includes the following steps:

- Runs Clippy to check for linting issues.
- Runs unit tests using `cargo test` to verify functionality.
- ~~Performs a `Snyk` security scan to identify vulnerabilities.~~ `Snyk` currently do not support `Rust` -_- .
- Builds a Docker image and pushes it to Docker Hub.

### CI Jobs

1. **Linting (Clippy)**
   - Uses Clippy to ensure the Rust code in `app_rust` follows best practices and is free of warnings.

2. **Testing (Cargo Test)**
   - Runs `cargo test` to execute unit tests and validate functionality.

3. **Security Scan (Snyk)**
   - Uses Snyk to check for vulnerabilities in dependencies and uploads results to GitHub Code Scanning.

4. **Build and Push Docker Image**
   - Builds the Docker image using Buildx and pushes it to Docker Hub under the provided credentials.
