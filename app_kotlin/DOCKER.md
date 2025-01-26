# Overview

## Best Practices Implemented

### Multi-Stage Dockerfile

- Multi-stage build: The Dockerfile with separated build and runtime environments. This choice makes final image size smaller and keeps runtime image clean.
    - Stage 1. Build Environment
        - `gradle:8.12-jdk21` is the base image for building the app
        - Gradle dependencies are cached to optimize build time
        - The fat JAR file is built in this stage (gradle-specific)
    - Stage 2. Runtime Environment:
        - `amazoncorretto:22` is the runtime base image for the standard image
        - The fat JAR file is copied from the build stage
        - Only the application JAR is included

## Distroless Image

- Base Image for distroless runtime `gcr.io/distroless/java21:nonroot` is used in the second version of the runtime image
- The nonroot tag ensures that the application runs with non-root privileges to enhance security
- The Distroless image is approximately half the size of the standard runtime image

[sizes comparison](size_comparison.png)
