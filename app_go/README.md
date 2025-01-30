# URL shortener web app

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
    storage_path: "./storage/storage.db"
    http_server:
        address: "localhost:8080"
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
