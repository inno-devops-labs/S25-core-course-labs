# Python Web Application - Moscow Time Display

## Overview

This Python web application displays the current time in Moscow. It updates every time the page is refreshed, ensuring the displayed time is always current.

## Features

- Displays current date and time in Moscow timezone.
- Simple application using Flask.

## Prerequisites

- Python 3.x
- pip package manager

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/MrTonyNeon/S25-core-course-labs -b lab1
   cd app_python
   ```

2. **Set Up Virtual Environment (Optional but Recommended):**

   ```bash
   python3 -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application:**

   ```bash
   python app.py
   ```

2. **Access in Browser:**

   - Navigate to `http://localhost:5000/`

## Project Structure

- `app.py` - Main application file.
- `requirements.txt` - List of dependencies.
- `PYTHON.md` - Documentation on framework choice and best practices.
- `README.md` - Project documentation.
- `.gitignore` - Git ignore file.

## .gitignore

A clean `.gitignore` file is maintained to exclude:

- `venv/` - Virtual environment files.
- `pycache/` - Python cache files.
