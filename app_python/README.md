# Flask Web Application: Moscow Time

This is a simple web application that displays the current time in Moscow, Russia. The application is built using the Flask framework and follows best practices for Python web development.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Testing](#testing)
6. [Author](#author)

---

## Overview

The application displays the current time in the Moscow timezone (`Europe/Moscow`). It is built using Flask, a lightweight Python web framework, and uses `pytz` for timezone handling.

---

## Prerequisites

Before proceeding, ensure you have the following installed:

- **Python 3.x**: Flask requires Python 3.6 or later. If you don't have Python installed, follow the official [Python installation guide](https://www.python.org/downloads/).
- **pip3**: Python's package installer. It usually comes preinstalled with Python.
- **Virtual Environment**: A virtual environment is recommended to isolate the project dependencies.

---

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone git@github.com:Mohammed-Nour/S25-core-course-labs.git
cd S25-core-course-labs/app_python
```

### 2. Set Up a Virtual Environment

A virtual environment is used to isolate the application's dependencies. Follow the steps below to set it up:

#### Linux/macOS

1. Install the `venv` module (if not already installed):

    ```bash
    sudo apt install python3-venv
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

#### Windows

1. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    ```bash
    venv\Scripts\activate
    ```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip3 install -r requirements.txt
```

---

## Running the Application

1. Ensure the virtual environment is activated (you should see `(venv)` in your terminal prompt).
2. Set the `FLASK_APP` environment variable:
   - **Linux/macOS**:

     ```bash
     export FLASK_APP=app.py
     ```

   - **Windows**:

     ```bash
     set FLASK_APP=app.py
     ```

3. Run the Flask application:

   ```bash
   flask run
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000/`.

   > **Note**: The application will start a development server on `http://127.0.0.1:5000/`. You can stop the server by pressing `Ctrl+C` in the terminal.

---

## Testing

To ensure the application works correctly:

1. Run the application and verify that the displayed time matches the current time in Moscow.
2. Refresh the page to confirm that the time updates dynamically.

---

## Code Quality Checks

To ensure the code adheres to best practices and coding standards, the following tools are used:

### 1. **Pylint**

Pylint is a static code analysis tool that checks for errors, enforces coding standards, and provides suggestions for improving code quality.

Run Pylint on the `app.py` file:

```bash
pylint app.py
```

### 2. **Flake8**

Flake8 is a tool that combines PyFlakes, pycodestyle, and McCabe complexity checks to ensure the code follows PEP 8 standards and is free of common errors.

Run Flake8 on the `app.py` file:

```bash
flake8 app.py
```

---

## Author

- **Name**: Mohamad Nour Shahin
- **Email**: <mo.shahin@innopolis.university>
