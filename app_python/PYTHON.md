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


## Start the application

`pip install Flask requests pytz`

`python app.py`