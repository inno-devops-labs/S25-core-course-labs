# PYTHON.md

## Best Practices Applied

### Coding Standards
- **PEP 8 Compliance**: The application follows Python's PEP 8 standards.
- **Modular Structure**: The code is minimal, readable and maintainable.

### Testing
- **Manual Testing**: The application was tested by running it locally and refreshing the browser to verify time updates.
- **Time Zone Handling**: The `pytz` library was used to provide the correct Moscow time regarding system's local time.

### Code Quality
- **Readability**: The code is well-structured to be readable and understandable.
- **Dependencies**: Only needed dependencies are included in `requirements.txt` for simplicity and efficiency.

### Framework Justification
Flask was chosen for its simplicity and lightweight nature, which perfectly matches the app.
Unlike more complex framework such as Django, Flask ensures fast development without unneeded complexity.
