# Lab 1 (Bonus): Web Application Development

## **Language:** JavaScript (Node.js)  
- Lightweight and efficient for small-scale web servers.
- Uses non-blocking I/O, making it ideal for handling simple HTTP requests.
- Easy to containerize with minimal dependencies.

## Best practices applied

1. **Built-in http Module for Simplicity**
    - Instead of installing additional dependencies, used the built-in http module. This keeps the application lightweight and free from unnecessary dependencies.

2. **Proper HTTP Headers for Response**
    - Every HTTP response includes a Content-Type header to indicate the type of content being sent to avoid ambiguity and potential security issues.

3. **Properly Handled Requests**
    - A basic server that responds to all incoming requests.