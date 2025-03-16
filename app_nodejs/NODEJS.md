### NODEJS.md

## Introduction

Hey there! For this lab assignment, I decided to build a very simple **Moscow Time** web application in Node.js. Instead of using a more complex web framework (like Express, Koa, Fastify, and so on), I went with Node.js's built-in `http` module. It's an excellent choice for quick, lightweight demos and completely satisfies our requirement to display the current time in Moscow. This approach also means we don't add extra dependencies—just one file that is ready to run on any machine with Node.js installed!

## Why `http`?

- **Built-in and Lightweight**: Since `http` is included with Node.js, no additional installation is needed. This matches perfectly with our lab's requirement for a simple web application.
- **Simplicity**: The lab is straightforward—show the current Moscow time. We don't need database connections, templates, or any complex web structure. Using a minimal built-in server keeps everything lean and easy.
- **No Extra Dependencies**: A big plus for projects like this is avoiding "dependency bloat." With `http`, we just run the script, and it works out of the box on any system with Node.js installed.

## Best Practices

1. **Clear Code Structure**  
   - A `getMoscowTime` function to handle time calculation.  
   - A `requestHandler` function to process HTTP requests.  
   - A `server.js` file that initializes and starts the server.
2. **Code Style Compliance**  
   - Proper indentation and spacing (2 spaces per indent).  
   - Descriptive naming for functions and variables.  
   - Linting with ESLint.
3. **Conventional Commits**  
   - I followed the [Conventional Commits](https://www.conventionalcommits.org) approach with short, descriptive commit messages (e.g., "feat: implement server returning Moscow time"). This practice keeps history readable and helps understand changes at a glance.
4. **Time Zone Handling**  
   - We explicitly set the timezone to Moscow (UTC+3) by adjusting for the offset. This ensures we always display the correct local time in Moscow.
5. **Security Considerations**  
   - Although this is a simple project, Node.js's built-in `http` module is not intended for production. For real-world scenarios, a framework like Express or a reverse proxy like Nginx should be used.

## Persistence Feature

The application now includes a persistence feature that tracks the number of visits:

1. **Visit Counter**:
   - The application keeps track of the number of times it's accessed.
   - Each GET request increments a counter stored in a file named `visits`.
   - The counter persists across server restarts.

2. **New Endpoint**:
   - A new `/visits` endpoint has been added to display the number of recorded visits.
   - Access this endpoint to see how many times the application has been accessed.

3. **Docker Volume**:
   - The `docker-compose.yml` file includes a volume to persist the `visits` file.
   - This ensures the counter is preserved even when containers are restarted.

4. **File System Operations**:
   - The application uses Node.js's `fs` module to read from and write to the `visits` file.
   - Error handling is implemented to ensure the application remains stable.

## Coding Standards

1. **Naming Conventions**:  
   - Functions like `getMoscowTime()` use camelCase.
2. **Single Responsibility**:  
   - The `requestHandler` function is solely responsible for handling HTTP requests.  
   - The `getMoscowTime` function only calculates the correct time.
3. **Modular Code**:  
   - Even though it's short, the logic is grouped—making it easy to expand if we need more features in the future.

## Testing

1. **Manual Testing**:  
   - I ran the application locally using `node server.js`.  
   - Visited `http://localhost:8000` in my browser to ensure the server responds correctly.  
   - Refreshed the page multiple times to confirm the displayed time updates properly.
   - Accessed the `/visits` endpoint to verify the counter increments correctly.
2. **Simple Verification**:  
   - Checked that it always displays the correct Moscow time (cross-checked with other world clock sources).  
   - Confirmed it handles multiple requests without error.
   - Verified that the visit counter persists across server restarts.

## Additional Setup

- **MIT License**:  
  I have included an MIT License file in the project. This keeps our code open-source and permissive for anyone to use or modify under the license terms.

- **Linting with ESLint**:  
  To maintain code quality and consistency, I used [ESLint](https://eslint.org/). ESLint checks for style compliance and potential issues in the code.

- **`package.json`**:  
  The project is configured with a basic `package.json` specifying:
  - Node.js version (>=18.0.0)  
  - Project metadata  
  - ESLint as a development dependency

## Conclusion

This tiny Node.js application was a fun way to quickly spin up a web server and showcase time zone handling! By leveraging Node.js's built-in `http` module, we avoided extra dependencies and focused on learning and applying best practices. The addition of the persistence feature demonstrates how to maintain state across server restarts, which is a crucial aspect of many web applications. If this application needed more complex features—like templating or database interactions—we could always switch to a full-fledged framework like Express in the future.

> **Tip**: If you are running into permission issues on certain ports, pick a higher port (e.g., 8000) or run as an administrator. Also, remember that Node.js's built-in server is not recommended for production-level deployments.
