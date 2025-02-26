# Moscow Time App

A simple application for display Moscow time, deployed using docker-compose.

## Requirements

- Docker
- Docker Compose

## Role Variables

- `docker_image`: Name of image for deployment. Recommended not to change.
- `container_name`: Name of container to be deployed.
- `external_port`: External port for container.
- `deployment_folder`: Folder to contain docker-compose configuration. Will be created if not exists.

## Example Playbook

```yaml
---
- hosts: all
  become: true
  roles:
    # - docker
    - web_app
```
