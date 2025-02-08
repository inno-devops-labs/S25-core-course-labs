FROM eclipse-temurin:21-jdk-jammy AS builder

WORKDIR /app

# Copy all necessary Gradle wrapper files and project files
COPY gradlew .
COPY gradlew.bat .
COPY gradle/wrapper/gradle-wrapper.jar .
COPY gradle/wrapper/gradle-wrapper.properties .
COPY build.gradle .
COPY settings.gradle .
COPY src ./src

# Make gradlew executable
RUN chmod +x ./gradlew

# Build the application
RUN ./gradlew build

# Use a smaller runtime image for the final stage
FROM eclipse-temurin:21-jre-jammy

WORKDIR /app

# Copy the built JAR file from the builder stage
COPY --from=builder /app/build/libs/mgntime-0.0.1-SNAPSHOT.jar app.jar

# Expose the port the application runs on
EXPOSE 8080

# Define the command to run the application
ENTRYPOINT ["java", "-jar", "app.jar"]
