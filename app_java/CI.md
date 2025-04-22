# Continuous Integration (CI) Best Practices for Java Spring Boot + Gradle

### **🔹 Build & Test**
- Checks out the repository.
- Sets up Java (`JDK 17`).
- Installs dependencies using Gradle.
- Runs unit tests with `JUnit`.
- If tests pass, proceeds to the Docker build step.

---

## **️Best Practices Implemented**
### **1. Automated Dependency Management**
- The workflow uses **Gradle** to manage dependencies.
- Caches Gradle dependencies for **faster builds**.

### **2. Code Linting & Formatting**
- Uses **Checkstyle** and **SpotBugs** for static code analysis.
- Ensures consistent code formatting with `google-java-format`.

### **3. Unit Testing Before Deployment**
- Runs tests **before building the Docker image** to prevent deployment of bad code.
- Uses **JUnit & MockMvc** for integration testing.

### **4. Optimized Docker Builds**
- Implements **layer caching (`--cache-from`)** for faster image builds.
- Uses a **multi-stage Docker build** to separate dependencies.

### **6. CI Trigger Optimization**
- The workflow runs **only when necessary**:
    - Triggers on `push` to `main` and `Lab3`.
    - Triggers on `pull_request` to `main`.
    - Future improvements: Restrict CI to run only when `src/` changes.
