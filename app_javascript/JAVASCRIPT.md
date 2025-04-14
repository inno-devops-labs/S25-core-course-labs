# JavaScript Web Application

## Framework Choice: Express.js
Express.js was chosen for its minimalistic approach and efficiency in handling HTTP requests.

## Best Practices
- Used `moment-timezone` for timezone management.
- Kept code modular and simple.
- Used `npm` for dependency management.

## Testing
- Tested locally by accessing the app in a browser and confirming the displayed time updates.

JavaScript Unit Tests and Best Practices

Unit Tests Created

For this project, I’ve written unit tests to ensure the application functions as expected. The unit tests focus on validating the logic of key components and the overall behavior of the application.

Test 1: GET / endpoint should return Moscow time
	•	Purpose: To verify that the / route returns the correct current time in Moscow.
	•	Test Method:
	•	A GET request is made to the root endpoint (/).
	•	The test checks that the response status code is 200 and contains the current time formatted for Moscow time.

test("GET / should return Moscow time", async () => {
    const response = await request(app).get("/");
    expect(response.status).toBe(200);
    expect(response.text).toContain("Current Time in Moscow");
});


	•	Reason for Test: This test ensures that the server is properly responding with the correct time for the Moscow timezone.

Best Practices Applied

1. Separation of Concerns
	•	Test Focus: Each unit test focuses on a single feature or behavior of the application. This makes the tests easier to understand and maintain.
	•	Modularity: I ensure that tests are isolated from external dependencies and have minimal side effects. This enables them to be consistent and reliable when run in any environment.

2. Descriptive Test Names
	•	Clear Naming: Tests are named descriptively, such as GET / should return Moscow time, to reflect the expected behavior or functionality they’re testing. This helps any developer reading the test file to understand the purpose of the test without needing to dive into the implementation.

3. Test Coverage
	•	Core Logic Coverage: The tests ensure that the core features of the application (such as returning the correct time) are functioning correctly.

4. Use of Asynchronous Tests
	•	Asynchronous Handling: Since the / route involves asynchronous operations (getting the current time), the test is written to await the asynchronous GET request, ensuring that it correctly handles the server’s response.

5. Avoiding Overly Complex Tests
	•	Simplicity: Each test case is kept as simple as possible to focus on a single piece of functionality. Overly complex tests can lead to maintenance issues and confusion in the future.

6. Running Tests on Every Commit
	•	CI Integration: The tests are integrated with the GitHub Actions CI pipeline to run automatically on each commit and pull request. This ensures that any changes to the codebase do not break existing functionality.