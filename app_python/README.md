# MSK Time Web App

## Overview

**FastApi** based web app that shows current time in Moscow upon reload.

Features Trump's face and a clean UI.

## Docker

### Building and Running

To build and run the container

- Configure `.env` file
  - Define host and port
    - Switch `DEV` to enable hot reload
    - For fresh builds and containers every time enable `DOCKER_UNSAVE`
- Run `./run.sh`

### Pulling

To pull the latest image

```bash
docker pull absorian/s25-devops-msk-time
```

You can run the container specifying ports and env file with at least host and port defined

```bash
docker run --env-file .env -p 8000:8000 absorian/s25-devops-msk-time
```
