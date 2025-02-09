# Java Web App - best practices and structure

## 1. **Project structure**

```
src/
├── main/
│ ├── java/
│ │     └── com/example/mgntime/
│ │         ├── ClockController.java
│ │         └── MgnTimeApplication.java # Main application class
│ └── resources/
│       ├── static/                 # Static files (e.g., images, CSS, JS)
│       ├── templates/              # Thymeleaf templates (e.g., HTML files)
│       └── application.properties  # Configuration properties
│ 
└── test/
    └── java/
        └── com/example/mgntime/
            └── ClockControllerTest.java # Unit test for controller
```

## 2. **Best practices**
### 2.1 **Separation of concerns**
- **Controller**: Handle HTTP requests and delegate business logic to services.
- **Templates**: Use Thymeleaf for server-side rendering of HTML.

### 2.2 **Use of dependency injection**
- Spring Boot’s `@Controller` and `@Autowired` annotations are used for dependency injection, ensuring loose coupling.

### 2.3 **Error handling**
- The JavaScript `fetch` API includes error handling to log issues with the `/time` endpoint.

### 2.4 **Testing**
- JUnit test is written for the `ClockController` to ensure the `/time` endpoint works as expected.

### 2.5 **Configuration**
- The `application.properties` file is used for configuration (e.g., server port, Thymeleaf settings).

### 2.6 **Frontend best practices**
- **CSS**: Styles are modular and scoped to specific components.
- **JavaScript**: The clock is updated dynamically using `fetch` and `setInterval`.

### 2.7 **Version control**
- A `.gitignore` file is included to exclude unnecessary files (e.g., build files, IDE files).

---

## 3. **Tools and libraries**
- **Spring Boot**: For building the web application.
- **Thymeleaf**: For server-side rendering of HTML.
- **Gradle**: For dependency management and building the project.
- **JUnit**: For unit testing.
---
