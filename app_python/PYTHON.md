# Framework choice

I have chosen Flask as I have some experience with it.
It is suitable for such a simple application.

## Coding standards and practices

1. **Separation of concerns**. The `main.py` file is responsible for running the app and rendering the page, while all
   other files including `html` and `css` files are placed into separate folders.
2. **Error handling**. The code entails an error handling practice using the `try-except` block to return error code 500
   if anything goes wrong with the application.
3. **Timezone configuration**. To display the correct time, timezone is configured using the `pytz` package to avoid
   displaying the wrong time.
4. **PEP 8 Formatting**. The code follows the PEP 8 standard to ensure code readability.
   These practices entail code quality making it more reliable and modular. With error-handling and PEP-8 formatting the
   code also becomes more maintainable.
