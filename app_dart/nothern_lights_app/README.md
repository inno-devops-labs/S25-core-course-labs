# Northern Lights Flutter App

## Description
A simple Flutter application that displays an animation of the Northern Lights.

## Installation
```bash
git clone https://github.com/Galyusha/s25-core-course-labs/app_dart/nothern_lights_app.git
cd northern-lights-app
flutter pub get
flutter run
```

## Unit Tests

### Running Tests
To run the unit tests for this Flutter application, use the following command:

```bash
flutter test
```

## Continuous Integration & Deployment (CI/CD)

### GitHub Actions Workflow
This repository uses GitHub Actions to automate the following:
1. Runs `flutter analyze` to check for code quality.
2. Runs the unit tests for the Flutter app.
3. If tests pass, the app is containerized and pushed to Docker Hub.