![Tests](https://github.com/dpttk/S25-core-course-labs/actions/workflows/tests.yml/badge.svg)
![Lint](https://github.com/dpttk/S25-core-course-labs/actions/workflows/linter.yml/badge.svg)
![Docker](https://github.com/dpttk/S25-core-course-labs/actions/workflows/docker.yml/badge.svg)
# Moscow time
Simple web application that shows current Moscow time and tracks visit counts

## Features

- Displays the current Moscow time
- Tracks and displays the number of visits to the site
- Provides a dedicated `/visits` endpoint to view the visit counter
- Persists visit count data using a volume mount

## How to run with Python

1. Install python3 
2. Clone this repo
3. Install all dependencies
4. Run the app 
5. You can check and see that it is now running on localhost:5000

```
git clone https://github.com/dpttk/S25-core-course-labs.git
cd app_python
pip install -r requirements.txt
python run.py
```

## How to run with Docker Compose

1. Clone this repo
2. Navigate to the app_python directory
3. Start the application with Docker Compose

```
git clone https://github.com/dpttk/S25-core-course-labs.git
cd app_python
docker-compose up -d
```

The application will be accessible at http://localhost:5000

### Persistence

The visit counter is stored in a file that persists between container restarts. The Docker Compose configuration includes a volume mount:

```
volumes:
  - ./data:/data
```

This maps the local `./data` directory to the `/data` directory in the container, where the visit count is stored in a file named `visits`.

## docker 
This application is containerized using Docker. Below are instructions for building, pulling, and running the Docker image.

### How to Build
`docker build -t iu-devops-lab2 .`
### How to Pull
`docker pull dpttk/iu-devops-lab2:latest`
### How to Run 
`docker run -p 5000:5000 dpttk/iu-devops-lab2:latest`
or if builded localy
`docker run -p 5000:5000 iu-devops-lab2`

## Unit Tests

Application does have unit tests. They are automatically running on pull requests by CI.

To run them manually type `python -m unittest discover tests`

## CI

Application does have unit tests ci pipelines. 

test.yml - runs unit tests on application 
linter.yml - validates code style quality
docker.yml - update docker build of the application
synk.yml - vulnurabilities check