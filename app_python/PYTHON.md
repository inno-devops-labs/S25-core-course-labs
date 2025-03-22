# Framework

I chose FastAPI because it's very popular, easy to learn and can be used for high-performance applications

## Best Practices

1. Usage of library `pytz` in order to work with different time zones
2. Usage of `KISS pattern` to make code more readable, reduce the likelihood of errors, and simplify maintenance

## Testing

1. Test for response status code, if code 200 - everything is fine
2. Test for html validity, if `<html>`, `<head>` and title "Текущее Московское время" in response html - everything is fine
3. Test for time validity, check if current time hours and minutes are in html, if so - everything is fine
