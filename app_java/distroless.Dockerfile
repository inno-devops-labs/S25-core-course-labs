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
FROM gcr.io/distroless/java17-debian12:nonroot

WORKDIR /app

ENV JAR_FILE=app_java-0.1.jar

COPY --from=build /app/target/${JAR_FILE} .

ENTRYPOINT ["java", "-jar", "app_java-0.1.jar"]
