# Lab 1
The web application to display moscow time

![CI Workflow](https://github.com/macoyshev/s25-core-course-labs/actions/workflows/app_python.yml/badge.svg)
## Installation
```bash
make install
```

## Launch 
```bash
make run
```

## Run formatters
```bash
make format
```

## Run linters
```bash
make check
make check-dockerfile
```

## Docker
### Build image
```bash
docker build . --target realise_image -t macoyshev/moscow-time
```
### Run container
```bash
docker run --rm --name moscow-time-app -p 8000:8000 macoyshev/moscow-time
```
### Pull image
```bash
docker pull macoyshev/moscow-time
```

### Run tests
```bash
make test
```
 
## Requirenments
- python3.12
