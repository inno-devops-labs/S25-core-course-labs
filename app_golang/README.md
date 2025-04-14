# Devops golang time API

## Overview

### Implementation technologies:

1) `Golang` - programming language
2) `Gin` - framework for API development

### App structure:

```
app_golang/       # application
    - main.go     # program code and entrypoint
```

## Launch

### Install requirements and build binary

```bash
cd app_golang
```

```bash
go install
```

```bash
go build
```

### Run

```bash
./app_golang
```

Then you can reach API endpoint at http://localhost:8080/time

## Docker

### Build

```bash
docker build -t wensiet/devops-go-app:latest .
```

### Pull

```bash
docker pull wensiet/devops-go-app:latest
```

### Run

```bash
docker run -p 8000:8000 wensiet/devops-go-app:latest
```
