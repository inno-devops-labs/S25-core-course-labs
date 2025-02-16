# Best Docker Practices
## Choose the right base image
``gcr.io/distroless/python3-debian12:nonroot`` is an image from a trusted source that has all the necessary elements, but nothing else.
## Pin base image versions
``python:alpine3.21@sha256:f9d772b2b40910ee8de2ac2b15ff740b5f26b37fc811f6ada28fce71a2542b0e`` 
was used precisely for this purpose.
## Exclude with .dockerignore
You may see, I have a .dockerignore file that excludes all unnecessary files.
## Don't install unnecessary packages
I do not add any unnecessary system packages and only download the python packages that are mandatory for the application.
## Leverage build cache and Dockerfile instructions
I have separated the steps of my build to: 
1. Change the working directory
2. `COPY` the templates and the necessary application file
3. `COPY` the requirements and install them
4. `EXPOSE` the port
5. Add and change to a different User
6. `CMD` the application
## Create ephemeral containers
My container is easily rebuild, I tried it when testing.

# Additional:
## Create reusable stages
Not needed in this project
## Rebuild your images often
I do, but I can not prove, can I?
## Decouple applications
Nothing to decouple
## Sort multi-line arguments
There is no sorting
## Build and test your images in CI
I believe I will get to do that in the future labs