# Golang web application for random number generation from 0 to 100. 

I used the `net/http` library to generate the html page. It provides easy setup for a web application without the need for complex dependencies, which is what's needed for a lightweight project like generating random numbers. 

## Coding standards
-   Separation of code into logical parts (in my example, it's `main`, which is responsible for starting the server, and `handle_time`, which is responsible for generating random numbers and rendering the HTML page).
-   Adhering to a uniform style of variable naming.
-   Clear structuring of the web application by components and their folders.
-   Handling and displaying possible errors when running the code.
-   Manual testing to determine the correct operation of the application on different browsers and devices.
-   Variable names adhere to a uniform naming convention (snake_case).
-   

## Unit-tests
To verify the correctness of the web application during the addition of new functionality, unit tests were written to maintain the quality and performance of the code. Below is a more detailed description of the code testing.

### TestServerIsUp
Task: To check that the server has started and is working.
Results: The test verifies the server's operability.

### TestNumber
Task: To verify that the generated number is displayed and is within the specified range from 0 to 100.
Results: We make a GET request, extract the HTML page, and then use regex to find the number. After that, we verify the received number within the specified range, which satisfies our requirements.

### Best practices
1. Isolated testing of each functionality.
2. Clear naming of functions and variables.
3. Error handling.
4. Code readability.