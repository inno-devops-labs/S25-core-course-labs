# Python Web Application for Displaying Current Time in Moscow

## Framework Choice

Since this is a web application, I decided to use **Flask** as a framework for the following reasons.


- **Lightweight and user-friendly**: Flask is extremely easy to set up, it is perfect for small scale web applications like this one.
- **Flexibility**: Using Flask gives me full control of the web application including routing, templates and error handling
- **Large community**: With a big user base, there are a large number of resources and example code available for most problems with Flask

## Application Logic

The web application performs the following steps:
1. When the user visits the homepage (`/`), the server renders a template that contains JavaScript to fetch and display the current time in Moscow.
2. The application attempts to get the current time from an external API (TimeAPI.io) using the `/time` route.
3. If the API is available, the server sends the time retrieved from the API in the response.
4. If the API is unavailable (e.g., no internet connection), the server sends the current time from the server's local clock.
5. The time on the page updates every second using JavaScript and AJAX requests.

## Best Practices

- **Modular code**: I separated the logic of getting time from the external API into a separate function (`get_time_from_api`).
- **Error handling**: The application includes error handling for failed API requests, falling back to the server time when necessary.
- **Separation of concerns**: The business logic (Flask app) is kept separate from the presentation layer (HTML and JavaScript).


## Coding Standards and Code Quality

- **Flake8**: I used **Flake8** to check for PEP8 compliance and catch potential issues in the code, ensuring high-quality, error-free code.
- **Requests Library**: For API interactions, I used the **requests** library to handle HTTP requests, ensuring easy error handling and reliable communication with external services.

## Testing

- **Manual Testing**: I tested the application by running it locally and checking the displayed time in Moscow through the browser.
- **Automatic Time Update**: I ensured that the time is updated every second, without needing to refresh the page.
- **Fallback Testing**: I tested the error handling by simulating a failure to fetch time from the API (disabling internet access) and verified that the server time was returned as a fallback.
- **Code Coverage**: Although not automated in this simple application, the code is structured to be easily testable, with external dependencies isolated and clear return values.

## Start the application

`pip install Flask requests pytz`

`python app.py`