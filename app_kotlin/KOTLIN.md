# KOTLIN.md

## Justification for Using Ktor

Ktor was chosen for this project due to its advantages, which align with the project's goals:

- **Kotlin Native**: Ktor is a Kotlin-native framework, allowing us to leverage the benefits of the Kotlin language.
- **Lightweight and Minimalistic**: Ktor follows a minimalistic approach, making it suitable for small and simple web applications like this one.
- **Asynchronous Support**: Ktor excels in handling asynchronous operations, which can improve the responsiveness of the application.

## Implementation of Best Practices and Coding Standards

I adhered to best practices:

- **Kotlin Style Guide**: Followed the official Kotlin style guide to maintain clean and consistent code.
- **Modular Structure**: Maintained a clear separation of concerns through a modular project structure.
- **Testing**: The web application is thoroughly tested using Kotest, a popular testing framework for Kotlin projects.
- **.gitignore**: Utilized a .gitignore file to exclude unnecessary files from version control.

## Testing the Application

To test the application you should run:

>`./gradlew test`

The test ensure the functionality and reliability of the Kotlin Ktor application.