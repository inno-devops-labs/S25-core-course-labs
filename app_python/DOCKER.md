# Applied Best Practices

* **Specify Python version and its `sha256` digest**: It guarantees that the exact image version is used and, as a
  result, reduces risk to face with breaking changes.
* **Run application tests when building the `Docker` image**: It makes our application more robust, because
  until some application component is not working correctly, image will not be built and distributed with broken code.
* **Add non-root user that runs application**: It minimizes the risk of taking control of the system by someone else.
* **Disable shell for this user**: The same reason as above.
* **Copy only specific files**: It keeps the image smaller by avoiding copying unnecessary files.
* **Use `.gitignore`**: The same reason as above.
* **Use `EXPOSE` in `Dockerfile`**: It tells the user what ports the application is listening on.
* **Add environment variable for application argument `--timezone`**: It makes container configurable, so its behavior
  can be changed without modifying source code and rebuilding the image.
