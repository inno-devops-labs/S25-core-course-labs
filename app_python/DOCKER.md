## Best practices

1. **Using a precise version of the base image and language**:
- Using a specific version of the base image provides stability and reduces the risk of issues.

2. **Create a non-root user and set permissions**:
- Running the app as a non-root user improves security by limiting privileges.

3. **Layer Sanity**
- Minimizing image layers reduces build time and image size.

4. **Use .dockerignore**
- Including a .dockerignore file reduces the image size.

5. **Copy only necessary files**:
- Coping only the necessary files to minimize the image size and avoid including sensitive files.