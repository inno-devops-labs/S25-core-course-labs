## Docker Best Practices:

## Rootless Container
The non-root user `app user` is used.

## Using a minimal image
Using `python:3.11.6-slim`, which reduces the size of the image.

## Optimized `COPY` command
Instead of `COPY . .`coping only the necessary files:
`COPY app.py requirements.txt ./`

## Usage of .dockerignore
Excluding of unnecessary files.

## Disabling the cache when loading dependencies:
`RUN pip install --no-cache-dir -r requirements.txt`