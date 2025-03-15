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

* **Mock services in `Test` application**: Unit tests without mocking are actually integration tests, which are always
  heavier and more complex, and if there are some changes in several services, it is harder to find where the error is.

* **There are arguments for timezone, host and port**: It allows you to easily change configuration of application
  without changing the source code.

## Tests

1. `TestController`, which mocks all services and checks that controller is working correctly.
2. `TestZonedTimeService`, which checks that `ZonedTimeService` is working correctly.
