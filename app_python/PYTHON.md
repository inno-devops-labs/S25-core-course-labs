# Python Moscow Time Web Application

## Overview

A simple web application that displays the current time in Moscow. Built with Flask.

## Features

- Displays the current Moscow time.
- Updates time on page refresh.

## Installation

1. Clone the repository.
2. Navigate to the `app_python` folder.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application:

   ```bash
   python app.py
   ```

5. (Optional) Run the tests:

   ```bash
   python tests/app_test.py
   ```

## Usage

- Open your browser and navigate to `http://127.0.0.1:5000`.

### Framework Choice

Flask was chosen because it is lightweight, easy to set up, and perfect for small projects like this one.

### Best Practices

- Followed PEP 8 standards.
- Used descriptive function names and modular structure.
- Secured the `requirements.txt` file to avoid unnecessary dependencies.

### Testing

- Verified the application locally with various refresh intervals to ensure accurate time updates.
- Developed and executed unit tests to validate functionality and reliability.
