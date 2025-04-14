# app_python

This web application displays current time in Moscow

## Framework Choice

For the implementation, FastAPI was chosen as it was the most simple solution to the given task in my opinion.

## Best Practices

* Code is formatted according to PEP8
* Typings are used where possible
* No global variables (FastAPI's one does not count, it wouldn't work without it)
* pytest is used for unit tests, the tests are written in separate module

## Unit Tests

### `test_create_time_string`

Checks if time string is formatted correctly

### `test_create_response`

Checks if created response always contains time string
