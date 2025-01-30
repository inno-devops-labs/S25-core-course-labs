# JavaScript Web Application – Moscow Time

## Overview
This is a simple **Express.js web application** that displays the **current time in Moscow (MSK)** and updates upon page refresh and dinamically.  

The project follows **best practices**, including:
- Clean and modular **JavaScript (Node.js)** code.
- Proper **ESLint** coding standards.
- Minimal and clear **package.json**.
- Well-structured **Markdown documentation**.

---

## ⚡ Installation & Setup 
- Clone the repository.
- Open folder **app_js**.
- Run **npm install** and **npm start**.

---

## Disctroless Image Version
**How to build?**  
  
- Use *docker build -t moscow-time-app-distroless -f distroless.Dockerfile .*
  
**How to run?**  
  
- Use *docker run -p 3000:3000 moscow-time-app-distroless*

---
The application is also available in a Distroless-based version. However, in this case, the Distroless image turned out to be slightly larger (168MB) compared to the regular image (131MB). This might be due to the build process or the use of additional dependencies.
