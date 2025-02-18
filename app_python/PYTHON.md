## Moscow Time Web Application

## Framework Choice

I choose Flask python framework, because it suitable for web applications.

## Applied best practices

I follow KISS and DRY best practises in my code every time. Also, I write clear documentation and comments to my code.

## Testing

First, I run the application and test manually.
I refresh page several times to ensure that time displays correctly.
Also, I check dev tools.
I see that layout is responsive, and page looks good in different devices and sizes.
I verify that the API requests are being sent correctly and that the time displayed is accurate according to Moscow's timezone. 

## Unit tests

#### Description

1. Test status code. It must be `200`.
2. Test time format and correct. It must be `%Y.%m.%d %H:%M:%S`.
3. Test that `/` returns the html page.

#### Best practices

1. Each test should be independent and not rely on others. This ensures accurate test results.
2. Use mocks, stubs or variables to isolate external dependencies, such as APIs or databases, to simulate their behavior.
3. Aim for good code coverage with tests.



