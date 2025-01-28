# DOCKER

## Docker Best Practices for JavaScript App

### 1. **Rootless Container**
   - The Dockerfile uses the `nginx:alpine` image, which runs Nginx as a non-root user by default. This minimizes security risks associated with running containers as root.

### 2. **Use COPY, But Only Specific Files**
   - The `COPY` command only copies the necessary application files (`index.html`, `myapp.js`, and `style_comic.css`) to reduce the image size and exclude unnecessary files.

### 3. **Layer Sanity**
   - The Dockerfile avoids unnecessary layers by using a single `COPY` command and minimizing other commands.

### 4. **Use `.dockerignore`**
   - A `.dockerignore` file is included to exclude unnecessary files, such as `.git` directories and `.env` files, from being copied into the Docker image.

### 5. **Precise Version of Base Image**
   - The base image `nginx:alpine` is a stable version of Nginx, ensuring that we get consistent builds and avoid the potential instability of the `latest` tag.

### 6. **Image Size**
   - By using the `nginx:alpine` base image, we ensure a smaller image size, which helps with faster deployment and reduced storage requirements.

## Docker Multi-Stage Builds
I read about Multi-Stage Builds and also tried to implement it for my javascript app. As I understood my app is small and includes an index.html file, styles (style_comic.css) and a JavaScript script (myapp.js), a multi-stage Dockerfile might be unnecessary unless I plan to add more complexity later, like using a build process (e.g., Webpack or Babel). As I'm only serving static files, a simpler Dockerfile would work better for this use case.

