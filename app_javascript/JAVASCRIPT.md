# Comic Fetcher - JavaScript Web Application

This web application fetches and displays the latest XKCD comic using a Node.js backend and a frontend interface.

## Language Choice

JavaScript was chosen for the frontend because it naturally integrates with HTML and CSS, allowing for the creation of dynamic, interactive web applications. The asynchronous nature of JavaScript (using `async/await` and Promises) makes it ideal for handling API requests in real-time without blocking the user interface.

## Features

- Fetches the latest XKCD comic from the public XKCD API.
- Displays the comic title, image, description, and release date.
- The comic is displayed upon clicking a button, and the page updates dynamically.

## How It Works

1. **Backend (Node.js Express)**: The backend serves the static files (HTML, CSS, JavaScript) located in the `public` folder.
   - The Express server listens for requests on port `3000` and serves the HTML page (`index.html`) when accessed via the root route `/`.

2. **Frontend (HTML + JavaScript)**:
   - **`myapp.js`**: The JavaScript file includes an asynchronous function, `ComicFetch()`, that sends a request to the XKCD API to fetch the latest comic data.
   - Once the data is retrieved, the comic's title, image, description, and release date are displayed in the HTML document by updating the DOM.
   - The comic information is shown only after the user clicks the button, using event listeners to trigger the fetch process.

3. **Styling**: The UI is styled with `style_comic.css` to provide an appealing layout.

## Dependencies

- **Express**: A minimal and flexible Node.js web application framework used for serving static files.
- **No external libraries** are required for the frontend.

## Error Handling

- **FetchComicError**: Custom error class for handling specific errors during the comic fetching process.
- **General Errors**: Any other errors are caught and logged either to the console or displayed as a user-friendly message.

## Best Practices

- **Modular Code**: The code is divided into small functions to handle specific tasks, such as fetching data and rendering the comic on the page.
- **Asynchronous Fetching**: The app uses `async/await` to handle the fetching of comic data, ensuring the UI remains responsive.
- **Error Handling**: Proper error handling is implemented to provide feedback if an issue arises during the comic fetch or any other unexpected errors.
- **Separation of Concerns**: HTML, CSS, and JavaScript are kept in separate files, making the project more maintainable and scalable.

## Unit Tests

### Overview

Unit tests are essential for ensuring the reliability of the JavaScript application. I have written test cases using Jest and Supertest to validate the behavior of both backend (Express server) and frontend JavaScript functions.

### Tests Implemented

#### 1. **Express Server Tests** (server.test.js)

- **GET /**: Ensures the root endpoint serves `index.html` correctly.
- **GET /nonexistent**: Verifies that a nonexistent route returns a 404 status.
- **GET /myapp.js**: Confirms that the JavaScript file is served correctly.

#### 2. **Frontend Logic Tests** (myapp.test.js)

- **DOM Manipulation**: Checks that the `ComicFetch` function correctly updates the DOM elements when fetching comic data.
- **Error Handling**: Ensures errors are properly logged when fetching fails.
- **Event Handling**: Validates that clicking the comic button triggers a fetch and updates UI elements.

### Best Practices Applied

- **Mocking API Calls**: I used `jest.fn()` to mock the `fetch` API and simulate different responses.
- **Isolation of Tests**: Each test runs independently using `beforeEach` and `afterEach` hooks.
- **DOM Setup and Cleanup**: The test suite sets up a mock DOM and resets it after each test.
- **Error Handling Verification**: The jest spy on `console.error` to ensure error logs are generated when necessary.
