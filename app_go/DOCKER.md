# Docker

## Best practices

1. Use official and minimal base image `golang:1.12-alpine` (this package is the most lightweight, so for this app 
I needed to add time zone database package in container, because alpine does not have it by default)
2. Use multi-stage builds to separate build and runtime environment 
3. `COPY` only necessary files and add unnecessary in `.dockerignore`
4. Install python dependencies without unnecessary cache files 
```RUN pip install --no-cache-dir -r requirements.txt```
5. Run as nonroot user to reduce the risk of privilege escalation 


# Distroless images

Distroless images are very small (we can see the comparison between usual image `go-app`
and with distroless image `go-dist`)

Also, it is more secure because does not contain a shell and run as non-root user by default

![img.png](/attachments/img.png)