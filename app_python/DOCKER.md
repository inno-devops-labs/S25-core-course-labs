# Best Practices Implemented

1. Using a Specific Base Image Version / Using a Minimal Image (Alpine)
   
   ``FROM python:3.12.8-alpine3.21@sha256:ba13ef990f6e5d13014e9e8d04c02a8fdb0fe53d6dccf6e19147f316e6cc3a84``
2. Running as a Non-Root User
   
   ``
   RUN addgroup -S appgroup && adduser -S appuser -G appgroup
   ``
   
   ``USER appuser``
3. Using Multi-Stage Dependency Installation 
   ```dockerfile
    RUN apk add --no-cache --virtual .build-deps \
        gcc=14.2.0-r4 \
        musl-dev=1.2.5-r8 \
        libffi-dev=3.4.6-r0 && \
        pip install --no-cache-dir --upgrade pip==25.0 && \
        pip install --no-cache-dir -r requirements.txt && \
        apk del .build-deps
    ```
4. Avoiding Cache in pip Install

    ``pip install --no-cache-dir -r requirements.txt``

5. Exposing Only the Required Port

   ``EXPOSE 5000``