# app_kotlin

![Workflow Status](https://github.com/nai1ka/S25-core-course-labs/actions/workflows/app_kotlin.yml/badge.svg)

A simple Kotlin Web application to show current time in Moscow.

## Prerequisites

- [Kotlin](<https://kotlinlang.org/>)
- [Gradle](<https://gradle.org/install/>)
- [Java](<https://www.oracle.com/java/technologies/javase-jdk11-downloads.html>)

## Install

Clone the repository:

```sh
git https://github.com/nai1ka/S25-core-course-labs
cd S25-core-course-labs/app_kotlin
```

Make sure you have gradle and java installed:

```sh
gradle -v
java -version
```

If you don't have them installed, please follow the links above.
Build the project:

```sh
./gradlew build
```

Run the app:

```sh
./gradlew run
```

The server will be available at [http://localhost:8080](http://localhost:8080)

## Docker

### Building

To build the image, run:

```sh
cd app_kotlin
docker build -t nai1ka/time-service-kotlin:latest .
```

You can use any tag you want instead of `nai1ka/time-service-kotlin:latest`.

### Pulling

To pull the image from the Docker Hub, run:

```sh
docker pull nai1ka/time-service-kotlin:latest
```

### Running

To run the container, run:

```sh
docker run -p 8080:8080 nai1ka/time-service-kotlin:latest
```

Don't forget to replace `nai1ka/time-service-kotlin:latest` with the tag you are using.

## Distroless Image Version

You can also build a distroless image:

```sh
# Build the image
docker build -t time-service-kotlin-distroless -f distroless.Dockerfile .
# Run the container
docker run -p 8080:8080 time-service-kotlin-distroless
```

## Unit Tests

This project includes Unit Test to automatically test the application.
They are running automatically when you push changs to `app_kotlin` directory. Or you can execute them manually:

```sh
./gradlew test
```

## CI workflow

The repository has a GitHub Actions workflow that runs the linter, unit tests and security check on every push to the repository.

### Steps

1. Building, linting and testing\
    In this step, the following actions are performed:
    - Building the project using gradle
    - Linting the code using detekt gradle plugin
    - Running the unit tests using `kotlin-test` library
2. Security check using Snyk
3. Building the distroless Docker image and pushing it to the Docker Hub
    - This step is triggered only when all of the previous steps are successful

Notes:

- The workflow is defined in `.github/workflows/app_kotlin.yml`
- The workflow is triggered only when changes occur in the `app_kotlin` directory or `.github/workflows/app_kotlin.yml` file.

## Structure

Directory structure (dotfiles are omitted):

```sh
.
├── CI.md
├── DOCKER.md
├── Dockerfile
├── KOTLIN.md
├── README.md
├── build.gradle.kts
├── distroless.Dockerfile
├── gradle
│   ├── libs.versions.toml
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradle.properties
├── gradlew
├── local.properties
├── settings.gradle.kts
└── src
    ├── main
    │   ├── kotlin
    │   │   ├── Application.kt
    │   │   ├── Routing.kt
    │   │   └── Utils.kt
    │   └── resources
    │       ├── application.yaml
    │       └── logback.xml
    └── test
        └── kotlin
            └── TimeTest.kt
```
