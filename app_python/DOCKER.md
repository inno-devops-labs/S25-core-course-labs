## best practices

1. **Minimal base image**: ised minimal python version to reduse size
2. **Non-root user**: created appuser to run the container securely
3. **Installed dependencies**
4. **Used --no-cache-dir** to avoid unnecessary cache storage
5. **Used .dockerignore** 
6. **Exposed only necessary port 5000**

## running the container

docker pull meowal/msk-time-app:latest

docker run -p 5000:5000 meowal/msk-time-app:latest
