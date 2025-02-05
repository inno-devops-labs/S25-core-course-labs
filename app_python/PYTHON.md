# Python Web Application

## 📌 Justification for Flask

- Flask is lightweight and easy to use for small web applications.
- Supports quick development with minimal setup.
- Provides built-in support for routing, making it ideal for RESTful APIs.

---

## ✅ Best Practices Followed

- **PEP 8 Compliance** → Code follows Python's official style guide.
- **Modular & Reusable Code** → Functions are structured for reusability.
- **Virtual Environment** → Dependencies are managed using `venv`.
- **Unit Testing** → Ensures correctness before deployment.
- **CI/CD Integration** → Automated testing using GitHub Actions.

---

## 🧪 Unit Tests Created

Unit tests were implemented using Python’s built-in `unittest` framework.  
These tests validate the correctness of the Flask web application.

### **📋 Test Cases**

| **Test Name**               | **Description** |
|-----------------------------|----------------|
| `test_homepage_status_code` | Ensures the homepage (`/`) returns HTTP `200 OK`. |
| `test_homepage_content`     | Checks if "Current Time in Moscow" is in the response. |
| `test_homepage_mime_type`   | Confirms the response is `text/html`. |
| `test_invalid_route`        | Ensures a non-existent page returns `404 Not Found`. |

---

## ▶️ Running Unit Tests Locally

To execute all test cases, run:

```bash
python -m unittest discover app_python/tests
```

Expected output:

```bash
....
----------------------------------------------------------------------
Ran 4 tests in X.XXXs

OK
```

---

## 🔄 CI/CD Integration with GitHub Actions

- The workflow (`.github/workflows/python-ci.yml`) **automatically runs these tests** on every push or pull request.
- If a test fails, GitHub Actions prevents deployment.

---

## ✅ Conclusion

These unit tests ensure the Flask app is **stable, reliable, and production-ready**.  
By integrating them into CI/CD, we catch issues **before deployment**.
