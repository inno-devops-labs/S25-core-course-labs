# Python Web Application

## Overview

This is a simple Python web application that displays the current time in the Moscow (MSK) timezone.  
It uses the **Flask** framework and the **pytz** library (or similar) to provide accurate local time.

## Features

- Displays hours, minutes, and seconds for the MSK timezone.
- Updates automatically when the page is refreshed.
- Follows PEP 8 coding standards and uses a virtual environment for dependencies.

## Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-account/your-repo.git
2. Navigate to app_python and (optionally) create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   python main.py
5. Open http://127.0.0.1:5000 in your browser.