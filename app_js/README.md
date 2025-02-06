# CryptoClicker web app

## Overview

**Svelte** based web app that is useful for people with ADHD to get distracted.

Features dynamic and random generated UI.

## Notes

>This is the rebuild on Svelte of the game part of [this project](https://github.com/absorian/cryptoclicker), which was written in pure JS.

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
docker pull absorian/s25-devops-cryptoclicker
```

You can run the container specifying ports and env file with at least host and port defined

```bash
docker run --env-file .env -p 8000:8000 absorian/s25-devops-cryptoclicker
```
