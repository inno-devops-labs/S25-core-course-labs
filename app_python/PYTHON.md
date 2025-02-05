# Why Flask?

## Framework Choice
For this web application, **Flask** was chosen as the web framework for the following reasons:

1. **Lightweight & Minimalistic**  
   - Flask is a micro-framework, meaning it has no unnecessary dependencies, making it fast and efficient for small web applications.

2. **Easy to Learn & Use**  
   - Flask has a simple and intuitive API, making it ideal for quick development.

3. **Flexible**  
   - Unlike larger frameworks like Django, Flask does not impose strict rules on how the application should be structured.

4. **Extensibility**  
   - Flask allows developers to add only the components they need, avoiding unnecessary bloat.

5. **Active Community & Good Documentation**  
   - Flask has an active developer community and extensive documentation, making problem-solving easier.

---

## Best Practices Implemented
### **Coding Standards**
- Followed **PEP8** for clean and readable code.
- Used **virtual environments** to manage dependencies.
- Kept the code modular and easy to maintain.

### **Testing**
- Manually tested to ensure the time updates correctly.
- Ensured Flask's built-in debugger is disabled in production.

### **Code Quality**
- Used a minimal **requirements.txt** file to include only necessary dependencies.
- Ensured that the application is **lightweight and efficient**.
- Followed a **clear folder structure** for better organization.

---

## Alternative Frameworks Considered
| Framework | Why Not? |
|-----------|---------|
| **Django** | Too heavy for a simple project, has a lot of built-in features that are not needed. |
| **FastAPI** | Great for APIs but overkill for a basic web page. |
| **Bottle** | Similar to Flask but has a smaller community and fewer extensions. |

### **Final Choice: Flask**
- Best balance between **simplicity**, **flexibility**, and **efficiency** for a small web project.

---

## Summary
Flask was the best choice for this project because it is lightweight, easy to use, and allows for rapid development while following best practices.


### Overview of Unit Tests

The unit tests are written using the `pytest` framework and test the functionality of the Flask application that displays the current time in Moscow. The tests ensure that:
1. The application returns a valid response.
2. The displayed time is in the correct format.
3. The displayed time is accurate (within a small margin of error).
4. The time updates correctly when the page is refreshed.

---

### Test Cases

#### 1. **Test Index Route (`test_index`)**
   - **Purpose**: Verify that the root route (`/`) returns a valid response and contains the expected text.
   - **Steps**:
     1. Send a GET request to the root route.
     2. Check that the response status code is `200`.
     3. Verify that the response contains the text `"Current time in Moscow:"`.
   - **Assertions**:
     - `assert response.status_code == 200`
     - `assert b"Current time in Moscow:" in response.data`

---

#### 2. **Test Time Format and Accuracy (`test_time`)**
   - **Purpose**: Verify that the displayed time is in the correct format and is accurate (within 5 seconds of the actual Moscow time).
   - **Steps**:
     1. Send a GET request to the root route.
     2. Extract the displayed time from the response.
     3. Verify that the time matches the format `YYYY-MM-DD HH:MM:SS`.
     4. Compare the displayed time with the actual Moscow time.
     5. Ensure the time difference is no more than 5 seconds.
   - **Assertions**:
     - `assert re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", app_moscow_time)`
     - `assert time_difference <= 5`

---

#### 3. **Test Time Updates (`test_time_updates`)**
   - **Purpose**: Verify that the displayed time updates correctly when the page is refreshed.
   - **Steps**:
     1. Send a GET request to the root route and record the displayed time.
     2. Wait for 2 seconds.
     3. Send another GET request and record the new displayed time.
     4. Verify that the two times are different.
   - **Assertions**:
     - `assert time1 != time2`

---

### Best Practices Applied

#### 1. **Use of `pytest` Framework**
   - The `pytest` framework is used for writing and running tests. It provides a simple and scalable way to write test cases.
   - Fixtures (e.g., `client`) are used to set up the test environment and avoid code duplication.

#### 2. **Test Isolation**
   - Each test case is independent and does not rely on the state of other tests.
   - The `client` fixture ensures that a fresh instance of the Flask app is used for each test.

#### 3. **Assertions**
   - Clear and descriptive assertions are used to validate the expected behavior of the application.
   - Regular expressions are used to validate the format of the displayed time.

#### 4. **Time Handling**
   - The `pytz` library is used to handle timezone conversions and ensure accurate comparisons with the actual Moscow time.
   - A small margin of error (5 seconds) is allowed to account for potential delays in processing.

#### 5. **Test Coverage**
   - The tests cover the core functionality of the application, including:
     - Response validation.
     - Time format validation.
     - Time accuracy.
     - Time updates.

#### 6. **Code Readability**
   - Test cases are well-documented with comments explaining their purpose and steps.
   - Variable names are descriptive (e.g., `true_moscow_time`, `app_moscow_time`).

---

### How to test?
  - Run *pytest app_python/tests/*
