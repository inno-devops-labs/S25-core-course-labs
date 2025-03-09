# Framework to work with: Express.js

## Explaining the choice of framework
Express is a minimal and flexible Node.js web application framework. I chose it because worked with WebStorm already.

## Best Practices
1. **Code Structure**: The application has a clear structure.
2. **Package management**: Used `package.json` for dependencies.
3. **Testing**: Easy to write tests for more complex apps. I didn't use them as the app is easy to launch and refresh the page to see that the time changes in real time.
4. **Handling specific timezone**: Used the `moment-timezone` library for Moscow timezone.

##  Dockerfile Distroless Key Features
### **Multi-Stage Build**:
Utilizes a builder stage to install dependencies and then copies only necessary files to the final image.
### **Base Image**:
Uses `gcr.io/distroless/nodejs20-debian12:nonroot`, which is a minimal, secure image.
### **Security**:
Runs the application as a non-root user by default.
### **Execution Context**:
The entrypoint of this image is set to "node", so this image expects users to supply a path to a .js file in the CMD.

## Unit tests
1. **Test Library**: `supertest` is a great choice for testing HTTP endpoints.
2. **Test Structure**:
* `describe`: Grouping your test cases for better readability
* `it`: Describing what the specific test should accomplish.
3. **Test Implementation**
* Using `await` to make an asynchronous request.
* The `moment-timezone` library is used to handle timezones explicitly.