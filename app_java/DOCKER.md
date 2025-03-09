# Docker Best Practices for Spring Boot

## 🛠️ Best Practices Implemented:

1. **Multi-stage build** – separates build and launch, reducing the size of the final image.
2. **Alpine-based JDK** – uses `eclipse-temurin:17-jdk-alpine` for minimum size.
3. **Minimal JRE for Runtime** – uses `eclipse-temurin:17-jre-alpine` instead of JDK.
4. **`.dockerignore` file** – eliminates unnecessary files (`target/`, `.mvn/`).
5. **Non-root user** – runs from `myuser', not `root'.
6. **Optimized layers** – The `poms' are copied first.xml` and `.mvn/` for caching dependencies.