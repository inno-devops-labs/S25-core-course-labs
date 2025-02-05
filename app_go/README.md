# URL shortener web app

[![url-shortener](https://github.com/justcgh9/S25-core-course-labs/actions/workflows/go.yaml/badge.svg)](https://github.com/justcgh9/S25-core-course-labs/actions/workflows/go.yaml)

This is an url shortener developed with golang and htmx

## Features

- Add an alias for an URL
- Get a page by its alias
- Delete unneeded alias

## Requirements

- Go 1.23

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/justcgh9/S25-core-course-labs.git
    cd S25-core-course-labs/app_go
    ```

2. Install the dependencies:

    ```bash
    go mod tidy
    ```

## Usage

1. Create a config file, and add it to .env:

    ```bash
    mkdir config
    touch config/local.yaml
    ```

    Example config:

    ```yaml
    env: "local"
    storage_path: "./storage.db"
    http_server:
        address: "0.0.0.0:8080"
        timeout: 4s
        iddle_timeout: 60s
    ```

    Now add it to .env

    ```bash
    echo CONFIG_PATH=config/local.yaml > .env
    ```

2. Make sure that your storage directory exists:

    ```bash
    mkdir storage
    ```

3. Build the project:

    ```bash
    go build ./cmd/url-shortener
    ```

4. Run the binary:

    ```bash
    ./url-shortener
    ```

## Endpoints

Now your service must be up on the port you specified (by default :8080), here is some information about endpoints

- GET /manage - will return an html resource for easily adding, going to, or removing the urls

- GET /urls/{alias} - Get a URL by alias. Alias is a string parameter - a short name to look up a url for. Returns a json with status and url found, or an error with corresponding status code.

- POST /urls - Create an alias for an url. Takes a form-data body: url - required string, a url that you are willing to create an alias for, alias - optional string, the desired alias. It will return a piece of html that will be added to the list of urls on the management page

- DELETE /urls?alias= - Delete a url by alias. Returns OK on success, an error otherwise.

## **Docker**  

This application can be containerized using Docker. Below are the instructions to build, pull, and run the container.  

### **How to build?**  

If you decide to build on your own, checkout your database path in config, if there are directories that are not created in a Dockerfile, add a dedicated build step, or in the logs you will see that sqlite could not find the path (its not necessary to create .db file, just all the directories). If I didn't really care, I would have just pulled the image.

```sh
docker build --build-arg config_path=./config/local.yaml -t justcgh/url-shortener .
```

### **How to pull?**  

```sh
docker pull justcgh/url-shortener:latest
```

### **How to run?**  

```sh
docker run -p 8080:8080 justcgh/url-shortener
```

## **Distroless Image Version**  

A Distroless-based image is also available for enhanced security and minimal footprint.

### **How to build the Distroless Image?**  

There are also db issues here. SQLite needs an access to the filesystem to operate correctly, which is available only for /tmp folder (I spent quite a lot of time to find that out) . That's why I would recommend to put something like /tmp/storage.db to your config as db path.

```sh
docker build --build-arg config_path=./config/local.yaml -t url-shortener-distroless -f distroless.Dockerfile .
```

### **How to pull the Distroless Container?**

```sh
docker pull justsgh/url-shortener-distroless
```

### **How to run the Distroless Container?**  

```sh
docker run -p 8080:8080 url-shortener-distroless
```

## Unit Testing Summary

I implemented unit tests for both the HTTP handlers and the SQLite storage layer. You can see a little bit of information below. However, if you need more of it, I tried to document the tests pretty heavily, so you might look at the source files.

- **HTTP Handlers:**  
  - Tested the *Save*, *Read*, and *Delete* handlers using table-driven tests.
  - Covered both success and error scenarios (e.g., validation errors, duplicate entries, not found).
  - Used mocks to isolate handler logic from external dependencies.

- **SQLite Storage:**  
  - Verified CRUD operations (save, retrieve, list, delete) using an in-memory database.
  - Ensured proper error handling for duplicate entries and not-found cases.

This approach promotes clarity and maintainability by isolating functionality and covering edge cases. To run all tests, use:

```bash
go test -v ./...
```
