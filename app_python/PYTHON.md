# Justification for Choosing Flask

I chose Flask for this project because it is a lightweight and flexible micro web framework for Python that is perfect for small apps like that one.

# Best Practices Applied in the Web Application

## Coding Standards
- **Flask Framework**: Used for clean, modular code.
- **PEP 8 Compliance**: Descriptive variable names and consistent formatting.
- **Separation of Concerns**: Backend logic isolated from frontend using templates.

## Testing and Verification
- **Manual Testing**:
  - Verified correct time display on page load.
  - Ensured local time updates every second without server requests.
  - Validated Moscow Time accuracy regardless of local machine settings.

## Code Quality
- **Performance**: Handled time updates locally with JavaScript to reduce server load.
- **Reliability**: Used `datetime` and `pytz` for accurate Moscow Time handling.
- **Security**: Debug mode for development only; no sensitive data exposed.
