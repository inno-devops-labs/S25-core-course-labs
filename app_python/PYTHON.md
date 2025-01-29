# Moscow Current Time Web Application

## Framework:

Flask was chosen as a framework for this project as it is simple yet functional and lightweight.

## Best practices:

1. Code matches PEP-8 standard, so it is easily readable.
2. Code has proper naming.
3. Code is well-structured and documented.

## Coding standarts:

- Timezone is handled via the pytz library that ensures the proper values for the Moscow.

- The current time is passed dynamically to the `index.html` template using Flask's `render_template` function.

## Testing:

Testing was done manually by checking if the time on the page update matches the real Moscow time zone time (which it does).
