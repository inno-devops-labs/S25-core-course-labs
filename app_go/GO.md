# Random Daily Predictions

## Task 1

### Choose a suitable framework for your web application and justify your choice

I chose Go's built-in net/http package because:

1) It is lightweight, performant, and suitable for simple web applications
2) It is easy to use, test and debug

## Task 2

### Describe best practices applied in the web application

1) Using camelCase for variable names
2) Keeping the code clean and readable

### Explain how you followed coding standards, implemented testing, and ensured code quality

I followed the following coding standards:

1) Organized the code for clarity and ensured logical separation of concerns.
2) Descriptive naming like randomPrediction to enhance code readability

**Testing:**

Obviously, I checked that the web application generates and displays a random prediction upon each request.

**Code quality:**

The code runs without errors, the code is light and scalable.

## Unit Tests

### Describe the unit tests and the best practices you applied

The unit tests check that:

- The HTTP endpoint (`/`) returns a valid JSON response.  
- The response contains a `prediction` field.  
- The predictions are randomly selected from the predefined list.  

I have applied the following practices:

- **Isolation**: Each test runs independently without side effects.  
- **Table-Driven Tests**: Structured test cases improve coverage.  
- **Error Handling**: Ensures proper HTTP responses and JSON encoding.  
- **Automated Execution**: Integrated into GitHub Actions for continuous validation.  
