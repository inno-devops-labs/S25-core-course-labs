# Docker Best Practices

## Security Enhancements
- **Minimal base image**: We use `python:3.11-slim`, reducing attack surface and image size.

## Performance Improvements
- **No-cache pip installs**: The `--no-cache-dir` option prevents unnecessary storage usage.

## Dockerfile Best Practices
- **Work directory setup**: We use `WORKDIR /app` instead of `cd` for better readability and consistency.
- **Port exposure**: Explicitly exposing port `5000` for clarity.

## Running the Container
To build and run the Docker container:

1. **Build the image:**
   ```bash
   docker build -t your-dockerhub-username/app_python .
   ```

2. **Run the container:**
   ```bash
   docker run -p 5000:5000 your-dockerhub-username/app_python
   ```

3. **Push to Docker Hub:**
   ```bash
   docker tag your-dockerhub-username/app_python your-dockerhub-username/app_python:latest
   docker push your-dockerhub-username/app_python:latest
   ```

4. **Pull and run from Docker Hub:**
   ```bash
   docker pull your-dockerhub-username/app_python:latest
   docker run -p 5000:5000 your-dockerhub-username/app_python
   ```

