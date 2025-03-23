# Python web application 

This is a python web application that shows the current time in Moscow. Flash allows you to quickly create a lightweight web application, JavaScript is used to update the current time every second, HTML and CSS are used to build and style a web application.

## To run web application:

1. Download the repository and navigate to it
```bash
cd app_python
```
2. Install the requirements using requirements.txt file
```bash
pip install -r requirements.txt
```
3. Run web application using flask
```bash
flask --app app run 
```
4. Open the http://127.0.0.1:5000

Now everything is almost ready and you can use the web application.

## Requirements

This web application uses Flask, JavaScript, HTML and CSS (see requirements.txt for details)

## Docker section:

1. To build the application, run
```bash
docker build -t app .
```
2. To pull the application, run
```bash
docker pull denisnesterov/app:latest
```
3. To run the application, run
```bash
docker run -p 8000:8000 denisnesterov/app:latest
```
4. Open the http://0.0.0.0:8000

Now application is running and you can use the web application.

## Unit Tests

There are several unit tests for testing the application. It is located in the `/test` folder and has a structured name `"*_test.py "`. To run the unit tests, run:
```bash
python -m unittest discover tests "*_test.py"
```

## CI

The CI workflow includes the following steps:
1. **Dependencies**: Install Python dependencies
2. **Linter**: Using flake8
3. **Tests**: Run unit tests using unittest python framework
4. **Docker**: Build and push a Docker image to Docker Hub

To see the entire workflow navofate to `.github/workflows/python-app.yml`

## Visits
There is an endpoint `/visits` in my application to see the visits of the home page. To see the number of visits open `http://localhost:8000/visits`. Number of visits stores in visits.txt file. 