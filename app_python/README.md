# Python Web Application: Current Moscow time
### Project Overview
This Python web application is designed to display the current time in Moscow, dynamically updating the time on each page refresh. The application is built using the **FastAPI** framework, ensuring high performance, developer-friendly design, and adherence to modern coding standards.

### Technologies used
- **FastAPI:** developer-friendly web framework which ensures safe and effective app programming
- **pytz:** Python library for precise time zone handling, ensuring accurate conversion and retrieval of the current time in Moscow (or any other timezone).

### Features
1. **Dynamic Time Updates:**
The application displays the current Moscow time, refreshing dynamically on each page reload.
2. **Modular Design:**
The logic for fetching the Moscow time is encapsulated in a separate function, promoting reusability and readability.
3. **Error Handling:**
The application gracefully handles unexpected errors using a ```try-except``` block, ensuring reliability in various scenarios.

### Installation and Usage
Clone the repository:
```bash
git clone https://github.com/Pupolina7/S25-core-course-labs.git
```
Navigate to the folder:
```bash
cd S25-core-course-labs/
```
Create virtual environment:

commands for MacOS
```bash
python -m venv env
source env/bin/activate
```
Install necessary dependencies:
```bash
pip install -r requirements.txt
```
Navigate to the ```app_python``` folder:
```bash
cd app_python/
```
Run the application locally:
```bash
uvicorn app:app --reload
```
Go to localhost:
```bash
http://127.0.0.1:8000
```
