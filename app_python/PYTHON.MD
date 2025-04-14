# Moscow Time Web App

## Why I chose Flask

I picked Flask for this project because:
- It's super easy to get started with
- Perfect for small projects like this one
- Has everything I need without extra stuff
- Great documentation when I got stuck

## What I did to make the code good

### Best Practices I followed:
- Split the code into separate files (templates, static files, etc.)
- Used proper timezone handling for Moscow time
- Added comments for tricky parts
- Made sure variable names make sense

### Code Standards:
- Followed PEP 8 for Python code style
- Used proper indentation
- Added docstrings for functions
- Kept functions small and focused

### Testing:
- Checked that the time updates correctly
- Tested on different browsers (Chrome, Firefox)
- Made sure it works on phones too
- Verified Moscow timezone is correct

## How I structured everything
```
app_python/
├── static/        # CSS stuff
├── templates/     # HTML pages
├── app.py         # Main code
└── other files    # Config and docs
```

## How I made sure the code is good:
- Double-checked all the timezone logic
- Tested everything myself
- Made the code easy to read
- Kept it simple but effective


## Testing Implementation

Test Cases
---------
1. test_home_status_code: 
   - Verifies that the home page returns HTTP 200 status code
   - Ensures the application is running and accessible

2. test_time_format:
   - Checks if time is displayed in HH:MM:SS format
   - Uses regex pattern \d{2}:\d{2}:\d{2} for validation

3. test_date_format:
   - Verifies date is shown in DD.MM.YYYY format
   - Uses regex pattern \d{2}\.\d{2}\.\d{4} for validation

4. test_moscow_timezone:
   - Confirms the displayed time is in Moscow timezone
   - Allows for ±1 hour tolerance to handle edge cases

Usage
-----
Run tests using:
python -m unittest test_app.py


Requirements
-----------
- Python 3.x
- Flask
- pytz
- unittest