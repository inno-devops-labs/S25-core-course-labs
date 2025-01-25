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
