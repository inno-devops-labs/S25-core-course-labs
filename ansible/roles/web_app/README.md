# Web App Role

This role deploys a web application using Docker and Docker Compose.

## Requirements

- Docker must be installed and running on the target host.
- Docker Compose must be available.
- The `docker` role is a dependency and will be executed prior to this role.

## Role Variables

- `docker_image` (default: "mydockerhubusername/myapp:latest"): The Docker image for the application.
- `app_port` (default: 8080): The port on the host mapped to container port 80.
- `web_app_full_wipe` (default: false): Set to true to perform a complete removal of the deployed application (container and files).

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - docker
    - web_app
