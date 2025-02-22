# Flutter Yekaterinburg Time Web App

## Framework Choice

I chose **Flutter** as a UI framework for its ease
of use in creating scalable, production-ready, cross-platform applications.

## Best Practices

- **Modular Code**: The application follows the principle
  of [Clean Architecture](https://www.geeksforgeeks.org/complete-guide-to-clean-architecture/)
  and provides strict way to separate business logic (domain layer) from the presentation layer.

- **Dart analysis Compliance**: The code conforms to standard Dart analysis
  to avoid potential warnings and errors and ensure consistent formatting.

- **Naming Conventions**: camelCase is used for variables and functions
  to enhance code readability and maintainability.

- **Integration testing**: Widget testing is implemented with
  Flutter widget testing to ensure that functionality is valid

## Unit tests

Comprehensive integration test is provided to check the correctness
of the primary web page: content and styles of each widget.
Source code can be found at `/test` folder

### Best practices

- **Comprehensive Ui test**: Each widget's parameter on the screen is checked on consistency (texts contents, styles). 

- **Optimized test execution time**: In order to optimize the duration of each ui test,
  Flutter test system uses its own time environment under the hood to skip unnecessary frames.
  Time is managed manually, meaning that scenario that requires 10 seconds will use only 3-4 seconds of real time
  See [docs](https://api.flutter.dev/flutter/flutter_test/WidgetTester/pump.html) for additional details.

- **Tests documentation**: Tests have documentation on what they are expected to cover
  and what constraints they will follow (e.g. one time request or continuous requests)
