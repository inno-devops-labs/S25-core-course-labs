## Spring Boot Framework
For this exercise, I chose Spring Boot because of its ability to simplify application development with Java. The task doesn’t require overly complex infrastructure, so Spring Boot's modularity and simplicity make it an ideal choice for a small-to-medium-sized project like this one.


---
## Best Practices
- Use Maven for dependency management
- Follow Java coding standards and conventions

---
## Testing
I tested manually

### Unit Tests

#### ✅ Test Cases Implemented

- **test_get_random_quote_html**: Verifies that the `/quotes/random` endpoint returns a successful response with the expected HTML format.
- **test_random_quote_content**: Validates that the response HTML contains a valid quote and author, checking for non-empty values in the `<p><strong>Quote:</strong>` and `<p><strong>Author:</strong>` tags.

#### 🧪 Testing Approach

- Used **JUnit 5** for writing and executing tests in the Spring Boot project.
- Utilized **MockMvc** to simulate HTTP requests and assert responses in the controller.
- Ensured that responses have the correct status code (`200 OK`) and match the expected HTML content.
- Included assertions to verify the structure and content of the returned HTML.
