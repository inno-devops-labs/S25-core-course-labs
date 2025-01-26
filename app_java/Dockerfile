#
# BUILD STAGE
#
FROM maven:3.9-amazoncorretto-17-alpine AS build
WORKDIR /app

COPY pom.xml .
COPY src ./src

RUN mvn clean package

#
# PACKAGE STAGE
#
FROM openjdk:17-jdk-alpine3.14

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

ENV JAR_FILE=app_java-0.1.jar

COPY --from=build /app/target/${JAR_FILE} /home/appuser/application.jar

ENTRYPOINT ["java", "-jar", "/home/appuser/application.jar"]
