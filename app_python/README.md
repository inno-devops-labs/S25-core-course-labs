# app_python

This web application displays current time in Moscow

## Running

- Install dependencies

```console
pip install -r requirements.txt
```

- Run the server

```console
uvicorn main:app
```

- The server's address will be `http://127.0.0.1:8000`

## Docker

### Building The Image

```console
docker build -t 2imt/app_python:1.2 .
```

### Pulling The Image

```console
docker pull 2imt/app_python:1.2
```

### Running The Image

```console
docker run --rm -p 8000:8000 2imt/app_python:1.2
```
