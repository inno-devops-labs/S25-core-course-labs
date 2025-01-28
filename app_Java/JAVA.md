# Java Web Application

## Framework Choice
**I selected the Spark Framework for this project due to the following reasons:**
1. It allows for rapid prototyping without the need for complex configurations.
2. With no additional dependencies or heavy abstractions, it focuses on serving HTTP requests efficiently.
3. Spark has excellent documentation, making it beginner-friendly and accessible for developers.

## Best Practices Applied
1. **Coding Standards:**
   - Followed **Java naming conventions** for classes, variables, and methods to maintain readability and consistency.
   - Used descriptive variable names (e.g., omskTime and formattedTime) to make the code self-explanatory.
   - Kept the code modular by limiting the logic to a single route handler.
  
2. **Code Quality and Testing:**
   - Added comments to clarify important parts of the code, such as timezone configuration and response formatting.
   - Ensured consistent indentation and spacing to enhance code readability.
   - Tested the application locally to verify that:
       1. The current time in Omsk updates dynamically when the page is refreshed.
       2. The displayed time format matches YYYY-MM-DD HH:MM:SS.
       3. The server runs smoothly on the default Spark port (4567).
    
3. **Timezone Management**
   - Utilized Java's **ZoneId** and **ZonedDateTime** classes to ensure accurate and reliable timezone handling for Omsk.
   - Ensured the application dynamically retrieves the current time for the Omsk timezone (Asia/Omsk), keeping it accurate even if the timezone rules change in the future.
