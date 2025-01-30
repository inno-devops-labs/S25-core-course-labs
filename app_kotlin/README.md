# Kotlin Ktor Time Display App

This is a simple Kotlin Ktor web application that displays the current time in Moscow.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Docker](#docker)
- [Contributing](#contributing)

## Installation

1. Clone the repository:

   > `git clone https://github.com/emapfff/S25-core-course-labs.git`

2. Navigate to the app_kotlin folder:

   > `cd app_kotlin`

3. Build the project using Gradle:
   > `./gradlew build`

## Usage

Run the Ktor application using Gradle:

> `./gradlew run`

Alternatively, you can run it directly from your IDE by running the main function in the Main.kt file.

Open your web browser and go to http://127.0.0.1:8080/ to view the current time in Moscow. Refresh the page to see the time update.

## Testing

To test the application you should run:

> `./gradlew test`

## Docker

### How to build

Run command

```
docker build -t app_kotlin:latest
```

### How to Pull

You can pull the Docker image from Docker Hub using(current version 1.0.2):

```
docker pull dyllasdek/app_kotlin:latest
```

### How to Run

To run the Docker container, use the following command:

```
docker run -p 5000:5000 app_kotlin
```

Make sure you have Docker installed and running on your system before executing these commands.

## Contributing

Contributions are welcome! If you'd like to improve this project or report issues, please open an issue or submit a pull request.

## Dependencies

Kotlin: [Official Kotlin Website](https://kotlinlang.org/)

Ktor: [Official Ktor Website](https://ktor.io/)

Gradle: [Official Gradle Website](https://gradle.org/)
