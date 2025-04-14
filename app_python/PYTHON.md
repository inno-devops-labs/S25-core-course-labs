This Python Flask application demonstrates the use of best practices for building a small, maintainable, and efficient web app.

# Frameworks Used


## Flask:
Flask is a lightweight web framework that is both flexible and secure, making it ideal for small applications like this. It integrates seamlessly with the Jinja2 templating engine to ensure secure rendering of dynamic HTML, protecting against Cross-Site Scripting (XSS) attacks by default. Flask’s modularity also allows easy scaling, while built-in features like session management and support for HTTPS enhance security.

Best practices are followed from the following source: https://jnikenoueba.medium.com/the-10-best-practices-for-building-a-flask-application-b5a7dbc784f5

# Project Structure
```
app_python/
│
├── templates/
│   └── index.html   
│
├── venv/
│
├── app.py
├── requirements.txt
├── PYTHON.md
├── README.md
└── .gitignore
```

# Coding Standards

1. **PEP 8 Compliance:**
   - Followed Python's PEP 8 guidelines for code formatting to ensure readability and consistency.
   - Used descriptive variable names such as `moscow_time` and `formatted_time` to make the usage of each variable clear.
   
2. **Comments and Handling Errors:**
   - Added comments to explain critical steps in the code.
   - Used a `try-except` block to handle errors gracefully when API calls fail.

3. **Secure and Performant Code:**
   - Limited the timeout for the API request (`timeout=5`) to avoid hanging indefinitely in case of server issues.
   - Used `response.raise_for_status()` to ensure HTTP errors are handled explicitly.

---

# Testing and Debugging

1. **Manual Testing:**
   - Tested the Flask app locally to ensure that:
     - The API integration works correctly.
     - Errors are displayed in case of issues (e.g., slow Internet connection or invalid API response).
     - The rendered HTML template is properly updated with the correct time.

2. **Error Handling:**
   - Used an `except` block to catch and display errors. This avoids exposing sensitive error details to users.
   - Included fallback behavior (e.g., displaying an error message) when API calls fail.

---

# Code Quality

1. **Dependencies:**
   - Used a `requirements.txt` file to list only the necessary dependencies.


2. **HTML Integration:**
   - Followed semantic HTML practices in `index.html` for accessibility and clarity.
   - Used CSS for responsive and visually appealing UI design.

---

# Unit Testing

In this project, unit tests are written to ensure functionality and robustness. Each test follows key best practices, such as:

1. **Clear Naming:**
Test names describe the method, scenario, and expected behavior.

2. **AAA Pattern:**
Tests follow the Arrange, Act, Assert structure for readability and clarity.

3. **Mocking:**
External dependencies like APIs are mocked using the ```mocker``` library.

4. **Single Responsibility:**
Each test focuses on one specific behavior or concern.

5. **Helper Methods:**
Repetitive setup code is centralized using fixtures.