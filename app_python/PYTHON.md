# Framework Selection for Moscow Time Web Application

## Introduction

To implement the web application displaying Moscow time, I opted for FastAPI. This tool was chosen due to my prior experience working with it, as well as its lightweight nature compared to Django, which would be an overkill for this specific task. FastAPI offers ease of development and seamless integration with Jinja2Templates, thus simplifying the creation of the HTML page.

Consequently, the selection of FastAPI was driven by the pursuit of maximally rapid and efficient development, providing the required functionality while minimizing time expenditure. This allowed for the quick creation of the necessary web application in accordance with the lab assignment specifications.

## Coding standards
- I strived to maintain a consistent coding style throughout the project.
- Variable names adhere to a uniform naming convention (snake_case).
- Comments are used strategically to explain complex or non-obvious code sections.
- The file system is clearly structured based on the type of files stored.
- Manual testing was performed to verify information updates, including cross-browser and mobile device testing.
- Using requirements.txt to install the necessary dependencies.
- Using the latest recommended version of python and libraries. 

## Unit tests

### test_server_start
**Purpose:** To check the server's operability.  
**Results:** The unit test sends a GET request and checks the response code to ensure the server is working correctly.

### test_time_check
**Purpose:** To verify the correct Moscow time in the web application.  
**Results:** We send a GET request to retrieve the HTML page, then parse the page and compare the time indicated on the page with the time obtained during the unit test using the same `pytz.timezone` library.

### Best practices
- Unit tests are isolated.
- Test names convey the purpose of the test.
- Tests are commented.
- Tests are not 'fragile'; for example, using `assertAlmostEqual(delta)` to account for possible deviations due to delays and other factors.