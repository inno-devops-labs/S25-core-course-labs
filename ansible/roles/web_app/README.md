# Web App Role

This role installs Docker, pulls the specified Docker image, and deploys it using Docker Compose.

## Requirements
- Ansible 2.9+
- Ubuntu 20.04+
- Docker installed

## Role Variables
- `docker_image`: Docker image to be used (default: `vika123vika/app_python:latest`)
- `app_port`: Port for the application (default: `8080`)
- `web_app_full_wipe`: Boolean to enable/disable the wipe task (default: `false`)

## Example Usage
```yaml
- hosts: all
  roles:
    - role: web_app
      become: true
```
