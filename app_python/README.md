# Python Web Application

This is a simple Python web application built using the Flask framework. It displays the current time in Moscow and updates it locally on the client side without making repeated server requests.

## Features
- Displays Moscow Time accurately.
- Local time updates every second using JavaScript.
- Lightweight and efficient, with minimal server-side logic.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd app_python
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## File Structure
- **app.py**: Main application file containing the Flask routes.
- **templates/**: Contains the HTML templates for the application.
- **static/**: Includes static assets like CSS and JavaScript files.

## How It Works
- The server fetches Moscow Time using Python's `datetime` and `pytz` libraries.
- The initial time is rendered into the HTML template.
- JavaScript updates the time locally every second to ensure smooth performance.

## Testing
- Verified that the time is correct on page load.
- Ensured the time updates locally without additional server requests.
- Tested with altered local system time to validate Moscow Time accuracy.

## Best Practices
- Follows PEP 8 coding standards for readability.
- Implements clean separation of concerns with templates and backend logic.
- Optimized for performance by reducing redundant server requests.


