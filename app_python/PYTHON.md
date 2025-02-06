# Python Web Application Documentation

## Chosen Framework: Flask

I chose [Flask](https://flask.palletsprojects.com/en/stable/) because:

- it is beginner-friendly and great for small projects like this one
- it has a flexible structure, so I can customize the code as needed
- easy and clear documentation for quick start

---

## Best Practices

1. **PEP 8 Compliance**  
   - All code follows PEP 8 style guidelines to ensure readability and consistency. flake8 can verify style adherence.

2. **requirements.txt**
   - All dependencies are described in requirements.txt file in root of the project so they could be all easely installed using pip.

3. **Logging**
   - Basic logging is set up using Python’s logging module to track activities within the application.

4. **Modular Structure**  
   - While this is a straightforward app, the code is structured to allow for future scaling.
   - If needed, additional modules for configuration, utilities, or routes could be added.

---

## Testing

- Run tests:

```pytest```

These tests check that the home page ("/") responds correctly, displays the proper content, and formats the time as expected.

### Home Status Code Test

- Accesses the home page.
- Verifies the response status code is 200.

### Home Time Update Test

- Mocks the current datetime to a fixed Moscow time (2023-01-01 12:00:00).
- Checks that this fixed time appears in the response.

### Home Content Test

- Retrieves the home page and decodes its HTML.
- Confirms it contains the text "Current Time in Moscow" and a ```<p>``` tag.

### Time Format Test

- Searches the HTML for a datetime string matching the "YYYY-MM-DD HH:MM:SS" pattern.
- Ensures the time string is correctly formatted.

---
