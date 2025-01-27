# Dart Web Application - Current Time in Moscow

## Overview
This is a simple Dart web application that fetches the current time in Moscow using the [TimeAPI](https://timeapi.io) and displays it on a webpage. The application runs a basic HTTP server using the `shelf` package and serves an HTML page with the current time in Moscow.

## Features
- Displays the current time in Moscow (Europe/Moscow timezone).
- Utilizes asynchronous programming with Dart’s `async` and `await`.
- Beautiful and simple HTML interface with inline CSS for styling.

## Requirements
- Dart SDK (>=2.x)
- Internet connection (to fetch time from the API)

## Setup and Installation

### 1. Clone the Repository
Clone the repository to your local machine


### 2. Install Dependencies
Navigate to the project directory and install dependencies:

```bash
cd app_dart
dart pub get
```

### 3. Run the Server
To start the server and view the time in Moscow:
```bash
dart run bin/server.dart
```