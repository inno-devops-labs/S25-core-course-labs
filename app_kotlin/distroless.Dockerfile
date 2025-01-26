# Stage 1: Build the Fat JAR
FROM gradle:8.12-jdk21 AS build
WORKDIR /home/gradle/src
COPY . .
RUN gradle buildFatJar --no-daemon

# Stage 2: Distroless Runtime Image
FROM gcr.io/distroless/java21:nonroot
EXPOSE 8080
WORKDIR /app
COPY --from=build /home/gradle/src/build/libs/*.jar /app/timezones.jar
ENTRYPOINT ["java", "-jar", "/app/timezones.jar"]
