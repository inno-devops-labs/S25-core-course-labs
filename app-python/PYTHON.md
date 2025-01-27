# Moscow Current Time Web Application

## Framework:

Flask was chosen as a framework for this project as it is simple yet functional and lightweight.

## Best practices:

1. Code matches PEP-8 standard, so it is easily readable.
2. Code has proper naming.
3. Code is well-structured and documented.

## Coding standarts:

Timezone is handled via the pytz library that ensures the proper values for the Moscow.

The current time is passed dynamically to the `index.html` template using Flask's `render_template` function.

## Testing:

Testing was done manually by checking if the time on the page update matches the real Moscow time zone time (which it does).

## Requirements:

- Python 3.9
- Flask
- pytz

## To run the web application on your machine, follow the steps:

1. Clone the repository:

```bash
    git clone https://github.com/mngcndl/S25-core-course-labs
    cd S25-core-course-labs/app-python
```

2. Create virtual environment:

```bash
    python3 -m venv venv
    source venv/bin/activate # for MacOS and Linux
    venv\Scripts\activate # for Windows
```

3. Install dependencies locally using the command

```bash
    pip install -r requirements.txt
```

4. Run the application:

```bash
    python app.py
```

5. Go to your web browser and open the url http://127.0.0.1:5000

## To run the web application on your machine using Docker, follow the steps:

If you already have all the files locally, build the image:

```bash
    docker build -t mangocandle/app_python:latest .
```

OR

1. Pull the image:

```bash
    docker pull mangocandle/app_python:latest .
```

2. Run the image:

```bash
    docker run -p 5000:5000 mangocandle/app_python:latest
```
