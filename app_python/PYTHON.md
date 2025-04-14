# Unit Tests

## Best Practices Applied
- Frequent commits and small changes
- Automated build and test processes
- Timeout-based testing. Simulate real-world usage and verify that the time is updated correctly.

## Best Practices Applied
- **test_homepage_status** This test executes a GET request to the main page ("/") and verifies that the response code is 200, indicating that the page has loaded successfully.
- **test_homepage_contains_time** This test check that the time is displayed on the main page.
- **test_get_time_format** This test verifies that the get_time() function returns a string corresponding to the time format "HH:MM:SS"
- **test_get_time_correctness** This test verifies that the time returned by the get_time() function corresponds to the current time in Moscow.
- **test_get_time_multiple_calls** This test executes five consecutive calls to the get_time() function with a 0.5 second pause between each call. We check that all calls return non-empty values and that the time varies between calls.
- **test_get_time_different_timezones** This test checks that passing a different time zone to the get_time() function affects the result. We set the time zone for Tokyo and check that the time matches the expected time.