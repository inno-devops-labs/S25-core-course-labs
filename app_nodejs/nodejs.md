# Node.js Web Application Documentation

## 1. Introduction  
This document outlines the development of the Node.js web application, including the rationale for choosing Node.js and Express, the best practices applied, and the testing methods used to ensure code quality and reliability.

---

## 2. Why Node.js and Express?  
- **Fast and Lightweight:** Node.js is ideal for quick prototyping and building scalable applications due to its non-blocking I/O model.  
- **Large Ecosystem:** The npm (Node Package Manager) provides access to a vast library of packages, enabling rapid development.  
- **Single Language:** Using JavaScript for both front-end and back-end development streamlines the development process and reduces context switching.  

---

## 3. Best Practices Applied  
The following best practices were implemented to ensure a clean and maintainable codebase:  

- **Folder Structure:** A minimal folder structure was maintained for simplicity, ensuring the demo remains easy to navigate and understand.  
- **Routing:** Express routing was implemented in a single file for simplicity, making it easier to manage endpoints in a small-scale application.  
- **Code Style:** Consistent JavaScript styling was enforced, with tools like ESLint or Prettier recommended for maintaining code readability and uniformity.  

---

## 4. Testing  
Testing was conducted to ensure the application functions as expected:  

- **Manual Testing:** The server was manually tested to confirm it starts correctly and that the web page is reachable at the specified endpoint.  
- **Automated Testing (Optional):** For production readiness, automated testing frameworks like Jest or Mocha could be added to create comprehensive test suites.  

---

## 5. Code Quality  
To maintain high code quality, the following practices were implemented:  

- **Version Control:** Changes were committed step-by-step using Git, ensuring clarity and traceability in the development process.  
- **Gitignore:** The `.gitignore` file was used to exclude unnecessary files like `node_modules` and logs, keeping the repository clean and focused.  

--- 

## 6. Unit Tests

The Node.js application includes automated unit tests implemented with Mocha, Chai, and Supertest. These tests ensure that key functionalities of the application are working as expected. The tests include:

- **Response Status and Content Type Check:**  
  Verifies that the homepage returns a 200 status code and that the content type is correctly set to HTML.

- **Response Content Validation:**  
  Confirms that the homepage contains the expected welcome message and a correctly formatted time string with the 'MSK' timezone abbreviation.

- **Time Accuracy Check:**  
  Validates that the displayed time is accurate by comparing it with the current time in the Moscow timezone, ensuring the difference is within a two-second threshold.

### Running the Unit Tests

To run all unit tests, execute:
```bash
npm test