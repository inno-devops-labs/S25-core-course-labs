# Use OpenJDK as the base image for compiling the Java application
FROM openjdk:11-jdk-slim AS build

# Install curl for downloading dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -m appuser

# Set working directory and give non-root user ownership
WORKDIR /app
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Copy the Java source file
COPY OmskTimeApp.java .

# Download the Spark framework (Spark 2.9.3)
RUN curl -o spark-core-2.9.3.jar https://repo1.maven.org/maven2/com/sparkjava/spark-core/2.9.3/spark-core-2.9.3.jar

# Compile the Java application
RUN javac -cp spark-core-2.9.3.jar OmskTimeApp.java

# Use a lightweight JRE base image for running the application
FROM openjdk:11-jre-slim

# Create a non-root user in the runtime container
RUN useradd -m appuser

# Set working directory and grant permissions
WORKDIR /app
RUN chown -R appuser:appuser /app
USER appuser

# Copy compiled Java files from the build stage
COPY --from=build /app /app

# Expose port 4567 for the web application
EXPOSE 4567

# Command to run the Java application
CMD ["java", "-cp", ".:spark-core-2.9.3.jar", "OmskTimeApp"]
