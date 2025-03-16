# Web app

## Overview

This role is designed to deploy a web application using a Docker image and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 or compatible Linux distributions
- Docker and Docker Compose

## Role Variables

- `docker_image`: The name of the Docker image to deploy (e.g., `my-flask-app:latest`).
- `app_port`: The port on which the application will be exposed (e.g., `8080`).
- `web_app_full_wipe`: A boolean flag to enable a full wipe of the container and associated files. Defaults to `false`.

## Usage

The role in playbook:

```yaml
- hosts: all
  become: true
  roles:
    - role: ansible/roles/docker
    - role: ansible/roles/web_app
```

