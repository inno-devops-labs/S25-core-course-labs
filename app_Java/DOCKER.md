# Docker Best Practices for Java Ib Application

## Best Practices Implemented

### 1. **Using a Minimal Base Image**

- I use `openjdk:11-jdk-slim` instead of a full OpenJDK image to reduce the image size and minimize security vulnerabilities.
  ```dockerfile
  FROM openjdk:11-jdk-slim AS build
  ```

### 2. **Setting a Working Directory**

- Using `WORKDIR /app` ensures all subsequent commands run within the `/app` directory, improving maintainability.
  ```dockerfile
  WORKDIR /app
  ```

### 3. **Copying Only Necessary Files**

- Instead of copying everything, I copy only the required files to minimize image size.
  ```dockerfile
  COPY OmskTimeApp.java .
  ```

### 4. **Using a .dockerignore File**

- A `.dockerignore` file is included to exclude unnecessary files from the build context:
  ```plaintext
  target/
  *.class
  .git/
  ```
- This reduces image size and improves build performance.

### 5. **Installing Dependencies Efficiently**

- I ensure that dependencies (like Spark) are downloaded within the build process efficiently.
  ```dockerfile
  RUN curl -o spark-core-2.9.3.jar https://repo1.maven.org/maven2/com/sparkjava/spark-core/2.9.3/spark-core-2.9.3.jar
  ```

### 6. **Exposing Only Necessary Ports**

- The application runs on port `4567`.
  ```dockerfile
  EXPOSE 4567
  ```

### 7. **Running the Application with CMD**

- Using `CMD` instead of `ENTRYPOINT` makes it easier to override the default command during runtime if needed.
  ```dockerfile
  CMD ["java", "-cp", ".:spark-core-2.9.3.jar", "OmskTimeApp"]
  ```

### 8. **Avoiding Running as Root User**

- To enhance security, I created a non-root user and run the application as that user:
  ```dockerfile
  RUN useradd -m appuser
  USER appuser
  ```
- This prevents privilege escalation in case of security vulnerabilities.

## **Comparison: Standard vs. Distroless Images**

- **Standard Image** - Larger; has package manager shell; standard performance.
- **Distroless Image** - Smaller; no shell, no package manager; more secure, optimized.

### Distroless

- Smaller attack surface: No shell or package manager reduces vulnerabilities.
- Faster startup: No OS-related overhead.
- More secure: Runs as a **non-root** user by default.

**Standard image is larger**, the **Distroless image provides an advantage** by:

- **Reducing unnecessary components**: Standard images include package managers and shell utilities that are not required for running Java applications.
- **Lowering security risks**: The absence of a shell and package manager minimizes the attack surface.
- **Improving efficiency**: Even with the same runtime functionality, a smaller image means faster deployment and less disk space usage.

Standard Image: 
![Скриншот 28-01-2025 224452](https://github.com/user-attachments/assets/c4294334-ec15-429d-8f40-6eaf024486ed)

Distroless Image: 
![Скриншот 28-01-2025 224517](https://github.com/user-attachments/assets/b72688fc-55a9-4815-96e8-eddf59c309bd)
