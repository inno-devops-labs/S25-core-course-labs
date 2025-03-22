# Docker best practices used (Updated for bonus)

1. **Use a distroless image**: minimizes image size and attack surface.
2. **Use a multi-stage build**: Separates build and runtime environments, reducing final image size by excluding build tools from production.
3. **Clean up unnecessary files**: apt-get clean && rm -rf /var/lib/apt/lists/\* reduces the final image size.
4. **Pin package versions**: Specifying exact versions ensures consistent builds across environments.
5. **Set a non-root user**: enhances security by avoiding the use of root in the runtime environment.
6. **Use explicit entrypoint**: ENTRYPOINT ensures the container runs the application (uvicorn) on startup with specific arguments.

## Distroless and Alpine images difference

Distroless images are different from Alpine images because they are much more minimal. They only include the application and its dependencies, without extra tools like package managers or shells. This makes Distroless images smaller and safer because there are fewer things that could be used for attacks. Even though sometimes the size of Alpine and Distroless can be similar, Distroless is still better for security because it doesn't have any extra parts that aren't needed for the app to run.

### Python App

![Python Screenshot](http://postimg.su/0ziWgU9X)

### JS App

![Js Screenshot](http://postimg.su/rypLNoLW)
