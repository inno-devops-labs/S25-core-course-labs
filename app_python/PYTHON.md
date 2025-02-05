## <ins>Which framework has been chosen</ins> 
*Django was chosen for this task because of its simplicity, well-organized structure, and ability to support rapid development, such as displaying the current time. Furthermore, its scalability ensures it can accommodate future enhancements seamlessly.*

## <ins>How the Time is displayed</ins>
*The app uses JavaScript's Date object in combination with the toLocaleString method and the timeZone option set to Europe/Moscow to ensure accurate timezone conversion for Moscow, it dynamically display the time*

## <ins>Testing</ins>
*It was tested manually by refreshing the page in order to check whether it still working and displaying correct time*

## <ins>Best practices, coding standards and code quality</ins>
*To ensure clean and maintainable code, issues like trailing whitespace and overly long lines were avoided. Proper naming conventions were followed, and PEP 8 guidelines were adhered to throughout.  <br>
Additionally, tools like flake8 and black were used to help maintain and enforce these coding standards and code quality.*

## Unit testing 
In the file ```test_views.py``` the following tests were considered: <br>
 - Valid page loads - ```test_home_page_status_code()``` and ``` test_home_page_template_used```
 - Valid title page contains - ```test_title_contains```
 - Invalid URLs return `404`.  ```test_return_404_for_invalid_url```
 - JavaScript dynamically updates content - ```test_page_shows_current_time```
#### <ins>Best Practices were applied</ins> <br>
- Used ```SimpleTestCase``` because of no database was required
- Used ```reverse()``` it makes to avoid hardcoding and make tests more maintainable 
- Ensures that the correct HTML template is rendered.
- Each test checks only one specific behavior
- Test method names clearly indicate what is being tested.
- Test Edge Cases

#### Test Coverage: 
```text
Name                    Stmts   Miss  Cover
-------------------------------------------
display_time/urls.py        3      0   100%
display_time/views.py       3      0   100%
-------------------------------------------
TOTAL                       6      0   100%
```