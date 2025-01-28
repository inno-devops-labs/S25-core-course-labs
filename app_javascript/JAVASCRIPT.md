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
