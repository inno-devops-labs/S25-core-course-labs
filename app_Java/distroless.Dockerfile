# Build stage
FROM openjdk:11-jdk-slim AS build
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY OmskTimeApp.java .
RUN curl -o spark-core-2.9.3.jar https://repo1.maven.org/maven2/com/sparkjava/spark-core/2.9.3/spark-core-2.9.3.jar
RUN javac -cp spark-core-2.9.3.jar OmskTimeApp.java

# Runtime stage using Distroless
FROM gcr.io/distroless/java11-debian11:nonroot

WORKDIR /app
COPY --from=build /app /app

EXPOSE 4567

CMD ["java", "-cp", ".:spark-core-2.9.3.jar", "OmskTimeApp"]
