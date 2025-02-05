# Python web-application

### Run application with the command
```python
python3 app.py
```

### Install dependencies
```bash
pip install -r requirements.txt
```

This application uses `Flask` as the framework.

### Project structure
```
app_python/
│
├── app.py
├── static/
    └── index.css
├── templates/
│   └── home.html
```

Using this web-application, you can check current time in Moscow.

# Docker

### Building the Docker image
```
docker build -t python-msk-time .
```

### Run the container
```
docker run -p 5000:5000 python-msk-time
```

### Pull from Docker Hub
```
docker pull nickolaus899/python-msk-time:latest
```

#### For the distroless one:
```
docker build -t py-distroless -f distroless.Dockerfile .

docker run -p 5000:5000 py-distroless

docker pull nickolaus899/py-distroless:latest
```


#### Working directory: `/app`

### Verification and manual testing
Manualy tested the container and pulling for the DockerHub.

## Unit tests
Firstly, you will need `flask-testing`
```
pip install flask-testing
```

Then, you can run tests with a command (in the folder `app_python`)
```
python3 -m unittest discover tests
```


# CI/CD
GitHub Actions were added to the project. I use `py.yml` for automated
actions. 

### Workflow:
1. **Dependencies:**: install from `requirements.txt`
2. **Linter:**: check code quality using `flake8`
3. **Tests:**: run unit tests with `pytest`
4. **Docker:**: build and push a Docker image to DockerHub

### Workflow Budge
[![Python CI with Docker](https://github.com/Nickolaus-899/S25-core-course-labs/actions/workflows/py.yml/badge.svg)](https://github.com/Nickolaus-899/S25-core-course-labs/actions/workflows/py.yml)
