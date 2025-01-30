# Python Web Application Description

## Framework Choice: Flask

**Justification:**

- **Lightweight & Minimalistic**: Ideal for small applications like a time display service
- **Template Support**: Built-in Jinja2 templating engine for HTML rendering
- **API Support**: Native JSON response handling via `jsonify`

## Best Practices Implementation

### 1. Code Organization

- Separation of concerns (routes, business logic, templates)
- Configuration constants (`START_HOST`, `START_PORT`) at module level
- Dedicated time calculation function (`get_current_time`)

### 2. Coding Standards

- PEP8 compliance
- Type hints for function signatures
- Descriptive variable names
- 79-character line length limit

### 3. Testing Strategy

1. **Manual Testing**:
    - Timezone validation (MSK vs UTC)
    - Auto-refresh functionality check
    - Cross-browser compatibility

2. **Automated Checks**:
   ```bash
   flake8 app.py
   mypy app.py
   black --check app.py
   ```
   
### 4. Architecture
```
app_python/
├── .gitignore
├── app.py
├── templates/
├── static/
├── requirements.txt
├── PYTHON.md
└── README.md
```
