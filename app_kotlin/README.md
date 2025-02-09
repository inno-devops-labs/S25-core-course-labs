# app_kotlin

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

## Layout

Directory structure (dotfiles are omitted):

```sh
.
├── KOTLIN.md
├── README.md
├── build.gradle.kts
├── gradle
│   ├── libs.versions.toml
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradle.properties
├── gradlew
├── settings.gradle.kts
└── src
    └── main
        ├── kotlin
        │   ├── Application.kt
        │   ├── Routing.kt
        │   └── Utils.kt
        └── resources
            ├── application.yaml
            └── logback.xml
```
