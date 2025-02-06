# Flutter Application (Northern Lights)

## Why Flutter?
- Flutter uses a **widget-based architecture** for building UIs.
- Its **hot-reload** feature enables faster development and iteration.
- Cross-platform capabilities allow the app to run on both Android and iOS with a single codebase.
- Flutter’s rich set of **pre-designed widgets** allows for highly customizable UIs.
- Built-in **animation support** makes it perfect for complex UI like the Northern Lights animation.

## Best Practices:
- Followed Flutter's **widget-based architecture** for UI components.
- Used **custom animations** for creating the Northern Lights effect.
- Managed **dependencies** effectively in `pubspec.yaml` file.
- Structured the project with **modular design** using different Dart files for UI and logic.
- Used `.gitignore` to ignore unnecessary files, including build artifacts.

## How to test the Northern Lights App?
- Run the app and verify the **Northern Lights animation** is visible.
- Ensure the app is responsive and works correctly across different screen sizes.
- Refresh the app and check that the animation runs continuously without errors.

# Unit Testing Best Practices for Flutter

## Unit Tests
The unit tests ensure that:
- The app renders the UI correctly without exceptions.
- The **NorthernLightsWidget** appears in the widget tree.
- **Unit tests for rendering** validate the presence of essential widgets, like the title and the animation.

### 1. Best Practices Applied
1. **Test Independence:** Each test is independent and does not rely on other tests or external data.
2. **Widget Testing:** Used `flutter_test` for widget testing to ensure the UI components are rendered correctly.
3. **Automated Assertions:** Used `expect` statements to check if essential widgets (like the title and animation) exist in the widget tree.
4. **UI Validations:** Ensured the app renders without any issues and the `NorthernLightsWidget` is visible on the screen.

### 2. How to Run Unit Tests Locally:
To manually run the unit tests, execute the following command:
```sh
flutter test
```