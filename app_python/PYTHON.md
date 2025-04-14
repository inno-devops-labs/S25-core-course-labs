# Python Web Application

## 🧩 Framework Choice

I have decided to use [FastAPI](https://fastapi.tiangolo.com/) framework.

Firstly, I have a lot of experience in it, so writing this application was very quick.  
Secondly, it is a popular framework and it is relatively lightweight.  
Thirdly, I think it is suitable for this application.

## 🧪 Testing

### Manual

Manual testing was performed by opening the webpage and comparing the showed time with the time on my devices.

### Automated

Automated tests are performed using `pytest` together with `FastAPI.TestClient` to simulate HTTP requests.

Currently, there is only one test that checks the response of my single endpoint:

- Correctness of the status code of response;
- Whether the response is HTML content;
- Whether the time information is present in response;
- Whether the time in response is correct (also, accounting some network delays);

Currently, test coverage is 100%:

```text
---------- coverage: platform win32, python 3.11.5-final-0 -----------
Name              Stmts   Miss  Cover
-------------------------------------
src\__init__.py       0      0   100%
src\config.py         7      0   100%
src\main.py           7      0   100%
src\routes.py        13      0   100%
-------------------------------------
TOTAL                27      0   100%
```

## ✅ Best Practices

- Code modularity that will ease the future development;
- `black` and `isort` formatters were used to format the Python code according to PEP 8;
- `pylint` linter and `mypy` static type checker were used to ensure the absense of stupid errors;
- Separated production and development requirements.txt files;
- Using Makefile to structure the different stages of development;
- `markdownlint` was used to check the Markdown files;
- Each test is independent and does not rely on results of other tests;
- Mocking API using `FastAPI.TestClient`;
- High coverage of the tests;
- Using specific assertions to validate expected outcomes;
- Using popular testing framework `pytest`;
