## Framework

Because this application is very small and there is no need in Flask features,
I chose lightweight `Bottle` framework.

## Applied best practice

* **Separate logic into services**: This not only makes it easier to test the application, but also allows you to easily
  change one behavior to another if needed, without changing unrelated code. So, there are two services:
    1. `TimeService`, which provides current time.
    2. `TemplateService`, which creates output for the user.

* **Configuration of `Production` and `Test` applications is separated**: One configuration does not affect the other
  in any way.

* **There are arguments for timezone, host and port**: It allows you to easily change configuration of application
  without changing the source code.

## Unit Tests

### Applied best practice

* **Mock services in `Test` application**: Unit tests without mocking are actually integration tests, which are always
  heavier and more complex, and if there are some changes in several services, it is harder to find where the error is.

* **Isolate side effects**: Also, mocks are very useful due to isolation from the world: for example, when some
  controller is tested, it is unnecessary to test external states like databases, real time, etc.

* **Use `setUp`**: This method is used in all test classes to initialize required objects before each test, reducing
  code duplication.

* **Use `assert`**: Each test has `assert` usage to not only verify that there are no errors, but also test expected
  behavior.

* **Tests with real time use time ranges in `assert`:** The retrieved time in such tests is compared with `start` and
  `end` timestamps.

### Tests lists

1. `TestController`, which mocks all services and checks that controller works correctly.
2. `TestZonedTimeService`, which checks that `ZonedTimeService` works correctly.
3. `TestAppConfiguration`, which checks that production application has correct configuration and works correctly.
