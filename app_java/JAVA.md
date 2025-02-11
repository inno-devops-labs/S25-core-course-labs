# Lab #1

Since there are no separate tasks for the bonus project, I will start by explaining everything immediately. Before that,
a brief overview:

- **Overview**: This is a Java-based application with an API for calculating vacation pay. The framework used is *
  *Spring Boot V3.0**, considered the gold standard for Java microservice development.

---

## Techniques for a Well-Structured Java Microservice

- **Java Code Conventions**:
  - Followed standard Java code conventions, including naming, file organization, and code file structure.

- **Flexible Configuration**:
  - Utilized a flexible approach by reading properties from special files in the resources folder for application
    configuration.

- **Checkstyle**:
  - Ensured code style consistency using Checkstyle, with additional properties configured in files located in the
    project root directory.

- **Maven Wrapper Usage**:
  - Deployed and built the application on different machines using Maven. The application is packaged as a
    single `.jar` file built with the Maven wrapper, ensuring compatibility across most operating systems.

---

## Comments on Code

I do not have any comments on the code. My point is that if the application is not complex and the code is not a "
spaghetti mess," we can make decisions based on the advice Robert J. Martin gave in his book "Clean Code": we do not
need to exhaustively comment our code if it is already understandable.

---

## P.S

When I was making this part of lab 1, I already knew that Dockerfiles is the next lab part, so
in the app_python there is a Dockerfile, and in the app_java I stopped on the .jar usage
(for now).

---

# Lab 2

---

For this application unit testing, I create the exhaustive set of tests that covered almost all the business logic
related codebase.
Only this functionality was tested because, in the specific Java language, there are a lot of frameworks, and this is
unnecessary to test each one's functionality.

## The main features

- Business logic functionality: tests are mostly covered indeed; the business functionality that will deliver
  the final answer to the user
- Separate Logic: Tests are separated into different files to make it more concise to read the tests and maintain
  them
- Naming: I use the given...when...then... test case naming to properly introduce the purpose of the
  specific test
- Separate context: to make tests more isolated, the library junit5 recreates the context for each test class.
  (context is a way of environment control provided by the Spring Boot framework)
