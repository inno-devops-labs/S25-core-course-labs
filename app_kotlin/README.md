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
