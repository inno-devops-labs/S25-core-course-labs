#Multistage build

# Build project in builder directory (using 'nobody' user)
FROM gradle:7.5.1-jdk11-alpine as builder
USER root
WORKDIR /builder
COPY . /builder
RUN gradle build --stacktrace

# Use official JDK image for running
FROM amazoncorretto:17-alpine3.15
# Create app folder
RUN mkdir /app && chown -R nobody /app
WORKDIR /app
# open ports
EXPOSE 8080
# Copy from builder our binary file
COPY --from=builder /builder/build/libs/com.example.app-sample-all.jar .
# Set final user as 'nobody'
USER nobody
# Run file
CMD ["java", "-jar", "com.example.app-sample-all.jar"]