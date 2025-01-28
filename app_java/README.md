# Instructrions to run the project

## Requirements:

- Java 17
- Maven
- Spring Boot

Also please add the following dependencies in your pom.xml for Maven:

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
