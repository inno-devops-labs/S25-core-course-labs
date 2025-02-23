# Docker best practices for the Java Web App

---

## 1. **Multi-stage builds**

- **Builder Stage**: Uses the `eclipse-temurin:21-jdk-jammy` image to build the application with Gradle.
- **Runtime Stage**: Uses the smaller `eclipse-temurin:21-jre-jammy` image to run the application, reducing the final
  image size.

---

## 2. **Base image**

- The `eclipse-temurin` image is used because it is a lightweight and widely-used base image for Java applications.
- The JDK image is used in the builder stage for compiling the application, while the JRE image is used in the runtime
  stage to reduce the image size.

---

## 3. **Layer caching**

- The `build.gradle`, `settings.gradle`, and `src` directory are copied separately to leverage Docker's layer caching.
  This ensures that only changes to these files trigger a rebuild of the corresponding layers.

---

## 4. **Minimizing image size**

- The final image only includes the built JAR file and the JRE, excluding unnecessary build tools and dependencies.
- This reduces the image size and improves security by minimizing the attack surface.

---

## 5. **Port exposure**

- The `EXPOSE 8080` instruction documents that the application listens on port 8080. This does not publish the port but
  serves as documentation for users.

---

## 6. **Entrypoint**

- The `ENTRYPOINT` instruction specifies the command to run the application. This ensures the application starts
  automatically when the container is run.

---

## 7. **Environment variables**

- If needed, environment variables can be passed to the container using the `-e` flag with `docker run`. For example:
  ```bash
  docker run -e "SPRING_PROFILES_ACTIVE=prod" -p 8080:8080 your-image-name
  ```

## 8. **.dockerignore practice**

- A .dockerignore file is recommended to exclude unnecessary files (e.g., build directories, IDE files) from being
  copied into the Docker image
