# Python web application: Moscow Time

## Overview

This web application displays the current time in Moscow, Russia. It is built using the Flask framework and follows best practices for web development in Python.

## Framework Choice: Flask

__*Flask*__ was chosen for its simplicity and flexibility, ideal for small web apps. Flask allows for quick setup and provides the necessary tools to create a functional web application with minimal boilerplate code.

### Key Features of Flask

- __*Lightweight*__: Flask has a small core but is extensible.
- __*Flexibility*__: Developers have the freedom to choose their tools and libraries.
- __*Simplicity*__: Flask's documentation is clear and beginner-friendly, making it easy to get started.

## Best Practices Applied

### 1. Code Structure

- The application follows a modular structure, separating the main logic (`app.py`) from the templates (`index.html`).
- Static files (e.g., images) are stored in the __*static*__ folder, and templates are stored in the __*templates*__ folder, adhering to Flask's conventions.

### 2. Time Zone Handling

- The `pytz` library is used to handle time zones accurately. The __*Europe/Moscow*__ time zone is explicitly set to ensure the correct time is displayed.

### 3. Template Rendering

- Flask's `render_template` function is used to render the `index.html` template, passing the current time as a variable. This separates the logic from the presentation layer.

### 4. Coding Standards

- The code follows PEP 8 guidelines for Python, including proper indentation, naming conventions, and spacing.

## Requirements

The following dependencies are required to run this application:

- `Flask`
- `pytz`
