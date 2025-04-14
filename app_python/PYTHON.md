# FAQ

This document contains some frequently asked questions and our answers. Use it to get justification of why the application is written as it is.

## Why you are not using Django, FastAPI, _insert framework name_ instead of old slow Flask?

We are aware that there are some pretty nice frameworks for python on the market, that could suite our needs. However, our team is small (1 person basically) and we want to keep our code neat and tidy. Also, we want to have a simple (yet nice) frontend for our application and it is not that could be accomplished neatly with FastAPI.

The project requirements are straightforward - we only need to:

- Handle a single route
- Perform simple datetime calculation
- Return a plain text response

Flask's microframework architecture provides exactly what we need without unnecessary complexity. With no database requirements or complex business logic, Flask's minimal dependencies (only 1MB in size) keep the application lean and efficient. A functional application can be created in a single Python file with minimal boilerplate code, allowing rapid development for this simple use case. Flask applications can be easily containerized or deployed to various hosting platforms, keeping deployment complexity minimal.

Alternatives Considered:
**Django** is overkill for a single-route application - it includes many unused features (ORM, admin interface, authentication system).

**FastAPI** is excellent for APIs and async operations, these features are unnecessary for this simple synchronous application and requires more boilerplate code for basic functionality compared to Flask

**Bottle** is similar microframework to Flask, but has less community support and fewer updates compared to Flask

Flask provides the perfect balance between simplicity and functionality for this time-display application. Its minimalistic approach aligns with our requirements while maintaining flexibility for potential future enhancements. The choice ensures efficient development, easy maintenance, and optimal resource usage.

## Why Unit Tests done this way?

The tests are organized into a separate tests/ directory, and we use Python’s built-in unittest framework. Why bother complex testing for such simple app?

The key tests include:

1. Valid Timezone Test to verify that get_moscow_time returns the correctly formatted date and time when provided with a valid timezone.
2. Invalid Timezone Test. Ensure that an invalid timezone configuration raises a pytz.exceptions.UnknownTimeZoneError.
3. Successful Render Test to confirm that the main endpoint (/) renders the index template correctly with a 200 status code when get_moscow_time succeeds.

### Best Practices Applied

1. Separation of Test and Production Code
2. Isolation of Dependencies
3. Descriptive Naming Conventions
4. Use of Context Managers and Clean-Up
5. Focused Unit Testing
