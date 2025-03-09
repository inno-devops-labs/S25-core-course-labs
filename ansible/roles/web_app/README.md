# Role Name

The `web_app` role allows you to deploy Moscow Time web application written in Python on the server.
The application itself runs in Docker container.

## Requirements

- Ansible 2.18.2+
- Python 3.12+
- Ubuntu 24.04

## Role Variables

- `docker_image_name`: The Docker image name to deploy.
- `docker_image_tag`: The tag of Docker image to deploy.
- `docker_app_port`: The port of Docker host that is to be published (default: `80`).
- `docker_container_name`: The name of Docker container. This name will be used when the application will be launched.
- `docker_container_port`: The port of Docker container that is to be published (default: `80`).
- `web_app_full_wipe`: The boolean wipe flag. If it is `true`, all app-related files will be removed (default: `false`).

## Dependencies

- `docker` role. It will install Docker and Docker Compose and their necessary dependencies.

## Example Playbook

```yaml
- hosts: all
  become: true
  name: Deploy Python application
  roles:
    - role: web_app
      vars:
        docker_image_name: dnworks/app_python
        docker_image_tag: latest
        docker_app_port: 80
        docker_container_name: app_python
        docker_container_port: 80
```
