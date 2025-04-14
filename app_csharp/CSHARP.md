# C# Web Application

## Framework Choice: **ASP.NET Core**

- **Justification**:  
  - **Performance**: High-speed, scalable framework for web apps.  
  - **Cross-Platform**: Runs on Windows, Linux, and macOS.  
  - **Built-in Dependency Injection**: Promotes modular, testable code.  

---

## Best Practices Applied

1. **MVC Pattern**:  
   - Separated logic into **Controllers**, **Views**, and shared **Models**.  
2. **Configuration**:  
   - Used `appsettings.json` for environment-specific settings.  
3. **Time Zone Handling**:  
   - Calculated Moscow time as `UTC+3` using `DateTime.UtcNow`.  
4. **Project Structure**:  
   - Followed ASP.NET Core conventions (e.g., `Controllers/`, `Views/`).  
   - Added `.gitignore` to exclude build artifacts (`bin/`, `obj/`).  
5. **Unit Testing**:
   - Used `xUnit` for structured, reliable testing.
   - Employed `Moq` to mock dependencies, ensuring controller logic is testable.
   - Validated the `HomeController` Index method correctly returns Moscow time.
   - **How to Run**:

      ``` bash
      dotnet test
      ```

      This will execute all unit tests and confirm the correct functionality of the application.

---

## Manual Testing

- **Verification Steps**:  
  1. Run `dotnet run` and access `http://localhost:5101` in a browser.  
  2. Confirm the displayed time matches [Moscow’s current time](https://time.is/Moscow).  

---

## How to Run

```bash
dotnet run
```  

Access the app at `http://localhost:5101`.  
