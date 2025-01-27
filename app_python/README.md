# Python Web Application: Moscow Time

## Overview
This is a simple Python web application built using the Flask framework, which displays the current time in Moscow. The time is dynamically updated each time the page is refreshed.

The application uses the `pytz` library to handle time zones and `datetime` to fetch the current time in Moscow. It is designed to be easy to deploy and test.

## Features
- Displays the current time in Moscow.
- The time is updated every time the page is refreshed.
- Developed using Flask, a lightweight web framework.
- Built following best practices for coding standards, testing, and project structure.

## Local Installation
To set up and run the application locally, follow these steps:

### Prerequisites:
- Python 3.x
- A virtual environment (recommended)

### Setup Instructions:

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/python-moscow-time.git
   cd python-moscow-time
    ```

2. Create a virtual environment:
    ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows: 
   ```bash
    .venv\Scripts\activate
   ```
   - On macOS/Linux
   ```bash
   source .venv/bin/activate
   ```
   
4. Install the required dependencies:
    ```bash
   pip install -r requirements.txt
   ```

5. Run the Flask application:
    ```bash
   python run.py
   ```

6. Open your web browser and visit http://127.0.0.1:5000/ to see the current time in Moscow.