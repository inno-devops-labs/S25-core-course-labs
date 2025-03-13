# Docker

## Best practices

1. Use official and precise base image `python:3.12-slim`
2. `COPY` only necessary files and add unnecessary in `.dockerignore`
3. Install python dependencies without unnecessary cache files 
```RUN pip install --no-cache-dir -r requirements.txt```
4. Run as nonroot user to reduce the risk of privilege escalation