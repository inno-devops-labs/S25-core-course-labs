# Python Web Application

## Framework Choice:
I have chosen Flask as the web framework for this application, because it is lightweight, easy to set up, 
and ideal for small applications like displaying the current time.

## Best Practices Applied:
- **Code Readability**: Used meaningful function and variable names for clarity.
- **Modular Structure**: Separated route logic from the main app structure.
- **Time Zone Handling**: Used `pytz` to ensure correct Moscow time handling.
- **Security**: Avoided hardcoded configurations and enabled debug mode only in development.
- **Minimal Dependencies**: Kept the `requirements.txt` minimal to avoid unnecessary packages.

## Coding Standards & Quality:
- Followed **PEP 8** coding conventions.
- Used `black` for code formatting.

## Testing:
- Verified time updates by refreshing the page.
- Checked that the time displayed on the web page matches the current time in Moscow.



