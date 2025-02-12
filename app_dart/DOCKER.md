# Docker Image Description

* Image can be found [here](https://hub.docker.com/repository/docker/paranid5/app_flutter/general)

## Best practices

### Dockerignore & only necessary files

`.dockerignore` is used to remove all files
that are not required to build and deploy application.

Application is compiled on release AOT mode which significantly
improves the performance and reduces the size of the app
(comparing with JIT compilation in debug mode).

Release mode helps to compile Dart code directly into .js files and use web canvas directly,
avoiding setup of DartVM in debug mode ([More details about Flutter compilation (RUS)](https://habr.com/ru/articles/662135/#3))

Additionally, **COPY** is used in `Dockerfile`
only for necessary files and folders.

### Non-root user

In order to minimize potential attack risks during the image execution,
`Dockerfile` contains command to create user with limited permissions.

### Multistage build

Multistage build is performed in order to inject compiled code
for the web platform directly to nginx web server.
