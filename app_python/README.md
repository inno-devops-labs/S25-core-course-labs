![Python app](https://github.com/dew1769/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)

# Python Application to display Moscow time

## Description
- **This application displays the current time in Moscow using Flask to run the app and pytz to get the appropriate 
timezone**
## Features
- Get the real time in Moscow by refreshing the page

## Getting started
### Prerequisites
- [Download the python 3.8+](https://www.python.org/downloads/)
- [Install pip](https://pip.pypa.io/en/stable/cli/pip_install/)
- [Install Docker](https://www.docker.com/get-started/)

### Local installation
1. Clone the repository:
     ```bash
    git clone https://github.com/dew1769/S25-core-course-labs.git
     cd app_python
    ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
    ```bash
   python app.py
   ```
   
## Docker Instruction
- **Here are steps to run the docker image locally and from docker hub**
### First steps
1. Build the image:
   ```sh
   docker build -t msc .

2. Run the container locally:
   ```sh
   docker run -p 5000:5000 msc

### Run image using Docker Hub
**Notice**: to use these commands, change my name `dew1769` to your username on Docker Hub
1. Login to Docker hub
   ```sh
   docker login
   
2. Tag the image
   ```sh
   docker tag msc dew1769/application-real-time:v1

3. Push the image
   ```sh
   docker push dew1769/application-real-time:v1

4. Pull and Run the image
   ```sh
   docker pull dew1769/application-real-time:v1
   docker run -p 5000:5000 dew1769/application-real-time:v1

## Counter

The updated file `app.py` now contains counter, we can run it using these commands:
   ```sh
   docker-compose build
   docker-compose up

## Unit Tests
The file 'test_cases.py' contains simple unit tests to check the correctness:
1. Page loading with HTTP code 200
2. Containing text about the time
3. The page displays the time

- Local usage (use the following command): `pytest app_python/test_cases.py`

## CI workflow
Git hub Actions (`.github/workflows/ci.yml`):

- Security check using `synk`
- Set up Python and dependencies
- Unit tests
- Docker Build & Push

## Usage
**After the application has been launched locally or with the use of Docker, open your browser and enter the address in
the search bar and test the application: 
`http://127.0.0.1:5000/`**

## Acknowledgments
- Flask documentation
- pytz
- Docker
- synk
- Github Actions