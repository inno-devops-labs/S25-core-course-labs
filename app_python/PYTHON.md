## Framework: Flask
- **Lightweight**: Minimal setup for a simple app
- **Flexible**: Easy to extend and modify
- **Built-in Server**: No need for additional tools to run locally

## Best Practices
1. **Timezone Handling**  
   Used `pytz` for accurate timezone conversion to Moscow (MSK).

2. **Code Quality**  
   - Followed PEP8 standards  
   - Used descriptive variable names  

3. **Security**  
   - Enabled debug mode only for development  
   - Used Flask's built-in HTML escaping  

4. **Maintainability**  
   - Added `requirements.txt` for dependency management  
   - Included a `.gitignore` file  
