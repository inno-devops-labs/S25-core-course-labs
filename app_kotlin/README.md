# Overview

[![Kotlin package](https://github.com/RwKaLs/S25-core-course-labs/actions/workflows/kotlin-ci.yml/badge.svg?branch=lab3)](https://github.com/RwKaLs/S25-core-course-labs/actions/workflows/kotlin-ci.yml)

This web application displays the current UTC time and updates it every second. It uses Ktor web framework and follows the best Kotlin web practices.

The application is able to return number of visits of the main app page on `/visits` endpoint.

## Tools

`Ktor`: Chosen for its lightweight nature, ideal for small web applications like this UTC-time showing.

`java.time`: Properly handles timezone.

## Installation and run

1. Clone repo
2. Navigate to `app_kotlin` directory
3. Install dependencies using `./gradlew build`
4. Run using `./gradlew run`
5. Navigate to [http://localhost:8080/](http://localhost:8080/) and observe the current UTC time

## Docker

This application is containerized using a multi-stage Docker build to optimize size and performance.

Dockerhub: [link](https://hub.docker.com/repository/docker/rwkals/app_kotlin)

### Building

From folder with Dockerfile:

```shell
docker build -t rwkals/app_kotlin:latest .
```

### Pulling

```shell
docker pull rwkals/app_kotlin:latest
```

### Running

```shell
docker run -p 8080:8080 rwkals/app_kotlin:latest
```

## Distroless Image

A distroless image, smaller and more secure. Details in [link](DOCKER.md)

Dockerhub: [link](https://hub.docker.com/repository/docker/rwkals/app_kotlin_distroless)

### Distroless Building

From folder with distroless.Dockerfile:

```shell
docker build -t rwkals/app_kotlin_distroless:latest -f distroless.Dockerfile .
```

### Distroless Pulling

```shell
docker pull rwkals/app_kotlin_distroless:latest
```

### Distroless Running

```shell
docker run -p 8080:8080 rwkals/app_kotlin_distroless:latest
```

## Continuous Integration Workflow

The project uses GitHub Actions for continuous integration.
The CI workflow includes Kotlin dependencies installation, linting the code using `ktlint`,
and running tests with `Gradle`.
Moreover, it integrates Docker steps: logging into Docker Hub, building, and pushing the image.
