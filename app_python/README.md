# Moscow Time Web Application

A simple Flask-based web application that displays the current time in Moscow.

---

## Overview

This application uses the Flask framework to create a web server. When accessed, it displays the current time in Moscow in the format `HH:MM`. The time is fetched using the `pytz` library to handle time zones.

---

## Features

- Displays the current time in Moscow.
- Lightweight and easy to deploy.
- Uses Flask for the web server and `pytz` for time zone handling.

---

## How to run
- **Clone the repository:**
    ```bash
    git https://github.com/ThePinkPanther77/S25-core-course-labs.git
    cd S25-core-course-labs/app_python
    ```
- **Run the application:**
    ```bash 
    flask --app main.py run
    ```
- **Access the application:** Check the app by opening the browser and navigating to `http://127.0.0.1:5000`