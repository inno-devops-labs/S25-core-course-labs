## Framework

`Spring Boot` was chosen for this application, because I can control every dependency and use only necessary ones.
Also, it is my favorite framework :)

## Applied best practice

* **Separate logic into services**: This not only makes it easier to test the application, but also allows you to easily
  change one behavior to another if needed, without changing unrelated code. So, there are three services:
    1. `MetricsService`, which counts the total number of visits to each page.
    2. `CharsParser`, which parse string to lists of characters. There are also two implementation: `PlainCharsService`,
       which simply copies chars from string, and `RangedCharsServices`, which can convert ranges such as `a-z` and
       `0-9`.
    3. `GeneratorService`, which generates password.

* **Mock services in tests**: Unit tests without mocking are actually integration tests, which are always heavier and
  more complex, and if there are some changes in several services, it is harder to find where the error is.

* **All services are fully covered with unit tests**: This, of course, does not provide a complete guarantee of the
  bugless application work, since integration tests are needed for this, but it is still very important when developing
  small and large systems.
