# Python Web Application

This is a simple Python web application developed using Flask that displays the current time in Moscow.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Docker](#docker)
- [Contributing](#contributing)

## Installation

1. Clone the repository:

   > `git clone https://github.com/emapfff/S25-core-course-labs.git`

2. Navigate to the app_python folder:

   > `cd app_python`

3. Create a virtual environment (recommended):

   > `python -m venv venv`

4. Activate the virtual environment:

- On Windows:
  > `venv\Scripts\activate`
- On macOS and Linux:
  > `source venv/bin/activate`

5. Install the required dependencies:
   > `pip install -r requirements.txt`

## Usage

Start the Flask application:

> `python app.py`

Open your web browser and go to http://127.0.0.1:5000/ to view the current time in Moscow. Refresh the page to see the time update.

## Testing

To test the application you should run:

> `python -m unittest test_app`

## Docker

### How to build

Run command

```
docker build -t app_python:latest
```

### How to Pull

You can pull the Docker image from Docker Hub using(current version 1.0.2):

```
docker pull dyllasdek/app_python:1.0.2
```

### How to Run

To run the Docker container, use the following command:

```
docker run -p 5000:5000 app_python:<version_of_container>
```

Make sure you have Docker installed and running on your system before executing these commands.

## Contributing

Contributions are welcome! If you'd like to improve this project or report issues, please open an issue or submit a pull request.
