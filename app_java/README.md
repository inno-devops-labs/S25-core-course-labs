# Instructrions to run the project

## Requirements:

- Java 17
- Maven
- Spring Boot

Also please add the following dependencies in your pom.xml for Maven if they are missing:

```bash
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-thymeleaf</artifactId>
    </dependency>
</dependencies>
```

## To run the web application on your machine, follow the steps:

1. Clone the repository:

```bash
    git clone https://github.com/mngcndl/S25-core-course-labs
    cd S25-core-course-labs/app_java
```

2. Build the project using Maven:

```bash
    mvn clean install
```

3. Run the application:

```bash
    mvn spring-boot:run
```

4. Go to your web browser and open the url: http://localhost:8080

## To run the web application on your machine using Docker, follow the steps:

If you already have all the files locally, build the image:

```bash
    docker build -t mangocandle/app_java:latest .
```

OR

1. Pull the image:

```bash
    docker pull mangocandle/app_java:latest .
```

2. Run the image:

```bash
    docker run -p 8080:8080 mangocandle/app_java:latest
```
