# XKCD Comic Fetcher - JavaScript Web Application

This web application loads the most recent comic from **XKCD** and displays it on the website.

## Language choose

I chose JavaScript for the bonus task because, as a frontend developer, it’s the most efficient and natural choice for building web applications. JavaScript integrates seamlessly with HTML and CSS, allowing me to quickly create dynamic and interactive UIs. Its asynchronous programming features, like Promises and async/await, make it ideal for handling real-time updates.

## Features

- Fetches the latest XKCD comic from the API.
- Displays the comic title, release date, description, and image.
- The comic information is displayed after clicking the button.

## How It Works

- The application makes a **fetch request** to the XKCD API using JavaScript's `fetch()` method to retrieve the latest comic data.
- If the fetch is successful, the comic's title, image, and description are displayed.
- If any error occurs during the fetch, an error message is logged to the console.

## Dependencies

No external libraries are required for this application.

## Error Handling

- **FetchComicError**: Custom error class for handling errors when fetching comic data.
- **General Errors**: Any unexpected errors are caught by the `catch` block and logged.

## Best Practices

- Code is structured in a modular way using functions and classes to handle errors.
- The app uses asynchronous JavaScript (`async/await`) to handle the fetching process.
- Proper error handling ensures that users get meaningful messages if something goes wrong.
