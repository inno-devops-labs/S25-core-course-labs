# Overview

This web application displays the current UTC time and updates it every second. It uses Ktor web framework and follows the best Kotlin web practices.

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
