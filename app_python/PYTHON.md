#Flask

## Why I choose Flask
1. Lightweight and simple
2. The project is small and Flask is known for it's quick development
3. I don't have to install many dependencies making starting using Flask easier than explaining why I'm using Flask)

# Best Practices Applied in the Web Application

## 1. Code Structure
- Created a separate function `get_moscow_time()` to improve code reusability and maintainability.
- Used Flask’s templating engine to separate business logic from presentation.

## 2. Coding Standards Followed
- Followed **PEP 8** coding standards to improve readability.
- Used **docstrings** for functions to improve documentation.
- Applied **meaningful variable names** to enhance code clarity.

## 3. Testing Implemented
- **Manual Testing**: Verified the Moscow time updates upon page refresh.
- **Automated Testing**: Used `unittest` to ensure the home page loads correctly.

#Testing

## 1️⃣ **Unit Tests Created**
In this section, we outline the **unit tests** created for the Moscow Time Web Application. 

### **test_home_page**
- **Description**: This test checks if the home page loads correctly and contains the text "Current Time in Moscow".
- **Tested**: We verify if the **HTTP status code** is 200 and ensure that the response includes the text `"Current Time in Moscow"`.

### **test_moscow_time_format**
- **Description**: This test verifies that the Moscow time returned is in the correct format.
- **Tested**: We use Python's `datetime.strptime` to ensure the time returned matches the `YYYY-MM-DD HH:MM:SS` format.

### **test_moscow_time_timezone**
- **Description**: This test checks if the time returned is correct for the Moscow timezone.
- **Tested**: We compare the time returned by the `get_moscow_time` function with the actual current time in the Moscow timezone.

---

## 2️⃣ **Best Practices Applied in Unit Testing**

### **Code Structure for Tests**
- **Organized test cases**: Grouped related tests into methods with clear and descriptive names.
- **Reusability**: Used the `setUp()` method to initialize the test client, ensuring code reusability.

### **Testing Standards Followed**
- **Descriptive Test Names**: Test names are descriptive, such as `test_home_page`, `test_moscow_time_format`, and `test_moscow_time_timezone`.
- **PEP 8 Compliance**: Followed Python's **PEP 8** to keep the test code readable and maintainable.
- **Edge Case Testing**: Verified edge cases such as time format and timezone correctness.

### **Test Coverage**
- **Positive and Negative Tests**: Included tests for both correct and incorrect behaviors, e.g., ensuring the correct time format and testing timezone correctness.
- **Test Automation**: Used `unittest` for automated testing of the Flask application to ensure everything works as expected.

## 3️⃣ **Unit Test Framework**
- **`unittest`**: The tests were implemented using Python’s built-in `unittest` module, which is simple, efficient, and integrates easily with the CI pipeline.

