# Stage 1
FROM gradle:8.12.0-jdk21-alpine AS builder

RUN addgroup -S gradlegroup && adduser -S gradleuser -G gradlegroup
USER gradleuser

WORKDIR /build

COPY build.gradle.kts settings.gradle.kts ./
COPY gradle ./gradle
COPY src ./src

RUN gradle build --no-daemon

# Stage 2
FROM gcr.io/distroless/java21-debian12:nonroot
WORKDIR /app
COPY --from=builder /build/build/libs/*.jar /app/app.jar
ENTRYPOINT ["/usr/bin/java", "-jar", "/app/app.jar"]