# Moscow Time Web Application

![CI Pipeline](https://github.com/tolmachdr/S25-core-course-labs/actions/workflows/go_app_ci.yml/badge.svg?branch=lab3)


This is a Go web application that displays the current time in Moscow.

## Application setup

1. Clone the repo
```
git clone https://github.com/tolmachdr/S25-core-course-labs -b lab1
```
2. Go to the folder and run the app
```aiignore
cd app_go
go run main.go
```


## Docker 

To run this application you also can use docker, for this you need to:

1. Build image
```
docker build -t go-app .
```

2. Run the container
```aiignore
docker run -p 8080:8080 go-app
```

OR

1. Pull existing image from dockerhub
```aiignore
docker pull dtolmach/go-app:latest
```
2. Run the container
```aiignore
docker run -p 8080:8080 go-app
```

## Unit tests

You can test the application using
```aiignore
go test -v
```

## CI

The project uses GitHub Actions for continuous integration. The workflow includes:

1. Installs required Go dependencies

2. `go vet` checks for potential code issues

3. `go test` tests API 

4. `Snyk` detects and reports vulnerabilities

5. Builds and pushes the image to Docker Hub


