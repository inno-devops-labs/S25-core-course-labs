# Swift Web Application for Displaying Current Moscow Time

## Overview

This project is a simple Swift web application developed using Vapor framework. The application displays the current time in Moscow, formatted as `YYYY-MM-DD HH:mm:ss`, and dynamically updates the time when the page is refreshed. The project leverages the SwiftDate library for handling time zone and region settings.

## Best Practices Applied

- **Framework Selection**: The project uses the **Vapor** framework for its simplicity and performance. Vapor is a highly extensible web framework built in Swift, well-suited for building REST APIs, web applications, and server-side apps.
  
- **Date and Time Handling**: We used the **SwiftDate** library for handling time zones and regional settings. The application fetches the current Moscow time using the `Region` class, converting it to the Moscow time zone and formatting it.

- **Modular Code**: The route and view logic are kept modular and clean. Each functionality is encapsulated in functions and is easily testable.

- **Error Handling**: The application provides robust error handling in case of invalid region or date-time formats, ensuring stability and security.

## Steps for Implementation

1. **Vapor Framework Setup**: The Vapor framework was installed using Swift Package Manager (SPM). It's used to define routes, handle HTTP requests, and render views.

2. **SwiftDate Library**: SwiftDate was used to manage time zones and format dates efficiently. It was configured to fetch the current date in the Moscow region.

3. **Leaf Templating Engine**: The application uses Leaf to render HTML content dynamically. The current Moscow time is passed as a variable to the Leaf template and displayed on the webpage.

4. **Route Definition**: The route `/` fetches the current Moscow time and renders it on an HTML page.

## Testing the Application

To test the application:

1. Clone the repository.
2. Install the necessary dependencies by running `vapor update`.
3. Start the server by running `vapor run serve`.
4. Open the browser and visit `http://localhost:8080` to view the current Moscow time.
