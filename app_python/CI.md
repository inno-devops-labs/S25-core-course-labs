# 🛠️ Continuous Integration (CI) Best Practices

This document outlines the best practices implemented in the **CI/CD pipeline** for the Moscow Time Web Application.

---

## 🚀 Implemented Best Practices

The CI/CD pipeline is designed to enhance **automation, reliability, and security**. It ensures that every change is **tested, linted, scanned for vulnerabilities, and deployed efficiently**.

---

## 🎯 Triggering CI/CD Only on Relevant Changes

The workflow is triggered only when files inside app_python/ change.
This prevents unnecessary CI/CD runs when other parts of the repository are updated.
```yaml
on:
    push:
        paths:
          - 'app_python/**'
          - '.github/workflows/app_python_ci.yml'
    pull_request:
        paths:
          - 'app_python/**'
          - '.github/workflows/app_python_ci.yml'
```

### **✅ Benefits**
- **Optimized CI/CD execution** → Only runs when Python-related files are modified.
- **Faster feedback loop** → Ensures CI/CD resources are used efficiently.

---

## ⚡ Dependency and Docker Caching

### ✅ Python Dependency Caching
To speed up package installations, the pipeline caches Python dependencies.
```yaml
name: Set Up Python
uses: actions/setup-python@v4
with:
    python-version: '3.11'
    cache: 'pip'
```
### **✅ Benefits**
- **Faster builds** → Dependencies do not need to be downloaded on every run.
- **Less network usage** → Reduces bandwidth and speeds up workflow execution.

### ✅ Docker Layer Caching
Docker caching is used to reuse previous **build layers**, reducing the time required for rebuilding images.
```yaml
name: Build and Push Docker Image
run: |
    docker build --cache-from=azazaki/app_python:latest -t azazaki/app_python:latest ./app_python
    docker push azazaki/app_python:latest
```

### **✅ Benefits**
- **Speeds up** builds by reusing unchanged layers.
- **Reduces** redundant computation and optimizes deployment.

---

## 🔍 Static Code Analysis with Flake8
The CI/CD pipeline runs flake8 to enforce PEP 8 coding standards.

```yaml
name: Run Linter (flake8)
working-directory: app_python
run: |
    pip install flake8
    flake8 app.py test_app.py --max-line-length=120
```

### **✅ Benefits**
- **Ensures** consistent code style across the project.
- **Prevents** syntax errors before merging changes.

---

## 🧪 Automated Unit Testing

Unit tests are executed using **pytest** to validate application functionality.
```yaml
name: Run Unit Tests
working-directory: app_python
run: |
    pytest test_app.py
```

### **What’s Tested?**

- **Server Status Code** → Ensures the homepage loads successfully (200 OK).
- **Correct Moscow Time Format** → Validates the response format.

### **✅ Benefits**
- **Prevents broken code from being merged.**
- **Ensures** application correctness before deployment.

---

## 🛡️ Security Scanning with Snyk

Snyk is integrated into the CI/CD pipeline to **scan for vulnerabilities**.
```yaml
name: Run Snyk to check for vulnerabilities
uses: snyk/actions/python@master
env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
with:
    args: --skip-unresolved --severity-threshold=high
```

### **✅ Benefits**

- **Detects security vulnerabilities** in Python dependencies.
- **Prevents insecure code** from being deployed.

---

## 🔄 Future Enhancements

- **Automate test coverage reporting** for better visibility.
- **Improve parallel execution** to further reduce build times.
- **Expand security checks** to scan the Docker image for vulnerabilities.

### 🚀 With these optimizations, CI/CD pipeline is faster, more secure, and highly efficient!