# Python Web Application Overview
This document provides details about the development process, framework selection, and best practices implemented for the Python web application that displays the current time in Moscow.

#  Framework Selection: Why Flask?
Flask was chosen as the web framework for this project due to the following reasons:

- Flask is ideal for small and straightforward applications as it does not impose a heavy structure.
- Flask is beginner-friendly and has straightforward syntax, making it a great choice for rapid development.
- Flask allows for the addition of functionality as needed without unnecessary overhead.
- Flask has a large, active community and comprehensive documentation, ensuring quick problem resolution and access to plugins.

# Features Implemented
Displays the current time in the Moscow timezone (Europe/Moscow).

Updates the displayed time every time the page is refreshed.

Best Practices Applied
- The application is structured to be clean and modular, allowing for easy extension or maintenance.
- The pytz library is used to manage timezones effectively, ensuring the application displays the correct Moscow time.

# Coding Standards:
- Followed PEP 8 for Python code style.
- Used meaningful function and variable names.
- The application was tested manually by refreshing the page to confirm the displayed time updates correctly.
- All required libraries (Flask and pytz) are listed in the requirements.txt file for easy installation.
- A .gitignore file was created to exclude unnecessary files like __pycache__ and virtual environments.

# Steps to Run the Application Locally

```python
pip3 install -r requirements.txt

```

Run the Application:
```python
python3 app.py
```
Screenshot: 
![](2.png)

Access the Application: Open a browser and navigate to http://127.0.0.1:5000/.