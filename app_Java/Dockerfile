# OpenJDK as the base image for compiling the Java application
FROM openjdk:11-jdk-slim AS build

# Create a non-root user and group
RUN useradd -m appuser
WORKDIR /app
USER appuser

COPY web_app.java .

# Download the Spark framework (Spark 2.9.3) and compile the Java application
RUN curl -o spark-core-2.9.3.jar https://repo1.maven.org/maven2/com/sparkjava/spark-core/2.9.3/spark-core-2.9.3.jar
RUN javac -cp spark-core-2.9.3.jar web_app.java

# Use a minimal JRE base image for running the application
FROM openjdk:11-jre-slim

# Create a non-root user in the runtime container
RUN useradd -m appuser
USER appuser

# Set working directory
WORKDIR /app

# Copy compiled Java files from the build stage
COPY --from=build /app /app
EXPOSE 4567

# Command to run the Java application
CMD ["java", "-cp", ".:spark-core-2.9.3.jar", "OmskTimeApp"]
