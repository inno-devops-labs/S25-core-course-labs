FROM eclipse-temurin:21-jdk-jammy AS builder

WORKDIR /app

# Install Gradle system-wide
RUN apt-get update && apt-get install -y gradle

RUN gradle -v

# Copy Gradle build files and project source code
COPY build.gradle settings.gradle ./
COPY src ./src

# Clean and build the application
RUN gradle clean build --no-daemon

# Use a smaller runtime image for the final stage
FROM eclipse-temurin:21-jre-jammy

WORKDIR /app

# Copy the built JAR file from the builder stage
COPY --from=builder /app/build/libs/mgntime-0.0.1-SNAPSHOT.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]