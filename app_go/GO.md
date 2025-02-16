# Go Web Application

## 🧩 Framework Choice

I have decided to use [Gin](https://github.com/gin-gonic/gin) framework.

Firstly, it is very easy to create a simple web application.  
Secondly, it is similar to FastAPI in Python.  
Thirdly, it is a popular framework and it is relatively lightweight.  
Fourthly, I think it is suitable for this application.

## 🧪 Testing

### Manual

Manual testing was performed by opening the webpage and comparing the calculated ages with real ages of myself and other people.

### Automated

Automated tests are performed using built-in `testing` package together with the `net/http/httptest` library to simulate HTTP requests.

Currently, there are several tests that check the responses of my endpoints:

- RenderIndex handler:
  - Whether the response status code is correct;
  - Whether the response content type is html;
- CalculateAge handler:
  - Whether the response status code is correct;
  - Whether the response body contains the expected JSON;
  - Whether correct error messages are returned;
- CalculateAge service:
  - Whether the age is calculated correctly;
  - Whether correct error messages are returned;

## ✅ Best Practices

- Code modularity that will ease the future development.
- Using popular [project layout](https://github.com/golang-standards/project-layout).
- `gofumpt` formatter with some strict formatting rules was used.
- `golangci-lint` linter was used to ensure the absense of stupid errors.
- Using Makefile to structure the different stages of development.
- `markdownlint` was used to check the Markdown files.
- Each test is independent and does not rely on results of other tests;
- Mocking API using `net/http/httptest`;
- High coverage of the tests;
- Using specific assertions to validate expected outcomes;
- Using built-in testing framework `testing`;
