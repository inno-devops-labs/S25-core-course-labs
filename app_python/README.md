# Moscow Time Web App

## Overview
This is a simple Python web application using **Flask** that displays the **current time in Moscow**. The time updates each time the page is refreshed.

## Installation Guide

### Prerequisites
- Python 3 installed
- `pip` installed

### Steps to Run Locally
1. Clone this repository:
   ```bash
    https://github.com/SuleimanKarimEddin/S25-core-course-labs/tree/master
    cd S25-core-course-labs
    git checkout lab1
    cd app_python
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python app.py 
   ```


## Framework Choice: Flask
I chose **Flask** for this project because:
- It is lightweight and easy to set up.
- It allows rapid development with minimal boilerplate code.
- It supports extensions and scalability for future improvements.

## Best Practices Followed
1. **Clean Code:** Code is structured with meaningful variable names.
2. **Code Readability:** Used proper indentation and formatting.
3. **Error Handling:** Flask has built-in error handling; can be expanded if needed.
4. **Time Handling:** Used `pytz` to ensure the correct Moscow timezone.

## Testing and Code Quality
- The app was tested by running it locally and refreshing the page to check if the time updates.
- Used Flask's `debug=True` mode for easy debugging.
