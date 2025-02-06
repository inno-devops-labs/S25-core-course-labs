# Code Quality and Best Practices

---

### Precise Base Image
Using ```python:3.9-slim``` ensures consistency and minimizes vulnerabilities compared to the ```latest``` tag.

---

### Nonroot User
Container runs with ```nonroot```, leave privilege for better security.

---

### Minimal Base Image
Using ```slim``` reduces unnecessary layers and memory size.

---
### .dockerignore
```.dockerignore``` file ensures to exclude unnecessary files.

---
