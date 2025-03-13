# Python app

## Task 1

### Chosen framework

I have decided to create this Python application using Flask. According to what I've read, Flask and FastAPI are both lightweight and simple to get started with. It was quicker for me to utilize this framework because I had already used Flask a few years ago. I've also used pytz to properly set the timezone.

## Task 2

### Best Practices

1. **Framework Choice**:
   I chose **Flask** for its simplicity and lightweight nature. Flask is easy to set up and perfect for small projects like this.

2. **Timezone Handling**:
   The application uses the **pytz** library to accurately manage the timezone for Moscow (`Europe/Moscow`). This ensures that the displayed time is always correct.

3. **Code Quality and Testing**:
   - The application follows **PEP 8** coding standards for readability and consistency.
   - The time is generated dynamically, and it is updated each time the page is refreshed.
   - Testing was done manually to verify the functionality by refreshing the browser and using a virtual machine with different timezones to ensure the correct time is displayed.

## Unit tests

Unit tests are essential to ensure that the code behaves as expected. For my Flask application, I have created a unit test to verify the behavior of the `current_time` function, which returns the current time in Moscow.

### Test File Structure

- **File Location:** `app_python/tests/test_main.py`
- **Purpose:** Validate that the `current_time` function returns the correct formatted time string for Moscow.

### **Best Practices Applied**

- Isolate tests into functions to make them reusable and maintainable.
- Use assertions to check for expected outcomes.
- Mock any external API calls or database interactions if necessary.
- The assertEqual method is used to validate that the actual output matches the expected output.
