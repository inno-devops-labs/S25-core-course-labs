# Golang web application for random number generation from 0 to 100. 

I used the `net/http` library to generate the html page. It provides easy setup for a web application without the need for complex dependencies, which is what's needed for a lightweight project like generating random numbers. 

## Coding standards
-   Separation of code into logical parts (in my example, it's `main`, which is responsible for starting the server, and `handle_time`, which is responsible for generating random numbers and rendering the HTML page).
-   Adhering to a uniform style of variable naming.
-   Clear structuring of the web application by components and their folders.
-   Handling and displaying possible errors when running the code.
-   Manual testing to determine the correct operation of the application on different browsers and devices.
-   Variable names adhere to a uniform naming convention (snake_case).